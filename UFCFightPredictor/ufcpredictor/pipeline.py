"""The in-season update: refresh data, refit, predict, log and grade.

Run it as often as you like (the GitHub Action runs it daily, and more often
on fight week). Each run:

1. Downloads the UFCStats scrape and the odds dataset and rebuilds the
   committed tables in ``data/``.
2. Rebuilds every fighter's ratings and profiles from the full history and
   refits the win, calibration, market-blend, method and round models on the
   last ten years, including every fight so far this year.
3. Reads the upcoming cards (UFCStats, ESPN, ``data/manual_card.csv``) and
   predicts every bout that has not started, with current prices.
4. Writes those predictions to the log, with the betting edge on each market
   (moneyline, round total, method; see edges.py) at the prices of the
   moment. A bout's prediction is replaced on every run until its card
   segment starts, then locked, so the logged one (and its edges) is always
   the last made before the fight. Bouts that drop off a card before
   they start (injuries, replacements) are removed, and a replacement bout
   gets its own prediction.
5. Fills in results for finished bouts and grades the year so far,
   including the record of the logged edges.
"""

from __future__ import annotations

import datetime as dt
import json
import logging

import numpy as np
import pandas as pd
from bettingcore import write_if_changed

from . import report
from .cards import fetch_card
from .config import DIVISIONS, OUTPUT_DIR, Hyperparams
from .data import current_year, load_data, refresh_data
from .edges import EDGE_COLUMNS, attach_edges
from .features import FeatureBuilder
from .model import EDGE_CHANCES, METHODS, MODEL_ONLY, FightModel
from .names import match_name, normalize_name, pair_key
from .odds import METHOD_ODDS, ROUND_ODDS, append_odds_log, market_odds

log = logging.getLogger(__name__)

LOG_PATH = OUTPUT_DIR / "log.csv"
LATEST_PATH = OUTPUT_DIR / "latest.json"
MODEL_PATH = OUTPUT_DIR / "model.json"
RATINGS_PATH = OUTPUT_DIR / "ratings.csv"
README_PATH = OUTPUT_DIR / "README.md"

PRED_COLUMNS = (["p_a", "p_model", "p_market", "p_glicko"] + [f"{s}_{m}" for s in "ab" for m in METHODS]
                + ["p_distance"] + [f"r{r}" for r in range(1, 6)] + ["best_side", "best_method", "best_prob"]
                + MODEL_ONLY + EDGE_CHANCES)
# Prices of the props (method of victory, round total) and the model-alone
# over chance at the posted round line; then each market's frozen edge.
PROP_PRICES = [*METHOD_ODDS, *ROUND_ODDS]
LOG_COLUMNS = [
    "bout_key", "event", "order", "date", "start", "division", "rounds", "title", "fighter_a", "fighter_b",
    "a_id", "b_id",
    *PRED_COLUMNS, "odds_a", "odds_b", "odds_source", "elo_prob", "a_age", "b_age",
    "a_fights", "b_fights", "predicted_at", "source",
    "first_predicted_at", "first_odds_a", "first_odds_b", "first_p_model",
    "status", "winner", "method", "end_round",
    *PROP_PRICES, "model_over_prob", *EDGE_COLUMNS, "end_seconds",
]
# The first prediction made once a price exists, kept so the model's early
# view can be compared with where the price moved by fight time.
FIRST_COLUMNS = ["first_predicted_at", "first_odds_a", "first_odds_b", "first_p_model"]
TIME_COLUMNS = ["start", "predicted_at", "first_predicted_at"]
ROUNDED = [c for c in PRED_COLUMNS if c not in ("best_side", "best_method")] + [
    "elo_prob", "a_age", "b_age", "first_p_model", "model_over_prob"] + [
    c for c in EDGE_COLUMNS if c.endswith(("_prob", "_ev"))]
# How far ahead to look for cards. UFC runs most weeks, so this covers the
# next card and usually the one after.
DEFAULT_DAYS = 15


def _identity(df: pd.DataFrame) -> pd.Series:
    """One key per bout across sources: fight date and the pair of names."""
    return pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d") + "|" + \
        pd.Series([pair_key(a, b) for a, b in zip(df["fighter_a"], df["fighter_b"])], index=df.index)


