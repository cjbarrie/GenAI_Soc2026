#!/usr/bin/env python3
"""Apply the verified Colab/local setup to the Week 1 and Week 2 notebooks."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def lines(text: str) -> list[str]:
    return text.strip("\n").splitlines(keepends=True) + ["\n"]


SETUP_MARKDOWN = """
## Prepare the notebook environment

Run the next cell before any other code. In Colab it installs the two small Python SDKs and downloads the public course repository. On a local machine it does not install anything silently: it checks that this notebook is using the course environment and gives the exact repair command if it is not.

**What this cell does not do:** Colab cannot run the Ollama server on your laptop. The Ollama call is therefore skipped in Colab and must be completed later in local JupyterLab or on the in-class machine.

For local work, download the complete repository rather than this notebook alone, start it with `uv run jupyter lab`, and follow any `NEXT STEP` printed by the setup cell. The full instructions are in `docs/ENVIRONMENT_SETUP.md` and in the course book's computing chapter.
"""


SETUP_CODE = r'''
# Run this cell first. It prepares Colab or checks the local Python environment.
import importlib as setup_importlib
import importlib.util as setup_importlib_util
import os as setup_os
import subprocess as setup_subprocess
import sys as setup_sys
from pathlib import Path as SetupPath

try:
    import google.colab as setup_colab  # type: ignore[import-not-found]
    IN_COLAB = True
except ImportError:
    IN_COLAB = False

course_packages = {
    "openrouter": "openrouter>=0.6,<1",
    "ollama": "ollama>=0.6,<1",
}
missing_packages = [
    package_name
    for package_name in course_packages
    if setup_importlib_util.find_spec(package_name) is None
]

if IN_COLAB:
    if missing_packages:
        packages_to_install = [course_packages[name] for name in missing_packages]
        setup_subprocess.run(
            [
                setup_sys.executable,
                "-m",
                "pip",
                "install",
                "--quiet",
                "--disable-pip-version-check",
                *packages_to_install,
            ],
            check=True,
        )
        setup_importlib.invalidate_caches()

    setup_repo = SetupPath(
        setup_os.getenv("COURSE_COLAB_ROOT", "/content/GenAI_Soc2026")
    )
    if not setup_repo.exists():
        setup_subprocess.run(
            [
                "git",
                "clone",
                "--depth",
                "1",
                "https://github.com/cjbarrie/GenAI_Soc2026.git",
                str(setup_repo),
            ],
            check=True,
        )
    COURSE_ROOT = setup_repo
    setup_os.chdir(COURSE_ROOT / "workbook" / SESSION)
else:
    COURSE_ROOT = SetupPath.cwd()
    while not (COURSE_ROOT / "config" / "course_models.json").exists() and COURSE_ROOT != COURSE_ROOT.parent:
        COURSE_ROOT = COURSE_ROOT.parent
    if missing_packages:
        missing_text = ", ".join(missing_packages)
        raise ModuleNotFoundError(
            f"This notebook is using a Python environment without: {missing_text}.\n\n"
            "Close Jupyter. Open a terminal in the GenAI_Soc2026 repository and run:\n"
            "    uv sync\n"
            "    uv run jupyter lab\n\n"
            "In VS Code, select the Python interpreter inside the repository's .venv folder."
        )
    if not (COURSE_ROOT / "config" / "course_models.json").exists():
        raise FileNotFoundError(
            "The complete GenAI_Soc2026 repository could not be found. A notebook "
            "downloaded by itself is not enough for local work. Download or clone the "
            "repository, open a terminal in that folder, and run: uv run jupyter lab"
        )

course_root_text = str(COURSE_ROOT)
if course_root_text not in setup_sys.path:
    setup_sys.path.insert(0, course_root_text)

still_missing = [
    package_name
    for package_name in course_packages
    if setup_importlib_util.find_spec(package_name) is None
]
if still_missing:
    raise ModuleNotFoundError(
        "Setup did not make these packages available: " + ", ".join(still_missing)
    )

print("Environment:", "Google Colab" if IN_COLAB else "local course environment")
print("Python executable:", setup_sys.executable)
print("Course root:", COURSE_ROOT)
print("Working folder:", SetupPath.cwd())
print("OpenRouter SDK: ready")
print("Ollama Python SDK: ready")
if IN_COLAB:
    print("Ollama model call: skipped here; run it from local JupyterLab")
else:
    import json as setup_json
    import ollama as setup_ollama

    setup_config = setup_json.loads(
        (COURSE_ROOT / "config" / "course_models.json").read_text()
    )
    setup_local_model = setup_config["local"]["model"]
    try:
        setup_models = setup_ollama.list().models
        setup_model_names = [
            getattr(item, "model", None) or getattr(item, "name", None)
            for item in setup_models
        ]
        print("Ollama server: reachable at localhost:11434")
        if setup_local_model in setup_model_names:
            print("Course local model: ready —", setup_local_model)
        else:
            print("Course local model: NOT INSTALLED —", setup_local_model)
            print("NEXT STEP: open a terminal and run: ollama pull " + setup_local_model)
    except Exception as setup_error:
        print("Ollama server: NOT REACHABLE")
        print("NEXT STEP: start the Ollama application, then run: ollama list")
        print("Diagnostic:", str(setup_error).splitlines()[0])
'''


def load_notebook(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_notebook(path: Path, notebook: dict) -> None:
    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            source = "".join(cell["source"])
            if "ollama.chat(" in source and "ollama.chat(think=False," not in source:
                cell["source"] = lines(
                    source.replace("ollama.chat(", "ollama.chat(think=False, ")
                )
    path.write_text(json.dumps(notebook, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def repair_week1() -> None:
    path = ROOT / "workbook/session01/session01_research_technology.ipynb"
    notebook = load_notebook(path)
    cells = notebook["cells"]
    assert "Open In Colab" in "".join(cells[1]["source"])
    cells[1]["source"] = lines(
        """
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cjbarrie/GenAI_Soc2026/blob/main/workbook/session01/session01_research_technology.ipynb)

