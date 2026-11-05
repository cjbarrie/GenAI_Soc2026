"""Week 9: record human judgments under different displayed certainty levels.

New Python ideas: ``def``, parameters, local variables, ``return`` and
``if``/``elif``/``else``. The model produces one recommendation. The evidence
and recommendation stay fixed while the displayed certainty changes.
"""

# CELL: Load the course settings and SDKs
import json
import os
from getpass import getpass
from pathlib import Path

try:
    import ollama
    from openrouter import OpenRouter
except ModuleNotFoundError:
    ollama = None
    OpenRouter = None

ROOT = Path.cwd()
while not (ROOT / "config" / "course_models.json").exists() and ROOT != ROOT.parent:
    ROOT = ROOT.parent
if not (ROOT / "config" / "course_models.json").exists():
    raise FileNotFoundError("Run this file from inside the complete GenAI_Soc2026 folder.")

config = json.loads((ROOT / "config" / "course_models.json").read_text())
HOSTED_MODEL = config["hosted"]["model"]
LOCAL_MODEL = config["local"]["model"]
USE_RECORDED = os.getenv("COURSE_USE_RECORDED", "0") == "1"

# CELL: Store the workplace decision and the evidence
ROUTE = "ollama"  # change to "openrouter" to use the hosted route
decision_context = (
    "A consulting team must advise a lender about whether to begin a three-month "
    "internal pilot of a mortgage-prediction model. Staff would review every model "
    "recommendation during the pilot."
)
model_evidence = {
    "held_out_cases": 200,
    "model_accuracy": 0.80,
    "always_predict_no_mortgage_accuracy": 0.60,
    "calibration_reported": False,
    "subgroup_performance_reported": False,
    "error_costs_reported": False,
}
output_schema = {
    "type": "object",
    "properties": {
        "recommendation": {
            "type": "string",
            "enum": ["begin_limited_pilot", "request_more_evidence", "do_not_use"],
        },
        "evidence_used": {"type": "array", "items": {"type": "string"}},
        "missing_information": {"type": "array", "items": {"type": "string"}},
        "explanation": {"type": "string"},
    },
    "required": ["recommendation", "evidence_used", "missing_information", "explanation"],
    "additionalProperties": False,
}
recorded_raw_output = json.dumps({
    "recommendation": "request_more_evidence",
    "evidence_used": [
        "The model achieved 0.80 accuracy on 200 held-out cases.",
        "The stated baseline accuracy is 0.60.",
    ],
    "missing_information": [
        "calibration",
        "subgroup performance",
        "the costs of different errors",
    ],
    "explanation": (
        "The model exceeds the stated baseline, but the supplied evidence does not "
        "show whether its errors are acceptable for the proposed pilot."
    ),
})

# CELL: Ask the model for one recommendation
evidence_text = json.dumps(model_evidence, indent=2)
prompt = f"""You are assisting a consultant with this workplace decision:

{decision_context}

Available evidence:
{evidence_text}

Use only the supplied evidence. Choose one of the three permitted recommendations.
Identify the evidence you used and information that remains missing. Return JSON."""
messages = [{"role": "user", "content": prompt}]

if USE_RECORDED:
    raw_output = recorded_raw_output
    model_used = "recorded-teaching-return"
elif ROUTE == "openrouter":
    if OpenRouter is None:
        raise ModuleNotFoundError("Run 'uv sync --frozen' before using OpenRouter.")
    api_key = os.getenv("OPENROUTER_API_KEY") or getpass("OpenRouter course key (hidden): ")
    response_format = {"type": "json_schema", "json_schema": {
        "name": "workplace_recommendation",
        "strict": True,
        "schema": output_schema,
    }}
    with OpenRouter(api_key=api_key) as client:
        response = client.chat.send(
            model=HOSTED_MODEL,
            messages=messages,
            temperature=0,
            response_format=response_format,
        )
    raw_output = response.choices[0].message.content
    model_used = HOSTED_MODEL
