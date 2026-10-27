# Session 9 literature review: LLMs at work

**Prepared:** 27 October 2026
**Scope:** literature and publication status checked through 27 October 2026
**Status:** approval gate 1 approved on 27 October 2026; methodological synthesis and session architecture now in development

## Current course material to replace

The existing Week 9 material is a provisional class on agent-based models, synchronous updating and generative agents. Its readings, slides, workbook and coding task are scaffolding rather than collaboratively reviewed teaching materials. The following are therefore superseded for Week 9 if the direction below is approved:

- Macy and Willer on classical agent-based models;
- Park et al. on generative agents;
- Chuang et al. on LLM opinion dynamics;
- the `synchronous_update` exercise;
- the Observe / Intervene / Simulate course map;
- the question about micro-level interaction producing macro-level order.

The first student-edited function remains the agreed Python milestone for Week 9, but it should be rebuilt around work rather than inherited from the obsolete agent-simulation plan.

## Recommended sociological question

**How does LLM assistance change worker performance, skill and control?**

This question is preferable to a general debate about whether AI will “replace jobs.” It supports comparison among several outcomes that the literature often collapses:

- performing a task more quickly;
- improving the quality of the current output;
- learning something that remains available without the tool;
- changing who exercises discretion;
- redistributing expertise within an occupation;
- changing wages, hours, hiring or staffing;
- moving work elsewhere in the AI production chain.

The question also gives the class a reason to move from the sociology of technology and work to recent LLM field studies. Earlier research already showed that the effects of a technology depend on occupational relations, managerial choices and the organization of work. The contemporary literature lets us ask whether natural-language assistance changes that conclusion.

## Historical and sociological lineage

### 1. Marx: machinery enters a social relation

The historical section should begin with Marx's analysis of machinery and large-scale industry in *Capital*, rather than with a generic story of technological progress. The relevant point is not that machines inevitably replace workers. Machinery is introduced within a capitalist labour process in which employers purchase labour power, organize cooperation and seek greater control over production. It can raise productive capacity while changing the worker's relation to the labour process and strengthening capital's command over it.

This gives the lecture its first question: **what is the technology being used to reorganize, and who controls that reorganization?** For LLMs, this directs attention away from model capability in isolation and towards ownership, task allocation, surveillance, evaluation and the distribution of the gains.

Use an original image of *Capital*, a readable crop from the machinery chapter and, if available, a historical image of machinery inside the factory. Do not present Marx as having predicted LLMs or as offering a simple claim that every technology deskills every worker.

### 2. Braverman: management separates conception from execution

Braverman's *Labor and Monopoly Capital* makes managerial control of knowledge central. Under scientific management, detailed knowledge of production can be taken from workers, codified by management and returned as instructions. His account of the separation of conception from execution supplies a direct question for generative AI at work: does an assistant enlarge workers' discretion, or does it embed a managerial version of good practice in the interface?

This is the right place to introduce Taylorism and time-and-motion documentation. Taylor supplies part of the object Braverman is analysing; he need not become a separate intellectual stop. The lecture should also avoid treating Braverman's deskilling thesis as an uncontested universal law. It leads directly to Burawoy's criticism and extension.

### 3. Burawoy: control also operates through consent

Burawoy's *Manufacturing Consent* shifts attention from managerial design alone to what workers do with the labour process. His shop-floor ethnography shows workers participating in games such as “making out,” through which effort, competition and consent are organized in everyday work. Workers are neither passive recipients of managerial control nor simply free agents outside it.

This adds a question that Braverman's account cannot answer on its own: **why might workers actively use, adapt and value a system that also intensifies work or advances managerial objectives?** Applied to LLMs, it suggests looking at convenience, competence, status, peer comparison and the satisfactions of accomplishing a difficult task—not only formal compulsion.

The visual material should include the original book, photographs or records from the Allied Corporation shop-floor setting where licensing permits, and a short passage explaining “making out.” Avoid reducing Burawoy to the slogan that workers “consent to exploitation”; the organization of the game and the conditions under which participation becomes meaningful are the sociological point.

### 4. Barley: technology does not determine one organizational outcome

Stephen Barley's 1986 comparison of two radiology departments supplies the strongest assigned historical anchor. Both departments introduced the same model of CT scanner. Barley observed approximately 400 examinations, including 96 CT scans, while documenting encounters and participants' interpretations. The scanner disturbed established relations between radiologists and technologists, but the two departments developed different role structures.

