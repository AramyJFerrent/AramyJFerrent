"""Download NHL data and reduce play-by-play to per-game summaries.

Raw play-by-play is about 19 MB a season, so it is downloaded to a local cache
and boiled down to four small CSVs per season that are committed to the repo:

- ``data/games/{season}_games.csv``: the schedule with final scores.
- ``data/games/{season}_teams.csv``: one row per team per game with time on
  ice, expected goals (xG) and goals by strength state, empty-net goals and how
  the game ended.
- ``data/games/{season}_goalies.csv``: one row per goalie per game with
  unblocked shots faced, xG faced and goals allowed, for goals saved above
  expected (GSAx).
- ``data/games/{season}_states.csv``: seconds played and goals scored by
  minute, score and pulled goalie, which the score simulator is fitted on.

Only the current season is re-downloaded on routine updates.
"""

from __future__ import annotations

import datetime as dt
import logging
from pathlib import Path

import numpy as np
import pandas as pd
import requests
from bettingcore import fetch

from .config import (
    CACHE_DIR,
    DISPLAY_TZ,
    FIRST_SEASON,
    GAMES_DIR,
    GOALIE_BOX_URL,
    PBP_URL,
    SCHEDULE_URL,
    TEAM_ALIASES,
)
from .shots import ShotModel, shot_events

log = logging.getLogger(__name__)

GAME_COLUMNS = ["game_id", "season", "game_type", "start", "home_team", "away_team",
                "home_score", "away_score", "game_state", "venue"]
TEAM_COLUMNS = [
    "game_id", "season", "game_type", "date", "team", "opp", "home",
    "toi_ev", "xgf_ev", "xga_ev", "gf_ev", "ga_ev",
    "toi_pp", "xgf_pp", "gf_pp", "toi_sh", "xga_sh", "ga_sh",
    "xgf", "xga", "gf", "ga", "reg_gf", "reg_ga", "en_gf", "en_ga",
    "periods", "shootout",
]
GOALIE_COLUMNS = ["game_id", "season", "date", "team", "goalie_id", "goalie_name", "starter",
                  "toi", "shots", "xga", "ga"]
STATE_COLUMNS = ["season", "game_type", "minute", "home_lead", "pulled", "seconds",
                 "home_goals", "away_goals"]
FINAL_STATES = {"OFF", "FINAL"}


def current_season(today: dt.date | None = None) -> int:
    """The NHL season in progress (named by the year it ends), or the next one
    from August, when the new schedule is out."""
    today = today or dt.date.today()
    return today.year + 1 if today.month >= 8 else today.year


def _alias(series: pd.Series) -> pd.Series:
    return series.replace(TEAM_ALIASES)


def load_raw(kind: str, season: int, max_age_hours: float = 6.0) -> pd.DataFrame:
    url, name = {
        "schedule": (SCHEDULE_URL, "nhl_schedule_{season}.parquet"),
        "pbp": (PBP_URL, "play_by_play_lite_{season}.parquet"),
        "goalies": (GOALIE_BOX_URL, "goalie_box_{season}.parquet"),
    }[kind]
    path = fetch(url.format(season=season), CACHE_DIR / name.format(season=season), max_age_hours)
    return pd.read_parquet(path)


def reduce_schedule(raw: pd.DataFrame) -> pd.DataFrame:
    """Regular-season and playoff games in the committed schedule format."""
    s = raw[raw["game_type"].isin(["R", "P"])].copy()
    s["start"] = pd.to_datetime(s["game_time"], utc=True, errors="coerce")
    s["home_team"] = _alias(s["home_team_abbr"])
    s["away_team"] = _alias(s["away_team_abbr"])
    done = s["game_state"].isin(FINAL_STATES)
    s["home_score"] = s["home_score"].where(done)
    s["away_score"] = s["away_score"].where(done)
    s["season"] = s["season"].astype(int)
    return s[GAME_COLUMNS].sort_values(["start", "game_id"]).reset_index(drop=True)


def prepare_games(sched: pd.DataFrame) -> pd.DataFrame:
    """Add the columns the model uses to the committed schedule.

    A game is neutral-site when its venue hosts home games of more than one
    team that season (the international Global Series games); outdoor games
    are played in the home team's market and keep home ice.
    """
    g = sched.copy()
    g["start"] = pd.to_datetime(g["start"], utc=True)
    g["date"] = g["start"].dt.tz_convert(DISPLAY_TZ).dt.date
    g["playoff"] = g["game_type"].eq("P")
    g["completed"] = g["home_score"].notna() & g["away_score"].notna()
    hosts = g.groupby(["season", "venue"])["home_team"].transform("nunique")
    g["neutral"] = hosts.gt(1) & g["venue"].notna()
    return g.sort_values(["start", "game_id"]).reset_index(drop=True)


