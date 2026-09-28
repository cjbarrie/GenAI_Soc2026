"""Build the Week 5 notebook from the reviewed teaching sequence."""

from pathlib import Path

import nbformat as nbf


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "workbook" / "session05" / "session05_treatment_generation.ipynb"


def markdown(text: str):
    return nbf.v4.new_markdown_cell(text.strip())


def code(text: str):
    return nbf.v4.new_code_cell(text.strip())


setup = r'''
SESSION = "session05"

import importlib as setup_importlib
import importlib.util as setup_importlib_util
import os as setup_os
import subprocess as setup_subprocess
import sys as setup_sys
from pathlib import Path as SetupPath

try:
    import google.colab as setup_colab  # type: ignore[import-not-found]
    IN_COLAB = True
except ImportError:
    IN_COLAB = False

course_packages = {
    "openrouter": "openrouter>=0.6,<1",
    "ollama": "ollama>=0.6,<1",
    "plotly": "plotly>=6.3,<7",
    "umap": "umap-learn>=0.5.9,<1",
    "pandas": "pandas>=2.3,<3",
}
missing_packages = [
    package_name
    for package_name in course_packages
    if setup_importlib_util.find_spec(package_name) is None
]

if IN_COLAB:
    if missing_packages:
        setup_subprocess.run(
            [
                setup_sys.executable,
                "-m",
                "pip",
                "install",
                "--quiet",
                "--disable-pip-version-check",
                *[course_packages[name] for name in missing_packages],
            ],
            check=True,
        )
        setup_importlib.invalidate_caches()

    COURSE_ROOT = SetupPath(
        setup_os.getenv("COURSE_COLAB_ROOT", "/content/GenAI_Soc2026")
    )
    if not COURSE_ROOT.exists():
        setup_subprocess.run(
            [
                "git",
                "clone",
                "--depth",
                "1",
                "https://github.com/cjbarrie/GenAI_Soc2026.git",
                str(COURSE_ROOT),
            ],
            check=True,
        )
    setup_os.chdir(COURSE_ROOT / "workbook" / SESSION)
else:
    COURSE_ROOT = SetupPath.cwd()
    while not (COURSE_ROOT / "config" / "course_models.json").exists() and COURSE_ROOT != COURSE_ROOT.parent:
        COURSE_ROOT = COURSE_ROOT.parent
    if missing_packages:
        missing_text = ", ".join(missing_packages)
        raise ModuleNotFoundError(
            f"This notebook is using a Python environment without: {missing_text}.\n\n"
            "Close Jupyter. Open a terminal in the GenAI_Soc2026 repository and run:\n"
            "    uv sync\n"
            "    uv run jupyter lab\n\n"
            "In VS Code, select the Python interpreter inside the repository's .venv folder."
        )
    if not (COURSE_ROOT / "config" / "course_models.json").exists():
        raise FileNotFoundError(
            "The complete GenAI_Soc2026 repository could not be found. A notebook "
            "downloaded by itself is not enough for local work. Download or clone the "
            "repository, open a terminal in that folder, and run: uv run jupyter lab"
        )

course_root_text = str(COURSE_ROOT)
if course_root_text not in setup_sys.path:
    setup_sys.path.insert(0, course_root_text)

still_missing = [
    package_name
    for package_name in course_packages
    if setup_importlib_util.find_spec(package_name) is None
]
if still_missing:
    raise ModuleNotFoundError(
        "Setup did not make these packages available: " + ", ".join(still_missing)
    )

print("Environment:", "Google Colab" if IN_COLAB else "local course environment")
print("Python executable:", setup_sys.executable)
print("Course root:", COURSE_ROOT)
print("Working folder:", SetupPath.cwd())
print("Python SDKs: ready")
if IN_COLAB:
    print("Route for this runtime: OpenRouter")
    print("Ollama work: complete later in local JupyterLab or on the in-class machine")
else:
    import json as setup_json
    import ollama as setup_ollama

    setup_config = setup_json.loads(
        (COURSE_ROOT / "config" / "course_models.json").read_text()
    )
    setup_local_model = setup_config["local"]["model"]
    setup_embedding_model = setup_config["local"]["embedding_model"]
    try:
        setup_models = setup_ollama.list().models
        setup_model_names = [
            getattr(item, "model", None) or getattr(item, "name", None)
            for item in setup_models
        ]
        print("Ollama server: reachable at localhost:11434")
        for setup_label, setup_model in (
            ("Course local model", setup_local_model),
            ("Course embedding model", setup_embedding_model),
        ):
            if setup_model in setup_model_names:
                print(setup_label + ": ready —", setup_model)
            else:
                print(setup_label + ": NOT INSTALLED —", setup_model)
                print("NEXT STEP: open a terminal and run: ollama pull " + setup_model)
    except Exception as setup_error:
        print("Ollama server: NOT REACHABLE")
        print("NEXT STEP: start the Ollama application, then run: ollama list")
        print("Diagnostic:", str(setup_error).splitlines()[0])
'''


imports = r'''
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

config = json.loads((ROOT / "config" / "course_models.json").read_text())
HOSTED_MODEL = config["hosted"]["model"]
HOSTED_EMBEDDING_MODEL = config["hosted"]["embedding_model"]
LOCAL_MODEL = config["local"]["model"]
LOCAL_EMBEDDING_MODEL = config["local"]["embedding_model"]

ROUTE = "openrouter" if IN_COLAB else "ollama"
if ROUTE == "openrouter" and not os.getenv("OPENROUTER_API_KEY"):
    os.environ["OPENROUTER_API_KEY"] = getpass("OpenRouter course key (hidden): ")

print("Route:", ROUTE)
print("Generation model:", HOSTED_MODEL if ROUTE == "openrouter" else LOCAL_MODEL)
'''