def prediction_rows(feats: pd.DataFrame, preds: pd.DataFrame, now, source: str) -> pd.DataFrame:
    feats = feats.reset_index(drop=True)
    rows = pd.DataFrame({c: feats[c] if c in feats else np.nan for c in LOG_COLUMNS})
    for c in PRED_COLUMNS:
        rows[c] = preds[c].to_numpy()
    rows["predicted_at"] = now
    rows["source"] = source
    has_price = rows["odds_a"].notna()
    rows["first_predicted_at"] = pd.Series(now, index=rows.index).where(has_price)
    rows["first_odds_a"] = rows["odds_a"]
    rows["first_odds_b"] = rows["odds_b"]
    rows["first_p_model"] = rows["p_model"].where(has_price)
    rows["status"] = "upcoming"
    for col in ("winner", "method", "end_round", "end_seconds"):
        rows[col] = np.nan
    for col in ("odds_a", "odds_b", *PROP_PRICES):
        rows[col] = pd.to_numeric(rows[col], errors="coerce")
    return attach_edges(rows)[LOG_COLUMNS]


def load_log() -> pd.DataFrame:
    if not LOG_PATH.exists():
        return pd.DataFrame(columns=LOG_COLUMNS)
    entries = pd.read_csv(LOG_PATH, dtype={"bout_key": str, "a_id": str, "b_id": str})
    for col in LOG_COLUMNS:
        if col not in entries:
            entries[col] = np.nan
    for col in TIME_COLUMNS:
        entries[col] = pd.to_datetime(entries[col], utc=True, format="ISO8601")
    entries["date"] = pd.to_datetime(entries["date"])
    return entries[LOG_COLUMNS]


def update_log(entries: pd.DataFrame, new: pd.DataFrame, card: pd.DataFrame, now: pd.Timestamp) -> pd.DataFrame:
    """Upsert pre-fight predictions; drop unstarted bouts that left their card.

    A logged bout is locked once its start time passes. Before that, a new
    prediction replaces it, except for the ``first_*`` columns, which keep the
    first prediction that had a price. A bout that has not started and is no
    longer on a card that was read this run (same date) was cancelled or
    changed, so it is dropped.
    """
    entries = entries.copy()
    if len(entries):
        entries["_id"] = _identity(entries)
    if len(new):
        new = new.copy()
        new["_id"] = _identity(new)
    locked = entries["start"] <= now if len(entries) else pd.Series(dtype=bool)
    if len(new) and len(entries):
        prev = entries.drop_duplicates("_id", keep="last").set_index("_id")
        # Same orientation as before so the first price stays attached to the right fighter.
        flipped = new["_id"].map(prev["fighter_a"]).notna() & (new["_id"].map(prev["fighter_a"]) != new["fighter_a"])
        seen = new["_id"].map(prev["first_odds_a"]).notna()
        if seen.any():
            for col in FIRST_COLUMNS:
                new.loc[seen, col] = new.loc[seen, "_id"].map(prev[col])
        swap = seen & flipped
        first_a, first_b = new.loc[swap, "first_odds_a"].copy(), new.loc[swap, "first_odds_b"].copy()
        new.loc[swap, "first_odds_a"], new.loc[swap, "first_odds_b"] = first_b, first_a
        new.loc[swap, "first_p_model"] = 1 - new.loc[swap, "first_p_model"]
        new = new[~new["_id"].isin(entries.loc[locked, "_id"])]
    if len(entries):
        on_card_dates = set(pd.to_datetime(card["date"]).dt.strftime("%Y-%m-%d")) if len(card) else set()
        card_ids = set(_identity(card)) if len(card) else set()
        dropped = (~locked & entries["date"].dt.strftime("%Y-%m-%d").isin(on_card_dates)
                   & ~entries["_id"].isin(card_ids) & entries["source"].eq("live"))
        if dropped.any():
            log.info("Removed %d bouts no longer on their card: %s", int(dropped.sum()),
                     "; ".join(entries.loc[dropped, "fighter_a"] + " vs " + entries.loc[dropped, "fighter_b"]))
        keep = entries[~dropped & ~entries["_id"].isin(new["_id"] if len(new) else [])]
    else:
        keep = entries
    merged = pd.concat([keep, new], ignore_index=True) if len(keep) else new.copy()
    return merged.drop(columns="_id", errors="ignore")


def _find_result(entry, by_day: dict) -> tuple | None:
    """The result for a logged bout and whether its corners match the log's.

    Looks a day either side (cards abroad can fall on a different US date),
    matching on fighter ids, then names, then close spellings.
    """
    day = pd.Timestamp(entry.date)
    cands = [r for shift in (0, -1, 1) for r in by_day.get((day + pd.Timedelta(days=shift)).strftime("%Y-%m-%d"), [])]
    for r in cands:
        if {r.a_id, r.b_id} == {entry.a_id, entry.b_id}:
            return r, r.a_id == entry.a_id
    pair = pair_key(entry.fighter_a, entry.fighter_b)
    for r in cands:
        if pair_key(r.fighter_a, r.fighter_b) == pair:
            return r, normalize_name(r.fighter_a) == normalize_name(entry.fighter_a)
    names = pd.Series({f"{i}:{s}": getattr(r, f"fighter_{s}") for i, r in enumerate(cands) for s in "ab"},
                      dtype=object)
    hit_a, hit_b = match_name(entry.fighter_a, names), match_name(entry.fighter_b, names)
    if hit_a and hit_b and hit_a.split(":")[0] == hit_b.split(":")[0] and hit_a != hit_b:
        return cands[int(hit_a.split(":")[0])], hit_a.endswith(":a")
    return None


