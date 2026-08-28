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

# CELL: Choose a route and load an instructor-authored original trajectory
ROUTE = "ollama"
original_trajectory = [
    {"stage":"plan","raw_output":"Search for evidence about replication records."},
    {"stage":"inspect","raw_output":"The source names prompts, models, settings and outputs."},
    {"stage":"write","raw_output":"Replication requires preserving the model-dependent research record."},
]
stages = ["plan", "inspect", "write"]
research_question = "What must be saved to understand a changed LLM-assisted result?"

# CELL: Run at most three model calls and preserve every event
rerun_trajectory = []
for stage in stages:
    prompt = (
        "Stage: " + stage + ". Research question: " + research_question +
        ". Produce one sentence. Prior events: " + json.dumps(rerun_trajectory)
    )
    messages = [{"role":"user","content":prompt}]
    if ROUTE == "openrouter":
        with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
            response = client.chat.send(model=HOSTED_MODEL,messages=messages,temperature=0,max_tokens=80)
        raw_output = response.choices[0].message.content.strip()
    else:
        response = ollama.chat(model=LOCAL_MODEL,messages=messages,options={"temperature":0,"num_predict":80})
        raw_output = response.message.content.strip()
    event = {"stage":stage,"route":ROUTE,"prompt":prompt,"raw_output":raw_output}
    rerun_trajectory.append(event)
    print("Saved event:", event)

# CELL: Write the rerun record to a clearly scoped student-output folder
output_dir = ROOT / "student_outputs"
output_dir.mkdir(exist_ok=True)
output_path = output_dir / "week12_rerun.json"
output_path.write_text(json.dumps(rerun_trajectory, indent=2))
print("Saved to:", output_path)

# CELL: Compare the original and rerun stage by stage
discrepancies = []
for original, rerun in zip(original_trajectory, rerun_trajectory):
    same_stage = original["stage"] == rerun["stage"]
    same_output = original["raw_output"] == rerun["raw_output"]
    discrepancies.append({"stage":rerun["stage"],"same_stage":same_stage,"same_output":same_output})
print(discrepancies)

# ONE CHANGE: change temperature from 0 to 0.7 in the selected route and rerun.
