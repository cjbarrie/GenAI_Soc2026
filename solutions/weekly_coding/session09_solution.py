"""Offline checks for the Week 9 human-judgment records."""


def record_human_judgment(recommendation, stated_certainty, human_action, human_reason):
    if human_action == "accept_recommendation":
        next_step = "Proceed with the recommendation."
    elif human_action == "ask_for_more_information":
        next_step = "Request additional evidence before deciding."
    elif human_action == "escalate_to_specialist":
        next_step = "Send the evidence and advice to a specialist."
    elif human_action == "reject_recommendation":
        next_step = "Do not proceed with the recommendation."
    else:
        raise ValueError("invalid human action")
    return {
        "recommendation": recommendation,
        "stated_certainty": stated_certainty,
        "human_action": human_action,
        "human_reason": human_reason,
        "next_step": next_step,
    }


def run_checks():
    certainty_levels = [0.55, 0.75, 0.95]
    actions = [
        "ask_for_more_information",
        "escalate_to_specialist",
        "accept_recommendation",
    ]
    records = [
        record_human_judgment("request_more_evidence", certainty, actions[index], "reason")
        for index, certainty in enumerate(certainty_levels)
    ]
    assert [record["stated_certainty"] for record in records] == certainty_levels
    assert {record["recommendation"] for record in records} == {"request_more_evidence"}
    assert records[1]["next_step"] == "Send the evidence and advice to a specialist."


if __name__ == "__main__":
    run_checks()
    print("All Session 9 checks passed.")
