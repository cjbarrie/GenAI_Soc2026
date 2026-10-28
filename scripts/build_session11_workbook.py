"""Build the Week 11 notebook from the canonical tested task."""

from pathlib import Path
import json

import nbformat as nbf

ROOT = Path(__file__).resolve().parents[1]
SOURCE_NOTEBOOK = ROOT / "workbook/session09/session09_llms_at_work.ipynb"
TASK = ROOT / "assessments/weekly_coding/session11_task.py"
OUTPUT = ROOT / "workbook/session11/session11_language_inequality.ipynb"

source_notebook = json.loads(SOURCE_NOTEBOOK.read_text())
setup_code = next(
    "".join(cell["source"])
    for cell in source_notebook["cells"]
    if cell["cell_type"] == "code" and "course_packages" in "".join(cell["source"])
).replace('SESSION = "session09"', 'SESSION = "session11"', 1)
setup_code = "# colab-setup\n" + setup_code

task = TASK.read_text()
imports_end = task.index("# These pairs come")
pairs_start = imports_end
recorded_start = task.index("# Recorded outputs")
function_start = task.index("def judge_utterance")
conditions_start = task.index("# Convert the three pair dictionaries")
comparison_start = task.index('print("\\nCOMPARISON TABLE")')

imports = task[:imports_end].replace('ROUTE = "ollama"  # In Colab, use "openrouter".', 'ROUTE = "openrouter" if IN_COLAB else "ollama"')
pairs_and_schema = task[pairs_start:recorded_start]
recorded = task[recorded_start:function_start]
function = task[function_start:conditions_start]
conditions = task[conditions_start:comparison_start]
comparison = task[comparison_start:]

notebook = nbf.v4.new_notebook()
notebook["metadata"] = {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python", "version": "3.11"},
}
notebook["cells"] = [
    nbf.v4.new_markdown_cell(
        "# Week 11 — Language, inequality and institutional power\n\n"
        "**Research task:** Compare one model's structured occupation choice for three published "
        "meaning-matched AAE and SAE pairs. This classroom routine is not a replication of "
        "Hofmann et al.'s probability-based audit.\n\n"
        "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]"
        "(https://colab.research.google.com/github/cjbarrie/GenAI_Soc2026/blob/main/"
        "workbook/session11/session11_language_inequality.ipynb)"
    ),
    nbf.v4.new_markdown_cell(
        "## Prepare the environment\n\nRun this cell first. Colab installs the two SDKs, clones the course repository and selects OpenRouter. Local JupyterLab checks the course environment and selects Ollama."
    ),
    nbf.v4.new_code_cell(setup_code),
    nbf.v4.new_markdown_cell(
        "## Import tools and select the route\n\nThe inputs are installed Python modules and the course model configuration. The output is a set of variables naming the selected models, route and recorded-return setting."
    ),
    nbf.v4.new_code_cell(imports),
    nbf.v4.new_markdown_cell(
        "## Store the published pairs and output schema\n\n`PAIRS` is a list of dictionaries. Each dictionary contains one identifier and two meaning-matched strings. `RESPONSE_SCHEMA` limits the returned occupation to the supplied list."
    ),
    nbf.v4.new_code_cell(pairs_and_schema),
    nbf.v4.new_markdown_cell(
        "## Recorded returns for the offline path\n\nThese dictionaries demonstrate the program without a live model. They are labelled teaching returns and must not be presented as empirical findings. Set `USE_RECORDED = True` temporarily if a live route is unavailable."
    ),
    nbf.v4.new_code_cell(recorded),
    nbf.v4.new_markdown_cell(
        "## Define one function\n\nThe function receives four strings, constructs one prompt, makes one visible route-specific call, prints the raw JSON, parses it and returns one result dictionary. Read the literal call below before generalizing the function."
    ),
    nbf.v4.new_code_cell(function),
    nbf.v4.new_markdown_cell(
        "## Build six conditions and run the first loop\n\nThe first iteration uses `talking`, `aae` and `they be talking`. The next iteration changes the variant and source text while the prompt template, occupation list, model and temperature remain fixed."
    ),
    nbf.v4.new_code_cell(conditions),
    nbf.v4.new_markdown_cell(
        "## Compare paired outputs\n\nThe Boolean field `different` reports whether the two variants received different occupation strings in this run. It does not explain the model's internal mechanism or establish an institutional effect."
    ),
    nbf.v4.new_code_cell(comparison),
    nbf.v4.new_markdown_cell(
        "## Your one change\n\nChange one predeclared model or route. Keep the texts, prompt, occupation list and temperature fixed. Trace one pair through both runs and explain the inputs, raw return, parsed dictionary and paired comparison."
    ),
]

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
nbf.write(notebook, OUTPUT)
print(OUTPUT)
