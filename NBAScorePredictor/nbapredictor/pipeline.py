"""The in-season update: refresh data, refit, predict, log and grade.

Run it as often as you like (the GitHub Action runs it several times a day,
around the injury report's deadlines). Each run:

1. Downloads this season's schedule, box scores and play-by-play and rebuilds
   this season's summaries.
2. Refits the points map, market blend and simulator on recent seasons plus
   every game played so far this season.
3. Reads lines, the injury report and current rosters from ESPN for the next
   few days of games, and projects each team's lineup and minutes.
4. Predicts every game in that window that has not started, finds any
   betting edge on the spread, moneyline and total from the model's own
   numbers, and writes the predictions to the log, overwriting earlier ones
   for the same game, so the logged prediction (and edge) is always the last
   one made before tip-off.
5. Fills in final scores for finished games and grades the season so far,
   edges included.
"""

from __future__ import annotations

import datetime as dt
import json
import logging

import numpy as np
import pandas as pd

from . import availability as avail
from . import edges, espn, report
from .backtest import devig
from .config import DISPLAY_TZ, ESPN_TEAM_IDS, FIRST_SEASON, OUTPUT_DIR, Hyperparams
from .data import current_season, load_raw, load_summaries, team_code, update_summaries
from .features import FeatureBuilder
from .lines import load_lines
from .model import ScoreModel
from .simulate import cover_prob, line_probs, over_prob

log = logging.getLogger(__name__)

LOG_PATH = OUTPUT_DIR / "log.csv"
LATEST_PATH = OUTPUT_DIR / "latest.json"
MODEL_PATH = OUTPUT_DIR / "model.json"
RATINGS_PATH = OUTPUT_DIR / "ratings.csv"
PLAYERS_PATH = OUTPUT_DIR / "players.csv"
README_PATH = OUTPUT_DIR / "README.md"

LOG_COLUMNS = [
    "game_id", "season", "game_type", "date", "start", "away_team", "home_team",
    "pred_away", "pred_home", "pred_margin", "pred_total", "model_margin", "model_total",
    "headline_away", "headline_home", "home_win_prob", "away_win_prob", "model_home_prob", "ot_prob",
    "away_low", "away_high", "home_low", "home_high",
    "spread", "total", "home_moneyline", "away_moneyline", "market_home_prob", "home_cover_prob", "over_prob",
    "line_source", "away_missing", "home_missing", "away_injury_cost", "home_injury_cost",
    "elo_spread", "elo_home_prob", "predicted_at", "source",
    "first_predicted_at", "first_spread", "first_total", "first_model_margin", "first_model_total",
    "away_score", "home_score", "periods",
    # Prices of each side, and the model's own chances against the line (before blending).
    "home_spread_price", "away_spread_price", "over_price", "under_price",
    "model_home_cover_prob", "model_spread_push_prob", "model_over_prob", "model_total_push_prob",
    *edges.EDGE_COLUMNS, "first_spread_edge_side",
]
# The first prediction made once a line exists, kept so line movement can be
# measured up to tip-off against it.
FIRST_COLUMNS = ["first_predicted_at", "first_spread", "first_total", "first_model_margin", "first_model_total",
                 "first_spread_edge_side"]
PRICE_COLUMNS = ["home_spread_price", "away_spread_price", "over_price", "under_price"]
MODEL_LINE_COLUMNS = ["model_home_cover_prob", "model_spread_push_prob", "model_over_prob", "model_total_push_prob"]
TEXT_COLUMNS = ["first_spread_edge_side"] + [f"{m}_edge_{f}" for m in edges.MARKETS for f in ("pick", "side")]
TIME_COLUMNS = ["start", "predicted_at", "first_predicted_at"]
# A player is listed as missing when he would usually play this much.
MISSING_MINUTES = 12.0


def select_upcoming(games: pd.DataFrame, season: int, now: pd.Timestamp, days: int) -> pd.DataFrame:
    """Games in the next ``days`` game days of ``season`` that have not started."""
    pending = games[(games["season"] == season) & ~games["completed"] & (games["start"] > now)]
    keep = sorted(pending["date"].unique())[:days]
    return pending[pending["date"].isin(keep)].reset_index(drop=True)