design = r'''
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

print(type(research_context), research_context)
print(type(fixed_description), fixed_description)
print(type(fixed_outcome_question), fixed_outcome_question)
print(type(frame_instructions), list(frame_instructions))
print(type(generation_jobs), generation_jobs)
'''


schema = r'''
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
print(json.dumps(batch_schema, indent=2))
'''


generation = r'''
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

Write exactly {messages_per_batch} alternative framing passages for batch {batch_number}. Each passage must:
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

    latency_seconds = round(time.perf_counter() - started, 2)
    raw_generation_records.append({
        "frame": frame,
        "batch": batch_number,
        "prompt": prompt,
        "raw_output": raw_output,
        "latency_seconds": latency_seconds,
    })

    parsed_batch = json.loads(raw_output)
    generated_messages = parsed_batch["messages"]
    if len(generated_messages) != messages_per_batch:
        raise ValueError(
            f"Expected {messages_per_batch} passages for {frame} batch "
            f"{batch_number}; received {len(generated_messages)}"
        )
    print(frame, "batch:", batch_number, "messages:", len(generated_messages), "seconds:", latency_seconds)

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

print("Total treatments:", len(treatment_records))
print("First treatment record:", treatment_records[0])
'''


save_population = r'''
output_folder = ROOT / "outputs" / "session05"
output_folder.mkdir(parents=True, exist_ok=True)
population_path = output_folder / "generated_treatments.json"
population_path.write_text(json.dumps({
    "research_context": research_context,
    "fixed_description": fixed_description,
    "fixed_outcome_question": fixed_outcome_question,
    "frame_instructions": frame_instructions,
    "generation_records": raw_generation_records,
    "treatments": treatment_records,
}, indent=2))
print("Saved:", population_path)
'''


embed = r'''
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

print("Embedding array shape:", embeddings.shape)
'''


project = r'''
projector = umap.UMAP(
    n_neighbors=10,
    min_dist=0.25,
    metric="cosine",
    random_state=42,
)
coordinates = projector.fit_transform(embeddings)
print("UMAP coordinate shape:", coordinates.shape)
print("First coordinate pair:", coordinates[0])
'''


plot = r'''
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

map_path = output_folder / "week05_treatment_map.html"
map_data.to_csv(output_folder / "week05_treatment_map.csv", index=False)
figure.write_html(map_path, include_plotlyjs=True)
print("Saved interactive map:", map_path)
'''


setup_cell = code(setup)
setup_cell["id"] = "colab-setup"

cells = [
    markdown('''
# Week 5 — Map a population of generated treatments

**Research task:** Generate 60 immigration-policy treatments, embed their wording and inspect an interactive two-dimensional semantic map.

**Python introduced:** strings, dictionaries, lists, a `for` loop, structured JSON, arrays, table columns and named arguments.
'''),
    markdown('''
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cjbarrie/GenAI_Soc2026/blob/main/workbook/session05/session05_treatment_generation.ipynb)

Run the setup cell immediately below. Colab uses OpenRouter. Local JupyterLab defaults to Ollama.
'''),
    markdown('''
## Prepare the notebook environment

This cell installs missing packages only in Colab. Locally, it tells you exactly how to enter the pinned course environment. Ollama users need both the generation model and the embedding model named by the cell.
'''),
    setup_cell,
    markdown("## Choose a route and load the model names\n\n**Input:** the course configuration. **Output:** four model-name strings and one route string."),
    code(imports),
    markdown("## Define the research setting and the fixed survey text\n\nThe model writes only the middle framing passage. Python keeps the policy description and outcome question identical across every candidate."),
    code(design),
    markdown("## Specify the structured output\n\nThe schema constrains the returned Python shape. It does not validate whether the messages instantiate the frames well."),
    code(schema),
    markdown("## Generate the framing passages\n\nThe prompt explains what participants will see, identifies the one component the model may write, and lists what must remain unchanged. Six jobs request two batches of ten passages for each frame. Smaller batches make malformed or placeholder output less likely. Python checks every passage before adding the same fixed description and outcome question."),
    code(generation),
    markdown("## Save the prompts, raw returns and cleaned records\n\nThis file is the reproducibility record for the population generated in this run."),
    code(save_population),
    markdown("## Embed all 60 framing passages\n\n**Input:** 60 variable passages. **Output:** a numerical array with one row per passage. We do not embed the repeated description or outcome question."),
    code(embed),
    markdown("## Use UMAP to project the embeddings into two dimensions\n\nThe coordinates support visual inspection. The axes do not have independent substantive meanings."),
    code(project),
    markdown("## Build the interactive map\n\nHover over points to read the underlying treatments. Inspect cross-frame neighbours, within-frame outliers and areas of overlap."),
    code(plot),
    markdown('''
## Completion recording

Set `temperature` to `0.3` before your recorded run. Explain what you expect that change to do, then inspect what the model actually produced. Trace one generation job through the loop, including its frame and batch number. Explain the input and output of the embedding call and how 60 embedding rows become 60 coordinate pairs. Use the hover text to discuss one close cross-frame pair and two separated same-frame treatments. Explain why this is a diagnostic map rather than a validation result.
'''),
]

notebook = nbf.v4.new_notebook(cells=cells)
notebook["metadata"]["kernelspec"] = {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3",
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
nbf.write(notebook, OUTPUT)
print(OUTPUT)
