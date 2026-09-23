"""Week 4: describe and check an ordered protest sequence.

Run from the repository root with:
    uv run python assessments/weekly_coding/session04_task.py
"""

# CELL: Load the course settings and choose a route
import json
import os
import sys
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

script_root = Path(__file__).resolve().parents[2]
required_images = ROOT / "slides" / "session04" / "images"
if not (ROOT / "config" / "course_models.json").exists() or not required_images.exists():
    if (script_root / "config" / "course_models.json").exists():
        ROOT = script_root
    else:
        raise FileNotFoundError(
            "The complete GenAI_Soc2026 repository could not be found. A task "
            "downloaded by itself is not enough. Use the course repository or "
            "the Week 4 offline bundle."
        )

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.genai_soc.media import image_to_data_url

config = json.loads((ROOT / "config" / "course_models.json").read_text())
HOSTED_MODEL = config["hosted"]["model"]
LOCAL_MODEL = config["local"]["model"]
ROUTE = "ollama"  # change to "openrouter" to use the hosted route

if ROUTE == "openrouter" and not os.getenv("OPENROUTER_API_KEY"):
    os.environ["OPENROUTER_API_KEY"] = getpass("OpenRouter course key (hidden): ")

print("Route:", ROUTE)
print("Hosted model:", HOSTED_MODEL)
print("Local model:", LOCAL_MODEL)

# CELL: Store four ordered frames
IMAGE_DIR = ROOT / "slides" / "session04" / "images"
frame_1 = IMAGE_DIR / "uttarakhand_frame_1_04.5s.png"
frame_2 = IMAGE_DIR / "uttarakhand_frame_2_05.0s.png"
frame_3 = IMAGE_DIR / "uttarakhand_frame_3_06.0s.png"
frame_4 = IMAGE_DIR / "uttarakhand_frame_4_08.5s.png"
frames = [frame_1, frame_2, frame_3, frame_4]

print("frames is a", type(frames))
print("frame_1 is a", type(frame_1))
files_exist = (
    frame_1.exists()
    and frame_2.exists()
    and frame_3.exists()
    and frame_4.exists()
)
print("All four files exist:", files_exist)
print("Frame 1:", frame_1)
print("Frame 2:", frame_2)
print("Frame 3:", frame_3)
print("Frame 4:", frame_4)

if not files_exist:
    raise FileNotFoundError(
        "One or more protest frames are missing. Run this task from the complete "
        "course repository or use the Week 4 offline bundle."
    )

# CELL: Record the source and its limits
source_record = {
    "case": "Uttarakhand protest confrontation",
    "creator": "Himalayanwarrior",
    "source": "Wikimedia Commons",
    "license": "CC BY-SA 4.0",
    "timestamps_seconds": [4.5, 5.0, 6.0, 8.5],
    "audio_used": False,
    "capture_limit": "Four selected stills from an 18-second video",
}

print(source_record)
print("source_record is a", type(source_record))
print("audio_used is a", type(source_record["audio_used"]))

# CELL: State the observational task and structured return
prompt = """
Examine these protest images in their supplied order.

Give one observation for each frame. Then describe visible changes in distance,
body orientation, gesture, physical contact and intervention by other people.

Do not infer motive, emotion, speech, political identity or responsibility.
State what these selected frames cannot establish.
"""

schema = {
    "type": "object",
    "properties": {
        "frame_observations": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 4,
            "maxItems": 4,
        },
        "visible_changes": {"type": "array", "items": {"type": "string"}},
        "physical_contact_visible": {"type": "boolean"},
        "third_party_intervention_visible": {"type": "boolean"},
        "not_established": {"type": "array", "items": {"type": "string"}},
    },
    "required": [
        "frame_observations",
        "visible_changes",
        "physical_contact_visible",
        "third_party_intervention_visible",
        "not_established",
    ],
    "additionalProperties": False,
}

print("prompt is a", type(prompt))
print("schema is a", type(schema))

# CELL: Send the images through the selected route
if ROUTE == "openrouter":
    content = [
        {"type": "text", "text": prompt},
        {"type": "image_url", "image_url": {"url": image_to_data_url(frame_1)}},
        {"type": "image_url", "image_url": {"url": image_to_data_url(frame_2)}},
        {"type": "image_url", "image_url": {"url": image_to_data_url(frame_3)}},
        {"type": "image_url", "image_url": {"url": image_to_data_url(frame_4)}},
    ]
    messages = [{"role": "user", "content": content}]
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        response = client.chat.send(
            model=HOSTED_MODEL,
            messages=messages,
            temperature=0,
            response_format={"type": "json_schema", "json_schema": {
                "name": "protest_sequence",
                "strict": True,
                "schema": schema,
            }},
        )
    raw_output = response.choices[0].message.content
else:
    messages = [{
        "role": "user",
        "content": prompt,
        "images": [str(frame_1), str(frame_2), str(frame_3), str(frame_4)],
    }]
    try:
        response = ollama.chat(think=False,
            model=LOCAL_MODEL,
            messages=messages,
            format=schema,
            options={"temperature": 0},
        )
    except ConnectionError as error:
        raise ConnectionError(
            "Python could not reach Ollama. Start the Ollama application, run "
            "'ollama list' in a terminal, and then rerun this task."
        ) from error
    raw_output = response.message.content

