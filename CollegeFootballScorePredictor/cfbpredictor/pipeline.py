"""The in-season update: refresh data, refit, predict, log and grade.

Run it as often as you like (the GitHub Action runs it daily, and several
times on Saturdays). Each run:

1. Downloads the latest schedules and scores, and this season's play-by-play,
   and rebuilds this season's efficiency summary and its betting lines.
2. Rebuilds this season's returning production from the latest rosters,
   until the season's first game is played.
3. Fetches current lines for the games ahead (CFBD with a key, else ESPN).
4. Refits the preseason prior, points map, market blend and simulator on
   recent seasons plus every game played so far this season.
5. Predicts every game in the next two weeks that has not kicked off.
6. Writes those predictions to the log, overwriting earlier ones for the same
   game, so the logged prediction is always the last one made before kickoff.
   Each carries the prices and the model-only chances behind it, and the
   betting edge (if any) in each market, so edges freeze at kickoff too.
7. Fills in final scores for finished games and grades the season so far.
"""

from __future__ import annotations

import datetime as dt
import json
import logging

import numpy as np
import pandas as pd
from bettingcore import TEXT_FIELDS, write_if_changed

from . import report
from .config import ELO_FIRST_SEASON, FIRST_SEASON, OUTPUT_DIR, Hyperparams
from .data import current_season, load_games, load_summaries, update_summaries
from .edges import edge_columns, edge_frame
from .elo import EloParams
from .features import FeatureBuilder
from .lines import load_lines
from .model import EDGE_PROBS, ScoreModel
from .odds import live_lines
from .returning import update_returning
from .travel import load_venues
from .weather import forecast_wind, load_weather, update_weather

log = logging.getLogger(__name__)

LOG_PATH = OUTPUT_DIR / "log.csv"
LATEST_PATH = OUTPUT_DIR / "latest.json"
MODEL_PATH = OUTPUT_DIR / "model.json"
RATINGS_PATH = OUTPUT_DIR / "ratings.csv"
README_PATH = OUTPUT_DIR / "README.md"
# The first season with a preseason prior behind it; earlier ones only seed ratings.
FIRST_FIT_SEASON = FIRST_SEASON + 1

# Posted prices (NaN when not posted), and the final prediction's chances against
# the logged lines (behind each game's betting edges, see edges.py) next to the
# model's own before the blend.
PRICE_COLUMNS = ["home_moneyline", "away_moneyline", "home_spread_price", "away_spread_price", "over_price",
                 "under_price"]
MODEL_PROB_COLUMNS = ["model_home_win_prob", "model_home_cover_prob", "model_spread_push_prob", "model_over_prob",
                      "model_total_push_prob"]
LOG_COLUMNS = [
    "game_id", "season", "week", "kickoff", "start_time_tbd", "away_team", "home_team",
    "away_division", "home_division",
    "neutral", "bowl", "pred_away", "pred_home", "pred_margin", "pred_total", "model_margin", "model_total",
    "headline_away", "headline_home", "home_win_prob", "away_win_prob", "one_score_prob",
    "away_low", "away_high", "home_low", "home_high",
    "spread_line", "total_line", "line_source", "wind_forecast", "elo_spread", "predicted_at", "source",
    "first_predicted_at", "first_spread_line", "first_model_margin",
    "away_score", "home_score",
    *PRICE_COLUMNS, *EDGE_PROBS, *MODEL_PROB_COLUMNS, *edge_columns(),
]
# The first prediction made once a line exists, kept so line movement up to
# kickoff can be measured against the early-week line.
FIRST_COLUMNS = ["first_predicted_at", "first_spread_line", "first_model_margin"]
TIME_COLUMNS = ["kickoff", "predicted_at", "first_predicted_at"]


TEXT_COLUMNS = ["away_team", "home_team", "away_division", "home_division", "line_source", "source",
                *edge_columns(TEXT_FIELDS)]