This matters because it rejects a simple technology-to-outcome story. Material features matter, but workers enact a technology inside an existing interaction order. The same reasoning applies to LLM deployment: a model licence does not by itself determine whether workers gain discretion, become dependent on recommendations, acquire knowledge, or lose authority.

**Useful evidence for later slides:**

- the published title page;
- Barley's description of the two similar departments and identical scanners;
- the passage on studying how technology enters members' everyday work;
- the original figure comparing operational decisions across phases and hospitals;
- one short passage on “clandestine teaching” between technologists and inexperienced radiologists.

### 5. Zuboff: computerization can automate work and produce information about it

Zuboff's *In the Age of the Smart Machine* follows computerization into workplaces rather than inferring its effects from technical specifications. Her distinction between **automating** and **informating** is useful here. A computerized system can perform or assist a task while also producing new information about the production process, employees and organizational activity. That information can support learning, but it can also make work newly visible to management.

This creates the immediate bridge to contemporary LLM systems. A workplace assistant does not only return text. It may also retain prompts, suggested answers, edits, acceptance decisions, response times and performance outcomes. The question is therefore not simply whether a worker becomes faster. It is also what the organization can now know and govern because the work passes through the system.

Use the original book and evidence from Zuboff's workplace cases. Do not turn “automate/informate” into an unsupported two-box course typology; explain it through one actual workplace process and cite the relevant passage.

### 6. Computerization changed tasks as well as jobs

Autor, Levy and Murnane later formalized a task-based account of computerization, distinguishing routine tasks that computers could codify from nonroutine work that remained comparatively difficult to automate.

This section should remain concise. Its purpose is to establish why generative AI attracted attention: language models can assist with forms of writing, interpretation, coding and analysis that earlier task accounts often classified as nonroutine cognitive work. Exposure is still not adoption, and task capability is not an observed employment effect.

### 7. Algorithms became part of workplace control before LLMs

Rosenblat and Stark's Uber study and Kellogg, Valentine and Christin's review of algorithmic control show how software can recommend actions, record behaviour, rate performance and distribute rewards while preserving informational asymmetries between firms and workers.

Kellogg and colleagues' six mechanisms are useful as a bridge rather than a new course typology: restricting and recommending direct work; recording and rating evaluate it; replacing and rewarding discipline it. LLM assistants often enter through “recommending,” but their suggestions may also feed recording, rating, training and staffing systems.

### 8. AI systems are themselves workplaces

Le Ludec, Cornet and Casilli reconstruct labour outsourced from French AI firms to data workers in Madagascar. Their study shows that annotation and model maintenance require expertise, supervision and repeated negotiation even when the finished service is described as automated. Recent ethnographies of Chinese data-annotation firms extend the same problem.

This prevents the class from treating “AI at work” only as employees using ChatGPT. The model's apparent autonomy depends on a distributed labour process that includes data production, annotation, evaluation, moderation and infrastructure work.

### 9. LLM assistance enters the labour process through language

The Brynjolfsson, Li and Raymond study gives the class its first exact contemporary system. A GPT-3-based assistant monitored customer chats and offered real-time response suggestions and links to internal documentation. Agents could ignore or edit the suggestions. The model was fine-tuned on past conversations and gave extra weight to chats conducted by top performers.

This provides the precise continuity and difference:

- **Continuity:** management collects examples of successful work, turns them into instructions, monitors performance and decides how assistance enters the workflow.
- **Difference:** the procedure can generate situated natural-language advice during a live customer interaction, including for moderately uncommon problems that a particular worker has not encountered often.

The novelty is therefore narrower than “AI changes everything.” The assistant can apply traces of prior workers' practice to new conversational situations at scale, but the organization still chooses the training material, interface, incentives, access and performance measures.

## Recommended required readings

I recommend three complete articles. The third is deliberate rather than an attempt to cover everything: it distinguishes improved assisted performance from retained knowledge, which neither of the first two papers can establish.

### 1. Historical and sociological anchor

**Barley, Stephen R. 1986. “Technology as an Occasion for Structuring: Evidence from Observations of CT Scanners and the Social Order of Radiology Departments.” *Administrative Science Quarterly* 31(1): 78–108. https://doi.org/10.2307/2392767.**

