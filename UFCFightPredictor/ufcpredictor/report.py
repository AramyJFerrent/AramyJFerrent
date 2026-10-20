"""Markdown pages for the predictions folder."""

from __future__ import annotations

import math

import numpy as np
import pandas as pd

from .config import DISPLAY_TZ, DIVISION_ABBR, DIVISIONS
from .edges import EDGE_MIN_EV, MARKET_NAMES, MARKETS, METHOD_NAMES, edge_cell, fair_american, record
from .edges import fmt_american as _ml
from .model import METHODS


def _pct(p, digits: int = 0) -> str:
    return "–" if pd.isna(p) else f"{100 * p:.{digits}f}%"


def _surname(name: str) -> str:
    return str(name).split()[-1] if isinstance(name, str) and name.split() else str(name)


def _start(ts) -> str:
    if pd.isna(ts):
        return ""
    return pd.Timestamp(ts).tz_convert(DISPLAY_TZ).strftime("%a %b %d, %I:%M %p ET").replace(" 0", " ")


def _tags(r) -> str:
    tags = [DIVISION_ABBR.get(r.division, r.division)]
    if r.title:
        tags.append("title")
    tags.append(f"{int(r.rounds)} rds")
    for side in ("a", "b"):
        if getattr(r, f"{side}_fights") == 0:
            tags.append(f"UFC debut: {_surname(getattr(r, 'fighter_' + side))}")
    return ", ".join(tags)


def most_likely(r) -> str:
    name = r.fighter_a if r.best_side == "a" else r.fighter_b
    return f"{_surname(name)} by {METHOD_NAMES[r.best_method]} ({_pct(r.best_prob)})"


def upcoming_tables(rows: pd.DataFrame) -> str:
    head = ["| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | "
            "Most likely result | Moneyline edge | Round total edge | Method edge |",
            "|---|---|---|---|---|---|---|---|---|---|---|"]
    timing = ["| Bout | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Decision |",
              "|---|---|---|---|---|---|---|"]
    for r in rows.itertuples(index=False):
        a, b = _surname(r.fighter_a), _surname(r.fighter_b)
        market = (f"{a} {_pct(r.p_market)} ({_ml(r.odds_a)} / {_ml(r.odds_b)})" if not pd.isna(r.p_market)
                  else "no line yet")
        split = (f"{a} {_pct(r.a_ko)} / {_pct(r.a_sub)} / {_pct(r.a_dec)}<br>"
                 f"{b} {_pct(r.b_ko)} / {_pct(r.b_sub)} / {_pct(r.b_dec)}")
        head.append(
            f"| **{r.fighter_a}** vs. **{r.fighter_b}**<br>{_tags(r)} "
            f"| {a} {_pct(r.p_a)} – {_pct(1 - r.p_a)} {b} "
            f"| {_ml(fair_american(r.p_a))} / {_ml(fair_american(1 - r.p_a))} "
            f"| {market} | {a} {_pct(r.p_model)} ({_ml(fair_american(r.p_model))}) | {split} "
            f"| {_pct(r.p_distance)} | {most_likely(r)} "
            "| " + " | ".join(edge_cell(r, m) for m in MARKETS) + " |"
        )
        cells = [_pct(getattr(r, f"r{k}")) if k <= r.rounds else "" for k in range(1, 6)]
        timing.append(f"| {a} vs. {b} | " + " | ".join(cells) + f" | {_pct(r.p_distance)} |")
    return "\n".join(head) + "\n\nWhen it ends (either fighter):\n\n" + "\n".join(timing)


# ---- grading ----------------------------------------------------------------