print("Raw JSON text:", raw_output)
print("raw_output is a", type(raw_output))

# CELL: Parse and inspect the model's claims
description = json.loads(raw_output)

print("description is a", type(description))
print("Frame observations:", description["frame_observations"])
print("Visible changes:", description["visible_changes"])
print("Physical contact visible:", description["physical_contact_visible"])
print("Third-party intervention visible:", description["third_party_intervention_visible"])
print("Not established:", description["not_established"])

# CELL: Record the researcher's assessment
supported_claim = input("One claim clearly supported by the frames: ").strip()
unsupported_claim = input("One unsupported or overstated claim: ").strip()
missing_observation = input("One visible detail the model missed: ").strip()

if not supported_claim or not unsupported_claim or not missing_observation:
    raise ValueError("Complete all three parts of the researcher check.")

researcher_check = {
    "supported_claim": supported_claim,
    "unsupported_or_overstated_claim": unsupported_claim,
    "missing_observation": missing_observation,
}

research_record = {
    "source": source_record,
    "route": ROUTE,
    "model": HOSTED_MODEL if ROUTE == "openrouter" else LOCAL_MODEL,
    "prompt": prompt,
    "raw_output": raw_output,
    "parsed_output": description,
    "researcher_check": researcher_check,
}

print("Saved record fields:", list(research_record.keys()))
print("Researcher check:", research_record["researcher_check"])

# ONE CHANGE: replace only the 8.5-second endpoint with the 11.5-second frame.
# Keep the first three frames, prompt, schema, route, model and temperature fixed.
frame_5 = IMAGE_DIR / "uttarakhand_frame_5_11.5s.png"
changed_frames = [frame_1, frame_2, frame_3, frame_5]
changed_timestamps = [4.5, 5.0, 6.0, 11.5]

print("Original endpoint:", source_record["timestamps_seconds"][-1])
print("Changed endpoint:", changed_timestamps[-1])

# CELL: Make the second model call
if ROUTE == "openrouter":
    changed_content = [
        {"type": "text", "text": prompt},
        {"type": "image_url", "image_url": {"url": image_to_data_url(frame_1)}},
        {"type": "image_url", "image_url": {"url": image_to_data_url(frame_2)}},
        {"type": "image_url", "image_url": {"url": image_to_data_url(frame_3)}},
        {"type": "image_url", "image_url": {"url": image_to_data_url(frame_5)}},
    ]
    changed_messages = [{"role": "user", "content": changed_content}]
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        changed_response = client.chat.send(
            model=HOSTED_MODEL,
            messages=changed_messages,
            temperature=0,
            response_format={"type": "json_schema", "json_schema": {
                "name": "protest_sequence",
                "strict": True,
                "schema": schema,
            }},
        )
    changed_raw_output = changed_response.choices[0].message.content
else:
    changed_messages = [{
        "role": "user",
        "content": prompt,
        "images": [str(frame_1), str(frame_2), str(frame_3), str(frame_5)],
    }]
    try:
        changed_response = ollama.chat(think=False,
            model=LOCAL_MODEL,
            messages=changed_messages,
            format=schema,
            options={"temperature": 0},
        )
    except ConnectionError as error:
        raise ConnectionError(
            "Python could not reach Ollama. Start the Ollama application, run "
            "'ollama list' in a terminal, and then rerun this task."
        ) from error
    changed_raw_output = changed_response.message.content

print("Changed raw JSON text:", changed_raw_output)
changed_description = json.loads(changed_raw_output)
print("Changed result:", changed_description)

# CELL: Check the changed return and save the comparison
changed_supported_claim = input(
    "One claim clearly supported in the later-endpoint return: "
).strip()
changed_unsupported_claim = input(
    "One unsupported or overstated claim in that return: "
).strip()
changed_missing_observation = input(
    "One visible detail that return missed: "
).strip()
endpoint_comparison = input(
    "How did replacing 8.5 seconds with 11.5 seconds change the account? "
).strip()

if not all([
    changed_supported_claim,
    changed_unsupported_claim,
    changed_missing_observation,
    endpoint_comparison,
]):
    raise ValueError("Complete all four parts of the endpoint comparison.")

changed_source_record = source_record.copy()
changed_source_record["timestamps_seconds"] = changed_timestamps
changed_researcher_check = {
    "supported_claim": changed_supported_claim,
    "unsupported_or_overstated_claim": changed_unsupported_claim,
    "missing_observation": changed_missing_observation,
}
changed_research_record = {
    "source": changed_source_record,
    "route": ROUTE,
    "model": HOSTED_MODEL if ROUTE == "openrouter" else LOCAL_MODEL,
    "prompt": prompt,
    "raw_output": changed_raw_output,
    "parsed_output": changed_description,
    "researcher_check": changed_researcher_check,
}
comparison_record = {
    "original": research_record,
    "later_endpoint": changed_research_record,
    "student_comparison": endpoint_comparison,
}

print("Original visible changes:", description["visible_changes"])
print("Later-endpoint visible changes:", changed_description["visible_changes"])
print("Your comparison:", endpoint_comparison)
