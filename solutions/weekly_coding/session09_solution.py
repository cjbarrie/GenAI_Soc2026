"""Offline checks for the Week 9 worker-controlled review record."""


def validate_reply_record(record):
    """Check the three requirements stated in the exercise."""
    output = record["parsed_output"]
    return {
        "compares_with_baseline": output["baseline_comparison"] == "model_outperforms_baseline",
        "does_not_make_causal_claim": output["causal_claim"] == "not_supported",
        "asks_for_more_evidence": output["decision_status"] == "needs_more_information",
    }


def run_checks():
    parsed = {
        "baseline_comparison": "model_outperforms_baseline",
        "causal_claim": "not_supported",
        "decision_status": "needs_more_information",
        "explanation": ["Accuracy exceeds the baseline but does not establish causality."],
        "questions_for_worker": ["Which errors matter for the decision?"],
        "data_science_escalation": "Request calibration and false-positive results.",
    }
    reply = {"parsed_output": parsed}
    assert all(validate_reply_record(reply).values())

    work_record = {
        "first_model_reply": reply,
        "worker_next_step": "ask_model_again",
        "worker_question": "What information is missing?",
        "second_model_reply": reply,
        "worker_final_action": "escalate_to_data_science",
        "worker_reason": "Specialist evidence is still required.",
    }
    assert work_record["worker_next_step"] == "ask_model_again"
    assert work_record["second_model_reply"] is not None
    assert work_record["worker_final_action"] == "escalate_to_data_science"


if __name__ == "__main__":
    run_checks()
    print("All Session 9 checks passed.")
