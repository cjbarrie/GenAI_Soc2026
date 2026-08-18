"""Worked solution for Session 7.

Read the function in this order: arguments → initial objects → loop/decision
→ return value. The comments name the research meaning of each operation.
"""


def group_summaries(records):
    """Return count, mean, and population variance for every source-by-group combination."""
    grouped = {}
    for record in records:
        key = (record["source"], record["group"])
        grouped.setdefault(key, []).append(record["response"])
    summaries = {}
    for key, values in grouped.items():
        mean = sum(values) / len(values)
        variance = sum((value - mean) ** 2 for value in values) / len(values)
        summaries[key] = {"n": len(values), "mean": mean, "variance": variance}
    return summaries


def run_checks():
    records = [{"source": "human", "group": "A", "response": 1}, {"source": "human", "group": "A", "response": 5}, {"source": "synthetic", "group": "A", "response": 3}, {"source": "synthetic", "group": "A", "response": 3}]
    summary = group_summaries(records)
    assert summary[("human", "A")]["mean"] == 3
    assert summary[("synthetic", "A")]["mean"] == 3
    assert summary[("human", "A")]["variance"] == 4
    assert summary[("synthetic", "A")]["variance"] == 0


if __name__ == "__main__":
    run_checks()
    print("All Session 7 checks passed.")
