"""Session 2 completion task: inspect classification error.

Fill in the two functions below. You may use AI with responsibility and
disclosure, but you must be able to explain every line in plain language.
"""


def count_support_outcomes(records):
    """Return counts for SUPPORT as {'tp', 'fp', 'fn', 'tn'}.

    Each record is a dictionary containing `human_label` and `model_label`.
    SUPPORT is the positive category; every other label is not SUPPORT.
    """
    # TODO: create a dictionary whose four counts start at zero.
    # TODO: loop through records and compare the two labels with "SUPPORT".
    # TODO: increment exactly one count for every record.
    raise NotImplementedError("Complete count_support_outcomes")


def precision_recall_f1(counts):
    """Return precision, recall, and F1 as a dictionary.

    If a denominator is zero, return 0.0 for that metric.
    """
    # TODO: calculate precision = tp / (tp + fp).
    # TODO: calculate recall = tp / (tp + fn).
    # TODO: calculate F1 from precision and recall.
    raise NotImplementedError("Complete precision_recall_f1")


# Run these checks after completing both functions.
if __name__ == "__main__":
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

