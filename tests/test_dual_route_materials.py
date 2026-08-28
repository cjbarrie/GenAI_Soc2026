import ast
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def task_source(week: int) -> str:
    return (ROOT / "assessments" / "weekly_coding" / f"session{week:02d}_task.py").read_text()


def test_recorded_contingency_covers_every_coding_week() -> None:
    data = json.loads((ROOT / "data" / "dual_route_recorded_outputs.json").read_text())
    assert all(f"session{week:02d}" in data for week in range(1, 14))
    assert all({"openrouter", "ollama"} <= set(data[f"session{week:02d}"]) for week in range(1, 14))


def test_route_progression_and_first_function() -> None:
    for week in (1, 2, 8):
        source = task_source(week)
        assert "client.chat.send" in source
        assert "ollama.chat" in source
    for week in range(3, 8):
        source = task_source(week)
        assert 'ROUTE = "ollama"' in source
        assert "client.chat.send" in source
        assert "ollama.chat" in source
    for week in range(1, 9):
        tree = ast.parse(task_source(week))
        assert not any(isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) for node in ast.walk(tree))
    assert "def choose_action(" in task_source(9)


def test_no_key_is_embedded_in_student_tasks() -> None:
    for week in range(1, 14):
        source = task_source(week)
        assert "sk-or-" not in source
        assert "getpass(" in source or week in (11, 12)
