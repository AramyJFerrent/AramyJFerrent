"""Download the UFCStats scrape and reduce it to three tidy tables.

The scrape (about 12 MB) is cached in ``.cache/`` and boiled down to small
CSVs committed to the repo, so the predictor still runs if a download fails:

- ``data/bouts.csv``: one row per UFC bout with date, division, scheduled
  rounds, winner, method, round and time.
- ``data/fight_stats.csv``: one row per fighter per bout with round totals
  summed (knockdowns, strikes landed and attempted by target and position,
  takedowns, submission attempts, control time).
- ``data/fighters.csv``: tale of the tape (height, reach, stance, birth date).

Fighters are identified by their UFCStats id. The scrape names fighters in
each bout by name only, so the nine names shared by two different fighters
are told apart by weight class and age.
"""

from __future__ import annotations

import datetime as dt
import logging
import os
import re
import time
from pathlib import Path

import numpy as np
import pandas as pd
import requests

from .config import CACHE_DIR, DATA_DIR, DIVISIONS, SCRAPE_FILES, SCRAPE_URL
from .names import normalize_name

log = logging.getLogger(__name__)

BOUTS_PATH = DATA_DIR / "bouts.csv"
STATS_PATH = DATA_DIR / "fight_stats.csv"
FIGHTERS_PATH = DATA_DIR / "fighters.csv"

BOUT_COLUMNS = [
    "bout_id", "event", "date", "location", "order", "fighter_a", "fighter_b", "a_id", "b_id",
    "division", "gender", "title", "rounds", "winner", "method", "decision", "end_round",
    "end_seconds", "fight_seconds", "referee",
]
STAT_PAIRS = ["sig", "tot", "td", "head", "body", "leg", "dist", "clinch", "ground"]
STAT_COLUMNS = (["bout_id", "side", "kd", "sub_att", "rev", "ctrl"]
                + [f"{p}_{k}" for p in STAT_PAIRS for k in ("l", "a")])
FIGHTER_COLUMNS = ["fighter_id", "name", "height", "reach", "stance", "dob", "weight"]

METHODS = {
    "KO/TKO": "KO", "TKO - Doctor's Stoppage": "KO", "Submission": "SUB",
    "Decision - Unanimous": "DEC", "Decision - Split": "DEC", "Decision - Majority": "DEC",
}


def current_year(today: dt.date | None = None) -> int:
    """UFC has no offseason; predictions are graded by calendar year."""
    return (today or dt.date.today()).year


def fetch(url: str, path: Path, max_age_hours: float = 6.0, retries: int = 4) -> Path:
    """Download ``url`` to ``path`` unless a fresh enough copy exists."""
    if path.exists() and (time.time() - path.stat().st_mtime) < max_age_hours * 3600:
        return path
    path.parent.mkdir(parents=True, exist_ok=True)
    delay = 2.0
    for attempt in range(retries):
        try:
            with requests.get(url, timeout=120, stream=True) as resp:
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


# ---- field parsers --------------------------------------------------------