def margin_points(model: ScoreModel, feats: pd.DataFrame, side: str, prefix: str = "p") -> np.ndarray:
    """A side's lineup strength turned into points of margin per game: its
    offense through the offense coefficient, its defense through the
    opponent's offense, at the game's expected pace."""
    c = model.eff_coef
    pace = model.model_means(feats)["pace"]
    off = c.get("p_off", 0.0) * feats[f"{prefix}_off_{side}"].to_numpy(float)
    de = c.get("p_def", 0.0) * feats[f"{prefix}_def_{side}"].to_numpy(float)
    return pace / 100.0 * (off - de)


def missing_players(a: pd.DataFrame) -> dict[tuple, str]:
    """The regulars each team will likely be without, with their status."""
    out = {}
    hurt = a[(a["play_prob"] < 0.9) & (a["proj_minutes"] >= MISSING_MINUTES) & a["has_history"]]
    for (gid, team), grp in hurt.groupby(["game_id", "team"]):
        grp = grp.sort_values("proj_minutes", ascending=False)
        out[(gid, team)] = "; ".join(f"{r.name} ({str(r.status).lower()})" for r in grp.itertuples())
    return out


def prediction_rows(feats: pd.DataFrame, preds: pd.DataFrame, own: pd.DataFrame, now: pd.Timestamp) -> pd.DataFrame:
    rows = pd.DataFrame({
        "game_id": feats["game_id"], "season": feats["season"], "game_type": feats["game_type"],
        "date": feats["date"].astype(str), "start": feats["start"],
        "away_team": feats["away_team"], "home_team": feats["home_team"],
        "pred_away": preds["sim_away"].to_numpy(), "pred_home": preds["sim_home"].to_numpy(),
        "pred_margin": (preds["sim_home"] - preds["sim_away"]).to_numpy(), "pred_total": preds["sim_total"].to_numpy(),
        "model_margin": preds["pred_model_margin"].to_numpy(), "model_total": preds["pred_model_total"].to_numpy(),
        "model_home_prob": own["home_win_prob"].to_numpy(),
        "elo_spread": feats["elo_spread"], "elo_home_prob": feats["elo_home_prob"],
        "predicted_at": now, "source": "live",
    })
    for col in ("headline_away", "headline_home", "home_win_prob", "away_win_prob", "ot_prob",
                "away_low", "away_high", "home_low", "home_high"):
        rows[col] = preds[col].to_numpy()
    for col in ("spread", "total", "home_moneyline", "away_moneyline", "line_source", "market_home_prob",
                "home_cover_prob", "over_prob", "away_missing", "home_missing", "away_injury_cost",
                "home_injury_cost", *PRICE_COLUMNS, *MODEL_LINE_COLUMNS):
        rows[col] = feats[col].to_numpy() if col in feats else np.nan
    rows = pd.concat([rows, edges.edge_columns(rows)], axis=1)
    rows["predicted_at"] = pd.to_datetime(rows["predicted_at"], utc=True)
    has_line = rows["spread"].notna()
    rows["first_predicted_at"] = rows["predicted_at"].where(has_line)
    rows["first_spread"] = rows["spread"]
    rows["first_total"] = rows["total"]
    rows["first_model_margin"] = rows["model_margin"].where(has_line)
    rows["first_model_total"] = rows["model_total"].where(has_line)
    rows["first_spread_edge_side"] = rows["spread_edge_side"].where(has_line).astype(object)
    rows["away_score"] = np.nan
    rows["home_score"] = np.nan
    rows["periods"] = np.nan
    return rows[LOG_COLUMNS]


def load_log() -> pd.DataFrame:
    if not LOG_PATH.exists():
        return pd.DataFrame(columns=LOG_COLUMNS)
    entries = pd.read_csv(LOG_PATH)
    for col in LOG_COLUMNS:
        if col not in entries:
            entries[col] = "live" if col == "source" else np.nan
    for col in TIME_COLUMNS:
        entries[col] = pd.to_datetime(entries[col], utc=True, format="ISO8601")
    for col in TEXT_COLUMNS:
        entries[col] = entries[col].astype(object)
    return entries[LOG_COLUMNS]


