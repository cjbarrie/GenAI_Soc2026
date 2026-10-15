"""Build the reviewed Week 7 notebook from the assessed script."""

from pathlib import Path

import nbformat as nbf


ROOT = Path(__file__).resolve().parents[1]
TASK = ROOT / "assessments" / "weekly_coding" / "session07_task.py"
OUTPUT = ROOT / "workbook" / "session07" / "session07_synthetic_representation.ipynb"


def markdown(text: str):
    return nbf.v4.new_markdown_cell(text.strip())


def code(text: str):
    return nbf.v4.new_code_cell(text.strip())


SETUP = r'''
SESSION = "session07"

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
    "matplotlib": "matplotlib>=3.10,<4",
}
missing_packages = [
    package_name
    for package_name in course_packages
    if setup_importlib_util.find_spec(package_name) is None
]

if IN_COLAB:
    if missing_packages:
        setup_subprocess.run(
            [
                setup_sys.executable,
                "-m",
                "pip",
                "install",
                "--quiet",
                "--disable-pip-version-check",
                *[course_packages[name] for name in missing_packages],
            ],
            check=True,
        )
        setup_importlib.invalidate_caches()

    COURSE_ROOT = SetupPath(
        setup_os.getenv("COURSE_COLAB_ROOT", "/content/GenAI_Soc2026")
    )
    if not COURSE_ROOT.exists():
        setup_subprocess.run(
            [
                "git",
                "clone",
                "--depth",
                "1",
                "https://github.com/cjbarrie/GenAI_Soc2026.git",
                str(COURSE_ROOT),
            ],
            check=True,
        )
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
            "The complete GenAI_Soc2026 repository could not be found. Download or "
            "clone the repository, open a terminal in that folder, and run: uv run jupyter lab"
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
print("Python SDKs: ready")
if IN_COLAB:
    print("Route for this runtime: OpenRouter")
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


EXPLANATIONS = {
    "Load the course settings and SDKs": (
        "## Load tools and choose a route\n\n"
        "**Input:** the course model configuration and, for OpenRouter, the hidden key. "
        "**Output:** two model-name strings and the selected route. The Colab version "
        "chooses OpenRouter automatically; local Jupyter defaults to Ollama."
    ),
    "Store one question and two persona dictionaries": (
        "## Store the question and two personas\n\n"
        "`question` is a string. `sparse_persona` and `rich_persona` are dictionaries. "
        "The `|` operator creates a new dictionary with two added attitude fields. "
        "The held-out human answer remains separate from every prompt."
    ),
    "Define one forced-choice schema and one probability schema": (
        "## Define the expected output structures\n\n"
        "The first schema permits one integer from 1 to 7. The second permits exactly "
        "seven numbers between 0 and 1. These are structure checks, not evidence that "
        "the values represent people."
    ),
    "Build the three prompts": (
        "## Build the prompt strings\n\n"
        "Read all three printed prompts. Conditions A and B use the same persona but "
        "request different outputs. Conditions B and C request the same output but use "
        "different persona information."
    ),
    "Condition A - sparse persona with a forced answer": (
        "## Condition A: one forced category\n\n"
        "**Input:** a one-item message list and the forced-choice schema. **Output:** "
        "`raw_forced`, a JSON-formatted string that is printed before parsing."
    ),
    "Condition B - sparse persona with seven probabilities": (
        "## Condition B: sparse-persona probabilities\n\n"
        "The persona matches Condition A. The model must now return a probability for "
        "every response category."
    ),
    "Condition C - richer persona with seven probabilities": (
        "## Condition C: richer-persona probabilities\n\n"
        "The requested output matches Condition B. The persona now includes two "
        "attitudinal statements."
    ),
    "Convert the three JSON strings into Python objects": (
        "## Parse the raw returns\n\n"
        "`json.loads(...)` turns each JSON string into a dictionary. Square brackets "
        "retrieve the integer or list stored under a named key."
    ),
    "Check the lists and calculate expected scores": (
        "## Check the lists and calculate expected scores\n\n"
        "`len` counts list entries, `sum` adds them and `[0]` through `[6]` retrieve "
        "the seven probabilities. The weighted sum gives an expected scale position."
    ),
    "Plot both probability distributions": (
        "## Plot both distributions\n\n"
        "The list `scale` supplies the x-values. Each probability list supplies one "
        "set of y-values. The vertical line shows the held-out human answer."
    ),
    "Compare the forced answer with the held-out answer": (
        "## Compare one forced answer\n\n"
        "The equality operator returns `True` or `False`. This evaluates one prediction "
        "for one observed case."
    ),
}


task_text = TASK.read_text(encoding="utf-8")
parts = task_text.split("# CELL: ")[1:]
task_cells = []
for part in parts:
    heading, body = part.split("\n", 1)
    if heading == "Load the course settings and SDKs":
        body = body.replace(
            'ROUTE = "ollama"  # change to "openrouter" if preferred',
            'ROUTE = "openrouter" if IN_COLAB else "ollama"',
        )
    task_cells.extend([markdown(EXPLANATIONS[heading]), code(body)])


setup_cell = code(SETUP)
setup_cell["id"] = "colab-setup"


cells = [
    markdown(
        """
        # Week 7 — How persona information and response format change a prediction

        We will run three explicit model calls: a forced answer from a sparse persona, a
        probability distribution from the same sparse persona, and a probability
        distribution from a richer persona. For every cell, identify the input, Python
        type, operation and output before moving on.
        """
    ),
    markdown(
        """
        [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cjbarrie/GenAI_Soc2026/blob/main/workbook/session07/session07_synthetic_representation.ipynb)

        Run the setup cell immediately below. Colab uses OpenRouter. Local Jupyter uses
        Ollama by default. Never show the shared key in your recording.
        """
    ),
    markdown(
        """
        ## Prepare the notebook environment

        In Colab, the next cell installs missing SDKs and downloads the public course
        repository. Locally, it checks that Jupyter is using the course environment and
        prints the exact repair command when something is missing.
        """
    ),
    setup_cell,
    *task_cells,
    markdown(
        """
        ## Completion task

        1. Run all three conditions and explain every call's input and output.
        2. Change exactly one value in `rich_persona`.
        3. Rebuild `rich_distribution_prompt` and rerun only Condition C.
        4. Recreate the plot and explain which probabilities moved.
        5. Explain the dictionary merge, JSON conversion, list indexing, `len`, `sum`
           and the plotted x and y values.
        6. State why the comparison is a prompt-sensitivity check rather than evidence
           that the personas represent a population.
        """
    ),
]

notebook = nbf.v4.new_notebook(cells=cells)
notebook.metadata.kernelspec = {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3",
}
notebook.metadata.language_info = {"name": "python", "version": "3"}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
nbf.write(notebook, OUTPUT)
print(f"Wrote {OUTPUT}")
