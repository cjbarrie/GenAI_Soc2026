"""Assessed dual-route routine. Run from the repository root."""

# CELL: Load the course settings and SDKs
import json
import os
from getpass import getpass
from pathlib import Path

try:
    import ollama
    from openrouter import OpenRouter
except ModuleNotFoundError as error:
    raise ModuleNotFoundError(
        "A course SDK is missing. Open a terminal in the complete GenAI_Soc2026 "
        "folder, run 'uv sync --frozen', then run this task with 'uv run python'."
    ) from error

ROOT = Path.cwd()
while not (ROOT / "config" / "course_models.json").exists() and ROOT != ROOT.parent:
    ROOT = ROOT.parent

if not (ROOT / "config" / "course_models.json").exists():
    raise FileNotFoundError(
        "The complete GenAI_Soc2026 repository could not be found. A task or "
        "notebook downloaded by itself is not enough for local work. Open a terminal "
        "in the complete course folder and run this file from there."
    )

config = json.loads((ROOT / "config" / "course_models.json").read_text())
HOSTED_MODEL = config["hosted"]["model"]
LOCAL_MODEL = config["local"]["model"]

print("Hosted model:", HOSTED_MODEL)
print("Local model:", LOCAL_MODEL)

# CELL: Choose one route and store four identified excerpts
ROUTE = "ollama"  # change to "openrouter" if preferred
if ROUTE == "openrouter" and not os.getenv("OPENROUTER_API_KEY"):
    os.environ["OPENROUTER_API_KEY"] = getpass("OpenRouter course key (hidden): ")
excerpts = [
    {"id": "T01_A", "text": "The grocery deliveries helped. At first I did not know who organized them."},
    {"id": "T01_B", "text": "Months later I helped with childcare and joined the tenants' meeting."},
    {"id": "T02_A", "text": "I accepted help but kept it separate from politics. I never attended meetings."},
    {"id": "T03_A", "text": "When the delivery rota became an obligation, I left the group."},
]
print("Route:", ROUTE)
print("First encounter:", excerpts[0])
print("Later account from the same tenant:", excerpts[1])
print("Contrasting accounts:", excerpts[2], excerpts[3])

# CELL: Save your reading before the model suggests one
first_memo = "Practical help sometimes led to meetings, but not for everyone."
print("My first reading:", first_memo)

# CELL: Convert the excerpts into prompt text and construct messages
prompt = (
    "Research question: How do tenants distinguish emergency help from political solidarity? "
    "Suggest one provisional theme. Cite one excerpt ID that supports it. "
    "Return JSON with exactly theme, evidence_id, and question_for_researcher. "
    "Do not treat a theme as a finding. Excerpts: " + json.dumps(excerpts)
)
messages = [{"role": "user", "content": prompt}]
print(prompt)

# CELL: Make the selected route's call without hiding either branch
if ROUTE == "openrouter":
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        response = client.chat.send(
            model=HOSTED_MODEL,
            messages=messages,
            temperature=0,
            response_format={"type": "json_object"},
        )
    raw_output = response.choices[0].message.content
else:
    response = ollama.chat(think=False,
        model=LOCAL_MODEL,
        messages=messages,
        format="json",
        options={"temperature": 0},
    )
    raw_output = response.message.content

print("Raw JSON text:", raw_output)

# CELL: Parse the JSON string and return to its cited source
suggestion = json.loads(raw_output)
evidence_id = suggestion["evidence_id"]
cited_excerpt = None
for excerpt in excerpts:
    if excerpt["id"] == evidence_id:
        cited_excerpt = excerpt

print("Theme:", suggestion["theme"])
print("Cited excerpt:", cited_excerpt)
print("Question:", suggestion["question_for_researcher"])

# CELL: Compare the model suggestion with contrasting cases
countercase_one = excerpts[2]
countercase_two = excerpts[3]
print("The model suggested:", suggestion["theme"])
print("I wrote before the call:", first_memo)
print("Does the cited ID exist?", cited_excerpt is not None)
print("Contrasting case 1:", countercase_one)
print("Contrasting case 2:", countercase_two)

# CELL: Record a reasoned researcher revision
revised_claim = (
    "Repeated exchanges sometimes led to meeting participation, "
    "but receiving help did not always produce political involvement."
)
researcher_reason = (
    "T01_B follows repeated contact; T02_A separates help from politics; "
    "T03_A describes withdrawal when help felt obligatory."
)
analysis_record = {
    "first_memo": first_memo,
    "route": ROUTE,
    "model_request": prompt,
    "raw_model_output": raw_output,
    "model_suggestion": suggestion,
    "cited_excerpt": cited_excerpt,
    "countercase_ids": ["T02_A", "T03_A"],
    "revised_claim": revised_claim,
    "researcher_reason": researcher_reason,
}
print("Revised claim:", analysis_record["revised_claim"])
print("Why it changed:", analysis_record["researcher_reason"])

# ONE CHANGE: change T02_A to
# "The food deliveries helped, but I avoided the group because meetings felt hostile."
# Rerun from the prompt cell and decide whether your revised claim needs to change.
