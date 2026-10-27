"""Week 9: compare two ways of assisting the same customer-support worker."""

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
if not os.getenv("OPENROUTER_API_KEY"):
    os.environ["OPENROUTER_API_KEY"] = getpass("OpenRouter course key (hidden): ")

# CELL: Store the case, policy and output schema
ROUTE = "ollama"  # change to "openrouter" to use the hosted route
customer_message = (
    "My bank shows two entries for my annual plan. One has completed and the other "
    "still says pending. The pending amount has reduced the money available for my "
    "rent tomorrow. Have I been charged twice, and can you refund it today?"
)
policy_text = (
    "A pending authorization is not a completed payment and normally disappears "
    "within three to five business days. Agents cannot manually release or refund "
    "a pending authorization. A duplicate-charge refund requires two distinct settled "
    "transaction identifiers. Immediate financial hardship may be escalated to a "
    "supervisor, but escalation does not itself authorize a refund."
)
output_schema = {
    "type": "object",
    "properties": {
        "known_facts": {"type": "array", "items": {"type": "string"}},
        "uncertainties": {"type": "array", "items": {"type": "string"}},
        "recommended_action": {"type": "string"},
        "policy_evidence": {"type": "string"},
        "worker_guidance": {"type": "string"},
        "customer_reply": {"type": ["string", "null"]},
    },
    "required": ["known_facts", "uncertainties", "recommended_action",
                 "policy_evidence", "worker_guidance", "customer_reply"],
    "additionalProperties": False,
}


# CELL: Define the first student-edited function
def request_assistance(customer_message, policy_text, assistance_mode, route):
    """Send one support case to the selected route and return a checked record."""
    if assistance_mode not in {"draft", "coach"}:
        raise ValueError("assistance_mode must be 'draft' or 'coach'")

    mode_instruction = (
        "Write a proposed customer-facing reply."
        if assistance_mode == "draft"
        else "Do not write a customer-facing reply; return null for customer_reply."
    )
    prompt = f"""
You are assisting a customer-support worker.

Customer message:
{customer_message}

Internal policy:
{policy_text}

Assistance mode: {assistance_mode}
{mode_instruction}

Separate known facts from uncertainties. Do not treat a pending authorization as
a second completed charge. Do not promise a refund unless two settled transaction
identifiers have been verified. Keep hardship escalation separate from refund
authorization. Return the six required fields as JSON.
""".strip()
    messages = [{"role": "user", "content": prompt}]
    print("Function input — mode:", assistance_mode, type(assistance_mode))
    print("Function input — route:", route, type(route))
    print("Complete prompt:\n", prompt)

    if route == "openrouter":
        with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
            response = client.chat.send(
                model=HOSTED_MODEL,
                messages=messages,
                temperature=0,
                response_format={"type": "json_schema", "json_schema": {
                    "name": "workplace_assistance", "strict": True,
                    "schema": output_schema,
                }},
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
    all_text = " ".join(
        parsed_output["known_facts"] + parsed_output["uncertainties"] + [
            parsed_output["recommended_action"], parsed_output["policy_evidence"],
            parsed_output["worker_guidance"], parsed_output["customer_reply"] or "",
        ]
    ).lower()
    checks = {
        "does_not_invent_two_completed_charges": "two completed charges" not in all_text,
        "does_not_promise_refund_today": "refund today" not in all_text,
        "mentions_hardship_escalation": "escalat" in all_text,
        "mode_contract_met": (
            parsed_output["customer_reply"] is not None
            if assistance_mode == "draft"
            else parsed_output["customer_reply"] is None
        ),
    }
    record = {
        "inputs": {"customer_message": customer_message, "policy_text": policy_text,
                   "assistance_mode": assistance_mode},
        "route": route,
        "model": model_used,
        "messages": messages,
        "raw_output": raw_output,
        "parsed_output": parsed_output,
        "checks": checks,
        "worker_decision": "not yet recorded",
    }
    print("Function output type:", type(record))
    print("Checks:", checks)
    return record


# CELL: Call the function in draft mode
draft_record = request_assistance(
    customer_message=customer_message,
    policy_text=policy_text,
    assistance_mode="draft",
    route=ROUTE,
)
print("Draft reply:", draft_record["parsed_output"]["customer_reply"])

# CELL: Change only the assistance mode
coach_record = request_assistance(
    customer_message=customer_message,
    policy_text=policy_text,
    assistance_mode="coach",
    route=ROUTE,
)
print("Coach reply:", coach_record["parsed_output"]["customer_reply"])

# ONE CHANGE: revise one sentence in mode_instruction, then rerun both calls.
