"""Read central model defaults without hiding what values are used."""

from __future__ import annotations

import json
import os
from pathlib import Path


def load_course_config(repo_root: Path) -> dict:
    """Return the recorded defaults, overridden by named environment variables.

    Input: the repository root as a Path.
    Transformation: read JSON, then check two environment variables.
    Output: a dictionary containing the resolved hosted and local settings.
    """
    config_path = repo_root / "config" / "course_models.json"
    config = json.loads(config_path.read_text(encoding="utf-8"))

    hosted_env = config["hosted"]["environment_variable"]
    local_env = config["local"]["environment_variable"]
    config["hosted"]["model"] = os.getenv(hosted_env, config["hosted"]["model"])
    config["local"]["model"] = os.getenv(local_env, config["local"]["model"])
    return config

