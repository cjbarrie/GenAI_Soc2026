"""Fast, offline structural checks for the course repository."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def check_exists(path: Path, problems: list[str]) -> None:
    if not path.exists():
        problems.append(f"missing: {path.relative_to(ROOT)}")


def check_notebook(path: Path, problems: list[str]) -> None:
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
        code_cells = [cell for cell in notebook["cells"] if cell["cell_type"] == "code"]
        for index, cell in enumerate(code_cells, start=1):
            source = cell["source"] if isinstance(cell["source"], str) else "".join(cell["source"])
            compile(source, f"{path.name}:code-cell-{index}", "exec")
    except Exception as error:  # report the file and original parser/compiler message
        problems.append(f"notebook error: {path.relative_to(ROOT)}: {error}")


def main() -> None:
    problems: list[str] = []
    for number in range(1, 15):
        sid = f"session{number:02d}"
        check_exists(ROOT / "syllabus" / f"{sid}.md", problems)
        check_exists(ROOT / "readings" / f"{sid}_reading_guide.md", problems)
        check_exists(ROOT / "instructor" / f"{sid}_notes.md", problems)
        check_exists(ROOT / "assessments" / "weekly_coding" / f"{sid}_task.py", problems)
        check_exists(ROOT / "solutions" / "weekly_coding" / f"{sid}_solution.py", problems)
        check_exists(ROOT / "slides" / sid / f"{sid}.qmd", problems)

        notebook_dir = ROOT / "workbook" / sid
        notebooks = list(notebook_dir.glob("*.ipynb")) if notebook_dir.exists() else []
        if len(notebooks) != 1:
            problems.append(f"expected one notebook in {notebook_dir.relative_to(ROOT)}; found {len(notebooks)}")
        else:
            check_notebook(notebooks[0], problems)

    foundation = ROOT / "workbook" / "00_python_foundations" / "python_foundations.ipynb"
    check_exists(foundation, problems)
    if foundation.exists():
        check_notebook(foundation, problems)

    tracked_text_suffixes = {".py", ".md", ".qmd", ".json", ".txt", ".toml"}
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix in tracked_text_suffixes and ".venv" not in path.parts:
            text = path.read_text(encoding="utf-8", errors="ignore")
            secret_prefix = "sk-or-" + "v1-"
            if secret_prefix in text:
                problems.append(f"possible OpenRouter secret in {path.relative_to(ROOT)}")

    if problems:
        print("Course checks failed:")
        for problem in problems:
            print("-", problem)
        raise SystemExit(1)

    print("Course structure, notebook syntax, and secret-pattern checks passed.")


if __name__ == "__main__":
    main()
