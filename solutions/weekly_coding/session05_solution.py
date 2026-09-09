"""Commented reference solution for the Session 5 completion task.

The functions preserve candidate-level decisions and compare retained pools.
They do not establish that either theoretical frame is valid.
"""

import json
from pathlib import Path

DATA_PATH = (
    Path(__file__).parents[2]
    / "data"
    / "session05"
    / "immigrant_frame_candidates.json"
)


def review_candidates(candidates, rules):
    """Return accepted candidates and rejected records with every failed rule."""
    accepted = []
    rejected = []

    for candidate in candidates:
        word_count = (
            len(candidate["text"].split())
            if "text" in candidate
            else candidate["word_count"]
        )
        reviewed_candidate = dict(candidate)
        reviewed_candidate["word_count"] = word_count
        reasons = []

        if candidate["intended_frame_score"] < rules["min_intended_frame_score"]:
            reasons.append("intended frame score is too low")
        if candidate["competing_frame_score"] > rules["max_competing_frame_score"]:
            reasons.append("competing frame score is too high")
        if word_count > rules["max_word_count"]:
            reasons.append("word count exceeds the limit")
        if candidate["unsupported_claim"] and not rules["allow_unsupported_claim"]:
            reasons.append("contains an unsupported claim")
        if candidate["stigmatizing_language"] and not rules["allow_stigmatizing_language"]:
            reasons.append("uses stigmatizing terminology")

        if reasons:
            rejected.append(
                {
                    "candidate_id": candidate["candidate_id"],
                    "condition": candidate["condition"],
                    "reasons": reasons,
                }
            )
        else:
            accepted.append(reviewed_candidate)

    return accepted, rejected


def summarize_pools(accepted, max_mean_difference=1.0):
    """Compare retained conditions on warmth and factual-density ratings."""
    conditions = sorted({candidate["condition"] for candidate in accepted})
    summaries = {}

    for condition in conditions:
        pool = [candidate for candidate in accepted if candidate["condition"] == condition]
        summaries[condition] = {
            "count": len(pool),
            "mean_warmth": round(
                sum(candidate["warmth_score"] for candidate in pool) / len(pool), 2
            ),
            "mean_factual_density": round(
                sum(candidate["factual_density_score"] for candidate in pool) / len(pool),
                2,
            ),
        }

    warnings = []
    if len(conditions) >= 2:
        warmth_values = [summaries[name]["mean_warmth"] for name in conditions]
        factual_values = [summaries[name]["mean_factual_density"] for name in conditions]
        if max(warmth_values) - min(warmth_values) > max_mean_difference:
            warnings.append("retained pools still differ in mean warmth")
        if max(factual_values) - min(factual_values) > max_mean_difference:
            warnings.append("retained pools still differ in mean factual density")

    return {
        "conditions": summaries,
        "warnings": warnings,
        "ready_for_assignment": len(warnings) == 0,
        "limit": "A pool summary does not establish construct validity.",
    }


def load_course_example():
    """Load the cached synthetic candidate pool and predeclared rules."""
    with DATA_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def run_checks():
    """Run checks whose expected values can be inspected by hand."""
    example = load_course_example()
    accepted, rejected = review_candidates(example["candidates"], example["rules"])
    summary = summarize_pools(
        accepted,
        example["rules"]["max_pool_mean_difference"],
    )

    assert [candidate["candidate_id"] for candidate in accepted] == [
        "rights_01",
        "rights_03",
        "rights_04",
        "econ_01",
        "econ_03",
        "econ_04",
        "family_01",
        "family_03",
        "family_04",
    ]
    assert rejected[0] == {
        "candidate_id": "rights_02",
        "condition": "rights",
        "reasons": [
            "word count exceeds the limit",
            "contains an unsupported claim",
        ],
    }
    assert summary["conditions"]["rights"]["count"] == 3
    assert summary["conditions"]["family"]["mean_warmth"] == 4.4
    assert "retained pools still differ in mean warmth" in summary["warnings"]
    assert summary["ready_for_assignment"] is False
    assert "does not establish construct validity" in summary["limit"]


if __name__ == "__main__":
    run_checks()
    print("All Session 5 checks passed. The retained pools still require review.")