def _utc(df: pd.DataFrame) -> pd.DataFrame:
    """The log with UTC timestamps (missing ones as NaT) and numeric columns as numbers."""
    df = df.copy()
    for col in TIME_COLUMNS:
        df[col] = pd.to_datetime(df[col], utc=True).astype("datetime64[ns, UTC]")
    for col in edge_columns(TEXT_FIELDS):
        if col in df:
            df[col] = df[col].astype(object).fillna("").astype(str)
    for col in df.columns.difference(TIME_COLUMNS + TEXT_COLUMNS + ["start_time_tbd", "neutral", "bowl"]):
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def select_upcoming(games: pd.DataFrame, season: int, now: pd.Timestamp, weeks: int) -> pd.DataFrame:
    """Games in the next ``weeks`` weeks of ``season`` that have not kicked off."""
    pending = games[(games["season"] == season) & ~games["completed"] & (games["kickoff"] > now)]
    keep = sorted(pending["week"].unique())[:weeks]
    return pending[pending["week"].isin(keep)].reset_index(drop=True)


def prediction_rows(feats: pd.DataFrame, preds: pd.DataFrame, now: pd.Timestamp) -> pd.DataFrame:
    rows = pd.DataFrame({
        "game_id": feats["game_id"].to_numpy(), "season": feats["season"].to_numpy(),
        "week": feats["week"].to_numpy(), "kickoff": feats["kickoff"].to_numpy(),
        "start_time_tbd": feats["start_time_tbd"].astype(bool).to_numpy(),
        "away_team": feats["away_team"].to_numpy(), "home_team": feats["home_team"].to_numpy(),
        "away_division": feats["away_division"].to_numpy(), "home_division": feats["home_division"].to_numpy(),
        "neutral": feats["neutral"].to_numpy(),
        "bowl": feats["bowl"].astype(bool).to_numpy() if "bowl" in feats else False,
        "pred_away": preds["pred_away"].to_numpy(), "pred_home": preds["pred_home"].to_numpy(),
        "pred_margin": preds["pred_margin"].to_numpy(), "pred_total": preds["pred_total"].to_numpy(),
        "model_margin": preds["pred_model_margin"].to_numpy(), "model_total": preds["pred_model_total"].to_numpy(),
        "spread_line": feats["spread_line"].to_numpy(), "total_line": feats["total_line"].to_numpy(),
        "line_source": feats["line_source"].to_numpy() if "line_source" in feats else np.nan,
        "wind_forecast": feats["wind_forecast"].to_numpy(float) if "wind_forecast" in feats else np.nan,
        "elo_spread": feats["elo_spread"].to_numpy(), "predicted_at": now, "source": "live",
    })
    for col in ("headline_away", "headline_home", "home_win_prob", "away_win_prob", "one_score_prob",
                "away_low", "away_high", "home_low", "home_high"):
        rows[col] = preds[col].to_numpy()
    lined = rows["spread_line"].notna()
    rows["first_predicted_at"] = rows["predicted_at"].where(lined)
    rows["first_spread_line"] = rows["spread_line"]
    rows["first_model_margin"] = rows["model_margin"].where(lined)
    rows["away_score"] = np.nan
    rows["home_score"] = np.nan
    for col in PRICE_COLUMNS:
        rows[col] = feats[col].to_numpy(float) if col in feats else np.nan
    for col in EDGE_PROBS + MODEL_PROB_COLUMNS:
        rows[col] = preds[col].to_numpy()
    if len(rows):
        rows[edge_columns()] = edge_frame(rows)
    else:
        rows = rows.reindex(columns=LOG_COLUMNS)
    return _utc(rows[LOG_COLUMNS])


def load_log() -> pd.DataFrame:
    if not LOG_PATH.exists():
        return pd.DataFrame(columns=LOG_COLUMNS)
    entries = pd.read_csv(LOG_PATH)
    for col in LOG_COLUMNS:
        if col not in entries:
            entries[col] = "live" if col == "source" else np.nan
    return _utc(entries[LOG_COLUMNS])


