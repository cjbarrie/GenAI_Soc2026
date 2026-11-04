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
        "## Store the fixed facts and two instructions",
        "The facts dictionary stays unchanged. The two strings allocate different work to the "
        "model. Recorded returns provide an outage fallback, not evidence about people.",
    ),
    (
        "## Define a function with a default Boolean parameter",
        "The first three parameters require values. `disclose_assistance=False` supplies a "
        "default Boolean when the caller omits that keyword argument.",
    ),
    (
        "## Compare two instructions",
        "Both calls use the same relationship and facts. Keyword arguments make each input "
        "visible at the call site.",
    ),
    (
        "## Repeat one instruction across relationships",
        "`enumerate(..., start=1)` returns a condition number and a relationship label on each "
        "iteration. The loop appends one record dictionary at a time.",
    ),
    (
        "## Make disclosure an explicit input",
        "The final keyword argument changes from its default `False` to `True`. The resulting "
        "text remains a generated message, not evidence of a recipient response.",
    ),
    (
        "## Keep researcher notes separate",
        "Write observations after inspecting the text. Do not ask the model to score sincerity, "
        "appropriateness or relationship quality.",
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
        "# Week 10 — LLM-mediated interpersonal messages\n\n"
        "**Research task:** Hold a broken commitment fixed while changing the writing "
        "instruction, relationship and assistance-disclosure setting. Inspect generated "
        "writing without claiming to observe sincerity or relationship repair.\n\n"
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
        "## Your change and recording\n\nChange one relationship description or set "
        "`disclose_assistance=True` for another relationship. Explain the default value, the "
        "keyword argument, the first `enumerate()` iteration and the returned record. State "
        "which human outcomes remain unobserved."
    )
)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
nbf.write(notebook, OUTPUT)
print(OUTPUT)
