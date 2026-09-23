"""Checks for the Week 4 protest-sequence exercise and its source record."""

from __future__ import annotations

import ast
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IMAGE_DIR = ROOT / "slides" / "session04" / "images"
FRAME_NAMES = [
    "uttarakhand_frame_1_04.5s.png",
    "uttarakhand_frame_2_05.0s.png",
    "uttarakhand_frame_3_06.0s.png",
    "uttarakhand_frame_4_08.5s.png",
    "uttarakhand_frame_5_11.5s.png",
]


def test_real_protest_source_and_attribution_are_packaged() -> None:
    assert (IMAGE_DIR / "uttarakhand_protest_confrontation.webm").stat().st_size > 5_000_000
    source_note = (IMAGE_DIR / "uttarakhand_protest_SOURCE.md").read_text()
    assert "Himalayanwarrior" in source_note
    assert "CC BY-SA 4.0" in source_note
    assert "4.5 seconds" in source_note
    assert "11.5 seconds" in source_note


def test_selected_frames_exist_and_are_genuinely_different() -> None:
    frames = [IMAGE_DIR / name for name in FRAME_NAMES]
    assert all(path.exists() for path in frames)
    hashes = [hashlib.sha256(path.read_bytes()).hexdigest() for path in frames]
    assert len(set(hashes)) == len(frames)


def test_current_task_uses_the_protest_sequence_and_beginner_python() -> None:
    task_path = ROOT / "assessments" / "weekly_coding" / "session04_task.py"
    source = task_path.read_text()
    tree = ast.parse(source)

    assert "Uttarakhand protest confrontation" in source
    assert "frame_observations" in source
    assert "researcher_check" in source
    assert "changed_research_record" in source
    assert "comparison_record" in source
    assert "uttarakhand_frame_5_11.5s.png" in source
    assert not any(
        isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) for node in ast.walk(tree)
    )


def test_notebook_and_course_page_name_the_same_assessed_fields() -> None:
    notebook = json.loads(
        (ROOT / "workbook/session04/session04_multimodal_evidence.ipynb").read_text()
    )
    notebook_text = "\n".join("".join(cell["source"]) for cell in notebook["cells"])
    page_text = (ROOT / "coursebook/python/session04.qmd").read_text()

    for field in (
        "frame_observations",
        "visible_changes",
        "physical_contact_visible",
        "third_party_intervention_visible",
        "not_established",
        "researcher_check",
        "changed_research_record",
        "comparison_record",
    ):
        assert field in notebook_text
        assert field in page_text

    assert "zidane_fine2" not in notebook_text
    assert "zidane_fine2" not in page_text


def test_notebook_and_course_page_use_identical_assessed_code() -> None:
    notebook = json.loads(
        (ROOT / "workbook/session04/session04_multimodal_evidence.ipynb").read_text()
    )
    notebook_code = [
        "".join(cell["source"]).rstrip()
        for cell in notebook["cells"]
        if cell["cell_type"] == "code"
    ]
    page_text = (ROOT / "coursebook/python/session04.qmd").read_text()
    page_code = [
        block.rstrip()
        for block in re.findall(r"```python\n(.*?)\n```", page_text, re.S)
    ]

    # The notebook begins with its supplied Colab/local setup cell. Every
    # assessed cell after that must be exactly the code students see online.
    assert page_code == notebook_code[1:]
