import json
from pathlib import Path
import runpy
from types import SimpleNamespace

from solutions.weekly_coding.session06_solution import (
    build_opening,
    build_paths,
    build_record,
    run_checks,
)


ROOT = Path(__file__).resolve().parents[1]


def test_session06_worked_solution():
    run_checks()


def test_paths_share_history_without_mutating_opening():
    opening = build_opening("protocol", "first answer")
    shared_path, case_path = build_paths(
        opening, "first probe", "shared answer", "case answer"
    )

    assert opening == [
        {"role": "system", "content": "protocol"},
        {"role": "user", "content": "first answer"},
    ]
    assert shared_path[:3] == case_path[:3]
    assert shared_path[-1]["content"] == "shared answer"
    assert case_path[-1]["content"] == "case answer"


def test_record_preserves_both_paths_and_raw_returns():
    opening = build_opening("protocol", "first answer")
    shared_path, case_path = build_paths(
        opening, "first probe", "shared answer", "case answer"
    )
    record = build_record(
        "ollama", "local-model", opening, "first probe", shared_path,
        "shared probe", case_path, "case probe", {"responsive": True},
        {"responsive": False},
    )

    assert record["shared_path"][-1]["content"] == "shared answer"
    assert record["case_path"][-1]["content"] == "case answer"
    assert record["shared_raw_return"] == "shared probe"
    assert record["case_review"] == {"responsive": False}


def test_notebook_is_valid_and_uses_clean_branch_recreation():
    notebook_path = (
        ROOT / "workbook" / "session06" / "session06_conversational_treatments.ipynb"
    )
    notebook = json.loads(notebook_path.read_text())
    source = "\n".join(
        "".join(cell.get("source", [])) for cell in notebook["cells"]
    )

    assert 'shared_path = conversation.copy()' in source
    assert 'case_path = conversation.copy()' in source
    assert 'if ROUTE == "openrouter" and not os.getenv("OPENROUTER_API_KEY")' in source
    assert "rerun from the append cell onward" not in source
    assert "shared_review" in source and "case_review" in source


def test_downloadable_task_does_not_require_openrouter_key_for_ollama():
    task = (
        ROOT / "assessments" / "weekly_coding" / "session06_task.py"
    ).read_text()
    assert 'if ROUTE == "openrouter" and not os.getenv("OPENROUTER_API_KEY")' in task
    assert 'shared_path = conversation.copy()' in task
    assert 'case_path = conversation.copy()' in task


def test_downloadable_task_runs_through_ollama_with_recorded_returns(monkeypatch):
    calls = []

    def fake_chat(*, model, messages, think, options):
        calls.append(messages)
        content = f"probe for {messages[-1]['content']}"
        return SimpleNamespace(message=SimpleNamespace(content=content))

    monkeypatch.setattr("ollama.chat", fake_chat)
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    namespace = runpy.run_path(
        ROOT / "assessments" / "weekly_coding" / "session06_task.py"
    )

    assert [len(messages) for messages in calls] == [2, 4, 4]
    assert namespace["research_record"]["route"] == "ollama"
    assert namespace["research_record"]["shared_raw_return"].startswith("probe for")


def test_downloadable_task_openrouter_branch_without_network(monkeypatch):
    calls = []

    class FakeChat:
        def send(self, *, model, messages, temperature):
            calls.append(messages)
            content = f"probe for {messages[-1]['content']}"
            message = SimpleNamespace(content=content)
            return SimpleNamespace(choices=[SimpleNamespace(message=message)])

    class FakeOpenRouter:
        def __init__(self, api_key):
            assert api_key == "test-key"
            self.chat = FakeChat()

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            return False

    task_path = ROOT / "assessments" / "weekly_coding" / "session06_task.py"
    source = task_path.read_text().replace(
        'ROUTE = "ollama"  # change to "openrouter" if preferred',
        'ROUTE = "openrouter"',
    )
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-key")
    monkeypatch.setattr("openrouter.OpenRouter", FakeOpenRouter)
    namespace = {"__name__": "__main__", "__file__": str(task_path)}
    exec(compile(source, str(task_path), "exec"), namespace)

    assert [len(messages) for messages in calls] == [2, 4, 4]
    assert namespace["research_record"]["route"] == "openrouter"
    assert namespace["research_record"]["case_raw_return"].startswith("probe for")
