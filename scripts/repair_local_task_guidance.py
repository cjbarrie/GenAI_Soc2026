#!/usr/bin/env python3
"""Add the same actionable local setup checks to task files and book code."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

OLD_IMPORTS = """import ollama
from openrouter import OpenRouter
"""

NEW_IMPORTS = """try:
    import ollama
    from openrouter import OpenRouter
except ModuleNotFoundError as error:
    raise ModuleNotFoundError(
        \"A course SDK is missing. Open a terminal in the complete GenAI_Soc2026 \"
        \"folder, run 'uv sync --frozen', then run this task with 'uv run python'.\"
    ) from error
"""

ROOT_LOOP = """ROOT = Path.cwd()
while not (ROOT / \"config\" / \"course_models.json\").exists() and ROOT != ROOT.parent:
    ROOT = ROOT.parent
"""

ROOT_WITH_CHECK = ROOT_LOOP + """
if not (ROOT / \"config\" / \"course_models.json\").exists():
    raise FileNotFoundError(
        \"The complete GenAI_Soc2026 repository could not be found. A task or \"
        \"notebook downloaded by itself is not enough for local work. Open a terminal \"
        \"in the complete course folder and run this file from there.\"
    )
"""


def repair(path: Path) -> None:
    source = path.read_text(encoding="utf-8")
    if OLD_IMPORTS in source:
        source = source.replace(OLD_IMPORTS, NEW_IMPORTS, 1)
    if ROOT_LOOP in source and "A task or" not in source:
        source = source.replace(ROOT_LOOP, ROOT_WITH_CHECK, 1)
    if "ollama.chat(" in source and "ollama.chat(think=False," not in source:
        source = source.replace("ollama.chat(", "ollama.chat(think=False, ")
    path.write_text(source, encoding="utf-8")


def main() -> None:
    paths = sorted((ROOT / "assessments" / "weekly_coding").glob("session*_task.py"))
    paths += sorted((ROOT / "coursebook" / "python").glob("session*.qmd"))
    for path in paths:
        repair(path)
    print(f"Repaired local guidance in {len(paths)} task and course-book files.")


if __name__ == "__main__":
    main()
