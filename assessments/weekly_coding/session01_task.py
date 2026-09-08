"""Assessed dual-route routine. Run from the repository root."""

# CELL: Load the course settings and SDKs
import json
import os
from getpass import getpass
from pathlib import Path

try:
    import ollama
    from openrouter import OpenRouter
except ModuleNotFoundError as error:
    raise ModuleNotFoundError(
        "A course SDK is missing. Open a terminal in the complete GenAI_Soc2026 "
        "folder, run 'uv sync --frozen', then run this task with 'uv run python'."
    ) from error

ROOT = Path.cwd()
while not (ROOT / "config" / "course_models.json").exists() and ROOT != ROOT.parent:
    ROOT = ROOT.parent

if not (ROOT / "config" / "course_models.json").exists():
    raise FileNotFoundError(
        "The complete GenAI_Soc2026 repository could not be found. A task or "
        "notebook downloaded by itself is not enough for local work. Open a terminal "
        "in the complete course folder and run this file from there."
    )

config = json.loads((ROOT / "config" / "course_models.json").read_text())
HOSTED_MODEL = config["hosted"]["model"]
LOCAL_MODEL = config["local"]["model"]

if not os.getenv("OPENROUTER_API_KEY"):
    os.environ["OPENROUTER_API_KEY"] = getpass("OpenRouter course key (hidden): ")

print("Hosted model:", HOSTED_MODEL)
print("Local model:", LOCAL_MODEL)

# CELL: Store the research material and construct one shared message list
text = "Most people can be trusted."
instruction = "Score the statement for generalized social trust from 0 to 2. Return one integer."
prompt = instruction + "\n\nStatement: " + text
messages = [{"role": "user", "content": prompt}]

print("text:", text)
print("type(text):", type(text))
print("messages:", messages)
print("type(messages):", type(messages))

# CELL: Send the message list through OpenRouter and unpack its return
with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
    hosted_response = client.chat.send(
        model=HOSTED_MODEL,
        messages=messages,
        temperature=0,
    )

hosted_choice = hosted_response.choices[0]
hosted_message = hosted_choice.message
hosted_answer = hosted_message.content.strip()
print("OpenRouter raw text:", hosted_answer)

# CELL: Send the same message list through Ollama and unpack its return
local_response = ollama.chat(think=False, 
    model=LOCAL_MODEL,
    messages=messages,
    options={"temperature": 0},
)
local_message = local_response.message
local_answer = local_message.content.strip()
print("Ollama raw text:", local_answer)

# CELL: Use the request to learn strings, lists and dictionaries
first_message = messages[0]

print("text value:", text)
print("text type:", type(text))
print("messages value:", messages)
print("messages type:", type(messages))
print("number of messages:", len(messages))
print("first message:", first_message)
print("first message type:", type(first_message))
print("role field:", first_message["role"])
print("content field:", first_message["content"])

# CELL: Use the returns to learn objects, attributes and methods
hosted_choices = hosted_response.choices

print("hosted response type:", type(hosted_response))
print("hosted choices type:", type(hosted_choices))
print("first hosted choice type:", type(hosted_choice))
print("hosted message type:", type(hosted_message))
print("hosted answer type:", type(hosted_answer))

print("local response type:", type(local_response))
print("local message type:", type(local_message))
print("local answer type:", type(local_answer))

# CELL: Derive an integer and a Boolean from the returned strings
hosted_character_count = len(hosted_answer)
local_character_count = len(local_answer)
routes_match = hosted_answer == local_answer

print("hosted character count:", hosted_character_count)
print("count type:", type(hosted_character_count))
print("routes returned identical text:", routes_match)
print("comparison type:", type(routes_match))

# CELL: Preserve the two runs as separate research records
hosted_record = {
    "route": "openrouter",
    "model": HOSTED_MODEL,
    "input": text,
    "raw_output": hosted_answer,
}
local_record = {
    "route": "ollama",
    "model": LOCAL_MODEL,
    "input": text,
    "raw_output": local_answer,
}

research_records = [hosted_record, local_record]

print(hosted_record)
print(local_record)
print("record collection type:", type(research_records))
print("first recorded route:", research_records[0]["route"])

# ONE CHANGE: replace text with "You cannot be too careful in dealing with people."
# Then rerun every cell from the shared message list onward.
