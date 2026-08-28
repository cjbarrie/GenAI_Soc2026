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

# CELL: Choose a route and construct the opening interview history
ROUTE = "ollama"  # change to "openrouter" if preferred
interview_messages = [
    {"role": "system", "content": (
        "Conduct a sociological interview. Ask one short follow-up about a concrete "
        "episode. Do not suggest a cause or put words in the participant's mouth."
    )},
    {"role": "user", "content": (
        "Participant: I spoke after the professor invited me to respond."
    )},
]
print(interview_messages)

# CELL: Make the first call through the selected route
if ROUTE == "openrouter":
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        first_response = client.chat.send(
            model=HOSTED_MODEL, messages=interview_messages, temperature=0,
        )
    first_raw = first_response.choices[0].message.content
else:
    first_response = ollama.chat(
        model=LOCAL_MODEL, messages=interview_messages,
        options={"temperature": 0},
    )
    first_raw = first_response.message.content
print("First raw return:", first_raw)
first_probe = first_raw.strip()
print("First probe:", first_probe)

# CELL: Append the realized probe and a second participant answer
interview_messages.append({"role": "assistant", "content": first_probe})
second_answer = "Participant: I felt safer because she made room for me to speak."
interview_messages.append({"role": "user", "content": second_answer})
print("Messages before second call:", len(interview_messages))
print(interview_messages)

# CELL: Make the second call with the expanded history
if ROUTE == "openrouter":
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        second_response = client.chat.send(
            model=HOSTED_MODEL, messages=interview_messages, temperature=0,
        )
    second_raw = second_response.choices[0].message.content
else:
    second_response = ollama.chat(
        model=LOCAL_MODEL, messages=interview_messages,
        options={"temperature": 0},
    )
    second_raw = second_response.message.content
print("Second raw return:", second_raw)
second_probe = second_raw.strip()
print("Second probe:", second_probe)

# ONE CHANGE: replace second_answer with
# "Participant: I spoke when there was a pause." and rerun from append onward.