def backfill(entries: pd.DataFrame, history: pd.DataFrame, season: int, n_sims: int) -> pd.DataFrame:
    """Walk-forward predictions for this season's finished games the log never saw.

    Used when the predictor starts mid-season (or misses a day), so the
    season-to-date grading has something to show, and rebuilt on every run.
    Each game is predicted from earlier days only, with the points map fitted
    on earlier seasons; these rows know who played and use any archived
    closing line, so they are marked ``backfill``, not ``live``.
    """
    done = history[(history["season"] == season) & history["completed"]
                   & ~history["game_id"].isin(entries["game_id"])].reset_index(drop=True)
    past = history[history["season"] < season]
    if done.empty or past.empty:
        return pd.DataFrame(columns=LOG_COLUMNS)
    model = ScoreModel.fit(past)
    preds, _ = model.predict(done, n_sims=n_sims, seed=season)
    own, own_sim = model.predict(done, n_sims=n_sims, seed=season, market=False)
    done = done.copy()
    done["market_home_prob"] = devig(done["home_moneyline"], done["away_moneyline"]) if "home_moneyline" in done \
        else np.nan
    for col, v in line_probs(own_sim, done["spread"], done["total"]).items():
        done[col] = v
    rows = prediction_rows(done, preds, own, pd.NaT)
    rows["source"] = "backfill"
    rows[FIRST_COLUMNS] = np.nan
    rows["first_predicted_at"] = pd.NaT
    return rows


def update_log(entries: pd.DataFrame, new: pd.DataFrame, games: pd.DataFrame) -> pd.DataFrame:
    """Upsert pre-game predictions and attach final scores.

    The latest prediction replaces earlier ones, except for the ``first_*``
    columns, which keep the first prediction that had a betting line.
    """
    if len(new) and len(entries):
        new = new.copy()
        prev = entries.drop_duplicates("game_id", keep="last").set_index("game_id")
        seen = new["game_id"].map(prev["first_spread"]).notna()
        if seen.any():
            for col in FIRST_COLUMNS:
                new.loc[seen, col] = new.loc[seen, "game_id"].map(prev[col])
    kept = entries[~entries["game_id"].isin(new["game_id"])]
    merged = pd.concat([kept, new], ignore_index=True) if len(kept) else new.copy()
    final = games[games["completed"]].set_index("game_id")
    done = merged["game_id"].isin(final.index)
    for col in ("home_score", "away_score", "periods"):
        merged.loc[done, col] = merged.loc[done, "game_id"].map(final[col])
    return merged.sort_values(["start", "game_id"], ignore_index=True)[LOG_COLUMNS]


def power_ratings(fb: FeatureBuilder, model: ScoreModel, season: int, today, strengths: pd.DataFrame) -> pd.DataFrame:
    """Each team's strength in points per 100 possessions against an average
    team on a neutral floor: its efficiency ratings and its healthy roster's
    player ratings, through the fitted points map, plus what today's injury
    report costs it in points of margin."""
    now = fb.ratings_now(season, today)
    eff, pace = now["team"]["eff"], now["team"]["pace"]
    c = model.eff_coef
    table = pd.DataFrame({"team": sorted(eff.off)})
    table["eff_off"] = table["team"].map(eff.off)
    table["eff_def"] = table["team"].map(eff.deff)
    table["pace"] = table["team"].map(lambda t: pace.mu + pace.off.get(t, 0.0) + pace.deff.get(t, 0.0))
    table = table.merge(strengths, on="team", how="left")
    for col in ("p_off", "p_def"):
        mean = table[col].mean()
        table[f"{col}_now"] = table[f"{col}_now"] - mean
        table[col] = table[col] - mean
    table = table.fillna(0.0)
    table["offense"] = c.get("eff_off", 0.0) * table["eff_off"] + c.get("p_off", 0.0) * table["p_off"]
    table["defense"] = -(c.get("eff_def", 0.0) * table["eff_def"] + c.get("p_def", 0.0) * table["p_def"])
    table["net"] = table["offense"] + table["defense"]
    table["net_per_game"] = table["net"] * table["pace"] / 100.0
    lost = c.get("p_off", 0.0) * (table["p_off"] - table["p_off_now"]) \
        - c.get("p_def", 0.0) * (table["p_def"] - table["p_def_now"])
    table["injury_cost"] = lost * table["pace"] / 100.0
    table["elo"] = table["team"].map(fb.elo_ratings)
    return table.sort_values("net", ascending=False, ignore_index=True)[
        ["team", "net", "net_per_game", "offense", "defense", "pace", "injury_cost", "elo"]]


