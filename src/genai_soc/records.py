"""Transparent research-record helpers used after students learn plain Python."""

from __future__ import annotations

from datetime import datetime, timezone


def require_fields(record: dict, required: list[str]) -> list[str]:
    """Return required field names that are absent or empty."""
    return [name for name in required if record.get(name) in (None, "", [])]


def make_research_record(
    *,
    question: str,
    input_data: object,
    transformation: str,
    raw_output: object,
    configuration: dict,
    validation: dict | None = None,
) -> dict:
    """Collect one inspectable input → transformation → output → check trace."""
    return {
        "question": question,
        "input": input_data,
        "transformation": transformation,
        "raw_output": raw_output,
        "configuration": configuration,
        "validation": validation,
        "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
    }

