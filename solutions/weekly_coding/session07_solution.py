"""Checks for the Week 7 persona and elicitation comparison."""


def validate_probabilities(probabilities):
    """Check that seven numeric probabilities lie in range and sum to one."""
    return (
        len(probabilities) == 7
        and all(isinstance(value, (int, float)) for value in probabilities)
        and all(0 <= value <= 1 for value in probabilities)
        and abs(sum(probabilities) - 1.0) < 0.000001
    )


def expected_score(probabilities):
    """Return the expected value of a probability distribution over 1–7."""
    if not validate_probabilities(probabilities):
        raise ValueError("Expected seven probabilities between 0 and 1 that sum to one")
    return sum((index + 1) * probability for index, probability in enumerate(probabilities))


def run_checks():
    sparse = [0.05, 0.10, 0.15, 0.30, 0.20, 0.15, 0.05]
    rich = [0.08, 0.16, 0.22, 0.24, 0.16, 0.09, 0.05]

    assert validate_probabilities(sparse)
    assert validate_probabilities(rich)
    assert abs(expected_score(sparse) - 4.15) < 0.000001
    assert abs(expected_score(rich) - 3.71) < 0.000001
    assert not validate_probabilities([0.5, 0.5])


if __name__ == "__main__":
    run_checks()
    print("All Week 7 checks passed.")
