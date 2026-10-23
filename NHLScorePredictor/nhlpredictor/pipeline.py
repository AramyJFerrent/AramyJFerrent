"""The in-season update: refresh data, refit, predict, log and grade.

Run it as often as you like (the GitHub Action runs it several times a day).
Each run:

1. Downloads this season's schedule, play-by-play and goalie box scores and
   rebuilds this season's summaries.
2. Refits the goal-rate model and the simulator on recent seasons plus every
   game played so far this season.
3. Fetches lines and probable starting goalies from ESPN for the next few
   days of games, backs the market's goal rates out of the lines and blends
   them with the model's.
4. Predicts every game in that window that has not started, prices the puck
   line, moneyline and total with the model's own (unblended) numbers to find
   betting edges, and writes the predictions to the log, overwriting earlier
   ones for the same game, so the logged prediction and edges are always the
   last ones made before puck drop.
5. Fills in final scores for finished games and grades the season so far,
   edges included.
"""

from __future__ import annotations

import datetime as dt
import json
import logging

import numpy as np
import pandas as pd
from bettingcore import write_if_changed

from . import espn, report
from .config import DISPLAY_TZ, FIRST_SEASON, OUTPUT_DIR, Hyperparams
from .data import current_season, load_summaries, update_summaries
from .edges import EDGE_COLUMNS, add_edges, puck_line
from .features import FeatureBuilder
from .goalies import SHOTS_PER_GAME, day_index
from .market import EDGE_PROBS, MarketInverter, devig, edge_chances, fit_blend
from .model import GoalModel
from .simulate import line_probs, over_prob

log = logging.getLogger(__name__)

LOG_PATH = OUTPUT_DIR / "log.csv"
LATEST_PATH = OUTPUT_DIR / "latest.json"
MODEL_PATH = OUTPUT_DIR / "model.json"
RATINGS_PATH = OUTPUT_DIR / "ratings.csv"
README_PATH = OUTPUT_DIR / "README.md"

LOG_COLUMNS = [
    "game_id", "season", "game_type", "date", "start", "away_team", "home_team",
    "away_goalie", "home_goalie", "away_goalie_status", "home_goalie_status",
    "pred_away", "pred_home", "pred_total", "headline_away", "headline_home",
    "home_win_prob", "away_win_prob", "model_home_prob", "home_reg_win_prob", "away_reg_win_prob",
    "ot_prob", "home_cover_prob", "away_cover_prob", "over_prob",
    "model_home_cover_prob", "model_away_cover_prob", "model_spread_push_prob",
    "model_over_prob", "model_under_prob", "model_total_push_prob",
    "away_low", "away_high", "home_low", "home_high",
    "model_away_rate", "model_home_rate", "market_away_rate", "market_home_rate", "away_rate", "home_rate",
    "home_moneyline", "away_moneyline", "total_line", "over_price", "under_price", "market_home_prob",
    "home_spread_line", "home_spread_price", "away_spread_price", *EDGE_PROBS,
    "line_source", "elo_home_prob", *EDGE_COLUMNS, "predicted_at", "source",
    "first_predicted_at", "first_home_moneyline", "first_away_moneyline", "first_market_home_prob",
    "first_model_home_prob",
    "away_score", "home_score", "result",
]
# The first prediction made once a line exists, kept so picks can be graded
# against the opening line and line movement measured up to puck drop.
FIRST_COLUMNS = ["first_predicted_at", "first_home_moneyline", "first_away_moneyline",
                 "first_market_home_prob", "first_model_home_prob"]
TIME_COLUMNS = ["start", "predicted_at", "first_predicted_at"]
# Model-only (before blending) chances at the posted puck line and total, for comparison; the
# edges use the final prediction's anchored chances (``EDGE_PROBS``).
LINE_PROB_COLUMNS = ["model_home_cover_prob", "model_away_cover_prob", "model_spread_push_prob",
                     "model_over_prob", "model_under_prob", "model_total_push_prob"]


def select_upcoming(games: pd.DataFrame, season: int, now: pd.Timestamp, days: int) -> pd.DataFrame:
    """Games in the next ``days`` game days of ``season`` that have not started."""
    pending = games[(games["season"] == season) & ~games["completed"] & (games["start"] > now)]
    keep = sorted(pending["date"].unique())[:days]
    return pending[pending["date"].isin(keep)].reset_index(drop=True)


def result_label(periods, shootout) -> str | None:
    if pd.isna(periods):
        return None
    if shootout and not pd.isna(shootout) and int(shootout) != 0:
        return "SO"
    return "OT" if int(periods) > 3 else "REG"