- **Question:** How does the introduction of the same technology become associated with different organizational structures?
- **Material and setting:** Comparative longitudinal observation in the radiology departments of two Massachusetts community hospitals introducing the same model of CT scanner.
- **Method:** Detailed observation of work encounters, scripts and participants' interpretations. The article reports roughly 400 observed examinations, including 96 CT scans.
- **Principal finding:** Similar structuring processes around identical scanners produced divergent role relations and distributions of authority. Existing interaction patterns and local action shaped what the technology became organizationally.
- **Limitations:** Two departments and one historical technology. The study develops a process explanation rather than estimating an average treatment effect.
- **Teaching job:** Establish that technology does not carry one organizational consequence into every workplace. This is the standard against which the recent LLM studies should be read.
- **Evidence to use:** title page; methods passage; the original cross-hospital decision figure; the passage on everyday incorporation; the “clandestine teaching” example.
- **Status:** final published article.

### 2. Contemporary workplace application

**Brynjolfsson, Erik, Danielle Li and Lindsey Raymond. 2025. “Generative AI at Work.” *Quarterly Journal of Economics* 140(2): 889–942. https://doi.org/10.1093/qje/qjae044.**

- **Question:** What happened to productivity, quality, learning and worker experience when customer-support agents received real-time LLM assistance?
- **Material and setting:** 5,172 customer-support agents in one Fortune 500 software firm. Eighty per cent of agents were based in the Philippines. The system used GPT-3, fine-tuned on earlier customer-agent conversations and related outcomes.
- **Design:** The published analysis studies a staggered rollout created by training and capacity constraints. It uses agent and time controls, alternative difference-in-differences estimators and an instrumental-variable robustness strategy. The main study should not be described as a simple randomized trial.
- **Principal finding:** Access increased issues resolved per hour by about 15% on average. Less experienced and lower-skilled agents saw much larger gains, including roughly 30% more resolutions per hour, while the most experienced agents saw little productivity gain and small declines on some quality measures. Treated agents with two months of tenure performed about as well as untreated agents with more than six months. Outage evidence is consistent with some learning, but it is not a direct knowledge test.
- **Limitations:** One firm, one occupation, one medium-run implementation, endogenous adherence and no direct evidence about wages, aggregate employment or long-run staffing. The firm's output and incentive measures define what counts as productivity.
- **Teaching job:** Show an actual LLM routine inside a labour process and make heterogeneity by worker experience central. It also raises the question of whether the tool transfers expertise, standardizes communication or changes whose past work becomes organizational capital.
- **Evidence to use:** the appendix image of the live agent interface; Table II for the average productivity effect; Figure IV for heterogeneity by tenure; Figure V for the experience curve; Figure VII for outages; the passage explaining that top-performer conversations received extra training weight.
- **Status:** final published article.

### 3. Deliberate contemporary contrast

**Wiles, Emma, Lisa Krayer, Mohamed Abbadi, Urvi Awasthi, Ryan Kennedy, Pamela Mishkin, Daniel Sack and François Candelon. 2026. “Generative AI and the Temporary Upskilling of Knowledge Workers.” *Nature Human Behaviour*. https://doi.org/10.1038/s41562-026-02566-6.**

- **Question:** Does performing unfamiliar work with generative AI mean that workers have acquired the underlying skill?
- **Material and setting:** 487 management consultants undertaking data-science tasks outside their existing skill set. The tasks required the combination of human work and ChatGPT; the authors state that ChatGPT could not solve them independently.
- **Design:** Randomized access and training, comparison with a control group, and expert data scientists as a performance benchmark. A subsequent assessment tested technical knowledge without ChatGPT.
- **Principal finding:** Treated consultants performed better than controls on three data-science tasks but remained below expert data scientists. The study found no evidence that treatment improved their ability to answer technical questions without ChatGPT afterward.
- **Limitations:** A bounded experiment with consultants and selected data-science tasks. Performance during assisted tasks and the post-experiment knowledge test do not cover every form of workplace learning. Several authors worked for BCG, and one worked for OpenAI; the paper reports these competing interests.
- **Teaching job:** Separate task expansion or assisted capability from durable learning. It gives the class a direct empirical comparison for claims about upskilling, deskilling and dependence.
- **Evidence to use:** title page; Figure 1 on task performance; Figure 2 on prior coding experience; Figure 3 on the post-experiment knowledge test. Figure 3 is the crucial evidentiary slide.
- **Status:** final peer-reviewed article, published 26 October 2026.

