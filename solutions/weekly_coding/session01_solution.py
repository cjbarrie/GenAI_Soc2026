"""Worked solution for Session 1.

Read the function in this order: arguments → initial objects → loop/decision
→ return value. The comments name the research meaning of each operation.
"""


def build_research_record(prompt, settings, cached_response):
    """Return a nested dictionary that preserves the input, configuration, raw output, and an empty validation field."""
    return {
        "input": {"prompt": prompt, "type": type(prompt).__name__},
        "configuration": settings.copy(),
        "raw_output": cached_response,
        "validation": None,
    }


def run_checks():
    record = build_research_record("Summarize this excerpt", {"temperature": 0}, "A cached summary")
    assert record["input"]["type"] == "str"
    assert record["configuration"]["temperature"] == 0
    assert record["raw_output"] == "A cached summary"
    assert record["validation"] is None


if __name__ == "__main__":
    run_checks()
    print("All Session 1 checks passed.")
