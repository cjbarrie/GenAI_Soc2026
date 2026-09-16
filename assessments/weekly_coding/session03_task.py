"""Week 3: a three-round researcher–model exchange about mutual aid."""

# CELL: Read course settings and installed SDKs
import json
import os
from getpass import getpass
from pathlib import Path

try:
    import ollama
    from openrouter import OpenRouter
except ModuleNotFoundError as error:
    raise ModuleNotFoundError(
        "A course SDK is missing. In the complete GenAI_Soc2026 folder, "
        "run 'uv sync --frozen' and then 'uv run python "
        "assessments/weekly_coding/session03_task.py'."
    ) from error

ROOT = Path.cwd()
while not (ROOT / "config" / "course_models.json").exists() and ROOT != ROOT.parent:
    ROOT = ROOT.parent
if not (ROOT / "config" / "course_models.json").exists():
    raise FileNotFoundError(
        "Run this script from the complete GenAI_Soc2026 repository. "
        "A downloaded script alone does not include the course configuration."
    )

config = json.loads((ROOT / "config" / "course_models.json").read_text())
HOSTED_MODEL = config["hosted"]["model"]
LOCAL_MODEL = config["local"]["model"]
print("Hosted model:", HOSTED_MODEL)
print("Local model:", LOCAL_MODEL)

# CELL: Choose a route and inspect eight instructor-authored excerpts
ROUTE = "ollama"  # change to "openrouter" to use the hosted route
if ROUTE == "openrouter" and not os.getenv("OPENROUTER_API_KEY"):
    os.environ["OPENROUTER_API_KEY"] = getpass("OpenRouter course key (hidden): ")

research_question = (
    "When, if at all, does mutual aid among tenants contribute "
    "to political solidarity?"
)
excerpts = [
    {
        "id": "T01_A",
        "text": "When the rent went up, grocery deliveries got us through the last week of the month. At that point I did not know who organized them.",
    },
    {
        "id": "T01_B",
        "text": "After a few months of taking turns with childcare, I started going to the tenants' meetings. The first time I spoke was about the broken elevator.",
    },
    {
        "id": "T02_A",
        "text": "I was grateful for the emergency fund, but I kept it separate from politics. I did not attend meetings and I still do not think of myself as an organizer.",
    },
    {
        "id": "T03_A",
        "text": "Once the delivery rota became a requirement, it stopped feeling like help. I missed two shifts, people kept messaging me, and I left the group.",
    },
    {
        "id": "T04_A",
        "text": "Fixing things together meant we already trusted one another when the eviction notices arrived. Six of us wrote the petition and delivered it together.",
    },
    {
        "id": "T05_A",
        "text": "The organizers call it solidarity. For me it was mostly a way to make it to payday. I did not want a political identity attached to it.",
    },
    {
        "id": "T06_A",
        "text": "I learned people's names and felt less alone. I would not say it made me political, but I was more willing to ask what others needed.",
        "context": "An AI-moderated follow-up asked whether deliveries changed relationships.",
    },
    {
        "id": "T07_A",
        "text": "The food deliveries ended for me, but the meetings were where we compared what the landlord had told each floor. I stayed because acting separately was not working.",
    },
]
print("Research question:", research_question)
for excerpt in excerpts:
    print(excerpt["id"], "—", excerpt["text"])
print("T06_A interviewer context:", excerpts[6]["context"])

# CELL: State your interpretation before asking the model
print("Example first memo: Help may build relationships, but receiving aid alone is not collective action.")
first_memo = input("Your one-sentence first reading: ")
print("Saved before the model:", first_memo)

# CELL: Send the first request and inspect the raw return
prompt_1 = (
    "Research question: " + research_question + "\n"
    "For this exercise, political solidarity means tenants identifying a shared "
    "problem and acting together; receiving aid alone does not establish it. "
    "Suggest one provisional pattern and cite one supplied excerpt ID. "
    "Return a JSON object with exactly theme, evidence_id, and "
    "question_for_researcher. These are synthetic interview excerpts: "
    + json.dumps(excerpts)
)
messages_1 = [{"role": "user", "content": prompt_1}]
print("Round 1 sends", len(excerpts), "labelled excerpts in one user message.")
if ROUTE == "openrouter":
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        response_1 = client.chat.send(
            model=HOSTED_MODEL,
            messages=messages_1,
            temperature=0,
            max_tokens=250,
            response_format={"type": "json_object"},
        )
    raw_1 = response_1.choices[0].message.content
else:
    response_1 = ollama.chat(think=False,
        model=LOCAL_MODEL,
        messages=messages_1,
        format="json",
        options={"temperature": 0, "num_predict": 250},
    )
    raw_1 = response_1.message.content
print("Round 1 raw output:", raw_1)

# CELL: Parse the first proposal and return to its source
proposal_1 = json.loads(raw_1)
print("Round 1 fields:", list(proposal_1))
print("Round 1 theme:", proposal_1.get("theme"))
print("Round 1 cited ID:", proposal_1.get("evidence_id"))
cited_1 = None
for excerpt in excerpts:
    if excerpt["id"] == proposal_1.get("evidence_id"):
        cited_1 = excerpt
