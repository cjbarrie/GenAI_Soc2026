"""Commented reference solution for the Session 2 completion task."""


def unstable_comment_ids(labels_by_comment):
    """Return IDs whose list contains more than one unique label."""
    unstable = []

    for comment_id, labels in labels_by_comment.items():
        unique_labels = set(labels)
        if len(unique_labels) > 1:
            unstable.append(comment_id)

    return unstable


def count_support_outcomes(records):
    """Count binary classification outcomes with SUPPORT as positive."""
    counts = {"tp": 0, "fp": 0, "fn": 0, "tn": 0}

    for record in records:
        human_support = record["human_label"] == "SUPPORT"
        model_support = record["model_label"] == "SUPPORT"

        if human_support and model_support:
            counts["tp"] += 1
        elif not human_support and model_support:
            counts["fp"] += 1
        elif human_support and not model_support:
            counts["fn"] += 1
        else:
            counts["tn"] += 1

    return counts


def safe_divide(numerator, denominator):
    """Divide two numbers, returning 0.0 when division is undefined."""
    if denominator == 0:
        return 0.0
    return numerator / denominator


def precision_recall_f1(counts):
    """Calculate three metrics from a dictionary of outcome counts."""
    precision = safe_divide(counts["tp"], counts["tp"] + counts["fp"])
    recall = safe_divide(counts["tp"], counts["tp"] + counts["fn"])
    f1 = safe_divide(2 * precision * recall, precision + recall)

    return {"precision": precision, "recall": recall, "f1": f1}


if __name__ == "__main__":
    variant_example = {
        "1": ["SUPPORT", "SUPPORT", "SUPPORT"],
        "3": ["SUPPORT", "UNCLEAR", "UNCLEAR"],
        "4": ["SUPPORT", "SUPPORT", "SUPPORT"],
    }
    assert unstable_comment_ids(variant_example) == ["3"]

    example = [
        {"human_label": "SUPPORT", "model_label": "SUPPORT"},
        {"human_label": "UNCLEAR", "model_label": "SUPPORT"},
        {"human_label": "OPPOSE", "model_label": "OPPOSE"},
    ]

    result = count_support_outcomes(example)
    assert result == {"tp": 1, "fp": 1, "fn": 0, "tn": 1}

    metrics = precision_recall_f1(result)
    assert metrics["precision"] == 0.5
    assert metrics["recall"] == 1.0
    assert round(metrics["f1"], 3) == 0.667

    empty = precision_recall_f1({"tp": 0, "fp": 0, "fn": 0, "tn": 2})
    assert empty == {"precision": 0.0, "recall": 0.0, "f1": 0.0}

    print("All checks passed.")
