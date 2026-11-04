"""Build the optional Week 12 project-record notebook."""

from pathlib import Path

import nbformat as nbf

ROOT = Path(__file__).resolve().parents[1]
TASK = ROOT / "assessments/weekly_coding/session12_task.py"
OUTPUT = ROOT / "workbook/session12/session12_project_record.ipynb"

task = TASK.read_text()
notebook = nbf.v4.new_notebook()
notebook["metadata"] = {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python", "version": "3.11"},
}
notebook["cells"] = [
    nbf.v4.new_markdown_cell(
        "# Optional project preparation — save a model-call record\n\n"
        "The class on 25 November is cancelled. There is no Week 12 coding submission. "
        "This optional offline notebook introduces file paths, writing a JSON file and "
        "reading it back while preparing for the proposal meeting."
    ),
    nbf.v4.new_markdown_cell(
        "## Complete flow\n\n"
        "Python dictionary → JSON text → file path → saved file → reopened text → "
        "Python dictionary → missing-field check"
    ),
    nbf.v4.new_code_cell(task),
    nbf.v4.new_markdown_cell(
        "## Optional change\n\nReplace two example fields with details from your own "
        "proposal. Save and reopen the record. There is no recording or upload."
    ),
]

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
nbf.write(notebook, OUTPUT)
print(OUTPUT)
