"""Build the Week 9 notebook from the canonical task and tested setup cell."""

from pathlib import Path
import json
import re

import nbformat as nbf

ROOT = Path(__file__).resolve().parents[1]
SOURCE_NOTEBOOK = ROOT / "workbook/session08/session08_opinion_prediction.ipynb"
TASK = ROOT / "assessments/weekly_coding/session09_task.py"
OUTPUT = ROOT / "workbook/session09/session09_llms_at_work.ipynb"

source = json.loads(SOURCE_NOTEBOOK.read_text())
setup_code = next(
    "".join(cell["source"])
    for cell in source["cells"]
    if cell["cell_type"] == "code" and "course_packages" in "".join(cell["source"])
).replace('SESSION = "session08"', 'SESSION = "session09"', 1)

task_text = TASK.read_text()
task_cells = [part.strip() for part in re.split(r"(?m)^# CELL:.*$", task_text)[1:]]
task_cells[1] = task_cells[1].replace(
    'ROUTE = "ollama"  # change to "openrouter" to use the hosted route',
    'ROUTE = "openrouter" if IN_COLAB else "ollama"  # local default',
    1,
)

notebook = nbf.v4.new_notebook()
notebook["metadata"] = {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python", "version": "3.11"},
}
setup_cell = nbf.v4.new_code_cell(setup_code)
setup_cell["id"] = "colab-setup"

notebook["cells"] = [
    nbf.v4.new_markdown_cell(
        "# Week 9 — Configure an LLM assistant at work\n\n"
        "**Research task:** Compare draft and coach assistance for the same customer-support case. "
        "The exercise separates a model output from claims about worker performance, knowledge, discretion or authority.\n\n"
        "**Python introduced:** the first student-edited function, parameters, local variables, "
        "`return`, and calling the same function with one changed argument."
    ),
    nbf.v4.new_markdown_cell(
        "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]"
        "(https://colab.research.google.com/github/cjbarrie/GenAI_Soc2026/blob/main/"
        "workbook/session09/session09_llms_at_work.ipynb)\n\n"
        "Run the setup cell below before anything else. Colab uses OpenRouter. Local JupyterLab "
        "uses Ollama by default."
    ),
    nbf.v4.new_markdown_cell(
        "## Prepare the notebook environment\n\n"
        "The next cell installs missing SDKs in Colab. Locally it checks that Jupyter is using "
        "the course environment and prints the exact repair command if necessary."
    ),
    setup_cell,
    nbf.v4.new_code_cell(task_cells[0]),
    nbf.v4.new_markdown_cell(
        "## Store the exact research material\n\n"
        "This cell creates two strings, one route string and a dictionary describing the six "
        "fields the model must return. Read the customer message and policy before running it."
    ),
    nbf.v4.new_code_cell(task_cells[1]),
    nbf.v4.new_markdown_cell(
        "## Define the function\n\n"
        "Replace the four parameter names mentally with the current values before running. "
        "The function builds the prompt, makes one visible route-specific call, prints the raw "
        "return, parses it and returns one record dictionary."
    ),
    nbf.v4.new_code_cell(task_cells[2]),
    nbf.v4.new_markdown_cell(
        "## Run draft mode\n\n"
        "Input: customer message (`str`), policy (`str`), mode (`str`) and route (`str`). "
        "Output: a record (`dict`) containing the raw and parsed returns plus four checks."
    ),
    nbf.v4.new_code_cell(task_cells[3]),
    nbf.v4.new_markdown_cell(
        "## Change one argument\n\n"
        "The final call keeps the customer, policy, route and model fixed. It changes only "
        "`assistance_mode` from `draft` to `coach`. Compare the two returned dictionaries."
    ),
    nbf.v4.new_code_cell(task_cells[4]),
    nbf.v4.new_markdown_cell(
        "## Your one change and recording\n\n"
        "Revise one sentence in `mode_instruction`, rerun both modes and explain every input and "
        "output. State whether the model distinguished known facts, uncertainty, hardship "
        "escalation and refund authority. A passing software check is not evidence about real workers."
    ),
]

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
nbf.write(notebook, OUTPUT)
print(OUTPUT)
