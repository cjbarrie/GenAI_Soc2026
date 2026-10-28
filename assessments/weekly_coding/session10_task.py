"""Week 10: compare LLM-mediated apologies without inventing human outcomes."""

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
HOSTED_MODEL = OPENROUTER_MODEL
LOCAL_MODEL = OLLAMA_MODEL

USE_RECORDED = os.getenv("COURSE_USE_RECORDED", "0") == "1"
ROUTE = "ollama"  # use "openrouter" for the hosted route

facts = {
    "commitment": "help with a move at 8 a.m. Saturday",
    "work_conflict_known": "noon Friday",
    "message_sent": "9 p.m. Friday",
    "reliance": "the recipient declined paid help because of the promise",
    "repairs": ["pay half the cost of a last-minute mover", "help on Sunday"],
}

thin_instruction = (
    "Write a message telling this person that I cannot help them move tomorrow. "
    "Use only the supplied facts and do not invent facts."
)
obligation_instruction = (
    "Write the message to this person. State the commitment that was broken, "
    "acknowledge the late notice and the plan they made in reliance on the promise, "
    "explain only the supplied facts, and offer both available forms of repair. "
    "Do not invent feelings, relationship history or motives."
)

recorded_returns = {
    ("thin", "close friend"): (
        "I’m sorry, but I can’t help with the move tomorrow because I have to work "
        "from 8 to 4. I can help on Sunday instead or pay half the cost of a mover."
    ),
    ("obligation", "colleague"): (
        "I need to apologize for breaking my commitment to help at 8 tomorrow and for "
        "waiting until 9 tonight to tell you. I learned at noon that I must work from "
        "8 to 4. You declined paid help because you expected me, so I can either pay "
        "half the cost of a last-minute mover or help on Sunday."
    ),
    ("obligation", "close friend"): (
        "I’m sorry. I promised to help at 8 tomorrow, and I should have told you at "
        "noon when I learned I had to work from 8 to 4. You turned down paid help "
        "because you were counting on me. I can pay half the cost of a last-minute "
        "mover or help on Sunday—please decide whether either would help."
    ),
    ("obligation", "romantic partner"): (
        "I broke my promise to help at 8 tomorrow, and I waited far too long to tell "
        "you after learning at noon that I have to work from 8 to 4. You declined paid "
        "help because you relied on me. I can pay half the cost of a last-minute mover "
        "or help on Sunday. You do not have to accept either option."
    ),
}


def draft_message(relationship, instruction_name, route):
    """Return one raw model-generated message for the supplied relationship."""
    if instruction_name == "thin":
        instruction = thin_instruction
    elif instruction_name == "obligation":
        instruction = obligation_instruction
    else:
        raise ValueError("instruction_name must be 'thin' or 'obligation'")

    prompt = f"""{instruction}

Relationship: {relationship}

Facts:
{json.dumps(facts, indent=2)}

Return only the message that could be sent."""

    print("Function input — relationship:", relationship, type(relationship))
    print("Function input — instruction_name:", instruction_name, type(instruction_name))
    print("Function input — route:", route, type(route))
    print("Prompt sent to the model:\n", prompt)

    if USE_RECORDED:
        try:
            raw_output = recorded_returns[(instruction_name, relationship)]
        except KeyError as error:
            raise KeyError(
                "No recorded return exists for that change. Set USE_RECORDED=False."
            ) from error
    elif route == "openrouter":
        if OpenRouter is None:
            raise ModuleNotFoundError("Run 'uv sync --frozen' before using OpenRouter.")
        api_key = os.getenv("OPENROUTER_API_KEY") or getpass("OpenRouter course key (hidden): ")
        with OpenRouter(api_key=api_key) as client:
            response = client.chat.send(
                model=OPENROUTER_MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
            )
        raw_output = response.choices[0].message.content
    elif route == "ollama":
        if ollama is None:
            raise ModuleNotFoundError("Run 'uv sync --frozen' before using Ollama.")
        response = ollama.chat(think=False,
            model=OLLAMA_MODEL,
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": 0},
        )
        raw_output = response.message.content
    else:
        raise ValueError("route must be 'openrouter' or 'ollama'")

    print("Raw model return:\n", raw_output)
    print("Function output type:", type(raw_output))
    return raw_output


# First hold the relationship fixed and change the instruction.
thin_message = draft_message("close friend", "thin", ROUTE)
obligation_message = draft_message("close friend", "obligation", ROUTE)
print("\nTHIN INSTRUCTION\n", thin_message)
print("\nRELATIONAL-OBLIGATION INSTRUCTION\n", obligation_message)

# Then hold the instruction and facts fixed; change the relationship.
relationships = ["colleague", "close friend", "romantic partner"]
records = []
for relationship in relationships:
    message = draft_message(relationship, "obligation", ROUTE)
    records.append({
        "relationship": relationship,
        "instruction": "obligation",
        "facts": facts.copy(),
        "raw_message": message,
    })

for record in records:
    print("\nRELATIONSHIP:", record["relationship"])
    print(record["raw_message"])

# These are researcher-written notes, not model judgments.
researcher_notes = {
    "invented_facts": [],
    "commitment_named": [],
    "late_notice_named": [],
    "reliance_named": [],
    "repairs_offered": [],
    "other_observations": [],
}
print("\nResearcher notes template:")
print(json.dumps(researcher_notes, indent=2))

reflection_questions = [
    "What changed between the two instructions for the close friend?",
    "What changed when only the relationship label changed?",
    "Did any output invent feelings, motives or relationship history?",
    "What would recipient data be needed to establish?",
    "Would disclosure of model assistance change the relational act?",
]
for question in reflection_questions:
    print("-", question)

# ONE CHANGE: edit one relationship description or one obligation, rerun, and compare.
