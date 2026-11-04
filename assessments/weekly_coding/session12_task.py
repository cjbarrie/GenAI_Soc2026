"""Optional project preparation for the cancelled 25 November class.

There is no Week 12 coding submission. This offline extension introduces file
I/O by saving and reopening one transparent model-call record. It makes no API
call and can be used while preparing a final-project proposal.
"""

import json
from pathlib import Path

# New Python idea: a Path object names a file without assuming one operating system.
output_directory = Path("student_outputs")
output_directory.mkdir(exist_ok=True)
record_path = output_directory / "project_model_call_record.json"

# Replace the example values with the planned routine for your own project.
project_record = {
    "research_question": "How does the wording of an apology vary by relationship?",
    "input_description": "One broken commitment and one relationship label",
    "model_route": "ollama",
    "model_name": "replace-with-the-model-you-plan-to-use",
    "prompt_version": "v1",
    "temperature": 0,
    "expected_output": "One generated message",
    "validation_evidence": "Researcher comparison against supplied facts",
}

# json.dumps returns a string. Path.write_text writes that string to disk.
json_text = json.dumps(project_record, indent=2)
record_path.write_text(json_text, encoding="utf-8")
print("Saved:", record_path.resolve())

# Path.read_text returns a string. json.loads turns it back into a dictionary.
reopened_text = record_path.read_text(encoding="utf-8")
reopened_record = json.loads(reopened_text)
print("Reopened type:", type(reopened_record))
print("Research question:", reopened_record["research_question"])

required_fields = [
    "research_question",
    "input_description",
    "model_route",
    "model_name",
    "prompt_version",
    "temperature",
    "expected_output",
    "validation_evidence",
]
missing_fields = []
for field in required_fields:
    if field not in reopened_record:
        missing_fields.append(field)

print("Missing fields:", missing_fields)
print("Record ready for proposal discussion:", len(missing_fields) == 0)

# OPTIONAL CHANGE: replace two fields with details from your proposal, save the
# file again and reopen it. There is no recording or submission for this week.
