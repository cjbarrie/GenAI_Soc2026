# Slide Design System — Evidence & Society

**Version:** 1.0  
**Approved:** 2026-08-18  
**Applies to:** All Fall 2026 lecture decks, the Phase 5 pilot, exported PDFs, and slide-derived figures.  
**Primary medium:** Quarto/Reveal.js viewed in a classroom and online.

## Communication job

> By the end of each session, graduate sociology students should be able to state what inference an LLM-assisted design supports, identify the evidence that would validate it, and explain the focal computation in plain language.

The visual system must make the relationship among **claim, evidence, computation, and validation** easier to follow. It should feel like contemporary sociology and careful empirical research—not a technology-company pitch, software dashboard, or generic “AI” presentation.

## Format and canvas

- **Aspect ratio:** 16:9.
- **Reveal.js canvas:** 1280 × 720 CSS pixels.
- **PDF equivalent:** 13.333 × 7.5 inches.
- **Primary background:** Paper (`#F5F1E8`).
- **Core safe area:** 72 px left/right, 52 px top, 42 px bottom.
- **Title area:** begins at 52 px and normally ends by 132 px.
- **Footer/source area:** bottom 32 px; it must never compete with body content.
- **Core content width:** 1136 px.
- **Grid:** 12 columns with 24 px gutters; content may span 4/8, 5/7, 6/6, 7/5, 8/4, or all 12 columns.
- **Baseline:** 8 px. Align text, charts, and figures to this rhythm.

Slides are projection-first. The web version may expose notes or links, but visible slides are not lecture transcripts.

## Typography

Fonts will be vendored locally as WOFF2 assets so slides render offline and consistently.

| Function | Typeface | Weight | Size / line height |
|---|---|---:|---:|
| Deck title | Source Serif 4 | 600 | 68 px / 1.02 |
| Major question | Source Serif 4 | 600 | 54 px / 1.08 |
| Section divider | Source Serif 4 | 600 | 52 px / 1.08 |
| Slide title | Source Sans 3 | 650 | 42 px / 1.08 |
| Lead statement | Source Sans 3 | 500 | 34 px / 1.22 |
| Body | Source Sans 3 | 400 | 29 px / 1.28 |
| Emphasis / labels | Source Sans 3 | 650 | 24 px / 1.18 |
| Code | IBM Plex Mono | 400/600 | 23 px / 1.35 |
| Figure caption | Source Sans 3 | 400 | 18 px / 1.22 |
| Visible source | Source Sans 3 | 400 | 16 px / 1.20 |
| Page marker | Source Sans 3 | 600 | 15 px / 1 |

Fallback stack:

- Serif: `"Source Serif 4", Georgia, serif`
- Sans: `"Source Sans 3", Arial, sans-serif`
- Mono: `"IBM Plex Mono", Menlo, monospace`

### Type rules

- Use Source Serif only for title slides, section openings, major questions, and short quotations.
- Use sentence case. Avoid all-caps except for very short data or schema labels.
- Prefer one-line takeaway titles. A deliberately written two-line question is permitted; accidental wrapping is not.
- Maximum body line length: approximately 55–65 characters.
- Never shrink body or code to fit. Shorten, split, or change the layout.
- Bold conveys hierarchy; italics are reserved for terms, book/journal titles, and the course’s recurring inference question.
- Underlining is reserved for hyperlinks.

## Spacing scale

Use only these values unless a figure crop requires an optical adjustment:

`8, 16, 24, 32, 48, 64, 96 px`

- 8: label-to-object or tightly related metadata.
- 16: caption separation, short list rhythm.
- 24: related text blocks or grid gutter.
- 32: title-to-lead statement.
- 48: separate conceptual groups.
- 64: section-level separation.
- 96: deliberate dramatic separation on sparse slides.

Avoid floating elements placed by eye without reference to the grid.

## Color system

### Core palette

| Token | Hex | Use |
|---|---|---|
| Paper | `#F5F1E8` | Default background |
| Clear paper | `#FFFCF5` | Figure field, quotation field, code-adjacent light area |
| Ink | `#182026` | Primary text, axes, human observations |
| Slate | `#5F6B72` | Secondary labels and rules; never for small text on weak contrast |
| Cobalt | `#2457A6` | LLM/model series, focal method, links |
| Vermilion | `#D5573B` | Failure, contradiction, warning, focal exception |
| Moss | `#5F7355` | Validation evidence, retained/accepted elements |
| Pale cobalt | `#DCE6F5` | Light emphasis field |
| Pale vermilion | `#F4DDD5` | Light warning field |
| Pale moss | `#DFE7DB` | Light validation field |

### Color rules

- Ink on Paper is the default. Most slides should use no more than one accent color.
- Cobalt may carry body-sized linked or highlighted text. Vermilion and Moss are marks, fills, or large/bold labels—not long passages of small text.
- **Human evidence = Ink; LLM/model output = Cobalt** across decks unless the substantive chart requires another mapping.
- **Unresolved failure or contradiction = Vermilion. Validation evidence or accepted check = Moss.**
- Never use red/green alone to distinguish categories. Pair color with labels, shapes, line styles, or position.
- Do not use gradients, glows, neon effects, or semitransparent decorative blobs.

