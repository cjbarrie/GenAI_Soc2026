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

# CELL: Load the supplied image transport utility and identify two frames
from src.genai_soc.media import image_to_data_url

ROUTE = "ollama"  # change to "openrouter" if preferred
frame_1 = ROOT / "slides" / "session04" / "images" / "zidane_fine2_168.png"
frame_2 = ROOT / "slides" / "session04" / "images" / "zidane_fine2_169.png"
timestamps = ["00:00", "00:01"]
print(frame_1)
print(frame_2)
print("Both files exist:", frame_1.exists() and frame_2.exists())

# CELL: State the evidentiary boundary and the required JSON fields
prompt = (
    "Compare these ordered frames. Describe only visible change. Do not name people, "
    "infer motive, or use remembered event knowledge. Return JSON with exactly "
    "observable_change, visible_evidence, and interpretation_withheld."
)
schema = {
    "type": "object",
    "properties": {
        "observable_change": {"type": "string"},
        "visible_evidence": {"type": "array", "items": {"type": "string"}},
        "interpretation_withheld": {"type": "string"},
    },
    "required": ["observable_change", "visible_evidence", "interpretation_withheld"],
    "additionalProperties": False,
}

# CELL: Send the images through the selected route
if ROUTE == "openrouter":
    content = [
        {"type": "text", "text": prompt},
        {"type": "image_url", "image_url": {"url": image_to_data_url(frame_1)}},
        {"type": "image_url", "image_url": {"url": image_to_data_url(frame_2)}},
    ]
    messages = [{"role": "user", "content": content}]
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        response = client.chat.send(
            model=HOSTED_MODEL, messages=messages, temperature=0,
            response_format={"type": "json_schema", "json_schema": {
                "name": "visible_sequence", "strict": True, "schema": schema,
            }},
        )
    raw_output = response.choices[0].message.content
else:
    messages = [{
        "role": "user", "content": prompt,
        "images": [str(frame_1), str(frame_2)],
    }]
    response = ollama.chat(
        model=LOCAL_MODEL, messages=messages, format=schema,
        options={"temperature": 0},
    )
    raw_output = response.message.content

print("Raw JSON text:", raw_output)

# CELL: Parse the three fields and compare them with the images
description = json.loads(raw_output)
print("Observable change:", description["observable_change"])
print("Visible evidence:", description["visible_evidence"])
print("Interpretation withheld:", description["interpretation_withheld"])

# ONE CHANGE: replace frame_2 with zidane_fine2_170.png and rerun.