def prediction_rows(feats: pd.DataFrame, preds: pd.DataFrame, model_only: pd.DataFrame,
                    now: pd.Timestamp, line_chances: pd.DataFrame | None = None) -> pd.DataFrame:
    """Log rows for predicted games. ``model_only`` and ``line_chances`` are the
    model's own numbers before blending, shown for comparison; the betting edges
    are priced from the anchored chances in ``feats`` (``EDGE_PROBS``)."""
    rows = pd.DataFrame({
        "game_id": feats["game_id"], "season": feats["season"], "game_type": feats["game_type"],
        "date": feats["date"].astype(str), "start": feats["start"],
        "away_team": feats["away_team"], "home_team": feats["home_team"],
        "away_goalie": feats["away_goalie_name"], "home_goalie": feats["home_goalie_name"],
        "away_goalie_status": feats["away_goalie_status"], "home_goalie_status": feats["home_goalie_status"],
        "pred_away": preds["sim_away"], "pred_home": preds["sim_home"], "pred_total": preds["sim_total"],
        "model_home_prob": model_only["home_win_prob"],
        "elo_home_prob": feats["elo_home_prob"], "predicted_at": now, "source": "live",
    })
    for col in ("headline_away", "headline_home", "home_win_prob", "away_win_prob", "home_reg_win_prob",
                "away_reg_win_prob", "ot_prob", "home_cover_prob", "away_cover_prob", "away_low",
                "away_high", "home_low", "home_high", "model_away_rate", "model_home_rate",
                "away_rate", "home_rate"):
        rows[col] = preds[col].to_numpy()
    for col in ("market_away_rate", "market_home_rate", "home_moneyline", "away_moneyline", "total_line",
                "over_price", "under_price", "market_home_prob", "line_source", "over_prob",
                "home_spread_line", "home_spread_price", "away_spread_price", *EDGE_PROBS):
        rows[col] = feats[col].to_numpy() if col in feats else np.nan
    for col in LINE_PROB_COLUMNS:
        rows[col] = line_chances[col].to_numpy() if line_chances is not None else np.nan
    rows["predicted_at"] = pd.to_datetime(rows["predicted_at"], utc=True)
    has_line = rows["home_moneyline"].notna()
    rows["first_predicted_at"] = rows["predicted_at"].where(has_line)
    rows["first_home_moneyline"] = rows["home_moneyline"]
    rows["first_away_moneyline"] = rows["away_moneyline"]
    rows["first_market_home_prob"] = rows["market_home_prob"]
    rows["first_model_home_prob"] = rows["model_home_prob"].where(has_line)
    rows["away_score"] = np.nan
    rows["home_score"] = np.nan
    rows["result"] = None
    return add_edges(rows)[LOG_COLUMNS]


def load_log() -> pd.DataFrame:
    if not LOG_PATH.exists():
        return pd.DataFrame(columns=LOG_COLUMNS)
    entries = pd.read_csv(LOG_PATH)
    for col in LOG_COLUMNS:
        if col not in entries:
            entries[col] = "live" if col == "source" else np.nan
    for col in TIME_COLUMNS:
        entries[col] = pd.to_datetime(entries[col], utc=True, format="ISO8601")
    return entries[LOG_COLUMNS]


def backfill(entries: pd.DataFrame, history: pd.DataFrame, states: pd.DataFrame, season: int,
             n_sims: int) -> pd.DataFrame:
    """Walk-forward predictions for this season's finished games the log never saw.

    Used when the predictor starts mid-season, so the season-to-date grading
    has something to show, and rebuilt on every run. Each game is predicted
    from earlier days only, with the goal-rate model fitted on earlier
    seasons; these rows use the actual starting goalies and no betting line,
    so they are marked ``backfill``, not ``live``.
    """
    done = history[(history["season"] == season) & history["completed"]
                   & ~history["game_id"].isin(entries["game_id"])].reset_index(drop=True)
    past = history[history["season"] < season]
    if done.empty or past.empty:
        return pd.DataFrame(columns=LOG_COLUMNS)
    model = GoalModel.fit(past, states[states["season"] < season])
    preds, _ = model.predict(done, n_sims=n_sims, seed=season)
    rows = prediction_rows(done, preds, preds, pd.NaT)
    rows["source"] = "backfill"
    rows[FIRST_COLUMNS[1:]] = np.nan
    return rows


