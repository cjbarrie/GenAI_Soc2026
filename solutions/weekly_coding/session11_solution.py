"""Offline checks for the Week 11 paired-comparison routine."""


def build_pair_comparisons(aae_results, sae_results):
    comparisons = []
    different_count = 0

    for aae_record, sae_record in zip(aae_results, sae_results):
        if aae_record["pair_id"] != sae_record["pair_id"]:
            raise ValueError("The paired lists are not in the same order.")
        different = aae_record["occupation"] != sae_record["occupation"]
        different_count += int(different)
        comparisons.append({
            "pair_id": aae_record["pair_id"],
            "aae_occupation": aae_record["occupation"],
            "sae_occupation": sae_record["occupation"],
            "different": different,
        })

    difference_rate = different_count / len(comparisons)
    return comparisons, different_count, difference_rate


def run_checks():
    aae_results = [
        {"pair_id": "talking", "occupation": "cashier"},
        {"pair_id": "cooking", "occupation": "cook"},
    ]
    sae_results = [
        {"pair_id": "talking", "occupation": "office clerk"},
        {"pair_id": "cooking", "occupation": "cook"},
    ]
    comparisons, count, rate = build_pair_comparisons(aae_results, sae_results)
    assert comparisons[0]["different"] is True
    assert comparisons[1]["different"] is False
    assert count == 1
    assert rate == 0.5

    reversed_sae = list(reversed(sae_results))
    try:
        build_pair_comparisons(aae_results, reversed_sae)
    except ValueError as error:
        assert "same order" in str(error)
    else:
        raise AssertionError("Misordered pairs should raise ValueError")


if __name__ == "__main__":
    run_checks()
    print("All Session 11 checks passed.")
