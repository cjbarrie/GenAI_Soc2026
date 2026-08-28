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

# CELL: Define two routes, two prompt frames and one output schema
routes = ["openrouter", "ollama"]
frames = {
    "individual":"Evaluate the action in terms of individual choice.",
    "collective":"Evaluate the action in terms of collective obligation.",
}
scenario = "A worker declines an unpaid request to stay late."
schema = {"type":"object","properties":{"approval":{"type":"integer","minimum":0,"maximum":100},"explanation":{"type":"string"}},"required":["approval","explanation"],"additionalProperties":False}
audit_records = []

# CELL: Run every route-by-frame condition
for route in routes:
    for frame_name, frame_instruction in frames.items():
        prompt = frame_instruction + " Score approval from 0 to 100. Scenario: " + scenario
        messages = [{"role":"user","content":prompt}]
        if route == "openrouter":
            with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
                response = client.chat.send(model=HOSTED_MODEL,messages=messages,temperature=0,response_format={"type":"json_schema","json_schema":{"name":"audit_response","strict":True,"schema":schema}})
            raw_output = response.choices[0].message.content
            requested_model = HOSTED_MODEL
        else:
            response = ollama.chat(model=LOCAL_MODEL,messages=messages,format=schema,options={"temperature":0})
            raw_output = response.message.content
            requested_model = LOCAL_MODEL
        parsed = json.loads(raw_output)
        record = {"route":route,"model":requested_model,"frame":frame_name,"prompt":prompt,"raw_output":raw_output,"approval":parsed["approval"]}
        audit_records.append(record)
        print("Condition record:", record)

# CELL: Inspect the plain records before making a table
for record in audit_records:
    print(record["route"], record["frame"], record["approval"])

# CELL: Convert the already understood records into a small table
import pandas as pd
audit_table = pd.DataFrame(audit_records)
print(audit_table[["route","model","frame","approval"]])

# ONE CHANGE: replace "worker" with "manager" and rerun the complete grid.
