"""Week 5: generate 60 treatments and inspect an interactive UMAP."""

import json
import os
import sys
import time
from getpass import getpass
from pathlib import Path

import numpy as np
import ollama
import pandas as pd
import plotly.express as px
import umap
from openrouter import OpenRouter

ROOT = Path.cwd()
while not (ROOT / "config" / "course_models.json").exists() and ROOT != ROOT.parent:
    ROOT = ROOT.parent
if not (ROOT / "config" / "course_models.json").exists():
    raise FileNotFoundError(
        "Run this task from the complete GenAI_Soc2026 repository. "
        "See docs/ENVIRONMENT_SETUP.md."
    )

config = json.loads((ROOT / "config" / "course_models.json").read_text())
HOSTED_MODEL = config["hosted"]["model"]
HOSTED_EMBEDDING_MODEL = config["hosted"]["embedding_model"]
LOCAL_MODEL = config["local"]["model"]
LOCAL_EMBEDDING_MODEL = config["local"]["embedding_model"]

ROUTE = "ollama"  # Change to "openrouter" if preferred.
if ROUTE == "openrouter" and not os.getenv("OPENROUTER_API_KEY"):
    os.environ["OPENROUTER_API_KEY"] = getpass("OpenRouter course key (hidden): ")

research_context = (
    "We are constructing candidate materials for an online survey experiment. "
    "Every participant will see a fixed policy description, one variable framing "
    "passage, and then the same outcome question. The model writes only the "
    "middle framing passage."
)
fixed_description = (
    "The proposal would create a pathway to permanent legal status for "
    "undocumented immigrants who meet residency and background-check requirements."
)
fixed_outcome_question = "How strongly do you support or oppose this proposal?"
frame_instructions = {
    "rights": (
        "Contrast the argument that long-term residents possess rights that should not "
        "depend entirely on citizenship with the argument that citizenship should "
        "determine full political membership."
    ),
    "economics": (
        "Contrast the argument that immigrants contribute through work and taxes with "
        "the argument that immigration may create pressure on jobs and public spending."
    ),
    "family": (
        "Contrast the argument that policy should keep families together with the "
        "argument that immigration rules should be enforced even when relatives may "
        "be separated."
    ),
}
messages_per_batch = 10
temperature = 0.9
# ONE CHANGE: set temperature to 0.3 before your recorded run. Explain what
# you expect this parameter change to do, then inspect the actual treatments.

generation_jobs = [
    {"frame": "rights", "batch": 1},
    {"frame": "rights", "batch": 2},
    {"frame": "economics", "batch": 1},
    {"frame": "economics", "batch": 2},
    {"frame": "family", "batch": 1},
    {"frame": "family", "batch": 2},
]

batch_schema = {
    "type": "object",
    "properties": {
        "messages": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": messages_per_batch,
            "maxItems": messages_per_batch,
        }
    },
    "required": ["messages"],
    "additionalProperties": False,
}

