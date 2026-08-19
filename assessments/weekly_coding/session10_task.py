"""Session 10 completion task — Summarize repeated group outcomes and flag a contamination probe that matches the target answer.

Complete means: predict → implement → run checks → interpret → connect to a reading.
This receives a completion mark, not a code-polish score.
"""


def compare_interaction_runs(runs, target_answer):
    """Return structure means, run counts, and IDs whose probe answer already equals the target."""
    # TODO: replace the next line with your small, explicit solution.
    raise NotImplementedError("Complete compare_interaction_runs")


# Before coding, explain the intended algorithm aloud:
# 1. The first dictionary groups outcomes by interaction structure.
# 2. The same loop performs a separate contamination check; it does not remove cases silently.
# 3. The second loop summarizes repeated runs rather than selecting the most impressive trajectory.
# 4. The function returns performance and probe evidence separately so the researcher must interpret both.


def run_checks():
    runs = [{"id": 1, "structure": "debate", "outcome": 8, "probe_answer": "unknown"}, {"id": 2, "structure": "debate", "outcome": 10, "probe_answer": "42"}, {"id": 3, "structure": "solo", "outcome": 6, "probe_answer": "unknown"}]
    summary, contaminated = compare_interaction_runs(runs, "42")
    assert summary["debate"] == {"n": 2, "mean": 9}
    assert summary["solo"]["mean"] == 6
    assert contaminated == [2]


# OPTIONAL EXTENSION (not required for completion):
# Add one small synthetic case designed to trigger the characteristic failure.
# Predict the result before running it, then explain whether the existing output
# makes that failure visible or whether the research record needs another field.


if __name__ == "__main__":
    run_checks()
    print("All checks passed. Now interpret one success or failure.")
