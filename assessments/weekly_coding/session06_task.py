"""Week 6 assessed routine: compare two adaptive interview paths."""

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


# CELL: Load the course settings and choose a route
ROOT = Path.cwd()
while not (ROOT / "config" / "course_models.json").exists() and ROOT != ROOT.parent:
    ROOT = ROOT.parent

if not (ROOT / "config" / "course_models.json").exists():
    raise FileNotFoundError(
        "The complete GenAI_Soc2026 repository could not be found. Run this script "
        "from inside the complete course repository."
    )

config = json.loads((ROOT / "config" / "course_models.json").read_text())
HOSTED_MODEL = config["hosted"]["model"]
LOCAL_MODEL = config["local"]["model"]
ROUTE = "ollama"  # change to "openrouter" if preferred

if ROUTE not in {"openrouter", "ollama"}:
    raise ValueError("COURSE_ROUTE must be 'openrouter' or 'ollama'.")

if ROUTE == "openrouter" and not os.getenv("OPENROUTER_API_KEY"):
    os.environ["OPENROUTER_API_KEY"] = getpass("OpenRouter course key (hidden): ")

print("Route:", ROUTE)
print("Hosted model:", HOSTED_MODEL)
print("Local model:", LOCAL_MODEL)


# CELL: Store the protocol and first answer
interview_protocol = """
Research question: How do evaluators decide that a candidate is a good cultural fit?
Ask one short follow-up question about a concrete judgment, episode or comparison.
Do not introduce a cause the evaluator has not mentioned.
Do not claim to have human feelings or experiences.
Return only the question.
"""

first_answer = "Evaluator: I could picture her working here."

conversation = [
    {"role": "system", "content": interview_protocol},
    {"role": "user", "content": first_answer},
]

print("Opening messages:", conversation)


# CELL: Generate the first adaptive probe
if ROUTE == "openrouter":
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        first_response = client.chat.send(
            model=HOSTED_MODEL, messages=conversation, temperature=0,
        )
    first_raw = first_response.choices[0].message.content
else:
    first_response = ollama.chat(think=False,
        model=LOCAL_MODEL, messages=conversation,
        options={"temperature": 0},
    )
    first_raw = first_response.message.content

first_probe = first_raw.strip()
print("First raw return:", first_raw)
print("First probe:", first_probe)


# CELL: Build two independent paths
shared_answer = (
    "Evaluator: We discovered that we had both rowed in college and understood "
    "long training days."
)
case_answer = (
    "Evaluator: She challenged an assumption in the case without becoming combative."
)

shared_path = conversation.copy()
shared_path.append({"role": "assistant", "content": first_probe})
shared_path.append({"role": "user", "content": shared_answer})

case_path = conversation.copy()
case_path.append({"role": "assistant", "content": first_probe})
case_path.append({"role": "user", "content": case_answer})

print("Shared path messages:", len(shared_path))
print("Case path messages:", len(case_path))


# CELL: Generate the next probe for each path
if ROUTE == "openrouter":
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        shared_response = client.chat.send(
            model=HOSTED_MODEL, messages=shared_path, temperature=0,
        )
        case_response = client.chat.send(
            model=HOSTED_MODEL, messages=case_path, temperature=0,
        )
    shared_raw = shared_response.choices[0].message.content
    case_raw = case_response.choices[0].message.content
else:
    shared_response = ollama.chat(think=False,
        model=LOCAL_MODEL, messages=shared_path,
        options={"temperature": 0},
    )
    case_response = ollama.chat(think=False,
        model=LOCAL_MODEL, messages=case_path,
        options={"temperature": 0},
    )
    shared_raw = shared_response.message.content
    case_raw = case_response.message.content

shared_probe = shared_raw.strip()
case_probe = case_raw.strip()

print("Shared-experience raw return:", shared_raw)
print("Case-performance raw return:", case_raw)
print("Shared-experience probe:", shared_probe)
print("Case-performance probe:", case_probe)


# CELL: Record the researcher's assessment
shared_review = {
    "responsive": True,
    "introduces_new_cause": False,
    "asks_for_concrete_evidence": True,
    "claims_human_experience": False,
    "notes": "Replace this sentence with your assessment of the shared path.",
}

case_review = {
    "responsive": True,
    "introduces_new_cause": False,
    "asks_for_concrete_evidence": True,
    "claims_human_experience": False,
    "notes": "Replace this sentence with your assessment of the case path.",
}


# CELL: Preserve the research record
model_used = HOSTED_MODEL if ROUTE == "openrouter" else LOCAL_MODEL
research_record = {
    "route": ROUTE,
    "requested_model": model_used,
    "opening_messages": conversation,
    "first_raw_return": first_raw,
    "shared_path": shared_path,
    "shared_raw_return": shared_raw,
    "case_path": case_path,
    "case_raw_return": case_raw,
    "shared_review": shared_review,
    "case_review": case_review,
}

print(json.dumps(research_record, indent=2))

# ONE CHANGE:
# Replace only case_answer, then rerun from "Build two independent paths" onward.
# The code recreates both path lists, so earlier turns will not be duplicated.
