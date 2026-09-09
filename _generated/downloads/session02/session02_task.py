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

# CELL: Store one comment, the codebook and a human reference label
comment = "I support the plan if rents remain affordable."
codebook = {
    "SUPPORT": "unconditional support for the proposal",
    "OPPOSE": "unconditional opposition to the proposal",
    "UNCLEAR": "conditional, mixed, procedural, or insufficient evidence",
}
human_label = "UNCLEAR"
print(comment)
print(codebook["UNCLEAR"])

# CELL: Construct the exact message list used by both routes
prompt = (
    "Apply this codebook: " + json.dumps(codebook) +
    "\nReturn only SUPPORT, OPPOSE, or UNCLEAR.\nComment: " + comment
)
messages = [{"role": "user", "content": prompt}]
print(messages[0]["content"])

# CELL: Make and unpack the OpenRouter call
with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
    hosted_response = client.chat.send(
        model=HOSTED_MODEL, messages=messages, temperature=0,
    )
hosted_choice = hosted_response.choices[0]
hosted_raw = hosted_choice.message.content
print("OpenRouter raw return:", hosted_raw)
hosted_label = hosted_raw.strip().upper()
print("OpenRouter label:", hosted_label)

# CELL: Make and unpack the Ollama call
local_response = ollama.chat(think=False, 
    model=LOCAL_MODEL, messages=messages, options={"temperature": 0},
)
local_raw = local_response.message.content
print("Ollama raw return:", local_raw)
local_label = local_raw.strip().upper()
print("Ollama label:", local_label)

# CELL: Compare route agreement and human-reference agreement
routes_agree = hosted_label == local_label
hosted_matches_human = hosted_label == human_label
local_matches_human = local_label == human_label
print("Routes agree:", routes_agree)
print("OpenRouter matches human label:", hosted_matches_human)
print("Ollama matches human label:", local_matches_human)

# ONE CHANGE: replace comment with
# "I oppose the rezoning proposal because it will displace tenants."
# Then rerun from the message-construction cell.
