"""Worked solution for Session 7: compare cached response distributions."""


def response_distribution(records, wanted_elicitation):
    """Return proportions for answers 1 through 7 in one elicitation condition."""
    selected = []
    for record in records:
        if record["elicitation"] == wanted_elicitation:
            selected.append(record)

    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
    for record in selected:
        answer = record["response"]
        counts[answer] = counts[answer] + 1

    total = len(selected)
    proportions = {}
    for answer in counts:
        proportions[answer] = counts[answer] / total

    return proportions


def run_checks():
    records = [
        {"elicitation": "forced_choice", "response": 4},
        {"elicitation": "reported_probabilities", "response": 2},
        {"elicitation": "forced_choice", "response": 4},
        {"elicitation": "forced_choice", "response": 5},
    ]
    forced = response_distribution(records, "forced_choice")
    assert abs(sum(forced.values()) - 1.0) < 0.000001
    assert forced[4] == 2 / 3
    assert forced[5] == 1 / 3
    assert forced[1] == 0


if __name__ == "__main__":
    run_checks()
    print("All Session 7 checks passed.")
