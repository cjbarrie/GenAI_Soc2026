"""Week 6 assessed routine: edit interviewer advice and test a fictional persona."""

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


# CELL: Load course settings and choose a route
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
    raise ValueError("ROUTE must be 'openrouter' or 'ollama'.")

if ROUTE == "openrouter" and not os.getenv("OPENROUTER_API_KEY"):
    os.environ["OPENROUTER_API_KEY"] = getpass("OpenRouter course key (hidden): ")

print("Route:", ROUTE)


# EXERCISE 1: Give the model interviewer advice
research_question = (
    "How do evaluators decide that a candidate is a good cultural fit?"
)
interviewer_advice = (
    "Ask one short follow-up that requests a concrete example. "
    "Do not suggest a cause or answer the question for the evaluator."
)
first_answer = "Evaluator: I could picture her working here."

interviewer_messages = [
    {
        "role": "system",
        "content": (
            f"Research question: {research_question}\n"
            f"Advice for the interviewer: {interviewer_advice}\n"
            "Return only the next interview question."
        ),
    },
    {"role": "user", "content": first_answer},
]

print("Interviewer advice:", interviewer_advice)
print("Model input:", interviewer_messages)

if ROUTE == "openrouter":
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        interviewer_response = client.chat.send(
            model=HOSTED_MODEL,
            messages=interviewer_messages,
            temperature=0,
        )
    interviewer_raw = interviewer_response.choices[0].message.content
else:
    interviewer_response = ollama.chat(think=False,
        model=LOCAL_MODEL,
        messages=interviewer_messages,
        options={"temperature": 0},
    )
    interviewer_raw = interviewer_response.message.content

interviewer_probe = interviewer_raw.strip()
print("Raw interviewer return:", interviewer_raw)
print("Generated probe:", interviewer_probe)


# EXERCISE 2: Generate a fictional response to the probe
persona = {
    "role": "junior evaluator at a consulting firm",
    "decision_power": "takes notes but does not cast the final vote",
    "evaluation_style": "prefers evidence from the case exercise",
    "known_episode": (
        "the candidate challenged an assumption in the case without becoming combative"
    ),
}

persona_text = json.dumps(persona, indent=2)
persona_messages = [
    {
        "role": "system",
        "content": (
            "Generate fictional test data for an interview protocol. "
            "Answer as the supplied persona, use only the supplied details, and say "
            "when the persona does not know. Do not claim that the response represents "
            "real hiring evaluators."
        ),
    },
    {
        "role": "user",
        "content": (
            f"Fictional persona:\n{persona_text}\n\n"
            f"Interview question:\n{interviewer_probe}"
        ),
    },
]

print("Persona:", persona)
print("Synthetic-response input:", persona_messages)

if ROUTE == "openrouter":
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        synthetic_response = client.chat.send(
            model=HOSTED_MODEL,
            messages=persona_messages,
            temperature=0,
        )
    synthetic_raw = synthetic_response.choices[0].message.content
else:
    synthetic_response = ollama.chat(think=False,
        model=LOCAL_MODEL,
        messages=persona_messages,
        options={"temperature": 0},
    )
    synthetic_raw = synthetic_response.message.content

synthetic_answer = synthetic_raw.strip()
print("Raw synthetic return:", synthetic_raw)
print("Synthetic answer:", synthetic_answer)


# TECHNICAL STEP: Reconstruct the interview's ordered state
conversation = [{"role": "user", "content": first_answer}]
conversation.append({"role": "assistant", "content": interviewer_probe})
conversation.append({"role": "user", "content": synthetic_answer})

print("Number of turns:", len(conversation))
print("The model's question:", conversation[1]["content"])
print("The fictional answer:", conversation[2]["content"])


# CELL: Preserve a small research record
model_used = HOSTED_MODEL if ROUTE == "openrouter" else LOCAL_MODEL
research_record = {
    "route": ROUTE,
    "requested_model": model_used,
    "research_question": research_question,
    "interviewer_advice": interviewer_advice,
    "persona": persona,
    "conversation": conversation,
}

print(json.dumps(research_record, indent=2))

# ONE CHANGE FOR EACH EXERCISE:
# 1. Edit only interviewer_advice and rerun Exercise 1. What changes in the probe?
# 2. Edit the persona fields and rerun Exercise 2. What changes in the answer?
