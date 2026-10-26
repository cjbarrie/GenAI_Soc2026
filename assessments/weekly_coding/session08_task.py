"""Week 8: forecast three published experimental effects through both routes."""

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
        "The complete GenAI_Soc2026 repository could not be found. Open a terminal "
        "in the complete course folder and run this file from there."
    )

config = json.loads((ROOT / "config" / "course_models.json").read_text())
HOSTED_MODEL = config["hosted"]["model"]
LOCAL_MODEL = config["local"]["model"]
if not os.getenv("OPENROUTER_API_KEY"):
    os.environ["OPENROUTER_API_KEY"] = getpass("OpenRouter course key (hidden): ")

# CELL: Store three published experiments and their held-out human results
experiments = [
    {
        "id": "turnout",
        "context": "Michigan registered voters before the 2006 primary",
        "control": "No mailing",
        "treatment": "A mailing says voting records are public and that an updated record will be sent to the household and its neighbours after the election.",
        "outcome": "Percent who voted",
        "human_control": 29.7,
        "human_treatment": 37.8,
    },
    {
        "id": "towels",
        "context": "Hotel guests staying at least two nights",
        "control": "A sign asks guests to help save the environment by reusing towels.",
        "treatment": "A sign says almost 75% of guests participate in the towel-reuse programme.",
        "outcome": "Percent who reused a towel",
        "human_control": 35.1,
        "human_treatment": 44.1,
    },
    {
        "id": "disease",
        "context": "Participants choose between programmes responding to a disease expected to kill 600 people",
        "control": "Gain frame: choose between saving 200 people for certain or a one-third chance of saving all 600.",
        "treatment": "Loss frame: choose between 400 people dying for certain or a one-third chance that nobody dies.",
        "outcome": "Percent choosing the certain option",
        "human_control": 72.0,
        "human_treatment": 22.0,
    },
]

schema = {
    "type": "object",
    "properties": {
        "predicted_control_percent": {"type": "number", "minimum": 0, "maximum": 100},
        "predicted_treatment_percent": {"type": "number", "minimum": 0, "maximum": 100},
    },
    "required": ["predicted_control_percent", "predicted_treatment_percent"],
    "additionalProperties": False,
}
temperature = 0
hosted_results = []
local_results = []
print("Experiments:", len(experiments))

# REFERENCE RUN SHOWN IN THE LECTURE
# On 26 October 2026, gemma4:e2b-it-qat at temperature 0 predicted
# 30% in the towel control condition and 75% in the treatment condition.
# That is a predicted effect of +45 points, compared with the observed +9 points,
# and an absolute error of 36 points.
# This is a dated example rather than an expected answer; your output may differ.

# CELL: Loop through the experiments and call both routes
for experiment in experiments:
    experiment_for_model = {
        "context": experiment["context"],
        "control": experiment["control"],
        "treatment": experiment["treatment"],
        "outcome": experiment["outcome"],
    }
    prompt = (
        "Forecast the two outcome rates for this randomized experiment in the stated population. "
        "Return percentages from 0 to 100. Do not claim that this replaces human evidence.\n"
        + json.dumps(experiment_for_model, indent=2)
    )
    messages = [{"role": "user", "content": prompt}]

    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        hosted_response = client.chat.send(
            model=HOSTED_MODEL,
            messages=messages,
            temperature=temperature,
            response_format={
                "type": "json_schema",
                "json_schema": {"name": "effect_forecast", "strict": True, "schema": schema},
            },
        )
    hosted_raw = hosted_response.choices[0].message.content

    local_response = ollama.chat(think=False,
        model=LOCAL_MODEL,
        messages=messages,
        format=schema,
        options={"temperature": temperature},
    )
    local_raw = local_response.message.content

    print(experiment["id"], "hosted raw:", hosted_raw)
    print(experiment["id"], "local raw:", local_raw)

    observed_effect = experiment["human_treatment"] - experiment["human_control"]

    hosted_parsed = json.loads(hosted_raw)
    hosted_effect = (
        hosted_parsed["predicted_treatment_percent"]
        - hosted_parsed["predicted_control_percent"]
    )
    hosted_results.append(
        {
            "id": experiment["id"],
            "predicted_effect": hosted_effect,
            "observed_effect": observed_effect,
            "absolute_error": abs(hosted_effect - observed_effect),
            "raw": hosted_raw,
        }
    )

    local_parsed = json.loads(local_raw)
    local_effect = (
        local_parsed["predicted_treatment_percent"]
        - local_parsed["predicted_control_percent"]
    )
    local_results.append(
        {
            "id": experiment["id"],
            "predicted_effect": local_effect,
            "observed_effect": observed_effect,
            "absolute_error": abs(local_effect - observed_effect),
            "raw": local_raw,
        }
    )

# CELL: Compare errors across the three contexts
hosted_error_total = 0
local_error_total = 0
for record in hosted_results:
    hosted_error_total = hosted_error_total + record["absolute_error"]
    print("Hosted:", record["id"], record)
for record in local_results:
    local_error_total = local_error_total + record["absolute_error"]
    print("Local:", record["id"], record)

hosted_mae = hosted_error_total / len(hosted_results)
local_mae = local_error_total / len(local_results)
print("Hosted mean absolute error:", round(hosted_mae, 1))
print("Local mean absolute error:", round(local_mae, 1))

# ONE CHANGE: set temperature to 0.7 and rerun only the towel experiment.
