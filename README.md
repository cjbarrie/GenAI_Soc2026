# Generative AI in Sociology — Fall 2026

NYU graduate seminar, Wednesdays 9:30 a.m.–12:15 p.m. The course moves from observing and measuring social material, through interventions and simulations, to delegated research and model audits.

## Start here

1. Read `docs/ENVIRONMENT_SETUP.md`.
2. Complete or diagnose yourself with `workbook/00_python_foundations/python_foundations.ipynb`.
3. Open the numbered session notebook.
4. For every code cell, name the **input**, **Python type**, **operation**, **output**, and **research meaning** before changing it.

Weeks 1–2 make live calls through both OpenRouter and Ollama using only synthetic or public teaching material. Students choose either route in Weeks 3–7 and compare both again in Week 8. Recorded returns remain available as an access contingency.

## Build and check

```bash
uv sync
uv run python -m pytest -q
uv run python scripts/check_course.py
uv run python scripts/integration_check.py
uv run python scripts/check_links.py
uv run python scripts/check_citations.py
```

Render a deck with `quarto render slides/session02/session02.qmd`. API keys belong in the environment, never in notebooks or repository files.

Before a release, also run the live variants of the link and citation checks. The exact maintenance and rendering sequence is in `docs/MAINTENANCE.md`; the completed Phase 7 record is in `docs/PHASE7_VERIFICATION.md`.
