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

# CELL: Choose a normal route and define the action schema
ROUTE = "ollama"
action_schema = {
    "type":"object",
    "properties":{"action":{"type":"string"},"reason":{"type":"string"}},
    "required":["action","reason"],"additionalProperties":False,
}

# CELL: Define the first student-edited model function
def choose_action(state, observation, route, temperature):
    prompt = (
        "Choose one next action for this simulated actor. State: " + json.dumps(state) +
        " Observation: " + observation + " Return action and reason as JSON."
    )
    messages = [{"role":"user","content":prompt}]

    if route == "openrouter":
        with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
            response = client.chat.send(
                model=HOSTED_MODEL, messages=messages, temperature=temperature,
                response_format={"type":"json_schema","json_schema":{
                    "name":"agent_action","strict":True,"schema":action_schema,
                }},
            )
        raw_output = response.choices[0].message.content
    else:
        response = ollama.chat(
            model=LOCAL_MODEL, messages=messages, format=action_schema,
            options={"temperature":temperature},
        )
        raw_output = response.message.content
    print("Raw function output:", raw_output)
    return json.loads(raw_output)

# CELL: Call the function and inspect its returned dictionary
state = {"speaker":"A","prior_action":"silent","goal":"be heard without conflict"}
observation = "Speaker B expresses disagreement in a calm tone."
result_1 = choose_action(state, observation, ROUTE, 0)
print("Returned value:", result_1)
print("Returned type:", type(result_1))

# CELL: Change one argument and call the same function again
# ONE CHANGE: the observation changes; state, route and temperature stay fixed.
changed_observation = "Speaker B interrupts and raises their voice."
result_2 = choose_action(state, changed_observation, ROUTE, 0)
print("First action:", result_1["action"])
print("Second action:", result_2["action"])