def _ll(p, y) -> float:
    p = np.clip(np.asarray(p, float), 1e-4, 1 - 1e-4)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def grade(entries: pd.DataFrame) -> pd.DataFrame:
    """Winner accuracy of logged predictions, next to the price logged with them."""
    g = entries[entries["status"].eq("final") & entries["winner"].isin(["a", "b"])]
    if g.empty:
        return pd.DataFrame()
    y = (g["winner"] == "a").to_numpy(float)
    rows = []
    for name, col in (("Final prediction", "p_a"), ("Model alone (before the market)", "p_model"),
                      ("Glicko-2 rating alone", "p_glicko")):
        p = g[col].to_numpy(float)
        rows.append({"Predictor": name, "Fights": len(g), "Log loss": _ll(p, y),
                     "Brier": float(np.mean((p - y) ** 2)), "Winners": float(np.mean((p > 0.5) == (y == 1)))})
    priced = g["p_market"].notna()
    if priced.any():
        gp, yp = g[priced], y[priced.to_numpy()]
        for name, p in (("Final, on fights with a price", gp["p_a"]),
                        ("Market price when predicted", gp["p_market"])):
            p = p.to_numpy(float)
            rows.append({"Predictor": name, "Fights": int(priced.sum()), "Log loss": _ll(p, yp),
                         "Brier": float(np.mean((p - yp) ** 2)),
                         "Winners": float(np.mean((p > 0.5) == (yp == 1)))})
    rows.append({"Predictor": "Coin flip", "Fights": len(g), "Log loss": math.log(2), "Brier": 0.25,
                 "Winners": np.nan})
    return pd.DataFrame(rows)


def method_grade(entries: pd.DataFrame) -> dict:
    g = entries[entries["status"].eq("final") & entries["winner"].isin(["a", "b"])
                & entries["method"].isin(["KO", "SUB", "DEC"])]
    if g.empty:
        return {}
    cols = [f"{s}_{m}" for s in "ab" for m in METHODS]
    actual = (g["winner"] + "_" + g["method"].str.lower()).map(cols.index).to_numpy()
    P = np.clip(g[cols].to_numpy(float), 1e-4, 1)
    went = (g["method"] == "DEC").to_numpy(float)
    return {"fights": len(g), "six_way": float(-np.mean(np.log(P[np.arange(len(g)), actual]))),
            "distance_predicted": float(g["p_distance"].mean()), "distance_actual": float(went.mean()),
            "exact": float(np.mean([s == w and m == meth.lower() for s, m, w, meth in
                                    zip(g["best_side"], g["best_method"], g["winner"], g["method"])]))}


def edge_records(entries: pd.DataFrame) -> str:
    """Per-market record of the logged edges, one unit a bet at the logged price."""
    lines = ["| Market | Edges | Record (W-L-P) | Units | ROI |", "|---|---|---|---|---|"]
    for m in MARKETS:
        r = record(entries, m)
        roi = "–" if pd.isna(r["roi"]) else f"{r['roi']:+.1%}"
        lines.append(f"| {MARKET_NAMES[m]} | {r['edges']} | {r['wins']}-{r['losses']}-{r['pushes']} "
                     f"| {r['units']:+.2f} | {roi} |")
    return "\n".join(lines)


def _table(df: pd.DataFrame) -> str:
    cols = list(df.columns)
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for _, r in df.iterrows():
        cells = []
        for c in cols:
            v = r[c]
            if c in ("Winners", "Predicted", "Actual"):
                cells.append(_pct(v, 1))
            elif c in ("Fights",):
                cells.append(str(int(v)))
            elif c == "Log loss":
                cells.append("–" if pd.isna(v) else f"{v:.4f}")
            elif isinstance(v, (float, np.floating)):
                cells.append("–" if pd.isna(v) else f"{v:.3f}")
            else:
                cells.append(str(v))
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def results_table(rows: pd.DataFrame) -> str:
    lines = ["| Bout | Predicted | Result | Chance given to the winner | Chance given to the exact result |",
             "|---|---|---|---|---|"]
    for r in rows.itertuples(index=False):
        a, b = _surname(r.fighter_a), _surname(r.fighter_b)
        fav = f"{a} {_pct(r.p_a)}" if r.p_a >= 0.5 else f"{b} {_pct(1 - r.p_a)}"
        if r.status != "final" or r.winner not in ("a", "b"):
            lines.append(f"| {r.fighter_a} vs. {r.fighter_b} | {fav} | {r.status} | – | – |")
            continue
        winner = r.fighter_a if r.winner == "a" else r.fighter_b
        p_win = r.p_a if r.winner == "a" else 1 - r.p_a
        method = str(r.method).lower()
        exact = getattr(r, f"{r.winner}_{method}") if method in METHODS else np.nan
        how = METHOD_NAMES.get(method, str(r.method))
        rnd = f", R{int(r.end_round)}" if method in ("ko", "sub") and not pd.isna(r.end_round) else ""
        lines.append(f"| {r.fighter_a} vs. {r.fighter_b} | {fav} | {winner} by {how}{rnd} "
                     f"| {_pct(p_win)} | {_pct(exact)} |")
    return "\n".join(lines)


