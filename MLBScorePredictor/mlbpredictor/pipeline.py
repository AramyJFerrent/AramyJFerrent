"""The in-season update: refresh data, refit, predict, log and grade.

Run it as often as you like (the GitHub Action runs it several times a day).
Each run:

1. Brings this season's games, box scores and players up to date from the
   MLB Stats API (and any newly published Retrosheet season).
2. Refits the run model and the simulator on the last three seasons plus
   every game played so far this season.
3. Reads the next few days of games with their probable pitchers, posted
   lineups and game-time weather, temperature forecasts for the rest, and
   betting lines from ESPN; backs the market's expected runs out of the lines
   and blends them with the model's.
4. Predicts every game in that window that has not started and writes the
   predictions to the log, overwriting earlier ones for the same game, so the
   logged prediction is always the last one made before first pitch.
5. Fills in final scores for finished games and grades the season so far.
"""

from __future__ import annotations

import datetime as dt
import json
import logging

import numpy as np
import pandas as pd

from . import espn, report, statsapi, weather
from .config import DISPLAY_TZ, FIRST_SEASON, OUTPUT_DIR, Hyperparams, current_season
from .data import load_summaries, update_summaries
from .features import SLOTS, FeatureBuilder
from .market import MarketInverter, blend, devig, fit_blend
from .model import RunModel
from .players import season_time
from .simulate import over_prob

log = logging.getLogger(__name__)

LOG_PATH = OUTPUT_DIR / "log.csv"
LATEST_PATH = OUTPUT_DIR / "latest.json"
MODEL_PATH = OUTPUT_DIR / "model.json"
RATINGS_PATH = OUTPUT_DIR / "ratings.csv"
README_PATH = OUTPUT_DIR / "README.md"

LOG_COLUMNS = [
    "game_id", "season", "game_type", "date", "start", "away_team", "home_team",
    "away_starter", "home_starter", "away_lineup", "home_lineup",
    "pred_away", "pred_home", "pred_total", "headline_away", "headline_home",
    "home_win_prob", "away_win_prob", "model_home_prob", "extra_prob", "home_cover_prob", "away_cover_prob",
    "over_prob", "f5_home_win_prob", "f5_tie_prob", "f5_total", "away_low", "away_high", "home_low", "home_high",
    "model_away_runs", "model_home_runs", "market_away_runs", "market_home_runs", "away_runs9", "home_runs9",
    "home_moneyline", "away_moneyline", "total_line", "over_price", "under_price", "market_home_prob",
    "line_source", "elo_home_prob", "temp", "predicted_at", "source",
    "first_predicted_at", "first_home_moneyline", "first_away_moneyline", "first_market_home_prob",
    "first_model_home_prob",
    "away_score", "home_score", "innings",
]
# The first prediction made once a line exists, kept so picks can be graded
# against the opening line and line movement measured up to first pitch.
FIRST_COLUMNS = ["first_predicted_at", "first_home_moneyline", "first_away_moneyline",
                 "first_market_home_prob", "first_model_home_prob"]
TIME_COLUMNS = ["start", "predicted_at", "first_predicted_at"]
LINE_COLUMNS = ["home_moneyline", "away_moneyline", "total_line", "over_price", "under_price", "line_source"]


def select_upcoming(games: pd.DataFrame, season: int, now: pd.Timestamp, days: int) -> pd.DataFrame:
    """Games in the next ``days`` game days of ``season`` that have not started."""
    pending = games[(games["season"] == season) & ~games["completed"] & games["status"].eq("scheduled")
                    & (games["start"] > now)]
    keep = sorted(pending["date"].unique())[:days]
    return pending[pending["date"].isin(keep)].reset_index(drop=True)


