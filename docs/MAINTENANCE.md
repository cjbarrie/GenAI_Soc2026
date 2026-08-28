# Course maintenance and release checklist

Run these checks from the repository root before the semester, after changing generated content, and shortly before each class whose notebook uses a live model.

## 1. Validate student-facing sources

```bash
uv sync --frozen
uv run python scripts/check_coursebook.py
```

`scripts/build_phase6.py` is an archived scaffolding utility. It no longer owns
reviewed slides, notebooks, reading guides or prose, and it must not appear in a
routine release command. It requires both an explicit session number and an
overwrite acknowledgment, for example:

```bash
python3 scripts/build_phase6.py --session 14 --confirm-overwrite-scaffold
```

Use that command only when deliberately replacing the named session with a new
scaffold that will receive a full literature-led and visual review.

## 2. Check notebooks without making live calls

```bash
uv run python scripts/check_course.py
uv run python scripts/integration_check.py
uv run pytest tests/test_dual_route_materials.py -q
for qmd in slides/session*/session*.qmd; do quarto render "$qmd" || exit 1; done
```

The structural checks parse every code cell and validate the recorded fixtures without executing student notebooks, because those notebooks deliberately contain live calls. Use `scripts/live_model_smoke.py` separately when credentials and the local model are available. This is different from the student exercise: Weeks 1–2 normally use both live routes, Weeks 3–7 use either route, and Week 8 compares both. Recorded returns are only an access contingency.

## 3. Build the course book

The book pre-render step renders any stale Reveal decks and packages only public
resources: self-contained slide HTML, student notebooks and weekly task files.

```bash
quarto render coursebook --to pdf
cp coursebook/_book/Generative-AI-in-Sociology.pdf /tmp/Generative-AI-in-Sociology.pdf
quarto render coursebook --to html
cp /tmp/Generative-AI-in-Sociology.pdf coursebook/_book/Generative-AI-in-Sociology.pdf
uv run python scripts/check_coursebook.py --rendered
```

The canonical site is written to `coursebook/_book/`; the PDF is
`coursebook/_book/Generative-AI-in-Sociology.pdf`. Both directories are release
artifacts and are ignored by Git. GitHub Actions rebuilds them from source and
publishes the HTML tree to GitHub Pages.

## 4. Run the remaining offline release checks

```bash
uv run pytest -q
uv run python scripts/check_links.py
uv run python scripts/check_citations.py
```

## 5. Check changing external state

```bash
uv run python scripts/check_links.py --external --json _build/phase7/link-report.json
uv run python scripts/check_citations.py --external --json _build/phase7/citation-report.json
```

Before teaching, confirm that the central hosted and local models in `config/course_models.json` remain available. Run `uv run python scripts/preflight_models.py --live` or the two-route instructor smoke test, `uv run python scripts/live_model_smoke.py`. After setting the shared key's budget, rate limits and model/provider allowlist in OpenRouter, run `uv run python scripts/class_cost_smoke.py --students 10 --calls-per-student 2`; it refuses more than 20 calls and reports the resolved run count and token usage. Confirm the corresponding cost and provider record in OpenRouter. Check the NYU academic calendar again if meeting dates change. A 401, 403, 405, 406, or 429 may mean the resource exists but blocks automated requests; open such links manually.

## 6. Rendered-page and slide QA

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

For the course book, capture every page at desktop and mobile widths after a
theme or structural change. Inspect the full PDF for page breaks, wrapped code,
citations and any HTML-only content that escaped its format condition.

## 7. Credential rule

Never put the shared OpenRouter key in a notebook, slide, task, solution, shell history example, or repository file. Distribute it privately as `OPENROUTER_API_KEY`, cap and monitor it, and rotate it if exposed.

## 8. Weekly exercise and submission rule

- The middle of each class is reserved for discussion of the assigned readings; the final part is a guided walkthrough of the week's code.
- Teach Python through an LLM routine. Name the input, operation and output of each block before introducing a new Python feature.
- Weeks 1–2 use both live routes. Weeks 3–7 use either route. Week 8 introduces a short dual-route loop. Week 9 introduces the first small student-edited function and explains every parameter.
- Every task changes one named input or parameter and runs the same routine again. Compactness and code elegance are not assessed.
- The submission is a narrated screen recording showing both runs and explaining every operation's input and output, one methodological limit and the reading connection.
- Recordings go to the dedicated NYU Box folder. Keep the public text `Box submission link: to be provided by the instructor.` until the instructor supplies the URL.
- Never ask students to display the shared key. They should enter it before recording or use a local model.
