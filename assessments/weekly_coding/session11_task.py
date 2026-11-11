"""Week 11: prepare a small study of judgments of AI-assisted reports.

New Python: a nested loop that creates a 2-by-2 condition grid.

Run with a local Ollama model after ``uv sync --frozen``. For the supplied
instructor-written example during an outage, set ``COURSE_USE_RECORDED=1``.
That example is labelled as such; it is not a recorded model response.
"""

# CELL: Load tools and select the model route
import json
import os
from getpass import getpass
from pathlib import Path

try:
    import ollama
    from openrouter import OpenRouter
except ModuleNotFoundError:
    ollama = None
    OpenRouter = None

ROOT = Path.cwd()
while not (ROOT / "config" / "course_models.json").exists() and ROOT != ROOT.parent:
    ROOT = ROOT.parent
if not (ROOT / "config" / "course_models.json").exists():
    raise FileNotFoundError(
        "Open a terminal in the complete GenAI_Soc2026 folder, then run this file."
    )

config = json.loads((ROOT / "config" / "course_models.json").read_text())
OPENROUTER_MODEL = config["hosted"]["model"]
OLLAMA_MODEL = config["local"]["model"]
HOSTED_MODEL = OPENROUTER_MODEL
LOCAL_MODEL = OLLAMA_MODEL
USE_EXAMPLE = os.getenv("COURSE_USE_RECORDED", "0") == "1"
ROUTE = "ollama"  # In Colab, use "openrouter".

# CELL: Store the fictional source and the editing instruction
SOURCE_PARAGRAPH = (
    "RivalCo launched a monthly subscription in April at $18. "
    "Our comparable plan costs $20. RivalCo advertises a free trial. "
    "We do not yet have data on customer switching after the launch."
)

EDITING_INSTRUCTION = (
    "Edit this short competitor report for clarity. Preserve every stated fact "
    "and the uncertainty about customer switching. Do not infer a market effect, "
    "invent data, or add a recommendation. Return only the revised report."
)

# This passage is an instructor-written fallback for an outage, not a model result.
EXAMPLE_REVISION = (
    "RivalCo launched an $18 monthly subscription in April. Our comparable "
    "$20 plan costs $2 more. RivalCo advertises a free trial. We do not yet "
    "have data on whether customers switched after the launch."
)

print("Source paragraph:", SOURCE_PARAGRAPH)
print("Python type:", type(SOURCE_PARAGRAPH))
print("Editing instruction:", EDITING_INSTRUCTION)

# CELL: Send one explicit editing request
def edit_paragraph(source_text, instruction, route):
    """Return the revision and preserve the exact text sent and received."""
    separator = "\n\nOriginal paragraph:\n"
    prompt = instruction + separator + source_text
    messages = [{"role": "user", "content": prompt}]
    print("Messages sent to the model:", messages)

    if USE_EXAMPLE:
        raw_text = EXAMPLE_REVISION
        model_name = "instructor-written outage example"
        used_route = "example"
    elif route == "openrouter":
        if OpenRouter is None:
            raise ModuleNotFoundError("Run 'uv sync --frozen' before using OpenRouter.")
        api_key = os.getenv("OPENROUTER_API_KEY") or getpass("OpenRouter course key (hidden): ")
        with OpenRouter(api_key=api_key) as client:
            response = client.chat.send(
                model=OPENROUTER_MODEL,
                messages=messages,
                temperature=0,
            )
        raw_text = response.choices[0].message.content
        model_name = OPENROUTER_MODEL
        used_route = route
    elif route == "ollama":
        if ollama is None:
            raise ModuleNotFoundError("Run 'uv sync --frozen' before using Ollama.")
        response = ollama.chat(think=False,
            model=OLLAMA_MODEL,
            messages=messages,
            options={"temperature": 0},
        )
        raw_text = response.message.content
        model_name = OLLAMA_MODEL
        used_route = route
    else:
        raise ValueError("route must be 'openrouter' or 'ollama'")

    if not isinstance(raw_text, str) or not raw_text.strip():
        raise ValueError("The model returned no usable text. Inspect the raw response.")
    print("Raw return:", raw_text)
    print("Return type:", type(raw_text))
    return {
        "source": source_text,
        "instruction": instruction,
        "messages": messages,
        "raw_return": raw_text,
        "route": used_route,
        "model": model_name,
    }

editing_record = edit_paragraph(SOURCE_PARAGRAPH, EDITING_INSTRUCTION, ROUTE)
REVISED_PARAGRAPH = editing_record["raw_return"].strip()

# CELL: Compare the revision with the original before using it
print("ORIGINAL:\n", SOURCE_PARAGRAPH)
print("REVISION:\n", REVISED_PARAGRAPH)
print("Check these facts yourself: April launch; $18 rival plan; $20 comparable plan;")
print("free trial; no customer-switching data yet.")
print("Reject any new claim about switching or market effects.")

# CELL: Build four hypothetical evaluation conditions
ROLE_CUES = [
    "The report author is the senior director of strategy.",
    "The report author is a junior market analyst.",
]
AI_USE_LABELS = [
    "The description gives no information about AI writing assistance.",
    "The author reports using ChatGPT to edit the report for clarity.",
]

conditions = []
for role_cue in ROLE_CUES:
    for ai_use_label in AI_USE_LABELS:
        condition = {
            "condition_id": len(conditions) + 1,
            "role_cue": role_cue,
            "ai_use_label": ai_use_label,
            "report_text": REVISED_PARAGRAPH,
        }
        conditions.append(condition)
        print("Added condition:", condition["condition_id"])
        print("  role cue:", role_cue)
        print("  AI-use label:", ai_use_label)

# CELL: Inspect the materials and perform software checks
for condition in conditions:
    print("\nCONDITION", condition["condition_id"])
    print(condition["role_cue"])
    print(condition["ai_use_label"])
    print(condition["report_text"])

assert len(conditions) == 4
assert len({item["condition_id"] for item in conditions}) == 4
assert all(item["report_text"] == REVISED_PARAGRAPH for item in conditions)
print("Four conditions exist, and every condition contains the same report.")
print("These checks do not show how a human reader would judge either worker.")

# ONE CHANGE: make the editing instruction more conservative, rerun, and inspect
# whether the revision changes. Keep the fictional source report fixed.