def lineup_frame(fresh: pd.DataFrame) -> pd.DataFrame:
    """Posted lineups from the schedule as rows indexed by (game_id, team)."""
    rows = []
    for g in fresh.itertuples(index=False):
        for side in ("home", "away"):
            ids = list(getattr(g, f"{side}_lineup_ids", []) or [])
            pos = list(getattr(g, f"{side}_lineup_pos", []) or [])
            if len(ids) < SLOTS:
                continue
            row = {"game_id": g.game_id, "team": getattr(g, f"{side}_team")}
            for i in range(SLOTS):
                row[f"p{i + 1}"] = ids[i]
                row[f"pos{i + 1}"] = int(pos[i]) if i < len(pos) and str(pos[i]).isdigit() else 0
            rows.append(row)
    cols = ["game_id", "team"] + [f"p{i}" for i in range(1, 10)] + [f"pos{i}" for i in range(1, 10)]
    return pd.DataFrame(rows, columns=cols).set_index(["game_id", "team"])


def refresh_upcoming(games: pd.DataFrame, upcoming: pd.DataFrame, now: pd.Timestamp, use_web: bool):
    """Latest probable pitchers, lineups and weather for the upcoming games.

    Updates ``games`` in place and returns the posted lineups."""
    lineups = lineup_frame(pd.DataFrame())
    if upcoming.empty:
        return lineups
    idx = games.index[games["game_id"].isin(upcoming["game_id"])]
    if use_web:
        try:
            fresh = statsapi.fetch_schedule(upcoming["date"].min(), upcoming["date"].max(),
                                            hydrate=statsapi.UPCOMING_HYDRATE)
        except Exception as exc:     # the stored schedule still has the probables
            log.warning("Could not refresh upcoming games: %s", exc)
            fresh = pd.DataFrame()
        if len(fresh):
            fresh = fresh.set_index("game_id")
            ids = games.loc[idx, "game_id"]
            for side in ("home", "away"):
                new = ids.map(fresh[f"{side}_starter"])
                games.loc[idx, f"{side}_starter"] = new.where(new.notna(), games.loc[idx, f"{side}_starter"])
            for col in ("temp", "dome", "wind", "wind_speed"):
                new = ids.map(fresh[col])
                games.loc[idx, col] = new.where(new.notna(), games.loc[idx, col])
            lineups = lineup_frame(fresh.reset_index())
        need = games.loc[idx][games.loc[idx, "temp"].isna() & games.loc[idx, "dome"].ne(1)]
        if len(need):
            fc = weather.forecast(need, now)
            games.loc[fc.index, "temp"] = fc["temp"]
            games.loc[fc.index, "dome"] = games.loc[fc.index, "dome"].fillna(0).where(fc["dome"].eq(0), 1)
    log.info("Lineups posted for %d of %d teams", len(lineups), 2 * len(upcoming))
    return lineups


def prediction_rows(feats: pd.DataFrame, preds: pd.DataFrame, model_only: pd.DataFrame, names: pd.Series,
                    now: pd.Timestamp) -> pd.DataFrame:
    rows = pd.DataFrame({
        "game_id": feats["game_id"], "season": feats["season"], "game_type": feats["game_type"],
        "date": feats["date"].astype(str), "start": feats["start"],
        "away_team": feats["away_team"], "home_team": feats["home_team"],
        "away_starter": feats["away_starter"].map(names).fillna(feats["away_starter"]).fillna("TBD"),
        "home_starter": feats["home_starter"].map(names).fillna(feats["home_starter"]).fillna("TBD"),
        "away_lineup": feats["away_lineup"], "home_lineup": feats["home_lineup"],
        "pred_away": preds["sim_away"], "pred_home": preds["sim_home"], "pred_total": preds["sim_total"],
        "model_home_prob": model_only["home_win_prob"], "elo_home_prob": feats["elo_home_prob"],
        "temp": np.where(feats["dome"].fillna(0).astype(bool), np.nan, pd.to_numeric(feats["temp"], errors="coerce")),
        "predicted_at": now, "source": "live",
    })
    for col in ("headline_away", "headline_home", "home_win_prob", "away_win_prob", "extra_prob", "home_cover_prob",
                "away_cover_prob", "f5_home_win_prob", "f5_tie_prob", "f5_total", "away_low", "away_high",
                "home_low", "home_high", "model_away_runs", "model_home_runs", "away_runs9", "home_runs9"):
        rows[col] = preds[col].to_numpy()
    for col in ("market_away_runs", "market_home_runs", "market_home_prob", "over_prob") + tuple(LINE_COLUMNS):
        rows[col] = feats[col].to_numpy() if col in feats else np.nan
    rows["predicted_at"] = pd.to_datetime(rows["predicted_at"], utc=True)
    has_line = rows["home_moneyline"].notna()
    rows["first_predicted_at"] = rows["predicted_at"].where(has_line)
    rows["first_home_moneyline"] = rows["home_moneyline"]
    rows["first_away_moneyline"] = rows["away_moneyline"]
    rows["first_market_home_prob"] = rows["market_home_prob"]
    rows["first_model_home_prob"] = rows["model_home_prob"].where(has_line)
    rows["away_score"] = np.nan
    rows["home_score"] = np.nan
    rows["innings"] = np.nan
    return rows[LOG_COLUMNS]