def ratings_section(table: pd.DataFrame, top: int = 5) -> str:
    lines = ["| Division | # | Fighter | Rating | ± | UFC record | Last fight |", "|---|---|---|---|---|---|---|"]
    for div in DIVISIONS:
        rows = table[table["division"] == div].head(top)
        for i, r in enumerate(rows.itertuples(index=False), 1):
            lines.append(f"| {div if i == 1 else ''} | {i} | {r.name} | {r.rating:.0f} | {2 * r.rd:.0f} "
                         f"| {r.ufc_record} | {r.last_fight} |")
    return "\n".join(lines)


def render(entries: pd.DataFrame, upcoming: pd.DataFrame, ratings: pd.DataFrame, model, now, year: int) -> str:
    stamp = pd.Timestamp(now).tz_convert(DISPLAY_TZ).strftime("%a %b %d, %Y %I:%M %p ET")
    cal = model.calibration
    parts = [
        "# UFC fight predictions",
        "",
        f"Updated {stamp}. Refreshed automatically every day and several times on fight week; "
        "each bout's prediction is locked when its part of the card starts and graded once the "
        "result is in.",
        "",
        "Each bout gets one consistent breakdown: each fighter's chance to win, split into KO/TKO, "
        "submission and decision, and the chance it ends in each round. The win chance blends the "
        f"model with the betting market (about {cal.market_weight:.0%} market, the weight that has "
        "predicted best on past fights) and corrects the market's habit of underrating heavy favorites. "
        "MMA is high-variance: even the most likely single result is usually well under 50%.",
        "",
        "The fair odds are the American odds that match the win chance with no bookmaker margin: "
        "-200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook only offers "
        "value on a fighter when its price beats the fair line.",
        "",
        "The three edge columns value every side of each market at its posted price: expected value "
        "(EV) is the average profit per $1 staked, from the model alone, before it is blended with the "
        "betting line (the \"Model alone\" win chance, with the same method and round models applied to "
        f"it). A side is an edge when its EV is at least {100 * EDGE_MIN_EV:.0f}%; each cell names the best "
        "side if one clears that bar, else \"no edge\". Moneylines and props are never priced near -110, "
        "so a missing price is never assumed: without one, the round-total cell shows the model's fair "
        "odds at the line closest to even and the method cell each fighter's fair KO/TKO, submission and "
        "decision odds. Over 1.5 rounds means the fight passes 2:30 of round 2 (a decision is always "
        "over); finishes are assumed spread evenly within a round.",
        "",
        "A caution from the backtest (backtest.md): the model alone is well behind the market, so it finds "
        "a 3% edge in most fights, and those edges lost money against the dataset's closing prices, about "
        "7% a bet on moneylines and 16% on method props, 2015–2026. Treat these columns as a live test of "
        "the model, tracked below, not as betting advice.",
        "",
    ]
    if len(upcoming):
        for (date, event), rows in upcoming.sort_values("order").groupby(["date", "event"], sort=True):
            first = rows["start"].min()
            parts += [f"## {event}", "", f"{pd.Timestamp(date):%A, %B %d, %Y}"
                      + (f" · first bout locks {_start(first)}" if not pd.isna(first) else ""), "",
                      upcoming_tables(rows), ""]
    else:
        parts += ["No upcoming bouts found on the next cards yet.", ""]

    year_log = entries[entries["date"].dt.year == year]
    graded = year_log[year_log["status"].eq("final")]
    parts += [f"## How the {year} predictions have done", ""]
    if len(graded):
        parts += [_table(grade(year_log)), "",
                  "Log loss scores the win chances (lower is better; a coin flip scores 0.693, and the "
                  "betting market about 0.61). Brier is the squared error of the win chance. Picking "
                  "every betting favorite already gets about two thirds of winners right, so the win "
                  "rate says little on its own.", ""]
        mg = method_grade(year_log)
        if mg:
            parts += [f"- Winner and method (six outcomes): log loss {mg['six_way']:.3f} on {mg['fights']} "
                      f"fights, against 1.792 for guessing uniformly. The single most likely result "
                      f"happened {_pct(mg['exact'])} of the time.",
                      f"- Went the distance: predicted {_pct(mg['distance_predicted'])} on average, "
                      f"actual {_pct(mg['distance_actual'])}."]
        backfilled = int((graded["source"] == "backfill").sum())
        if backfilled:
            parts += ["", f"{backfilled} of these fights happened before the predictor went live. They are "
                      "backfilled walk-forward (each fight predicted from earlier fights only, with models "
                      "fitted on earlier years) using the odds dataset's approximate closing prices, which "
                      "run only through March 2026, so later backfilled fights use the model alone. Every "
                      "fight since is graded on the prediction logged before it started."]
        parts.append("")
        live = year_log[year_log["source"].eq("live")]
        parts += ["### Edge record", "",
                  "Every edge logged with a live prediction (the last one before the fight), one unit a bet "
                  "at the price logged with it. Pushes return the stake (a no contest voids every bet; a draw "
                  "refunds the moneyline).", "", edge_records(live), ""]
        last_date = graded["date"].max()
        last = year_log[year_log["date"] == last_date].sort_values("order")
        parts += [f"### Latest results: {last['event'].iloc[0]}", "", results_table(last), ""]
    else:
        parts += ["Nothing graded yet; results appear here after the first predicted fights.", ""]

    pending = entries[entries["status"].eq("upcoming") & (entries["start"] <= now)]
    if len(pending):
        parts += [f"{len(pending)} locked predictions are waiting for official results.", ""]

    parts += ["## Top fighters by division", "",
              "Glicko-2 rating from UFC results, with finishes counting as clearer wins than decisions. "
              "± is two rating deviations (fighters with few or old fights are less certain), and the "
              "ranking uses the rating minus that margin so an unproven fighter does not top a division "
              "on one big win. Active fighters only (a fight in the last two years).", "",
              ratings_section(ratings), ""]

    weights = pd.Series(model.win.weights()).sort_values(key=np.abs, ascending=False).head(6)
    parts += [
        "## Current model fit", "",
        f"- Fitted on {model.fit_fights} fights from {model.fit_years[0]}–{model.fit_years[-1]}.",
        f"- Market blend: {cal.market_weight:.0%} weight on the de-vigged price, total slope "
        f"{cal.blend_model + cal.blend_market:.2f} (above 1 stretches favorites, correcting the "
        f"favorite-longshot bias). Without a price: slope {cal.model_slope:.2f} on the model alone.",
        "- Strongest win-model inputs (log-odds per standard deviation, A minus B): "
        + ", ".join(f"{k.removeprefix('d_')} {v:+.2f}" for k, v in weights.items()) + ".",
        "",
    ]
    return "\n".join(parts)


