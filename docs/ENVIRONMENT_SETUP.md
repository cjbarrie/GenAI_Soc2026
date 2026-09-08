# Set up Python, OpenRouter and Ollama

Local JupyterLab or VS Code is the normal course environment. Google Colab is an OpenRouter fallback; it cannot run the model on your own computer. Complete this setup before Week 1. Ask for help with an error rather than repeatedly reinstalling software.

## What the pieces are

- **Python** runs the course code.
- **JupyterLab or VS Code** gives you a place to run that code in short cells.
- **OpenRouter** sends a request over the internet to a hosted model using the course key.
- **Ollama** runs a downloaded model through a server on your own computer.
- **The SDK** is the Python package that lets your code talk to either service.

OpenRouter and Ollama are not models. OpenRouter is a remote routing service; Ollama is a local model server. In both cases, an SDK turns Python objects into an API request and turns the reply into a Python response object.

The OpenRouter route is:

```text
Python → openrouter SDK → internet → OpenRouter → model provider → response
```

The Ollama route is:

```text
Python → ollama SDK → http://localhost:11434 → downloaded model → response
```

`localhost` means the same computer. The Ollama model must already have been downloaded; the OpenRouter model remains on external provider hardware. The full beginner explanation is in the course-book chapter [Setting up Python, OpenRouter and Ollama](../coursebook/computing.qmd).

## 1. Install `uv` and Python

### macOS

1. Open Terminal.
2. Follow the current [official `uv` installation instructions](https://docs.astral.sh/uv/getting-started/installation/).
3. Close and reopen Terminal.
4. Run `uv --version`.

### Windows

1. Open PowerShell, not Command Prompt.
2. Follow the Windows section of the [official `uv` installation instructions](https://docs.astral.sh/uv/getting-started/installation/).
3. Close and reopen PowerShell.
4. Run `uv --version`.

### Linux

1. Open a terminal.
2. Follow the Linux section of the [official `uv` installation instructions](https://docs.astral.sh/uv/getting-started/installation/).
3. Close and reopen the terminal.
4. Run `uv --version`.

Do not install a separate system Python unless the diagnostic says it is necessary. `uv` will install the course's supported Python version.

## 2. Download the repository and install its Python packages

Download or clone the course repository, open a terminal in its top-level folder, and run:

```bash
uv sync
uv run jupyter lab
```

`uv sync` creates an isolated `.venv` and installs JupyterLab, OpenRouter, Ollama and the other course packages. Do not upload or submit `.venv`.

## 3. Install Ollama

Download Ollama from the [official Ollama download page](https://ollama.com/download). It supports macOS, Windows and Linux. Start the application once after installation, then open a new terminal and run:

```bash
ollama --version
ollama pull gemma4:e2b-it-qat
ollama list
curl http://localhost:11434/api/version
```

The first command checks the installed application. `ollama pull` downloads the model artifact. `ollama list` checks that the tag is installed. The final command makes a direct request to the local API; a JSON version reply shows that the server is reachable. The pull is several gigabytes and may take time. The exact course tag is `gemma4:e2b-it-qat`; do not silently substitute `gemma4`, which currently downloads a larger artifact.

Make the first terminal call:

```bash
ollama run gemma4:e2b-it-qat "Reply with the words LOCAL MODEL READY."
```

If the model cannot run on your computer, bring the diagnostic output to class. You will complete the initial local calls on a paired or instructor machine; hardware ownership does not affect the mark.

## 4. Receive the OpenRouter key

The instructor distributes one capped course key privately. Never put it in a notebook, task file, screen recording, chat message or repository commit. The setup notebook uses hidden input so the key exists only in the current Python process.

In a local terminal, an alternative is to set `OPENROUTER_API_KEY` in the current shell using your operating system's normal environment-variable method. Confirm only whether Python can see it:

```python
import os
print(os.getenv("OPENROUTER_API_KEY") is not None)
```

The output is `True` or `False`; it never displays the key.

## 5. Run the course preflight

From the repository root, run:

```bash
uv run python scripts/preflight_models.py
```

This checks Python, both SDKs, the key, the Ollama server and the installed local model without making paid calls. Then run the live test:

```bash
uv run python scripts/preflight_models.py --live
```

The live test sends one very short synthetic request through each route. It prints only status and the model replies. The key is never printed.

You can instead open `workbook/00_setup/dual_route_preflight.ipynb` and run its cells in order.

## 6. Start work each week

1. Start Ollama if you plan to use the local route.
2. Open a terminal in the repository.
3. Run `uv sync` after the instructor announces an environment update.
4. Run `uv run jupyter lab`.
5. Open the weekly notebook.
6. Set `ROUTE` to `"ollama"` or `"openrouter"` when the notebook asks.

## Troubleshooting

| Message | What it usually means | First check |
|---|---|---|
| `command not found: uv` | the terminal has not picked up the installation | restart the terminal and run `uv --version` |
| `No module named ...` in local Jupyter | the notebook is using the wrong Python environment | close Jupyter, run `uv sync`, then start it with `uv run jupyter lab` |
| `No module named ...` in Colab | the setup cell at the top was not run, or its installation failed | restart the runtime and run the setup cell before any imports |
| Ollama connection refused | the local application/server is not running | start Ollama and run `ollama list` |
| model not found | the exact tag is not installed | run `ollama pull gemma4:e2b-it-qat` |
| out of memory or very slow | the model does not fit comfortably | stop other applications and bring the diagnostic to class |
| OpenRouter unauthorized | the key is absent, mistyped or expired | re-enter the privately supplied key without displaying it |
| rate limited | the shared class quota is temporarily busy | wait, use Ollama, or use the clearly labelled cached contingency |

Only synthetic, public or instructor-authored teaching data may be sent through the shared course key.

If you use VS Code instead of `uv run jupyter lab`, select the repository interpreter explicitly: `.venv/bin/python` on macOS/Linux or `.venv\\Scripts\\python.exe` on Windows.
