"""Single-slot local session persistence for PrepFlow."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


SAVE_VERSION = 1
SAVE_DIRECTORY = Path.home() / ".prepflow"
SAVE_PATH = SAVE_DIRECTORY / "session.json"


def save_session(state: dict[str, Any]) -> Path:
    """Overwrite the single PrepFlow session save."""
    SAVE_DIRECTORY.mkdir(parents=True, exist_ok=True)

    payload = {
        "version": SAVE_VERSION,
        "session": state,
    }

    temporary_path = SAVE_PATH.with_suffix(".tmp")
    temporary_path.write_text(
        json.dumps(payload, indent=2),
        encoding="utf-8",
    )
    temporary_path.replace(SAVE_PATH)

    return SAVE_PATH


def load_session() -> dict[str, Any] | None:
    """Load the saved session, or return None when no valid save exists."""
    if not SAVE_PATH.exists():
        return None

    try:
        payload = json.loads(SAVE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None

    if payload.get("version") != SAVE_VERSION:
        return None

    session = payload.get("session")
    return session if isinstance(session, dict) else None


def has_saved_session() -> bool:
    """Return whether a readable session save exists."""
    return load_session() is not None


def delete_saved_session() -> None:
    """Remove the single session save when present."""
    try:
        SAVE_PATH.unlink()
    except FileNotFoundError:
        pass
