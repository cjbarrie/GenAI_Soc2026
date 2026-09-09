import json
from pathlib import Path

from solutions.weekly_coding.session03_solution import (
    REQUIRED_REVIEW_FIELDS,
    check_review_readiness,
    run_checks,
    trace_sources,
)


DATA_PATH = (
    Path(__file__).parents[1]
    / "data"
    / "session03"
    / "mutual_aid_interviews.json"
)


def load_session_data():
    with DATA_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def test_session03_worked_examples():
    run_checks()


def test_all_candidate_source_ids_are_traceable():
    data = load_session_data()
    candidate = data["candidate_model_proposal"]

    result = trace_sources(data["excerpts"], candidate["supporting_excerpt_ids"])

    assert result["source_traceable"] is True
    assert result["missing_ids"] == []
    assert [item["excerpt_id"] for item in result["found_excerpts"]] == [
        "T01_B",
        "T04_A",
        "T06_A",
    ]


def test_missing_source_id_is_reported_without_becoming_a_validity_claim():
    data = load_session_data()

    result = trace_sources(data["excerpts"], ["T01_B", "T99_A"])

    assert result["source_traceable"] is False
    assert result["missing_ids"] == ["T99_A"]
    assert "validate an interpretation" in result["warning"]


def test_revised_claim_record_is_complete_for_human_review():
    data = load_session_data()

    result = check_review_readiness(data["revised_claim_record"])

    assert result["ready_for_human_review"] is True
    assert result["missing_fields"] == []
    assert result["present_fields"] == REQUIRED_REVIEW_FIELDS
    assert "does not make the claim valid" in result["warning"]


def test_empty_counterexample_list_counts_as_missing_review_work():
    data = load_session_data()
    incomplete = dict(data["revised_claim_record"])
    incomplete["counterexample_ids"] = []

    result = check_review_readiness(incomplete)

    assert result["ready_for_human_review"] is False
    assert result["missing_fields"] == ["counterexample_ids"]


def test_dataset_marks_ai_moderated_excerpt_and_synthetic_provenance():
    data = load_session_data()
    ai_excerpts = [
        item for item in data["excerpts"] if item["interview_mode"] == "ai_moderated_text"
    ]

    assert len(ai_excerpts) == 1
    assert "generated follow-up" in ai_excerpts[0]["context"]
    assert "synthetic" in data["study"]["provenance"].lower()
