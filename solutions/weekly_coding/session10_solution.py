"""Offline checks for the Week 10 relationship-mediation exercise."""

import json

FACTS = {
    "commitment": "help with a move at 8 a.m. Saturday",
    "work_conflict_known": "noon Friday",
    "message_sent": "9 p.m. Friday",
    "reliance": "the recipient declined paid help because of the promise",
    "repairs": ["pay half the cost of a last-minute mover", "help on Sunday"],
}


def make_prompt(relationship, instruction, facts):
    return f"""{instruction}

Relationship: {relationship}

Facts:
{json.dumps(facts, indent=2)}

Return only the message that could be sent."""


def make_record(relationship, instruction_name, raw_message):
    return {
        "relationship": relationship,
        "instruction": instruction_name,
        "facts": FACTS.copy(),
        "raw_message": raw_message,
    }


def run_checks():
    prompt = make_prompt("close friend", "Acknowledge the obligation.", FACTS)
    assert "Relationship: close friend" in prompt
    assert "declined paid help" in prompt
    assert "help on Sunday" in prompt
    record = make_record("colleague", "obligation", "A raw model return")
    assert record["relationship"] == "colleague"
    assert record["raw_message"] == "A raw model return"
    assert record["facts"] is not FACTS
    assert set(record) == {"relationship", "instruction", "facts", "raw_message"}


if __name__ == "__main__":
    run_checks()
    print("All Session 10 checks passed.")
