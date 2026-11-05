from solutions.weekly_coding.session10_solution import run_checks
from pathlib import Path
import os
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def test_session10_worked_solution():
    run_checks()


def test_session10_actual_task_runs_with_recorded_returns():
    environment = os.environ.copy()
    environment["COURSE_USE_RECORDED"] = "1"
    result = subprocess.run(
        [sys.executable, str(ROOT / "assessments/weekly_coding/session10_task.py")],
        cwd=ROOT,
        env=environment,
        check=True,
        capture_output=True,
        text=True,
    )
    assert "Number of audited situations: 3" in result.stdout
    assert "Situation: private_information" in result.stdout
