"""Offline checks for the optional Week 12 JSON-record extension."""

import json
from pathlib import Path
from tempfile import TemporaryDirectory


REQUIRED_FIELDS = [
    "research_question",
    "input_description",
    "model_route",
    "model_name",
    "prompt_version",
    "temperature",
    "expected_output",
    "validation_evidence",
]


def missing_fields(record):
    missing = []
    for field in REQUIRED_FIELDS:
        if field not in record:
            missing.append(field)
    return missing


def run_checks():
    record = {field: "example" for field in REQUIRED_FIELDS}
    record["temperature"] = 0
    assert missing_fields(record) == []

    incomplete = record.copy()
    del incomplete["validation_evidence"]
    assert missing_fields(incomplete) == ["validation_evidence"]

    with TemporaryDirectory() as temporary_directory:
        path = Path(temporary_directory) / "record.json"
        path.write_text(json.dumps(record, indent=2), encoding="utf-8")
        reopened = json.loads(path.read_text(encoding="utf-8"))
    assert reopened == record


if __name__ == "__main__":
    run_checks()
    print("All Session 12 checks passed.")