## Proposed additional readings

These readings perform distinct jobs. They should not all receive equal space in the lecture.

### Workplace control before generative AI

**Kellogg, Katherine C., Melissa A. Valentine and Angèle Christin. 2020. “Algorithms at Work: The New Contested Terrain of Control.” *Academy of Management Annals* 14(1): 366–410. https://doi.org/10.5465/annals.2018.0174.**

- **Question and material:** Interdisciplinary review of how algorithmic systems alter organizational control and worker resistance.
- **Finding:** The authors organize algorithmic control around restricting, recommending, recording, rating, replacing and rewarding, while also identifying worker resistance strategies.
- **Teaching job:** Supply the immediate pre-LLM organizational context. It prevents us from treating algorithmic recommendations, monitoring and opacity as inventions of ChatGPT.
- **Status:** final published review article.

### Worker experience beyond productivity metrics

**Oder, Noah and Daniel Béland. 2025. “Artificial Intelligence, Emotional Labor, and the Quest for Sociological and Political Imagination among Low-Skilled Workers.” *Policy and Society* 44(1): 116–128. https://doi.org/10.1093/polsoc/puae034.**

- **Question and material:** Constructivist grounded-theory study using semi-structured interviews in an Austrian call centre.
- **Finding:** Workers described flawed AI tools as adding emotional demands, stress and repair work. The authors argue that immediate workplace pressures limited how most participants connected their experience to wider labour-market and political processes.
- **Limitations:** One qualitative case. The proposed mechanism between emotional labour and political imagination is interpretive and partly hypothetical.
- **Teaching job:** Challenge the assumption that a productivity measure captures the experience or politics of AI-assisted work.
- **Status:** final open-access article. The earlier project memo incorrectly attributed this paper to Berger and colleagues; this review corrects the record.

### Task boundaries and overreliance

**Dell'Acqua, Fabrizio, Edward McFowland III, Ethan R. Mollick, Hila Lifshitz-Assaf, Katherine Kellogg, Saran Rajendran, Lisa Krayer, François Candelon and Karim R. Lakhani. 2026. “Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality.” *Organization Science* 37(2): 403–423. https://doi.org/10.1287/orsc.2025.21838.**

- **Question and material:** Experiment with 758 BCG consultants completing realistic consulting tasks with or without GPT-4.
- **Finding:** For 18 tasks inside the tested capability frontier, AI increased speed by more than 25%, performance by more than 30% and completion by more than 12%. On one task outside the frontier, AI users were 19 percentage points less likely to reach the correct solution.
- **Limitations:** Only one task represented performance outside the frontier; writing-intensive tasks used subjective evaluation rubrics.
- **Teaching job:** Show why “access to AI” is not one stable treatment across tasks and why fluent advice can reduce performance.
- **Status:** final published article.

### Individual time savings and organizational coordination

**Dillon, Eleanor Wiske, Sonia Jaffe, Nicole Immorlica and Christopher T. Stanton. 2025. “Shifting Work Patterns with Generative AI.” NBER Working Paper 33795. https://doi.org/10.3386/w33795.**

- **Question and material:** Six-month randomized field experiment across 66 firms and 7,137 knowledge workers using Microsoft 365 Copilot.
- **Finding:** Workers changed behaviours that they could change individually, especially email time and document completion, but the study did not detect changes in meeting time or the broader composition of tasks. Estimates differ between intention-to-treat effects and effects among frequent users and must not be conflated.
- **Teaching job:** Distinguish individual time savings from organizational change requiring coordination among workers.
- **Status:** working paper. Include it only with that status visible.

### Adoption and labour-market outcomes

**Humlum, Anders and Emilie Vestergaard. 2025. “Large Language Models, Small Labor Market Effects.” Working paper.**

- **Question and material:** Two surveys covering 25,000 workers and 7,000 workplaces in 11 exposed Danish occupations, linked to matched employer-employee records.
- **Finding:** Employer encouragement and training increased adoption, but reported time savings averaged 2.8% of work hours. The study detected no significant effect on earnings or recorded hours and ruled out average effects larger than roughly 1% in its main summary.
- **Limitations:** Early observation window, selected exposed occupations and a Danish labour-market setting. Adoption and observed labour-market outcomes remain distinct.
- **Teaching job:** Prevent extrapolation from task-level experimental gains to wages, hours or employment.
- **Status:** working paper.

