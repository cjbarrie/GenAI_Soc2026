"""Build the beginner Python foundations notebook with executable outputs cleared."""

from __future__ import annotations

import json
from hashlib import sha1
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def md(text: str) -> dict:
    cell_id = sha1(("markdown\0" + text).encode()).hexdigest()[:12]
    return {"cell_type": "markdown", "id": cell_id, "metadata": {}, "source": text}


def code(text: str) -> dict:
    cell_id = sha1(("code\0" + text).encode()).hexdigest()[:12]
    return {"cell_type": "code", "id": cell_id, "execution_count": None, "metadata": {}, "outputs": [], "source": text}


cells = [
    md("""# Python foundations for LLM-assisted sociology

This workbook assumes no prior Python. Its goal is **computational fluency for empirical sociology**, not software engineering.

Use the same speaking routine for every cell:

1. **Input:** What values already exist?
2. **Type:** Are they strings, numbers, booleans, lists, dictionaries, or something else?
3. **Operation:** What does this line do to those values?
4. **Output:** What exact value and type should appear?
5. **Research meaning:** What would the value represent in a study?

Predict first. Run second. Explain third. Change only one thing at a time."""),
    md("""## Diagnostic

If you can explain every line below, predict every printed value, and repair the final assertion without help, skim Units 0–3 and begin at Unit 4. Otherwise work in order."""),
    code('''prompt = "Classify this meeting comment"
settings = {"temperature": 0, "live": False}
messages = [{"role": "user", "content": prompt}]
print(type(prompt), len(messages), settings["live"])
assert messages[0]["content"] == prompt'''),
    md("""# Unit 0 — Running code

A notebook contains **markdown cells** like this one and **code cells** like the next one. Python evaluates a code cell from top to bottom. A name created in one cell remains available later until the kernel restarts.

`#` begins a comment. Python ignores the rest of that line. `print(...)` makes a value visible; it does not change the value."""),
    code('''# A string value appears between quotation marks.
cached_output = "SUPPORT"

# print sends the value to the visible notebook output.
print(cached_output)'''),
    md("""### Say it aloud

Input: the string `"SUPPORT"`. Operation: assign it the name `cached_output`, then print the value attached to that name. Output: the text `SUPPORT`. Research meaning: one cached model label—not a validated measurement."""),
    md("""# Unit 1 — Values, variables, and types

A **value** is data. A **type** tells Python what operations make sense for that value. A **variable** is a name pointing to a value. `=` assigns; it does not mean “is mathematically equal to.”"""),
    code('''prompt_text = "Summarize this excerpt"   # str: text
token_budget = 120                         # int: whole number
temperature = 0.2                          # float: decimal number
request_succeeded = True                   # bool: True or False
human_label = None                          # NoneType: deliberately missing

print(type(prompt_text))
print(type(token_budget))
print(type(temperature))
print(type(request_succeeded))
print(type(human_label))'''),
    md("""### Why types matter

`"120"` is a string; `120` is an integer. Python can add integers, but adding strings joins text. `None` is not zero, an empty string, or the word “unknown.” It records the absence of a value. In research, decide whether missingness means not collected, not applicable, failed, or deliberately withheld."""),
    code('''print(120 + 5)        # numeric addition → 125
print("120" + "5")    # string concatenation → "1205"

print(request_succeeded == True)  # == asks a question and returns a Boolean
print(human_label is None)         # `is None` checks deliberate missingness'''),
    md("""### Micro-task

Create variables for a model identifier, a run date, the number of records, a live/cached flag, and a missing validation score. Print each type. Then explain why the date is best stored as a string at this stage."""),
    code('''model_id = "cached-demo-v1"
run_date = "2026-09-02"
number_of_records = 12
used_live_model = False
validation_score = None

assert type(model_id) is str
assert type(number_of_records) is int
assert type(used_live_model) is bool
assert validation_score is None'''),
    md("""# Unit 2 — Lists and indexing

A **list** is an ordered collection written with square brackets. Positions start at zero. `items[0]` is the first item; `items[-1]` is the last. `append` changes the existing list by adding one value at the end."""),
    code('''labels = ["SUPPORT", "OPPOSE", "UNCLEAR"]
print(labels)
print(labels[0])
print(labels[-1])
print(len(labels))

labels.append("MISSING")
print(labels)'''),
    md("""### Slicing

`items[start:stop]` returns a new list from `start` up to—but not including—`stop`. Predict before running."""),
    code('''model_outputs = ["SUPPORT", "SUPPORT", "OPPOSE", "UNCLEAR"]
first_two = model_outputs[0:2]
print(first_two)
assert first_two == ["SUPPORT", "SUPPORT"]'''),
    md("""# Unit 3 — Dictionaries and nested records

A **dictionary** stores key–value pairs inside braces. Retrieve a value by key: `record["model"]`. Unlike a list position, a key describes the field's meaning."""),
    code('''settings = {
    "model": "cached-demo-v1",
    "temperature": 0,
    "live": False,
}

print(settings["model"])
print(type(settings))
settings["retrieved_at"] = "2026-09-02"
print(settings)'''),
    md("""### Lists of dictionaries

This is the central course data structure: the list is the collection; each dictionary is one case; dictionary keys are fields. Read brackets from the outside inward."""),
    code('''records = [
    {"id": 1, "text": "I support the plan", "label": "SUPPORT"},
    {"id": 2, "text": "The plan costs too much", "label": "OPPOSE"},
]

first_record = records[0]
first_text = records[0]["text"]
print(type(records), type(first_record), type(first_text))
print(first_text)'''),
    md("""### Mutation and copying

Two names can point to the same mutable dictionary. A direct assignment does not copy it. Use `.copy()` when the research record should preserve the prior state."""),
    code('''original = {"label": "UNCLEAR"}
same_object = original
separate_copy = original.copy()

same_object["label"] = "SUPPORT"
print(original)       # changed because both names point to one object
print(separate_copy)  # unchanged because it is a copy'''),
    md("""# Unit 4 — Decisions with `if`, `elif`, and `else`

A conditional chooses one branch. Python evaluates conditions from top to bottom and runs the first branch whose condition is `True`. Indentation shows which lines belong to a branch."""),
    code('''label = "UNCLEAR"

if label == "SUPPORT":
    decision = "count as explicit support"
elif label == "OPPOSE":
    decision = "count as explicit opposition"
else:
    decision = "retain for review"

print(decision)'''),
    md("""### Boolean logic

`and` requires both conditions; `or` requires at least one; `not` reverses a Boolean. Parentheses make a compound decision easier to read."""),
    code('''label_is_valid = label in ["SUPPORT", "OPPOSE", "UNCLEAR"]
has_human_check = False

if label_is_valid and not has_human_check:
    status = "structured but not validated"
else:
    status = "inspect the record"

print(status)'''),
    md("""# Unit 5 — Repetition with `for` loops

A `for` loop runs the indented block once for every item in a collection. Trace the first iteration with an actual value before describing the general pattern."""),
    code('''labels = ["SUPPORT", "OPPOSE", "SUPPORT", "UNCLEAR"]

for label in labels:
    print("current value:", label)'''),
    md("""### Accumulation

An accumulator starts before the loop and changes during each iteration. Here `support_count` begins at zero and increases only when the condition is true."""),
    code('''support_count = 0

for label in labels:
    if label == "SUPPORT":
        support_count = support_count + 1

print(support_count)
assert support_count == 2'''),
    md("""### Frequency dictionary

`counts.get(label, 0)` retrieves the current count or uses zero if the key is new. The right side is calculated before being assigned back to the key."""),
    code('''counts = {}

for label in labels:
    old_count = counts.get(label, 0)
    new_count = old_count + 1
    counts[label] = new_count

print(counts)
assert counts == {"SUPPORT": 2, "OPPOSE": 1, "UNCLEAR": 1}'''),
    md("""# Unit 6 — Functions

A function gives a reusable name to an algorithm. **Arguments** are the input values supplied at the call. Variables inside are local working names. `return` sends one output value back to the caller."""),
    code('''def count_label(labels, target):
    """Return how many values in labels equal target."""
    count = 0
    for label in labels:
        if label == target:
            count += 1
    return count


result = count_label(labels, "SUPPORT")
print(result)
assert result == 2'''),
    md("""### Function trace

When `count_label(labels, "SUPPORT")` runs:

1. the existing list enters under the local name `labels`;
2. the string `"SUPPORT"` enters under `target`;
3. `count` begins at zero;
4. the loop compares each list value with the target;
5. `return count` produces the integer `2`;
6. the caller assigns that integer the name `result`.

Changing the variable name does not change the algorithm. Changing the argument value may change the output."""),
    md("""# Unit 7 — CSV, JSON, and research data

CSV is a rectangular text format. JSON can represent nested lists, dictionaries, numbers, strings, booleans, and null values. Reading a file transforms bytes/text on disk into Python objects; parsing does not validate the research meaning."""),
    code('''import json

raw_json = '{"id": 1, "label": "SUPPORT", "validated": false}'
parsed = json.loads(raw_json)

print(type(raw_json))
print(type(parsed))
print(type(parsed["validated"]))
assert parsed["label"] == "SUPPORT"'''),
    md("""### Plain Python before pandas

Pandas can summarize tables compactly, but begin by understanding each record and loop. The two approaches below calculate the same counts; the first exposes the algorithm."""),
    code('''records = [
    {"group": "A", "response": 1},
    {"group": "A", "response": 0},
    {"group": "B", "response": 1},
]

totals = {}
for record in records:
    group = record["group"]
    totals[group] = totals.get(group, 0) + record["response"]

print(totals)'''),
    md("""# Unit 8 — Research algorithms

Most course code repeats a small set of patterns:

- **filter:** retain cases that meet a condition;
- **transform:** create a new value from each case;
- **count/accumulate:** update a running summary;
- **group:** collect cases sharing a key;
- **match:** join two records using an ID;
- **deduplicate:** retain one record for an explicit key;
- **sort:** order records using a declared field;
- **decompose:** move one understandable operation into a function.

Write the research rule in a sentence before expressing it in Python."""),
    code('''human = [{"id": 1, "label": "SUPPORT"}, {"id": 2, "label": "OPPOSE"}]
model = [{"id": 1, "label": "SUPPORT"}, {"id": 2, "label": "SUPPORT"}]

# Match: create a lookup from model ID to model label.
model_by_id = {}
for record in model:
    model_by_id[record["id"]] = record["label"]

# Transform: build paired records without discarding the human reference.
paired = []
for record in human:
    paired.append({
        "id": record["id"],
        "human_label": record["label"],
        "model_label": model_by_id[record["id"]],
    })

print(paired)'''),
    md("""# Reading errors

An error message is evidence about where Python could not continue. Read the final line first, then the named line of your code. Ask:

1. What object did I think I had?
2. What type/value did Python actually report?
3. Which earlier line created it?

Common messages:

- `NameError`: the name does not exist in the current kernel state;
- `KeyError`: a dictionary lacks that exact key;
- `IndexError`: a list position does not exist;
- `TypeError`: the operation does not apply to the supplied type;
- `AssertionError`: an explicit expectation was false.

Do not delete a failing assertion merely to make the notebook run."""),
    md("""# Final foundations check

Complete this without compact pandas syntax. Then explain every line aloud."""),
    code('''def label_counts(records):
    """Return a frequency dictionary for each record's label field."""
    counts = {}
    for record in records:
        label = record["label"]
        counts[label] = counts.get(label, 0) + 1
    return counts


example_records = [
    {"id": 1, "label": "SUPPORT"},
    {"id": 2, "label": "UNCLEAR"},
    {"id": 3, "label": "SUPPORT"},
]

assert label_counts(example_records) == {"SUPPORT": 2, "UNCLEAR": 1}
assert label_counts([]) == {}
print("Foundations checks passed.")'''),
    md("""# What we deliberately omit

You do not need classes, decorators, asynchronous code, package architecture, or machine-learning mathematics to succeed in this course. You do need to inspect structured data, trace loops and decisions, write small functions, read errors, and connect computational output to a research claim.

Further help:

- [Official Python tutorial](https://docs.python.org/3/tutorial/)
- [JupyterLab documentation](https://jupyterlab.readthedocs.io/)
- [Python for Data Analysis: community edition](https://wesmckinney.com/book/)
- NYU Data Services and course office hours

If a resource introduces a shortcut you cannot explain, return to the plain loop first."""),
]


notebook = {
    "cells": cells,
    "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python", "version": "3.11"}},
    "nbformat": 4,
    "nbformat_minor": 5,
}

path = ROOT / "workbook" / "00_python_foundations" / "python_foundations.ipynb"
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(notebook, indent=1) + "\n", encoding="utf-8")
print(path)
