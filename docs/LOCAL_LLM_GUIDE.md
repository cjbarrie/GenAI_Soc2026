# Running local LLMs for this course

**Checked:** August 27, 2026. Every student completes the initial Ollama setup and calls in Weeks 1–2, using a paired or instructor machine when their own hardware is unsuitable. From Week 3, students may choose Ollama or OpenRouter for normal assessed work. Cached records are contingencies for genuine access failures.

“Local” describes where inference runs. It does not establish quality, validity, privacy, openness, or reproducibility by itself.

## Decide before downloading

1. **What is the research reason?** Privacy, cost control, inspectable artifacts, offline work, or comparison with a hosted route are defensible reasons. Novelty alone is not.
2. **Can the data leave the machine?** If not, also check backups, logs, telemetry, plugins, and whether any cloud features are active.
3. **What fits?** Model weights, the key/value cache created by the context, and runtime overhead all use memory. Longer context can make a model that loaded successfully run slowly or fail.
4. **What license applies?** “Open weights” does not necessarily mean open source or unrestricted research use. Record the license and model source.
5. **What is the fallback?** Cache the exact raw output and configuration used for class.

## Hardware decision tree

- **Apple Silicon with 16 GB or more unified memory:** begin with a small quantized model in Ollama or LM Studio. Increase size only after checking memory pressure and latency.
- **Windows/Linux with a supported GPU:** choose a model whose quantized weights and context fit available VRAM. Partial CPU offload can work but may be much slower.
- **8 GB or an older/unsupported machine:** use the smallest available model for mechanics, or use the supplied cache. Hardware ownership never changes the grading standard.
- **Shared or managed computer:** confirm permission and disk quota before downloading multi-gigabyte model files.

Parameter count is not a memory estimate by itself. Quantization compresses stored weights, usually trading some numerical precision for lower memory and sometimes higher speed. Record the exact artifact/tag and quantization rather than merely saying “Llama” or “Gemma.”

## Route 1 — Ollama (course default)

Ollama supports macOS, Windows, and Linux. Its official quickstart is <https://docs.ollama.com/quickstart>; its local API normally runs at `http://localhost:11434/api`.

```bash
ollama run gemma4:e2b-it-qat
```

Exit an interactive chat with `/bye`. Inspect models already downloaded with `ollama list`; inspect currently loaded models and CPU/GPU placement with `ollama ps`.

### Call the local server from plain Python

```python
import requests

request_record = {
    "model": "gemma4:e2b-it-qat",
    "prompt": "Classify the synthetic comment as SUPPORT, OPPOSE, or UNCLEAR.",
    "stream": False,
    "options": {"temperature": 0},
}

response = requests.post(
    "http://localhost:11434/api/generate",
    json=request_record,
    timeout=120,
)
response.raise_for_status()
raw_record = response.json()
print(raw_record)
```

Read this code in six steps:

1. `request_record` is a dictionary describing the intended transformation.
2. `requests.post(...)` sends that dictionary to the server on this computer.
3. `timeout=120` prevents an endless wait; it does not control model generation length.
4. `raise_for_status()` turns an HTTP failure into a visible Python error.
5. `response.json()` converts the response body into Python dictionaries/lists/numbers/strings.
6. Printing the entire raw object comes before extracting text, so metadata is not silently lost.

Ollama can enforce JSON or a JSON schema in local structured output. Even well-formed JSON still requires construct validation: <https://docs.ollama.com/capabilities/structured-outputs>.

## Route 2 — LM Studio (GUI alternative)

LM Studio provides a graphical model browser/loader and can run an API server. Check current platform requirements before installing: <https://lmstudio.ai/docs/app/system-requirements>.

1. Download a model in **Discover**.
2. Load it from **Chat** or **Developer**.
3. Start the server in **Developer**, or run `lms server start`.
4. Record the displayed model identifier, load settings, runtime, and server port.

The local server normally listens at `http://localhost:1234` and exposes compatible endpoints. Once model files and runtimes are downloaded, LM Studio documents that chatting and local serving can operate offline: <https://lmstudio.ai/docs/app/offline>.

## One comparable research record

Hosted and local paths should be mapped into the same visible schema:

```python
record = {
    "runtime": "ollama",          # or "openrouter" / "lm_studio"
    "model": "gemma4:e2b-it-qat", # exact requested identifier
    "model_artifact": None,        # add hash/path/tag when available
    "quantization": None,          # record when exposed
    "parameters": {"temperature": 0},
    "input": request_record,
    "raw_output": raw_record,
    "retrieved_at": "2026-09-09T14:20:00Z",
    "latency_seconds": None,
    "validation": None,
}
```

The common schema enables comparison. It does not make the systems scientifically equivalent.

## Privacy and network boundaries

- Use only synthetic course data during setup.
- Do not bind a local server to `0.0.0.0` or expose it through a tunnel for this course.
- A server on `localhost` is accessible from this machine; check what other local software can reach it.
- Disable optional cloud features when a study requires a genuinely local path.
- Model downloads, update checks, and discovery catalogs require network access even when later inference is offline.
- Local logs, chat histories, crash reports, and backups may retain content. Locate and review them before handling research data.

## Reproducibility record

Save, when available:

- runtime and version;
- exact model tag, source URL, file hash, and quantization;
- license/version;
- system information relevant to execution;
- context length and generation settings;
- prompt/messages and raw output;
- retrieval/run date and random seed where supported;
- latency and failure/retry record;
- code commit or notebook version;
- validation data and decision.

Temperature zero reduces one source of variation but does not freeze runtime versions, kernels, prompt templates, model artifacts, or implementation details.

## Troubleshooting without guessing

| Symptom | Inspect first | Likely next action |
|---|---|---|
| command not found | installation and terminal restart | use the documented executable path |
| connection refused | whether the local server is running and the port | start server; confirm URL |
| model not found | `ollama list` or LM Studio model list | use the exact installed tag |
| out of memory | model size, quantization, context, other apps | unload; shorten context; choose smaller model |
| extremely slow | `ollama ps`, CPU/GPU placement, context | reduce model/context; use cache |
| invalid JSON | raw output and requested schema | preserve raw text; parse defensively; retry only under a recorded rule |
| different class result | prompt, model artifact, template, settings | treat as a discrepancy to analyze, not an installation failure |

## Stop, unload, and remove

Stop a running chat or server using the runtime’s documented controls. Confirm nothing is loaded (`ollama ps` or the LM Studio Developer view) before deleting model files. Use the runtime’s model-management command/UI rather than deleting broad folders manually. Model removal is optional; do it only after resolving the exact artifact and confirming no class project depends on it.

## Course checkpoints

- Session 1: runtime, weights, quantization, and research records.
- Session 2: same annotation schema across cache, OpenRouter, and local output.
- Session 3: synthetic interview privacy clinic.
- Session 7: full setup and troubleshooting lab.
- Session 8: hosted/local population predictions, neither treated as gold standard.
- Session 12: exact-artifact replication where feasible.
