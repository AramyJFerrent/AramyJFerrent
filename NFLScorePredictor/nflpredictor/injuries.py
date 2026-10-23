"""Non-quarterback injuries: snap-weighted losses from the weekly injury report.

For each team and week, every player on nflverse's injury report except
quarterbacks (they have their own adjustment, ``qb.py``) counts by his role,
his share of the offense's or the defense's snaps over his last three games
with the team (this season, or last season's at the start), times the chance
a player with his report status sits. Those chances were measured on
2013-2025: Out 99.9%, Doubtful 99.2%, Questionable 33%, Probable 4% (snap
counts start in 2013). The losses are summed by position group, so a team
missing two full-time cornerbacks has a ``back`` loss of 2:

    ol     tackles, guards and centers
    skill  running backs, receivers and tight ends
    front  the defensive line and linebackers
    back   cornerbacks and safeties

A player on injured reserve is no longer on the report, and his recent snap
share is zero, so only fresh absences count: the team ratings already
reflect players who have been out for weeks. The points map weighs each
group (``model.py``). Seasons are summarized into ``data/injuries`` like the
play-by-play, and only the current one is downloaded again.
"""

from __future__ import annotations

import logging

import numpy as np
import pandas as pd
from bettingcore import fetch

from .config import CACHE_DIR, DATA_DIR, TEAM_ALIASES

INJURIES_URL = "https://github.com/nflverse/nflverse-data/releases/download/injuries/injuries_{season}.csv"
SNAPS_URL = "https://github.com/nflverse/nflverse-data/releases/download/snap_counts/snap_counts_{season}.csv"
INJURY_DIR = DATA_DIR / "injuries"
FIRST_INJURY_SEASON = 2013
GROUPS = {
    "ol": {"T", "G", "C", "OL", "OT", "OG"},
    "skill": {"RB", "FB", "HB", "WR", "TE"},
    "front": {"DE", "DT", "NT", "DL", "LB", "OLB", "ILB", "MLB", "EDGE"},
    "back": {"CB", "S", "FS", "SS", "DB", "SAF"},
}
OFFENSE = ("ol", "skill")
LOSS_COLUMNS = [f"inj_{g}" for g in GROUPS]
# Share of players with each report status who sat out, 2013-2025.
MISS_RATE = {"Out": 0.999, "Doubtful": 0.992, "Questionable": 0.33, "Probable": 0.04}
ROLE_GAMES = 3
# Weeks are indexed season * WEEK_SLOTS + week, so last season's games come first.
WEEK_SLOTS = 25

log = logging.getLogger(__name__)


def position_group(position) -> str | None:
    for group, positions in GROUPS.items():
        if position in positions:
            return group
    return None


def _key(names: pd.Series) -> pd.Series:
    """Names reduced to lowercase letters, to join the two sources."""
    return names.astype(str).str.lower().str.replace(r"[^a-z]", "", regex=True)


def roles(snaps: pd.DataFrame) -> pd.DataFrame:
    """Each player-game with the player's position group and his role after it:
    his average snap share (offense for offensive groups, defense otherwise) over his last
    ``ROLE_GAMES`` games with the team."""
    s = snaps.assign(team=snaps["team"].replace(TEAM_ALIASES), key=_key(snaps["player"]),
                     group=snaps["position"].map(position_group), t=snaps["season"] * WEEK_SLOTS + snaps["week"])
    s = s[s["group"].notna()].copy()
    s["share"] = np.where(s["group"].isin(OFFENSE), s["offense_pct"], s["defense_pct"]).astype(float)
    s = s.sort_values(["key", "team", "t"])
    s["role"] = s.groupby(["key", "team"])["share"].transform(lambda x: x.rolling(ROLE_GAMES, min_periods=1).mean())
    return s[["key", "team", "t", "group", "role"]].reset_index(drop=True)


def losses(injuries: pd.DataFrame, snaps: pd.DataFrame) -> pd.DataFrame:
    """Expected snap-share losses by team and week (``LOSS_COLUMNS``), from the injury reports
    and the snap counts of earlier games (about a season back at most)."""
    r = roles(snaps)
    i = injuries[injuries["position"] != "QB"]
    i = i.assign(team=i["team"].replace(TEAM_ALIASES), key=_key(i["full_name"]),
                 t=i["season"] * WEEK_SLOTS + i["week"], miss=i["report_status"].map(MISS_RATE))
    i = i[i["miss"].notna()].sort_values("t")
    if i.empty or r.empty:
        return pd.DataFrame(columns=["season", "week", "team", *LOSS_COLUMNS])
    m = pd.merge_asof(i, r.rename(columns={"t": "role_t"}).sort_values("role_t"), left_on="t", right_on="role_t",
                      by=["key", "team"], allow_exact_matches=False, direction="backward")
    m = m[m["role"].notna() & (m["t"] - m["role_t"] <= WEEK_SLOTS + 5)]
    m = m.assign(loss=m["role"] * m["miss"])
    out = m.pivot_table(index=["season", "week", "team"], columns="group", values="loss", aggfunc="sum")
    out = out.reindex(columns=list(GROUPS)).fillna(0.0).add_prefix("inj_").round(4)
    return out.reset_index()


def _download(url: str, name: str, season: int, max_age_hours: float) -> pd.DataFrame:
    try:
        return pd.read_csv(fetch(url.format(season=season), CACHE_DIR / f"{name}_{season}.csv", max_age_hours))
    except Exception as exc:                       # a season not published yet
        log.warning("No %s for %s: %s", name, season, exc)
        return pd.DataFrame()


def update_losses(seasons, refresh=frozenset(), max_age_hours: float = 6.0) -> None:
    """Write ``data/injuries/{season}.csv`` for every season that lacks one or is in ``refresh``.

    A season's losses need last season's snap counts too, for each player's role in week 1."""
    INJURY_DIR.mkdir(parents=True, exist_ok=True)
    for season in seasons:
        path = INJURY_DIR / f"{season}.csv"
        if season < FIRST_INJURY_SEASON or (path.exists() and season not in refresh):
            continue
        age = max_age_hours if season in refresh else 24.0 * 365
        injuries = _download(INJURIES_URL, "injuries", season, age)
        if injuries.empty:
            continue
        snaps = [_download(SNAPS_URL, "snaps", s, age if s == season else 24.0 * 365) for s in (season - 1, season)]
        snaps = [d for d in snaps if len(d)]
        if not snaps:
            continue
        out = losses(injuries, pd.concat(snaps, ignore_index=True))
        out = out[out["season"] == season]
        out.to_csv(path, index=False)
        log.info("Injury losses for %s: %d team-weeks", season, len(out))


def load_losses(first: int, last: int) -> pd.DataFrame:
    frames = [pd.read_csv(INJURY_DIR / f"{s}.csv") for s in range(first, last + 1)
              if (INJURY_DIR / f"{s}.csv").exists()]
    if not frames:
        return pd.DataFrame(columns=["season", "week", "team", *LOSS_COLUMNS])
    return pd.concat(frames, ignore_index=True)
