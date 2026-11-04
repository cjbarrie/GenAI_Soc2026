"""Offline checks for the Week 10 relationship-mediation exercise."""

import json

FACTS = {
    "commitment": "help with a move at 8 a.m. Saturday",
    "reliance": "the recipient declined paid help because of the promise",
}


def make_prompt(relationship, instruction, disclose_assistance=False):
    disclosure_request = ""
    if disclose_assistance:
        disclosure_request = "\nDisclose that an AI writing assistant helped."
    return f"""{instruction}

Relationship: {relationship}

Facts:
{json.dumps(FACTS, indent=2)}
{disclosure_request}"""


def make_record(relationship, raw_message, disclose_assistance=False):
    return {
        "relationship": relationship,
        "disclose_assistance": disclose_assistance,
        "facts": FACTS.copy(),
        "raw_message": raw_message,
    }


def run_checks():
    ordinary_prompt = make_prompt("close friend", "Acknowledge the obligation.")
    disclosed_prompt = make_prompt(
        "close friend",
        "Acknowledge the obligation.",
        disclose_assistance=True,
    )
    assert "Relationship: close friend" in ordinary_prompt
    assert "AI writing assistant" not in ordinary_prompt
    assert "AI writing assistant" in disclosed_prompt

    record = make_record(
        relationship="colleague",
        raw_message="A raw model return",
        disclose_assistance=True,
    )
    assert record["disclose_assistance"] is True
    assert record["facts"] is not FACTS
    assert set(record) == {
        "relationship",
        "disclose_assistance",
        "facts",
        "raw_message",
    }

    numbered = []
    for position, relationship in enumerate(["colleague", "friend"], start=1):
        numbered.append((position, relationship))
    assert numbered == [(1, "colleague"), (2, "friend")]


if __name__ == "__main__":
    run_checks()
    print("All Session 10 checks passed.")
