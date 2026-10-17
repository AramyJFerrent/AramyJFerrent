"""The in-season update: refresh data, refit, predict, log and grade.

Run it as often as you like (the GitHub Action runs it daily). Each run:

1. Downloads the latest schedule, scores and lines, and this season's
   play-by-play, and rebuilds this season's efficiency summary.
2. Refits the points map, market blend and simulator on recent seasons plus
   every game played so far this season.
3. Predicts every game in the next two weeks that has not kicked off, using
   current lines, projected starting QBs and kickoff wind forecasts.
4. Writes those predictions to the log, overwriting earlier ones for the same
   game, so the logged prediction is always the last one made before kickoff.
5. Fills in final scores for finished games and grades the season so far.
"""

from __future__ import annotations

import datetime as dt
import json
import logging

import numpy as np
import pandas as pd

from . import report
from .config import FIRST_SEASON, OUTPUT_DIR, Hyperparams
from .data import current_season, load_games, load_summaries, update_summaries
from .features import FeatureBuilder
from .model import ScoreModel
from .weather import forecast_wind

log = logging.getLogger(__name__)

LOG_PATH = OUTPUT_DIR / "log.csv"
LATEST_PATH = OUTPUT_DIR / "latest.json"
MODEL_PATH = OUTPUT_DIR / "model.json"
RATINGS_PATH = OUTPUT_DIR / "ratings.csv"
README_PATH = OUTPUT_DIR / "README.md"

LOG_COLUMNS = [
    "game_id", "season", "week", "kickoff", "away_team", "home_team", "away_qb", "home_qb",
    "pred_away", "pred_home", "pred_margin", "pred_total", "model_margin", "model_total",
    "headline_away", "headline_home", "home_win_prob", "away_win_prob", "tie_prob",
    "one_score_prob", "away_low", "away_high", "home_low", "home_high",
    "spread_line", "total_line", "wind_forecast", "elo_spread", "predicted_at", "source",
    "away_score", "home_score",
]


def select_upcoming(games: pd.DataFrame, season: int, now: pd.Timestamp, weeks: int) -> pd.DataFrame:
    """Games in the next ``weeks`` weeks of ``season`` that have not kicked off."""
    pending = games[(games["season"] == season) & ~games["completed"] & (games["kickoff"] > now)]
    keep = sorted(pending["week"].unique())[:weeks]
    return pending[pending["week"].isin(keep)].reset_index(drop=True)


def prediction_rows(feats: pd.DataFrame, preds: pd.DataFrame, wind: pd.Series | None,
                    now: pd.Timestamp) -> pd.DataFrame:
    rows = pd.DataFrame({
        "game_id": feats["game_id"], "season": feats["season"], "week": feats["week"],
        "kickoff": feats["kickoff"], "away_team": feats["away_team"], "home_team": feats["home_team"],
        "away_qb": feats["away_qb_name"], "home_qb": feats["home_qb_name"],
        "pred_away": preds["pred_away"], "pred_home": preds["pred_home"],
        "pred_margin": preds["pred_margin"], "pred_total": preds["pred_total"],
        "model_margin": preds["pred_model_margin"], "model_total": preds["pred_model_total"],
        "spread_line": feats["spread_line"], "total_line": feats["total_line"],
        "wind_forecast": wind if wind is not None else np.nan,
        "elo_spread": feats["elo_spread"], "predicted_at": now, "source": "live",
    })
    for col in ("headline_away", "headline_home", "home_win_prob", "away_win_prob", "tie_prob",
                "one_score_prob", "away_low", "away_high", "home_low", "home_high"):
        rows[col] = preds[col].to_numpy()
    rows["away_score"] = np.nan
    rows["home_score"] = np.nan
    return rows[LOG_COLUMNS]


def load_log() -> pd.DataFrame:
    if not LOG_PATH.exists():
        return pd.DataFrame(columns=LOG_COLUMNS)
    entries = pd.read_csv(LOG_PATH)
    for col in ("kickoff", "predicted_at"):
        entries[col] = pd.to_datetime(entries[col], utc=True)
    if "source" not in entries:
        entries["source"] = "live"
    return entries[LOG_COLUMNS]


def backfill(entries: pd.DataFrame, history: pd.DataFrame, season: int, n_sims: int) -> pd.DataFrame:
    """Walk-forward predictions for this season's finished games the log never saw.

    Used when the predictor starts mid-season, so the season-to-date grading
    has something to show. Each game is predicted from earlier weeks only, with
    the points map and blend fitted on earlier seasons; these rows use closing
    lines and actual starters, so they are marked ``backfill``, not ``live``.
    """
    done = history[(history["season"] == season) & history["completed"]
                   & ~history["game_id"].isin(entries["game_id"])].reset_index(drop=True)
    past = history[history["season"] < season]
    if done.empty or past.empty:
        return pd.DataFrame(columns=LOG_COLUMNS)
    preds = ScoreModel.fit(past).predict(done, n_sims=n_sims, seed=season)
    rows = prediction_rows(done, preds, None, pd.NaT)
    rows["source"] = "backfill"
    return rows


