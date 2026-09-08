import ast
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def notebook_sources(week: int) -> list[str]:
    files = list((ROOT / "workbook" / f"session{week:02d}").glob("*.ipynb"))
    assert len(files) == 1
    path = files[0]
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


def test_all_student_notebooks_prepare_colab_before_importing_sdks() -> None:
    for week in range(1, 14):
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
        if week >= 3:
            assert "setup_sys.path.insert(0, course_root_text)" in setup
        if week == 13:
            assert 'course_packages["pandas"]' in setup


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


def test_weeks_3_to_12_select_openrouter_in_colab() -> None:
    for week in (3, 4, 5, 6, 7, 9, 10, 11, 12):
        source = "\n".join(notebook_sources(week))
        assert 'ROUTE = "openrouter" if IN_COLAB else "ollama"' in source


def test_dual_route_weeks_degrade_explicitly_in_colab() -> None:
    week8 = "\n".join(notebook_sources(8))
    assert 'if IN_COLAB:\n        local_raw = None' in week8
    assert "local_matches = None if IN_COLAB else 0" in week8
    assert "local_mean = None if IN_COLAB else" in week8

    week13 = "\n".join(notebook_sources(13))
    assert 'routes = ["openrouter"] if IN_COLAB else ["openrouter", "ollama"]' in week13
    assert "Ollama rows" in week13
