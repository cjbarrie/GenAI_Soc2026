"""Week 9: work through a model review while retaining worker decisions."""

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
        "A course SDK is missing. In the complete course folder run 'uv sync --frozen', "
        "then run this task with 'uv run python'."
    ) from error

ROOT = Path.cwd()
while not (ROOT / "config" / "course_models.json").exists() and ROOT != ROOT.parent:
    ROOT = ROOT.parent
if not (ROOT / "config" / "course_models.json").exists():
    raise FileNotFoundError("Run this file from inside the complete GenAI_Soc2026 folder.")

config = json.loads((ROOT / "config" / "course_models.json").read_text())
HOSTED_MODEL = config["hosted"]["model"]
LOCAL_MODEL = config["local"]["model"]

# CELL: Store the consulting task and the response fields
ROUTE = "ollama"  # change to "openrouter" to use the hosted route
model_results = {
    "task": "Predict whether a couple will take out a mortgage",
    "test_cases": 200,
    "actual_mortgage_cases": 80,
    "model_accuracy": 0.80,
    "always_predict_no_mortgage_accuracy": 0.60,
    "false_negatives": 20,
    "evidence": "Performance on held-out historical applications",
}
ai_analysis = (
    "The model is 80% accurate, so it is ready to guide an investment strategy. "
    "Its score shows that increasing a couple's score causes them to take out a mortgage. "
    "It also performs much better than the current baseline, which is no better than chance."
)
assistant_instruction = (
    "Act as a coach. Check the analysis and explain the problems you find. "
    "Ask the consultant questions, but do not write the final client advice."
)
output_schema = {
    "type": "object",
    "properties": {
        "baseline_comparison": {
            "type": "string",
            "enum": ["model_outperforms_baseline", "no_difference", "insufficient_information"],
        },
        "causal_claim": {"type": "string", "enum": ["supported", "not_supported"]},
        "decision_status": {"type": "string", "enum": ["ready", "needs_more_information"]},
        "explanation": {"type": "array", "items": {"type": "string"}},
        "questions_for_worker": {"type": "array", "items": {"type": "string"}},
        "data_science_escalation": {"type": "string"},
    },
    "required": [
        "baseline_comparison", "causal_claim", "decision_status", "explanation",
        "questions_for_worker", "data_science_escalation",
    ],
    "additionalProperties": False,
}

# CELL: Define the first student-edited function
def call_review_assistant(messages, route):
    """Send the current conversation to one model route and preserve its return."""
    print("Function input — messages:", type(messages), "with", len(messages), "items")
    print("Function input — route:", route, type(route))
    print("Latest message:\n", messages[-1]["content"])

    if route == "openrouter":
        api_key = os.getenv("OPENROUTER_API_KEY") or getpass("OpenRouter course key (hidden): ")
        response_format = {"type": "json_schema", "json_schema": {
            "name": "work_review", "strict": True,
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
    elif route == "ollama":
        response = ollama.chat(think=False,
            model=LOCAL_MODEL,
            messages=messages,
            format=output_schema,
            options={"temperature": 0},
        )
        raw_output = response.message.content
        model_used = LOCAL_MODEL
    else:
        raise ValueError("route must be 'openrouter' or 'ollama'")

    print("Raw model return:\n", raw_output)
    print("Raw return type:", type(raw_output))
    parsed_output = json.loads(raw_output)
    checks = {
        "compares_with_baseline": (
            parsed_output["baseline_comparison"] == "model_outperforms_baseline"
        ),
        "does_not_make_causal_claim": parsed_output["causal_claim"] == "not_supported",
        "asks_for_more_evidence": parsed_output["decision_status"] == "needs_more_information",
    }
    reply_record = {
        "messages_sent": messages.copy(),
        "route": route,
        "model": model_used,
        "raw_output": raw_output,
        "parsed_output": parsed_output,
        "checks": checks,
    }
    print("Function output type:", type(reply_record))
    print("Checks:", checks)
    return reply_record

# CELL: Ask for an initial review
results_text = json.dumps(model_results, indent=2)
initial_prompt = f"""
You assist a general consultant who is reviewing an unfamiliar data-science analysis.
The consultant remains responsible for the advice given to the client. A data-science
team can investigate technical questions that the supplied evidence cannot settle.

Model results:
{results_text}

AI-written analysis to review:
{ai_analysis}

Instruction:
{assistant_instruction}

Compare 0.80 accuracy with the 0.60 baseline. Treat held-out predictive evidence as
predictive rather than causal. Explain whether accuracy alone makes the model ready for
an investment decision. Return the six required fields as JSON.
""".strip()
messages = [{"role": "user", "content": initial_prompt}]
first_reply = call_review_assistant(messages=messages, route=ROUTE)
print("Questions offered to the worker:", first_reply["parsed_output"]["questions_for_worker"])

# CELL: Let the worker choose what happens next
available_actions = [
    "ask_model_again",
    "escalate_to_data_science",
    "write_client_note",
]
worker_next_step = "ask_model_again"  # choose one value from available_actions
print("Available actions:", available_actions)
print("Worker chose:", worker_next_step)

follow_up_question = (
    "Explain why 80% overall accuracy does not tell me whether the model is safe to use "
    "for an investment decision. Use only the supplied results and name what is missing."
)

if worker_next_step == "ask_model_again":
    messages.append({"role": "assistant", "content": first_reply["raw_output"]})
    messages.append({"role": "user", "content": follow_up_question})
    second_reply = call_review_assistant(messages=messages, route=ROUTE)
elif worker_next_step in {"escalate_to_data_science", "write_client_note"}:
    second_reply = None
else:
    raise ValueError("Choose one action from available_actions")

print("Second model call made:", second_reply is not None)

# CELL: Record the worker's final decision
final_actions = [
    "escalate_to_data_science",
    "write_cautious_client_note",
    "recommend_against_use",
]
worker_final_action = "escalate_to_data_science"  # choose after inspecting the reply
worker_reason = (
    "The supplied results do not show calibration, false-positive errors or the costs "
    "of different mistakes, so the investment recommendation requires specialist review."
)

if worker_final_action not in final_actions:
    raise ValueError("Choose one action from final_actions")

work_record = {
    "source_material": {"model_results": model_results, "ai_analysis": ai_analysis},
    "first_model_reply": first_reply,
    "worker_next_step": worker_next_step,
    "worker_question": follow_up_question if second_reply is not None else None,
    "second_model_reply": second_reply,
    "worker_final_action": worker_final_action,
    "worker_reason": worker_reason,
}
print("Final worker action:", work_record["worker_final_action"])
print("Worker reason:", work_record["worker_reason"])
print("Work record type:", type(work_record))

# CELL: Reflect on the organization of the work
reflection_questions = [
    "Which reasoning did the model perform before you made a choice?",
    "What decision did you retain as the worker?",
    "Did the second call improve your understanding or move more reasoning to the model?",
    "What can an organization now observe about your question and decision?",
    "What could you explain later without the assistant?",
]
for question in reflection_questions:
    print(question)

# CELL: Answer one question without model assistance
knowledge_check = (
    "Does 80% overall accuracy tell us what percentage of couples predicted to take "
    "out a mortgage actually did so? Explain why or why not."
)
print(knowledge_check)

# ONE CHANGE: edit worker_next_step or follow_up_question, rerun, and compare the work record.