def _event_state(p: pd.DataFrame) -> pd.DataFrame:
    """Strength, score and pulled-goalie state after each event, from the home side."""
    hs = p["home_skaters"].astype(float)
    as_ = p["away_skaters"].astype(float)
    h_in = p["home_goalie_in"].fillna(1).astype(int).eq(1)
    a_in = p["away_goalie_in"].fillna(1).astype(int).eq(1)
    both = h_in & a_in
    state = np.select([~h_in, ~a_in, both & (hs == 5) & (as_ == 5), both & (hs > as_), both & (hs < as_)],
                      ["home_pulled", "away_pulled", "ev", "home_pp", "home_sh"], "other")
    pulled = np.where(~h_in, "home", np.where(~a_in, "away", "none"))
    return pd.DataFrame({"state": state, "pulled": pulled}, index=p.index)


def summarize_pbp(pbp: pd.DataFrame, goalie_box: pd.DataFrame, model: ShotModel,
                  schedule: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Collapse one season of play-by-play into team-game, goalie-game and state rows."""
    p = pbp[pbp["game_id"].isin(schedule["game_id"])].copy()
    p["home_abbr"] = _alias(p["home_abbr"])
    p["away_abbr"] = _alias(p["away_abbr"])
    p = p.sort_values(["game_id", "event_idx"]).reset_index(drop=True)
    in_play = p["period_type"].ne("SHOOTOUT")
    play = p[in_play].copy()
    play = play.join(_event_state(play))
    nxt = play.groupby("game_id")["game_seconds"].shift(-1)
    play["secs"] = (nxt - play["game_seconds"]).clip(lower=0).fillna(0.0)
    play["reg"] = play["period"] <= 3

    games = (play.groupby("game_id").agg(season=("season", "first"), game_type=("season_type", "first"),
                                         home=("home_abbr", "first"), away=("away_abbr", "first"),
                                         periods=("period", "max"))
             .reset_index())
    starts = pd.to_datetime(schedule.set_index("game_id")["start"], utc=True)
    games["date"] = games["game_id"].map(starts.dt.tz_convert(DISPLAY_TZ).dt.strftime("%Y-%m-%d"))
    so = p[~in_play & p["event_type"].eq("GOAL")].groupby(["game_id", "event_team_type"]).size().unstack()
    so = so.reindex(columns=["home", "away"]).fillna(0)
    games["so_home"] = games["game_id"].map(np.sign(so["home"] - so["away"])).fillna(0).astype(int)

    # Time on ice by state, from the home side.
    toi = play.groupby(["game_id", "state"])["secs"].sum().unstack(fill_value=0.0) / 60.0
    toi = toi.reindex(columns=["ev", "home_pp", "home_sh"], fill_value=0.0)

    shots = shot_events(p)
    shots["xg"] = model.xg(shots)
    shots["xg_adj"] = shots["xg"] * model.score_weight(shots)
    shots["reg"] = shots["period"] <= 3
    rated = ~shots["strength"].isin(["empty_net"])

    def by_side(mask: pd.Series, col: str) -> pd.DataFrame:
        return shots[mask].groupby(["game_id", "side"])[col].sum().unstack().reindex(
            columns=["home", "away"]).fillna(0.0)

    ev = shots["strength"].eq("ev")
    pp = shots["strength"].eq("pp")
    goal = shots["goal"].eq(1)
    parts = {
        "xg_ev": by_side(ev, "xg_adj"), "g_ev": by_side(ev & goal, "goal"),
        "xg_pp": by_side(pp, "xg"), "g_pp": by_side(pp & goal, "goal"),
        "xg_all": by_side(rated, "xg"), "g_all": by_side(rated & goal, "goal"),
        "g_reg": by_side(~shots["strength"].isin(["empty_net", "extra_attacker"]) & goal & shots["reg"], "goal"),
        "g_en": by_side(shots["strength"].eq("empty_net") & goal & shots["reg"], "goal"),
    }

    rows = []
    for side, other, flag in (("home", "away", 1), ("away", "home", 0)):
        t = games.rename(columns={side: "team", other: "opp"})[["game_id", "season", "game_type", "date",
                                                                "team", "opp", "periods"]].copy()
        t["home"] = flag
        gid = t["game_id"]
        t["toi_ev"] = gid.map(toi["ev"]).fillna(0.0)
        pp_col, sh_col = ("home_pp", "home_sh") if side == "home" else ("home_sh", "home_pp")
        t["toi_pp"] = gid.map(toi[pp_col]).fillna(0.0)
        t["toi_sh"] = gid.map(toi[sh_col]).fillna(0.0)
        for name, col_for, col_ag in (("xg_ev", "xgf_ev", "xga_ev"), ("g_ev", "gf_ev", "ga_ev"),
                                      ("xg_all", "xgf", "xga"), ("g_all", "gf", "ga"),
                                      ("g_reg", "reg_gf", "reg_ga"), ("g_en", "en_gf", "en_ga")):
            t[col_for] = gid.map(parts[name][side]).fillna(0.0)
            t[col_ag] = gid.map(parts[name][other]).fillna(0.0)
        t["xgf_pp"] = gid.map(parts["xg_pp"][side]).fillna(0.0)
        t["gf_pp"] = gid.map(parts["g_pp"][side]).fillna(0.0)
        t["xga_sh"] = gid.map(parts["xg_pp"][other]).fillna(0.0)
        t["ga_sh"] = gid.map(parts["g_pp"][other]).fillna(0.0)
        sign = 1 if side == "home" else -1
        t["shootout"] = gid.map(games.set_index("game_id")["so_home"]) * sign
        rows.append(t)
    teams = pd.concat(rows, ignore_index=True)
    teams["season"] = teams["season"].astype(str).str[-4:].astype(int)
    count_cols = ["gf_ev", "ga_ev", "gf_pp", "ga_sh", "gf", "ga", "reg_gf", "reg_ga", "en_gf", "en_ga"]
    teams[count_cols] = teams[count_cols].astype(int)
    teams = teams[TEAM_COLUMNS].sort_values(["date", "game_id", "home"], ascending=[True, True, False])

    goalies = summarize_goalies(shots, goalie_box, games)
    states = summarize_states(play)
    return teams.reset_index(drop=True), goalies, states


def summarize_goalies(shots: pd.DataFrame, box: pd.DataFrame, games: pd.DataFrame) -> pd.DataFrame:
    """Unblocked shots, xG and goals each goalie faced, with box-score starts."""
    b = box[box["game_id"].isin(games["game_id"])].copy()
    b["team"] = _alias(b["team_abbrev"])
    mins = b["toi"].astype(str).str.split(":", expand=True)
    b["toi"] = pd.to_numeric(mins[0], errors="coerce").fillna(0) + \
        pd.to_numeric(mins[1], errors="coerce").fillna(0) / 60.0
    b = b.rename(columns={"player_id": "goalie_id", "player_name": "goalie_name"})
    b["starter"] = b["starter"].fillna(False).astype(bool)

    faced = shots[~shots["strength"].isin(["empty_net", "penalty_shot"])].copy()
    faced["def_side"] = np.where(faced["side"] == "home", "away", "home")
    teams = games.set_index("game_id")
    faced["team"] = np.where(faced["def_side"] == "home", faced["game_id"].map(teams["home"]),
                             faced["game_id"].map(teams["away"]))
    starters = b[b["starter"]].drop_duplicates(["game_id", "team"]).set_index(["game_id", "team"])["goalie_id"]
    fallback = pd.Series(list(zip(faced["game_id"], faced["team"])), index=faced.index).map(starters)
    faced["goalie_id"] = faced["event_goalie_id"].fillna(fallback).astype("Int64")
    # Full names from play-by-play (box scores abbreviate first names).
    names = faced.dropna(subset=["event_goalie_name"]).groupby("event_goalie_id")["event_goalie_name"].agg(
        lambda s: s.mode().iloc[0])
    agg = faced.groupby(["game_id", "team", "goalie_id"]).agg(
        shots=("goal", "size"), xga=("xg", "sum"), ga=("goal", "sum")).reset_index()
    out = b.merge(agg, on=["game_id", "team", "goalie_id"], how="left")
    out = out[(out["toi"] > 0) | out["starter"]]
    out[["shots", "ga"]] = out[["shots", "ga"]].fillna(0).astype(int)
    out["xga"] = out["xga"].fillna(0.0)
    out["goalie_name"] = out["goalie_id"].map(names).fillna(out["goalie_name"])
    out["goalie_id"] = out["goalie_id"].astype("int64")
    out["season"] = out["season"].astype(str).str[-4:].astype(int)
    out["date"] = out["game_id"].map(games.set_index("game_id")["date"])
    return out[GOALIE_COLUMNS].sort_values(["date", "game_id", "team", "starter"],
                                           ascending=[True, True, True, False]).reset_index(drop=True)


def summarize_states(play: pd.DataFrame) -> pd.DataFrame:
    """Seconds and goals by game minute, home lead and pulled goalie.

    Each interval between events carries the state after the earlier event.
    Each goal is counted at the score just before it, with the goalies as
    they were for the goal itself: a pull often has no event of its own, so
    the event before an empty-net goal can still show both goalies in.
    """
    lead = (play["home_score"] - play["away_score"]).clip(-3, 3)
    minute = (play["game_seconds"] // 60).clip(upper=play["period"] * 20 - 1).astype(int)
    base = pd.DataFrame({"season": play["season"].astype(str).str[-4:].astype(int),
                         "game_type": play["season_type"], "minute": minute, "home_lead": lead,
                         "pulled": play["pulled"], "seconds": play["secs"]})
    time_rows = base.groupby(["season", "game_type", "minute", "home_lead", "pulled"])["seconds"].sum()

    prev = play.groupby("game_id")
    before = pd.DataFrame({
        "season": base["season"], "game_type": base["game_type"], "minute": base["minute"],
        "home_lead": (prev["home_score"].shift().fillna(0) - prev["away_score"].shift().fillna(0)).clip(-3, 3),
        "pulled": play["pulled"],
        "home_goals": (play["event_type"].eq("GOAL") & play["event_team_type"].eq("home")).astype(int),
        "away_goals": (play["event_type"].eq("GOAL") & play["event_team_type"].eq("away")).astype(int),
    })
    goals = before[(before["home_goals"] + before["away_goals"]) > 0]
    goal_rows = goals.groupby(["season", "game_type", "minute", "home_lead", "pulled"])[
        ["home_goals", "away_goals"]].sum()
    out = pd.concat([time_rows, goal_rows], axis=1).fillna(0).reset_index()
    out["home_lead"] = out["home_lead"].astype(int)
    out[["home_goals", "away_goals"]] = out[["home_goals", "away_goals"]].astype(int)
    return out[STATE_COLUMNS]


def summary_paths(season: int) -> dict[str, Path]:
    return {kind: GAMES_DIR / f"{season}_{kind}.csv" for kind in ("games", "teams", "goalies", "states")}


def update_summaries(seasons: list[int], refresh: set[int] = frozenset(),
                     max_age_hours: float = 6.0, model: ShotModel | None = None) -> None:
    """Build missing season summaries and rebuild the ones in ``refresh``."""
    GAMES_DIR.mkdir(parents=True, exist_ok=True)
    for season in seasons:
        paths = summary_paths(season)
        if all(p.exists() for p in paths.values()) and season not in refresh:
            continue
        try:
            sched = reduce_schedule(load_raw("schedule", season, max_age_hours))
        except requests.HTTPError as exc:
            log.info("No schedule for %s yet (%s)", season, exc)
            continue
        sched.to_csv(paths["games"], index=False)
        played = sched[sched["home_score"].notna()]
        if played.empty:
            for kind, cols in (("teams", TEAM_COLUMNS), ("goalies", GOALIE_COLUMNS), ("states", STATE_COLUMNS)):
                pd.DataFrame(columns=cols).to_csv(paths[kind], index=False)
            log.info("Saved the %s schedule; no games played yet", season)
            continue
        try:
            pbp = load_raw("pbp", season, max_age_hours)
            box = load_raw("goalies", season, max_age_hours)
        except requests.HTTPError as exc:
            log.info("No play-by-play for %s yet (%s)", season, exc)
            continue
        model = model or ShotModel.load()
        teams, goalies, states = summarize_pbp(pbp, box, model, played)
        teams.to_csv(paths["teams"], index=False, float_format="%.3f")
        goalies.to_csv(paths["goalies"], index=False, float_format="%.3f")
        states.to_csv(paths["states"], index=False, float_format="%.1f")
        log.info("Summarized %s: %d games, %d goalie-games", season, len(teams) // 2, len(goalies))


def load_summaries(first: int = FIRST_SEASON, last: int | None = None) -> dict[str, pd.DataFrame]:
    """All committed summaries, oldest first, keyed by kind."""
    columns = {"games": GAME_COLUMNS, "teams": TEAM_COLUMNS, "goalies": GOALIE_COLUMNS,
               "states": STATE_COLUMNS}
    frames: dict[str, list] = {k: [] for k in columns}
    for season in range(first, (last or current_season()) + 1):
        for kind, path in summary_paths(season).items():
            if path.exists():
                frames[kind].append(pd.read_csv(path))
    out = {}
    for kind, cols in columns.items():
        parts = [f for f in frames[kind] if len(f)]
        out[kind] = pd.concat(parts, ignore_index=True).reindex(columns=cols) if parts else pd.DataFrame(columns=cols)
    out["games"] = prepare_games(out["games"])
    return out
