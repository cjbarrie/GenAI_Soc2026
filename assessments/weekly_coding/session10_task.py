"""Week 10: compare LLM-mediated apologies without inventing human outcomes.

New Python ideas: default parameter values, Boolean values, keyword arguments
and ``enumerate()``. The model generates messages. The researcher interprets
the text. Recipient and relationship outcomes remain unobserved.
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
HOSTED_MODEL = OPENROUTER_MODEL
LOCAL_MODEL = OLLAMA_MODEL
USE_RECORDED = os.getenv("COURSE_USE_RECORDED", "0") == "1"
ROUTE = "ollama"  # use "openrouter" for the hosted route

# CELL: Store the fixed facts and the two writing instructions
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
    "State the commitment that was broken, acknowledge the late notice and the "
    "plan made in reliance on the promise, explain only the supplied facts, and "
    "offer both available forms of repair. Do not invent feelings, relationship "
    "history or motives."
)

# Recorded outputs demonstrate the code path during an outage. They are not
# observations of human communication or relationship outcomes.
recorded_returns = {
    ("thin", "close friend", False): (
        "I’m sorry, but I can’t help with the move tomorrow because I have to work. "
        "I can help on Sunday instead or pay half the cost of a mover."
    ),
    ("obligation", "colleague", False): (
        "I need to apologize for breaking my commitment to help at 8 tomorrow and "
        "for waiting until 9 tonight to tell you. I learned at noon that I must work. "
        "You declined paid help because you expected me, so I can either pay half the "
        "cost of a last-minute mover or help on Sunday."
    ),
    ("obligation", "close friend", False): (
        "I’m sorry. I promised to help at 8 tomorrow, and I should have told you at "
        "noon when I learned I had to work. You turned down paid help because you were "
        "counting on me. I can pay half the cost of a mover or help on Sunday."
    ),
    ("obligation", "romantic partner", False): (
        "I broke my promise to help at 8 tomorrow, and I waited too long to tell you. "
        "You declined paid help because you relied on me. I can pay half the cost of a "
        "last-minute mover or help on Sunday."
    ),
    ("obligation", "close friend", True): (
        "I’m sorry. I promised to help at 8 tomorrow, and I should have told you at "
        "noon when I learned I had to work. You turned down paid help because you were "
        "counting on me. I can pay half the cost of a mover or help on Sunday. I used "
        "an AI writing assistant to help me draft this message."
    ),
}

# CELL: Define a function with a default Boolean parameter
def draft_message(
    relationship,
    instruction_name,
    route,
    disclose_assistance=False,
):
    """Return a record containing one model-generated message and its inputs."""
    if instruction_name == "thin":
        instruction = thin_instruction
    elif instruction_name == "obligation":
        instruction = obligation_instruction
    else:
        raise ValueError("instruction_name must be 'thin' or 'obligation'")

    disclosure_request = ""
    if disclose_assistance:
        disclosure_request = (
            "\nEnd with this factual disclosure: I used an AI writing assistant "
            "to help me draft this message."
        )

    prompt = f"""{instruction}

Relationship: {relationship}

Facts:
{json.dumps(facts, indent=2)}
{disclosure_request}

Return only the message that could be sent."""

    print("relationship:", relationship, type(relationship))
    print("instruction_name:", instruction_name, type(instruction_name))
    print("disclose_assistance:", disclose_assistance, type(disclose_assistance))
    print("route:", route, type(route))
    print("Prompt sent to the model:\n", prompt)

    if USE_RECORDED:
        key = (instruction_name, relationship, disclose_assistance)
        try:
            raw_output = recorded_returns[key]
        except KeyError as error:
            raise KeyError(
                "No recorded return exists for that combination. Use a live route or "
                "restore one of the supplied combinations."
            ) from error
        model_name = "recorded-teaching-return"
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
        model_name = OPENROUTER_MODEL
    elif route == "ollama":
        if ollama is None:
            raise ModuleNotFoundError("Run 'uv sync --frozen' before using Ollama.")
        response = ollama.chat(think=False,
            model=OLLAMA_MODEL,
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": 0},
        )
        raw_output = response.message.content
        model_name = OLLAMA_MODEL
    else:
        raise ValueError("route must be 'openrouter' or 'ollama'")

    record = {
        "relationship": relationship,
        "instruction_name": instruction_name,
        "disclose_assistance": disclose_assistance,
        "route": "recorded" if USE_RECORDED else route,
        "model": model_name,
        "facts": facts.copy(),
        "raw_message": raw_output,
    }
    print("Raw model return:\n", raw_output)
    print("Function output type:", type(record))
    return record

# CELL: Compare two instructions while holding the relationship fixed
thin_record = draft_message(
    relationship="close friend",
    instruction_name="thin",
    route=ROUTE,
)
obligation_record = draft_message(
    relationship="close friend",
    instruction_name="obligation",
    route=ROUTE,
)
print("\nTHIN INSTRUCTION\n", thin_record["raw_message"])
print("\nRELATIONAL-OBLIGATION INSTRUCTION\n", obligation_record["raw_message"])

# CELL: Repeat the obligation instruction across three relationships
relationships = ["colleague", "close friend", "romantic partner"]
relationship_records = []
for position, relationship in enumerate(relationships, start=1):
    print("\nCondition", position, "of", len(relationships))
    record = draft_message(
        relationship=relationship,
        instruction_name="obligation",
        route=ROUTE,
    )
    relationship_records.append(record)

# CELL: Make assistance disclosure an explicit input
undisclosed_record = obligation_record
disclosed_record = draft_message(
    relationship="close friend",
    instruction_name="obligation",
    route=ROUTE,
    disclose_assistance=True,
)
print("\nWITHOUT DISCLOSURE REQUEST\n", undisclosed_record["raw_message"])
print("\nWITH DISCLOSURE REQUEST\n", disclosed_record["raw_message"])

# CELL: Keep researcher notes separate from generated text
researcher_notes = {
    "instruction_comparison": "",
    "relationship_comparison": "",
    "disclosure_comparison": "",
    "invented_facts": [],
    "human_evidence_needed": (
        "Recipient interpretations, sender experience and later interaction data."
    ),
}
print(json.dumps(researcher_notes, indent=2))

# ONE CHANGE: edit one relationship description or set disclose_assistance=True
# for another relationship. Do not treat the generated difference as a human effect.
