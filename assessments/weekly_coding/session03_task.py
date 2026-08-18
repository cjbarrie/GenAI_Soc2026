"""Session 3 completion task — Link proposed qualitative themes to exact supporting excerpts and reject unsupported labels.

Complete means: predict → implement → run checks → interpret → connect to a reading.
This receives a completion mark, not a code-polish score.
"""


def link_themes_to_evidence(excerpts, proposals):
    """Return accepted theme records and a list of rejected proposal IDs."""
    # TODO: replace the next line with your small, explicit solution.
    raise NotImplementedError("Complete link_themes_to_evidence")


# Before coding, explain the intended algorithm aloud:
# 1. The first dictionary comprehension builds a lookup: excerpt ID → full source text.
# 2. The loop considers one proposed interpretation at a time.
# 3. The `if` branch rejects missing excerpts, empty quotations, and quotations not found verbatim in the source.
# 4. The output separates auditable proposals from records that require human review.


def run_checks():
    excerpts = [{"id": 1, "text": "Neighbors shared childcare when shifts changed."}, {"id": 2, "text": "I stopped attending after the fee increased."}]
    proposals = [{"excerpt_id": 1, "theme": "mutual aid", "quote": "shared childcare"}, {"excerpt_id": 2, "theme": "trust", "quote": "everyone trusted staff"}]
    accepted, rejected = link_themes_to_evidence(excerpts, proposals)
    assert accepted[0]["theme"] == "mutual aid"
    assert accepted[0]["quote"] == "shared childcare"
    assert rejected == [2]


if __name__ == "__main__":
    run_checks()
    print("All checks passed. Now interpret one success or failure.")
