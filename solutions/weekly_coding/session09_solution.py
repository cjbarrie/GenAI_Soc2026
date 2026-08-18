"""Worked solution for Session 9.

Read the function in this order: arguments → initial objects → loop/decision
→ return value. The comments name the research meaning of each operation.
"""


def synchronous_update(states, neighbors, threshold):
    """Return a new state dictionary; adopt 1 when the prior-state neighbor mean reaches the threshold."""
    next_states = states.copy()
    for agent, neighbor_ids in neighbors.items():
        neighbor_values = [states[neighbor] for neighbor in neighbor_ids]
        neighbor_mean = sum(neighbor_values) / len(neighbor_values)
        next_states[agent] = 1 if neighbor_mean >= threshold else 0
    return next_states


def run_checks():
    states = {"a": 0, "b": 1, "c": 1}
    neighbors = {"a": ["b", "c"], "b": ["a", "c"], "c": ["a", "b"]}
    updated = synchronous_update(states, neighbors, 0.5)
    assert updated == {"a": 1, "b": 1, "c": 1}
    assert states == {"a": 0, "b": 1, "c": 1}
    assert updated is not states


if __name__ == "__main__":
    run_checks()
    print("All Session 9 checks passed.")
