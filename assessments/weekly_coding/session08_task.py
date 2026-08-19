"""Session 8 completion task — Calculate three target-specific errors from matched human and synthetic records.

Complete means: predict → implement → run checks → interpret → connect to a reading.
This receives a completion mark, not a code-polish score.
"""


def score_inferential_targets(records):
    """Return individual MAE, aggregate mean error, and absolute error in the A–B group gap."""
    # TODO: replace the next line with your small, explicit solution.
    raise NotImplementedError("Complete score_inferential_targets")


# Before coding, explain the intended algorithm aloud:
# 1. The first list contains one absolute individual error per matched record.
# 2. Two means are computed across the whole dataset for the aggregate target.
# 3. The nested loops compute separate source-by-group means before constructing each group gap.
# 4. The returned dictionary prevents one score from silently standing in for all inferential targets.


def run_checks():
    records = [{"group": "A", "human": 5, "synthetic": 3}, {"group": "A", "human": 1, "synthetic": 3}, {"group": "B", "human": 2, "synthetic": 2}, {"group": "B", "human": 2, "synthetic": 2}]
    scores = score_inferential_targets(records)
    assert scores["individual_mae"] == 1
    assert scores["aggregate_error"] == 0
    assert scores["group_gap_error"] == 0


# OPTIONAL EXTENSION (not required for completion):
# Add one small synthetic case designed to trigger the characteristic failure.
# Predict the result before running it, then explain whether the existing output
# makes that failure visible or whether the research record needs another field.


if __name__ == "__main__":
    run_checks()
    print("All checks passed. Now interpret one success or failure.")