### Labour behind the model

**Le Ludec, Clément, Maxime Cornet and Antonio A. Casilli. 2023. “The Problem with Annotation: Human Labour and Outsourcing between France and Madagascar.” *Big Data & Society* 10. https://doi.org/10.1177/20539517231188723.**

- **Question and material:** Interviews with 26 data workers and eight employees of French AI start-ups, alongside research on a canteen checkout system and a shoplifting-detection system.
- **Finding:** AI production relied on an extended subcontracting chain, domain expertise, annotation-guide revision and communication between workers and model developers. The authors argue that apparent automation displaced and externalized labour rather than simply eliminating it.
- **Limitations:** Two production chains and a specific France-Madagascar outsourcing relation. The study predates some recent generative-AI training arrangements.
- **Teaching job:** Extend the unit of analysis from employees using an assistant to the workers who make AI services possible.
- **Evidence to use:** the published production-chain figure and a short passage on annotator expertise.
- **Status:** final open-access article.

## Lecture-only sources and visual material

These sources can support the prehistory and opening without adding to the assigned reading load.

- **Marx, *Capital*, volume 1 (1867), chapter 15, “Machinery and Modern Industry”:** an original edition or reputable complete text, with a short passage showing that Marx's object is the capitalist application of machinery rather than machinery in the abstract. The chapter is too long to add casually to the required list, but it establishes the relation among machinery, surplus value and control of the labour process.
- **Braverman, *Labor and Monopoly Capital: The Degradation of Work in the Twentieth Century* (1974):** original book cover, scientific-management material and a carefully checked passage on separating conception from execution. Use Braverman to develop the deskilling and managerial-control argument, not as a claim that every new technology has the same effect.
- **Burawoy, *Manufacturing Consent: Changes in the Labor Process under Monopoly Capitalism* (1979):** original book image and a passage or diagram explaining the game of “making out.” Burawoy supplies worker agency and consent within the labour process, rather than a second version of Braverman.
- **Zuboff, *In the Age of the Smart Machine: The Future of Work and Power* (1988):** original book image and an empirically grounded example of the distinction between automating work and producing new information about it. This supplies the closest historical bridge to logged LLM assistance.
- **Autor, Levy and Murnane (2003):** the routine/nonroutine task argument as the immediate economic background to claims that generative AI reaches different work.
- **Rosenblat and Stark (2016):** an original interface or driver communication that makes algorithmic information asymmetry concrete.
- **Bick, Blandin, Deming and Schumacher (2026), “What Work Does Generative AI Do?”:** current nationally representative evidence that exposure measures explain only part of adoption and that use is widespread but shallow within most tasks and occupations. This is an NBER working paper and should be labelled accordingly.
- **Cui et al. (2026), “The Effects of Generative AI on High-Skilled Work”:** three randomized trials covering 4,867 developers found a pooled 26.08% increase in completed tasks, with greater adoption and gains among less experienced developers. This is a concise occupational comparison rather than another focal paper.
- **Dell'Acqua et al. (2026), “The Cybernetic Teammate”:** 791 P&G professionals randomized across individual/team and AI/no-AI conditions. Useful only if the lecture needs a short example of AI changing expertise integration; it should not become a detour into agentic systems.

## The empirical disagreement worth carrying into class

The recent literature does not support one general claim about “AI productivity.” It measures different outcomes in different work arrangements:

- Brynjolfsson and colleagues observe higher throughput and faster movement down one firm's experience curve.
- Wiles and colleagues find improved assisted performance without evidence of retained technical knowledge.
- Dell'Acqua and colleagues show positive and negative effects depending on whether a task falls inside the tested capability frontier.
- Dillon and colleagues find that workers changed email and document work more readily than meeting structures requiring coordination.
- Humlum and Vestergaard find widespread adoption but little detectable change in earnings or recorded hours during the observed period.
- Oder and Béland describe additional emotional and repair work that output metrics would miss.
- Le Ludec and colleagues locate further work in the production chain behind the system.