def player_table(fb: FeatureBuilder, season: int, today, rosters: pd.DataFrame | None, top: int = 30) -> pd.DataFrame:
    """The league's highest-rated players with real minutes, and their teams."""
    off, de, _ = fb.ratings_now(season, today)["players"]
    start = pd.Timestamp(today, tz=DISPLAY_TZ).tz_convert("UTC")
    m = fb.minutes[fb.minutes["start"] < start].drop_duplicates("player_id", keep="last").set_index("player_id")
    t = pd.DataFrame({"offense": pd.Series(off), "defense": -pd.Series(de)})
    t["net"] = t["offense"] + t["defense"]
    t["minutes"] = m["exp_after"].reindex(t.index)
    t["team"] = m["team"].reindex(t.index)
    if rosters is not None and len(rosters):
        t["team"] = rosters.drop_duplicates("player_id").set_index("player_id")["team"].reindex(t.index).fillna(t["team"])
    t["name"] = fb.names.reindex(t.index)
    t = t[(t["minutes"] >= 20) & t["name"].notna()]
    return t.sort_values("net", ascending=False).head(top).reset_index(names="player_id")[
        ["player_id", "name", "team", "net", "offense", "defense", "minutes"]]


def write_if_changed(path, text: str, volatile: tuple[str, ...] = ()) -> bool:
    """Write ``text`` unless it matches the file apart from lines starting with ``volatile``."""
    def stable(t: str) -> list[str]:
        return [line for line in t.splitlines() if not line.lstrip().startswith(volatile)]
    if path.exists() and stable(path.read_text()) == stable(text):
        return False
    path.write_text(text)
    return True


def season_roster(season: int, max_age_hours: float) -> pd.DataFrame | None:
    """The season roster sportsdataverse publishes, as a fallback for ESPN's live one."""
    try:
        raw = load_raw("rosters", season, max_age_hours=max(max_age_hours, 12.0))
    except Exception as exc:  # any failure here only loses a fallback
        log.info("No published %s roster (%s)", season, exc)
        return None
    return pd.DataFrame({"team": team_code(raw["team_abbreviation"]),
                         "player_id": pd.to_numeric(raw["athlete_id"], errors="coerce")}).dropna().astype(
        {"player_id": "int64"})


