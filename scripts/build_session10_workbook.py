"""Build the Week 10 notebook from the canonical task and tested setup cell."""

from pathlib import Path
import json
import re

import nbformat as nbf

ROOT = Path(__file__).resolve().parents[1]
SOURCE_NOTEBOOK = ROOT / "workbook/session09/session09_llms_at_work.ipynb"
TASK = ROOT / "assessments/weekly_coding/session10_task.py"
OUTPUT = ROOT / "workbook/session10/session10_relationship_mediation.ipynb"

source = json.loads(SOURCE_NOTEBOOK.read_text())
setup_code = next(
    "".join(cell["source"])
    for cell in source["cells"]
    if cell["cell_type"] == "code" and "course_packages" in "".join(cell["source"])
).replace('SESSION = "session09"', 'SESSION = "session10"', 1)

task_text = TASK.read_text()
task_cells = [part.strip() for part in re.split(r"(?m)^# CELL:.*$", task_text)[1:]]
task_cells[0] = task_cells[0].replace(
    'ROUTE = "ollama"  # use "openrouter" for the hosted route',
    'ROUTE = "openrouter" if IN_COLAB else "ollama"',
    1,
)

headings = [
    (
        "## Import tools and store the course models",
        "This cell locates the complete repository and selects the hosted and local models. "
        "Colab uses OpenRouter; local JupyterLab uses Ollama by default.",
    ),
    (
        "## Store the social situations and your responses",
        "The three dictionaries describe different relationships and obligations. Edit at least "
        "one human response before viewing the model output. Your response is a comparison, not an answer key.",
    ),
    (
        "## Define the model-call function",
        "The function receives one situation dictionary and a route. It preserves the raw return "
        "before parsing the proposed action, possible message, reasoning and missing information.",
    ),
    (
        "## Generate advice for each situation",
        "`enumerate(..., start=1)` numbers the cases. The loop calls the same function once for "
        "each situation and appends one model record to the initially empty list.",
    ),
    (
        "## Store your audit judgments",
        "Read each model output before editing these values. Record whether you would follow it, "
        "the most important difference and what you would do after seeing the suggestion.",
    ),
    (
        "## Define a function with a default Boolean",
        "The audit function combines the situation, initial human response and model response. "
        "The default records that the student would not automatically follow the model.",
    ),
    (
        "## Build the audit dataset",
        "The loop retrieves objects from matching list positions and passes them as keyword "
        "arguments. Each returned audit dictionary is appended to `audit_records`.",
    ),
    (
        "## Interpret the audit cautiously",
        "The student response provides a situated comparison rather than a gold standard. The "
        "model outputs do not establish how a real writer or recipient would behave.",
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
        "# Week 10 — Auditing LLM advice about social situations\n\n"
        "**Research task:** Record how you would respond to three social situations before "
        "viewing model advice. Then audit how the model understands each relationship, "
        "obligation and possible response.\n\n"
        "**Python introduced:** default parameter values, Boolean values, keyword arguments "
        "and `enumerate()`.\n\n"
        "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]"
        "(https://colab.research.google.com/github/cjbarrie/GenAI_Soc2026/blob/main/"
        "workbook/session10/session10_relationship_mediation.ipynb)"
    ),
    nbf.v4.new_markdown_cell(
        "## Prepare the notebook environment\n\nRun this cell first. Colab installs the "
        "two SDKs and uses OpenRouter. Local JupyterLab checks the course environment and "
        "uses Ollama by default."
    ),
    setup_cell,
]

for (heading, explanation), code in zip(headings, task_cells):
    notebook["cells"].append(nbf.v4.new_markdown_cell(f"{heading}\n\n{explanation}"))
    notebook["cells"].append(nbf.v4.new_code_cell(code))

notebook["cells"].append(
    nbf.v4.new_markdown_cell(
        "## Your change and recording\n\nReplace at least one initial response and audit "
        "answer with your own judgment. Explain the default Boolean, keyword arguments, first "
        "`enumerate()` iteration and one complete audit record. State why your response is a "
        "comparison rather than a gold standard."
    )
)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
nbf.write(notebook, OUTPUT)
print(OUTPUT)
