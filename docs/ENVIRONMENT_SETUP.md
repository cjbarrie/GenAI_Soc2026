# Supported course environment

The canonical materials are ordinary Jupyter notebooks. Use local JupyterLab or VS Code when possible; Colab is a fallback. Required work never depends on a live model.

## Path A — local Jupyter with `uv` (recommended)

1. Install `uv` using the instructions for your operating system: <https://docs.astral.sh/uv/getting-started/installation/>.
2. In a terminal, change into this repository.
3. Run `uv sync`.
4. Run `uv run jupyter lab`.
5. In JupyterLab, open `workbook/00_python_foundations/python_foundations.ipynb`.

`uv sync` reads `pyproject.toml` and builds an isolated `.venv`. The environment is disposable: do not submit it and do not copy it between computers.

## Path B — `pip`

Use Python 3.11, create a virtual environment, activate it, and run `python -m pip install -r requirements.txt`. Then start Jupyter with `python -m jupyter lab`.

## Path C — Colab fallback

Upload the notebook and the small data files it names. Run the first “locate files” cell only after setting `REPO_ROOT` to the Colab folder. Cached-output exercises remain identical; see `docs/COLAB_FALLBACK.md`.

## OpenRouter key

The instructor distributes the shared, capped key privately. Set it as `OPENROUTER_API_KEY`; never paste it into a notebook cell. Confirm only that the variable exists:

```python
import os
print(os.getenv("OPENROUTER_API_KEY") is not None)
```

This prints `True` or `False`, not the secret. The course uses the official `openrouter` Python SDK: <https://openrouter.ai/docs/client-sdks/python/overview>.

## First diagnostic

Run `uv run python scripts/check_course.py`. A failure message should tell you what object or file is missing. Copy the error text when asking for help; never include a key.

