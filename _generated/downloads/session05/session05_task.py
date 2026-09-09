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

# CELL: Choose a route and store the fixed facts and changing frame
import time

ROUTE = "ollama"  # change to "openrouter" if preferred
shared_facts = (
    "The proposal would create a pathway to permanent legal status for undocumented "
    "immigrants who meet residency and background-check requirements."
)
frame = "rights"
temperature = 0.7
max_tokens = 140

# CELL: Construct the prompt with an f-string
prompt = (
    f"Write one 70–90 word survey message using a {frame} frame. "
    f"Use only these facts and return only the message:\n\n{shared_facts}"
)
messages = [{"role": "user", "content": prompt}]
print(prompt)

# CELL: Make one timed call and preserve route-specific metadata
started = time.perf_counter()
if ROUTE == "openrouter":
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        response = client.chat.send(
            model=HOSTED_MODEL, messages=messages,
            temperature=temperature, max_tokens=max_tokens,
        )
    raw_output = response.choices[0].message.content
    input_tokens = getattr(response.usage, "prompt_tokens", None)
    output_tokens = getattr(response.usage, "completion_tokens", None)
else:
    response = ollama.chat(think=False, 
        model=LOCAL_MODEL, messages=messages,
        options={"temperature": temperature, "num_predict": max_tokens},
    )
    raw_output = response.message.content
    input_tokens = response.prompt_eval_count
    output_tokens = response.eval_count
latency_seconds = round(time.perf_counter() - started, 2)

print("Raw candidate:", raw_output.strip())
print("Input tokens:", input_tokens)
print("Output tokens:", output_tokens)
print("Latency seconds:", latency_seconds)

# CELL: Save the design settings beside the candidate
candidate_record = {
    "route": ROUTE,
    "frame": frame,
    "shared_facts": shared_facts,
    "temperature": temperature,
    "max_tokens": max_tokens,
    "raw_output": raw_output.strip(),
}
print(candidate_record)

# ONE CHANGE: change frame from "rights" to "economics" and nothing else.
