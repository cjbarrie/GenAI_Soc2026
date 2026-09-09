"""Exercise the local setup paths and their beginner-facing repair messages."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]


def setup_source(week: int) -> str:
    path = next((ROOT / "workbook" / f"session{week:02d}").glob("*.ipynb"))
    notebook = json.loads(path.read_text())
    return next(
        "".join(cell["source"])
        for cell in notebook["cells"]
        if cell["cell_type"] == "code" and "course_packages" in "".join(cell["source"])
    )


@pytest.mark.parametrize("week", range(1, 14))
def test_package_discovery_runs_in_a_fresh_python_process(week: int) -> None:
    """Do not let imports already performed by pytest conceal setup-cell errors."""
    discovery_prefix = setup_source(week).split("if IN_COLAB:", 1)[0]
    program = (
        f'SESSION = "session{week:02d}"\n'
        + discovery_prefix
        + '\nprint("FRESH PACKAGE DISCOVERY COMPLETED")\n'
    )
    result = subprocess.run(
        [sys.executable, "-I", "-c", program],
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert "FRESH PACKAGE DISCOVERY COMPLETED" in result.stdout


@pytest.mark.parametrize("week", range(1, 14))
def test_local_setup_explains_missing_model(
    week: int,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    import ollama

    monkeypatch.chdir(ROOT)
    monkeypatch.setattr(ollama, "list", lambda: type("Models", (), {"models": []})())
    namespace: dict[str, object] = {"SESSION": f"session{week:02d}"}
    exec(setup_source(week), namespace)
    output = capsys.readouterr().out
    assert "Ollama server: reachable" in output
    assert "Course local model: NOT INSTALLED" in output
    assert "NEXT STEP: open a terminal and run: ollama pull" in output
    assert "Python executable:" in output
    assert "Course root:" in output


@pytest.mark.parametrize("week", range(1, 14))
def test_local_setup_explains_stopped_server(
    week: int,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    import ollama

    monkeypatch.chdir(ROOT)

    def stopped_server() -> object:
        raise ConnectionError("connection refused")

    monkeypatch.setattr(ollama, "list", stopped_server)
    namespace: dict[str, object] = {"SESSION": f"session{week:02d}"}
    exec(setup_source(week), namespace)
    output = capsys.readouterr().out
    assert "Ollama server: NOT REACHABLE" in output
    assert "NEXT STEP: start the Ollama application, then run: ollama list" in output
    assert "connection refused" in output


@pytest.mark.parametrize("week", range(1, 14))
def test_local_setup_explains_standalone_notebook(
    week: int, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.chdir(tmp_path)
    namespace: dict[str, object] = {"SESSION": f"session{week:02d}"}
    with pytest.raises(FileNotFoundError, match="notebook downloaded by itself"):
        exec(setup_source(week), namespace)
