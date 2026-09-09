"""Fast, offline structural checks for the course repository."""

from __future__ import annotations

import ast
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OBSOLETE_WEEK14 = (
    ROOT / "assessments/weekly_coding/session14_task.py",
    ROOT / "readings/session14_reading_guide.md",
    ROOT / "slides/session14/session14.qmd",
    ROOT / "solutions/weekly_coding/session14_solution.py",
    ROOT / "workbook/session14/session14_evidence_standards.ipynb",
)


def check_notebook(path: Path, problems: list[str]) -> None:
    try:
        notebook = json.loads(path.read_text())
        for index, cell in enumerate(notebook["cells"], start=1):
            if cell["cell_type"] != "code":
                continue
            source = cell["source"] if isinstance(cell["source"], str) else "".join(cell["source"])
            ast.parse(source, filename=f"{path.name}:cell-{index}")
    except Exception as error:
        problems.append(f"notebook error: {path.relative_to(ROOT)}: {error}")


def main() -> None:
    problems: list[str] = []
    for week in range(1, 15):
        syllabus = ROOT / "syllabus" / f"session{week:02d}.md"
        if not syllabus.exists():
            problems.append(f"missing: {syllabus.relative_to(ROOT)}")

    for week in range(1, 14):
        session = f"session{week:02d}"
        task = ROOT / "assessments/weekly_coding" / f"{session}_task.py"
        if not task.exists():
            problems.append(f"missing: {task.relative_to(ROOT)}")
        else:
            try:
                ast.parse(task.read_text(), filename=str(task))
            except SyntaxError as error:
                problems.append(f"task syntax: {task.relative_to(ROOT)}: {error}")
        notebooks = sorted((ROOT / "workbook" / session).glob("*.ipynb"))
        if len(notebooks) != 1:
            problems.append(f"expected one notebook in workbook/{session}; found {len(notebooks)}")
        else:
            check_notebook(notebooks[0], problems)

    for path in OBSOLETE_WEEK14:
        if path.exists():
            problems.append(f"Week 14 is presentation-only: remove {path.relative_to(ROOT)}")

    patterns = (re.compile(r"sk-or-v1-[A-Za-z0-9_-]{12,}"), re.compile(r"sk-[A-Za-z0-9]{20,}"))
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in {".py", ".md", ".qmd", ".json", ".toml", ".ipynb"}:
            continue
        if any(part in {".git", ".venv", "_book", "_build"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in patterns:
            if pattern.search(text):
                problems.append(f"possible secret in {path.relative_to(ROOT)}")

    if problems:
        print("Course checks failed:")
        print("\n".join(f"- {problem}" for problem in problems))
        raise SystemExit(1)
    print("Course structure, Weeks 1–13 notebook/task syntax, presentation week, and secret checks passed.")


if __name__ == "__main__":
    main()
