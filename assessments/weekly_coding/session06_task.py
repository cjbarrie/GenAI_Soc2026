"""Session 6 completion task — Convert ordered dialogue turns into a transparent exposure summary.

Complete means: predict → implement → run checks → interpret → connect to a reading.
This receives a completion mark, not a code-polish score.
"""


def summarize_exposure(turns):
    """Count speaker turns and collect the topics actually encountered in order."""
    # TODO: replace the next line with your small, explicit solution.
    raise NotImplementedError("Complete summarize_exposure")


# Before coding, explain the intended algorithm aloud:
# 1. `summary` starts as a state dictionary containing counters and an empty ordered list.
# 2. The loop reads one turn at a time, preserving conversational order.
# 3. The f-string converts `user` into the key `user_turns` and `assistant` into `assistant_turns`.
# 4. The membership check prevents a repeated topic from being counted as a new kind of exposure.


def run_checks():
    turns = [{"role": "user", "text": "What about rent?", "topic": "housing"}, {"role": "assistant", "text": "Here is one policy.", "topic": "housing"}, {"role": "user", "text": "And transit?", "topic": "transit"}]
    summary = summarize_exposure(turns)
    assert summary["user_turns"] == 2
    assert summary["assistant_turns"] == 1
    assert summary["topics"] == ["housing", "transit"]


# OPTIONAL EXTENSION (not required for completion):
# Add one small synthetic case designed to trigger the characteristic failure.
# Predict the result before running it, then explain whether the existing output
# makes that failure visible or whether the research record needs another field.


if __name__ == "__main__":
    run_checks()
    print("All checks passed. Now interpret one success or failure.")
