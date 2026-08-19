"""Session 7 completion task — Calculate group means and population variances for human and synthetic records.

Complete means: predict → implement → run checks → interpret → connect to a reading.
This receives a completion mark, not a code-polish score.
"""


def group_summaries(records):
    """Return count, mean, and population variance for every source-by-group combination."""
    # TODO: replace the next line with your small, explicit solution.
    raise NotImplementedError("Complete group_summaries")


# Before coding, explain the intended algorithm aloud:
# 1. A tuple `(source, group)` is used as one dictionary key so the two dimensions stay together.
# 2. `setdefault` creates an empty list the first time a key appears, then every response is appended.
# 3. The second loop summarizes each list only after grouping is complete.
# 4. Equal means beside unequal variances make flattening visible.


def run_checks():
    records = [{"source": "human", "group": "A", "response": 1}, {"source": "human", "group": "A", "response": 5}, {"source": "synthetic", "group": "A", "response": 3}, {"source": "synthetic", "group": "A", "response": 3}]
    summary = group_summaries(records)
    assert summary[("human", "A")]["mean"] == 3
    assert summary[("synthetic", "A")]["mean"] == 3
    assert summary[("human", "A")]["variance"] == 4
    assert summary[("synthetic", "A")]["variance"] == 0


# OPTIONAL EXTENSION (not required for completion):
# Add one small synthetic case designed to trigger the characteristic failure.
# Predict the result before running it, then explain whether the existing output
# makes that failure visible or whether the research record needs another field.


if __name__ == "__main__":
    run_checks()
    print("All checks passed. Now interpret one success or failure.")
