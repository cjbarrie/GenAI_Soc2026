#!/usr/bin/env python3
"""Instructor-only capped OpenRouter load test; this makes paid live calls."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from openrouter import OpenRouter

ROOT = Path(__file__).resolve().parents[1]
MODEL = json.loads((ROOT / "config/course_models.json").read_text())["hosted"]["model"]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--students", type=int, default=10)
    parser.add_argument("--calls-per-student", type=int, default=2)
    args = parser.parse_args()
    call_count = args.students * args.calls_per_student
    if not 1 <= call_count <= 20:
        raise SystemExit("Refusing to make fewer than 1 or more than 20 calls.")
    key = os.getenv("OPENROUTER_API_KEY")
    if not key:
        raise SystemExit("OPENROUTER_API_KEY is not set. The key was not displayed.")

    messages = [{"role": "user", "content": "Return only the label UNCLEAR."}]
    total_tokens = 0
    with OpenRouter(api_key=key) as client:
        for call_number in range(1, call_count + 1):
            response = client.chat.send(
                model=MODEL,
                messages=messages,
                temperature=0,
                max_tokens=6,
            )
            usage = getattr(response, "usage", None)
            total_tokens += int(getattr(usage, "total_tokens", 0) or 0)
            print(f"Call {call_number}/{call_count}: returned text = {bool(response.choices[0].message.content)}")
    print("Requested model:", MODEL)
    print("Calls completed:", call_count)
    print("Reported total tokens:", total_tokens)
    print("Confirm the corresponding cost, provider resolution and rate-limit record in OpenRouter.")


if __name__ == "__main__":
    main()
