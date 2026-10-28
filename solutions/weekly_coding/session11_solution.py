"""Offline checks for the Week 11 dialect-comparison routine."""

import json


def build_pair_comparisons(results):
    """Summarize whether the two variants in each pair received the same choice."""
    pair_ids = []
    for row in results:
        if row["pair_id"] not in pair_ids:
            pair_ids.append(row["pair_id"])

    comparisons = []
    for pair_id in pair_ids:
        rows = [row for row in results if row["pair_id"] == pair_id]
        assert len(rows) == 2
        by_variant = {row["variant"]: row for row in rows}
        comparisons.append({
            "pair_id": pair_id,
            "aae_occupation": by_variant["aae"]["occupation"],
            "sae_occupation": by_variant["sae"]["occupation"],
            "different": by_variant["aae"]["occupation"] != by_variant["sae"]["occupation"],
        })
    return comparisons


def run_checks():
    results = [
        {"pair_id": "talking", "variant": "aae", "occupation": "cashier"},
        {"pair_id": "talking", "variant": "sae", "occupation": "office clerk"},
        {"pair_id": "cooking", "variant": "aae", "occupation": "cook"},
        {"pair_id": "cooking", "variant": "sae", "occupation": "cook"},
    ]
    comparisons = build_pair_comparisons(results)
    assert comparisons[0]["different"] is True
    assert comparisons[1]["different"] is False
    assert json.loads('{"occupation": "cook"}')["occupation"] == "cook"


if __name__ == "__main__":
    run_checks()
    print("All Session 11 checks passed.")
