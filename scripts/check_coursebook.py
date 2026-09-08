#!/usr/bin/env python3
"""Validate the student-facing Quarto course book and its public resources."""

from __future__ import annotations

import argparse
import ast
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "coursebook"
WEEK_DIR = BOOK / "weeks"
PYTHON_DIR = BOOK / "python"
MANIFEST = BOOK / "readings.json"
BIB = ROOT / "references.bib"
LOCAL_ANCHOR_PDF = BOOK / "downloads" / "readings" / "ai-and-research-methods-barrie-et-al-2026.pdf"
SUBMISSION_PAGE = BOOK / "recording-and-submission.qmd"
BOX_URL = "https://nyu.box.com/s/3oylc29m569ack3jv79rk22chk5r90dp"
COLAB_REPO = "https://colab.research.google.com/github/christopherbarrie/GenAI_Soc2026/blob/main"

REQUIRED_SECTIONS = [
    "## This week’s sociological question",
    "## Connection to the preceding material",
    "## Learning outcomes",
    "## Essential readings and what each contributes",
    "## Additional readings grouped by purpose",
    "## Sociological and methodological background",
    "## Synthesis of the current LLM literature",
    "## Slides",
    "## Summary and preparation",
]

OUTLINE_SECTIONS = [
    "## Question",
    "## Why this week belongs here",
    "## Provisional core readings",
    "## Planned chapter and class arc",
    "## Development status",
]

PYTHON_REQUIRED_SECTIONS = [
    "## Python walkthrough:",
    "## Workbook and environment links",
    "## Take-home exercise",
]

PYTHON_OUTLINE_SECTIONS = [
    "## Planned code trace",
    "## Planned completion recording",
    "## Development status",
]

PRESENTATION_SECTIONS = [
    "## Presentation format",
    "## What to bring",
]

DEVELOPED_SESSION_MAX = 7

BANNED_PUBLIC_FRAGMENTS = [
    "solutions/",
    "instructor/",
    "literature/source_pdfs",
    "OPENROUTER_API_KEY=",
    "sk-or-",
    "Lee-TF-APSA-AI-Report-2026-Tucker-Persily.pdf",
]

OBSOLETE_SESSION14_MATERIALS = [
    ROOT / "assessments" / "weekly_coding" / "session14_task.py",
    ROOT / "readings" / "session14_reading_guide.md",
    ROOT / "slides" / "session14" / "session14.qmd",
    ROOT / "solutions" / "weekly_coding" / "session14_solution.py",
    ROOT / "workbook" / "session14" / "session14_evidence_standards.ipynb",
]


class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.targets: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        for name in ("href", "src"):
            value = attributes.get(name)
            if value:
                self.targets.append(value)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def bib_keys() -> set[str]:
    return set(re.findall(r"^@\w+\{([^,]+),", BIB.read_text(encoding="utf-8"), re.MULTILINE))


def validate_notebook(path: Path, errors: list[str]) -> None:
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, f"Unreadable notebook {path}: {exc}")
        return
    if notebook.get("nbformat") != 4 or not isinstance(notebook.get("cells"), list):
        fail(errors, f"Invalid notebook structure: {path}")


def validate_rendered_links(errors: list[str]) -> None:
    output = BOOK / "_book"
    for page in output.rglob("*.html"):
        collector = LinkCollector()
        collector.feed(page.read_text(encoding="utf-8", errors="replace"))
        for raw_target in collector.targets:
            parsed = urlsplit(raw_target)
            if parsed.scheme or raw_target.startswith(("#", "//", "data:")):
                continue
            relative = unquote(parsed.path)
            if not relative:
                continue
            target = (page.parent / relative).resolve()
            if target.is_dir():
                target = target / "index.html"
            if not target.exists():
                fail(errors, f"Broken rendered link in {page.relative_to(output)}: {raw_target}")