def load_log() -> pd.DataFrame:
    if not LOG_PATH.exists():
        return pd.DataFrame(columns=LOG_COLUMNS)
    entries = pd.read_csv(LOG_PATH, dtype={"game_id": str})
    for col in LOG_COLUMNS:
        if col not in entries:
            entries[col] = "live" if col == "source" else np.nan
    for col in TIME_COLUMNS:
        entries[col] = pd.to_datetime(entries[col], utc=True, format="ISO8601")
    return entries[LOG_COLUMNS]


def backfill(entries: pd.DataFrame, history: pd.DataFrame, fb: FeatureBuilder, season: int, n_sims: int,
             hp: Hyperparams) -> pd.DataFrame:
    """Walk-forward predictions for this season's finished games the log never saw.

    Used when the predictor starts mid-season (or misses a game), so the
    season-to-date grading has something to show. Each game is predicted
    from earlier days only, with the run model fitted on earlier seasons;
    these rows use the actual lineups and starters and no betting line, so
    they are marked ``backfill``, not ``live``. Once written they are kept,
    so the log only changes where there is news.
    """
    done = history[(history["season"] == season) & history["completed"]
                   & ~history["game_id"].isin(entries["game_id"])].reset_index(drop=True)
    past = history[history["season"].between(season - hp.fit_window_seasons, season - 1)]
    if done.empty or past.empty:
        return pd.DataFrame(columns=LOG_COLUMNS)
    model = RunModel.fit(past, fb.chain(season))
    preds, _ = model.predict(done, n_sims=n_sims, seed=season)
    rows = prediction_rows(done, preds, preds, fb.names, pd.NaT)
    rows["source"] = "backfill"
    rows[FIRST_COLUMNS[1:]] = np.nan
    return rows


def update_log(entries: pd.DataFrame, new: pd.DataFrame, games: pd.DataFrame) -> pd.DataFrame:
    """Upsert pregame predictions and attach final scores.

    The latest prediction replaces earlier ones, except for the ``first_*``
    columns, which keep the first prediction that had a betting line.
    """
    if len(new) and len(entries):
        new = new.copy()
        prev = entries.drop_duplicates("game_id", keep="last").set_index("game_id")
        seen = new["game_id"].map(prev["first_home_moneyline"]).notna()
        if seen.any():
            for col in FIRST_COLUMNS:
                new.loc[seen, col] = new.loc[seen, "game_id"].map(prev[col])
    kept = entries[~entries["game_id"].isin(new["game_id"])]
    merged = pd.concat([kept, new], ignore_index=True) if len(kept) else new.copy()
    final = games[games["completed"]].set_index("game_id")
    done = merged["game_id"].isin(final.index)
    for col in ("home_score", "away_score", "innings"):
        merged.loc[done, col] = merged.loc[done, "game_id"].map(final[col])
    # Games called off before they were played leave the log.
    gone = games[games["status"].eq("postponed")]["game_id"]
    merged = merged[~(merged["game_id"].isin(gone) & merged["home_score"].isna())]
    return merged.sort_values(["start", "game_id"], ignore_index=True)[LOG_COLUMNS]


