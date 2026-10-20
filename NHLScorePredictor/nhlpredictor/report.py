"""Markdown pages for the predictions folder."""

from __future__ import annotations

import math

import numpy as np
import pandas as pd

from .config import DISPLAY_TZ, season_label
from .edges import (EDGE_MIN_EV, MARKETS, edge_record, expected_value, fair_american, format_line, format_price,
                    price_assumed, puck_line, roi_interval)

MARKET_NAMES = {"spread": "Puck line", "moneyline": "Moneyline", "total": "Total"}
ASSUMED_NOTE = "\\* price not posted; assumed -110."


def _time(ts) -> str:
    t = pd.Timestamp(ts).tz_convert(DISPLAY_TZ)
    return t.strftime("%I:%M %p").lstrip("0")


def _day(date) -> str:
    return pd.Timestamp(date).strftime("%A, %B %d").replace(" 0", " ")


def _num(x, fmt="{:.1f}") -> str:
    return "–" if x is None or pd.isna(x) else fmt.format(x)


def _goalie(name, status) -> str:
    if name is None or pd.isna(name):
        return "?"
    status = "" if status is None or pd.isna(status) else str(status)
    if status.startswith("projected"):
        return f"{name} ({status.split()[-1]}?)"
    if status.startswith("ESPN"):
        return f"{name} ({status.removeprefix('ESPN ')})"
    return str(name)


def fair_moneyline(home_win: float, home: str, away: str) -> str:
    return f"{away} {format_price(fair_american(1 - home_win))} / {home} {format_price(fair_american(home_win))}"


def _priced(r, market: str) -> bool:
    """Whether the market has a line and at least one price to bet it at."""
    if market == "spread":
        return not pd.isna(r.home_spread_line) and not (pd.isna(r.home_spread_price) and pd.isna(r.away_spread_price))
    if market == "moneyline":
        return not (pd.isna(r.home_moneyline) and pd.isna(r.away_moneyline))
    return not pd.isna(r.total_line)                      # missing total prices are assumed -110


def _fair(r, market: str) -> str:
    """The model's own fair puck-line odds, for a puck line with no price to compare against. (A game
    without a moneyline is never blended, so its fair moneyline column is already the model's own.)"""
    if market == "spread" and not pd.isna(r.model_home_cover_prob):
        line = puck_line(r.home_spread_line, r.model_home_prob)
        return (f"model fair {r.home_team} {format_line(line)} {format_price(fair_american(r.model_home_cover_prob))}"
                f" / {r.away_team} {format_line(-line)} {format_price(fair_american(r.model_away_cover_prob))}")
    return ""


def edge_cell(r, market: str) -> str:
    """``MTL -1.5 (+150): EV +5.0%, model 42%``, ``no edge`` or ``no line yet``."""
    pick = getattr(r, f"{market}_edge_pick")
    if isinstance(pick, str) and pick:
        price = format_price(getattr(r, f"{market}_edge_price")) + ("*" if price_assumed(r, market) else "")
        return (f"{pick} ({price}): EV {getattr(r, f'{market}_edge_ev'):+.1%}, "
                f"model {getattr(r, f'{market}_edge_prob'):.0%}")
    if _priced(r, market):
        return "no edge"
    fair = _fair(r, market)
    if market == "spread" and not pd.isna(r.home_spread_line):
        return "no price" + (f" ({fair})" if fair else "")
    return "no line yet" + (f" ({fair})" if fair else "")