def backfill(entries: pd.DataFrame, history: pd.DataFrame, season: int, n_sims: int) -> pd.DataFrame:
    """Walk-forward predictions for this season's finished games the log never saw.

    Used when the predictor starts mid-season, so the season-to-date grading
    has something to show, and rebuilt on every run. Each game is predicted
    from earlier weeks only, with the points map and blend fitted on earlier
    seasons; these rows use closing lines, so they are marked ``backfill``.
    """
    done = history[(history["season"] == season) & history["completed"]
                   & ~history["game_id"].isin(entries["game_id"])].reset_index(drop=True)
    past = history[history["season"] < season]
    if done.empty or past.empty:
        return pd.DataFrame(columns=LOG_COLUMNS)
    preds = ScoreModel.fit(past).predict(done, n_sims=n_sims, seed=season)
    done = done.assign(line_source="closing line")
    rows = prediction_rows(done, preds, pd.NaT)
    rows["source"] = "backfill"
    rows[FIRST_COLUMNS] = np.nan  # no early-week line was ever seen for these games
    return _utc(rows)


def update_log(entries: pd.DataFrame, new: pd.DataFrame, games: pd.DataFrame) -> pd.DataFrame:
    """Upsert pre-kickoff predictions and attach final scores.

    The latest prediction replaces earlier ones, except for the ``first_*``
    columns, which keep the first prediction that had a betting line.
    """
    entries, new = _utc(entries), _utc(new)
    if len(new) and len(entries):
        prev = entries.drop_duplicates("game_id", keep="last").set_index("game_id")
        seen = new["game_id"].map(prev["first_spread_line"]).notna()
        for col in FIRST_COLUMNS:
            new[col] = new["game_id"].map(prev[col]).where(seen, new[col])
    kept = entries[~entries["game_id"].isin(new["game_id"])]
    merged = pd.concat([kept, new], ignore_index=True) if len(kept) else new.copy()
    final = games[games["completed"]].set_index("game_id")
    done = merged["game_id"].isin(final.index)
    if done.any():
        merged.loc[done, "home_score"] = merged.loc[done, "game_id"].map(final["home_score"])
        merged.loc[done, "away_score"] = merged.loc[done, "game_id"].map(final["away_score"])
    return merged.sort_values(["kickoff", "game_id"], ignore_index=True)[LOG_COLUMNS]


def power_ratings(ratings: dict, model: ScoreModel, fb: FeatureBuilder, season: int) -> pd.DataFrame:
    """FBS ratings in points per game against an average team on a neutral field."""
    table = ratings["epa"].table()
    st = ratings["st"]
    members = fb.members.get(season, {})
    table["conference"] = table["team"].map({t: c for t, (c, _) in members.items()})
    table["division"] = table["team"].map({t: d for t, (_, d) in members.items()})
    table["off_pts"] = model.coef["off"] * table["off"]
    table["def_pts"] = -model.coef["def_opp"] * table["def"]
    table["st_pts"] = (model.coef.get("st", 0.0) * table["team"].map(st.off).fillna(0.0)
                       - model.coef.get("st_opp", 0.0) * table["team"].map(st.deff).fillna(0.0))
    table["elo"] = table["team"].map(fb.elo_ratings)
    # The margin model also leans on Elo; its share is shown as its own column.
    table["elo_pts"] = model.coef.get("elo", 0.0) * table["elo"] / EloParams().elo_per_point
    table = table[table["division"] == "fbs"].copy()
    # Centered on the average FBS team.
    for col in ("off_pts", "def_pts", "st_pts", "elo_pts"):
        table[col] = table[col] - table[col].mean()
    table["net_pts"] = table[["off_pts", "def_pts", "st_pts", "elo_pts"]].sum(axis=1)
    return table.sort_values("net_pts", ascending=False, ignore_index=True)[
        ["team", "conference", "net_pts", "off_pts", "def_pts", "st_pts", "elo_pts", "elo"]]


def with_live_lines(lines: pd.DataFrame, live: pd.DataFrame, upcoming: pd.DataFrame) -> pd.DataFrame:
    """Lines table with the live lines of upcoming games in place of anything older."""
    if live.empty:
        return lines
    live = live.merge(upcoming[["game_id", "season"]], on="game_id")
    rest = lines[~lines["game_id"].isin(live["game_id"])]
    return pd.concat([rest, live.assign(books=0)], ignore_index=True)