def render_backtest(win: pd.DataFrame, method: pd.DataFrame, rounds: pd.DataFrame, calib: pd.DataFrame,
                    boot: dict, bets: pd.DataFrame, years: tuple) -> str:
    parts = [
        "# Walk-forward backtest",
        "",
        f"Fights from {years[0]} to {years[-1]}. Every fight is predicted from ratings and profiles built "
        "on earlier fights only, with the win model, calibration, market blend, method and round models "
        "fitted on the ten years before its year. Benchmarks are scored on the same fights. Prices are "
        "the Ultimate UFC Dataset's moneylines (approximate closing prices) with the margin removed "
        "proportionally.",
        "",
        "## Who wins",
        "",
        _table(win.rename(columns={"predictor": "Predictor", "fights": "Fights", "log_loss": "Log loss",
                                   "brier": "Brier", "winners": "Winners"})),
        "",
        "## Is the difference real?",
        "",
        "Paired bootstrap of the per-fight log loss (negative favors the first).",
        "",
        "| Comparison | Mean difference | 95% interval |",
        "|---|---|---|",
    ]
    for name, (mean, lo, hi) in boot.items():
        parts.append(f"| {name} | {mean:+.4f} | {lo:+.4f} to {hi:+.4f} |")
    parts += ["", "## How and when", "",
              "Six-way log loss over each fighter winning by KO/TKO, submission or decision, on fights "
              "with method props. Distance: the chance the fight goes to the judges.", "",
              _table(method.rename(columns={"predictor": "Predictor", "fights": "Fights",
                                            "six_way_log_loss": "Six-way log loss",
                                            "distance_predicted": "Predicted", "distance_actual": "Actual",
                                            "distance_log_loss": "Distance log loss"})),
              "", "Round: log loss over finishing in each round or going the distance.", "",
              _table(rounds.rename(columns={"rounds": "Scheduled rounds", "predictor": "Predictor",
                                            "fights": "Fights", "log_loss": "Log loss"})),
              "", "## Win-chance calibration", "",
              "Chance given to the predicted favorite against how often favorites won.", "",
              "| Favorite's chance | Fights | Predicted | Actual |", "|---|---|---|---|"]
    for idx, r in calib.iterrows():
        parts.append(f"| {idx} | {int(r.fights)} | {r.predicted:.1%} | {r.actual:.1%} |")
    if len(bets):
        parts += ["", "## Betting edges", "",
                  "The live page's edges, valued the same way: every side of each market at the dataset's "
                  "price (approximate closing lines, bookmaker margin left in), with the model alone, before "
                  f"the market blend. A side is bet, one unit, when its expected value is at least "
                  f"{100 * EDGE_MIN_EV:.0f}%; only the best side of each market per fight. The 95% range "
                  "resamples the bets.", "",
                  "| Market | Fights with prices | Edges | Record (W-L-P) | Units | ROI | 95% range "
                  "| Model's average EV | On underdogs |",
                  "|---|---|---|---|---|---|---|---|---|"]
        for r in bets.itertuples(index=False):
            name = MARKET_NAMES[r.market]
            if not r.fights:
                parts.append(f"| {name} | no historical prices | – | – | – | – | – | – | – |")
            elif not r.edges:
                parts.append(f"| {name} | {r.fights} | 0 | – | – | – | – | – | – |")
            else:
                parts.append(f"| {name} | {r.fights} | {r.edges} | {r.wins:.0f}-{r.losses:.0f}-{r.pushes:.0f} "
                             f"| {r.units:+.1f} | {r.roi:+.1%} | {r.roi_low:+.1%} to {r.roi_high:+.1%} | {r.mean_ev:+.1%} "
                             f"| {r.underdogs:.0%} |")
        parts += ["",
                  "- \"Model's average EV\" is what the model expected to make per unit on the bets it took; "
                  "the ROI is what they made. The gap is how much the model overrates its own edges: what it "
                  "knows that the market does not is outweighed by what the market knows that it does not "
                  "(debutants' regional records, injuries, camp news).",
                  "- Method props whose six prices add up to less than 100% implied (no bookmaker margin, so not "
                  "prices anyone could bet; about a third of the dataset's 2025–26 props) are left out.",
                  "- Caveats: the dataset does not say when its prices were captured or whether they are one "
                  "book's or the best available, and real stakes would move real prices. The live page tracks "
                  "these edges on the prices it logged before each fight, which is the test that counts."]
    return "\n".join(parts) + "\n"
