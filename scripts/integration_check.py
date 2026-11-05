"""Check the implemented Python/LLM learning progression across artifacts."""

from __future__ import annotations

import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str, problems: list[str]) -> None:
    if not condition:
        problems.append(message)


def main() -> None:
    problems: list[str] = []
    config = json.loads((ROOT / "config/course_models.json").read_text())
    require(config["hosted"]["model"] == "openai/gpt-5.2", "unexpected hosted model", problems)
    require(config["local"]["model"] == "gemma4:e2b-it-qat", "unexpected local model", problems)
    fixtures = json.loads((ROOT / "data/dual_route_recorded_outputs.json").read_text())

    for week in range(1, 12):
        session = f"session{week:02d}"
        task_path = ROOT / "assessments/weekly_coding" / f"{session}_task.py"
        notebooks = sorted((ROOT / "workbook" / session).glob("*.ipynb"))
        require(task_path.exists(), f"missing task for {session}", problems)
        require(len(notebooks) == 1, f"expected one notebook for {session}", problems)
        require(session in fixtures, f"missing recorded contingency for {session}", problems)
        if not task_path.exists():
            continue
        source = task_path.read_text()
        functions = [node for node in ast.walk(ast.parse(source)) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
        if week < 9:
            require(not functions, f"{session}: function introduced before Week 9", problems)
        if week == 9:
            require(
                "def record_human_judgment(" in source,
                "Week 9 must introduce record_human_judgment",
                problems,
            )
        require("raw" in source.lower(), f"{session}: raw return is not visibly preserved", problems)
        if week == 3:
            require(
                "feedback_1 = input" in source and "feedback_2 = input" in source,
                f"{session}: missing the two researcher replies",
                problems,
            )
        else:
            require("ONE CHANGE" in source, f"{session}: missing one named change", problems)
        if week in (1, 2, 8):
            require("client.chat.send" in source and "ollama.chat" in source, f"{session}: both routes required", problems)
        if 3 <= week <= 7:
            require('ROUTE = "ollama"' in source, f"{session}: missing visible ROUTE selector", problems)
            require("client.chat.send" in source and "ollama.chat" in source, f"{session}: route branches not shown", problems)

        if len(notebooks) == 1:
            notebook = json.loads(notebooks[0].read_text())
            require("Open In Colab" in json.dumps(notebook), f"{session}: missing Colab badge", problems)
            for cell in notebook["cells"]:
                if cell["cell_type"] == "code":
                    cell_source = cell["source"] if isinstance(cell["source"], str) else "".join(cell["source"])
                    ast.parse(cell_source)

    optional_task = ROOT / "assessments/weekly_coding/session12_task.py"
    optional_notebooks = sorted((ROOT / "workbook/session12").glob("*.ipynb"))
    require(optional_task.exists(), "missing optional project-record task", problems)
    require(len(optional_notebooks) == 1, "expected one optional project-record notebook", problems)
    if optional_task.exists():
        optional_source = optional_task.read_text()
        require(
            "There is no Week 12 coding submission" in optional_source,
            "Week 12 task must remain explicitly optional",
            problems,
        )
        require("write_text" in optional_source and "read_text" in optional_source,
                "optional project record must show a JSON file round trip", problems)
    if len(optional_notebooks) == 1:
        optional_notebook = json.loads(optional_notebooks[0].read_text())
        require(
            "There is no Week 12 coding submission" in json.dumps(optional_notebook),
            "optional notebook must not imply an assignment",
            problems,
        )
        for cell in optional_notebook["cells"]:
            if cell["cell_type"] == "code":
                cell_source = cell["source"] if isinstance(cell["source"], str) else "".join(cell["source"])
                ast.parse(cell_source)

    combined_policy = (ROOT / "syllabus/SYLLABUS.md").read_text() + (ROOT / "workbook/PROGRESSION.md").read_text()
    for phrase in ("both OpenRouter and Ollama", "Week 8", "Week 9"):
        require(phrase in combined_policy, f"course policy missing {phrase!r}", problems)
    require("Project presentations" in combined_policy and "no new reading" in combined_policy, "Week 14 policy missing", problems)

    if problems:
        print("Dual-route integration checks failed:")
        print("\n".join(f"- {problem}" for problem in problems))
        raise SystemExit(1)
    print("Dual-route progression passed: both routes in Weeks 1–2 and 8, route choice in 3–7, function and control flow in 9, distinct syntax in 10–11, and no assessed task after 18 November.")


if __name__ == "__main__":
    main()
