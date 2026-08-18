# Generative AI in Sociology — Fall 2026

NYU graduate seminar, Wednesdays 9:30 a.m.–12:15 p.m. The course moves from observing and measuring social material, through interventions and simulations, to delegated research and model audits.

## Start here

1. Read `docs/ENVIRONMENT_SETUP.md`.
2. Complete or diagnose yourself with `workbook/00_python_foundations/python_foundations.ipynb`.
3. Open the numbered session notebook.
4. For every code cell, name the **input**, **Python type**, **operation**, **output**, and **research meaning** before changing it.

Required exercises always work from cached or synthetic data. A live OpenRouter call or local model is an optional, replaceable transformation.

## Build and check

```bash
uv sync
uv run python -m pytest -q
uv run python scripts/check_course.py
```

Render a deck with `quarto render slides/session02/session02.qmd`. API keys belong in the environment, never in notebooks or repository files.

