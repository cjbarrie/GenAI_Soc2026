# Session 7 source and visual plan

**Status:** Pre-build source plan, 25 August 2026.

This is the acquisition and screenshot gate between the approved architecture and slide authoring. It exists to prevent four recurring problems: screenshots of the wrong document, unreadable full-page previews, cropped figures, and claims that appear before their source has been introduced.

## Rules for every paper sequence

1. Introduce the paper with its full citation, research question, sample or corpus, design and reason it is in the session.
2. Use the published paper or author-posted manuscript, not a search-result card, library-login page or unrelated preprint version.
3. Render the complete relevant PDF page before choosing a crop.
4. Crop only after checking the figure number, caption, axis labels, sample size and surrounding qualifying text.
5. Put a readable crop on the slide. A thumbnail of a full page does not count as evidence.
6. State in ordinary language what the image shows and which claim it supports.
7. Keep the full citation on screen in a consistent short format; put the DOI or stable URL in the notes or reference field rather than allowing it to run off the slide.
8. If the source cannot be acquired, stop and ask for the PDF. Do not substitute a web preview or a less suitable paper.

## Sources already local

| Source | Local file | Planned visual job | Verification still required |
|---|---|---|---|
| NORC, 2024 GSS Release 3a codebook | `literature/source_pdfs/session07/gss_2024_codebook_release_3a.pdf` | Slides 5 and 56: identify the official item and show the unweighted 2024 frequency table | Crop the `EQWLTH` box across codebook pages 187–188; do not use its truncated label as the full question wording |
| Taubenfeld et al. (2026) | `literature/source_pdfs/session07/taubenfeld_et_al_2026_behavioral_dispositions.pdf` | Slides 35–37: pipeline, directional alignment and missed human disagreement | Render Figure 1 and Figures 2–3 with captions; choose one legible panel per slide |
| Gordon et al. (2026) | `literature/source_pdfs/session07/gordon_et_al_2026_fidelity_paradox.pdf` | Slides 45–49: sample, persona conditions, forced answer versus probability elicitation, post-stratification | Verify the exact figure and table locations and retain the N=996 design details on screen |
| Minder et al. (2026) | `literature/source_pdfs/session07/minder_et_al_2026_synthetic_persona_pretraining.pdf` | At most one terminology aside, if retained | Do not treat an alignment/pretraining paper as population-validation evidence |

## Priority sources to acquire before slide authoring

| Source | Slide job | Required evidence image |
|---|---|---|
| Kish (1965 or 1985) | Explain why representativeness comes from the sampling design | A readable passage or diagram that distinguishes sample surveys from other forms of observation |
| Groves and Lyberg (2010) | Introduce total survey error | The authors' framework or a precisely relevant passage, not an instructor-invented checklist presented as theirs |
| Deming (1944) | Show that survey error is a chain, not one number | A short highlighted passage naming several sources of error |
| Bourdieu, “Public Opinion Does Not Exist” | Explain forced opinion, common question meaning and aggregation | The full surrounding quotation for the three assumptions; highlight only after verifying context |
| McCall (2005) | Explain heterogeneity within categories | A short passage on intracategorical complexity with enough surrounding text to preserve meaning |
| Argyle et al. (2023) | State the original silicon-sampling proposition fairly | The main design figure or table plus the paper's own claim |
| Kozlowski and Evans (2025) | Organize the methodological promise and risks | The source's own framework or a set of short verified passages; do not invent a six-part diagram and attribute it to them |
| Park et al. (2024/2025) | Present the strongest interview-grounded positive case | The agent-construction/evaluation design and the result benchmarked against participants' test-retest agreement |
| Boelaert et al. (2025) | Show topic-specific bias and restricted variation | A figure that displays disagreement between model and poll distributions |
| Bisbee et al. (2024) | Show why matching a mean can hide variance, associations and instability | At least two panels from the published article, separated across slides if labels become small |
| Wang, Morgenstern and Dickerson (2025) | Show within-group flattening and exaggerated group differences | The central empirical figure plus a short passage defining the harm at issue |
| Chen, Zhu and Zheng (2026) | Show demographic over-determination | A cross-domain result in which persona fields pull responses too strongly toward stereotypes |
| Abeliuk, Gaete and Bro (2026) | Extend the problem across societies | The clearest cross-societal comparison with countries and models readable |

## GSS visual sequence

The GSS example needs two different official sources because the 2024 codebook's `EQWLTH` label is truncated.

1. **Question slide:** use the complete wording from an official GSS questionnaire and typeset it at readable size. A small source crop may sit beside it, but the question itself must be readable without zooming.
2. **Benchmark slide:** use a tight crop of the Release 3a codebook table. The slide text must say “unweighted frequencies among 2,161 valid responses.”
3. **Population-claim slide:** place the unweighted table beside the documented weighting step. Do not label the table “U.S. public opinion.”

The verified counts for scale points 1–7 are `699, 180, 294, 326, 207, 120, 335`. The verified valid-response percentages are `32.3, 8.3, 13.6, 15.1, 9.6, 5.6, 15.5`.

## Visual-format checks before a source enters the deck

- The source is the intended article and version.
- Figure and table numbers match the slide text.
- The crop includes enough context to identify the evidence.
- No axis label, legend, caption qualifier or sample size is cut off.
- Text intended to be read is at least as large as body text after insertion.
- Aspect ratio is preserved; images are never stretched to fill slide width.
- Highlight boxes point to a specific finding and do not conceal source text.
- Two source images are used only when both remain readable; otherwise split the slide.
- The citation fits above the footer with visible breathing room.

## Build order

1. Acquire and inventory the priority PDFs.
2. Render the planned pages and record candidate page numbers.
3. Build only the opening and “what came before” section.
4. Render that section and run the title-only, purpose, source and transition checks.
5. Build the positive-case and validation-evidence sections.
6. Render and inspect every paper image at presentation size.
7. Build the cumulative example, local-model walkthrough and Python sequence.
8. Run the code with cached data, then render and inspect the complete deck.
9. Re-read the slide titles alone and confirm that they express the argument in ordinary spoken English.
