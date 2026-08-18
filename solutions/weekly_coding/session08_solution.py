"""Worked solution for Session 8.

Read the function in this order: arguments → initial objects → loop/decision
→ return value. The comments name the research meaning of each operation.
"""


def score_inferential_targets(records):
    """Return individual MAE, aggregate mean error, and absolute error in the A–B group gap."""
    individual_errors = [abs(row["human"] - row["synthetic"]) for row in records]
    individual_mae = sum(individual_errors) / len(individual_errors)
    human_mean = sum(row["human"] for row in records) / len(records)
    synthetic_mean = sum(row["synthetic"] for row in records) / len(records)
    means = {}
    for source in ("human", "synthetic"):
        for group in ("A", "B"):
            values = [row[source] for row in records if row["group"] == group]
            means[(source, group)] = sum(values) / len(values)
    human_gap = means[("human", "A")] - means[("human", "B")]
    synthetic_gap = means[("synthetic", "A")] - means[("synthetic", "B")]
    return {"individual_mae": individual_mae, "aggregate_error": abs(human_mean - synthetic_mean), "group_gap_error": abs(human_gap - synthetic_gap)}


def run_checks():
    records = [{"group": "A", "human": 5, "synthetic": 3}, {"group": "A", "human": 1, "synthetic": 3}, {"group": "B", "human": 2, "synthetic": 2}, {"group": "B", "human": 2, "synthetic": 2}]
    scores = score_inferential_targets(records)
    assert scores["individual_mae"] == 1
    assert scores["aggregate_error"] == 0
    assert scores["group_gap_error"] == 0


if __name__ == "__main__":
    run_checks()
    print("All Session 8 checks passed.")