def run_update(now: dt.datetime | None = None, days: int = 2, n_sims: int = 10000,
               use_espn: bool = True, max_age_hours: float = 1.0) -> pd.DataFrame:
    now = pd.Timestamp(now or dt.datetime.now(dt.timezone.utc))
    today = now.tz_convert(DISPLAY_TZ).date()
    hp = Hyperparams.load()
    season = current_season(today)
    refresh = {season} | ({season - 1} if today.month in (7, 8, 9) else set())
    update_summaries(list(range(FIRST_SEASON, season + 1)), refresh=refresh, max_age_hours=max_age_hours)
    summaries = load_summaries(FIRST_SEASON, season)
    games = summaries["games"]

    fb = FeatureBuilder(summaries, hp, load_lines())
    first = max(season - hp.fit_window_seasons, FIRST_SEASON + 1)
    history = fb.walk_forward(range(first, season + 1), until=today)
    model = ScoreModel.fit(history)
    log.info("Fitted on %d games; market weight %.2f on the margin, %.2f on the total; SD %.1f, rho %.2f",
             model.fit_games, 1 - model.margin_weight, 1 - model.total_weight, model.sim.sd, model.sim.rho)

    # Backfilled games are rebuilt every run so they always reflect the current model.
    entries = load_log()
    entries = entries[entries["source"] != "backfill"].reset_index(drop=True)
    filled = backfill(entries, history, season, min(n_sims, 4000))
    if len(filled):
        log.info("Backfilled %d finished games from earlier this season", len(filled))
        entries = pd.concat([entries, filled], ignore_index=True) if len(entries) else filled

    upcoming = select_upcoming(games, season, now, days)
    roster = injuries = None
    if use_espn and len(upcoming):
        roster, roster_injuries = espn.fetch_rosters(ESPN_TEAM_IDS)
        injuries = espn.fetch_injuries(ESPN_TEAM_IDS)
        if injuries is None or injuries.empty:
            injuries = roster_injuries
        log.info("ESPN: %d rostered players, %d on the injury report", len(roster), 0 if injuries is None else len(injuries))
    published = season_roster(season, max_age_hours)
    a = avail.build(upcoming, fb, today, roster, injuries, published)
    strengths = avail.team_strengths(fb, season, today, avail.candidates(fb, today, roster, published), injuries)
    feats, alt = fb.current(upcoming, season, today, a, scenarios={"full": avail.full_strength(a)})
    full = alt["full"]
    if len(upcoming):
        board = espn.fetch_scoreboards(upcoming["date"]) if use_espn else pd.DataFrame(columns=espn.COLUMNS)
        lined = espn.attach_lines(upcoming, board)
        for col in espn.NUMERIC + ["line_source"]:
            feats[col] = lined[col].to_numpy()
        feats["market_home_prob"] = devig(feats["home_moneyline"], feats["away_moneyline"])
        missing = missing_players(a)
        for side in ("home", "away"):
            cost = margin_points(model, full, side) - margin_points(model, feats, side)
            feats[f"{side}_injury_cost"] = cost
            feats[f"{side}_missing"] = [missing.get((g, t)) for g, t in zip(feats["game_id"], feats[f"{side}_team"])]
        preds, sim = model.predict(feats, n_sims=n_sims)
        # The model's own simulation, before blending with the line: its win
        # chance and its chances against the line are what the edges use.
        own, own_sim = model.predict(feats, n_sims=n_sims, market=False)
        spread = feats["spread"].to_numpy(float)
        total = feats["total"].to_numpy(float)
        feats["home_cover_prob"] = np.where(np.isnan(spread), np.nan, cover_prob(sim, np.nan_to_num(spread)))
        feats["over_prob"] = np.where(np.isnan(total), np.nan, over_prob(sim, np.nan_to_num(total)))
        for col, v in line_probs(own_sim, spread, total).items():
            feats[col] = v
        new = prediction_rows(feats, preds, own, now)
    else:
        new = pd.DataFrame(columns=LOG_COLUMNS)
    entries = update_log(entries, new, games)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    entries.to_csv(LOG_PATH, index=False, float_format="%.4f")
    table = power_ratings(fb, model, season, today, strengths)
    table.to_csv(RATINGS_PATH, index=False, float_format="%.3f")
    stars = player_table(fb, season, today, roster)
    stars.to_csv(PLAYERS_PATH, index=False, float_format="%.3f")
    MODEL_PATH.write_text(json.dumps({"hyperparams": hp.__dict__, **model.to_dict()}, indent=2, default=float) + "\n")
    upcoming_rows = new.copy()
    for col in TIME_COLUMNS:
        upcoming_rows[col] = upcoming_rows[col].astype(str)
    latest = json.dumps({
        "generated_at": now.isoformat(),
        "season": season,
        "games": json.loads(upcoming_rows.to_json(orient="records")),
    }, indent=2) + "\n"
    # Timestamps alone are not news: skip rewrites (and commits) when nothing else changed.
    write_if_changed(LATEST_PATH, latest, volatile=('"generated_at"', '"predicted_at"', '"first_predicted_at"'))
    write_if_changed(README_PATH, report.render(entries, new, table, stars, model, now, season),
                     volatile=("Updated ",))
    return new
