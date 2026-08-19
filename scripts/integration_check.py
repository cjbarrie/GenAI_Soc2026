"""Deterministic cross-artifact checks for the Phase 7 course release."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SESSION_DATES = {
    1: "September 2", 2: "September 9", 3: "September 16", 4: "September 23",
    5: "September 30", 6: "October 7", 7: "October 21", 8: "October 28",
    9: "November 4", 10: "November 11", 11: "November 18", 12: "November 25",
    13: "December 2", 14: "December 9",
}
REQUIRED_NOTEBOOK_CUES = {
    "input": ("input",),
    "Python type": ("python type", "type →", "identify the python type"),
    "operation": ("operation", "transformation"),
    "output": ("output", "return"),
    "research meaning": ("research meaning", "research question"),
    "prediction pause": ("pause and say it aloud", "before running", "predict"),
    "oral explanation": ("oral-assessment rehearsal", "explain every line", "plain language"),
}
SECRET_PATTERNS = {
    "OpenRouter key": re.compile("sk-or-" + r"v1-[A-Za-z0-9_-]{12,}"),
    "OpenAI-style key": re.compile(r"sk-[A-Za-z0-9]{20,}"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}


def add(condition: bool, message: str, problems: list[str]) -> None:
    if not condition:
        problems.append(message)


def load_notebook(path: Path, problems: list[str]) -> dict:
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except Exception as error:
        problems.append(f"invalid notebook JSON: {path.relative_to(ROOT)}: {error}")
        return {}
    cells = notebook.get("cells", [])
    ids = [cell.get("id") for cell in cells]
    add(all(ids), f"missing notebook cell ID: {path.relative_to(ROOT)}", problems)
    add(len(ids) == len(set(ids)), f"duplicate notebook cell ID: {path.relative_to(ROOT)}", problems)
    for index, cell in enumerate(cells, start=1):
        if cell.get("cell_type") != "code":
            continue
        source = cell.get("source", "")
        if isinstance(source, list):
            source = "".join(source)
        try:
            compile(source, f"{path.name}:cell-{index}", "exec")
        except SyntaxError as error:
            problems.append(f"notebook syntax: {path.relative_to(ROOT)} cell {index}: {error}")
        add(cell.get("execution_count") is not None, f"unexecuted code cell: {path.relative_to(ROOT)} cell {index}", problems)
        for output in cell.get("outputs", []):
            add(output.get("output_type") != "error", f"error output: {path.relative_to(ROOT)} cell {index}", problems)
    return notebook


def main() -> None:
    problems: list[str] = []
    syllabus = (ROOT / "syllabus" / "SYLLABUS.md").read_text(encoding="utf-8")
    plan = (ROOT / "COURSE_PLAN.md").read_text(encoding="utf-8")
    config = json.loads((ROOT / "config" / "course_models.json").read_text(encoding="utf-8"))

    for number, date in SESSION_DATES.items():
        sid = f"session{number:02d}"
        paths = {
            "syllabus": ROOT / "syllabus" / f"{sid}.md",
            "reading guide": ROOT / "readings" / f"{sid}_reading_guide.md",
            "instructor notes": ROOT / "instructor" / f"{sid}_notes.md",
            "task": ROOT / "assessments" / "weekly_coding" / f"{sid}_task.py",
            "solution": ROOT / "solutions" / "weekly_coding" / f"{sid}_solution.py",
            "test": ROOT / "tests" / f"test_{sid}_solution.py",
            "deck": ROOT / "slides" / sid / f"{sid}.qmd",
        }
        for label, path in paths.items():
            add(path.exists(), f"missing {label}: {path.relative_to(ROOT)}", problems)
        notebook_paths = sorted((ROOT / "workbook" / sid).glob("*.ipynb"))
        add(len(notebook_paths) == 1, f"expected one notebook for {sid}; found {len(notebook_paths)}", problems)
        if len(notebook_paths) != 1 or any(not path.exists() for path in paths.values()):
            continue

        texts = {label: path.read_text(encoding="utf-8") for label, path in paths.items()}
        notebook = load_notebook(notebook_paths[0], problems)
        notebook_text = json.dumps(notebook, ensure_ascii=False)
        function_match = re.search(r"def\s+([a-z][a-z0-9_]*)\(", texts["solution"])
        add(function_match is not None, f"no solution function found for {sid}", problems)
        if function_match:
            function = function_match.group(1)
            for label in ("task",):
                add(function in texts[label], f"{sid}: function {function} absent from {label}", problems)
            add("run_checks" in texts["test"] or function in texts["test"], f"{sid}: test invokes neither run_checks nor {function}", problems)
            if number != 2:  # Session 2 is the richer pilot and names two linked functions.
                for label in ("deck", "reading guide", "instructor notes"):
                    add(function in texts[label], f"{sid}: function {function} absent from {label}", problems)
            add(function in notebook_text, f"{sid}: function {function} absent from notebook", problems)

        add(date in texts["syllabus"], f"{sid}: date mismatch in session syllabus", problems)
        add(date in texts["deck"], f"{sid}: date mismatch in deck", problems)
        add(f"| {number} |" in syllabus and date.split()[0][:3] in syllabus, f"{sid}: missing from master schedule", problems)
        add("optional extension" in texts["task"].lower(), f"{sid}: task lacks optional extension", problems)
        add("[Sources]" in texts["deck"], f"{sid}: deck lacks source notes", problems)
        lower_notebook = notebook_text.lower()
        for cue, alternatives in REQUIRED_NOTEBOOK_CUES.items():
            add(any(phrase in lower_notebook for phrase in alternatives), f"{sid}: notebook lacks novice-code cue '{cue}'", problems)

    foundation_path = ROOT / "workbook" / "00_python_foundations" / "python_foundations.ipynb"
    add(foundation_path.exists(), "missing Python foundations notebook", problems)
    if foundation_path.exists():
        foundation = load_notebook(foundation_path, problems)
        foundation_text = json.dumps(foundation, ensure_ascii=False).lower()
        for term in ("string", "dictionary", "condition", "loop", "function", "json", "algorithm"):
            add(term in foundation_text, f"Python foundations lacks {term}", problems)

    hosted_model = config["hosted"]["model"]
    local_model = config["local"]["model"]
    session2 = (ROOT / "workbook" / "session02" / "session02_annotation_measurement.ipynb").read_text(encoding="utf-8")
    add(hosted_model in session2, "Session 2 hosted-model default differs from central config", problems)
    add(local_model in (ROOT / "docs" / "LOCAL_LLM_GUIDE.md").read_text(encoding="utf-8"), "Local guide differs from central model config", problems)
    phase6_done = any(
        marker in plan
        for marker in ("Phase 6 — Scale:** Implemented", "Phase 6 — Scale:** Completed")
    )
    add(phase6_done, "COURSE_PLAN does not record Phase 6 completion", problems)

    tracked_suffixes = {".py", ".md", ".qmd", ".json", ".toml", ".txt", ".ipynb"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in tracked_suffixes or any(part in {".git", ".venv", "_build"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in SECRET_PATTERNS.items():
            add(pattern.search(text) is None, f"possible {label} in {path.relative_to(ROOT)}", problems)

    bib = (ROOT / "references.bib").read_text(encoding="utf-8")
    keys = re.findall(r"(?m)^@\w+\{([^,]+),", bib)
    add(len(keys) == len(set(keys)), "duplicate bibliography keys", problems)
    add(len(keys) >= 30, f"bibliography unexpectedly small: {len(keys)} entries", problems)

    if problems:
        print("Integration checks failed:")
        for problem in problems:
            print("-", problem)
        raise SystemExit(1)
    print("Phase 7 integration checks passed: 14 aligned sessions, 15 executed notebooks, central models, bibliography, and secret scan.")


if __name__ == "__main__":
    main()
