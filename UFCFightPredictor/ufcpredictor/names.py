"""Fighter-name normalization and matching across sources.

UFCStats, ESPN and the odds dataset spell names differently ("Waldo Cortes
Acosta" / "Waldo Cortes-Acosta", "Sean King III", accents). Names are compared
in a normalized form: ASCII, lower case, punctuation and generational
suffixes removed.
"""

from __future__ import annotations

import difflib
import re
import unicodedata

import pandas as pd

SUFFIXES = {"jr", "sr", "ii", "iii", "iv"}


def normalize_name(name) -> str:
    if name is None or (isinstance(name, float) and pd.isna(name)):
        return ""
    text = unicodedata.normalize("NFKD", str(name)).encode("ascii", "ignore").decode()
    text = re.sub(r"[-‐_/]", " ", text.lower())
    text = re.sub(r"[^a-z ]", "", text)
    tokens = [t for t in text.split() if t not in SUFFIXES]
    return " ".join(tokens)


def match_name(name, candidates: pd.Series, cutoff: float = 0.88) -> str | None:
    """Index label in ``candidates`` (id -> name) that best matches ``name``.

    Tries, in order: the same normalized name, the same tokens in any order,
    the same first initial and last name, then a close spelling. A rule that
    matches more than one candidate is ambiguous and falls through, so a
    debutant who shares a surname with a veteran is not merged with the veteran.
    """
    target = normalize_name(name)
    if not target or candidates.empty:
        return None
    norm = candidates.map(normalize_name)
    exact = norm[norm == target]
    if len(exact) == 1:
        return exact.index[0]
    if len(exact) > 1:
        return None
    key = " ".join(sorted(target.split()))
    tokens = norm[norm.map(lambda s: " ".join(sorted(s.split()))) == key]
    if len(tokens) == 1:
        return tokens.index[0]
    parts = target.split()
    if len(parts) >= 2:
        loose = norm[norm.str.startswith(parts[0][0]) & norm.str.endswith(" " + parts[-1])]
        if len(loose) == 1 and difflib.SequenceMatcher(None, target, loose.iloc[0]).ratio() >= 0.7:
            return loose.index[0]
    close = difflib.get_close_matches(target, norm.tolist(), n=2, cutoff=cutoff)
    if len(close) == 1 or (len(close) == 2 and close[0] != close[1] and
                           difflib.SequenceMatcher(None, target, close[0]).ratio()
                           - difflib.SequenceMatcher(None, target, close[1]).ratio() > 0.05):
        hits = norm[norm == close[0]]
        if len(hits) == 1:
            return hits.index[0]
    return None


def pair_key(a, b) -> str:
    """Order-free key for a bout between two names."""
    return "|".join(sorted([normalize_name(a), normalize_name(b)]))
