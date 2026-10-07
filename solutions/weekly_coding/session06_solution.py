"""Instructor checks for the Week 6 interviewer and persona exercise."""

import json


def build_interviewer_messages(research_question, advice, first_answer):
    """Put the research question, interviewer advice and answer into model messages."""
    return [
        {
            "role": "system",
            "content": (
                f"Research question: {research_question}\n"
                f"Advice for the interviewer: {advice}\n"
                "Return only the next interview question."
            ),
        },
        {"role": "user", "content": first_answer},
    ]


def build_persona_messages(persona, probe):
    """Put a fictional persona and the generated probe into a second model input."""
    persona_text = json.dumps(persona, indent=2)
    return [
        {
            "role": "system",
            "content": (
                "Generate fictional test data for an interview protocol. "
                "Use only the supplied persona details and say when the persona "
                "does not know. Do not present the answer as evidence about real people."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Fictional persona:\n{persona_text}\n\n"
                f"Interview question:\n{probe}"
            ),
        },
    ]


def build_conversation(first_answer, probe, synthetic_answer):
    """Reconstruct the ordered turns that the interview system would retain."""
    conversation = [{"role": "user", "content": first_answer}]
    conversation.append({"role": "assistant", "content": probe})
    conversation.append({"role": "user", "content": synthetic_answer})
    return conversation


def build_record(route, model, research_question, advice, conversation, persona):
    """Keep editable inputs and the realized conversation together."""
    return {
        "route": route,
        "requested_model": model,
        "research_question": research_question,
        "interviewer_advice": advice,
        "persona": persona,
        "conversation": conversation,
    }


def run_checks():
    question = "How do evaluators decide that a candidate is a good cultural fit?"
    advice = "Ask for one concrete example without suggesting a cause."
    answer = "Evaluator: I could picture her working here."
    probe = "What did she say or do that made you think that?"
    synthetic_answer = "She challenged a case assumption calmly."
    persona = {
        "role": "junior evaluator",
        "known_episode": "the candidate challenged a case assumption calmly",
    }

    interviewer_messages = build_interviewer_messages(question, advice, answer)
    assert len(interviewer_messages) == 2
    assert advice in interviewer_messages[0]["content"]
    assert interviewer_messages[1]["content"] == answer

    changed = build_interviewer_messages(
        question, "Ask how the evaluator felt at that moment.", answer
    )
    assert changed[0] != interviewer_messages[0]
    assert changed[1] == interviewer_messages[1]

    persona_messages = build_persona_messages(persona, probe)
    assert '"role": "junior evaluator"' in persona_messages[1]["content"]
    assert probe in persona_messages[1]["content"]

    conversation = build_conversation(answer, probe, synthetic_answer)
    assert len(conversation) == 3
    assert conversation[1]["role"] == "assistant"
    assert conversation[2]["content"] == synthetic_answer

    record = build_record(
        "ollama", "local-model", question, advice, conversation, persona
    )
    assert record["interviewer_advice"] == advice
    assert record["persona"] == persona
    assert record["conversation"] == conversation


if __name__ == "__main__":
    run_checks()
    print("All Session 6 checks passed.")
