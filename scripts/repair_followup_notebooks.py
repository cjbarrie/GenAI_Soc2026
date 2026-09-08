#!/usr/bin/env python3
"""Apply the verified Colab/local setup to the Week 3–13 notebooks."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def lines(text: str) -> list[str]:
    return text.strip("\n").splitlines(keepends=True) + ["\n"]


SETUP_MARKDOWN = """
## Prepare the notebook environment

Run the next cell before any other code. In Colab it installs the Python SDKs used by this notebook, downloads the public course repository and selects OpenRouter because Colab cannot reach the Ollama server on your computer. On a local machine it installs nothing silently: it checks that the notebook is using the course environment and gives the exact repair command if it is not.

The setup also adds the repository root to Python's import path. This is necessary for Week 4's supplied image utility and prevents a second kind of `ModuleNotFoundError` after the repository has been cloned.
"""


SETUP_CODE = r'''
# Run this cell first. It prepares Colab or checks the local Python environment.
import importlib as setup_importlib
import os as setup_os
import subprocess as setup_subprocess
import sys as setup_sys
from pathlib import Path as SetupPath

try:
    import google.colab as setup_colab  # type: ignore[import-not-found]
    IN_COLAB = True
except ImportError:
    IN_COLAB = False

course_packages = {
    "openrouter": "openrouter>=0.6,<1",
    "ollama": "ollama>=0.6,<1",
}
if SESSION == "session13":
    course_packages["pandas"] = "pandas>=2.2,<3"

missing_packages = [
    package_name
    for package_name in course_packages
    if setup_importlib.util.find_spec(package_name) is None
]

if IN_COLAB:
    if missing_packages:
        packages_to_install = [course_packages[name] for name in missing_packages]
        setup_subprocess.run(
            [
                setup_sys.executable,
                "-m",
                "pip",
                "install",
                "--quiet",
                "--disable-pip-version-check",
                *packages_to_install,
            ],
            check=True,
        )
        setup_importlib.invalidate_caches()

    COURSE_ROOT = SetupPath(
        setup_os.getenv("COURSE_COLAB_ROOT", "/content/GenAI_Soc2026")
    )
    if not COURSE_ROOT.exists():
        setup_subprocess.run(
            [
                "git",
                "clone",
                "--depth",
                "1",
                "https://github.com/cjbarrie/GenAI_Soc2026.git",
                str(COURSE_ROOT),
            ],
            check=True,
        )
    setup_os.chdir(COURSE_ROOT / "workbook" / SESSION)
else:
    COURSE_ROOT = SetupPath.cwd()
    while not (COURSE_ROOT / "config" / "course_models.json").exists() and COURSE_ROOT != COURSE_ROOT.parent:
        COURSE_ROOT = COURSE_ROOT.parent
    if missing_packages:
        missing_text = ", ".join(missing_packages)
        raise ModuleNotFoundError(
            f"This notebook is using a Python environment without: {missing_text}.\n\n"
            "Close Jupyter. Open a terminal in the GenAI_Soc2026 repository and run:\n"
            "    uv sync\n"
            "    uv run jupyter lab\n\n"
            "In VS Code, select the Python interpreter inside the repository's .venv folder."
        )
    if not (COURSE_ROOT / "config" / "course_models.json").exists():
        raise FileNotFoundError(
            "The course repository root could not be found. Start Jupyter from the "
            "GenAI_Soc2026 folder with: uv run jupyter lab"
        )

course_root_text = str(COURSE_ROOT)
if course_root_text not in setup_sys.path:
    setup_sys.path.insert(0, course_root_text)

still_missing = [
    package_name
    for package_name in course_packages
    if setup_importlib.util.find_spec(package_name) is None
]
if still_missing:
    raise ModuleNotFoundError(
        "Setup did not make these packages available: " + ", ".join(still_missing)
    )

print("Environment:", "Google Colab" if IN_COLAB else "local course environment")
print("Course root:", COURSE_ROOT)
print("Working folder:", SetupPath.cwd())
print("Python SDKs: ready")
if IN_COLAB:
    print("Route for this runtime: OpenRouter")
    print("Ollama work: complete later in local JupyterLab or on the in-class machine")
'''


def notebook_path(week: int) -> Path:
    files = list((ROOT / "workbook" / f"session{week:02d}").glob("*.ipynb"))
    if len(files) != 1:
        raise RuntimeError(f"Expected one notebook for Week {week}; found {len(files)}")
    return files[0]


def replace_route_selector(source: str) -> str:
    return re.sub(
        r'^ROUTE = "ollama"[^\n]*$',
        'ROUTE = "openrouter" if IN_COLAB else "ollama"  # Ollama is the local default',
        source,
        flags=re.MULTILINE,
    )


def repair_standard_notebook(week: int, notebook: dict) -> None:
    cells = notebook["cells"]
    cells[1]["source"] = lines(
        f"""
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cjbarrie/GenAI_Soc2026/blob/main/workbook/session{week:02d}/{notebook_path(week).name})