def write_if_changed(path, text: str, volatile: tuple[str, ...] = ()) -> bool:
    """Write ``text`` unless it matches the file apart from lines starting with ``volatile``."""
    def stable(t: str) -> list[str]:
        return [line for line in t.splitlines() if not line.lstrip().startswith(volatile)]
    if path.exists() and stable(path.read_text()) == stable(text):
        return False
    path.write_text(text)
    return True


def first_eight(games: pd.DataFrame) -> pd.DataFrame:
    """Each finished game's runs in innings 1-8 (both teams always bat them)."""
    out = {}
    for side in ("home", "away"):
        n = games["sched_innings"].fillna(9).astype(int) - 1
        out[f"{side}_r8"] = [sum(int(v) for v in str(line).split()[:k] if v != "x")
                             for line, k in zip(games[f"{side}_line"], n)]
    return pd.DataFrame(out, index=games["game_id"]).where(games.set_index("game_id")["completed"])


def blend_weight(entries: pd.DataFrame, games: pd.DataFrame, hp: Hyperparams) -> tuple[float, int]:
    """Weight on the model from logged live games with a line, shrunk toward the backtest's."""
    e = entries[(entries["source"] == "live") & entries["market_home_runs"].notna()]
    e = e.join(first_eight(games[games["game_id"].isin(e["game_id"])]), on="game_id")
    _, weight, n = fit_blend(e["model_home_runs"], e["model_away_runs"], e["market_home_runs"],
                             e["market_away_runs"], e["home_r8"], e["away_r8"], prior=hp.market_weight)
    return weight, n


