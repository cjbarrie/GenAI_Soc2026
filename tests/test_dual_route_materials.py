import ast
import json
import re
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
    assert all(f"session{week:02d}" in data for week in range(1, 12))
    assert all({"openrouter", "ollama"} <= set(data[f"session{week:02d}"]) for week in range(1, 12))


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
    assert "def record_human_judgment(" in task_source(9)


def test_no_key_is_embedded_in_student_tasks() -> None:
    for week in range(1, 12):
        source = task_source(week)
        assert "sk-or-" not in source
        assert "getpass(" in source


def test_all_student_notebooks_prepare_colab_before_importing_sdks() -> None:
    for week in range(1, 12):
        sources = notebook_sources(week)
        setup_index = next(i for i, source in enumerate(sources) if "course_packages" in source)
        import_index = next(i for i, source in enumerate(sources) if "from openrouter import OpenRouter" in source)
        setup = sources[setup_index]

        assert setup_index < import_index
        assert "setup_sys.executable" in setup
        assert "import importlib as setup_importlib" in setup
        assert "import importlib.util as setup_importlib_util" in setup
        assert "setup_importlib_util.find_spec" in setup
        assert "setup_importlib.invalidate_caches()" in setup
        assert "setup_importlib.find_spec" not in setup
        assert "setup_importlib.util.find_spec" not in setup
        assert '"-m",\n                "pip",\n                "install"' in setup
        assert '"openrouter>=0.6,<1"' in setup
        assert '"ollama>=0.6,<1"' in setup
        assert "https://github.com/cjbarrie/GenAI_Soc2026.git" in setup
        assert "uv sync" in setup
        assert "uv run jupyter lab" in setup
        if week >= 3:
            assert "setup_sys.path.insert(0, course_root_text)" in setup


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


def test_weeks_3_to_11_select_openrouter_in_colab() -> None:
    for week in (3, 4, 5, 6, 7, 9, 10, 11):
        source = "\n".join(notebook_sources(week))
        assert 'ROUTE = "openrouter" if IN_COLAB else "ollama"' in source


def test_dual_route_weeks_degrade_explicitly_in_colab() -> None:
    week8 = "\n".join(notebook_sources(8))
    assert 'if IN_COLAB:\n        local_raw = None' in week8
    assert "local_results = []" in week8
    assert "local_mae = None if IN_COLAB else" in week8

def test_student_ollama_calls_return_visible_content() -> None:
    """Gemma 4 should not spend a short output allowance only on reasoning text."""
    for week in range(1, 12):
        notebook = "\n".join(notebook_sources(week))
        task = task_source(week)
        chapter = (ROOT / "coursebook" / "python" / f"session{week:02d}.qmd").read_text()
        for source in (notebook, task, chapter):
            unsafe_calls = re.findall(r"ollama\.chat\((?!think=False,|\.\.\.)", source)
            assert unsafe_calls == []


def test_cancelled_week_has_only_an_optional_offline_notebook() -> None:
    source = task_source(12)
    notebook = "\n".join(notebook_sources(12))
    assert "There is no Week 12 coding submission" in source
    assert "There is no Week 12 coding submission" in notebook
    assert "client.chat.send" not in source
    assert "ollama.chat" not in source
    assert "write_text" in source and "read_text" in source
