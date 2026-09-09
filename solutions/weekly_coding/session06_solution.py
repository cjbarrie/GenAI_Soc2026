"""Worked solution for Session 6: reconstruct the realized interview path."""


def audit_interview(turns):
    """Preserve counts, topic order, and the exact adaptive probes delivered."""
    audit = {
        "interviewer_turns": 0,
        "participant_turns": 0,
        "protocol_questions": 0,
        "adaptive_probes": 0,
        "topics": [],
        "probe_log": [],
    }

    for turn_number, turn in enumerate(turns, start=1):
        if turn["role"] == "interviewer":
            audit["interviewer_turns"] += 1
            if turn["source"] == "protocol":
                audit["protocol_questions"] += 1
            elif turn["source"] == "adaptive_probe":
                audit["adaptive_probes"] += 1
                audit["probe_log"].append(
                    {
                        "turn_number": turn_number,
                        "text": turn["text"],
                        "responds_to": turn["responds_to"],
                    }
                )
        elif turn["role"] == "participant":
            audit["participant_turns"] += 1

        topic = turn.get("topic")
        if topic and topic not in audit["topics"]:
            audit["topics"].append(topic)

    return audit


def run_checks():
    turns = [
        {"role": "interviewer", "text": "Tell me about a moment.", "topic": "participation", "source": "protocol", "responds_to": None},
        {"role": "participant", "text": "I decided not to speak.", "topic": "participation", "source": "participant_response", "responds_to": 1},
        {"role": "interviewer", "text": "What shaped that decision?", "topic": "status", "source": "adaptive_probe", "responds_to": 2},
        {"role": "participant", "text": "A senior student dominated.", "topic": "status", "source": "participant_response", "responds_to": 3},
    ]
    audit = audit_interview(turns)
    assert audit["interviewer_turns"] == 2
    assert audit["participant_turns"] == 2
    assert audit["protocol_questions"] == 1
    assert audit["adaptive_probes"] == 1
    assert audit["topics"] == ["participation", "status"]
    assert audit["probe_log"][0] == {
        "turn_number": 3,
        "text": "What shaped that decision?",
        "responds_to": 2,
    }


if __name__ == "__main__":
    run_checks()
    print("All Session 6 checks passed.")
