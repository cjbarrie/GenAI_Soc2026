import json
from pathlib import Path
import runpy
from types import SimpleNamespace

from solutions.weekly_coding.session06_solution import (
    build_conversation,
    build_interviewer_messages,
    build_persona_messages,
    build_record,
    inspect_probe_and_context,
    run_checks,
)


ROOT = Path(__file__).resolve().parents[1]


def test_session06_worked_solution():
    run_checks()


def test_advice_is_visible_and_easy_to_change():
    first = build_interviewer_messages("question", "ask for an example", "answer")
    changed = build_interviewer_messages("question", "ask for chronology", "answer")
    assert "ask for an example" in first[0]["content"]
    assert "ask for chronology" in changed[0]["content"]
    assert first[1] == changed[1] == {"role": "user", "content": "answer"}


def test_persona_and_probe_are_both_sent_to_second_call():
    persona = {"role": "junior evaluator", "known_episode": "a disagreement"}
    messages = build_persona_messages(persona, "What happened next?")
    assert '"role": "junior evaluator"' in messages[1]["content"]
    assert '"known_episode": "a disagreement"' in messages[1]["content"]
    assert "What happened next?" in messages[1]["content"]
    assert "fictional test data" in messages[0]["content"]


def test_conversation_state_preserves_order_and_nested_values():
    conversation = build_conversation("first answer", "probe", "fictional answer")
    assert [turn["role"] for turn in conversation] == ["user", "assistant", "user"]
    assert conversation[1]["content"] == "probe"
    assert conversation[2]["content"] == "fictional answer"


def test_boolean_checks_negative_indexing_and_slicing():
    conversation = build_conversation("answer", "Why?", "fictional answer")
    inspection = inspect_probe_and_context("Why?", conversation)
    assert inspection["is_question"] is True
    assert inspection["mentions_because"] is False
    assert inspection["latest_turn"] == conversation[-1]
    assert inspection["recent_context"] == conversation[-2:]


def test_record_preserves_inputs_and_realized_conversation():
    persona = {"role": "junior evaluator"}
    conversation = build_conversation("answer", "probe", "fictional answer")
    record = build_record(
        "ollama", "local-model", "question", "advice", conversation, persona
    )
    assert record["interviewer_advice"] == "advice"
    assert record["persona"] == persona
    assert record["conversation"] == conversation


def test_notebook_is_valid_and_matches_the_two_exercises():
    path = ROOT / "workbook/session06/session06_conversational_treatments.ipynb"
    notebook = json.loads(path.read_text())
    source = "\n".join("".join(cell.get("source", [])) for cell in notebook["cells"])
    assert 'if ROUTE == "openrouter" and not os.getenv("OPENROUTER_API_KEY")' in source
    assert "interviewer_advice" in source and "interviewer_messages" in source
    assert "persona = {" in source and "persona_messages" in source
    assert "Raw interviewer return" in source and "Raw synthetic return" in source
    assert "conversation.append" in source
    assert 'conversation[1]["content"]' in source
    assert 'interviewer_probe.endswith("?")' in source
    assert 'persona.get("age", "not supplied")' in source
    assert "conversation[-1]" in source and "conversation[-2:]" in source
    assert "evidence about real hiring" in source


def test_downloadable_task_does_not_require_openrouter_key_for_ollama():
    task = (ROOT / "assessments/weekly_coding/session06_task.py").read_text()
    assert 'if ROUTE == "openrouter" and not os.getenv("OPENROUTER_API_KEY")' in task
    assert "interviewer_advice" in task and "persona = {" in task
    assert "conversation.append" in task
    assert 'interviewer_probe.endswith("?")' in task
    assert 'persona.get("age", "not supplied")' in task
    assert "conversation[-1]" in task and "conversation[-2:]" in task
    assert "shared_path" not in task and "case_path" not in task


def test_downloadable_task_runs_through_ollama_with_recorded_returns(monkeypatch):
    calls = []

    def fake_chat(*, model, messages, think, options):
        calls.append(messages)
        content = f"return for {messages[-1]['content']}"
        return SimpleNamespace(message=SimpleNamespace(content=content))

    monkeypatch.setattr("ollama.chat", fake_chat)
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    namespace = runpy.run_path(ROOT / "assessments/weekly_coding/session06_task.py")
    assert [len(messages) for messages in calls] == [2, 2]
    assert namespace["research_record"]["route"] == "ollama"
    assert len(namespace["research_record"]["conversation"]) == 3


def test_downloadable_task_openrouter_branch_without_network(monkeypatch):
    calls = []

    class FakeChat:
        def send(self, *, model, messages, temperature):
            calls.append(messages)
            message = SimpleNamespace(content=f"return for {messages[-1]['content']}")
            return SimpleNamespace(choices=[SimpleNamespace(message=message)])

    class FakeOpenRouter:
        def __init__(self, api_key):
            assert api_key == "test-key"
            self.chat = FakeChat()

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            return False

    task_path = ROOT / "assessments/weekly_coding/session06_task.py"
    source = task_path.read_text().replace(
        'ROUTE = "ollama"  # change to "openrouter" if preferred',
        'ROUTE = "openrouter"',
    )
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-key")
    monkeypatch.setattr("openrouter.OpenRouter", FakeOpenRouter)
    namespace = {"__name__": "__main__", "__file__": str(task_path)}
    exec(compile(source, str(task_path), "exec"), namespace)
    assert [len(messages) for messages in calls] == [2, 2]
    assert namespace["research_record"]["route"] == "openrouter"
    assert len(namespace["research_record"]["conversation"]) == 3
