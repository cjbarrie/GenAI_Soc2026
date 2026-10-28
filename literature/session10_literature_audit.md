# Week 10 literature audit: writing, influence and relationships

**Status:** Superseded by `session10_revised_architecture.md`. The earlier audit treated AI companionship as a main component. The revised plan is confined to LLMs within human-to-human relationships.

## Recommended question

**What happens when an LLM becomes part of a conversation?**

This question covers two arrangements that need to be distinguished:

1. **AI-mediated communication:** a model modifies, completes or generates a message sent from one person to another.
2. **Human–AI communication:** the model is itself the apparent conversational partner.

The two arrangements raise related questions about authorship, influence, disclosure and relationships, but they do not provide the same evidence or support the same claims.

## Historical lineage

### 1. Communication is jointly accomplished

Clark and Brennan's work on grounding treats communication as the collaborative establishment of sufficient common ground for the present purpose. A message is not only a container for information. Its meaning is established through what the parties know, what they believe each other knows, and the opportunities a medium gives them to repair misunderstanding.

**Teaching job:** establish why an intervention in message production can alter the interaction rather than merely save keystrokes.

### 2. Computer mediation changes the conditions of interaction

Kiesler, Siegel and McGuire compared face-to-face and computer-mediated group communication and studied differences in participation, decision-making and consensus. Early work often attributed computer-mediated communication's impersonal quality to reduced social-context and non-verbal cues.

Walther challenged a simple cues-removed account. His social-information-processing perspective argued that people can form interpersonal impressions and relationships through text, but do so through different cues and over a different timescale. The medium changes how relational information is conveyed; it does not remove relational work.

**Teaching job:** show that technologically mediated conversation had a substantial research history before generative AI, and that the effects of a medium depend on setting, time and use.

### 3. Interlocutors adapt their language to one another

Work on linguistic style matching showed that conversational partners coordinate aspects of their language, including turn by turn. This matters because wording is both an individual expression and an interactional accomplishment.

**Teaching job:** provide a sociological reason to care when a third party begins supplying the words.

### 4. Predictive text began intervening in message formulation

Arnold, Chauncey and Gajos found that predictive text suggestions encouraged shorter and more predictable image descriptions. Hohenstein and colleagues later showed in randomized messaging experiments that smart replies affected speed, emotional language and perceptions of the conversational partner.

**Teaching job:** establish the immediate predecessor to LLM co-writing. Suggestions were already shaping language and interaction before open-ended chat assistants.

### 5. AI-mediated communication names the new intermediary

Hancock, Naaman and Levy define AI-mediated communication as interpersonal communication in which an intelligent agent operates on behalf of a communicator by modifying, augmenting or generating messages to accomplish communication goals.

Their framework makes the source of the message analytically important. A recipient may be responding to the sender, the system, or a hybrid whose division of labour is not visible.

**Teaching job:** give the class a precise vocabulary for the first arrangement.

### 6. LLMs extend mediation and can become the interlocutor

LLMs differ from earlier smart replies in degree and, in some uses, in kind. They can generate extended and adaptive contributions across many domains, respond to conversational history, reproduce a stance across many suggestions, and conduct the exchange directly. The system can therefore influence a message sent to another person, shape the writer's own subsequent judgment, or become the object of disclosure and attachment.

The novelty should not be overstated. People still interpret messages through social context; recipients still make inferences about authorship and effort; relationships still depend on histories outside a single exchange. The research burden is to separate changes in text, changes in the writer, changes in the recipient's judgment, and changes in a relationship over time.

## Proposed required readings

### 1. The conceptual anchor

Hancock, Jeffrey T., Mor Naaman, and Karen Levy. 2020. “AI-Mediated Communication: Definition, Research Agenda, and Ethical Considerations.” *Journal of Computer-Mediated Communication* 25(1): 89–100. https://doi.org/10.1093/jcmc/zmz022.

- **Publication status:** Peer-reviewed journal article.
- **Question:** What is AI-mediated communication, and which parts of existing communication theory need to be reconsidered when AI operates on a communicator's behalf?
- **Material:** Conceptual synthesis of computer-mediated communication, signaling, trust, language production and human–computer interaction.
- **Design:** Theory and research agenda rather than an empirical test.
- **Principal contribution:** Defines AI-mediated communication and distinguishes possible roles for AI in producing interpersonal messages.
- **Limitation:** Written before current general-purpose LLMs. It anticipates rather than tests many of the systems now in use.
- **Teaching job:** Supplies the vocabulary and bridge from the history of computer-mediated communication to LLM-assisted writing.
- **Useful slide evidence:** The article's definition and framework for where AI enters the communication process.