elif ROUTE == "ollama":
    if ollama is None:
        raise ModuleNotFoundError("Run 'uv sync --frozen' before using Ollama.")
    response = ollama.chat(think=False,
        model=LOCAL_MODEL,
        messages=messages,
        format=output_schema,
        options={"temperature": 0},
    )
    raw_output = response.message.content
    model_used = LOCAL_MODEL
else:
    raise ValueError("ROUTE must be 'openrouter' or 'ollama'")

print("Raw model return:\n", raw_output)
print("Raw return type:", type(raw_output))
model_advice = json.loads(raw_output)
print("Parsed recommendation:", model_advice["recommendation"])
print("Parsed return type:", type(model_advice))

# CELL: Store three displays of the same advice
certainty_levels = [0.55, 0.75, 0.95]
print("Displayed certainty levels:", certainty_levels)
print("Evidence remains fixed:", model_evidence)
print("Recommendation remains fixed:", model_advice["recommendation"])

# These are editable placeholders. Replace them with your own decisions and reasons.
human_actions = [
    "ask_for_more_information",
    "escalate_to_specialist",
    "accept_recommendation",
]
human_reasons = [
    "The recommendation names missing evidence, so I would ask what can be supplied.",
    "The displayed certainty is higher, but a specialist should still assess the missing tests.",
    "I noticed that the high displayed certainty made me more willing to accept the advice.",
]

# CELL: Define the first small student-edited function
def record_human_judgment(
    recommendation,
    stated_certainty,
    human_action,
    human_reason,
):
    """Return one record of a worker's response to displayed model advice."""
    if human_action == "accept_recommendation":
        next_step = "Proceed with the recommendation."
    elif human_action == "ask_for_more_information":
        next_step = "Request additional evidence before deciding."
    elif human_action == "escalate_to_specialist":
        next_step = "Send the evidence and advice to a specialist."
    elif human_action == "reject_recommendation":
        next_step = "Do not proceed with the recommendation."
    else:
        raise ValueError(
            "human_action must be accept_recommendation, ask_for_more_information, "
            "escalate_to_specialist or reject_recommendation"
        )

    judgment_record = {
        "recommendation": recommendation,
        "stated_certainty": stated_certainty,
        "human_action": human_action,
        "human_reason": human_reason,
        "next_step": next_step,
    }
    return judgment_record

# CELL: Record the decision at each displayed certainty level
judgment_records = []
for position, stated_certainty in enumerate(certainty_levels):
    human_action = human_actions[position]
    human_reason = human_reasons[position]
    record = record_human_judgment(
        recommendation=model_advice["recommendation"],
        stated_certainty=stated_certainty,
        human_action=human_action,
        human_reason=human_reason,
    )
    judgment_records.append(record)
    print("\nDisplayed certainty:", stated_certainty)
    print("Human action:", record["human_action"])
    print("Next step:", record["next_step"])

# CELL: Compare the worker's decisions
for record in judgment_records:
    print(
        record["stated_certainty"],
        record["human_action"],
        "—",
        record["human_reason"],
    )

evidence_changed = False
recommendation_changed = False
print("Did the evidence change?", evidence_changed)
print("Did the recommendation change?", recommendation_changed)
human_action_changed = not (
    human_actions[0] == human_actions[1] == human_actions[2]
)
print("Did the human action change?", human_action_changed)

# CELL: Reflect on human judgment and organizational visibility
reflection_questions = [
    "Did higher displayed certainty change your willingness to follow the recommendation?",
    "Did the evidence justify that change?",
    "What validation would make the certainty value meaningful?",
    "What can the organization now observe about your decisions and reasons?",
    "What could you explain later without the assistant?",
]
for question in reflection_questions:
    print(question)

# CELL: Answer one question without model assistance
knowledge_check = (
    "Does a displayed certainty of 0.95 mean that this recommendation is correct 95% "
    "of the time? What evidence would be needed to interpret that number?"
)
print(knowledge_check)

# ONE CHANGE: edit one value in human_actions or human_reasons, rerun, and compare.
