#!/usr/bin/env python3
"""Run four bounded checks against the exact configured Ollama course model."""

from __future__ import annotations

import json
from pathlib import Path

import ollama


ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / "config" / "course_models.json").read_text())
MODEL = CONFIG["local"]["model"]


def mark(name: str, answer: str) -> None:
    if not answer.strip():
        raise RuntimeError(f"{name} returned empty text")
    print(f"[PASS] {name} — {len(answer)} characters returned")


def main() -> None:
    print("Model:", MODEL)

    text_response = ollama.chat(
        think=False,
        model=MODEL,
        messages=[{"role": "user", "content": "Reply with exactly: LOCAL TEXT READY"}],
        options={"temperature": 0, "num_predict": 20},
    )
    mark("plain-text call", text_response.message.content)

    schema = {
        "type": "object",
        "properties": {
            "label": {"type": "string", "enum": ["SUPPORT", "OPPOSE", "UNCLEAR"]}
        },
        "required": ["label"],
        "additionalProperties": False,
    }
    structured_response = ollama.chat(
        think=False,
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": (
                    "Label this conditional comment and return JSON: "
                    "I support the plan if rents remain affordable."
                ),
            }
        ],
        format=schema,
        options={"temperature": 0, "num_predict": 40},
    )
    parsed = json.loads(structured_response.message.content)
    if parsed["label"] not in schema["properties"]["label"]["enum"]:
        raise RuntimeError("structured call returned a label outside the schema")
    mark("JSON-schema call", structured_response.message.content)

    conversation_response = ollama.chat(
        think=False,
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "Ask one short, non-leading follow-up about a concrete episode.",
            },
            {
                "role": "user",
                "content": "Participant: I spoke after the professor invited me to respond.",
            },
        ],
        options={"temperature": 0, "num_predict": 50},
    )
    mark("conversation call", conversation_response.message.content)

    frame_1 = ROOT / "slides" / "session04" / "images" / "zidane_fine2_168.png"
    frame_2 = ROOT / "slides" / "session04" / "images" / "zidane_fine2_169.png"
    for frame in (frame_1, frame_2):
        if not frame.exists():
            raise FileNotFoundError(f"Missing Week 4 image: {frame}")
    image_response = ollama.chat(
        think=False,
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": "State one directly visible difference between these ordered frames.",
                "images": [str(frame_1), str(frame_2)],
            }
        ],
        options={"temperature": 0, "num_predict": 60},
    )
    mark("multimodal call", image_response.message.content)


if __name__ == "__main__":
    main()
