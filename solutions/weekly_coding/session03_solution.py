"""Commented reference solution for the Session 3 completion task.

The two functions check whether a proposed interpretation has a traceable source
record and enough documented material for human review. They do not decide
whether the interpretation is valid.
"""


REQUIRED_REVIEW_FIELDS = [
    "candidate_theme",
    "supporting_excerpt_ids",
    "counterexample_ids",
    "context_note",
    "alternative_interpretation",
    "researcher_decision",
    "model",
    "access_route",
    "prompt_id",
    "researcher_memo",
]


def trace_sources(excerpts, cited_excerpt_ids):
    """Return source records found for the cited IDs and identify missing IDs."""
    excerpt_by_id = {}

    for excerpt in excerpts:
        excerpt_id = excerpt["excerpt_id"]
        excerpt_by_id[excerpt_id] = excerpt

    found_excerpts = []
    missing_ids = []

    for excerpt_id in cited_excerpt_ids:
        if excerpt_id in excerpt_by_id:
            found_excerpts.append(excerpt_by_id[excerpt_id])
        else:
            missing_ids.append(excerpt_id)

    return {
        "source_traceable": len(missing_ids) == 0,
        "found_excerpts": found_excerpts,
        "missing_ids": missing_ids,
        "warning": "Traceable sources do not by themselves validate an interpretation.",
    }


def check_review_readiness(claim_record, required_fields=REQUIRED_REVIEW_FIELDS):
    """Report whether required interpretive-review fields are present."""
    present_fields = []
    missing_fields = []

    for field_name in required_fields:
        field_value = claim_record.get(field_name)

        if field_value in (None, "", []):
            missing_fields.append(field_name)
        else:
            present_fields.append(field_name)

    return {
        "ready_for_human_review": len(missing_fields) == 0,
        "present_fields": present_fields,
        "missing_fields": missing_fields,
        "warning": "A complete record makes review possible; it does not make the claim valid.",
    }


def run_checks():
    """Run small examples whose results students can inspect by hand."""
    excerpts = [
        {
            "excerpt_id": "T01_B",
            "text": "After several exchanges, I attended the tenants' meeting.",
        },
        {
            "excerpt_id": "T02_A",
            "text": "I accepted help but did not attend political meetings.",
        },
    ]

    trace = trace_sources(excerpts, ["T01_B", "T99_A"])
    assert trace["source_traceable"] is False
    assert trace["missing_ids"] == ["T99_A"]
    assert trace["found_excerpts"][0]["excerpt_id"] == "T01_B"

    incomplete_record = {
        "candidate_theme": "Mutual aid always produces political solidarity.",
        "supporting_excerpt_ids": ["T01_B"],
        "counterexample_ids": [],
    }
    review = check_review_readiness(incomplete_record)
    assert review["ready_for_human_review"] is False
    assert "counterexample_ids" in review["missing_fields"]
    assert "researcher_memo" in review["missing_fields"]


if __name__ == "__main__":
    run_checks()
    print("All checks passed. The interpretation still requires human judgment.")
