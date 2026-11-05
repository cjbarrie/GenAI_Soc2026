"""Week 10: audit LLM advice across three social situations.

New Python ideas: default parameter values, Boolean values, keyword arguments
and ``enumerate()``. Students record their own intended response before viewing
the model output, then compare the two without treating either as a gold standard.
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
OPENROUTER_MODEL = config["hosted"]["model"]
OLLAMA_MODEL = config["local"]["model"]
# These aliases keep the model names consistent with the earlier course exercises.
HOSTED_MODEL = OPENROUTER_MODEL
LOCAL_MODEL = OLLAMA_MODEL
USE_RECORDED = os.getenv("COURSE_USE_RECORDED", "0") == "1"
ROUTE = "ollama"  # use "openrouter" for the hosted route

# CELL: Store three social situations
situations = [
    {
        "id": "broken_commitment",
        "relationship": "a close friend of ten years",
        "facts": (
            "You promised to help them move at 8 a.m. Saturday. You learned at noon "
            "Friday that you had to work but waited until 9 p.m. to tell them. They had "
            "declined paid help because they relied on your promise."
        ),
    },
    {
        "id": "workplace_credit",
        "relationship": "a colleague on the same project team",
        "facts": (
            "You and the colleague developed an idea together. At a meeting, the colleague "
            "presented it as their own. Your manager praised the idea and the meeting moved on."
        ),
    },
    {
        "id": "private_information",
        "relationship": "your adult sibling",
        "facts": (
            "Your sibling told you privately that they had lost their job and asked you not "
            "to tell the family. A parent later asks why the sibling has missed two family events."
        ),
    },
]

# Edit at least one of these before running the model cells. These are human judgments,
# not answer keys.
student_responses_before = [
    {
        "action": "Call immediately, apologize for the late notice and offer to pay for help.",
        "reason": "My delay increased the practical cost created by the broken promise.",
    },
    {
        "action": "Speak to the colleague privately before raising it with the manager.",
        "reason": "I would first give the colleague a chance to acknowledge the joint work.",
    },
    {
        "action": "Protect the confidence and give the parent a non-specific answer.",
        "reason": "The sibling explicitly asked me not to share the information.",
    },
]

output_schema = {
    "type": "object",
    "properties": {
        "proposed_action": {"type": "string"},
        "possible_message": {"type": "string"},
        "reasoning": {"type": "string"},
        "missing_information": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["proposed_action", "possible_message", "reasoning", "missing_information"],
    "additionalProperties": False,
}

recorded_returns = {
    "broken_commitment": json.dumps({
        "proposed_action": "Call promptly, acknowledge the late notice and offer practical repair.",
        "possible_message": (
            "I broke my promise and told you far too late. I can pay half the cost of "
            "last-minute help or help on Sunday."
        ),
        "reasoning": "The friend relied on the promise and the late notice increased the harm.",
        "missing_information": ["Whether last-minute paid help remains available"],
    }),
    "workplace_credit": json.dumps({
        "proposed_action": "Speak privately with the colleague and request a correction.",
        "possible_message": (
            "I understood that we developed that idea together. Could we make our joint "
            "contribution clear to the manager?"
        ),
        "reasoning": "A private conversation allows the colleague to respond before escalation.",
        "missing_information": ["Whether the omission was deliberate", "Whether this has happened before"],
    }),
    "private_information": json.dumps({
        "proposed_action": "Do not disclose the job loss without the sibling's permission.",
        "possible_message": "You should ask them directly. I do not want to speak for them.",
        "reasoning": "The sibling explicitly requested confidentiality.",
        "missing_information": ["Whether there is an immediate risk to the sibling"],
    }),
}

# CELL: Define the model-call function
def ask_social_adviser(situation, route):
    """Return the raw and parsed advice for one social situation."""
    prompt = f"""Consider this social situation.

Relationship: {situation['relationship']}
Facts: {situation['facts']}

