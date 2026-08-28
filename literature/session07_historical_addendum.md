# Session 7 historical addendum — before “silicon samples”

## Why this belongs in the lecture

Clinton and colleagues open *Public Opinion in the Age of AI* by placing LLM-generated respondents beside an earlier effort to turn survey traces into a computational public: the Simulmatics Corporation’s 1960 election work. This history sharpens rather than merely decorates the lecture. It shows that three current questions predate LLMs:

1. Which people and opinions are represented in the source data?
2. What behavioral assumptions turn those records into predictions?
3. Is the output being used to understand a public, predict it, or help act upon it?

## Simulmatics: verified teaching points

- Simulmatics was founded in 1959 and was bankrupt by 1970. Its most famous early project supplied computer-assisted election analysis to the Kennedy campaign in 1960 (Lepore & Berman 2021; JFK Library archival catalogue).
- The project assembled roughly 100,000 earlier poll records stored on punch cards, divided voters into 480 types and grouped issues into approximately fifty clusters. These categories supported counterfactual predictions about how segments might respond to campaign moves (Lepore 2020; de Sola Pool, Abelson & Popkin 1964).
- The model ran on contemporary mainframe computing. The important novelty was not a machine interviewing virtual people in natural language. It was the combination of accumulated survey data, a categorical model of voter behavior and rapid scenario comparison.
- “People Machine” was partly publicity language. The 1964 scholarly account explicitly rejected the idea that a machine ran the campaign and described the work as a research technique for understanding voter behavior (de Sola Pool, Abelson & Popkin 1964).
- After Kennedy won, Simulmatics claimed influence without demonstrating that its advice caused the victory. That is an early warning against inferring practical impact from a successful outcome (Lepore & Berman 2021).
- The historical record also exposes a representation failure: Black voters were poorly represented in the poll archives on which the categories were built. A more elaborate simulation could not restore people excluded from the underlying observations (Lepore 2020).

## Nearby but distinct simulation traditions

- **Microsimulation:** Orcutt (1957) proposed simulating individual decision units with explicit probabilistic relationships to study policy consequences. The inferential object was a modeled socioeconomic system, not a collection of fluent survey respondents.
- **Mechanism-based social simulation:** Schelling’s segregation models show how specified local rules can generate unexpected aggregate patterns. The model is useful because its rules are explicit and deliberately simplified, not because each checker is claimed to be a realistic person.
- **Synthetic populations for agent-based models:** later work constructs populations whose attributes match selected survey or census margins, then applies stated rules. Matching margins is a population-construction step; it does not by itself validate behavior or opinion generation.

These traditions should not be presented as primitive LLMs. Their value for Session 7 is the contrast in claims. LLM personas often hide their behavioral model inside trained weights and produce realistic language, whereas classical simulations normally expose a smaller set of rules. Both still require a defined target, source data and validation appropriate to the intended inference.

## Sources

- Joshua D. Clinton et al. 2026. *Public Opinion in the Age of AI*. APSA Preprints, version 5, 15 July 2026. https://doi.org/10.33774/apsa-2026-1rg21-v5. Local PDF: `literature/source_pdfs/session07/clinton_et_al_2026_public_opinion_age_ai.pdf`.
- Ithiel de Sola Pool, Robert P. Abelson and Samuel L. Popkin. 1964. *Candidates, Issues, and Strategies: A Computer Simulation of the 1960 Presidential Election*. MIT Press.
- Jill Lepore and Fran Berman. 2021. “The People Machine: The Earliest Machine Learning?” *Harvard Data Science Review* 3(1). https://doi.org/10.1162/99608f92.87b0ec26.
- John F. Kennedy Presidential Library and Museum. “1960 Campaign: Simulmatics (1 of 2 folders),” Lawrence F. O’Brien Personal Papers, LOBPP-016-010.
- Guy H. Orcutt. 1957. “A New Type of Socio-Economic System.” *Review of Economics and Statistics* 39(2): 116–123. https://doi.org/10.2307/1928528.
- Thomas C. Schelling. 1971. “Dynamic Models of Segregation.” *Journal of Mathematical Sociology* 1(2): 143–186. https://doi.org/10.1080/0022250X.1971.9989794.
- Kevin Chapuis, Patrick Taillandier and Alexis Drogoul. 2022. “Generation of Synthetic Populations in Social Simulations: A Review of Methods and Practices.” *Journal of Artificial Societies and Social Simulation* 25(2): 6. https://doi.org/10.18564/jasss.4762.
