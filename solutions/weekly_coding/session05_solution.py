"""Worked solution for Session 5.

Read the function in this order: arguments → initial objects → loop/decision
→ return value. The comments name the research meaning of each operation.
"""


def construct_treatments(frames, tones, length_by_variant, max_words):
    """Return accepted factorial treatments and rejected condition names."""
    accepted = []
    rejected = []
    for frame in frames:
        for tone in tones:
            condition = f"{frame}_{tone}"
            words = length_by_variant[condition]
            record = {"condition": condition, "frame": frame, "tone": tone, "words": words}
            if words <= max_words:
                accepted.append(record)
            else:
                rejected.append(condition)
    return accepted, rejected


def run_checks():
    lengths = {"gain_neutral": 38, "gain_warm": 44, "loss_neutral": 39, "loss_warm": 61}
    accepted, rejected = construct_treatments(["gain", "loss"], ["neutral", "warm"], lengths, 50)
    assert len(accepted) == 3
    assert rejected == ["loss_warm"]
    assert accepted[0]["condition"] == "gain_neutral"


if __name__ == "__main__":
    run_checks()
    print("All Session 5 checks passed.")
