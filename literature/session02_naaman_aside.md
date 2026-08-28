# Focused literature search — Mor Naaman group and AI-shaped writing

**Status:** Focused search for a short Session 2 aside, conducted August 19, 2026.

## Recommendation

Use **Agarwal, Naaman, and Vashistha (2025)** as the focal aside. It most directly matches the remembered finding that AI suggestions can change people’s writing style. Pair it with Schroeder, Roy, and Kabbara under one methodological point:

> The texts and human labels used in a measurement study may already have been shaped by an AI system.

This deserves two or three slides, not another full paper section. The aside broadens provenance in a useful way:

- **Schroeder et al.:** a human benchmark may not be independent if annotators first see model suggestions.
- **Agarwal et al.:** the source text may not be independent of AI if writers compose with model suggestions.

For a study of public comments, social-media posts, applications, or workplace communication, researchers may therefore be measuring a hybrid human–model artifact rather than unaided human expression.

## Best match: writing style and cultural homogenization

### Agarwal, Dhruv, Mor Naaman, and Aditya Vashistha. 2025. “AI Suggestions Homogenize Writing Toward Western Styles and Diminish Cultural Nuances.” *CHI 2025*.

- **Design:** Cross-cultural controlled experiment with 118 participants from India and the United States. Participants completed four culturally grounded English-language writing tasks with or without GPT-4o autocomplete suggestions.
- **Tasks:** Favorite food, favorite public figure, a festival or holiday, and an email asking a manager for two weeks of leave.
- **Evidence:** Interaction logs, embedding similarity, predictive modeling, lexical diversity, and qualitative content analysis.
- **Main result:** Writing produced with AI suggestions became more similar across the Indian and American samples. The directional analyses indicated stronger movement of Indian writing toward unassisted American writing than the reverse.
- **Concrete style result:** AI suggestions increased lexical diversity among Indian participants toward the American baseline, eliminating the initial difference on that measure. The authors also report more generic cultural descriptions and fewer culturally specific details in assisted Indian writing.
- **Unequal benefit:** Both groups became faster, but the productivity gains were larger for American participants; Indian participants more often had to work around culturally incongruent suggestions.
- **Important limit:** This is a relatively small, English-language, two-country experiment using particular tasks and an autocomplete implementation. It does not establish that every writing assistant or cultural setting produces the same direction of homogenization.

**Session 2 use:** Put one study-interface image or the paper’s comparison of cultural descriptions beside one direct question: “If an AI helped produce the comments, what exactly are we measuring when we classify them?”

This should not become a generic warning that all AI-assisted text is inauthentic. The methodological point is that mode of production becomes relevant provenance and may affect group comparisons, temporal comparisons, and interpretations of voice or cultural style.

**Primary sources:** [arXiv full text](https://arxiv.org/html/2409.11360v3); [CHI DOI](https://doi.org/10.1145/3706598.3713564).

## Closely related work from the same collaboration

### Jakesch, Maurice, Advait Bhat, Daniel Buschek, Lior Zalmanson, and Mor Naaman. 2023. “Co-Writing with Opinionated Language Models Affects Users’ Views.” *CHI 2023*.

- Online experiment with 1,506 participants writing about whether social media is good for society.
- Treatment participants received language-model suggestions configured to favor a positive or negative view.
- The suggestions changed the positions expressed in participants’ writing and shifted responses in a subsequent attitude survey.
- This paper establishes that AI assistance may affect not only style but also the views writers express and report.

**Primary sources:** [arXiv](https://arxiv.org/abs/2302.00560); [CHI DOI](https://doi.org/10.1145/3544548.3581196).

### Williams-Ceci, Sterling, Maurice Jakesch, Advait Bhat, Kowe Kadoma, Lior Zalmanson, and Mor Naaman. 2026. “Biased AI Writing Assistants Shift Users’ Attitudes on Societal Issues.” *Science Advances* 12(11): eadw5578.

- Two preregistered experiments with 2,582 participants writing about contested societal issues.
- Biased autocomplete suggestions shifted post-task attitudes toward the assistant’s position.
- The influence was stronger than exposure to similar static text, suggesting that the effect was not simply access to the arguments.
- Most participants did not recognize the bias or its influence; warnings before or after writing did not remove the effect.
- This is the strongest recent causal evidence in the sequence, but its focus is attitude change rather than writing-style homogenization.

**Primary sources:** [open-access article](https://pmc.ncbi.nlm.nih.gov/articles/PMC12978215/); [DOI](https://doi.org/10.1126/sciadv.adw5578); [materials and data](https://zenodo.org/doi/10.5281/zenodo.18048642).

### Bhat, Advait, Marianne Aubin Le Quéré, Mor Naaman, and Maurice Jakesch. 2026. “Reactive Writers: How Co-Writing with AI Changes How We Engage with Ideas.” *CHI 2026*.

- Mixed-methods study combining 19 retrospective interviews with interaction traces from 1,291 AI-assisted writing sessions.
- The authors describe **reactive writing**: writers spend more of the process evaluating suggestions, often before completing their own ideation.
- Suggested ideas can seed directions that writers subsequently elaborate, even while writers feel in control and do not notice the influence.
- This offers a plausible process account connecting autocomplete assistance to the observed changes in expression and attitudes.

**Primary sources:** [arXiv full text](https://arxiv.org/html/2603.10374v1); [CHI DOI](https://doi.org/10.1145/3772318.3791529).

## Suggested placement and wording

Place this immediately after the Schroeder aside and before the break. The two-paper turn can be framed in ordinary language:

1. “The human reference labels may already reflect the model’s suggestion.”
2. “The texts we want to classify may also have been written with model suggestions.”
3. “So provenance is not only a model-and-prompt field. We may also need to record how the source text and reference labels were produced.”

One optional discussion question is enough:

> If AI assistance changes how groups express the same experience, what happens to a study comparing those groups with a text classifier?

This links the substantive result back to measurement without requiring additional code. A later workbook note can add an optional `text_production_mode` field with values such as `unassisted`, `ai_autocomplete`, `ai_rewrite`, or `unknown`.

## Reading-status recommendation

- Agarwal et al.: in-class aside with a paper image and one result; optional reading.
- Williams-Ceci et al.: optional current extension in the reading guide or speaker notes.
- Bhat et al.: optional current extension, especially useful in a later session on human–AI interaction or cognitive offloading.
- Jakesch et al.: background predecessor; do not assign in addition to the 2026 *Science Advances* paper.