def update_log(entries: pd.DataFrame, new: pd.DataFrame, games: pd.DataFrame,
               outcomes: pd.DataFrame | None = None) -> pd.DataFrame:
    """Upsert pre-game predictions and attach final scores.

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
    if done.any():
        merged.loc[done, "home_score"] = merged.loc[done, "game_id"].map(final["home_score"])
        merged.loc[done, "away_score"] = merged.loc[done, "game_id"].map(final["away_score"])
    if outcomes is not None and len(outcomes):
        labels = pd.Series([result_label(p, s) for p, s in zip(outcomes["periods"], outcomes["shootout"])],
                           index=outcomes.index)
        merged["result"] = merged["game_id"].map(labels).where(done, merged["result"])
    return merged.sort_values(["start", "game_id"], ignore_index=True)[LOG_COLUMNS]


def power_ratings(feats_ratings: dict, model: GoalModel, fb: FeatureBuilder, env: float) -> pd.DataFrame:
    """Goals per game better than an average team, from the fitted goal-rate model."""
    c = model.coef
    teams = sorted(feats_ratings["ev"].off)
    rows = []
    for t in teams:
        off = sum(c.get(f"{n}_off", 0.0) * feats_ratings[n].off.get(t, 0.0) for n in ("ev", "pp", "draw", "goals"))
        deff = sum(c.get(f"{n}_def", 0.0) * feats_ratings[n].deff.get(t, 0.0) for n in ("ev", "pp", "draw", "goals"))
        rows.append({
            "team": t,
            "off_goals": env * (np.exp(off) - 1.0),
            "def_goals": -env * (np.exp(deff) - 1.0),
            "xgf_ev": feats_ratings["ev"].mu + feats_ratings["ev"].off.get(t, 0.0),
            "xga_ev": feats_ratings["ev"].mu + feats_ratings["ev"].deff.get(t, 0.0),
            "pp_xg": feats_ratings["pp"].mu + feats_ratings["pp"].off.get(t, 0.0),
            "pk_xga": feats_ratings["pp"].mu + feats_ratings["pp"].deff.get(t, 0.0),
            "elo": fb.elo_ratings.get(t, np.nan),
        })
    table = pd.DataFrame(rows)
    table["net_goals"] = table["off_goals"] + table["def_goals"]
    return table.sort_values("net_goals", ascending=False, ignore_index=True)[
        ["team", "net_goals", "off_goals", "def_goals", "xgf_ev", "xga_ev", "pp_xg", "pk_xga", "elo"]]


def goalie_table(fb: FeatureBuilder, season: int, today) -> pd.DataFrame:
    """Each team's likeliest starter for its next game, and his value."""
    dix = int(day_index([today])[0])
    values = fb.goalies.values(dix)
    games = fb.games
    ahead = games[(games["season"] == season) & ~games["completed"] & (games["date"] >= today)]
    next_day = pd.concat([ahead[["home_team", "date"]].rename(columns={"home_team": "team"}),
                          ahead[["away_team", "date"]].rename(columns={"away_team": "team"})]
                         ).groupby("team")["date"].min()
    rows = []
    for team in sorted(fb.engines["ev"].sums(season).teams):
        game_day = int(day_index([next_day.get(team, today)])[0])
        probs = fb.goalies.start_probabilities(team, game_day)
        if probs.empty:
            continue
        gid = int(probs.idxmax())
        rows.append({"team": team, "goalie": fb.goalies.names.get(gid, str(gid)),
                     "start_share": float(probs.max()),
                     "gsax_per_100": fb.goalies.value_of(values, gid),
                     "goals_per_game": fb.goalies.value_of(values, gid) * SHOTS_PER_GAME / 100.0})
    return pd.DataFrame(rows).sort_values("gsax_per_100", ascending=False, ignore_index=True) if rows else \
        pd.DataFrame(columns=["team", "goalie", "start_share", "gsax_per_100", "goals_per_game"])


def recent_goalies(fb: FeatureBuilder, today, days: int = 120) -> dict[str, pd.Series]:
    dix = int(day_index([today])[0])
    g = fb.goalies.g[fb.goalies.g["dix"] >= dix - days]
    return {team: grp.drop_duplicates("goalie_id", keep="last").set_index("goalie_id")["goalie_name"]
            for team, grp in g.groupby("team")}


def blend_weight(entries: pd.DataFrame, outcomes: pd.DataFrame) -> tuple[float, int]:
    """Fitted weight on the model, from logged live games that had a line."""
    e = entries[(entries["source"] == "live") & entries["market_home_rate"].notna()]
    e = e.join(outcomes[["home_reg", "away_reg"]], on="game_id")
    return fit_blend(e["model_home_rate"], e["model_away_rate"], e["market_home_rate"], e["market_away_rate"],
                     e["home_reg"], e["away_reg"])