def validate_sources(rendered: bool) -> list[str]:
    errors: list[str] = []
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    weeks = manifest.get("weeks", {})
    keys = bib_keys()

    if not LOCAL_ANCHOR_PDF.exists():
        fail(errors, f"Missing local course anchor PDF: {LOCAL_ANCHOR_PDF}")

    if not SUBMISSION_PAGE.exists():
        fail(errors, f"Missing recording and submission guide: {SUBMISSION_PAGE}")
    else:
        submission_text = SUBMISSION_PAGE.read_text(encoding="utf-8")
        required_submission_text = [
            BOX_URL,
            "5:00 p.m. Eastern on the Tuesday before the next class",
            "## Record on a Mac",
            "## Record on Windows",
            "## Record on a Chromebook",
            "screen recording",
        ]
        for required_text in required_submission_text:
            if required_text not in submission_text:
                fail(errors, f"recording-and-submission.qmd: missing {required_text!r}")

    for obsolete_path in OBSOLETE_SESSION14_MATERIALS:
        if obsolete_path.exists():
            fail(errors, f"Presentation week must not contain course content: {obsolete_path}")

    if set(weeks) != {f"session{n:02d}" for n in range(1, 15)}:
        fail(errors, "Reading manifest must contain exactly session01–session14.")

    for number in range(1, 15):
        session = f"session{number:02d}"
        chapter = WEEK_DIR / f"{session}.qmd"
        if not chapter.exists():
            fail(errors, f"Missing chapter: {chapter}")
            continue
        text = chapter.read_text(encoding="utf-8")
        python_page = PYTHON_DIR / f"{session}.qmd"
        python_text = ""
        if number <= 13:
            if not python_page.exists():
                fail(errors, f"Missing separate Python page: {python_page}")
            else:
                python_text = python_page.read_text(encoding="utf-8")
        elif python_page.exists():
            fail(errors, "session14: presentation week must not have a Python page")

        if number <= DEVELOPED_SESSION_MAX:
            expected_sections = REQUIRED_SECTIONS
        elif number == 14:
            expected_sections = PRESENTATION_SECTIONS
        else:
            expected_sections = OUTLINE_SECTIONS
        for heading in expected_sections:
            if heading not in text:
                fail(errors, f"{chapter.name}: missing standard section beginning {heading!r}")
        for fragment in BANNED_PUBLIC_FRAGMENTS:
            if fragment in text:
                fail(errors, f"{chapter.name}: banned public fragment {fragment!r}")
            if fragment in python_text:
                fail(errors, f"{python_page.name}: banned public fragment {fragment!r}")

        if number <= DEVELOPED_SESSION_MAX:
            for heading in PYTHON_REQUIRED_SECTIONS:
                if heading not in python_text:
                    fail(errors, f"{python_page.name}: missing standard section beginning {heading!r}")
        elif number <= 13:
            for heading in PYTHON_OUTLINE_SECTIONS:
                if heading not in python_text:
                    fail(errors, f"{python_page.name}: missing provisional section {heading!r}")

        if number <= 13 and f"../python/{session}.qmd" not in text:
            fail(errors, f"{chapter.name}: missing link to separate Python page")
        if number <= 13 and f"../weeks/{session}.qmd" not in python_text:
            fail(errors, f"{python_page.name}: missing return link to weekly page")

        if number <= DEVELOPED_SESSION_MAX:
            if f'_generated/slides/{session}.html' not in text:
                fail(errors, f"{chapter.name}: missing slide embed/full-screen link")
            if ".ipynb" not in python_text:
                fail(errors, f"{python_page.name}: missing notebook download")
            if f"{session}_task.py" not in python_text:
                fail(errors, f"{python_page.name}: missing task download")
            if f"{session}_offline_bundle.zip" not in python_text:
                fail(errors, f"{python_page.name}: missing offline bundle download")
            if "screen recording" not in python_text:
                fail(errors, f"{python_page.name}: missing narrated screen-recording instructions")
        elif "_generated/slides" in text or ".ipynb" in text or ".ipynb" in python_text:
            fail(errors, f"{session}: provisional pages must not publish unfinished materials")

        if number <= 13:
            if "../recording-and-submission.qmd" not in python_text:
                fail(errors, f"{python_page.name}: missing link to the canonical submission guide")
            if "5:00 p.m. Eastern on the Tuesday before the next class" not in python_text:
                fail(errors, f"{python_page.name}: missing weekly recording deadline")

        entries = weeks.get(session, [])
        if number == 14:
            if entries:
                fail(errors, "session14: presentation week must not assign readings")
        else:
            statuses = {entry.get("status") for entry in entries}
            if not {"essential", "additional"}.issubset(statuses):
                fail(errors, f"{session}: manifest requires essential and additional readings")
            for entry in entries:
                key = entry.get("key", "")
                if key not in keys:
                    fail(errors, f"{session}: unknown citation key {key!r}")
                if f"@{key}" not in text:
                    fail(errors, f"{chapter.name}: manifest reading {key} is not cited")
                for field in ("section", "purpose", "url"):
                    if not entry.get(field):
                        fail(errors, f"{session}/{key}: missing {field}")
                url = entry.get("url", "")
                if not url.startswith("https://"):
                    fail(errors, f"{session}/{key}: URL is not HTTPS")
                if key == "BarrieEtAl2026AIResearchMethods":
                    expected_local = "downloads/readings/ai-and-research-methods-barrie-et-al-2026.pdf"
                    if entry.get("local_url") != expected_local:
                        fail(errors, f"{session}/{key}: missing canonical local PDF path")
                    if f"../{expected_local}" not in text:
                        fail(errors, f"{chapter.name}: missing local APSA chapter download link")

        if number <= DEVELOPED_SESSION_MAX:
            source_notebooks = sorted((ROOT / "workbook" / session).glob("*.ipynb"))
            if len(source_notebooks) != 1:
                fail(errors, f"{session}: expected exactly one source notebook")
            else:
                source_notebook = source_notebooks[0]
                validate_notebook(source_notebook, errors)
                colab_url = f"{COLAB_REPO}/workbook/{session}/{source_notebook.name}"
                if colab_url not in python_text:
                    fail(errors, f"{python_page.name}: missing Google Colab launch link")
                notebook_text = source_notebook.read_text(encoding="utf-8")
                if colab_url not in notebook_text:
                    fail(errors, f"{source_notebook.name}: missing internal Google Colab badge")
                if "colab-setup" not in notebook_text:
                    fail(errors, f"{source_notebook.name}: missing Colab repository setup cell")
            task = ROOT / "assessments" / "weekly_coding" / f"{session}_task.py"
            try:
                task_source = task.read_text(encoding="utf-8")
                task_tree = ast.parse(task_source, filename=str(task))
            except (OSError, SyntaxError) as exc:
                fail(errors, f"Invalid task Python {task}: {exc}")
            else:
                advanced_definitions = (
                    ast.FunctionDef,
                    ast.AsyncFunctionDef,
                    ast.ClassDef,
                    ast.Lambda,
                )
                if any(isinstance(node, advanced_definitions) for node in ast.walk(task_tree)):
                    fail(errors, f"{task.name}: beginner completion tasks must not define functions or classes")
                if '__name__ == "__main__"' in task_source or "__name__ == '__main__'" in task_source:
                    fail(errors, f"{task.name}: unexplained __main__ guard is not allowed")
                if number in (1, 2):
                    if "client.chat.send" not in task_source or "ollama.chat" not in task_source:
                        fail(errors, f"{task.name}: Weeks 1–2 must show both live routes")
                if 3 <= number <= 7:
                    if 'ROUTE = "ollama"' not in task_source:
                        fail(errors, f"{task.name}: missing visible route selector")
                    if "client.chat.send" not in task_source or "ollama.chat" not in task_source:
                        fail(errors, f"{task.name}: both route branches must remain visible")

        if rendered:
            html = BOOK / "_book" / "weeks" / f"{session}.html"
            if not html.exists():
                fail(errors, f"Rendered chapter missing: {html}")
            if number <= 13:
                python_html = BOOK / "_book" / "python" / f"{session}.html"
                if not python_html.exists():
                    fail(errors, f"Rendered Python page missing: {python_html}")
            if number <= DEVELOPED_SESSION_MAX:
                slide = BOOK / "_book" / "_generated" / "slides" / f"{session}.html"
                bundle = BOOK / "_book" / "_generated" / "downloads" / session / f"{session}_offline_bundle.zip"
                if not slide.exists():
                    fail(errors, f"Packaged slide missing: {slide}")
                if not bundle.exists():
                    fail(errors, f"Offline bundle missing: {bundle}")

    # Coding artifacts exist for Weeks 8–13 even though their public book pages
    # remain bare outlines until the literature and slides are developed.
    for number in range(8, 14):
        session = f"session{number:02d}"
        task = ROOT / "assessments" / "weekly_coding" / f"{session}_task.py"
        notebooks = sorted((ROOT / "workbook" / session).glob("*.ipynb"))
        if not task.exists():
            fail(errors, f"Missing provisional coding task: {task}")
            continue
        try:
            source = task.read_text(encoding="utf-8")
            tree = ast.parse(source, filename=str(task))
        except SyntaxError as exc:
            fail(errors, f"Invalid task Python {task}: {exc}")
            continue
        definitions = [node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
        if number == 8:
            if definitions:
                fail(errors, "session08_task.py: Week 8 must not define a function")
            if "client.chat.send" not in source or "ollama.chat" not in source or "for profile in profiles" not in source:
                fail(errors, "session08_task.py: missing bounded dual-route loop")
        if number == 9 and "def choose_action(" not in source:
            fail(errors, "session09_task.py: Week 9 must introduce choose_action")
        if len(notebooks) != 1:
            fail(errors, f"{session}: expected exactly one provisional coding notebook")
        else:
            validate_notebook(notebooks[0], errors)

    fixture_path = ROOT / "data" / "dual_route_recorded_outputs.json"
    try:
        fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, f"Unreadable recorded-output contingency: {exc}")
    else:
        for number in range(1, 14):
            if f"session{number:02d}" not in fixture:
                fail(errors, f"Recorded-output contingency missing session{number:02d}")

    if rendered:
        packaged_anchor = BOOK / "_book" / "downloads" / "readings" / LOCAL_ANCHOR_PDF.name
        if not packaged_anchor.exists():
            fail(errors, f"Packaged local APSA chapter missing: {packaged_anchor}")

    if rendered:
        validate_rendered_links(errors)

    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rendered", action="store_true", help="Also check rendered HTML resources.")
    args = parser.parse_args()
    errors = validate_sources(args.rendered)
    if errors:
        print("Course-book validation failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    print("Course-book validation passed: 14 weekly pages, 13 separate Python pages, and presentation-only Week 14.")


if __name__ == "__main__":
    main()
