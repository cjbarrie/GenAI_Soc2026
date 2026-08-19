"""Session 9 completion task — Write and test one synchronous threshold-update step for a small network.

Complete means: predict → implement → run checks → interpret → connect to a reading.
This receives a completion mark, not a code-polish score.
"""


def synchronous_update(states, neighbors, threshold):
    """Return a new state dictionary; adopt 1 when the prior-state neighbor mean reaches the threshold."""
    # TODO: replace the next line with your small, explicit solution.
    raise NotImplementedError("Complete synchronous_update")


# Before coding, explain the intended algorithm aloud:
# 1. `states.copy()` creates the future state without changing the prior state.
# 2. The loop visits each agent and retrieves the IDs of its neighbors.
# 3. The list comprehension looks every neighbor up in the old `states` dictionary.
# 4. Only after computing from prior state does the function assign the agent's next value.


def run_checks():
    states = {"a": 0, "b": 1, "c": 1}
    neighbors = {"a": ["b", "c"], "b": ["a", "c"], "c": ["a", "b"]}
    updated = synchronous_update(states, neighbors, 0.5)
    assert updated == {"a": 1, "b": 1, "c": 1}
    assert states == {"a": 0, "b": 1, "c": 1}
    assert updated is not states


# OPTIONAL EXTENSION (not required for completion):
# Add one small synthetic case designed to trigger the characteristic failure.
# Predict the result before running it, then explain whether the existing output
# makes that failure visible or whether the research record needs another field.


if __name__ == "__main__":
    run_checks()
    print("All checks passed. Now interpret one success or failure.")