def run_update(now: dt.datetime | None = None, weeks: int = 2, n_sims: int = 10000,
               use_live_lines: bool = True, use_weather: bool = True, max_age_hours: float = 1.0) -> pd.DataFrame:
    now = pd.Timestamp(now or dt.datetime.now(dt.timezone.utc))
    hp = Hyperparams.load()
    season = current_season(now.date())
    games = load_games(ELO_FIRST_SEASON, season, max_age_hours)
    update_summaries(list(range(FIRST_SEASON, season + 1)), refresh={season}, max_age_hours=max_age_hours)
    started = bool((games["season"].eq(season) & games["completed"]).any())
    returning = update_returning(season, started, max_age_hours)
    team_games = load_summaries(FIRST_SEASON, season)
    lines = load_lines(ELO_FIRST_SEASON, season)

    upcoming = select_upcoming(games, season, now, weeks)
    live = live_lines(upcoming) if use_live_lines and len(upcoming) else pd.DataFrame()
    lines = with_live_lines(lines, live, upcoming)

    venues = load_venues()
    weather = update_weather(games, venues, now.to_pydatetime()) if use_weather else load_weather()
    fb = FeatureBuilder(games, team_games, returning, lines, venues, hp, weather=weather)
    if len(live):
        source = live.set_index("game_id")["line_source"]
        fb.games["line_source"] = fb.games["game_id"].map(source)
    first_fit = max(season - hp.fit_window_seasons, FIRST_FIT_SEASON)
    history = fb.walk_forward(range(first_fit, season + 1))
    model = ScoreModel.fit(history)
    log.info("Fitted on %d games; market weight margin %.2f total %.2f",
             model.fit_games, 1 - model.margin_weight, 1 - model.total_weight)

    # Backfilled games are rebuilt every run so they always reflect the current model.
    entries = load_log()
    entries = entries[entries["source"] != "backfill"].reset_index(drop=True)
    filled = backfill(entries, history, season, n_sims)
    if len(filled):
        log.info("Backfilled %d finished games from earlier this season", len(filled))
        entries = pd.concat([entries, filled], ignore_index=True) if len(entries) else filled

    feats, ratings = fb.current(upcoming["game_id"], season)
    feats = feats.sort_values(["kickoff", "game_id"]).reset_index(drop=True)
    if len(feats):
        wind = forecast_wind(feats, venues, now.to_pydatetime()) if use_weather else None
        preds = model.predict(feats, n_sims=n_sims, wind=wind)
        new = prediction_rows(feats.assign(wind_forecast=wind if wind is not None else np.nan), preds, now)
    else:
        new = pd.DataFrame(columns=LOG_COLUMNS)
    entries = update_log(entries, new, games)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    entries.to_csv(LOG_PATH, index=False, float_format="%.4f")
    table = power_ratings(ratings, model, fb, season)
    table.to_csv(RATINGS_PATH, index=False, float_format="%.3f")
    MODEL_PATH.write_text(json.dumps(
        {"hyperparams": hp.__dict__, **model.to_dict(),
         "prior": fb.engines["epa"].priors.coefficients(season)}, indent=2, default=float) + "\n")
    upcoming_rows = new.copy()
    for col in ("kickoff", "predicted_at", "first_predicted_at"):
        upcoming_rows[col] = upcoming_rows[col].astype(str)
    latest = json.dumps({
        "generated_at": now.isoformat(),
        "season": season,
        "games": json.loads(upcoming_rows.to_json(orient="records")),
    }, indent=2) + "\n"
    # Timestamps alone are not news: skip rewrites (and commits) when nothing else changed.
    write_if_changed(LATEST_PATH, latest, volatile=('"generated_at"', '"predicted_at"', '"first_predicted_at"'))
    write_if_changed(README_PATH, report.render(entries, new, table, model, now, season),
                     volatile=("Updated ",))
    return new
