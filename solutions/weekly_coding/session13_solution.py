"""Worked solution for Session 13.

Read the function in this order: arguments → initial objects → loop/decision
→ return value. The comments name the research meaning of each operation.
"""


def factorial_audit(models, languages, frames, responses):
    """Return every requested condition with its observed response and report missing conditions."""
    conditions = []
    missing = []
    for model in models:
        for language in languages:
            for frame in frames:
                key = (model, language, frame)
                if key in responses:
                    conditions.append({"model": model, "language": language, "frame": frame, "response": responses[key]})
                else:
                    missing.append(key)
    return conditions, missing


def run_checks():
    responses = {("m1", "en", "neutral"): 2, ("m1", "es", "neutral"): 3}
    conditions, missing = factorial_audit(["m1"], ["en", "es"], ["neutral"], responses)
    assert len(conditions) == 2
    assert conditions[1]["language"] == "es"
    assert missing == []
    _, missing_two = factorial_audit(["m1"], ["en"], ["neutral", "student"], responses)
    assert missing_two == [("m1", "en", "student")]


if __name__ == "__main__":
    run_checks()
    print("All Session 13 checks passed.")