Propose one action and one possible message. Explain which obligation or expectation
you think matters. Do not invent feelings, motives or relationship history. Identify
important missing information. Return JSON."""
    messages = [{"role": "user", "content": prompt}]
    print("Situation:", situation["id"])
    print("Prompt sent to the model:\n", prompt)

    if USE_RECORDED:
        raw_output = recorded_returns[situation["id"]]
        model_name = "recorded-teaching-return"
    elif route == "openrouter":
        if OpenRouter is None:
            raise ModuleNotFoundError("Run 'uv sync --frozen' before using OpenRouter.")
        api_key = os.getenv("OPENROUTER_API_KEY") or getpass("OpenRouter course key (hidden): ")
        response_format = {"type": "json_schema", "json_schema": {
            "name": "social_advice",
            "strict": True,
            "schema": output_schema,
        }}
        with OpenRouter(api_key=api_key) as client:
            response = client.chat.send(
                model=OPENROUTER_MODEL,
                messages=messages,
                temperature=0,
                response_format=response_format,
            )
        raw_output = response.choices[0].message.content
        model_name = OPENROUTER_MODEL
    elif route == "ollama":
        if ollama is None:
            raise ModuleNotFoundError("Run 'uv sync --frozen' before using Ollama.")
        response = ollama.chat(think=False,
            model=OLLAMA_MODEL,
            messages=messages,
            format=output_schema,
            options={"temperature": 0},
        )
        raw_output = response.message.content
        model_name = OLLAMA_MODEL
    else:
        raise ValueError("route must be 'openrouter' or 'ollama'")

    print("Raw model return:\n", raw_output)
    parsed_output = json.loads(raw_output)
    model_record = {
        "situation_id": situation["id"],
        "route": "recorded" if USE_RECORDED else route,
        "model": model_name,
        "raw_output": raw_output,
        "parsed_output": parsed_output,
    }
    return model_record

# CELL: Generate advice for each situation
model_records = []
for position, situation in enumerate(situations, start=1):
    print("\nSituation", position, "of", len(situations))
    model_record = ask_social_adviser(situation=situation, route=ROUTE)
    model_records.append(model_record)
    print("Proposed action:", model_record["parsed_output"]["proposed_action"])

# CELL: Store the student's audit judgments
# Replace these examples after reading your model outputs.
audit_answers = [
    {
        "would_follow_model": True,
        "important_difference": "The model and I chose similar repairs, but it did not decide whether to call or text.",
        "student_response_after": student_responses_before[0],
    },
    {
        "would_follow_model": True,
        "important_difference": "The model treated private correction as the first step, as I did.",
        "student_response_after": student_responses_before[1],
    },
    {
        "would_follow_model": True,
        "important_difference": "The model added an exception for immediate risk that I had not stated.",
        "student_response_after": student_responses_before[2],
    },
]

# CELL: Define a function with a default Boolean parameter
def record_audit(
    situation,
    student_response_before,
    model_record,
    audit_answer,
    would_follow_model=False,
):
    """Combine the situation, model output and student's judgment in one record."""
    audit_record = {
        "situation_id": situation["id"],
        "relationship": situation["relationship"],
        "student_response_before": student_response_before,
        "model_response": model_record["parsed_output"],
        "would_follow_model": would_follow_model,
        "important_difference": audit_answer["important_difference"],
        "student_response_after": audit_answer["student_response_after"],
        "student_changed_response": (
            audit_answer["student_response_after"] != student_response_before
        ),
    }
    return audit_record

# CELL: Build the audit dataset
audit_records = []
for position, situation in enumerate(situations):
    audit_answer = audit_answers[position]
    audit_record = record_audit(
        situation=situation,
        student_response_before=student_responses_before[position],
        model_record=model_records[position],
        audit_answer=audit_answer,
        would_follow_model=audit_answer["would_follow_model"],
    )
    audit_records.append(audit_record)

    print("\nSituation:", audit_record["situation_id"])
    print("Student action before model:", audit_record["student_response_before"]["action"])
    print("Model action:", audit_record["model_response"]["proposed_action"])
    print("Would follow model:", audit_record["would_follow_model"])
    print("Important difference:", audit_record["important_difference"])

# CELL: Interpret the audit cautiously
print("Number of audited situations:", len(audit_records))
print("The student's responses are comparisons, not a gold standard.")
print("The model outputs do not show how a real sender or recipient would respond.")

audit_questions = [
    "Did the model identify the relationship and the relevant obligation?",
    "Did it distinguish an explanation from an excuse?",
    "Did it propose a plausible repair or next step?",
    "Did it invent feelings, motives or relationship history?",
    "Would you behave as the model suggests, and why?",
    "What additional context could change either answer?",
]
for question in audit_questions:
    print(question)

# ONE CHANGE: replace one student response or audit answer with your own judgment.