def grade(entries: pd.DataFrame, bouts: pd.DataFrame) -> pd.DataFrame:
    """Attach results to logged bouts; mark bouts that never happened as cancelled.

    A logged bout whose card is in the results but which is not is marked
    cancelled. Every run grades again, so a result that arrives late still
    replaces a premature "cancelled".
    """
    if entries.empty:
        return entries
    entries = entries.copy()
    for col in ("status", "winner", "method"):
        entries[col] = entries[col].astype(object)
    by_day: dict[str, list] = {}
    for r in bouts.itertuples(index=False):
        by_day.setdefault(r.date.strftime("%Y-%m-%d"), []).append(r)
    for idx, entry in zip(entries.index, entries.itertuples(index=False)):
        found = _find_result(entry, by_day)
        if found is None:
            day = pd.Timestamp(entry.date)
            if any((day + pd.Timedelta(days=s)).strftime("%Y-%m-%d") in by_day for s in (-1, 0, 1)):
                entries.at[idx, "status"] = "cancelled"
            continue
        r, same = found
        winner = r.winner if same or r.winner not in ("a", "b") else {"a": "b", "b": "a"}[r.winner]
        entries.at[idx, "winner"] = winner
        entries.at[idx, "method"] = r.method
        entries.at[idx, "end_round"] = r.end_round
        entries.at[idx, "end_seconds"] = getattr(r, "end_seconds", np.nan)
        entries.at[idx, "status"] = {"draw": "draw", "nc": "no contest"}.get(r.winner, "final")
    return entries


def backfill(entries: pd.DataFrame, feats: pd.DataFrame, year: int, window: int, ridge: float) -> pd.DataFrame:
    """Walk-forward predictions for this year's finished bouts the log never saw.

    Used when the predictor starts partway through a year, so the year-to-date
    grading has something to show, and rebuilt on every run. Each bout uses
    features from earlier fights only and models fitted on earlier years; the
    prices are the dataset's approximate closing lines, so these rows are
    marked ``backfill``, not ``live``.
    """
    years = feats["date"].dt.year
    done = feats[(years == year) & feats["winner"].notna()].reset_index(drop=True)
    if len(entries):
        done = done[~_identity(done).isin(_identity(entries))].reset_index(drop=True)
    train = feats[(years >= year - window) & (years < year)]
    if done.empty or train.empty:
        return pd.DataFrame(columns=LOG_COLUMNS)
    model = FightModel.fit(train, ridge)
    rows = prediction_rows(done.assign(start=pd.to_datetime(done["date"]).dt.tz_localize("UTC")),
                           model.predict(done), pd.NaT, "backfill")
    rows[FIRST_COLUMNS] = np.nan
    rows["first_predicted_at"] = pd.NaT
    rows["predicted_at"] = pd.NaT
    rows["bout_key"] = done["bout_id"].to_numpy()
    rows["winner"] = done["winner"].to_numpy()
    rows["method"] = done["method"].to_numpy()
    rows["end_round"] = done["end_round"].to_numpy()
    rows["end_seconds"] = done["end_seconds"].to_numpy() if "end_seconds" in done else np.nan
    rows["status"] = done["winner"].map({"draw": "draw", "nc": "no contest"}).fillna("final").to_numpy()
    return rows


def ratings_table(fb: FeatureBuilder, bouts: pd.DataFrame, now: pd.Timestamp, active_days: int = 730) -> pd.DataFrame:
    """Glicko-2 ratings of fighters active in the last two years, by their latest division."""
    day = now.tz_localize(None) if now.tzinfo else now
    rows = []
    record = {}
    for r in bouts.itertuples(index=False):
        for fid, side in ((r.a_id, "a"), (r.b_id, "b")):
            w, l, d = record.get(fid, (0, 0, 0))
            if r.winner == side:
                w += 1
            elif r.winner in ("a", "b"):
                l += 1
            elif r.winner == "draw":
                d += 1
            record[fid] = (w, l, d)
    for fid, last in fb.last_date.items():
        if (day - last).days > active_days or fb.last_div.get(fid) not in DIVISIONS:
            continue
        rating, rd, fights = fb.glicko.state(fid, pd.Timestamp(day).value / 86_400e9)
        w, l, d = record.get(fid, (0, 0, 0))
        rows.append({"fighter_id": fid, "name": fb.names.get(fid), "division": fb.last_div[fid],
                     "rating": rating, "rd": rd, "ufc_record": f"{w}-{l}" + (f"-{d}" if d else ""),
                     "last_fight": last.date()})
    table = pd.DataFrame(rows)
    order = {d: i for i, d in enumerate(DIVISIONS)}
    # Conservative rating (two deviations down) keeps lightly tested fighters off the top.
    table["rank_score"] = table["rating"] - 2 * table["rd"]
    table = table.sort_values(["division", "rank_score"], ascending=[True, False],
                              key=lambda s: s.map(order) if s.name == "division" else s)
    return table.reset_index(drop=True)


