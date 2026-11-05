"""Offline checks for the Week 10 social-advice audit."""


def record_audit(
    situation,
    student_response_before,
    model_record,
    audit_answer,
    would_follow_model=False,
):
    return {
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


def run_checks():
    situation = {"id": "broken_commitment", "relationship": "close friend"}
    before = {"action": "call", "reason": "late notice"}
    model_record = {"parsed_output": {"proposed_action": "call and offer repair"}}
    unchanged_answer = {
        "important_difference": "The model adds repair.",
        "student_response_after": before,
    }
    unchanged = record_audit(situation, before, model_record, unchanged_answer)
    assert unchanged["would_follow_model"] is False
    assert unchanged["student_changed_response"] is False

    changed_answer = {
        "important_difference": "The model identifies a financial cost.",
        "student_response_after": {"action": "call and pay", "reason": "repair"},
    }
    changed = record_audit(
        situation,
        before,
        model_record,
        changed_answer,
        would_follow_model=True,
    )
    assert changed["would_follow_model"] is True
    assert changed["student_changed_response"] is True


if __name__ == "__main__":
    run_checks()
    print("All Session 10 checks passed.")
