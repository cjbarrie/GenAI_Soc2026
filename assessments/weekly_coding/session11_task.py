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
if not os.getenv("OPENROUTER_API_KEY"):
    os.environ["OPENROUTER_API_KEY"] = getpass("OpenRouter course key (hidden): ")

# CELL: Choose a route and store a small local source corpus
ROUTE = "ollama"
course_corpus = [
    {"id":"s1","title":"Replication for language models","excerpt":"A rerun must preserve prompts, model access, settings and outputs."},
    {"id":"s2","title":"Research agents and long tasks","excerpt":"Errors can enter during search, extraction, coding and synthesis."},
    {"id":"s3","title":"Synthetic survey respondents","excerpt":"Aggregate similarity does not establish individual correspondence."},
]

# CELL: Define the one tool available to the agent
def search_course_corpus(query):
    query_words = query.lower().split()
    matches = []
    for source in course_corpus:
        searchable = (source["title"] + " " + source["excerpt"]).lower()
        if any(word in searchable for word in query_words):
            matches.append(source)
    return {"query":query,"matches":matches}

# CELL: Ask the model which search to make
request_schema = {
    "type":"object","properties":{
        "tool_name":{"type":"string","enum":["search_course_corpus"]},
        "query":{"type":"string"}},
    "required":["tool_name","query"],"additionalProperties":False,
}
research_question = "Where can errors enter during a long research-agent task?"
messages = [{"role":"user","content":(
    "Choose the one available tool and a short query for this research question: " + research_question
)}]
if ROUTE == "openrouter":
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        response = client.chat.send(model=HOSTED_MODEL,messages=messages,temperature=0,response_format={"type":"json_schema","json_schema":{"name":"tool_request","strict":True,"schema":request_schema}})
    request_raw = response.choices[0].message.content
else:
    response = ollama.chat(think=False, model=LOCAL_MODEL,messages=messages,format=request_schema,options={"temperature":0})
    request_raw = response.message.content
tool_request = json.loads(request_raw)
print("Raw tool request:", request_raw)

# CELL: Dispatch the named tool and inspect its returned record
if tool_request["tool_name"] == "search_course_corpus":
    tool_result = search_course_corpus(tool_request["query"])
print("Tool result:", tool_result)

# CELL: Return the evidence to the model and request one bounded claim
claim_schema = {"type":"object","properties":{"claim":{"type":"string"},"source_id":{"type":"string"}},"required":["claim","source_id"],"additionalProperties":False}
claim_messages = [{"role":"user","content":(
    "Answer with one bounded claim and one source_id using only this tool result: " + json.dumps(tool_result)
)}]
if ROUTE == "openrouter":
    with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
        response = client.chat.send(model=HOSTED_MODEL,messages=claim_messages,temperature=0,response_format={"type":"json_schema","json_schema":{"name":"source_claim","strict":True,"schema":claim_schema}})
    claim_raw = response.choices[0].message.content
else:
    response = ollama.chat(think=False, model=LOCAL_MODEL,messages=claim_messages,format=claim_schema,options={"temperature":0})
    claim_raw = response.message.content
claim = json.loads(claim_raw)
trajectory = {"question":research_question,"tool_request":tool_request,"tool_result":tool_result,"claim":claim}
print("Trajectory:", trajectory)

# ONE CHANGE: ask "What must be saved to reproduce an LLM result?"