def upcoming_table(rows: pd.DataFrame) -> str:
    lines = [
        "| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range "
        "| Overtime | Puck line | Total: model / line | Goalies | Posted moneyline "
        "| Puck line edge | Moneyline edge | Total edge |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for r in rows.itertuples(index=False):
        fav, p = (r.home_team, r.home_win_prob) if r.home_win_prob >= 0.5 else (r.away_team, r.away_win_prob)
        cover = (f"{r.home_team} -1.5 {r.home_cover_prob:.0%}" if r.home_win_prob >= 0.5
                 else f"{r.away_team} -1.5 {r.away_cover_prob:.0%}")
        total = f"{r.pred_total:.1f}"
        if not pd.isna(r.total_line):
            total += f" / {r.total_line:g}" + (f" (over {r.over_prob:.0%})" if not pd.isna(r.over_prob) else "")
        posted = (f"{r.away_team} {format_price(r.away_moneyline)} / {r.home_team} {format_price(r.home_moneyline)}"
                  if not pd.isna(r.home_moneyline) else "–")
        edges = " | ".join(edge_cell(r, m) for m in MARKETS)
        lines.append(
            f"| {_time(r.start)} | {r.away_team} @ {r.home_team} "
            f"| {r.away_team} {int(r.headline_away)}, {r.home_team} {int(r.headline_home)} "
            f"| {fav} {p:.0%} | {fair_moneyline(r.home_win_prob, r.home_team, r.away_team)} "
            f"| {r.pred_away:.1f} – {r.pred_home:.1f} "
            f"| {int(r.away_low)}–{int(r.away_high)} / {int(r.home_low)}–{int(r.home_high)} "
            f"| {r.ot_prob:.0%} | {cover} | {total} "
            f"| {_goalie(r.away_goalie, r.away_goalie_status)} / {_goalie(r.home_goalie, r.home_goalie_status)} "
            f"| {posted} | {edges} |"
        )
    if any(price_assumed(r, "total") for r in rows.itertuples(index=False)):
        lines += ["", ASSUMED_NOTE]
    return "\n".join(lines)


def _log_loss(p, y) -> float:
    p = np.clip(np.asarray(p, dtype=float), 1e-4, 1 - 1e-4)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def grade(entries: pd.DataFrame) -> pd.DataFrame:
    """Accuracy of logged predictions, next to the market and Elo on the same games."""
    g = entries.dropna(subset=["home_score", "away_score"])
    if g.empty:
        return pd.DataFrame()

    def row(name, d, prob, goals=True):
        y = (d["home_score"] > d["away_score"]).astype(float).to_numpy()
        p = np.asarray(prob, dtype=float)
        out = {"Predictor": name, "Games": len(d), "Log loss": _log_loss(p, y),
               "Brier": float(np.mean((p - y) ** 2)), "Winners": float(np.mean((p >= 0.5) == (y == 1))),
               "Goals MAE": np.nan, "Total MAE": np.nan, "80% range hit": np.nan}
        if goals:
            out["Goals MAE"] = float(np.mean(np.abs(np.concatenate([d["home_score"] - d["pred_home"],
                                                                    d["away_score"] - d["pred_away"]]))))
            out["Total MAE"] = float(np.mean(np.abs(d["home_score"] + d["away_score"] - d["pred_total"])))
            out["80% range hit"] = float(np.mean(np.concatenate([
                d["home_score"].between(d["home_low"], d["home_high"]),
                d["away_score"].between(d["away_low"], d["away_high"])])))
        return out

    rows = [row("Final prediction", g, g["home_win_prob"])]
    lined = g[g["market_home_prob"].notna()]
    if len(lined):
        rows.append(row("Model only (before blending)", g, g["model_home_prob"], goals=False))
    rows.append(row("Elo", g, g["elo_home_prob"], goals=False))
    if len(lined):
        rows += [row("Final prediction, games with a line", lined, lined["home_win_prob"]),
                 row("Model only, games with a line", lined, lined["model_home_prob"], goals=False)]
        market = row("Betting market (de-vigged moneyline)", lined, lined["market_home_prob"], goals=False)
        has_total = lined["total_line"].notna()
        market["Total MAE"] = float(np.mean(np.abs(
            (lined["home_score"] + lined["away_score"] - lined["total_line"])[has_total]))) if has_total.any() else np.nan
        rows.append(market)
    return pd.DataFrame(rows)


def _first_moneyline_edge(r) -> str | None:
    """The moneyline side with an edge against the first line seen, if any."""
    p = r["first_model_home_prob"]
    best, best_ev = None, EDGE_MIN_EV
    for side, prob, price in (("home", p, r["first_home_moneyline"]), ("away", 1 - p, r["first_away_moneyline"])):
        if pd.isna(price) or pd.isna(prob):
            continue
        ev = expected_value(prob, 0.0, price)
        if ev >= best_ev:
            best, best_ev = side, ev
    return best


def edge_table(entries: pd.DataFrame) -> str:
    """Record of each market's edges at the price logged with the last prediction before puck drop."""
    g = entries.dropna(subset=["home_score", "away_score"])
    lines = ["| Market | Edges | Record (W-L-P) | Units | ROI |", "|---|---|---|---|---|"]
    for market in MARKETS:
        r = edge_record(g, market)
        roi = f"{r['roi']:+.1%}" if r["bets"] else "–"
        lines.append(f"| {MARKET_NAMES[market]} | {r['bets']} | {r['wins']}-{r['losses']}-{r['pushes']} "
                     f"| {r['units']:+.2f} | {roi} |")
    # Closing line value: did the moneyline move toward the edge the model saw on the first line?
    e = entries.dropna(subset=["first_market_home_prob", "market_home_prob", "first_model_home_prob"])
    sides = pd.Series([_first_moneyline_edge(r) for _, r in e.iterrows()], index=e.index, dtype=object)
    move = e["market_home_prob"] - e["first_market_home_prob"]
    moved = sides.notna() & (move.abs() >= 0.005)
    toward = int((np.sign(move[moved]) == np.where(sides[moved] == "home", 1, -1)).sum())
    lines += ["", f"Moneyline moved toward the model's edge on the first line seen before puck drop: {toward} of "
              f"{int(moved.sum())} games" + (f" ({toward / moved.sum():.0%})." if moved.sum() else ".")]
    return "\n".join(lines)


def backtest_edge_table(records: dict) -> str:
    """Per-market edge record over the backtest; ``None`` marks a market with no historical prices."""
    lines = ["| Market | Edges | Record (W-L-P) | Units | ROI | 95% range of ROI |", "|---|---|---|---|---|---|"]
    for market in MARKETS:
        r = records.get(market)
        if r is None:
            lines.append(f"| {MARKET_NAMES[market]} | no historical prices | – | – | – | – |")
            continue
        lo, hi = roi_interval(r["per_bet"])
        roi = f"{r['roi']:+.1%}" if r["bets"] else "–"
        span = f"{lo:+.1%} to {hi:+.1%}" if r["bets"] else "–"
        lines.append(f"| {MARKET_NAMES[market]} | {r['bets']} | {r['wins']}-{r['losses']}-{r['pushes']} "
                     f"| {r['units']:+.2f} | {roi} | {span} |")
    return "\n".join(lines)


def _metrics_table(df: pd.DataFrame) -> str:
    cols = list(df.columns)
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for _, r in df.iterrows():
        cells = []
        for c in cols:
            v = r[c]
            if c in ("Winners", "80% range hit"):
                cells.append(_num(v, "{:.1%}"))
            elif c in ("Brier", "Log loss", "Total-goals RPS"):
                cells.append(_num(v, "{:.4f}"))
            elif c == "Games":
                cells.append(str(int(v)))
            elif isinstance(v, (float, np.floating)):
                cells.append(_num(v, "{:.2f}"))
            else:
                cells.append(str(v))
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def results_table(rows: pd.DataFrame) -> str:
    lines = ["| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |",
             "|---|---|---|---|---|---|"]
    for r in rows.itertuples(index=False):
        home_won = r.home_score > r.away_score
        winner_p = r.home_win_prob if home_won else r.away_win_prob
        inside = (r.home_low <= r.home_score <= r.home_high) and (r.away_low <= r.away_score <= r.away_high)
        suffix = f" ({r.result})" if isinstance(r.result, str) and r.result != "REG" else ""
        lines.append(
            f"| {r.away_team} @ {r.home_team} | {int(r.headline_away)}–{int(r.headline_home)} "
            f"| {int(r.away_score)}–{int(r.home_score)}{suffix} | {winner_p:.0%} "
            f"| {'yes' if inside else 'no'} | {_goalie(r.away_goalie, None)} / {_goalie(r.home_goalie, None)} |"
        )
    return "\n".join(lines)


def ratings_table(table: pd.DataFrame) -> str:
    lines = ["| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(table.itertuples(index=False), 1):
        lines.append(f"| {i} | {r.team} | {r.net_goals:+.2f} | {r.off_goals:+.2f} | {r.def_goals:+.2f} "
                     f"| {r.xgf_ev:.2f} | {r.xga_ev:.2f} | {r.pp_xg:.2f} | {r.pk_xga:.2f} | {_num(r.elo, '{:.0f}')} |")
    return "\n".join(lines)


def goalies_table(table: pd.DataFrame) -> str:
    lines = ["| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |",
             "|---|---|---|---|---|"]
    for r in table.itertuples(index=False):
        lines.append(f"| {r.team} | {r.goalie} | {r.start_share:.0%} | {r.gsax_per_100:+.2f} | {r.goals_per_game:+.2f} |")
    return "\n".join(lines)


def render(entries: pd.DataFrame, upcoming: pd.DataFrame, ratings: pd.DataFrame, goalies: pd.DataFrame,
           model, weight: float, lined_games: int, now, season: int) -> str:
    stamp = pd.Timestamp(now).tz_convert(DISPLAY_TZ).strftime("%a %b %d, %Y %I:%M %p ET")
    parts = [
        "# NHL score predictions",
        "",
        f"Updated {stamp}. Refreshed automatically several times a day during the season; each game's "
        "prediction is locked at puck drop and graded once the final score is in.",
        "",
        "Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, "
        "overtime and shootouts. The predicted score is the most common final score in which the likelier "
        "winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring "
        "and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) "
        "before the single score.",
        "",
        "Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "
        "\"probable\" or \"confirmed\" ones come from ESPN and replace the projection when available.",
        "",
        "The fair moneyline is the American odds that match the win chance exactly, with no bookmaker "
        "margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price "
        "is a little worse on both sides because of its cut, so a book only offers value on a team when its "
        "price beats the fair line. The puck line is the favorite's chance to win by two or more.",
        "",
        "The edge columns price each side of the puck line, moneyline and total with the model's own "
        "numbers, before they are blended with the betting line, and show the side with the best expected value "
        "(EV) per $1 bet at the posted price, overtime and shootout included (the shootout winner gets one "
        f"goal). A side is an edge only if its EV is at least {EDGE_MIN_EV:.0%}: a pick shows its price, EV and "
        "the model's chance of winning the bet; \"no edge\" means neither side clears the bar. A total with no "
        "posted price is assumed to be -110 (marked \\*); the puck line and moneyline are never assumed, so "
        "without a price the cell shows the model's fair odds instead. Treat the edges as an experiment: no free "
        "source has a history of NHL lines, so they could not be backtested against the market, and the "
        "backtest's margins are thin (the model beats Elo by 0.0035 log loss per game, small next to a "
        "sportsbook's cut). Their record is tracked live below.",
        "",
    ]
    if len(upcoming):
        for date, rows in upcoming.groupby("date", sort=True):
            parts += [f"## {_day(date)}", "", upcoming_table(rows), ""]
    else:
        parts += ["No upcoming games on the schedule in the next few days.", ""]

    season_log = entries[entries["season"] == season]
    graded = season_log.dropna(subset=["home_score", "away_score"])
    parts += [f"## How the {season_label(season)} predictions have done", ""]
    if len(graded):
        parts += [_metrics_table(grade(season_log)), "",
                  "Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and "
                  "0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and "
                  "only over hundreds of games. Goals MAE is the average miss on each team's goals.", ""]
        reg = graded[graded["game_type"] == "R"]
        if len(reg) and reg["result"].notna().any():
            parts += [f"Overtime: predicted in {reg['ot_prob'].mean():.1%} of regular-season games, "
                      f"happened in {reg['result'].isin(['OT', 'SO']).mean():.1%}.", ""]
        backfilled = int((graded["source"] == "backfill").sum())
        if backfilled:
            parts += [f"{backfilled} of these games were played before the predictor went live. They are "
                      "backfilled walk-forward (each day predicted from earlier days only) with the actual "
                      "starting goalies and no betting line. Every game since is graded on the prediction "
                      "logged before puck drop.", ""]
        live = graded[graded["source"] == "live"]
        if live["market_home_prob"].notna().any() or live["total_line"].notna().any():
            parts += ["### Betting edges", "", edge_table(season_log[season_log["source"] == "live"]), "",
                      "One unit on each edge at the price logged with the last prediction before puck drop; "
                      "pushes return the stake. The moneyline moving toward the model's edge (closing line "
                      "value) is the quickest sign that it knows something the market doesn't yet.", ""]
        last_day = graded["date"].max()
        parts += [f"### Results, {_day(last_day)}", "", results_table(graded[graded["date"] == last_day]), ""]
    else:
        parts += ["Nothing graded yet; results appear here after the first predicted games finish.", ""]

    parts += ["## Power ratings", "",
              "Goals per game better than an average team, from the goal-rate model: offense and defense "
              "combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each "
              "weighted against a preseason prior. Defense is positive when it holds opponents below average. "
              "Goaltending is rated separately below.", "",
              ratings_table(ratings), ""]
    if len(goalies):
        parts += ["## Goalies", "",
                  "Each team's likeliest next starter. GSAx is goals saved above expected (from this "
                  "predictor's own shot model), shrunk hard toward a slightly below-average prior, since "
                  "goaltending repeats poorly from season to season.", "",
                  goalies_table(goalies), ""]

    c = model.coef
    sim = model.sim
    # Minutes left when the trailing team usually has its goalie out.
    pull1 = next((60 - m for m, p in zip(range(54, 60), sim.pull[1]) if p >= 0.5), 1)
    pull2 = next((60 - m for m, p in zip(range(54, 60), sim.pull[2]) if p >= 0.5), 1)
    blend = (f"{1 - weight:.0%} on the betting line wherever there is one (fitted on {lined_games} logged "
             "games, shrunk toward an even split)" if lined_games else
             f"{1 - weight:.0%} on the betting line wherever there is one (an even split until enough logged "
             "games with lines exist to fit it)")
    parts += [
        "## Current model fit", "",
        f"- Fitted on {model.fit_games} games from {season_label(model.fit_seasons[0])} to "
        f"{season_label(model.fit_seasons[-1])}.",
        f"- Home ice: {math.exp(c.get('home', 0.0)) - 1:+.1%} goals for the home team relative to the visitor.",
        f"- Second night of a back-to-back: {math.exp(c.get('b2b', 0.0)) - 1:+.1%} goals scored, "
        f"{math.exp(c.get('b2b_opp', 0.0)) - 1:+.1%} goals allowed.",
        f"- Starting goalie: each goal per game he saves above average lowers the opponent's rate by "
        f"{1 - math.exp(c.get('goalie', 0.0)):.0%}.",
        f"- Blend: {blend}.",
        f"- Simulator: {model.tie_rate:.1%} of recent regular-season games reached overtime; trailing teams "
        f"usually have the goalie pulled with {pull1} minutes left when down one and {pull2} when down two; "
        f"empty-net goals come at {sim.en_rate:.2f} a minute with the net empty; three-on-three overtime "
        f"produces {sim.ot_rate * 5:.2f} goals per five minutes.",
        "",
    ]
    return "\n".join(parts)


def render_backtest(scores: dict, checks: dict, bootstrap: dict, seasons: tuple, extra: dict,
                    edges: dict | None = None) -> str:
    parts = [
        "# Walk-forward backtest",
        "",
        f"Seasons {season_label(seasons[0])} to {season_label(seasons[-1])}. Every game is predicted using only "
        "earlier days of its season plus the preseason prior, with the goal-rate model and simulator fitted on "
        "earlier seasons only. Baselines are scored on the same games. No free source has a long history of "
        "NHL betting lines, so the market comparison lives on the predictions page, graded live.",
        "",
    ]
    for label, df in scores.items():
        df = df.rename(columns={
            "predictor": "Predictor", "games": "Games", "log_loss": "Log loss", "brier": "Brier",
            "winner_pct": "Winners", "goals_mae": "Goals MAE", "total_mae": "Total MAE",
            "rps_total": "Total-goals RPS",
        })
        parts += [f"## {label}", "", _metrics_table(df), ""]
    parts += ["## Is the difference real?", "",
              "Paired bootstrap of the per-game log loss (negative favors the first).", "",
              "| Comparison | Mean difference | 95% interval |", "|---|---|---|"]
    for name, (mean, lo, hi) in bootstrap.items():
        parts.append(f"| {name} | {mean:+.4f} | {lo:+.4f} to {hi:+.4f} |")
    calib = checks["calibration"]
    parts += ["", "## Win-probability calibration", "",
              "| Predicted home win | Games | Mean predicted | Actual |", "|---|---|---|---|"]
    for idx, r in calib.iterrows():
        parts.append(f"| {idx} | {int(r.games)} | {r.predicted:.1%} | {r.actual:.1%} |")
    parts += ["", "## Score distribution checks (regular season)", "",
              "| Check | Simulator | Independent Poisson, same rates | Actual |", "|---|---|---|---|",
              f"| Tied after regulation | {checks['ot_predicted']:.1%} | {checks['ot_indep']:.1%} | {checks['ot_actual']:.1%} |",
              f"| One-goal regulation margin (empty-netters counted) | {checks['one_goal_predicted']:.1%} "
              f"| {checks['one_goal_indep']:.1%} | {checks['one_goal_actual']:.1%} |",
              f"| Game with an empty-net goal | {checks['en_predicted']:.1%} | – | {checks['en_actual']:.1%} |",
              f"| Home team wins by 2+ (all games) | {checks['home_cover_predicted']:.1%} | – "
              f"| {checks['home_cover_actual']:.1%} |",
              f"| Total-goals ranked probability score (lower is better) | {checks['rps_sim']:.4f} "
              f"| {checks['rps_poisson']:.4f} | – |",
              "",
              f"- 80% ranges contained the team's actual goals {checks['range_coverage']:.1%} of the time "
              "(goals are whole numbers, so a range covers a little more than 80%).",
              f"- Headline score exactly right: {checks['headline_exact']:.1%} of games.",
              ""]
    if extra:
        parts += ["## Starting goalies", ""]
        parts += [f"- {line}" for line in extra.get("goalie_lines", [])]
        parts.append("")
    parts += ["## Betting edges", "",
              f"Edges are sides whose expected value at the posted price is at least {EDGE_MIN_EV:.0%}, priced "
              "from the model alone. No free source has a history of NHL puck-line, moneyline or total prices, so "
              "none can be backtested here; the predictions page grades them live.", "",
              backtest_edge_table(edges or {}), ""]
    return "\n".join(parts)
