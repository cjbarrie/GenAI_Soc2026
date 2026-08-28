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

# CELL: Store five deidentified teaching profiles and held-out answers
profiles = [
    {"id":"p01","age_group":"18–29","education":"some college","region":"Northeast","party":"Democrat","human_answer":2},
    {"id":"p02","age_group":"30–44","education":"bachelor's","region":"South","party":"Independent","human_answer":4},
    {"id":"p03","age_group":"45–64","education":"high school","region":"Midwest","party":"Republican","human_answer":6},
    {"id":"p04","age_group":"65+","education":"graduate","region":"West","party":"Democrat","human_answer":3},
    {"id":"p05","age_group":"30–44","education":"high school","region":"South","party":"Republican","human_answer":6},
]
question = "Place yourself from 1 (very liberal) to 7 (very conservative)."
schema = {
    "type":"object",
    "properties":{"predicted_category":{"type":"integer","minimum":1,"maximum":7}},
    "required":["predicted_category"],"additionalProperties":False,
}
print("Profiles:", len(profiles))

# CELL: Start two empty result lists
hosted_results = []
local_results = []
print(hosted_results)
print(local_results)

# CELL: Loop through the profiles and call both routes
for profile in profiles:
    # Build the model input explicitly. The held-out answer is not included.
    public_profile = {
        "age_group": profile["age_group"],
        "education": profile["education"],
        "region": profile["region"],
        "party": profile["party"],
    }
    prompt = "Predict the survey answer. Profile: " + json.dumps(public_profile) + " Item: " + question
    messages = [{"role":"user","content":prompt}]

    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        hosted_response = client.chat.send(
            model=HOSTED_MODEL, messages=messages, temperature=0,
            response_format={"type":"json_schema","json_schema":{
                "name":"opinion_prediction","strict":True,"schema":schema,
            }},
        )
    hosted_raw = hosted_response.choices[0].message.content
    hosted_prediction = json.loads(hosted_raw)["predicted_category"]
    hosted_results.append({"id":profile["id"],"prediction":hosted_prediction,"human":profile["human_answer"]})

    local_response = ollama.chat(
        model=LOCAL_MODEL, messages=messages, format=schema,
        options={"temperature":0},
    )
    local_raw = local_response.message.content
    local_prediction = json.loads(local_raw)["predicted_category"]
    local_results.append({"id":profile["id"],"prediction":local_prediction,"human":profile["human_answer"]})

    print(profile["id"], "hosted raw:", hosted_raw, "local raw:", local_raw)

# CELL: Calculate individual exact matches separately
hosted_matches = 0
local_matches = 0
for record in hosted_results:
    if record["prediction"] == record["human"]:
        hosted_matches = hosted_matches + 1
for record in local_results:
    if record["prediction"] == record["human"]:
        local_matches = local_matches + 1
print("Hosted exact matches:", hosted_matches, "of", len(profiles))
print("Local exact matches:", local_matches, "of", len(profiles))

# CELL: Compare one aggregate quantity without confusing it with individual accuracy
human_total = 0
hosted_total = 0
local_total = 0
for record in hosted_results:
    human_total = human_total + record["human"]
    hosted_total = hosted_total + record["prediction"]
for record in local_results:
    local_total = local_total + record["prediction"]
human_mean = human_total / len(profiles)
hosted_mean = hosted_total / len(profiles)
local_mean = local_total / len(profiles)
print("Human mean:", human_mean)
print("Hosted mean:", hosted_mean)
print("Local mean:", local_mean)

# ONE CHANGE: change p02 education to "high school" and rerun the full loop.
