"""Build the Week 11 notebook from the canonical task and tested setup cell."""

from pathlib import Path
import json
import re

import nbformat as nbf

ROOT = Path(__file__).resolve().parents[1]
SOURCE_NOTEBOOK = ROOT / "workbook/session10/session10_relationship_mediation.ipynb"
TASK = ROOT / "assessments/weekly_coding/session11_task.py"
OUTPUT = ROOT / "workbook/session11/session11_language_inequality.ipynb"

source = json.loads(SOURCE_NOTEBOOK.read_text())
setup_code = next(
    "".join(cell["source"])
    for cell in source["cells"]
    if cell["cell_type"] == "code" and "course_packages" in "".join(cell["source"])
).replace('SESSION = "session10"', 'SESSION = "session11"', 1)

task_text = TASK.read_text()
task_cells = [part.strip() for part in re.split(r"(?m)^# CELL:.*$", task_text)[1:]]
task_cells[0] = task_cells[0].replace(
    'ROUTE = "ollama"  # In Colab, use "openrouter".',
    'ROUTE = "openrouter" if IN_COLAB else "ollama"',
    1,
)

headings = [
    (
        "## Import tools and select the route",
        "The cell locates the complete repository and names the selected route and model. "
        "The recorded-return path supports tracing during an outage.",
    ),
    (
        "## Store the published pairs and output schema",
        "Each dictionary contains one identifier and two meaning-matched strings. The schema "
        "limits the forced occupation choice to the same list for every condition.",
    ),
    (
        "## Define the model-call function",
        "This function reuses ideas from Weeks 9 and 10. The new lesson comes after the calls: "
        "how to preserve the paired design in Python.",
    ),
    (
        "## Create two ordered result lists",
        "Each source pair contributes one AAE result and one SAE result in the same position. "
        "The ordering becomes important when the lists are paired.",
    ),
    (
        "## Pair records with zip and count differences",
        "`zip()` supplies one item from each list. Tuple unpacking names those two items. "
        "`+=` updates the running count when a forced occupation choice differs.",
    ),
    (
        "## State the interpretation boundary",
        "The code reports what happened for three pairs in one run. It does not estimate a "
        "stable disparity or measure an institutional consequence for a person.",
    ),
]

notebook = nbf.v4.new_notebook()
notebook["metadata"] = {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python", "version": "3.11"},
}
setup_cell = nbf.v4.new_code_cell(setup_code)
setup_cell["id"] = "colab-setup"

notebook["cells"] = [
    nbf.v4.new_markdown_cell(
        "# Week 11 — Language, inequality and institutional power\n\n"
        "**Research task:** Compare one model's forced occupation choice for three "
        "published meaning-matched AAE and SAE pairs. This classroom routine is not a "
        "replication of Hofmann et al.'s probability-based audit.\n\n"
        "**Python introduced:** `zip()`, tuple unpacking and a running counter with `+=`.\n\n"
        "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]"
        "(https://colab.research.google.com/github/cjbarrie/GenAI_Soc2026/blob/main/"
        "workbook/session11/session11_language_inequality.ipynb)"
    ),
    nbf.v4.new_markdown_cell(
        "## Prepare the environment\n\nRun this cell first. Colab uses OpenRouter. "
        "Local JupyterLab uses Ollama by default."
    ),
    setup_cell,
]

for (heading, explanation), code in zip(headings, task_cells):
    notebook["cells"].append(nbf.v4.new_markdown_cell(f"{heading}\n\n{explanation}"))
    notebook["cells"].append(nbf.v4.new_code_cell(code))

notebook["cells"].append(
    nbf.v4.new_markdown_cell(
        "## Your change and recording\n\nChange one predeclared model or route while "
        "holding the texts, prompt, occupation list and temperature fixed. Trace one pair "
        "through `zip()`, explain the running counter and state why the result does not "
        "establish a stable model-level or institutional effect."
    )
)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
nbf.write(notebook, OUTPUT)
print(OUTPUT)