treatment_records = []
raw_generation_records = []
for job in generation_jobs:
    frame = job["frame"]
    batch_number = job["batch"]
    frame_instruction = frame_instructions[frame]
    prompt = f"""
{research_context}

Fixed description shown before the framing passage:
{fixed_description}

Fixed question shown after the framing passage:
{fixed_outcome_question}

Assigned {frame.upper()} frame:
{frame_instruction}

Write exactly {messages_per_batch} alternative framing passages. Each passage must:
- contain 30–45 words;
- present both positions in the assigned contest;
- keep the order of the two positions constant;
- use no arguments from either of the other frames;
- introduce no statistics, examples, or new factual claims;
- contain no question;
- make no reference to participants, surveys, framing, or experiments;
- avoid repeating or rewriting the fixed policy description.

Vary the wording and sentence structure without changing the underlying contrast.
Return only the framing passages in JSON matching the supplied schema.
""".strip()
    model_messages = [{"role": "user", "content": prompt}]
    started = time.perf_counter()

    if ROUTE == "openrouter":
        with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
            response = client.chat.send(
                model=HOSTED_MODEL,
                messages=model_messages,
                temperature=temperature,
                max_tokens=5000,
                response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": "treatment_batch",
                        "strict": True,
                        "schema": batch_schema,
                    },
                },
            )
        raw_output = response.choices[0].message.content
    else:
        response = ollama.chat(think=False,
            model=LOCAL_MODEL,
            messages=model_messages,
            format=batch_schema,
            options={"temperature": temperature, "num_predict": 5000},
        )
        raw_output = response.message.content

    raw_generation_records.append({
        "frame": frame,
        "batch": batch_number,
        "prompt": prompt,
        "raw_output": raw_output,
        "latency_seconds": round(time.perf_counter() - started, 2),
    })
    generated_messages = json.loads(raw_output)["messages"]
    if len(generated_messages) != messages_per_batch:
        raise ValueError(
            f"Expected {messages_per_batch} passages for {frame} batch "
            f"{batch_number}; received {len(generated_messages)}"
        )

    for position, text in enumerate(generated_messages, start=1):
        framing_passage = text.strip()
        if len(framing_passage.split()) < 10 or framing_passage.lower().startswith(
            ("framing_passage_", "support_or_oppose_", "family_contrast")
        ):
            raise ValueError(
                f"{frame} batch {batch_number} returned a placeholder instead of a "
                "framing passage. Rerun the generation cell before continuing."
            )
        full_stimulus = (
            fixed_description
            + "\n\n"
            + framing_passage
            + "\n\n"
            + fixed_outcome_question
        )
        treatment_records.append({
            "treatment_id": f"{frame}_b{batch_number}_{position:02d}",
            "frame": frame,
            "batch": batch_number,
            "framing_passage": framing_passage,
            "full_stimulus": full_stimulus,
            "word_count": len(framing_passage.split()),
            "route": ROUTE,
            "model": HOSTED_MODEL if ROUTE == "openrouter" else LOCAL_MODEL,
            "temperature": temperature,
        })

output_folder = ROOT / "outputs" / "session05"
output_folder.mkdir(parents=True, exist_ok=True)
(output_folder / "generated_treatments.json").write_text(json.dumps({
    "research_context": research_context,
    "fixed_description": fixed_description,
    "fixed_outcome_question": fixed_outcome_question,
    "frame_instructions": frame_instructions,
    "generation_records": raw_generation_records,
    "treatments": treatment_records,
}, indent=2))

treatment_texts = [record["framing_passage"] for record in treatment_records]
if ROUTE == "openrouter":
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        embedding_response = client.embeddings.generate(
            model=HOSTED_EMBEDDING_MODEL,
            input=treatment_texts,
            encoding_format="float",
            timeout_ms=120_000,
        )
    embeddings = np.array([item.embedding for item in embedding_response.data])
else:
    embedding_response = ollama.embed(
        model=LOCAL_EMBEDDING_MODEL,
        input=treatment_texts,
    )
    embeddings = np.array(embedding_response.embeddings)

coordinates = umap.UMAP(
    n_neighbors=10,
    min_dist=0.25,
    metric="cosine",
    random_state=42,
).fit_transform(embeddings)

map_data = pd.DataFrame(treatment_records)
map_data["umap_1"] = coordinates[:, 0]
map_data["umap_2"] = coordinates[:, 1]
figure = px.scatter(
    map_data,
    x="umap_1",
    y="umap_2",
    color="frame",
    hover_name="treatment_id",
    hover_data={
        "framing_passage": True,
        "word_count": True,
        "frame": True,
        "umap_1": ":.2f",
        "umap_2": ":.2f",
    },
    title="Semantic map of 60 generated immigration-frame treatments",
)
figure.update_traces(marker={"size": 11, "opacity": 0.78})
figure.update_layout(legend_title_text="Assigned frame")
if "ipykernel" in sys.modules:
    figure.show()
map_data.to_csv(output_folder / "week05_treatment_map.csv", index=False)
figure.write_html(output_folder / "week05_treatment_map.html", include_plotlyjs=True)

print("Treatments:", len(treatment_records))
print("Embedding array:", embeddings.shape)
print("UMAP coordinates:", coordinates.shape)
print("Saved outputs in:", output_folder)