print("Round 1 cited passage:", cited_1)
print("Round 1 model question:", proposal_1.get("question_for_researcher"))
print("Your earlier memo:", first_memo)
print("Compare T02_A, T03_A and T05_A before accepting a general claim.")

# CELL: Reply to the model with a countercase
print(
    "Example reply: T02_A accepted help but rejected political involvement; "
    "T03_A left when help became obligatory. How does your theme handle both?"
)
feedback_1 = input("Your reply to the model, naming at least one excerpt ID: ")
messages_2 = messages_1 + [
    {"role": "assistant", "content": raw_1},
    {
        "role": "user",
        "content": (
            feedback_1
            + " Reconsider your theme using the supplied excerpts. Do not simply "
            "agree with me; explain any evidence that resists my challenge. "
            "Return JSON with exactly theme, evidence_id, and "
            "question_for_researcher."
        ),
    },
]
print("Round 2 new researcher input:", feedback_1)
if ROUTE == "openrouter":
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        response_2 = client.chat.send(
            model=HOSTED_MODEL,
            messages=messages_2,
            temperature=0,
            max_tokens=250,
            response_format={"type": "json_object"},
        )
    raw_2 = response_2.choices[0].message.content
else:
    response_2 = ollama.chat(think=False,
        model=LOCAL_MODEL,
        messages=messages_2,
        format="json",
        options={"temperature": 0, "num_predict": 250},
    )
    raw_2 = response_2.message.content
print("Round 2 raw output:", raw_2)
proposal_2 = json.loads(raw_2)
print("Round 2 theme:", proposal_2.get("theme"))
cited_2 = None
for excerpt in excerpts:
    if excerpt["id"] == proposal_2.get("evidence_id"):
        cited_2 = excerpt
print("Round 2 cited passage:", cited_2)
print("Round 2 model question:", proposal_2.get("question_for_researcher"))

# CELL: Press on the proposed mechanism and evidence
print(
    "Example reply: T04_A mentions trust and a petition. What is observed, "
    "and what is only an interpretation about why tenants acted together?"
)
feedback_2 = input("Your second reply, naming an excerpt and a remaining question: ")
messages_3 = messages_2 + [
    {"role": "assistant", "content": raw_2},
    {
        "role": "user",
        "content": (
            feedback_2
            + " Distinguish reported events from an inferred mechanism. "
            "Do not claim these few interviews establish a causal effect. "
            "Keep the theme about mutual aid and solidarity; put remaining "
            "methodological uncertainty in question_for_researcher. "
            "Return JSON with exactly theme, evidence_id, and "
            "question_for_researcher."
        ),
    },
]
print("Round 3 new researcher input:", feedback_2)
if ROUTE == "openrouter":
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        response_3 = client.chat.send(
            model=HOSTED_MODEL,
            messages=messages_3,
            temperature=0,
            max_tokens=250,
            response_format={"type": "json_object"},
        )
    raw_3 = response_3.choices[0].message.content
else:
    response_3 = ollama.chat(think=False,
        model=LOCAL_MODEL,
        messages=messages_3,
        format="json",
        options={"temperature": 0, "num_predict": 250},
    )
    raw_3 = response_3.message.content
print("Round 3 raw output:", raw_3)
proposal_3 = json.loads(raw_3)
print("Round 3 theme:", proposal_3.get("theme"))
cited_3 = None
for excerpt in excerpts:
    if excerpt["id"] == proposal_3.get("evidence_id"):
        cited_3 = excerpt
print("Round 3 cited passage:", cited_3)
print("Round 3 model question:", proposal_3.get("question_for_researcher"))

# CELL: Make and save your own provisional judgment
print("The model's three themes:", proposal_1.get("theme"), "|", proposal_2.get("theme"), "|", proposal_3.get("theme"))
print("Your independent first memo:", first_memo)
final_memo = input(
    "Your provisional answer to the research question, with a countercase and limit: "
)
if ROUTE == "openrouter":
    selected_model = HOSTED_MODEL
else:
    selected_model = LOCAL_MODEL
analysis_record = {
    "research_question": research_question,
    "first_memo": first_memo,
    "route": ROUTE,
    "model": selected_model,
    "excerpts": excerpts,
    "round_1": {"messages": messages_1, "raw": raw_1, "proposal": proposal_1, "cited": cited_1},
    "round_2": {"feedback": feedback_1, "messages": messages_2, "raw": raw_2, "proposal": proposal_2, "cited": cited_2},
    "round_3": {"feedback": feedback_2, "messages": messages_3, "raw": raw_3, "proposal": proposal_3, "cited": cited_3},
    "final_memo": final_memo,
}
print("Final researcher memo:", analysis_record["final_memo"])
print("Saved rounds:", list(analysis_record))
