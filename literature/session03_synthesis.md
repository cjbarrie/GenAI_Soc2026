# Session 3 literature synthesis

## Central synthesis

The session should begin from sociology's existing qualitative practice rather than from a list of possible AI uses. The most productive question is how a researcher can use a bounded model contribution while preserving the comparisons, source context, memos and revisions that give a qualitative claim its warrant.

## Foundational spine

### Deterding and Waters (2021)

Flexible coding distinguishes broad index coding from later analytic coding. This gives the class a concrete way to explain why locating relevant passages and developing an interpretation are different forms of work.

### Timmermans and Tavory (2012, 2022)

Abductive analysis treats surprises and misfitting cases as opportunities to revisit assumptions, compare alternatives and develop theory. This anchors the use of countercases and revision in established qualitative methodology rather than in an AI-specific checklist.

### Stuart and Laryea (2026)

Their pragmatist framework asks how researchers move beyond recurring topics toward accounts of goals, obstacles, strategies and consequences. It helps distinguish a descriptive theme from a sociological explanation.

## LLM evidence

### Liu et al. (2024) and Wu et al. (2025)

Long input is not equivalent to cumulative analytic memory. Liu et al. show weaker use of relevant information placed in the middle of long contexts. LongMemEval separates memory into indexing, retrieval and reading, making clear that systems decide what earlier material is stored, recovered or omitted. These findings motivate explicit source IDs, retrieval records and researcher memos.

### Mehta et al. (2025)

Their published examples show generated quotations that modify or truncate transcript wording. This supplies an empirical reason to perform exact source checks before assessing a model-proposed theme.

### Than et al. (2025)

Than and colleagues evaluate LLM classification of complete news articles inside a researcher-led coding workflow. Their contribution is a bounded division of labour: researchers define the task, models classify, disagreement identifies cases for closer inspection and researchers validate or revise the coding process. Their paper does not show autonomous thematic analysis.

### Ibrahim and Voyer (2026)

Technological reflexivity directs attention to both sides of the interaction: researchers encode assumptions in prompts, and model responses can redirect later analysis. The relevant research record therefore includes the researcher's pre-model memo, exact prompt and supplied material, raw output, subsequent response and any change in the working interpretation.

## Applied design

The cumulative example uses eight labelled interview excerpts about mutual aid and political solidarity. The model receives a clearly stated question and the complete small corpus, then proposes one candidate relationship with supporting excerpt IDs. The researcher:

1. verifies that the cited records exist;
2. reads the passages with speaker and sequence information;
3. compares supporting and contrary cases;
4. considers another explanation;
5. records how the suggestion affected subsequent attention; and
6. writes a narrower claim.

The same process is then represented in Python. Code organizes the record and performs traceable checks; it does not decide whether an interpretation is sociologically convincing.

## Reading-to-code alignment

| Literature contribution | Python object or operation | Research meaning |
|---|---|---|
| Deterding and Waters | excerpt records and stable index codes | Preserve a route from coding back to the material. |
| Liu et al.; Wu et al. | explicit corpus sent in the prompt and source index | Do not assume long context or a new call carries analytic memory. |
| Mehta et al. | source-ID lookup and exact record retrieval | Establish whether cited evidence exists without calling the theme valid. |
| Than et al. | separate model proposal and researcher review | Give the model a defined job inside a larger workflow. |
| Ibrahim and Voyer | `interaction_log` | Record what the researcher thought before, what the model proposed and what changed next. |

## Source files used in the deck

- `literature/source_pdfs/session03/than_et_al_2025_published.pdf`
- `literature/source_pdfs/session03/ibrahim_voyer_2026_published.pdf`
- `literature/source_pdfs/session03/mehta_et_al_2025_scientific_reports.pdf`
- `literature/source_pdfs/session03/stuart_laryea_2026.pdf`
- `literature/source_pdfs/session03/liu_et_al_2024_lost_in_middle.pdf`
- `literature/source_pdfs/session03/wu_et_al_2025_longmemeval.pdf`
