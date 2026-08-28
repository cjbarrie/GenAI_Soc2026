"""Assessed dual-route routine. Run from the repository root."""

# CELL: Load the course settings and SDKs
import json
import os
from getpass import getpass
from pathlib import Path

import ollama
from openrouter import OpenRouter

ROOT = Path.cwd()
while not (ROOT / "config" / "course_models.json").exists() and ROOT != ROOT.parent:
    ROOT = ROOT.parent

config = json.loads((ROOT / "config" / "course_models.json").read_text())
HOSTED_MODEL = config["hosted"]["model"]
LOCAL_MODEL = config["local"]["model"]

if not os.getenv("OPENROUTER_API_KEY"):
    os.environ["OPENROUTER_API_KEY"] = getpass("OpenRouter course key (hidden): ")

print("Hosted model:", HOSTED_MODEL)
print("Local model:", LOCAL_MODEL)

# CELL: Choose a route and store one deidentified profile and survey item
ROUTE = "ollama"  # change to "openrouter" if preferred
profile = {
    "age_group": "30–44",
    "education": "bachelor's degree",
    "region": "South",
    "party_identification": "independent",
}
question = "On a scale from 1 (very liberal) to 7 (very conservative), where would you place yourself?"
held_out_human_answer = 4
print(profile)
print(question)

# CELL: Define the exact output structure
schema = {
    "type": "object",
    "properties": {
        "predicted_category": {"type": "integer", "minimum": 1, "maximum": 7},
        "probabilities": {
            "type": "array", "items": {"type": "number"},
            "minItems": 7, "maxItems": 7,
        },
    },
    "required": ["predicted_category", "probabilities"],
    "additionalProperties": False,
}
prompt = (
    "Predict this deidentified respondent's answer. Return seven probabilities in "
    "order from 1 to 7. Profile: " + json.dumps(profile) + " Item: " + question
)
messages = [{"role": "user", "content": prompt}]

# CELL: Make the selected structured-output call
if ROUTE == "openrouter":
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        response = client.chat.send(
            model=HOSTED_MODEL, messages=messages, temperature=0,
            response_format={"type": "json_schema", "json_schema": {
                "name": "polviews_prediction", "strict": True, "schema": schema,
            }},
        )
    raw_output = response.choices[0].message.content
else:
    response = ollama.chat(
        model=LOCAL_MODEL, messages=messages, format=schema,
        options={"temperature": 0},
    )
    raw_output = response.message.content
print("Raw JSON text:", raw_output)

# CELL: Parse, check structure and only then compare with the held-out answer
prediction = json.loads(raw_output)
probabilities = prediction["probabilities"]
seven_values = len(probabilities) == 7
sum_is_close = abs(sum(probabilities) - 1.0) < 0.02
matches_human = prediction["predicted_category"] == held_out_human_answer
print("Predicted category:", prediction["predicted_category"])
print("Seven probabilities:", seven_values)
print("Sum close to one:", sum_is_close)
print("Held-out human answer:", held_out_human_answer)
print("Exact match:", matches_human)

# ONE CHANGE: change age_group to "18–29" and rerun.