Run the setup cell immediately below before doing anything else. Colab supports the OpenRouter call. The Ollama call is completed in local JupyterLab or VS Code because Colab cannot reach the Ollama server on your computer.
"""
    )
    cells[2]["cell_type"] = "markdown"
    cells[2].pop("execution_count", None)
    cells[2].pop("outputs", None)
    cells[2]["source"] = lines(SETUP_MARKDOWN)
    cells[3]["cell_type"] = "code"
    cells[3]["execution_count"] = None
    cells[3]["outputs"] = []
    cells[3]["source"] = lines('SESSION = "session01"\n' + SETUP_CODE)
    cells[10]["source"] = lines(
        '''
if IN_COLAB:
    local_response = None
    local_message = None
    local_answer = None
    print("Ollama was not called: Colab cannot reach the local Ollama server.")
else:
    local_response = ollama.chat(
        model=LOCAL_MODEL,
        messages=messages,
        options={"temperature": 0},
    )
    local_message = local_response.message
    local_answer = local_message.content.strip()
    print("Ollama raw text:", local_answer)
'''
    )
    cells[16]["source"] = lines(
        '''
hosted_character_count = len(hosted_answer)
local_character_count = None if local_answer is None else len(local_answer)
routes_match = None if local_answer is None else hosted_answer == local_answer

print("hosted character count:", hosted_character_count)
print("count type:", type(hosted_character_count))
print("routes returned identical text:", routes_match)
print("comparison type:", type(routes_match))
'''
    )
    cells[19]["source"] = lines(
        """
## Methodological check

The two scores are proposed measurements. Neither route establishes that the score matches the intended construct or a defensible human codebook. If `local_answer` is `None`, that means the local route was deliberately not run in Colab; it is not a model response.

## Completion recording

Run both routes on the original statement and on `You cannot be too careful in dealing with people.` In the narrated recording, explain every string, the message list, where each inference runs, each returned object and each research record. Finish by explaining why either score still needs validation.

Explain every input and output aloud. Never show the shared key. If you began in Colab, complete the Ollama portion locally or on the in-class machine.
"""
    )
    save_notebook(path, notebook)


def repair_week2() -> None:
    path = ROOT / "workbook/session02/session02_annotation_measurement.ipynb"
    notebook = load_notebook(path)
    cells = notebook["cells"]
    assert "Open In Colab" in "".join(cells[1]["source"])
    cells[1]["source"] = lines(
        """
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cjbarrie/GenAI_Soc2026/blob/main/workbook/session02/session02_annotation_measurement.ipynb)

Run the setup cell immediately below before doing anything else. Colab supports the OpenRouter call. The Ollama call is completed in local JupyterLab or VS Code because Colab cannot reach the Ollama server on your computer.
"""
    )
    cells[2]["cell_type"] = "markdown"
    cells[2].pop("execution_count", None)
    cells[2].pop("outputs", None)
    cells[2]["source"] = lines(SETUP_MARKDOWN)
    cells[3]["cell_type"] = "code"
    cells[3]["execution_count"] = None
    cells[3]["outputs"] = []
    cells[3]["source"] = lines('SESSION = "session02"\n' + SETUP_CODE)
    cells[12]["source"] = lines(
        '''
if IN_COLAB:
    local_response = None
    local_raw = None
    local_label = None
    print("Ollama was not called: Colab cannot reach the local Ollama server.")
else:
    local_response = ollama.chat(
        model=LOCAL_MODEL,
        messages=messages,
        options={"temperature": 0},
    )
    local_raw = local_response.message.content
    print("Ollama raw return:", local_raw)
    local_label = local_raw.strip().upper()
    print("Ollama label:", local_label)
'''
    )
    cells[14]["source"] = lines(
        '''
routes_agree = None if local_label is None else hosted_label == local_label
hosted_matches_human = hosted_label == human_label
local_matches_human = None if local_label is None else local_label == human_label
print("Routes agree:", routes_agree)
print("OpenRouter matches human label:", hosted_matches_human)
print("Ollama matches human label:", local_matches_human)

# ONE CHANGE: replace comment with
# "I oppose the rezoning proposal because it will displace tenants."
# Then rerun from the message-construction cell.
'''
    )
    cells[15]["source"] = lines(
        """
## Methodological check

Agreement between the routes is a reproducibility observation. Agreement with one human label is criterion evidence. Neither alone proves that the codebook measures the construct well. If an Ollama comparison prints `None`, that means the local route was deliberately not run in Colab; it is not disagreement between two models.

## Completion recording

Run both routes on the changed opposition comment. Explain the comment string, codebook dictionary, message list, `[0]`, each response path and all three comparisons. State whether disagreement is between routes, with the human reference, or both.

Explain every input and output aloud. Never show the shared key. If you began in Colab, complete the Ollama portion locally or on the in-class machine.
"""
    )
    save_notebook(path, notebook)


if __name__ == "__main__":
    repair_week1()
    repair_week2()
    print("Repaired Week 1 and Week 2 notebook setup and Colab branches.")
