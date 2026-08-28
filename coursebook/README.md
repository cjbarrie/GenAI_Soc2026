# Student course book

This directory is a separate Quarto Book subproject. It does not own or rewrite
the source slide decks, notebooks or weekly tasks.

From the repository root:

```bash
python3 scripts/check_coursebook.py
quarto render coursebook --to pdf
cp coursebook/_book/Generative-AI-in-Sociology.pdf /tmp/Generative-AI-in-Sociology.pdf
quarto render coursebook --to html
cp /tmp/Generative-AI-in-Sociology.pdf coursebook/_book/Generative-AI-in-Sociology.pdf
python3 scripts/check_coursebook.py --rendered
```

Each `quarto render` command succeeds independently. Quarto replaces the shared
output directory when switching formats, so a release build preserves the PDF
temporarily while constructing the canonical HTML tree, then adds it to the site.

The pre-render step calls `scripts/build_coursebook.py --prepare`. It packages
only developed Weeks 1–7: stale Reveal decks, student notebooks, task files and
runnable offline bundles. Weeks 8–14 remain explicit planning pages until each
receives the literature-led build and review. Solutions, instructor notes, API
administration and source PDFs are never copied.

The weekly reading source of truth is `readings.json`. Every record has a BibTeX
key, essential/additional status, assigned section, student-facing purpose and
stable public URL. Weekly chapters are deliberately human-authored; no build
script generates their argument or prose.
