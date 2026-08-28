"""Transparent review helpers for Session 5 synthetic treatment candidates."""


def review_candidates(candidates, rules):
    """Return accepted candidates and rejected records with every failed rule."""
    accepted = []
    rejected = []

    for candidate in candidates:
        # Full course records contain the displayed text, so Python calculates
        # the count from that text. The short completion task supplies a cached
        # count because it omits the full messages.
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
    """Compare retained conditions on two nuisance ratings."""
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
        factual_values = [
            summaries[name]["mean_factual_density"] for name in conditions
        ]
        warmth_difference = max(warmth_values) - min(warmth_values)
        factual_difference = max(factual_values) - min(factual_values)

        if warmth_difference > max_mean_difference:
            warnings.append("retained pools still differ in mean warmth")
        if factual_difference > max_mean_difference:
            warnings.append("retained pools still differ in mean factual density")

    return {
        "conditions": summaries,
        "warnings": warnings,
        "ready_for_assignment": len(warnings) == 0,
        "limit": "A pool summary does not establish construct validity.",
    }
