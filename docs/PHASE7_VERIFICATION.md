# Phase 7 verification record

Completed August 19, 2026.

## Release result

The course is internally integrated and ready for instructor review. The final pass verified:

- 14 aligned sessions and all required artifact families;
- 15 notebooks executed in place with no error outputs;
- novice-facing code cues, actual input values and Python types, return values, checks, reading links, and oral-explanation prompts;
- 16 automated tests passing;
- 35 structurally valid bibliography entries and 30 DOI records matching Crossref metadata;
- 135 files with no broken internal links;
- 59 distinct external links: 57 reachable and 2 access-restricted, with none broken;
- 14 Reveal decks comprising 237 slides, all rendered with no detected overflow;
- 29 rendered notebook/deck pages checked at desktop and mobile widths, for 58 checks with no failures;
- consistent central model identifiers and no embedded API keys or other secret patterns.

The two restricted resources returned HTTP 403 from Oxford Academic and the University of Michigan workshop site. Their responses indicate automated-access restrictions rather than broken targets. The Alvero et al. DOI is retained in the bibliography, while student-facing materials use the functioning Sociological Science article page because the DOI resolver currently redirects to a broken route.

## Visual and pedagogical findings

The slide review led to shorter shared headings and multiline versions of dense dictionary/list construction in Sessions 3, 4, 13, and 14. The capture checker now distinguishes Quarto's intentional line-number gutter from actual code wrapping. The generated notebooks were rebuilt after these changes and executed again.

Every scaled worked example now makes students identify the input, Python type, operation, output, check, and substantive meaning. The printed trace exposes actual argument values and types immediately before the function call. Optional extensions are visibly separated so weekly completion credit remains narrow and attainable.

## Scope note

The repository has no separate course-site configuration. Accordingly, web/mobile QA covers the actual student-facing outputs present here: rendered Jupyter notebooks and Reveal decks. The repeatable release procedure is documented in `docs/MAINTENANCE.md`.
