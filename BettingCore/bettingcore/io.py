"""Downloads with a local cache, and writes that skip files whose content did not change."""

from __future__ import annotations

import logging
import os
import time
from pathlib import Path

import requests

log = logging.getLogger(__name__)


def fetch(url: str, path: Path, max_age_hours: float = 6.0, retries: int = 4, timeout: float = 120,
          session: requests.Session | None = None) -> Path:
    """Download ``url`` to ``path`` unless a copy younger than ``max_age_hours`` exists.

    Failures are retried with exponential backoff. A 404 is raised at once. If
    every attempt fails and an older copy exists, that copy is used.
    """
    path = Path(path)
    if path.exists() and (time.time() - path.stat().st_mtime) < max_age_hours * 3600:
        return path
    path.parent.mkdir(parents=True, exist_ok=True)
    getter = session or requests
    delay = 2.0
    for attempt in range(retries):
        try:
            with getter.get(url, timeout=timeout, stream=True) as resp:
                resp.raise_for_status()
                tmp = path.with_suffix(path.suffix + ".part")
                with open(tmp, "wb") as fh:
                    for chunk in resp.iter_content(chunk_size=1 << 20):
                        fh.write(chunk)
                os.replace(tmp, path)
            return path
        except requests.RequestException as exc:
            if isinstance(exc, requests.HTTPError) and exc.response is not None \
                    and exc.response.status_code == 404:
                raise
            if attempt == retries - 1:
                if path.exists():
                    log.warning("Using stale %s after download failed: %s", path.name, exc)
                    return path
                raise
            log.warning("Download of %s failed (%s); retrying in %.0fs", url, exc, delay)
            time.sleep(delay)
            delay *= 2
    return path


def write_if_changed(path, text: str, volatile: tuple[str, ...] = (), contains: bool = False) -> bool:
    """Write ``text`` unless it matches the file apart from volatile lines.

    A line is volatile when it starts with (or, with ``contains``, includes)
    one of the ``volatile`` strings, such as an "Updated ..." timestamp.
    Returns whether the file was written.
    """
    path = Path(path)

    def stable(t: str) -> list[str]:
        if contains:
            return [line for line in t.splitlines() if not any(v in line for v in volatile)]
        return [line for line in t.splitlines() if not line.lstrip().startswith(volatile)]

    if path.exists() and stable(path.read_text()) == stable(text):
        return False
    path.write_text(text)
    return True