## Narrative and deck architecture

Each deck is an argument, not a list of readings. A typical sequence is:

1. sociological question or empirical tension;
2. competing claims from the readings;
3. inferential target and methodological opportunity;
4. mechanism or study anatomy;
5. evidence and its limits;
6. focal input → transformation → output handoff;
7. characteristic failure and validation response;
8. synthesis or open inference question.

This is not a mandatory eight-slide template. It is the logic used to select and order slides. Aim for roughly 24–34 core slides for the lecture/discussion portion of a 165-minute seminar; technical detail belongs in the workbook or appendix.

### Title language

- Prefer claims: “A good population mean can hide representational failure.”
- Avoid containers: “Results,” “Reading 2,” “Why it matters,” or “Introduction.”
- A slide devoted to a paper uses the paper’s empirical or methodological takeaway as the title; the citation identifies the paper.

## Layout families

Adjacent slides should vary silhouette while maintaining the same grid.

### 1. Minimal title

- Course name or session question in Source Serif 4.
- Session number/date in small sans text.
- No agenda, learning objectives, institutional boilerplate, or decorative robot imagery.

### 2. Question field

- One major question spanning 8–10 columns.
- Optional one-sentence tension below.
- Used to open a discussion or mark an intellectual turn.

### 3. Claim + evidence

- 4/8 or 5/7 split.
- Short claim or interpretation on the narrow side; dominant figure, quotation, or result on the wide side.
- Avoid enclosing either side in a card.

### 4. Full-bleed evidence

- Figure or image occupies most of the safe area.
- Takeaway title above; direct annotations on the evidence; caption and visible source below.
- No duplicated prose explaining what the audience can already see.

### 5. Study anatomy

- Left-to-right or top-to-bottom sequence only when causal or procedural order matters.
- Use no more than five stages.
- Use thin Ink rules and concise labels; avoid decorative flowcharts.

### 6. Comparison

- 6/6 aligned columns or two stacked bands.
- Shared baseline and identical visual scale.
- A thin central rule may separate conditions; do not use two floating cards.
- The comparison title states the important difference.

### 7. Code trace

- 7/5 or 8/4 split: short code fragment plus plain-language state/output.
- Highlight only the focal 1–3 lines.
- The slide states the input type, transformation, and resulting object.

### 8. Quotation or excerpt

- Maximum 35–45 words visible.
- Serif quotation; sans attribution.
- Highlight a short phrase only when it is the discussion object.
- Longer text belongs in the workbook or reading guide.

### 9. Validation turn

- Central claim or estimate followed by one decisive diagnostic.
- Moss marks evidence that supports the method; Vermilion marks failure or unresolved dependence.
- State the revised inference, not merely “limitations.”

### 10. Synthesis / exit question

- Return to the opening question.
- Use the recurring form: **claim → target → evidence → failure mode → revised claim**.
- Never end on “Thank you,” housekeeping, or an unframed bibliography.

## Figures and charts

- One primary message per chart; encode only the comparisons necessary for that message.
- Use direct labels wherever practical. Avoid legends that force eye travel.
- Use Ink for human observations and Cobalt for model output by default.
- Show uncertainty and sample size when the source supports them.
- Use Vermilion for a focal discrepancy, not automatically for every negative value.
- Use no 3D, shadows, gradient fills, boxed legends, or heavy borders.
- Gridlines are sparse and light; zero or substantively meaningful reference lines are stronger.
- Axes and annotations use plain language and include units.
- Do not truncate an axis when doing so distorts the comparison; if a justified detail view is used, label it explicitly.
- A figure reconstructed from a paper must preserve the data, scale, uncertainty, and substantive meaning. Record the source and reconstruction method in notes.
- Small multiples share scales unless the difference is explicitly marked.
- Maps require a legend, projection/source note, and non-color cue when categories matter.

## Tables

- Use tables only for exact mappings or compact comparisons.
- Maximum guideline: 5 columns × 7 body rows. Split larger tables.
- No vertical gridlines. Use one header rule and light row separators only where needed.
- Left-align text; right-align numbers; align decimals when useful.
- Emphasize one row/column through type weight or a pale field, not saturated fills.
- Never paste a spreadsheet screenshot.

## Code and computational objects

- Slides show no more than roughly 8–12 lines of code. Longer code belongs in the workbook.
- Code must be large enough to read from the back of the room: 23 px minimum on the 1280 × 720 canvas.
- Use a restrained light code field (`#ECE8DE`) with Ink text. Syntax color is minimal: Cobalt for names/functions, Vermilion for errors, Moss for passed checks.
- Never show an API key, `.env` contents, identifiable data, or a live credential field.
- Always label the exact input object and output object; display `type(...)`, a compact `repr`, or a small schema when it helps.
- Highlight the line under discussion and show its plain-language effect beside it.
- Terminal screenshots are not code slides. Recreate the relevant line or output as accessible text.
- Use fragments only when students must predict the next state before it appears.

