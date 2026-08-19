# Course maintenance and release checklist

Run these checks from the repository root before the semester, after changing generated content, and shortly before each class whose notebook uses a live model.

## 1. Rebuild and execute

```bash
uv sync --frozen
python3 scripts/build_phase6.py
uv run jupyter nbconvert --to notebook --execute --inplace \
  workbook/00_python_foundations/python_foundations.ipynb \
  workbook/session*/*.ipynb \
  --ExecutePreprocessor.timeout=120
for qmd in slides/session*/session*.qmd; do quarto render "$qmd" || exit 1; done
```

The generator owns Sessions 1 and 3–14. Session 2 is the hand-built pilot and is intentionally preserved. Required exercises use cached or synthetic data, so execution does not require an API key.

## 2. Run offline release checks

```bash
uv run pytest -q
uv run python scripts/check_course.py
uv run python scripts/integration_check.py
uv run python scripts/check_links.py
uv run python scripts/check_citations.py
```

## 3. Check changing external state

```bash
uv run python scripts/check_links.py --external --json _build/phase7/link-report.json
uv run python scripts/check_citations.py --external --json _build/phase7/citation-report.json
```

Before teaching, confirm that the central hosted model in `course_config.py` remains available through OpenRouter and that the local model named in `docs/LOCAL_LLM_GUIDE.md` remains available through Ollama. Check the NYU academic calendar again if meeting dates change. A 401, 403, 405, 406, or 429 may mean the resource exists but blocks automated requests; open such links manually.

## 4. Rendered-page and slide QA

Render notebook HTML into `_build/phase7/notebooks`, then run:

```bash
node design/qa/check_web_pages.mjs _build/phase7/web-report.json \
  _build/phase7/notebooks/*.html slides/session*/session*.html
for html in slides/session*/session*.html; do
  sid=${html:h:t}
  node design/qa/capture_reveal.mjs "$html" "_build/phase7/slides/$sid" || exit 1
done
```

Inspect the captured PNGs after any content or theme change, with particular attention to code wrapping, headings, citations, and projection legibility. Generated HTML and `_build` reports are release artifacts and are intentionally ignored by Git.

## 5. Credential rule

Never put the shared OpenRouter key in a notebook, slide, task, solution, shell history example, or repository file. Distribute it privately as `OPENROUTER_API_KEY`, cap and monitor it, and rotate it if exposed.