### 2. The causal study of influence during writing

Williams-Ceci, Sterling, Maurice Jakesch, Advait Bhat, Kowe Kadoma, Lior Zalmanson, and Mor Naaman. 2026. “Biased AI Writing Assistants Shift Users' Attitudes on Societal Issues.” *Science Advances* 12(11): eadw5578. https://doi.org/10.1126/sciadv.adw5578.

- **Publication status:** Peer-reviewed journal article; open access.
- **Question:** Can biased autocomplete suggestions affect the attitudes of people using them to write about contested issues?
- **Participants and task:** Two preregistered experiments with 2,582 participants. Participants wrote short essays about societal issues with no suggestions, biased AI autocomplete, or relevant comparison conditions.
- **Design:** Experiment 1 compared control, biased AI suggestions and static arguments. Experiment 2 examined four issues and tested warnings and debriefing.
- **Principal finding:** In experiment 1, biased suggestions moved post-task attitudes 0.44 points toward the assistant's position on a five-point scale relative to control (95% CI 0.21–0.67; Cohen's d = 0.24). The corresponding estimate in experiment 2 was 0.41 points (95% CI 0.05–0.77; Cohen's d = 0.19). Static exposure did not account for the full effect, and warnings before or after the task did not significantly reduce it.
- **Limitation:** Short online writing tasks do not establish durable attitude change or effects in ordinary long-form writing. The study manipulates deliberately biased suggestions rather than estimating the distribution of bias in deployed assistants.
- **Teaching job:** Shows that the writing interface can be an influence mechanism, not merely a productivity tool.
- **Useful slide evidence:** The autocomplete interface, experimental design, and result comparing control, AI and static-text conditions.
- **Course continuity:** Week 3 cited this paper briefly to motivate a pre-model memo. Week 10 is where students would read and evaluate the full study.

### 3. The substantive application to ongoing relationships

Zhang, Yutong, Dora Zhao, Jeffrey T. Hancock, Robert Kraut, and Diyi Yang. 2026. “Interaction with AI Companions and Psychological Well-Being.” *Nature Human Behaviour* 10: 1966–1980. https://doi.org/10.1038/s41562-026-02516-2.

- **Publication status:** Peer-reviewed journal article, published 4 August 2026.
- **Question:** How do people's offline social networks, reasons for using AI companions, patterns of use and psychological well-being relate to one another?
- **Participants and material:** Survey responses from 1,131 adult Character.AI users in the United States, plus 4,664 donated chat sessions containing 464,687 messages from 237 participants.
- **Design:** Observational mixed-data study combining self-report, relationship descriptions and analysis of donated conversations.
- **Principal finding:** Smaller offline social networks were associated with identifying companionship as the primary use (beta = -0.03, 95% CI -0.05 to -0.01); companionship use was associated with lower well-being (beta = -0.48, 95% CI -0.70 to -0.25). This association was stronger among intensive and highly self-disclosing users.
- **Limitation:** The study cannot establish that companion use caused lower well-being. Users selected into the platform and the study; donated chats came from one changing platform and a smaller, technically able subset of the survey sample.
- **Teaching job:** Moves from an AI shaping a message between people to an AI becoming a sustained conversational partner. It also forces students to distinguish observed association from causal influence.
- **Useful slide evidence:** Study overview, usage categories, and the interaction between companionship use, offline social context and well-being.

## Why these three readings belong together

- **Hancock, Naaman and Levy** define the communication arrangement.
- **Williams-Ceci and colleagues** identify a causal effect on the writer in a bounded task.
- **Zhang and colleagues** study sustained use in an actual companion platform but provide associational evidence.

The contrast is methodologically useful. We can make a relatively strong causal claim about a short writing task and only a more cautious claim about longer relationships. The class should not flatten these into a generic conclusion that AI “changes people.”

## Proposed additional readings

### Earlier computer-mediated communication

1. Walther, Joseph B. 1992. “Interpersonal Effects in Computer-Mediated Interaction: A Relational Perspective.” *Communication Research* 19(1): 52–90. https://doi.org/10.1177/009365092019001003.
   - Establishes that text-based computer mediation can support relational communication through different cues and timescales.

### Predictive text and human–human interaction

2. Arnold, Kenneth C., Krysta Chauncey, and Krzysztof Z. Gajos. 2020. “Predictive Text Encourages Predictable Writing.” In *Proceedings of IUI 2020*, 128–138. https://doi.org/10.1145/3377325.3377523.
   - Shows that suggestion systems can narrow wording even without contemporary LLM chat interfaces.

3. Hohenstein, Jess, et al. 2023. “Artificial Intelligence in Communication Impacts Language and Social Relationships.” *Scientific Reports* 13: 5487. https://doi.org/10.1038/s41598-023-30938-9.
   - Two randomized messaging experiments connect smart-reply use to speed, emotional language and perceptions of a conversation partner.

### How LLM suggestions enter expression and judgment

4. Agarwal, Dhruv, Mor Naaman, and Aditya Vashistha. 2025. “AI Suggestions Homogenize Writing Toward Western Styles and Diminish Cultural Nuances.” In *CHI 2025*. https://doi.org/10.1145/3706598.3713564.
   - A cross-cultural experiment showing unequal efficiency gains and movement toward Western writing conventions. Already introduced briefly in Week 2, so it should not become another required reading here.

5. Bhat, Advait, Marianne Aubin Le Quéré, Mor Naaman, and Maurice Jakesch. 2026. “Reactive Writers: How Co-Writing with AI Changes How We Engage with Ideas.” In *CHI 2026*, Article 732, 1–21. https://doi.org/10.1145/3772318.3791529.
   - Nineteen retrospective interviews and traces from 1,291 writing sessions describe an evaluation-first, suggestion-led writing process. This is particularly useful for designing the coding exercise.

### Longer-term companion use

6. Folk, Dunigan, and Elizabeth Dunn. 2026. “How Does Turning to AI for Companionship Predict Loneliness and Vice Versa?” *Psychological Science* 37(4): 276–286. https://doi.org/10.1177/09567976261427747.
   - A four-wave, twelve-month study of 2,149 adults finds evidence that increased chatbot use predicted subsequent emotional isolation, while lower social connection predicted later chatbot use. The analyses are exploratory and do not settle causal direction.

## Papers considered but not proposed for the main list

- **Jakesch et al. (2023):** important predecessor to Williams-Ceci et al., but the 2026 study expands the issues, comparisons and awareness tests. Use it to explain the research sequence, not as another assigned article.
- **Doshi and Hauser (2024):** strong experiment on individual story quality and collective similarity. It fits a class focused on creativity, but would widen this week's argument beyond mediated conversation.
- **Ma, Wang and Wang (2026):** valuable qualitative study of 22 Chinese young adults' “bounded supportive companionship.” It is a useful lecture contrast to population-level well-being measures, but not essential if students already read Zhang et al.
- **Agarwal et al. (2025):** substantively important, but already used in Week 2 and overlaps with the writing-assistant mechanism tested more comprehensively by Williams-Ceci et al.

## Prospective reading-to-code connection

The code exercise should reproduce the research object without pretending to reproduce the published causal estimates:

1. the student writes a short response before seeing model suggestions;
2. the model offers several possible continuations under a visible instruction;
3. the student accepts, edits, rejects or asks for a different suggestion;
4. Python records the suggestion, decision, edit and final text;
5. the student compares the unaided and assisted versions and reflects on what became easier to say, what disappeared, and whether retaining the final click meant retaining authorship or independent judgment.

The exercise would teach a small function, a list of decision records and simple string comparisons. It would not use a model to infer whether the student's attitude changed or whether a relationship improved.

## Source availability

- Hancock, Naaman and Levy: an author-hosted PDF is openly available.
- Williams-Ceci et al.: the final open-access article and materials are available.
- Zhang et al.: the final article is currently restricted on the publisher site. The accepted/preprint version is public, but the published PDF is preferred for screenshots and assigned reading.
- Walther, Arnold et al., Hohenstein et al., Agarwal et al., Bhat et al. and Folk and Dunn all have accessible author or open versions.

**PDF request:** if NYU access permits it, place the final published PDF of Zhang et al. (2026), DOI `10.1038/s41562-026-02516-2`, in `literature/source_pdfs/session10/`. No other publisher PDF is currently needed from the instructor.

## Files that this direction would replace

After approval, the existing Week 10 agent-simulation deck should be replaced rather than edited. Its collective-intelligence question, neighborhood agents and `update_agent(...)` exercise belong to the superseded course sequence. The bare Week 10 course-book and Python pages should then be developed around the communication question above.
