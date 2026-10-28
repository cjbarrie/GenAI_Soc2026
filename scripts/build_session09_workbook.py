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
        "# Week 9 — Work with an LLM assistant\n\n"
        "**Research task:** Review an unfamiliar mortgage-prediction analysis as a consultant. "
        "After the first model reply, choose whether to ask another question, consult the "
        "data-science team or write the client note. The exercise adapts the statistical task "
        "in Wiles et al. (2026).\n\n"
        "**Python introduced:** the first student-edited function, parameters, local variables, "
        "`return`, calling a function twice and an `if/elif` branch controlled by a worker choice."
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
        "This cell creates a dictionary of model results, the AI-written interpretation, the "
        "coaching instruction and a schema describing the six fields the model must return. "
        "Read the results and identify the questionable claims before running it."
    ),
    nbf.v4.new_code_cell(task_cells[1]),
    nbf.v4.new_markdown_cell(
        "## Define the function\n\n"
        "The function receives two values: the current message list and the selected route. It "
        "makes one visible route-specific call, prints the raw return, parses it and returns one "
        "reply-record dictionary. We use the same function again only if the worker asks another question."
    ),
    nbf.v4.new_code_cell(task_cells[2]),
    nbf.v4.new_markdown_cell(
        "## Ask for an initial review\n\n"
        "The input is one message list containing the evidence, questionable analysis and coach "
        "instruction. The output is a dictionary containing the raw and parsed reply plus three checks."
    ),
    nbf.v4.new_code_cell(task_cells[3]),
    nbf.v4.new_markdown_cell(
        "## Choose what happens next\n\n"
        "The worker now chooses among `ask_model_again`, `escalate_to_data_science` and "
        "`write_client_note`. The supplied path asks one follow-up question. The program appends "
        "the first reply and the worker's question to the conversation before calling the same function."
    ),
    nbf.v4.new_code_cell(task_cells[4]),
    nbf.v4.new_markdown_cell(
        "## Record the worker's final decision\n\n"
        "Inspect the second reply, select one final action and state your reason. The resulting "
        "`work_record` preserves the model replies and the choices made by the worker."
    ),
    nbf.v4.new_code_cell(task_cells[5]),
    nbf.v4.new_markdown_cell(
        "## Reflect on the work\n\n"
        "Use these questions to distinguish work performed by the model from reasoning and choices "
        "retained by the consultant. Also consider what the stored interaction makes visible to the organization."
    ),
    nbf.v4.new_code_cell(task_cells[6]),
    nbf.v4.new_markdown_cell(
        "## A short unassisted check\n\n"
        "Answer this question yourself before asking a model. It mirrors the distinction in "
        "Wiles et al. between completing work with ChatGPT and demonstrating knowledge without it."
    ),
    nbf.v4.new_code_cell(task_cells[7]),
    nbf.v4.new_markdown_cell(
        "## Your one change and recording\n\n"
        "Change `worker_next_step` or rewrite `follow_up_question`, rerun and explain every input "
        "and output. Explain why you made the final decision and what the second model call did to "
        "the nature of your work. A passing software check is not evidence about real workers."
    ),
]

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
nbf.write(notebook, OUTPUT)
print(OUTPUT)
