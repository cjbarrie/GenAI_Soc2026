"""Session 5 completion task — Construct factorial treatment records and filter variants that violate a fidelity bound.

Complete means: predict → implement → run checks → interpret → connect to a reading.
This receives a completion mark, not a code-polish score.
"""


def construct_treatments(frames, tones, length_by_variant, max_words):
    """Return accepted factorial treatments and rejected condition names."""
    # TODO: replace the next line with your small, explicit solution.
    raise NotImplementedError("Complete construct_treatments")


# Before coding, explain the intended algorithm aloud:
# 1. The outer loop chooses one frame; the inner loop pairs it with every tone.
# 2. The f-string creates a stable condition name used to retrieve its word count.
# 3. Each dictionary is one treatment record, not the treatment text itself.
# 4. The conditional applies the rule declared before looking at outcomes.


def run_checks():
    lengths = {"gain_neutral": 38, "gain_warm": 44, "loss_neutral": 39, "loss_warm": 61}
    accepted, rejected = construct_treatments(["gain", "loss"], ["neutral", "warm"], lengths, 50)
    assert len(accepted) == 3
    assert rejected == ["loss_warm"]
    assert accepted[0]["condition"] == "gain_neutral"


if __name__ == "__main__":
    run_checks()
    print("All checks passed. Now interpret one success or failure.")
