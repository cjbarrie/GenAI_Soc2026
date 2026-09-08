#!/usr/bin/env python3
"""Check the two supported model routes without displaying credentials."""

from __future__ import annotations

import argparse
import getpass
import importlib.util
import json
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "course_models.json"
TEST_MESSAGE = "Reply with exactly: ROUTE READY"


def report(ok: bool, label: str, detail: str = "") -> None:
    mark = "PASS" if ok else "FAIL"
    suffix = f" — {detail}" if detail else ""
    print(f"[{mark}] {label}{suffix}")


def installed(package: str) -> bool:
    return importlib.util.find_spec(package) is not None


def model_names(response: object) -> list[str]:
    models = getattr(response, "models", [])
    names: list[str] = []
    for item in models:
        name = getattr(item, "model", None) or getattr(item, "name", None)
        if name:
            names.append(str(name))
    return names


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true", help="Make one short call through each route.")
    args = parser.parse_args()

    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    hosted_model = os.getenv("COURSE_HOSTED_MODEL", config["hosted"]["model"])
    local_model = os.getenv("COURSE_LOCAL_MODEL", config["local"]["model"])

    python_ok = (3, 11) <= sys.version_info[:2] < (3, 13)
    report(python_ok, "Supported Python", sys.version.split()[0])
    print(f"[INFO] Python executable — {sys.executable}")
    print(f"[INFO] Course root — {ROOT}")

    openrouter_ok = installed("openrouter")
    ollama_ok = installed("ollama")
    report(openrouter_ok, "OpenRouter Python SDK installed")
    report(ollama_ok, "Ollama Python SDK installed")
    if not openrouter_ok or not ollama_ok:
        print("[NEXT STEP] From the course repository run: uv sync")

    key_present = bool(os.getenv("OPENROUTER_API_KEY"))
    report(key_present, "OpenRouter key present", "value hidden")
    if not key_present:
        print("[NEXT STEP] You may enter the course key through hidden input in a notebook.")

    local_server_ok = False
    local_model_ok = False
    if ollama_ok:
        try:
            import ollama

            installed_models = model_names(ollama.list())
            local_server_ok = True
            local_model_ok = local_model in installed_models
            report(True, "Ollama server reachable", "localhost only")
            report(local_model_ok, "Course local model installed", local_model)
            if not local_model_ok:
                print(f"[NEXT STEP] In a terminal run: ollama pull {local_model}")
        except Exception as error:
            report(False, "Ollama server reachable", str(error).splitlines()[0])
            print("[NEXT STEP] Start the Ollama application, then run: ollama list")

    if not args.live:
        print("\nRun again with --live after the checks above pass.")
        return

    if openrouter_ok:
        key = os.getenv("OPENROUTER_API_KEY")
        if not key:
            key = getpass.getpass("OpenRouter course key (hidden): ")
        try:
            from openrouter import OpenRouter

            with OpenRouter(api_key=key) as client:
                response = client.chat.send(
                    model=hosted_model,
                    messages=[{"role": "user", "content": TEST_MESSAGE}],
                    temperature=0,
                    max_tokens=12,
                )
            answer = (response.choices[0].message.content or "").strip()
            report(bool(answer), "OpenRouter live call", f"{hosted_model}: {answer}")
        except Exception as error:
            report(False, "OpenRouter live call", str(error).splitlines()[0])
            print(
                "[NEXT STEP] Re-enter the privately supplied course key. If the error "
                "continues, ask the instructor to check that the key is active and funded."
            )

    if ollama_ok and local_server_ok and local_model_ok:
        try:
            import ollama

            response = ollama.chat(
                think=False,
                model=local_model,
                messages=[{"role": "user", "content": TEST_MESSAGE}],
                options={"temperature": 0},
            )
            answer = response.message.content.strip()
            report(bool(answer), "Ollama live call", f"{local_model}: {answer}")
        except Exception as error:
            report(False, "Ollama live call", str(error).splitlines()[0])
            print(
                f"[NEXT STEP] Run: ollama list; then confirm that {local_model} appears."
            )


if __name__ == "__main__":
    main()