Run the setup cell immediately below before doing anything else. Colab installs the required Python packages and uses OpenRouter. Ollama is used from local JupyterLab or VS Code because Colab cannot reach the Ollama server on your computer.
"""
    )

    cells[2]["cell_type"] = "markdown"
    cells[2].pop("execution_count", None)
    cells[2].pop("outputs", None)
    cells[2]["source"] = lines(SETUP_MARKDOWN)

    cells[3]["cell_type"] = "code"
    cells[3]["execution_count"] = None
    cells[3]["outputs"] = []
    cells[3]["source"] = lines(f'SESSION = "session{week:02d}"\n' + SETUP_CODE)

    for cell in cells:
        if cell["cell_type"] == "code":
            source = "".join(cell["source"])
            revised = replace_route_selector(source)
            if revised != source:
                cell["source"] = lines(revised)

    route_note = (
        "\n\nIn Colab, `ROUTE` is set to `\"openrouter\"` automatically. "
        "On a local machine it defaults to `\"ollama\"`; you may change it to OpenRouter."
    )
    for cell in cells:
        if cell["cell_type"] == "markdown" and "Choose" in "".join(cell["source"]) and "route" in "".join(cell["source"]).lower():
            cell["source"] = lines("".join(cell["source"]).rstrip() + route_note)
            break


def repair_week8(notebook: dict) -> None:
    cells = notebook["cells"]
    cells[10]["source"] = lines(
        '''
for profile in profiles:
    # Build the model input explicitly. The held-out answer is not included.
    public_profile = {
        "age_group": profile["age_group"],
        "education": profile["education"],
        "region": profile["region"],
        "party": profile["party"],
    }
    prompt = "Predict the survey answer. Profile: " + json.dumps(public_profile) + " Item: " + question
    messages = [{"role":"user","content":prompt}]

    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        hosted_response = client.chat.send(
            model=HOSTED_MODEL, messages=messages, temperature=0,
            response_format={"type":"json_schema","json_schema":{
                "name":"opinion_prediction","strict":True,"schema":schema,
            }},
        )
    hosted_raw = hosted_response.choices[0].message.content
    hosted_prediction = json.loads(hosted_raw)["predicted_category"]
    hosted_results.append({"id":profile["id"],"prediction":hosted_prediction,"human":profile["human_answer"]})

    if IN_COLAB:
        local_raw = None
        print(profile["id"], "hosted raw:", hosted_raw, "local raw: not run in Colab")
    else:
        local_response = ollama.chat(
            model=LOCAL_MODEL, messages=messages, format=schema,
            options={"temperature":0},
        )
        local_raw = local_response.message.content
        local_prediction = json.loads(local_raw)["predicted_category"]
        local_results.append({"id":profile["id"],"prediction":local_prediction,"human":profile["human_answer"]})
        print(profile["id"], "hosted raw:", hosted_raw, "local raw:", local_raw)
'''
    )
    cells[12]["source"] = lines(
        '''
hosted_matches = 0
local_matches = None if IN_COLAB else 0
for record in hosted_results:
    if record["prediction"] == record["human"]:
        hosted_matches = hosted_matches + 1
if not IN_COLAB:
    for record in local_results:
        if record["prediction"] == record["human"]:
            local_matches = local_matches + 1
print("Hosted exact matches:", hosted_matches, "of", len(profiles))
print("Local exact matches:", local_matches, "of", len(profiles))
'''
    )
    cells[14]["source"] = lines(
        '''
human_total = 0
hosted_total = 0
local_total = 0
for record in hosted_results:
    human_total = human_total + record["human"]
    hosted_total = hosted_total + record["prediction"]
if not IN_COLAB:
    for record in local_results:
        local_total = local_total + record["prediction"]
human_mean = human_total / len(profiles)
hosted_mean = hosted_total / len(profiles)
local_mean = None if IN_COLAB else local_total / len(profiles)
print("Human mean:", human_mean)
print("Hosted mean:", hosted_mean)
print("Local mean:", local_mean)

# ONE CHANGE: change p02 education to "high school" and rerun the full loop.
'''
    )
    cells[15]["source"] = lines(
        """
## Methodological check

A close mean is aggregate evidence only. It can coexist with incorrect person-level pairings and cannot establish subgroup fidelity from five teaching cases. In Colab, the local counts and mean are `None`, meaning “not run.” Complete the Ollama comparison later in local JupyterLab or on the in-class machine.

## Recording

Trace p02 through one complete iteration for each route, make the named education change, and explain why the exact-match counts and means answer different questions.
"""
    )


def repair_week13(notebook: dict) -> None:
    cells = notebook["cells"]
    cells[6]["source"] = lines(
        '''
routes = ["openrouter"] if IN_COLAB else ["openrouter", "ollama"]
frames = {
    "individual":"Evaluate the action in terms of individual choice.",
    "collective":"Evaluate the action in terms of collective obligation.",
}
scenario = "A worker declines an unpaid request to stay late."
schema = {"type":"object","properties":{"approval":{"type":"integer","minimum":0,"maximum":100},"explanation":{"type":"string"}},"required":["approval","explanation"],"additionalProperties":False}
audit_records = []
print("Routes available in this runtime:", routes)
if IN_COLAB:
    print("The Ollama rows are completed later in local JupyterLab or on the in-class machine.")
'''
    )
    cells[13]["source"] = lines(
        """
## Methodological check

The grid identifies patterned output differences under declared conditions. Route, model size, provider, prompt and training differences remain entangled; do not label the pattern a cultural or ideological cause. Colab produces the OpenRouter rows only; the local Ollama rows must be added outside Colab.

## Recording

Trace one cell through both loops, make the role-word change, present one bounded observed difference and name at least two unresolved explanations.
"""
    )


def repair() -> None:
    for week in range(3, 14):
        path = notebook_path(week)
        notebook = json.loads(path.read_text(encoding="utf-8"))
        repair_standard_notebook(week, notebook)
        if week == 8:
            repair_week8(notebook)
        if week == 13:
            repair_week13(notebook)
        path.write_text(json.dumps(notebook, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Repaired Week {week}: {path.name}")


if __name__ == "__main__":
    repair()
