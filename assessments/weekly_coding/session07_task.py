"""Week 7: compare forced choice and probability outputs for two personas.

Run from the repository root with:
    uv run python assessments/weekly_coding/session07_task.py
"""

# CELL: Load the course settings and SDKs
import json
import os
from getpass import getpass
from pathlib import Path

import matplotlib.pyplot as plt
import ollama
from openrouter import OpenRouter

ROOT = Path.cwd()
while not (ROOT / "config" / "course_models.json").exists() and ROOT != ROOT.parent:
    ROOT = ROOT.parent

if not (ROOT / "config" / "course_models.json").exists():
    raise FileNotFoundError(
        "Run this file from the complete GenAI_Soc2026 repository. "
        "The course configuration could not be found."
    )

config = json.loads((ROOT / "config" / "course_models.json").read_text())
HOSTED_MODEL = config["hosted"]["model"]
LOCAL_MODEL = config["local"]["model"]

ROUTE = "ollama"  # change to "openrouter" if preferred
if ROUTE == "openrouter" and not os.getenv("OPENROUTER_API_KEY"):
    os.environ["OPENROUTER_API_KEY"] = getpass("OpenRouter course key (hidden): ")

print("Route:", ROUTE)
print("Model:", HOSTED_MODEL if ROUTE == "openrouter" else LOCAL_MODEL)

# CELL: Store one question and two persona dictionaries
question = (
    "Where would you place yourself from 1 (extremely liberal) "
    "to 7 (extremely conservative)?"
)
sparse_persona = {
    "age_group": "30–44",
    "education": "bachelor's degree",
    "region": "South",
    "party_identification": "independent",
}
rich_persona = sparse_persona | {
    "economic_view": "government should reduce inequality",
    "social_view": "often supports traditional social norms",
}
held_out_human_answer = 4

print("Question:", question)
print("Sparse persona:", sparse_persona)
print("Richer persona:", rich_persona)

# CELL: Define one forced-choice schema and one probability schema
forced_schema = {
    "type": "object",
    "properties": {
        "category": {"type": "integer", "minimum": 1, "maximum": 7}
    },
    "required": ["category"],
    "additionalProperties": False,
}
distribution_schema = {
    "type": "object",
    "properties": {
        "probabilities": {
            "type": "array",
            "items": {"type": "number", "minimum": 0, "maximum": 1},
            "minItems": 7,
            "maxItems": 7,
        }
    },
    "required": ["probabilities"],
    "additionalProperties": False,
}

# CELL: Build the three prompts
forced_prompt = f"""
Predict this person's answer to the survey item.
Return one category from 1 to 7.

PERSONA: {json.dumps(sparse_persona)}
QUESTION: {question}
"""
sparse_distribution_prompt = f"""
Predict this person's answer to the survey item.
Return seven probabilities in scale order from 1 to 7. They must sum to 1.

PERSONA: {json.dumps(sparse_persona)}
QUESTION: {question}
"""
rich_distribution_prompt = f"""
Predict this person's answer to the survey item.
Return seven probabilities in scale order from 1 to 7. They must sum to 1.

PERSONA: {json.dumps(rich_persona)}
QUESTION: {question}
"""

print(forced_prompt)
print(sparse_distribution_prompt)
print(rich_distribution_prompt)

# CELL: Condition A - sparse persona with a forced answer
forced_messages = [{"role": "user", "content": forced_prompt}]
if ROUTE == "openrouter":
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        forced_response = client.chat.send(
            model=HOSTED_MODEL,
            messages=forced_messages,
            temperature=0,
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "forced_answer",
                    "strict": True,
                    "schema": forced_schema,
                },
            },
        )
    raw_forced = forced_response.choices[0].message.content
else:
    forced_response = ollama.chat(
        model=LOCAL_MODEL,
        messages=forced_messages,
        format=forced_schema,
        options={"temperature": 0},
    )
    raw_forced = forced_response.message.content
