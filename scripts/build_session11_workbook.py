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
    ("## Load tools and select a route", "The script reads the two course model names. Colab selects OpenRouter; a local notebook selects Ollama."),
    ("## Store one fictional report", "The report and editing instruction are strings. The report contains no confidential business information."),
    ("## Ask the model for one edit", "The function shows the complete message, calls the chosen route, prints the raw return and keeps a record of the call."),
    ("## Check the revision", "Read the source and revision together. Preserve all five points, including that customer switching is unknown."),
    ("## Make the four conditions", "The outer loop selects one worker role. For each role, the inner loop selects each AI-use label. The same report goes into all four records."),
    ("## Inspect and check the materials", "The assertions verify the four-record structure and identical report text. Human readers would still be needed to measure evaluation."),
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
        "# Week 11 — AI use and judgments of competence\n\n"
        "**Research task:** Use an LLM to edit a fictional competitor report. "
        "Check the edit and use Python to prepare four conditions for a possible "
        "human-reader study.\n\n"
        "**Python introduced:** one nested loop that crosses two lists of conditions.\n\n"
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
        "## Your change and recording\n\nMake the editing instruction more conservative "
        "while keeping the source report fixed. Rerun and compare the raw revision. "
        "Then trace one complete pass through the outer and inner loops. Explain why "
        "the four materials cannot tell us what human readers would think about either worker."
    )
)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
nbf.write(notebook, OUTPUT)
print(OUTPUT)
