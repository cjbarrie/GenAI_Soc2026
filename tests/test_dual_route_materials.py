import ast
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def notebook_sources(week: int) -> list[str]:
    names = {
        1: "session01_research_technology.ipynb",
        2: "session02_annotation_measurement.ipynb",
    }
    path = ROOT / "workbook" / f"session{week:02d}" / names[week]
    notebook = json.loads(path.read_text())
    return ["".join(cell["source"]) for cell in notebook["cells"]]


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


def test_intro_notebooks_prepare_colab_before_importing_sdks() -> None:
    for week in (1, 2):
        sources = notebook_sources(week)
        setup_index = next(i for i, source in enumerate(sources) if "course_packages" in source)
        import_index = next(i for i, source in enumerate(sources) if "from openrouter import OpenRouter" in source)
        setup = sources[setup_index]

        assert setup_index < import_index
        assert "setup_sys.executable" in setup
        assert '"-m",\n                "pip",\n                "install"' in setup
        assert '"openrouter>=0.6,<1"' in setup
        assert '"ollama>=0.6,<1"' in setup
        assert "https://github.com/cjbarrie/GenAI_Soc2026.git" in setup
        assert "uv sync" in setup
        assert "uv run jupyter lab" in setup


def test_intro_notebooks_do_not_contact_ollama_from_colab() -> None:
    for week in (1, 2):
        sources = notebook_sources(week)
        local_call = next(
            source
            for source in sources
            if "ollama.chat(" in source and source.lstrip().startswith("if IN_COLAB:")
        )
        comparisons = next(
            source
            for source in sources
            if "is None else" in source
            and ("routes_match" in source or "routes_agree" in source)
        )

        assert "if IN_COLAB:" in local_call
        assert "Ollama was not called" in local_call
        assert "= None" in local_call
        assert "is None else" in comparisons