## Images and screenshots

- Prefer one dominant, substantively relevant image to a collage.
- Documentary photographs, archival material, streetscape/satellite imagery, interaction frames, and study materials are appropriate when they carry evidence.
- Avoid generic AI brains, robots, circuit heads, glowing chat bubbles, and decorative stock photography.
- Screenshots are used only when the interface, prompt presentation, or original visual rhetoric is itself the object of analysis.
- Crop deliberately to the intended frame; do not stretch.
- Target at least 2000 px on the long edge for a dominant raster image. Replace visibly soft or compressed assets.
- Every meaningful image requires alt text and a source/licence record.
- Do not reuse the same image in the same deck except when a deliberate return supports the narrative.

## Quotations, captions, and citations

### Visible citation

At the bottom-left of a sourced slide:

`Author(s), year · Short title or venue · DOI/domain`

- 16 px Source Sans 3 in Ink or a contrast-checked secondary tone.
- Prefer DOI or canonical publisher URL.
- Cite the exact source supporting the visible claim or asset.
- A citation is not a substitute for explaining what the evidence means.

### Figure captions

- One sentence maximum.
- State what is measured or shown; do not restate the title.
- Put sample, units, or condition details here when needed to interpret the figure.

### Speaker-note source block

Every externally sourced visual and every non-trivial externally sourced claim receives a structured note:

```markdown
::: {.notes}
[Sources]
- Claim: concise description | Source: DOI or canonical URL | Accessed: YYYY-MM-DD
- Asset: filename/description | Source: canonical URL | License/permission: status
[/Sources]
:::
```

Instructor prompts and timing may appear elsewhere in notes, never inside the `[Sources]` block. No planning notes appear on the visible slide.

## Callouts and emphasis

- Prefer composition, scale, and whitespace to boxes.
- One callout maximum per slide.
- Callouts use a 4 px left rule and a pale semantic field; no rounded dashboard cards, icons, or drop shadows.
- Cobalt = definition/method; Moss = validation; Vermilion = failure/caution.
- Do not use a callout for ordinary body text.

## Section dividers and course orientation

- Section dividers use Ink background with Paper serif type and one small Cobalt, Vermilion, or Moss rule.
- Each week includes one early “where we are” course-map slide showing the four cumulative movements: Observe, Intervene, Simulate, Delegate & Audit.
- The active movement is indicated by position, weight, and color—not color alone.
- Do not repeat a full agenda after every break. Use a short transition question when resuming.

## Motion and interaction

- Deck transition: short fade only; no slide, zoom, cube, or background animation.
- Use fragments sparingly for prediction, sequential causal logic, or stepwise code tracing.
- Never animate chart values merely for drama.
- No autoplay media. Provide captions/transcripts for audio or video.
- Honor `prefers-reduced-motion` in the web theme.

## Accessibility

- Meet WCAG AA contrast for all instructional text; aim for AAA for normal body text.
- Never communicate meaning by color alone.
- Provide alt text for every meaningful visual and mark purely decorative elements accordingly.
- Maintain a logical reading order in HTML and PDF.
- Use descriptive link text, not bare “click here.”
- Avoid flashing, rapid motion, very long italic passages, and fully justified text.
- Explain abbreviations on first use.
- Use captions or a transcript for audio/video; ensure discussion materials are available without hearing the clip live.
- Test at 1280 × 720 and 1920 × 1080 and inspect a PDF export at 100%.

## Central implementation

The pilot will establish—not duplicate—the following shared assets:

```text
design/
├── DESIGN_SYSTEM.md
├── theme.scss              # all colors, type, spacing, and Reveal overrides
├── fonts/                  # vendored WOFF2 files and licences
├── components/             # minimal Quarto partials/classes only if repeated
└── qa/                     # render/overflow/accessibility checks
```

- Decks import one central theme. They do not define per-week palettes or font sizes.
- Model identifiers, code utilities, and workbook styles remain outside the slide theme.
- Reusable classes describe communicative function (`question`, `evidence`, `comparison`, `code-trace`, `validation`) rather than visual trivia.
- Avoid gratuitous layout abstractions. Standard Quarto columns plus a small set of semantic classes should be sufficient.

## Rendering and QA gate

Before any deck is approved:

1. Render the HTML deck from a clean environment.
2. Capture every slide at 1280 × 720.
3. Inspect every slide individually at full size; use a montage only for rhythm and consistency.
4. Check title wrapping, text overflow, code clipping, figure resolution/crops, source visibility, alt text, and reading order.
5. Confirm every non-trivial claim and external asset has a `[Sources]` note block.
6. Export and inspect the PDF at 100%; check that fragments resolve intelligibly and links/citations remain legible.
7. Check that the deck contains no secrets, stale model identifiers, unresolved placeholders, or workbook-length code.
8. Confirm the deck’s opening question is resolved or productively revised by its final slide.

The Phase 5 pilot is not approved until these checks pass and the instructor has reviewed the rendered output.

