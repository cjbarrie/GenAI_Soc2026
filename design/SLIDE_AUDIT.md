# 2025 Slide Audit

**Audit date:** 2026-08-18  
**Scope:** Eleven Quarto/Reveal.js source decks (`week1`–`week11`), ten rendered HTML decks, one PDF, and their local visual assets. The original repository remains read-only.

## Executive finding

The old slides should be mined for arguments, study summaries, and selected figures—not restyled wholesale. Across 4,893 source lines there are 424 headings, 101 image references, 86 code-fence delimiters, and 54 blank slide titles. Deck length varies from 24 to 74 principal headings, while most weeks use the unmodified Reveal.js appearance. The resulting course looks episodic rather than like one designed intellectual sequence.

The strongest reusable material is conceptual: the sociology/computational-methods lineage in Week 1; qualitative workflow in Week 5; structured-output and validation distinctions in Week 6; synthetic-population validation in Week 7; experimental interaction distinctions in Week 8; selected network reasoning in Week 9; and experiment-forecasting design in Week 10. Most code should move to the workbook, and most screenshots should be replaced or recropped from verified current sources.

## Cross-deck findings

### Critical

- **No shared design system.** Decks repeat similar YAML settings but have no common SCSS, layout primitives, typography hierarchy, citation rule, or image treatment.
- **Lecture and workbook functions are mixed.** Weeks 4, 6, 7, 9, and 10 carry extended code and implementation detail on slides. This encourages passive copying and leaves too little space for inspecting intermediate outputs.
- **The narrative often follows a reading inventory.** Repeated “Reading 1 / design / results / questions” sequences summarize papers without consistently building a lecture-level claim.
- **Visual provenance is inconsistent.** Some captions include a DOI or source; many images have no visible source, and there are no speaker-note source records.
- **The early technical sequence dominates.** Weeks 2–3 contain 62 principal headings on embeddings, attention, training, and classification heads that no longer match the approved architecture.
- **Several screenshots and model/API examples are time-stamped to 2025.** These require replacement rather than cosmetic reuse.

### Important

- **Density is inconsistent.** Week 9 is a 962-line research-talk deck with 74 principal headings, while Week 1 has 34 headings and almost no explanatory notes. Several lectures would be difficult to pace inside a discussion-and-lab seminar.
- **Slide titles often name topics rather than make claims.** Examples include “Why it matters,” “Introduction,” “Reading 1,” and 54 untitled slides. Titles therefore do little to preserve the argument when students revisit the deck.
- **Figures are usually screenshots of paper pages or interfaces.** Many should become clean, directly labeled reconstructions; screenshots should remain only when the interface or original visual rhetoric is itself evidence.
- **Repeated incremental bullets create a default rhythm.** Incremental reveal is enabled in most decks, sometimes globally. It should be used only when sequence or prediction matters.
- **Callouts are overused as layout.** Quarto callout boxes frequently substitute for hierarchy and produce a documentation-site aesthetic.
- **Some image links omit extensions in Week 1.** Even where a browser resolves them, this is fragile and should not be copied.
- **No speaker notes are present.** Instructor prompts, timing, transition logic, and source blocks need a consistent home outside visible slide copy.

### Nice to have

- Consolidate 115 raster assets into a sourced asset library; remove 88 generated/publishing-worktree duplicates from any new repository structure.
- Prefer vector or high-resolution exports for plots and diagrams. The 242×410 Goffman cover and the 512×164 Schelling image are unsuitable for large projection.
- Add alt text for meaningful visuals and never encode distinctions by color alone.
- Provide projection-first HTML plus a checked PDF export; do not force one dense slide to serve simultaneously as lecture, transcript, and workbook.

## Deck-by-deck disposition

| Old deck | Main function | Reuse | Retire or rebuild |
|---|---|---|---|
| Week 1 | Course opening and computational-sociology lineage | AI-policy voice; text-as-data, ML, simulation, and audit lineage | Replace the long screenshot parade with one coherent course map and a small number of sourced examples |
| Week 2 | Static embeddings | At most one optional conceptual comparison | Retire as a weekly deck; move historical/technical detail to optional foundations material |
| Week 3 | Transformers and DistilBERT | One compact account of context-sensitive prediction | Retire architecture and training-loop sequence; move relevant classification mechanics to the workbook |
| Week 4 | LLM foundations, access, annotation | Messages/inputs/settings distinctions; hosted/local routes; validation logic | Rebuild around current OpenRouter SDK and research records; move API implementations to the workbook; replace interface screenshots |
| Week 5 | Qualitative inquiry | Researcher → LLM → researcher loop; evidence linkage; reflexivity; data stewardship | Rebuild around the 2026 three-paper disagreement; replace unattributed paper screenshots |
| Week 6 | Structured output and annotation studies | Structured-output choices and validation/replication concepts | Redistribute into Sessions 1–3 and 12; move code patterns to worked notebook cells |
| Week 7 | Synthetic survey respondents | Persona construction, distributional validation, flattening distinction | Update readings and results; retain only figures whose claims and provenance remain current |
| Week 8 | Interactive/personalized experiments | Fixed versus conversational treatment distinction; design questions | Rebuild with 2025–26 conversational studies; reduce political-science prehistory and screenshot sequences |
| Week 9 | Survey-response-network research talk | Selected explanation of constraint, centrality, and network structure as a substantive case | Do not use as a lecture template; substantially shorten and move technical metrics to an optional case/appendix |
| Week 10 | Forecasting experiments and cognition models | Experimental-forecasting design and observed-versus-predicted comparison | Replace working-paper metadata with the 2026 *Nature* article; move Centaur to optional material |
| Week 11 | Interactionism and multimodal data | General question of modality-specific evidence and a few data-schema ideas | Drop Blumer/Seamless spine; rebuild Session 4 from current multimodal measurement literature |

## Content that belongs off slides

- complete SDK calls and setup instructions;
- blocks longer than roughly 8–12 lines of code;
- package installation and provider comparison tables that will date quickly;
- full prompt templates when only one design decision matters;
- detailed metric definitions that students need while coding;
- prose summaries that duplicate the workbook or assigned paper;
- large bibliographic entries.

These belong in the workbook, instructor notes, appendices, or linked reference pages. Slides may show a short focal code fragment when the class is actively tracing it.

## New-deck narrative contract

The communication job is:

> By the end of each session, graduate sociology students should be able to state what inference an LLM-assisted design supports, identify the evidence that would validate it, and explain the focal computation in plain language.

Each deck should therefore follow a flexible argument rather than a fixed template:

1. sociological question or empirical tension;
2. competing claims from the readings;
3. methodological opportunity and inferential target;
4. study anatomy or mechanism;
5. evidence and what it does—and does not—show;
6. one focal input → transformation → output handoff to the workbook;
7. failure mode and validation response;
8. synthesis or open inference question.

The sequence should not become eight labeled agenda sections. It is the narrative logic used to select and order slides.

