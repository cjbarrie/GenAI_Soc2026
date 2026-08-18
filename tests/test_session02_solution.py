from solutions.weekly_coding.session02_solution import (
    count_support_outcomes,
    precision_recall_f1,
)


def test_outcome_counts_cover_each_case():
    records = [
        {"human_label": "SUPPORT", "model_label": "SUPPORT"},
        {"human_label": "UNCLEAR", "model_label": "SUPPORT"},
        {"human_label": "SUPPORT", "model_label": "OPPOSE"},
        {"human_label": "OPPOSE", "model_label": "OPPOSE"},
    ]
    assert count_support_outcomes(records) == {
        "tp": 1,
        "fp": 1,
        "fn": 1,
        "tn": 1,
    }


def test_metrics_are_calculated_from_counts():
    metrics = precision_recall_f1({"tp": 4, "fp": 2, "fn": 0, "tn": 6})
    assert round(metrics["precision"], 3) == 0.667
    assert metrics["recall"] == 1.0
    assert round(metrics["f1"], 3) == 0.8


def test_zero_denominators_are_safe():
    assert precision_recall_f1({"tp": 0, "fp": 0, "fn": 0, "tn": 4}) == {
        "precision": 0.0,
        "recall": 0.0,
        "f1": 0.0,
    }

