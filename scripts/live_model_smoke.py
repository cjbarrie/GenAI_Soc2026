#!/usr/bin/env python3
"""Instructor-only, low-cost smoke test for the two configured live routes."""

from __future__ import annotations

import json
import os
from pathlib import Path

import ollama
from openrouter import OpenRouter


ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / "config" / "course_models.json").read_text())


def main() -> None:
    key = os.getenv("OPENROUTER_API_KEY")
    if not key:
        raise SystemExit("OPENROUTER_API_KEY is not set. The key was not displayed.")

    messages = [{"role": "user", "content": "Reply with exactly: course smoke test"}]
    with OpenRouter(api_key=key) as client:
        hosted = client.chat.send(
            model=CONFIG["hosted"]["model"],
            messages=messages,
            temperature=0,
            max_tokens=8,
        )
    local = ollama.chat(
        model=CONFIG["local"]["model"],
        messages=messages,
        options={"temperature": 0, "num_predict": 8},
    )
    print("OpenRouter returned text:", bool(hosted.choices[0].message.content))
    print("Ollama returned text:", bool(local.message.content))


if __name__ == "__main__":
    main()
