import json
from pathlib import Path

from solutions.weekly_coding.session08_solution import run_checks


ROOT = Path(__file__).resolve().parents[1]


def test_session08_worked_solution():
    run_checks()


def test_session08_reference_run_is_consistent_across_public_materials():
    reference = json.loads(
        (ROOT / "data/session08/example_outputs/towel_local_reference.json").read_text()
    )
    assert reference["predicted_effect_points"] == 45
    assert reference["observed_effect_points"] == 9.0
    assert reference["absolute_error_points"] == 36.0

    public_sources = [
        ROOT / "slides/session08/session08.qmd",
        ROOT / "coursebook/python/session08.qmd",
        ROOT / "workbook/session08/session08_opinion_prediction.ipynb",
        ROOT / "assessments/weekly_coding/session08_task.py",
    ]
    for path in public_sources:
        text = path.read_text()
        assert "gemma4:e2b-it-qat" in text
        assert "45" in text
        assert "36" in text
