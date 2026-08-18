"""Worked solution for Session 10.

Read the function in this order: arguments → initial objects → loop/decision
→ return value. The comments name the research meaning of each operation.
"""


def compare_interaction_runs(runs, target_answer):
    """Return structure means, run counts, and IDs whose probe answer already equals the target."""
    values_by_structure = {}
    contaminated = []
    for run in runs:
        values_by_structure.setdefault(run["structure"], []).append(run["outcome"])
        if run.get("probe_answer") == target_answer:
            contaminated.append(run["id"])
    summary = {}
    for structure, values in values_by_structure.items():
        summary[structure] = {"n": len(values), "mean": sum(values) / len(values)}
    return summary, contaminated


def run_checks():
    runs = [{"id": 1, "structure": "debate", "outcome": 8, "probe_answer": "unknown"}, {"id": 2, "structure": "debate", "outcome": 10, "probe_answer": "42"}, {"id": 3, "structure": "solo", "outcome": 6, "probe_answer": "unknown"}]
    summary, contaminated = compare_interaction_runs(runs, "42")
    assert summary["debate"] == {"n": 2, "mean": 9}
    assert summary["solo"]["mean"] == 6
    assert contaminated == [2]


if __name__ == "__main__":
    run_checks()
    print("All Session 10 checks passed.")