def _strip(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for col in df.columns:
        if df[col].dtype == object or pd.api.types.is_string_dtype(df[col]):
            df[col] = df[col].astype(str).str.strip().replace({"nan": np.nan, "": np.nan})
    return df


def _of(series: pd.Series) -> tuple[pd.Series, pd.Series]:
    """'9 of 37' -> (9, 37)."""
    parts = series.astype(str).str.extract(r"(\d+)\s+of\s+(\d+)")
    return parts[0].astype(float), parts[1].astype(float)


def _clock(series: pd.Series) -> pd.Series:
    """'2:32' -> 152 seconds."""
    parts = series.astype(str).str.extract(r"(\d+):(\d+)")
    return parts[0].astype(float) * 60 + parts[1].astype(float)


def _inches(series: pd.Series) -> pd.Series:
    feet = series.astype(str).str.extract(r"(\d+)'\s*(\d+)")
    out = feet[0].astype(float) * 12 + feet[1].astype(float)
    plain = series.astype(str).str.extract(r"^(\d+(?:\.\d+)?)\"")[0].astype(float)
    return out.fillna(plain)


def parse_weightclass(text) -> tuple[str, str, bool]:
    """'UFC Women's Flyweight Title Bout' -> ("Women's Flyweight", 'F', True)."""
    text = str(text or "")
    women = "Women" in text
    title = "Title" in text or "Championship" in text
    # Tournament finals (TUF, Road to UFC) are not UFC title fights.
    if "Tournament" in text or "Ultimate Fighter" in text or "Road to UFC" in text:
        title = False
    for name in sorted(DIVISIONS, key=len, reverse=True):
        base = name.replace("Women's ", "")
        if base in text and (name.startswith("Women's") == women):
            return name, "F" if women else "M", title
    if "Catch" in text:
        return "Catch Weight", "F" if women else "M", title
    if "Open" in text or "Superfight" in text:
        return "Open Weight", "M", title
    return "Catch Weight", "F" if women else "M", title


def parse_time_format(text) -> tuple[int, list[int]]:
    """Scheduled rounds and round lengths in minutes from '3 Rnd (5-5-5)'."""
    text = str(text or "")
    m = re.match(r"(\d+)\s*Rnd", text)
    lengths = [int(x) for x in re.findall(r"\d+", text.split("(", 1)[1])] if "(" in text else []
    if not m:
        return 0, lengths
    return int(m.group(1)), lengths


# ---- tables ---------------------------------------------------------------

def build_fighters(tott: pd.DataFrame) -> pd.DataFrame:
    t = _strip(tott)
    out = pd.DataFrame({
        "fighter_id": t["URL"].str.extract(r"fighter-details/(\w+)")[0],
        "name": t["FIGHTER"],
        "height": _inches(t["HEIGHT"]),
        "reach": _inches(t["REACH"]),
        "stance": t["STANCE"],
        "dob": pd.to_datetime(t["DOB"], format="%b %d, %Y", errors="coerce"),
        "weight": t["WEIGHT"].astype(str).str.extract(r"(\d+)")[0].astype(float),
    })
    return out.dropna(subset=["fighter_id"]).drop_duplicates("fighter_id").reset_index(drop=True)


def _slug(name: str) -> str:
    return "x-" + normalize_name(name).replace(" ", "-")


def resolve_ids(names: pd.Series, divisions: pd.Series, dates: pd.Series,
                fighters: pd.DataFrame) -> pd.Series:
    """UFCStats id for each bout appearance.

    A name shared by two fighters goes to the one whose listed weight is
    nearest the bout's division limit, then to the one of plausible age.
    Names missing from the tale of the tape get a stable id from the name.
    """
    by_name = fighters.groupby("name")
    unique = fighters.drop_duplicates("name", keep=False).set_index("name")["fighter_id"]
    ids = names.map(unique)
    shared = set(fighters.loc[fighters["name"].duplicated(keep=False), "name"])
    for idx in names.index[names.isin(shared)]:
        cands = by_name.get_group(names[idx])
        limit = DIVISIONS.get(divisions[idx], np.nan)
        gap = (cands["weight"] - limit).abs().fillna(999.0) if not np.isnan(limit) else \
            pd.Series(999.0, index=cands.index)
        age = (dates[idx] - cands["dob"]).dt.days / 365.25
        gap = gap + np.where(age.between(18, 45), 0.0, 50.0)
        ids[idx] = cands.loc[gap.idxmin(), "fighter_id"]
    missing = ids.isna()
    ids[missing] = names[missing].map(_slug)
    return ids


def build_bouts(results: pd.DataFrame, events: pd.DataFrame, fighters: pd.DataFrame) -> pd.DataFrame:
    r = _strip(results)
    e = _strip(events)
    e["date"] = pd.to_datetime(e["DATE"], format="%B %d, %Y", errors="coerce")
    e = e.drop_duplicates("EVENT").set_index("EVENT")
    # A few events were renamed and appear twice; keep the copy whose event is listed.
    r["listed"] = r["EVENT"].isin(e.index)
    r["order"] = r.groupby("EVENT").cumcount()
    r = r.sort_values("listed", ascending=False, kind="stable").drop_duplicates("URL")
    r = r[r["listed"]].sort_index()
    names = r["BOUT"].str.split(r"\s+vs\.\s+", n=1, expand=True)
    div = r["WEIGHTCLASS"].map(parse_weightclass)
    fmt = r["TIME FORMAT"].map(parse_time_format)
    rounds = fmt.map(lambda x: x[0])
    end_round = pd.to_numeric(r["ROUND"], errors="coerce")
    end_seconds = _clock(r["TIME"])

    def elapsed(i) -> float:
        lengths = fmt[i][1]
        k = int(end_round[i]) if not np.isnan(end_round[i]) else 1
        if not lengths:
            return np.nan if k > 1 else end_seconds[i]
        return 60.0 * sum(lengths[:k - 1]) + end_seconds[i]

    outcome = r["OUTCOME"].map({"W/L": "a", "L/W": "b", "D/D": "draw", "NC/NC": "nc"})
    method_raw = r["METHOD"].fillna("")
    out = pd.DataFrame({
        "bout_id": r["URL"].str.extract(r"fight-details/(\w+)")[0],
        "event": r["EVENT"],
        "date": r["EVENT"].map(e["date"]),
        "location": r["EVENT"].map(e["LOCATION"]),
        "order": r["order"],
        "fighter_a": names[0].str.strip(),
        "fighter_b": names[1].str.strip(),
        "division": div.map(lambda x: x[0]),
        "gender": div.map(lambda x: x[1]),
        "title": div.map(lambda x: x[2]),
        "rounds": rounds,
        "winner": outcome,
        "method": method_raw.map(METHODS).fillna("OTHER"),
        "decision": method_raw.str.extract(r"Decision - (\w+)")[0].str.lower(),
        "end_round": end_round,
        "end_seconds": end_seconds,
        "fight_seconds": [elapsed(i) for i in r.index],
        "referee": r["REFEREE"],
    })
    out.loc[out["winner"].isin(["draw", "nc"]), "method"] = out["winner"].str.upper()
    out["a_id"] = resolve_ids(out["fighter_a"], out["division"], out["date"], fighters)
    out["b_id"] = resolve_ids(out["fighter_b"], out["division"], out["date"], fighters)
    # Within a card the scrape lists the main event first; fights happen in reverse.
    out = out.sort_values(["date", "event", "order"], ascending=[True, True, False])
    return out[BOUT_COLUMNS].reset_index(drop=True)


def build_stats(stats: pd.DataFrame, results: pd.DataFrame, bouts: pd.DataFrame) -> pd.DataFrame:
    s = _strip(stats)
    r = _strip(results)
    r["bout_id"] = r["URL"].str.extract(r"fight-details/(\w+)")[0]
    # Map (event, bout) to the id through every copy, so renamed events still match.
    key = r.drop_duplicates(["EVENT", "BOUT"]).set_index(["EVENT", "BOUT"])["bout_id"]
    s = s.join(key, on=["EVENT", "BOUT"])
    s = s.dropna(subset=["bout_id"]).drop_duplicates(["bout_id", "ROUND", "FIGHTER"])
    cols = {"kd": pd.to_numeric(s["KD"], errors="coerce"),
            "sub_att": pd.to_numeric(s["SUB.ATT"], errors="coerce"),
            "rev": pd.to_numeric(s["REV."], errors="coerce"),
            "ctrl": _clock(s["CTRL"])}
    for name, src in [("sig", "SIG.STR."), ("tot", "TOTAL STR."), ("td", "TD"), ("head", "HEAD"),
                      ("body", "BODY"), ("leg", "LEG"), ("dist", "DISTANCE"), ("clinch", "CLINCH"),
                      ("ground", "GROUND")]:
        cols[f"{name}_l"], cols[f"{name}_a"] = _of(s[src])
    per_round = pd.DataFrame(cols, index=s.index)
    per_round["bout_id"] = s["bout_id"]
    per_round["fighter"] = s["FIGHTER"]
    totals = per_round.groupby(["bout_id", "fighter"], as_index=False).sum(min_count=1)
    b = bouts.set_index("bout_id")
    side_a = totals["bout_id"].map(b["fighter_a"]) == totals["fighter"]
    side_b = totals["bout_id"].map(b["fighter_b"]) == totals["fighter"]
    totals["side"] = np.where(side_a, "a", np.where(side_b, "b", None))
    totals = totals.dropna(subset=["side"])
    return totals[STAT_COLUMNS].sort_values(["bout_id", "side"]).reset_index(drop=True)


def refresh_data(max_age_hours: float = 6.0) -> bool:
    """Download the scrape and rewrite the committed tables. False if it failed."""
    try:
        paths = {name: fetch(SCRAPE_URL.format(name=name), CACHE_DIR / f"{name}.csv", max_age_hours)
                 for name in SCRAPE_FILES}
    except requests.RequestException as exc:
        log.warning("UFCStats scrape download failed (%s); using committed data", exc)
        return False
    raw = {name: pd.read_csv(path, dtype=str, keep_default_na=False) for name, path in paths.items()}
    fighters = build_fighters(raw["ufc_fighter_tott"])
    bouts = build_bouts(raw["ufc_fight_results"], raw["ufc_event_details"], fighters)
    stats = build_stats(raw["ufc_fight_stats"], raw["ufc_fight_results"], bouts)
    if BOUTS_PATH.exists() and len(bouts) < 0.95 * len(pd.read_csv(BOUTS_PATH, usecols=["bout_id"])):
        log.warning("Downloaded scrape has only %d bouts; keeping committed data", len(bouts))
        return False
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    bouts.to_csv(BOUTS_PATH, index=False, date_format="%Y-%m-%d")
    stats.to_csv(STATS_PATH, index=False, float_format="%.0f")
    fighters.sort_values("fighter_id").to_csv(FIGHTERS_PATH, index=False, date_format="%Y-%m-%d",
                                              float_format="%.1f")
    log.info("Rebuilt data: %d bouts through %s, %d fighter-bout stat lines, %d fighters",
             len(bouts), bouts["date"].max().date(), len(stats), len(fighters))
    return True


def load_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Committed bouts, per-fighter stats and fighters."""
    bouts = pd.read_csv(BOUTS_PATH, parse_dates=["date"], dtype={"bout_id": str, "a_id": str, "b_id": str})
    bouts["title"] = bouts["title"].astype(bool)
    stats = pd.read_csv(STATS_PATH, dtype={"bout_id": str})
    fighters = pd.read_csv(FIGHTERS_PATH, parse_dates=["dob"], dtype={"fighter_id": str})
    return bouts, stats, fighters
