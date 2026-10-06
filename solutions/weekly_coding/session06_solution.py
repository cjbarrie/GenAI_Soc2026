"""Instructor checks for the Week 6 adaptive-interview state."""


def build_opening(protocol, first_answer):
    """Return the two messages sent to the first model call."""
    return [
        {"role": "system", "content": protocol},
        {"role": "user", "content": first_answer},
    ]


def build_paths(conversation, first_probe, shared_answer, case_answer):
    """Create two independent paths that share the same earlier messages."""
    shared_path = conversation.copy()
    shared_path.append({"role": "assistant", "content": first_probe})
    shared_path.append({"role": "user", "content": shared_answer})

    case_path = conversation.copy()
    case_path.append({"role": "assistant", "content": first_probe})
    case_path.append({"role": "user", "content": case_answer})
    return shared_path, case_path


def build_record(route, model, conversation, first_raw, shared_path, shared_raw,
                 case_path, case_raw, shared_review, case_review):
    """Keep model inputs, raw returns and researcher reviews together."""
    return {
        "route": route,
        "requested_model": model,
        "opening_messages": conversation,
        "first_raw_return": first_raw,
        "shared_path": shared_path,
        "shared_raw_return": shared_raw,
        "case_path": case_path,
        "case_raw_return": case_raw,
        "shared_review": shared_review,
        "case_review": case_review,
    }


def run_checks():
    protocol = "Ask for a concrete episode without introducing a cause."
    first_answer = "Evaluator: I could picture her working here."
    first_probe = "What did she say or do that made you think that?"
    shared_answer = "Evaluator: We had both rowed in college."
    case_answer = "Evaluator: She challenged the case assumption calmly."

    conversation = build_opening(protocol, first_answer)
    shared_path, case_path = build_paths(
        conversation, first_probe, shared_answer, case_answer
    )

    assert len(conversation) == 2
    assert len(shared_path) == 4
    assert len(case_path) == 4
    assert shared_path is not case_path
    assert shared_path[:3] == case_path[:3]
    assert shared_path[-1]["content"] == shared_answer
    assert case_path[-1]["content"] == case_answer

    changed_shared, changed_case = build_paths(
        conversation,
        first_probe,
        shared_answer,
        "Evaluator: She asked careful questions about the firm's clients.",
    )
    assert len(changed_shared) == 4
    assert len(changed_case) == 4
    assert changed_case[-1] != case_path[-1]
    assert len(conversation) == 2


if __name__ == "__main__":
    run_checks()
    print("All Session 6 checks passed.")
