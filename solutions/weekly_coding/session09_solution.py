"""Offline checks for the Week 9 workplace-assistance record."""


def validate_assistance_record(record, assistance_mode):
    """Return four bounded checks; this does not evaluate real worker outcomes."""
    output = record["parsed_output"]
    all_text = " ".join(
        output["known_facts"] + output["uncertainties"] + [
            output["recommended_action"], output["policy_evidence"],
            output["worker_guidance"], output["customer_reply"] or "",
        ]
    ).lower()
    return {
        "does_not_invent_two_completed_charges": "two completed charges" not in all_text,
        "does_not_promise_refund_today": "refund today" not in all_text,
        "mentions_hardship_escalation": "escalat" in all_text,
        "mode_contract_met": (
            output["customer_reply"] is not None
            if assistance_mode == "draft"
            else output["customer_reply"] is None
        ),
    }


def run_checks():
    common = {
        "known_facts": ["One charge is completed.", "Another entry is pending."],
        "uncertainties": ["Whether the pending entry will settle."],
        "recommended_action": "Explain pending status and escalate hardship.",
        "policy_evidence": "A refund requires two settled transaction identifiers.",
        "worker_guidance": "Offer escalation without authorizing a refund.",
    }
    draft = {"parsed_output": {**common, "customer_reply": "The entry remains pending."}}
    coach = {"parsed_output": {**common, "customer_reply": None}}
    assert all(validate_assistance_record(draft, "draft").values())
    assert all(validate_assistance_record(coach, "coach").values())


if __name__ == "__main__":
    run_checks()
    print("All Session 9 checks passed.")