def run_update(now: dt.datetime | None = None, days: int = 2, n_sims: int = 10000,
               use_web: bool = True) -> pd.DataFrame:
    now = pd.Timestamp(now or dt.datetime.now(dt.timezone.utc))
    today = now.tz_convert(DISPLAY_TZ).date()
    hp = Hyperparams.load()
    season = current_season(today)
    if use_web:
        update_summaries(season)
    summaries = load_summaries(FIRST_SEASON, season)
    games = summaries["games"]

    upcoming = select_upcoming(games, season, now, days)
    lineups = refresh_upcoming(games, upcoming, now, use_web)
    fb = FeatureBuilder(summaries, hp)
    first = max(season - hp.fit_window_seasons, FIRST_SEASON + 1)
    hist_games = games[games["season"].between(first, season) & games["completed"]
                       & (pd.to_datetime(games["date"]) < pd.Timestamp(today))]
    history = fb.build(hist_games)
    model = RunModel.fit(history, fb.chain(season))
    log.info("Fitted on %d games; game spread %.0f, closer effect %.2f, walk-off home runs %.0f%%",
             model.fit_games, model.sim.frailty, model.sim.closer_mult, 100 * model.sim.walkoff_hr)

    entries = load_log()
    filled = backfill(entries, history, fb, season, min(n_sims, 2000), hp)
    if len(filled):
        log.info("Backfilled %d finished games from earlier this season", len(filled))
        entries = pd.concat([entries, filled], ignore_index=True) if len(entries) else filled

    weight, n_lined = blend_weight(entries, games, hp)
    upcoming = games[games["game_id"].isin(upcoming["game_id"])].reset_index(drop=True)
    if len(upcoming):
        board = espn.fetch_scoreboards(upcoming["date"]) if use_web else pd.DataFrame(columns=espn.COLUMNS)
        lined = espn.attach(upcoming, board)
        feats = fb.build(upcoming, lineups=lineups)
        for col in LINE_COLUMNS:
            feats[col] = lined[col].to_numpy()
        own = model.expected_runs(feats)
        feats["market_home_runs"] = np.nan
        feats["market_away_runs"] = np.nan
        feats["market_home_prob"] = devig(feats["home_moneyline"], feats["away_moneyline"])
        if feats["home_moneyline"].notna().any():
            profile = np.exp(np.asarray(model.inning))
            for ghost in (True, False):
                rows = (feats["tiebreaker"].fillna(0).astype(int) == 1).to_numpy() == ghost
                if not rows.any() or not feats.loc[rows, "home_moneyline"].notna().any():
                    continue
                market = MarketInverter(model.sim, profile, ghost=ghost).rates(feats[rows])
                feats.loc[rows, "market_home_runs"] = market["market_home_runs"].to_numpy()
                feats.loc[rows, "market_away_runs"] = market["market_away_runs"].to_numpy()
        home = blend(own["home"], feats["market_home_runs"], weight)
        away = blend(own["away"], feats["market_away_runs"], weight)
        preds, sim = model.predict(feats, home / own["home"], away / own["away"], n_sims=n_sims)
        lines = feats["total_line"].to_numpy(float)
        feats["over_prob"] = np.where(np.isnan(lines), np.nan, over_prob(sim, np.nan_to_num(lines)))
        has = feats["market_home_runs"].notna().to_numpy()
        model_only = preds
        if has.any():
            model_only, _ = model.predict(feats, n_sims=n_sims)
            # Games without a line were never blended: keep one set of numbers for them.
            model_only.loc[~has, "home_win_prob"] = preds.loc[~has, "home_win_prob"]
        new = prediction_rows(feats, preds, model_only, fb.names, now)
    else:
        new = pd.DataFrame(columns=LOG_COLUMNS)
    entries = update_log(entries, new, games)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    entries.to_csv(LOG_PATH, index=False, float_format="%.4f")
    table = power_ratings(fb, model, season, today)
    table.to_csv(RATINGS_PATH, index=False, float_format="%.3f")
    MODEL_PATH.write_text(json.dumps(
        {"hyperparams": hp.__dict__, "blend_weight": weight, "blend_games": n_lined, **model.to_dict()},
        indent=2, default=float) + "\n")
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
    next_game = games[(games["season"] >= season) & games["status"].eq("scheduled")]["date"].min()
    write_if_changed(README_PATH, report.render(entries, new, table, model, weight, n_lined, now, season, next_game),
                     volatile=("Updated ",))
    return new


def power_ratings(fb: FeatureBuilder, model: RunModel, season: int, today) -> pd.DataFrame:
    """Runs per game better than an average team, by unit, from the fitted run model.

    Offense is the latest lineup against average pitching; run prevention
    splits between the rotation (weighted by how deep its starters go) and
    the bullpen; the team rating adds what the player ratings miss."""
    t = fb.team_table(season, today)
    if t.empty:
        return t
    c = model.coef
    base = 9 * float(fb.environment(season_time([today], [season]))[0])
    share = np.clip(t["rotation_outs"] / 27.0, 0, 1)
    out = pd.DataFrame({"team": t["team"]})
    out["offense"] = base * (np.exp(c["x_sp"] * t["lineup_x"] + c.get("team_off", 0.0) * t["team_off"]) - 1)
    out["rotation"] = -base * share * (np.exp(c["x_sp"] * t["rotation_x"]) - 1)
    out["bullpen"] = -base * (1 - share) * (np.exp(c["x_bp"] * t["bullpen_x"]) - 1)
    out["fielding_etc"] = -base * (np.exp(c.get("team_def", 0.0) * t["team_def"]) - 1)
    out["net"] = out[["offense", "rotation", "bullpen", "fielding_etc"]].sum(axis=1)
    out["starter_innings"] = t["rotation_outs"] / 3.0
    out["elo"] = t["elo"]
    return out.sort_values("net", ascending=False, ignore_index=True)
