"""Session 13 completion task — Create factorial audit conditions and summarize the observed response by condition.

Complete means: predict → implement → run checks → interpret → connect to a reading.
This receives a completion mark, not a code-polish score.
"""


def factorial_audit(models, languages, frames, responses):
    """Return every requested condition with its observed response and report missing conditions."""
    # TODO: replace the next line with your small, explicit solution.
    raise NotImplementedError("Complete factorial_audit")


# Before coding, explain the intended algorithm aloud:
# 1. Three nested loops construct the Cartesian product one factor at a time.
# 2. A tuple is the exact key for one model-language-frame condition.
# 3. The membership check distinguishes an unobserved condition from a response value of zero.
# 4. The outputs describe what was observed and what is missing; neither output supplies a causal explanation.


def run_checks():
    responses = {("m1", "en", "neutral"): 2, ("m1", "es", "neutral"): 3}
    conditions, missing = factorial_audit(["m1"], ["en", "es"], ["neutral"], responses)
    assert len(conditions) == 2
    assert conditions[1]["language"] == "es"
    assert missing == []
    _, missing_two = factorial_audit(["m1"], ["en"], ["neutral", "student"], responses)
    assert missing_two == [("m1", "en", "student")]


# OPTIONAL EXTENSION (not required for completion):
# Add one small synthetic case designed to trigger the characteristic failure.
# Predict the result before running it, then explain whether the existing output
# makes that failure visible or whether the research record needs another field.


if __name__ == "__main__":
    run_checks()
    print("All checks passed. Now interpret one success or failure.")