def run_update(now: dt.datetime | None = None, days: int = 3, n_sims: int = 10000,
               use_espn: bool = True, max_age_hours: float = 1.0) -> pd.DataFrame:
    now = pd.Timestamp(now or dt.datetime.now(dt.timezone.utc))
    today = now.tz_convert(DISPLAY_TZ).date()
    hp = Hyperparams.load()
    season = current_season(today)
    refresh = {season} | ({season - 1} if today.month in (8, 9) else set())
    update_summaries(list(range(FIRST_SEASON, season + 1)), refresh=refresh, max_age_hours=max_age_hours)
    summaries = load_summaries(FIRST_SEASON, season)
    games = summaries["games"]

    fb = FeatureBuilder(games, summaries, hp)
    first = max(season - hp.fit_window_seasons, FIRST_SEASON + 1)
    history = fb.walk_forward(range(first, season + 1), until=today)
    model = GoalModel.fit(history, summaries["states"])
    log.info("Fitted on %d games; overtime rate %.3f; score-state exponent %.1f, lead shift %.2f",
             model.fit_games, model.tie_rate, model.sim.gamma, model.sim.lead_shift)

    # Backfilled games are rebuilt every run so they always reflect the current model.
    entries = load_log()
    entries = entries[entries["source"] != "backfill"].reset_index(drop=True)
    filled = backfill(entries, history, summaries["states"], season, min(n_sims, 2000))
    if len(filled):
        log.info("Backfilled %d finished games from earlier this season", len(filled))
        entries = pd.concat([entries, filled], ignore_index=True) if len(entries) else filled

    upcoming = select_upcoming(games, season, now, days)
    weight, n_lined = blend_weight(entries, fb.outcomes)
    if len(upcoming):
        board = espn.fetch_scoreboards(upcoming["date"]) if use_espn else pd.DataFrame(columns=espn.COLUMNS)
        upcoming = espn.attach(upcoming, board, fb.goalies.names, recent_goalies(fb, today))
        feats, ratings = fb.current(upcoming, season, today)
        for side in ("home", "away"):
            src = upcoming[f"{side}_goalie_source"].to_numpy()
            feats[f"{side}_goalie_status"] = np.where(pd.notna(src), src, feats[f"{side}_goalie_status"])
        for col in espn.NUMERIC + ["line_source"]:
            feats[col] = upcoming[col].to_numpy()
        own = model.rates(feats)
        feats["market_home_rate"] = np.nan
        feats["market_away_rate"] = np.nan
        feats["market_home_prob"] = devig(feats["home_moneyline"], feats["away_moneyline"])
        if feats["home_moneyline"].notna().any():
            market = MarketInverter(model.sim).rates(feats)
            feats["market_home_rate"] = market["market_home_rate"].to_numpy()
            feats["market_away_rate"] = market["market_away_rate"].to_numpy()
        has = feats["market_home_rate"].notna().to_numpy()
        home_rate = np.where(has, weight * own["home"] + (1 - weight) * feats["market_home_rate"], own["home"])
        away_rate = np.where(has, weight * own["away"] + (1 - weight) * feats["market_away_rate"], own["away"])
        preds, sim = model.predict(feats, home_rate, away_rate, n_sims=n_sims)
        lines = feats["total_line"].to_numpy(float)
        feats["over_prob"] = np.where(np.isnan(lines), np.nan, over_prob(sim, np.nan_to_num(lines)))
        model_only, model_sim = preds, sim
        if has.any():
            model_only, model_sim = model.predict(feats, n_sims=n_sims)
            # Games without a line were never blended: keep one set of numbers for them.
            model_only.loc[~has, "home_win_prob"] = preds.loc[~has, "home_win_prob"]
        # The model's own chances at the posted puck line (or -1.5 on its favorite, for
        # fair odds, until one is posted) and total, for comparison.
        home_lines = [puck_line(hl, p) for hl, p in zip(feats["home_spread_line"], model_only["home_win_prob"])]
        chances = line_probs(model_sim, home_lines, lines)
        chances.loc[~has] = line_probs(sim, home_lines, lines).loc[~has]
        # The edges' chances: the final prediction anchored to the same simulation at the market's rates.
        ref_home = np.where(has, feats["market_home_rate"], home_rate)
        ref_away = np.where(has, feats["market_away_rate"], away_rate)
        ref, ref_sim = model.predict(feats, ref_home, ref_away, n_sims=n_sims)
        feats[EDGE_PROBS] = edge_chances(feats, preds, sim, ref, ref_sim, feats["home_spread_line"]).to_numpy()
        del ref_sim
        new = prediction_rows(feats, preds, model_only, now, chances)
    else:
        feats, ratings = fb.current(upcoming, season, today)
        new = pd.DataFrame(columns=LOG_COLUMNS)
    entries = update_log(entries, new, games, fb.outcomes)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    entries.to_csv(LOG_PATH, index=False, float_format="%.4f")
    env = fb.scoring_environment(int(day_index([today])[0]))
    table = power_ratings(ratings, model, fb, env)
    table.to_csv(RATINGS_PATH, index=False, float_format="%.3f")
    goalies = goalie_table(fb, season, today)
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
    write_if_changed(README_PATH, report.render(entries, new, table, goalies, model, weight, n_lined, now, season),
                     volatile=("Updated ",))
    return new
