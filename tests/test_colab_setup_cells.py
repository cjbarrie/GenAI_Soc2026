"""Exercise the package-installation branch of every Colab setup cell."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from types import ModuleType

import pytest


ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("week", range(1, 14))
def test_fresh_colab_setup_installs_then_imports(
    week: int, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Simulate a new Colab runtime where none of the notebook packages exist yet."""
    monkeypatch.chdir(ROOT)
    monkeypatch.setenv("COURSE_COLAB_ROOT", str(ROOT))
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-only-key")

    google_module = ModuleType("google")
    google_module.__path__ = []  # type: ignore[attr-defined]
    colab_module = ModuleType("google.colab")
    google_module.colab = colab_module  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, "google", google_module)
    monkeypatch.setitem(sys.modules, "google.colab", colab_module)

    required = {"openrouter", "ollama"}
    if week == 13:
        required.add("pandas")
    packages_installed = False
    original_find_spec = importlib.util.find_spec

    def fresh_runtime_find_spec(name: str, package: str | None = None) -> object | None:
        if name in required:
            return object() if packages_installed else None
        return original_find_spec(name, package)

    install_commands: list[list[str]] = []

    def record_install(command: list[str], check: bool = False, **_: object) -> subprocess.CompletedProcess:
        nonlocal packages_installed
        assert check is True
        assert command[1:4] == ["-m", "pip", "install"]
        install_commands.append(command)
        packages_installed = True
        return subprocess.CompletedProcess(command, 0)

    monkeypatch.setattr(importlib.util, "find_spec", fresh_runtime_find_spec)
    monkeypatch.setattr(subprocess, "run", record_install)

    files = list((ROOT / "workbook" / f"session{week:02d}").glob("*.ipynb"))
    assert len(files) == 1
    notebook = json.loads(files[0].read_text())
    code_cells = [
        "".join(cell["source"])
        for cell in notebook["cells"]
        if cell["cell_type"] == "code"
    ]

    original_sys_path = list(sys.path)
    namespace: dict[str, object] = {"__name__": "__main__"}
    try:
        exec(code_cells[0], namespace)
        assert namespace["IN_COLAB"] is True
        assert packages_installed is True
        assert len(install_commands) == 1
        assert "openrouter>=0.6,<1" in install_commands[0]
        assert "ollama>=0.6,<1" in install_commands[0]
        if week == 13:
            assert "pandas>=2.2,<3" in install_commands[0]

        # This is the cell that previously raised immediately after setup.
        exec(code_cells[1], namespace)
        assert namespace["HOSTED_MODEL"]
        assert namespace["LOCAL_MODEL"]
    finally:
        sys.path[:] = original_sys_path
