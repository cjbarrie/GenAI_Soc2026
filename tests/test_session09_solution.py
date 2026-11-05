from solutions.weekly_coding.session09_solution import run_checks
from pathlib import Path
import os
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def test_session09_worked_solution():
    run_checks()


def test_session09_actual_task_runs_with_recorded_return():
    environment = os.environ.copy()
    environment["COURSE_USE_RECORDED"] = "1"
    result = subprocess.run(
        [sys.executable, str(ROOT / "assessments/weekly_coding/session09_task.py")],
        cwd=ROOT,
        env=environment,
        check=True,
        capture_output=True,
        text=True,
    )
    assert "Did the evidence change? False" in result.stdout
    assert "Displayed certainty: 0.95" in result.stdout
