"""Worked solution for Session 6.

Read the function in this order: arguments → initial objects → loop/decision
→ return value. The comments name the research meaning of each operation.
"""


def summarize_exposure(turns):
    """Count speaker turns and collect the topics actually encountered in order."""
    summary = {"user_turns": 0, "assistant_turns": 0, "topics": []}
    for turn in turns:
        role_key = f"{turn['role']}_turns"
        summary[role_key] += 1
        topic = turn.get("topic")
        if topic and topic not in summary["topics"]:
            summary["topics"].append(topic)
    return summary


def run_checks():
    turns = [{"role": "user", "text": "What about rent?", "topic": "housing"}, {"role": "assistant", "text": "Here is one policy.", "topic": "housing"}, {"role": "user", "text": "And transit?", "topic": "transit"}]
    summary = summarize_exposure(turns)
    assert summary["user_turns"] == 2
    assert summary["assistant_turns"] == 1
    assert summary["topics"] == ["housing", "transit"]


if __name__ == "__main__":
    run_checks()
    print("All Session 6 checks passed.")
