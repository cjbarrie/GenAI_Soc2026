"""Run the Week 8 towel-reuse forecast repeatedly across local Ollama models.

This script uses the same prompt, experiment input and JSON schema as the
student workbook. It varies only the local model and random seed. Results are
written after every successful call so an interrupted run can be resumed.
"""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import ollama
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RESULTS_PATH = ROOT / "data/session08/example_outputs/towel_local_model_distribution.json"
CSV_PATH = ROOT / "data/session08/example_outputs/towel_local_model_distribution.csv"
FIGURE_PATH = ROOT / "slides/session08/images/towel_local_model_distribution.png"

MODELS = {
    "Gemma 4 E2B": "gemma4:e2b-it-qat",
    "Llama 3.2 3B": "llama3.2:3b",
    "Falcon 3 7B": "falcon3:7b",
    "DeepSeek R1 8B": "deepseek-r1:8b",
    "Salamandra 7B": "hf.co/mradermacher/salamandra-7b-instruct-2606-GGUF:Q8_0",
}

EXPERIMENT = {
    "context": "Hotel guests staying at least two nights",
    "control": "A sign asks guests to help save the environment by reusing towels.",
    "treatment": "A sign says almost 75% of guests participate in the towel-reuse programme.",
    "outcome": "Percent who reused a towel",
}

SCHEMA = {
    "type": "object",
    "properties": {
        "predicted_control_percent": {"type": "number", "minimum": 0, "maximum": 100},
        "predicted_treatment_percent": {"type": "number", "minimum": 0, "maximum": 100},
    },
    "required": ["predicted_control_percent", "predicted_treatment_percent"],
    "additionalProperties": False,
}

TEMPERATURE = 0.7
HUMAN_CONTROL = 35.1
HUMAN_TREATMENT = 44.1
HUMAN_EFFECT = HUMAN_TREATMENT - HUMAN_CONTROL


def build_messages() -> list[dict[str, str]]:
    prompt = (
        "Forecast the two outcome rates for this randomized experiment in the stated population. "
        "Return percentages from 0 to 100. Do not claim that this replaces human evidence.\n"
        + json.dumps(EXPERIMENT, indent=2)
    )
    return [{"role": "user", "content": prompt}]


def load_existing() -> list[dict]:
    if RESULTS_PATH.exists():
        return json.loads(RESULTS_PATH.read_text())["runs"]
    return []


def save_results(runs: list[dict], repetitions: int) -> None:
    payload = {
        "run_date": str(date.today()),
        "experiment_id": "towels",
        "temperature": TEMPERATURE,
        "repetitions_requested_per_model": repetitions,
        "human_control_percent": HUMAN_CONTROL,
        "human_treatment_percent": HUMAN_TREATMENT,
        "human_effect_points": HUMAN_EFFECT,
        "model_input": EXPERIMENT,
        "prompt": build_messages()[0]["content"],
        "schema": SCHEMA,
        "models": MODELS,
        "runs": runs,
    }
    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(payload, indent=2) + "\n")
    pd.DataFrame(runs).to_csv(CSV_PATH, index=False)


def run_models(repetitions: int) -> list[dict]:
    runs = load_existing()
    completed = {(row["model"], row["seed"]) for row in runs}
    messages = build_messages()

    for label, model in MODELS.items():
        print(f"\n{label} ({model})")
        for repetition in range(repetitions):
            seed = 20261000 + repetition
            if (model, seed) in completed:
                print(f"  seed {seed}: already saved")
                continue

            response = ollama.chat(
                model=model,
                messages=messages,
                format=SCHEMA,
                think=False,
                options={"temperature": TEMPERATURE, "seed": seed},
                keep_alive="15m",
            )
            raw = response.message.content
            parsed = json.loads(raw)
            control = float(parsed["predicted_control_percent"])
            treatment = float(parsed["predicted_treatment_percent"])
            if not (0 <= control <= 100 and 0 <= treatment <= 100):
                raise ValueError(f"Out-of-range return from {model}: {raw}")
            effect = treatment - control
            row = {
                "model_label": label,
                "model": model,
                "seed": seed,
                "temperature": TEMPERATURE,
                "predicted_control_percent": control,
                "predicted_treatment_percent": treatment,
                "predicted_effect_points": effect,
                "absolute_error_points": abs(effect - HUMAN_EFFECT),
                "raw_return": raw,
            }
            runs.append(row)
            completed.add((model, seed))
            save_results(runs, repetitions)
            print(f"  seed {seed}: control {control:g}, treatment {treatment:g}, effect {effect:+g}")
    return runs


def make_figure(runs: list[dict]) -> None:
    frame = pd.DataFrame(runs)
    order = list(MODELS)
    colors = ["#2457a6", "#6e1f3b", "#d5573b", "#4f7d65", "#7b6aa2"]

    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 12,
        "axes.titlesize": 17,
        "axes.labelsize": 13,
    })
    fig, ax = plt.subplots(figsize=(12.5, 6.5), facecolor="#f7f5ef")
    ax.set_facecolor("#f7f5ef")

    values = [frame.loc[frame["model_label"] == label, "predicted_effect_points"].to_numpy() for label in order]
    positions = np.arange(1, len(order) + 1)
    box = ax.boxplot(
        values,
        positions=positions,
        widths=0.52,
        patch_artist=True,
        showfliers=False,
        medianprops={"color": "#1f2326", "linewidth": 2.2},
        whiskerprops={"color": "#666666", "linewidth": 1.3},
        capprops={"color": "#666666", "linewidth": 1.3},
        boxprops={"linewidth": 1.4},
    )
    for patch, color in zip(box["boxes"], colors, strict=True):
        patch.set_facecolor(color)
        patch.set_alpha(0.22)
        patch.set_edgecolor(color)

    for position, label, color in zip(positions, order, colors, strict=True):
        subset = frame.loc[frame["model_label"] == label].sort_values("seed")
        jitter = np.linspace(-0.17, 0.17, len(subset))
        ax.scatter(
            position + jitter,
            subset["predicted_effect_points"],
            s=46,
            color=color,
            edgecolor="white",
            linewidth=0.7,
            alpha=0.9,
            zorder=3,
        )

    ax.axhline(HUMAN_EFFECT, color="#111111", linewidth=2.2, linestyle=(0, (6, 4)))
    ax.text(5.36, HUMAN_EFFECT + 1.5, "Human experiment: +9 points", va="bottom", ha="right", fontsize=11.5,
            backgroundcolor="#f7f5ef")
    ax.axhline(0, color="#9a968e", linewidth=1)
    ax.set_xticks(positions, order)
    ax.set_ylabel("Predicted treatment effect (percentage points)")
    ax.grid(axis="y", color="#d8d3c8", linewidth=0.8)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.margins(x=0.06)
    fig.tight_layout()
    FIGURE_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURE_PATH, dpi=180, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repetitions", type=int, default=15)
    parser.add_argument("--plot-only", action="store_true")
    args = parser.parse_args()

    runs = load_existing() if args.plot_only else run_models(args.repetitions)
    make_figure(runs)
    frame = pd.DataFrame(runs)
    summary = frame.groupby("model_label")["predicted_effect_points"].agg(["count", "median", "min", "max"])
    print("\n", summary.to_string())
    print(f"\nHuman effect: {HUMAN_EFFECT:g} points")
    print(f"Saved {RESULTS_PATH}")
    print(f"Saved {CSV_PATH}")
    print(f"Saved {FIGURE_PATH}")


if __name__ == "__main__":
    main()
