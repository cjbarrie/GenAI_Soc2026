"""Small transport utilities used in the multimodal teaching notebook."""

from __future__ import annotations

import base64
import mimetypes
from pathlib import Path


def image_to_data_url(path: Path) -> str:
    """Convert one local image path into an embeddable data URL.

    Input: a Path pointing to a local image.
    Output: one string containing the MIME type and base64-encoded bytes.

    Students use this boundary in Week 4 but are not assessed on base64.
    """
    path = Path(path)
    mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"