These results can coexist. They refer to different units, outcomes, time horizons, workers, firms and technologies. The class should therefore ask what exactly changed and for whom before describing a workplace as “transformed.”

## What appears continuous and what is plausibly different with LLMs

### Continuities

- Firms still decide which knowledge becomes formalized and whose performance becomes the benchmark.
- New technologies still enter existing occupational hierarchies and interaction orders.
- Productivity measures still reflect organizational priorities rather than a neutral definition of good work.
- Workers still repair technologies and absorb failures that formal evaluations may omit.
- Adoption still depends on training, incentives, discretion, trust and complementary organizational change.
- Automation claims still obscure work moved to contractors, data workers and infrastructure providers.

### Differences that the lecture can defend

- Natural-language interfaces let systems intervene in writing, interpretation, explanation and conversational work without a separately programmed rule for every utterance.
- A single underlying model can be configured across many work tasks, although performance remains uneven and task-specific.
- Suggestions are probabilistic and can be fluent even when incorrect, making capability boundaries difficult for workers to see.
- Firms can convert large archives of earlier worker-customer interaction into situated recommendations during later interactions.
- Workers may receive an answer or recommendation without acquiring the knowledge needed to reproduce it once assistance is removed.
- External model providers and routing infrastructure introduce another organizational actor into questions of data, maintenance, access and control.

These are hypotheses and observed features of particular systems, not proof that LLMs constitute a wholly unprecedented labour regime.

## Initial implication for the cumulative example and Python exercise

The most promising cumulative case is an instructor-authored customer-support setting loosely modeled on the system anatomy in Brynjolfsson, Li and Raymond. Students would see:

1. a customer message;
2. a short internal policy or knowledge-base passage;
3. a worker profile stating experience with this issue;
4. an LLM-generated recommendation;
5. a worker decision to accept, edit or reject it;
6. a later check against the policy and the desired customer outcome.

This would let the first student-edited function take transparent inputs such as the case, assistance mode and route. Before the function is introduced, the same literal values would appear in a direct model call. A small comparison could change one organizational choice, such as full-answer assistance versus a coaching prompt, and inspect the advice returned.

The exercise could demonstrate how an organization configures advice and records interaction. It could not demonstrate that a real novice learned, that productivity increased, or that the advice changed a labour market. Those outcomes require human workers and a research design.

This direction should remain provisional until the readings and cumulative question are approved.

## PDFs and source files

The following published PDFs are already accessible online and can be acquired after approval without asking the instructor to locate substitutes:

- Barley (1986), exact published page images;
- Brynjolfsson, Li and Raymond (2025), publisher version;
- Kellogg, Valentine and Christin (2020), author-hosted published version;
- Oder and Béland (2025), open-access publisher version;
- Dell'Acqua et al. (2026), open-access publisher version;
- Dillon et al. (2025), revised working paper;
- Humlum and Vestergaard (2025), working paper;
- Le Ludec, Cornet and Casilli (2023), open-access publisher PDF.

The publisher PDF of Wiles et al. (2026), “Generative AI and the Temporary Upskilling of Knowledge Workers,” has now been supplied and verified at:

`literature/source_pdfs/session09/wiles_et_al_2026_temporary_upskilling.pdf`

Before slides are drafted, obtain or verify scan-quality source material for Marx, Braverman, Burawoy and Zuboff. Book covers alone will not be used as evidence: any quotation, diagram or empirical claim must be checked against the relevant edition.

If the historical section later uses a direct quotation from Braverman or Zuboff, obtain the relevant book pages before writing the quotation slide. A cover image alone does not require a local book PDF.

## Recommendation at approval gate 1

Approve the following required-reading set:

1. Barley (1986), complete article;
2. Brynjolfsson, Li and Raymond (2025), complete article;
3. Wiles et al. (2026), complete article.

This is a deliberate three-paper week. Barley establishes the organizational sociology. Brynjolfsson provides the workplace LLM case. Wiles makes us distinguish assisted performance from retained skill. Oder and Béland should receive a meaningful lecture section and remain additional reading because the central class already asks students to read approximately 100 pages across the three required papers.

If that load is too high, the least damaging reduction is to move Wiles et al. to the top of the additional list while still teaching Figures 1 and 3. I do not recommend dropping Barley or Brynjolfsson: without Barley, the week loses its sociological standard; without Brynjolfsson, it loses the clearest real workplace LLM implementation.