print("Raw forced-answer JSON:", raw_forced)

# CELL: Condition B - sparse persona with seven probabilities
sparse_messages = [{"role": "user", "content": sparse_distribution_prompt}]
if ROUTE == "openrouter":
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        sparse_response = client.chat.send(
            model=HOSTED_MODEL,
            messages=sparse_messages,
            temperature=0,
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "sparse_distribution",
                    "strict": True,
                    "schema": distribution_schema,
                },
            },
        )
    raw_sparse = sparse_response.choices[0].message.content
else:
    sparse_response = ollama.chat(
        model=LOCAL_MODEL,
        messages=sparse_messages,
        format=distribution_schema,
        options={"temperature": 0},
    )
    raw_sparse = sparse_response.message.content
print("Raw sparse-persona JSON:", raw_sparse)

# CELL: Condition C - richer persona with seven probabilities
rich_messages = [{"role": "user", "content": rich_distribution_prompt}]
if ROUTE == "openrouter":
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        rich_response = client.chat.send(
            model=HOSTED_MODEL,
            messages=rich_messages,
            temperature=0,
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "rich_distribution",
                    "strict": True,
                    "schema": distribution_schema,
                },
            },
        )
    raw_rich = rich_response.choices[0].message.content
else:
    rich_response = ollama.chat(
        model=LOCAL_MODEL,
        messages=rich_messages,
        format=distribution_schema,
        options={"temperature": 0},
    )
    raw_rich = rich_response.message.content
print("Raw rich-persona JSON:", raw_rich)

# CELL: Convert the three JSON strings into Python objects
forced_result = json.loads(raw_forced)
sparse_result = json.loads(raw_sparse)
rich_result = json.loads(raw_rich)

forced_category = forced_result["category"]
sparse_probabilities = sparse_result["probabilities"]
rich_probabilities = rich_result["probabilities"]

print("Forced category:", forced_category)
print("Sparse probabilities:", sparse_probabilities)
print("Rich probabilities:", rich_probabilities)

# CELL: Check the lists and calculate expected scores
print("Sparse list has seven values:", len(sparse_probabilities) == 7)
print("Rich list has seven values:", len(rich_probabilities) == 7)
print("Sparse sum:", sum(sparse_probabilities))
print("Rich sum:", sum(rich_probabilities))

sparse_expected_score = (
    sparse_probabilities[0] * 1 + sparse_probabilities[1] * 2
    + sparse_probabilities[2] * 3 + sparse_probabilities[3] * 4
    + sparse_probabilities[4] * 5 + sparse_probabilities[5] * 6
    + sparse_probabilities[6] * 7
)
rich_expected_score = (
    rich_probabilities[0] * 1 + rich_probabilities[1] * 2
    + rich_probabilities[2] * 3 + rich_probabilities[3] * 4
    + rich_probabilities[4] * 5 + rich_probabilities[5] * 6
    + rich_probabilities[6] * 7
)

print("Sparse expected score:", sparse_expected_score)
print("Rich expected score:", rich_expected_score)

# CELL: Plot both probability distributions
scale = [1, 2, 3, 4, 5, 6, 7]
plt.plot(scale, sparse_probabilities, marker="o", label="sparse persona")
plt.plot(scale, rich_probabilities, marker="o", label="richer persona")
plt.axvline(held_out_human_answer, color="black", linestyle="--", label="held-out answer")
plt.xlabel("Political views category")
plt.ylabel("Model-assigned probability")
plt.xticks(scale)
plt.legend()
plt.show()

# CELL: Compare the forced answer with the held-out answer
exact_match = forced_category == held_out_human_answer
print("Forced model answer:", forced_category)
print("Held-out human answer:", held_out_human_answer)
print("Exact match:", exact_match)

# ONE CHANGE: edit one value in rich_persona, rebuild rich_distribution_prompt,
# rerun only Condition C, and recreate the plot. Explain every changed input and output.
