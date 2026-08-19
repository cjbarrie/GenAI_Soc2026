"""Session 1 completion task — Build one complete research record from a prompt, settings, and cached response.

Complete means: predict → implement → run checks → interpret → connect to a reading.
This receives a completion mark, not a code-polish score.
"""


def build_research_record(prompt, settings, cached_response):
    """Return a nested dictionary that preserves the input, configuration, raw output, and an empty validation field."""
    # TODO: replace the next line with your small, explicit solution.
    raise NotImplementedError("Complete build_research_record")


# Before coding, explain the intended algorithm aloud:
# 1. The three arguments are existing Python objects: two strings and one dictionary.
# 2. `settings.copy()` makes a new dictionary so later edits do not silently alter the saved record.
# 3. The returned dictionary nests related fields under names a researcher can inspect.
# 4. `None` means validation has not happened; it does not mean the output is valid.


def run_checks():
    record = build_research_record("Summarize this excerpt", {"temperature": 0}, "A cached summary")
    assert record["input"]["type"] == "str"
    assert record["configuration"]["temperature"] == 0
    assert record["raw_output"] == "A cached summary"
    assert record["validation"] is None


# OPTIONAL EXTENSION (not required for completion):
# Add one small synthetic case designed to trigger the characteristic failure.
# Predict the result before running it, then explain whether the existing output
# makes that failure visible or whether the research record needs another field.


if __name__ == "__main__":
    run_checks()
    print("All checks passed. Now interpret one success or failure.")
