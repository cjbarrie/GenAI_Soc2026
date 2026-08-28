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

# CELL: Choose a route and define the action schema
ROUTE = "ollama"
action_schema = {
    "type":"object","properties":{"action":{"type":"string"}},
    "required":["action"],"additionalProperties":False,
}

# CELL: Define one actor update function
def choose_action(actor, observation, route):
    messages = [{"role":"user","content":(
        "Choose JOIN or STAY_OUT for this simulated actor. Actor: " + json.dumps(actor) +
        " Observation: " + observation + " Return JSON."
    )}]
    if route == "openrouter":
        with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
            response = client.chat.send(
                model=HOSTED_MODEL,messages=messages,temperature=0,
                response_format={"type":"json_schema","json_schema":{
                    "name":"join_action","strict":True,"schema":action_schema,
                }},
            )
        raw_output = response.choices[0].message.content
    else:
        response = ollama.chat(model=LOCAL_MODEL,messages=messages,format=action_schema,options={"temperature":0})
        raw_output = response.message.content
    return json.loads(raw_output)["action"]

# CELL: Store three actors and two conditions
actors = [
    {"id":"a","initial_support":"low"},
    {"id":"b","initial_support":"medium"},
    {"id":"c","initial_support":"high"},
]
conditions = ["baseline", "interaction"]
all_runs = []

# CELL: Repeat each condition three times
for condition in conditions:
    for run_number in range(3):
        actions = []
        previous_action = "No prior action is visible."
        for actor in actors:
            if condition == "baseline":
                observation = "No other actor's action is visible."
            else:
                observation = "The preceding actor chose: " + previous_action
            action = choose_action(actor, observation, ROUTE)
            actions.append(action)
            previous_action = action
        all_runs.append({"condition":condition,"run":run_number,"actions":actions})
        print(condition, run_number, actions)

# CELL: Compare convergence without selecting one favorite run
for record in all_runs:
    all_same = len(set(record["actions"])) == 1
    print(record["condition"], record["run"], "all same:", all_same)

# ONE CHANGE: reverse the actor order and rerun all conditions.
