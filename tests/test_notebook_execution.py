"""Execute every student notebook with controlled, correctly shaped model returns."""

from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import pytest


ROOT = Path(__file__).resolve().parents[1]


def response_text(messages: list[dict], schema_name: str | None = None, schema: dict | None = None) -> str:
    prompt = str(messages[-1].get("content", ""))
    properties = set((schema or {}).get("properties", {}))
    if schema_name == "visible_sequence" or "observable_change" in properties:
        return json.dumps(
            {
                "observable_change": "One figure changes position.",
                "visible_evidence": ["The head position differs."],
                "interpretation_withheld": "Identity and motive.",
            }
        )
    if schema_name in {"polviews_prediction", "opinion_prediction"} or "predicted_category" in properties:
        value = {"predicted_category": 4}
        if "probabilities" in properties:
            value["probabilities"] = [0.1, 0.1, 0.15, 0.3, 0.15, 0.1, 0.1]
        return json.dumps(value)
    if schema_name == "agent_action" or properties == {"action", "reason"}:
        return json.dumps({"action": "speak calmly", "reason": "The observation changed."})
    if schema_name == "join_action" or properties == {"action"}:
        return json.dumps({"action": "JOIN"})
    if schema_name == "tool_request" or "tool_name" in properties:
        return json.dumps({"tool_name": "search_course_corpus", "query": "errors research"})
    if schema_name == "source_claim" or "source_id" in properties:
        return json.dumps({"claim": "Errors can enter during several stages.", "source_id": "s2"})
    if schema_name == "audit_response" or "approval" in properties:
        return json.dumps({"approval": 60, "explanation": "A bounded test response."})
    if "provisional theme" in prompt:
        return json.dumps(
            {
                "theme": "Participation differs",
                "evidence_id": "e01",
                "question_for_researcher": "What explains the difference?",
            }
        )
    if "survey message" in prompt.lower():
        return "The proposal creates a pathway to legal status for people meeting the stated requirements."
    if "interview" in prompt.lower():
        return "Can you describe a specific moment?"
    return "A short bounded stage response."


class FakeOpenRouter:
    def __init__(self, **_: object) -> None:
        pass

    def __enter__(self) -> "FakeOpenRouter":
        return self

    def __exit__(self, *_: object) -> bool:
        return False

    @property
    def chat(self) -> "FakeOpenRouter":
        return self

    def send(self, **kwargs: object) -> SimpleNamespace:
        response_format = kwargs.get("response_format") or {}
        schema_record = response_format.get("json_schema") or {}
        content = response_text(
            kwargs["messages"], schema_record.get("name"), schema_record.get("schema")
        )
        return SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content=content))],
            usage=SimpleNamespace(prompt_tokens=12, completion_tokens=8),
        )


def fake_ollama(**kwargs: object) -> SimpleNamespace:
    supplied_format = kwargs.get("format")
    schema = supplied_format if isinstance(supplied_format, dict) else None
    content = response_text(kwargs["messages"], schema=schema)
    return SimpleNamespace(
        message=SimpleNamespace(content=content), prompt_eval_count=12, eval_count=8
    )


@pytest.mark.parametrize("week", range(3, 14))
@pytest.mark.parametrize("runtime", ["local", "colab"])
def test_followup_notebook_executes_without_live_services(
    week: int, runtime: str, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.chdir(ROOT)
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-only-key")
    files = list((ROOT / "workbook" / f"session{week:02d}").glob("*.ipynb"))
    assert len(files) == 1
    notebook = json.loads(files[0].read_text())
    code_cells = [
        "".join(cell["source"])
        for cell in notebook["cells"]
        if cell["cell_type"] == "code"
    ]

    namespace: dict[str, object] = {"__name__": "__main__"}
    exec(code_cells[0], namespace)
    exec(code_cells[1], namespace)
    namespace["OpenRouter"] = FakeOpenRouter
    namespace["ollama"].chat = fake_ollama
    namespace["IN_COLAB"] = runtime == "colab"

    for source in code_cells[2:]:
        if week == 12 and "output_dir = ROOT" in source:
            namespace["ROOT"] = tmp_path
        exec(source, namespace)

    if runtime == "colab" and week in {3, 4, 5, 6, 7, 9, 10, 11, 12}:
        assert namespace["ROUTE"] == "openrouter"
    if week == 8 and runtime == "colab":
        assert namespace["local_results"] == []
        assert namespace["local_mean"] is None
    if week == 13:
        expected_routes = ["openrouter"] if runtime == "colab" else ["openrouter", "ollama"]
        assert namespace["routes"] == expected_routes
