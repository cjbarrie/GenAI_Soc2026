#!/usr/bin/env python3
"""Keep the student local-preflight notebook explicit and beginner-safe."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "workbook" / "00_setup" / "dual_route_preflight.ipynb"


def lines(text: str) -> list[str]:
    return text.strip("\n").splitlines(keepends=True) + ["\n"]


def main() -> None:
    notebook = json.loads(PATH.read_text(encoding="utf-8"))
    cells = notebook["cells"]

    cells[1]["source"] = lines(
        """
## What this notebook is checking

The cells check one layer at a time: Python version → complete course folder → installed SDKs → hidden key → local server → downloaded model. These are separate pieces. A successful SDK import does **not** mean that the Ollama application is running or that its model has been downloaded.

Start this notebook from the complete repository with `uv run jupyter lab`. If a check fails, follow its `NEXT STEP`, rerun that cell and continue. Do not repeatedly reinstall everything.

**Hosted path:** notebook → `openrouter` client → internet → OpenRouter → model provider → response object.

**Local path:** notebook → `ollama` client → `localhost:11434` → downloaded model → response object.
"""
    )

    cells[2]["source"] = lines(
        """
import json
import os
import sys
from getpass import getpass
from pathlib import Path

print("Python:", sys.version.split()[0])
print("Supported version:", (3, 11) <= sys.version_info[:2] < (3, 13))
print("Python executable:", sys.executable)
"""
    )

    cells[3]["source"] = lines(
        """
repo_root = Path.cwd()
while not (repo_root / "config" / "course_models.json").exists() and repo_root != repo_root.parent:
    repo_root = repo_root.parent

if not (repo_root / "config" / "course_models.json").exists():
    raise FileNotFoundError(
        "The complete GenAI_Soc2026 repository could not be found. A notebook "
        "downloaded by itself is not enough for local work. Download or clone the "
        "repository, open a terminal in that folder, and run: uv run jupyter lab"
    )

config = json.loads((repo_root / "config" / "course_models.json").read_text())
HOSTED_MODEL = config["hosted"]["model"]
LOCAL_MODEL = config["local"]["model"]
print("Course root:", repo_root)
print("Hosted model:", HOSTED_MODEL)
print("Local model:", LOCAL_MODEL)
"""
    )

    cells[4]["source"] = lines(
        """
try:
    from openrouter import OpenRouter
    import ollama
except ModuleNotFoundError as error:
    raise ModuleNotFoundError(
        "A course SDK is missing from this Python environment. Close Jupyter, open "
        "a terminal in GenAI_Soc2026, run 'uv sync --frozen', and restart with "
        "'uv run jupyter lab'. In VS Code, select the repository's .venv interpreter."
    ) from error

print("✅ Both Python SDKs imported.")
"""
    )

    cells[6]["source"] = lines(
        """
try:
    local_models = [
        getattr(item, "model", None) or getattr(item, "name", None)
        for item in ollama.list().models
    ]
    OLLAMA_SERVER_READY = True
    LOCAL_MODEL_READY = LOCAL_MODEL in local_models
    print("✅ Ollama server reachable at localhost:11434")
    print("Course model installed:", LOCAL_MODEL_READY)
    if not LOCAL_MODEL_READY:
        print("NEXT STEP: open a terminal and run: ollama pull " + LOCAL_MODEL)
except Exception as error:
    OLLAMA_SERVER_READY = False
    LOCAL_MODEL_READY = False
    print("❌ Ollama server is not reachable.")
    print("NEXT STEP: start the Ollama application, then run: ollama list")
    print("Diagnostic:", str(error).splitlines()[0])
"""
    )

    cells[9]["source"] = lines(
        """
test_message = "Reply with exactly: ROUTE READY"
hosted_messages = [{"role": "user", "content": test_message}]

try:
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        hosted_response = client.chat.send(
            model=HOSTED_MODEL,
            messages=hosted_messages,
            temperature=0,
            max_tokens=12,
        )
    hosted_answer = hosted_response.choices[0].message.content.strip()
    print("✅ OpenRouter reachable:", bool(hosted_answer))
    print("Hosted output:", hosted_answer)
except Exception as error:
    raise RuntimeError(
        "OpenRouter rejected the live request. Re-enter the privately supplied key. "
        "If the error continues, ask the instructor to check that the course key is "
        "active and funded. Original message: " + str(error).splitlines()[0]
    ) from error
"""
    )

    cells[11]["source"] = lines(
        """
if not OLLAMA_SERVER_READY:
    raise RuntimeError(
        "Ollama is not reachable. Start the Ollama application, run 'ollama list', "
        "then rerun the Ollama status cell above."
    )
if not LOCAL_MODEL_READY:
    raise RuntimeError(
        "The course model is not installed. In a terminal run: ollama pull " + LOCAL_MODEL
    )

local_messages = [{"role": "user", "content": test_message}]
try:
    local_response = ollama.chat(
        model=LOCAL_MODEL,
        messages=local_messages,
        options={"temperature": 0},
    )
    local_answer = local_response.message.content.strip()
    print("✅ Ollama reachable:", bool(local_answer))
    print("Local output:", local_answer)
except Exception as error:
    raise RuntimeError(
        "The local call failed after setup. Run 'ollama list' and confirm that "
        + LOCAL_MODEL + " appears. Original message: " + str(error).splitlines()[0]
    ) from error
"""
    )

    PATH.write_text(
        json.dumps(notebook, indent=1, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"Repaired {PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
