"""Session 12 completion task — Produce a discrepancy report from cached and rerun configurations.

Complete means: predict → implement → run checks → interpret → connect to a reading.
This receives a completion mark, not a code-polish score.
"""


def compare_replication_records(original, rerun):
    """Return changed configuration fields, whether output changed, and an interpretable dependence label."""
    # TODO: replace the next line with your small, explicit solution.
    raise NotImplementedError("Complete compare_replication_records")


# Before coding, explain the intended algorithm aloud:
# 1. `fields` declares in advance which configuration elements will be compared.
# 2. The list comprehension retains only fields whose values differ across the two dictionaries.
# 3. Output difference is calculated separately from configuration difference.
# 4. The final condition labels visible workflow dependence before invoking unexplained stochasticity.


def run_checks():
    original = {"model": "m1", "provider": "p1", "prompt": "Q", "temperature": 0, "date": "2025", "output": "A"}
    same = compare_replication_records(original, original.copy())
    rerun = {**original, "model": "m2", "date": "2026", "output": "B"}
    changed = compare_replication_records(original, rerun)
    assert same["label"] == "same recorded output"
    assert changed["changed_fields"] == ["model", "date"]
    assert changed["label"] == "workflow dependence"


if __name__ == "__main__":
    run_checks()
    print("All checks passed. Now interpret one success or failure.")
