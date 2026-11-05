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
        "# Week 9 — Human judgment and model certainty\n\n"
        "**Research task:** Inspect one model recommendation while its displayed certainty "
        "changes from 0.55 to 0.75 to 0.95. The evidence and recommendation remain fixed. "
        "Record whether the certainty display changes your decision.\n\n"
        "**Python introduced:** the first small student-edited function, parameters, local "
        "variables, `return` and an `if/elif/else` branch controlled by a human choice."
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
        "## Store the workplace decision and evidence\n\n"
        "The consultant must advise on a limited internal pilot. The dictionary contains the "
        "only evidence available to the model. It does not contain calibration, subgroup results "
        "or information about the costs of different errors."
    ),
    nbf.v4.new_code_cell(task_cells[1]),
    nbf.v4.new_markdown_cell(
        "## Ask the model for one recommendation\n\n"
        "This cell makes the only model call. It prints the raw JSON string before parsing it. "
        "The same parsed recommendation will appear beside all three certainty displays."
    ),
    nbf.v4.new_code_cell(task_cells[2]),
    nbf.v4.new_markdown_cell(
        "## Store three displays of the same advice\n\n"
        "Edit the human actions and reasons so that they reflect what you would do. The certainty "
        "values change, but the evidence and recommendation do not."
    ),
    nbf.v4.new_code_cell(task_cells[3]),
    nbf.v4.new_markdown_cell(
        "## Define the first small function\n\n"
        "The function receives a recommendation, displayed certainty, human action and human "
        "reason. Its branch translates the selected action into an organizational next step."
    ),
    nbf.v4.new_code_cell(task_cells[4]),
    nbf.v4.new_markdown_cell(
        "## Record one decision at each certainty level\n\n"
        "The loop takes the action and reason at the same list position as the current certainty. "
        "The function returns one judgment dictionary, which is appended to the results list."
    ),
    nbf.v4.new_code_cell(task_cells[5]),
    nbf.v4.new_markdown_cell(
        "## Compare the worker's decisions\n\n"
        "This cell prints all three records and verifies that the evidence and recommendation "
        "remained unchanged. Any difference in the action therefore requires a human explanation."
    ),
    nbf.v4.new_code_cell(task_cells[6]),
    nbf.v4.new_markdown_cell(
        "## Reflect on judgment and organizational visibility\n\n"
        "The questions connect reliance on the recommendation to Barley, Zuboff and Wiles et al."
    ),
    nbf.v4.new_code_cell(task_cells[7]),
    nbf.v4.new_markdown_cell(
        "## A short unassisted check\n\n"
        "Answer this without asking the model. A displayed certainty value has no frequency "
        "interpretation unless someone has validated how that number relates to outcomes."
    ),
    nbf.v4.new_code_cell(task_cells[8]),
    nbf.v4.new_markdown_cell(
        "## Your one change and recording\n\n"
        "Change one action or reason, rerun and explain the function inputs, branch and returned "
        "record. State whether certainty language changed your judgment despite unchanged evidence."
    ),
]

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
nbf.write(notebook, OUTPUT)
print(OUTPUT)