def run_update(now: dt.datetime | None = None, days: int = DEFAULT_DAYS, max_age_hours: float = 1.0,
               use_ufcstats: bool = True, use_espn: bool = True) -> pd.DataFrame:
    now = pd.Timestamp(now or dt.datetime.now(dt.timezone.utc))
    hp = Hyperparams.load()
    year = current_year(now.date())
    refresh_data(max_age_hours)
    bouts, stats, fighters = load_data()
    bouts = bouts[bouts["date"] < now.tz_localize(None).normalize() + pd.Timedelta(days=1)].reset_index(drop=True)
    odds = market_odds(bouts, max_age_hours=max(max_age_hours, 24.0))

    fb = FeatureBuilder(bouts, stats, fighters, hp)
    feats = fb.build().join(odds.reset_index(drop=True))
    years = feats["date"].dt.year
    model = FightModel.fit(feats[years >= year - hp.fit_window_years], hp.ridge)
    log.info("Fitted on %d fights (%s-%s); market weight %.2f", model.fit_fights, model.fit_years[0],
             model.fit_years[-1], model.calibration.market_weight)

    # This year's backfilled bouts are rebuilt every run so they always reflect the
    # current data; earlier years' stay as they were.
    entries = load_log()
    rebuilt = entries["source"].eq("backfill") & (entries["date"].dt.year == year)
    entries = entries[~rebuilt].reset_index(drop=True)
    filled = backfill(entries, feats, year, hp.fit_window_years, hp.ridge)
    if len(filled):
        log.info("Backfilled %d bouts from earlier this year", len(filled))

    known = pd.Series(fb.names)
    card = fetch_card(now, days, known, fb.last_div, use_ufcstats=use_ufcstats, use_espn=use_espn)
    upcoming = card[card["start"] > now].reset_index(drop=True)
    if len(upcoming):
        up_feats = fb.upcoming(upcoming)
        preds = model.predict(up_feats)
        new = prediction_rows(up_feats, preds, now, "live")
        append_odds_log(upcoming.assign(odds_source=upcoming["odds_source"].fillna("unknown")), now)
    else:
        new = pd.DataFrame(columns=LOG_COLUMNS)
    entries = update_log(entries, new, card, now)
    entries = pd.concat([entries, filled], ignore_index=True) if len(filled) else entries
    entries["date"] = pd.to_datetime(entries["date"])
    for col in TIME_COLUMNS:
        entries[col] = pd.to_datetime(entries[col], utc=True)
    entries = grade(entries, bouts)
    entries = entries.sort_values(["date", "event", "order", "fighter_a"], ignore_index=True,
                                  na_position="last")[LOG_COLUMNS]

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    saved = entries.copy()
    for col in TIME_COLUMNS:
        saved[col] = saved[col].map(lambda t: t.isoformat() if not pd.isna(t) else "")
    for col in ROUNDED:
        saved[col] = pd.to_numeric(saved[col], errors="coerce").round(4)
    saved.to_csv(LOG_PATH, index=False, date_format="%Y-%m-%d")

    table = ratings_table(fb, bouts, now)
    table.to_csv(RATINGS_PATH, index=False, float_format="%.1f")
    MODEL_PATH.write_text(json.dumps({"hyperparams": hp.__dict__, **model.to_dict()}, indent=2,
                                     default=float) + "\n")
    shown = entries[(entries["source"] == "live") & (entries["status"] == "upcoming") & (entries["start"] > now)]
    payload = shown.copy()
    for col in TIME_COLUMNS + ["date"]:
        payload[col] = payload[col].astype(str)
    latest = json.dumps({"generated_at": now.isoformat(),
                         "bouts": json.loads(payload.to_json(orient="records"))}, indent=2) + "\n"
    # Timestamps alone are not news: skip rewrites (and commits) when nothing else changed.
    write_if_changed(LATEST_PATH, latest, volatile=('"generated_at"', '"predicted_at"'), contains=True)
    write_if_changed(README_PATH, report.render(entries, shown, table, model, now, year), volatile=("Updated ",),
                     contains=True)
    return new
