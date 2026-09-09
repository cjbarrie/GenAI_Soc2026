from solutions.weekly_coding.session06_solution import audit_interview, run_checks


def test_session06_worked_solution():
    run_checks()


def test_probe_wording_and_link_are_preserved():
    turns = [
        {"role": "participant", "text": "It felt risky.", "topic": "risk", "source": "participant_response", "responds_to": None},
        {"role": "interviewer", "text": "What made it feel risky?", "topic": "risk", "source": "adaptive_probe", "responds_to": 1},
    ]
    audit = audit_interview(turns)
    assert audit["probe_log"] == [{"turn_number": 2, "text": "What made it feel risky?", "responds_to": 1}]
