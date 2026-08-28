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

# CELL: Choose one route and store two identified excerpts
ROUTE = "ollama"  # change to "openrouter" if preferred
excerpts = [
    {"id": "e01", "text": "After several exchanges, I attended the tenants' meeting."},
    {"id": "e02", "text": "I accepted help but did not attend political meetings."},
]
print("Route:", ROUTE)
print("First excerpt:", excerpts[0])

# CELL: Convert the excerpts into prompt text and construct messages
prompt = (
    "Suggest one provisional theme. Return JSON with exactly theme, evidence_id, "
    "and question_for_researcher. Excerpts: " + json.dumps(excerpts)
)
messages = [{"role": "user", "content": prompt}]
print(prompt)

# CELL: Make the selected route's call without hiding either branch
if ROUTE == "openrouter":
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        response = client.chat.send(
            model=HOSTED_MODEL,
            messages=messages,
            temperature=0,
            response_format={"type": "json_object"},
        )
    raw_output = response.choices[0].message.content
else:
    response = ollama.chat(
        model=LOCAL_MODEL,
        messages=messages,
        format="json",
        options={"temperature": 0},
    )
    raw_output = response.message.content

print("Raw JSON text:", raw_output)

# CELL: Parse the JSON string and return to its cited source
suggestion = json.loads(raw_output)
evidence_id = suggestion["evidence_id"]
cited_excerpt = None
for excerpt in excerpts:
    if excerpt["id"] == evidence_id:
        cited_excerpt = excerpt

print("Theme:", suggestion["theme"])
print("Cited excerpt:", cited_excerpt)
print("Question:", suggestion["question_for_researcher"])

# ONE CHANGE: change e02 to
# "The food deliveries helped, but I avoided the group because meetings felt hostile."
