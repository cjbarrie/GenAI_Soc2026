#!/usr/bin/env python3
"""Prepare public course-book resources without generating course prose.

This script renders the existing Reveal decks when they are stale, then copies
the self-contained HTML, student notebooks and weekly task files into the
coursebook's generated resource directory. It never edits source slides,
notebooks, chapters, solutions or instructor materials.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from zipfile import ZIP_DEFLATED, ZipFile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "coursebook"
GENERATED = BOOK / "_generated"
DEVELOPED_SESSIONS = range(1, 9)
GLOSSARY_PAGES = [
    "model-call-basics",
    "context-and-memory",
    "outputs-and-tools",
    "agents-and-harnesses",
    "models-and-evaluation",
]


def newest_mtime(paths: list[Path]) -> float:
    existing = [path.stat().st_mtime for path in paths if path.exists()]
    return max(existing, default=0.0)


def render_slide_if_needed(session: str) -> Path:
    slide_dir = ROOT / "slides" / session
    source = slide_dir / f"{session}.qmd"
    rendered = slide_dir / f"{session}.html"
    dependencies = [source, ROOT / "design" / "theme.scss"]
    dependencies.extend(slide_dir.glob("*.css"))
    dependencies.extend(slide_dir.glob("images/**/*"))

    if not rendered.exists() or rendered.stat().st_mtime < newest_mtime(list(dependencies)):
        subprocess.run(
            ["quarto", "render", str(source), "--to", "revealjs"],
            cwd=ROOT,
            check=True,
        )
    return rendered


def prepare_glossary_notebooks() -> None:
    """Create offline companion notebooks from the tested book examples."""
    output_dir = GENERATED / "downloads" / "glossary"
    output_dir.mkdir(parents=True, exist_ok=True)

    for stem in GLOSSARY_PAGES:
        source = BOOK / "glossary" / f"{stem}.qmd"
        text = source.read_text(encoding="utf-8")
        sections = list(
            re.finditer(
                r"^## (?P<title>.+?) \{#(?P<anchor>[a-z0-9-]+)\}\s*$",
                text,
                re.MULTILINE,
            )
        )
        cells: list[dict[str, object]] = [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# Companion notebook: {stem.replace('-', ' ').title()}\n",
                    "\n",
                    "These examples run offline. Read the field-guide entry beside each example before changing it.\n",
                ],
            }
        ]

        for position, match in enumerate(sections):
            end = sections[position + 1].start() if position + 1 < len(sections) else len(text)
            block = text[match.end():end]
            code_blocks = re.findall(r"```python\n(.*?)\n```", block, re.DOTALL)
            if len(code_blocks) != 1:
                raise RuntimeError(
                    f"Expected one Python example in {source.name}#{match.group('anchor')}; "
                    f"found {len(code_blocks)}"
                )
            public_url = (
                "https://cjbarrie.github.io/GenAI_Soc2026/glossary/"
                f"{stem}.html#{match.group('anchor')}"
            )
            cells.append(
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        f"## {match.group('title')}\n",
                        "\n",
                        f"[Read the complete entry]({public_url}).\n",
                    ],
                }
            )
            cells.append(
                {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": code_blocks[0].splitlines(keepends=True),
                }
            )

        notebook = {
            "cells": cells,
            "metadata": {
                "kernelspec": {
                    "display_name": "Python 3",
                    "language": "python",
                    "name": "python3",
                },
                "language_info": {"name": "python", "version": "3.11"},
            },
            "nbformat": 4,
            "nbformat_minor": 5,
        }
        destination = output_dir / f"{stem}.ipynb"
        destination.write_text(json.dumps(notebook, indent=1) + "\n", encoding="utf-8")


def prepare() -> None:
    if GENERATED.exists():
        shutil.rmtree(GENERATED)
    slide_output = GENERATED / "slides"
    slide_output.mkdir(parents=True, exist_ok=True)

    for number in DEVELOPED_SESSIONS:
        session = f"session{number:02d}"
        rendered_slide = render_slide_if_needed(session)
        shutil.copy2(rendered_slide, slide_output / f"{session}.html")

        download_dir = GENERATED / "downloads" / session
        download_dir.mkdir(parents=True, exist_ok=True)

        notebooks = sorted((ROOT / "workbook" / session).glob("*.ipynb"))
        if len(notebooks) != 1:
            raise RuntimeError(f"Expected one notebook for {session}; found {len(notebooks)}")
        shutil.copy2(notebooks[0], download_dir / notebooks[0].name)

        task = ROOT / "assessments" / "weekly_coding" / f"{session}_task.py"
        if not task.exists():
            raise FileNotFoundError(task)
        shutil.copy2(task, download_dir / task.name)

        bundle = download_dir / f"{session}_offline_bundle.zip"
        with ZipFile(bundle, "w", compression=ZIP_DEFLATED) as archive:
            archive.write(notebooks[0], Path("workbook") / session / notebooks[0].name)
            archive.write(task, Path("assessments") / "weekly_coding" / task.name)
            data_dir = ROOT / "data" / session
            if data_dir.exists():
                for data_file in sorted(path for path in data_dir.rglob("*") if path.is_file()):
                    if data_file.suffix.lower() in {".pdf", ".doc", ".docx", ".xls", ".xlsx"}:
                        raise RuntimeError(f"Refusing to package restricted source format: {data_file}")
                    archive.write(data_file, data_file.relative_to(ROOT))

    prepare_glossary_notebooks()

    print("Prepared public slides, weekly resources and field-guide companion notebooks.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--prepare",
        action="store_true",
        help="Render stale slides and package public course-book resources.",
    )
    args = parser.parse_args()
    if not args.prepare:
        parser.error("No action selected. Use --prepare.")
    prepare()


if __name__ == "__main__":
    main()
