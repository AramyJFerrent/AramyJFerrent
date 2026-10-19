"""Who is expected to play in upcoming games, and for how long.

Each team's candidates are its current roster: ESPN's live roster when it can
be read, else the players listed healthy in the team's box scores over the
last month, else (before the season starts) the roster sportsdataverse
publishes for the season. Each candidate's expected
minutes come from his recent games for any team, counting healthy scratches
as zero, so a deep reserve barely moves the team's strength. The injury
report turns each status into a chance of playing; a questionable player
counts with about half his minutes, which weighs the two scenarios by how
likely each is (the report's advice for morning predictions). The team's
total is then rescaled to 240 minutes, so missing minutes go to the players
who are left.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .players import DEBUT_MINUTES

# Chance of playing by injury-report status. The official designations are
# defined by these odds (probable is very likely, questionable uncertain,
# doubtful unlikely); ESPN's "day-to-day" is used for any minor issue.
PLAY_PROB = [
    ("out", 0.0), ("suspen", 0.0), ("injured reserve", 0.0), ("not with team", 0.0),
    ("doubtful", 0.15), ("questionable", 0.55), ("day-to-day", 0.7), ("day to day", 0.7),
    ("game time", 0.55), ("probable", 0.95), ("available", 1.0), ("active", 1.0),
]
RECENT_DAYS = 30
AVAILABILITY_COLUMNS = ["game_id", "team", "player_id", "name", "proj_minutes", "play_prob", "status", "detail"]


def play_probability(status) -> float:
    s = str(status or "").strip().lower()
    if not s:
        return 1.0
    for key, p in PLAY_PROB:
        if key in s:
            return p
    return 0.5


def recent_rosters(fb, today, days: int = RECENT_DAYS) -> pd.DataFrame:
    """Players listed healthy in each team's games over the last ``days`` days,
    dropping anyone whose latest game was for another team."""
    m = fb.minutes
    start = pd.Timestamp(today, tz="America/New_York").tz_convert("UTC")
    recent = m[(m["start"] < start) & (m["start"] >= start - pd.Timedelta(days=days))]
    latest = m[m["start"] < start].sort_values("start").drop_duplicates("player_id", keep="last")
    now_team = latest.set_index("player_id")["team"]
    r = recent.drop_duplicates(["team", "player_id"])[["team", "player_id"]]
    return r[r["player_id"].map(now_team) == r["team"]].reset_index(drop=True)


def candidates(fb, today, roster: pd.DataFrame | None, season_roster: pd.DataFrame | None = None,
               teams=None) -> dict[str, np.ndarray]:
    """Each team's current players: the live roster, else the players listed
    healthy in its games over the last month, else (before it has played)
    the published season roster."""
    recent = recent_rosters(fb, today)
    recent = {t: g["player_id"].astype(int).to_numpy() for t, g in recent.groupby("team")}
    live = {t: g["player_id"].astype(int).to_numpy() for t, g in roster.groupby("team")} \
        if roster is not None and len(roster) else {}
    published = {t: g["player_id"].astype(int).to_numpy() for t, g in season_roster.groupby("team")} \
        if season_roster is not None and len(season_roster) else {}
    teams = teams if teams is not None else sorted(set(recent) | set(live) | set(published))
    out = {}
    for team in teams:
        for source in (live, recent, published):
            ids = source.get(team)
            if ids is not None and len(ids) >= 8:
                break
        else:
            ids = recent.get(team, np.zeros(0, dtype=int))
        out[team] = np.unique(ids)
    return out


def statuses(injuries: pd.DataFrame | None) -> tuple[dict, dict]:
    if injuries is None or injuries.empty:
        return {}, {}
    inj = injuries.dropna(subset=["player_id"]).drop_duplicates("player_id", keep="first")
    ids = inj["player_id"].astype(int)
    return dict(zip(ids, inj["status"])), dict(zip(ids, inj["detail"]))


def build(games: pd.DataFrame, fb, today, roster: pd.DataFrame | None, injuries: pd.DataFrame | None,
          season_roster: pd.DataFrame | None = None) -> pd.DataFrame:
    """Expected players for both sides of each upcoming game."""
    start = pd.Timestamp(today, tz="America/New_York").tz_convert("UTC")
    expected = fb.latest_minutes(start)
    status, detail = statuses(injuries)
    teams = pd.unique(games[["home_team", "away_team"]].to_numpy().ravel())
    team_players = candidates(fb, today, roster, season_roster, teams)
    rows = []
    for g in games.itertuples(index=False):
        for team in (g.home_team, g.away_team):
            for pid in team_players.get(team, []):
                st = status.get(int(pid), "")
                rows.append({"game_id": g.game_id, "team": team, "player_id": int(pid),
                             "name": fb.names.get(int(pid), str(pid)),
                             "proj_minutes": float(expected.get(int(pid), DEBUT_MINUTES)),
                             "play_prob": play_probability(st), "status": st or None,
                             "detail": detail.get(int(pid))})
    return pd.DataFrame(rows, columns=AVAILABILITY_COLUMNS)


def team_strengths(fb, season: int, today, team_players: dict[str, np.ndarray],
                   injuries: pd.DataFrame | None) -> pd.DataFrame:
    """Every team's lineup strength at full strength and with today's injury report."""
    start = pd.Timestamp(today, tz="America/New_York").tz_convert("UTC")
    expected = fb.latest_minutes(start)
    status, _ = statuses(injuries)
    ratings = fb.ratings_now(season, today)["players"]
    rows = []
    for team, ids in team_players.items():
        if not len(ids):
            continue
        mins = np.array([expected.get(int(p), DEBUT_MINUTES) for p in ids], dtype=float)
        probs = np.array([play_probability(status.get(int(p), "")) for p in ids])
        full = fb.strength(ids, mins, ratings)
        now = fb.strength(ids, mins * probs, ratings)
        rows.append({"team": team, "p_off": full[0], "p_def": full[1], "p_off_now": now[0], "p_def_now": now[1]})
    return pd.DataFrame(rows, columns=["team", "p_off", "p_def", "p_off_now", "p_def_now"])


def full_strength(availability: pd.DataFrame) -> pd.DataFrame:
    """The same players with everyone available, for measuring what injuries cost."""
    out = availability.copy()
    out["play_prob"] = 1.0
    return out
