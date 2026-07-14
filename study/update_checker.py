"""Utilities for checking whether a newer PrepFlow release exists."""

from __future__ import annotations

import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from study.version import APP_VERSION, LATEST_RELEASE_API_URL


def version_tuple(version: str) -> tuple[int, ...]:
    """Convert a release version such as v1.1.0 into comparable integers."""
    cleaned = version.strip().lower().removeprefix("v")
    return tuple(int(part) for part in cleaned.split("."))


def is_newer_version(latest_version: str) -> bool:
    """Return True when latest_version is newer than this installation."""
    return version_tuple(latest_version) > version_tuple(APP_VERSION)


def fetch_latest_version(timeout: int = 5) -> str:
    """Return the latest published PrepFlow release version from GitHub."""
    request = Request(
        LATEST_RELEASE_API_URL,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": f"PrepFlow/{APP_VERSION}",
        },
    )

    try:
        with urlopen(request, timeout=timeout) as response:
            payload = json.load(response)
    except (HTTPError, URLError, TimeoutError) as error:
        raise RuntimeError(
            "PrepFlow could not connect to the update service."
        ) from error

    tag_name = payload.get("tag_name")

    if not isinstance(tag_name, str) or not tag_name.strip():
        raise RuntimeError(
            "The update service returned an invalid release version."
        )

    return tag_name