def update_log(entries: pd.DataFrame, new: pd.DataFrame, games: pd.DataFrame) -> pd.DataFrame:
    """Upsert pre-kickoff predictions and attach final scores."""
    kept = entries[~entries["game_id"].isin(new["game_id"])]
    merged = pd.concat([kept, new], ignore_index=True) if len(kept) else new.copy()
    final = games[games["completed"]].set_index("game_id")
    done = merged["game_id"].isin(final.index)
    merged.loc[done, "home_score"] = merged.loc[done, "game_id"].map(final["home_score"])
    merged.loc[done, "away_score"] = merged.loc[done, "game_id"].map(final["away_score"])
    return merged.sort_values(["kickoff", "game_id"], ignore_index=True)[LOG_COLUMNS]


def power_ratings(ratings, model: ScoreModel, fb: FeatureBuilder) -> pd.DataFrame:
    """Ratings in points per game against an average opponent."""
    table = ratings.table()
    table["off_pts"] = model.coef["off"] * table["off"]
    table["def_pts"] = -model.coef["def_opp"] * table["def"]
    table["net_pts"] = table["off_pts"] + table["def_pts"]
    table["elo"] = table["team"].map(fb.elo_ratings)
    return table.sort_values("net_pts", ascending=False, ignore_index=True)[
        ["team", "net_pts", "off_pts", "def_pts", "elo"]]


def write_if_changed(path, text: str, volatile: tuple[str, ...] = ()) -> bool:
    """Write ``text`` unless it matches the file apart from lines starting with ``volatile``."""
    def stable(t: str) -> list[str]:
        return [line for line in t.splitlines() if not line.lstrip().startswith(volatile)]
    if path.exists() and stable(path.read_text()) == stable(text):
        return False
    path.write_text(text)
    return True


def run_update(now: dt.datetime | None = None, weeks: int = 2, n_sims: int = 10000,
               use_weather: bool = True, max_age_hours: float = 1.0) -> pd.DataFrame:
    now = pd.Timestamp(now or dt.datetime.now(dt.timezone.utc))
    hp = Hyperparams.load()
    season = current_season(now.date())
    games = load_games(max_age_hours)
    update_summaries(list(range(FIRST_SEASON, season + 1)), refresh={season}, max_age_hours=max_age_hours)
    team_games, qbs = load_summaries(FIRST_SEASON, season)

    fb = FeatureBuilder(games, team_games, qbs, hp)
    history = fb.walk_forward(range(max(season - hp.fit_window_seasons, FIRST_SEASON + 1), season + 1))
    model = ScoreModel.fit(history)
    log.info("Fitted on %d games; market weight margin %.2f total %.2f",
             model.fit_games, 1 - model.margin_weight, 1 - model.total_weight)

    entries = load_log()
    filled = backfill(entries, history, season, n_sims)
    if len(filled):
        log.info("Backfilled %d finished games from earlier this season", len(filled))
        entries = pd.concat([entries, filled], ignore_index=True) if len(entries) else filled

    upcoming = select_upcoming(games, season, now, weeks)
    feats, ratings = fb.current(upcoming, season)
    wind = None
    if len(upcoming):
        wind = forecast_wind(feats, now.to_pydatetime()) if use_weather else None
        preds = model.predict(feats, n_sims=n_sims, wind=wind)
        new = prediction_rows(feats, preds, wind, now)
    else:
        new = pd.DataFrame(columns=LOG_COLUMNS)
    entries = update_log(entries, new, games)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    entries.to_csv(LOG_PATH, index=False, float_format="%.4f")
    table = power_ratings(ratings, model, fb)
    table.to_csv(RATINGS_PATH, index=False, float_format="%.3f")
    MODEL_PATH.write_text(json.dumps(
        {"hyperparams": hp.__dict__, **model.to_dict()}, indent=2, default=float) + "\n")
    upcoming_rows = new.copy()
    upcoming_rows["kickoff"] = upcoming_rows["kickoff"].astype(str)
    upcoming_rows["predicted_at"] = upcoming_rows["predicted_at"].astype(str)
    latest = json.dumps({
        "generated_at": now.isoformat(),
        "season": season,
        "games": json.loads(upcoming_rows.to_json(orient="records")),
    }, indent=2) + "\n"
    # Timestamps alone are not news: skip rewrites (and commits) when nothing else changed.
    write_if_changed(LATEST_PATH, latest, volatile=('"generated_at"', '"predicted_at"'))
    write_if_changed(README_PATH, report.render(entries, new, table, model, now, season),
                     volatile=("Updated ",))
    return new
