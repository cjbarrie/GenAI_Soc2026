import json
from pathlib import Path

from solutions.weekly_coding.session05_solution import run_checks
from src.genai_soc.treatments import review_candidates, summarize_pools


DATA_PATH = (
    Path(__file__).parents[1]
    / "data"
    / "session05"
    / "immigrant_frame_candidates.json"
)


def load_session_data():
    with DATA_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def test_session05_worked_solution():
    run_checks()


def test_rejected_candidates_preserve_every_reason():
    data = load_session_data()
    _, rejected = review_candidates(data["candidates"], data["rules"])

    by_id = {record["candidate_id"]: record for record in rejected}
    assert by_id["rights_02"]["reasons"] == [
        "word count exceeds the limit",
        "contains an unsupported claim",
    ]
    assert by_id["econ_02"]["reasons"] == [
        "intended frame score is too low",
        "competing frame score is too high",
    ]
    assert by_id["family_02"]["reasons"] == [
        "uses stigmatizing terminology",
    ]


def test_accepted_pool_keeps_provenance_and_original_text():
    data = load_session_data()
    accepted, _ = review_candidates(data["candidates"], data["rules"])

    assert len(accepted) == 9
    assert all(candidate["source"] == "cached_course_generation" for candidate in accepted)
    assert all(candidate["prompt_version"] == "v3" for candidate in accepted)
    assert all(candidate["text"] for candidate in accepted)
    assert all(
        candidate["word_count"] == len(candidate["text"].split())
        for candidate in accepted
    )


def test_candidate_screening_does_not_hide_condition_level_differences():
    data = load_session_data()
    accepted, _ = review_candidates(data["candidates"], data["rules"])
    summary = summarize_pools(
        accepted,
        data["rules"]["max_pool_mean_difference"],
    )

    assert summary["conditions"]["economics"] == {
        "count": 3,
        "mean_warmth": 2.1,
        "mean_factual_density": 4.3,
    }
    assert summary["conditions"]["family"] == {
        "count": 3,
        "mean_warmth": 4.4,
        "mean_factual_density": 2.33,
    }
    assert summary["conditions"]["rights"] == {
        "count": 3,
        "mean_warmth": 3.0,
        "mean_factual_density": 2.8,
    }
    assert summary["ready_for_assignment"] is False


def test_dataset_provenance_and_inferential_limit_are_explicit():
    data = load_session_data()
    accepted, _ = review_candidates(data["candidates"], data["rules"])
    summary = summarize_pools(accepted)

    assert "synthetic course materials" in data["study"]["provenance"].lower()
    assert "not evidence" in data["study"]["provenance"].lower()
    assert "not llm judgments" in data["field_provenance"]["intended_frame_competing_frame_warmth_emotionality_factual_density_readability"].lower()
    assert "does not establish construct validity" in summary["limit"]


def test_every_cached_word_count_matches_the_displayed_text():
    data = load_session_data()
    for candidate in data["candidates"]:
        assert candidate["word_count"] == len(candidate["text"].split())
