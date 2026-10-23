"""Markdown pages for the predictions folder."""

from __future__ import annotations

import json

import numpy as np
import pandas as pd

from bettingcore import EDGE_MIN_EV, GAME_CAP_UNITS, KELLY_FRACTION, fair_american
from bettingcore import format_american as american_text

from .config import DISPLAY_TZ, OUTPUT_DIR
from .edges import MARKETS, assumed_price, edge_results, no_edges, record

BACKTEST_SUMMARY_PATH = OUTPUT_DIR / "backtest_summary.json"
MARKET_NAMES = {"spread": "Spread", "moneyline": "Moneyline", "total": "Total"}


def _kickoff(ts, tbd=False) -> str:
    t = pd.Timestamp(ts).tz_convert(DISPLAY_TZ)
    return t.strftime("%a %m/%d").replace(" 0", " ") + (" TBA" if tbd else t.strftime(" %I:%M %p").replace(" 0", " "))


def _spread(margin: float, home: str, away: str) -> str:
    if pd.isna(margin):
        return "–"
    if abs(margin) < 0.05:
        return "PK"
    return f"{home} -{margin:.1f}" if margin > 0 else f"{away} -{-margin:.1f}"


def _num(x, fmt="{:.1f}") -> str:
    return "–" if pd.isna(x) else fmt.format(x)


def fair_moneyline(home_win: float, away_win: float, home: str, away: str) -> str:
    """Both sides' fair moneylines."""
    home_p = home_win / (home_win + away_win)
    return (f"{away} {american_text(fair_american(1 - home_p))} / "
            f"{home} {american_text(fair_american(home_p))}")


def edge_cell(r, market: str) -> str:
    """The logged edge in ``market`` for one game, 'no edge', or 'no line yet'."""
    pick = getattr(r, f"{market}_edge_pick")
    if no_edges(r._asdict()):
        return "none in bowls (opt-outs)"
    if isinstance(pick, str) and pick:
        star = "*" if assumed_price(r._asdict(), market) else ""
        stake = getattr(r, f"{market}_edge_stake", np.nan)
        return (f"{pick} ({american_text(getattr(r, f'{market}_edge_price'))}{star}): "
                f"EV {getattr(r, f'{market}_edge_ev'):+.1%}, {getattr(r, f'{market}_edge_prob'):.0%}"
                + ("" if pd.isna(stake) else f", stake {stake:.1f}u"))
    if market == "moneyline":
        if pd.notna(r.home_moneyline) or pd.notna(r.away_moneyline):
            return "no edge"
        p = r.home_win_prob
        if pd.isna(p):
            return "no line yet"
        team, p = (r.home_team, p) if p >= 0.5 else (r.away_team, 1 - p)
        return f"no line yet (fair: {team} {american_text(fair_american(p))})"
    return "no edge" if pd.notna(r.spread_line if market == "spread" else r.total_line) else "no line yet"


def _matchup(r) -> str:
    sep = "vs" if bool(r.neutral) else "@"
    return f"{r.away_team} {sep} {r.home_team}"


def upcoming_table(rows: pd.DataFrame) -> str:
    lines = [
        "| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | "
        "80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge "
        "| Notes |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for r in rows.itertuples(index=False):
        home_p = r.home_win_prob / (r.home_win_prob + r.away_win_prob)
        fav, p = (r.home_team, home_p) if home_p >= 0.5 else (r.away_team, 1 - home_p)
        notes = []
        if r.home_division == "fcs" or r.away_division == "fcs":
            notes.append("FCS opponent")
        if bool(r.neutral):
            notes.append("neutral site")
        if any(isinstance(getattr(r, f"{m}_edge_pick"), str) and getattr(r, f"{m}_edge_pick")
               and assumed_price(r._asdict(), m) for m in ("spread", "total")):
            notes.append("* price not posted; assumed -110")
        lines.append(
            f"| {_kickoff(r.kickoff, getattr(r, 'start_time_tbd', False))} | {_matchup(r)} "
            f"| {r.away_team} {int(r.headline_away)}, {r.home_team} {int(r.headline_home)} "
            f"| {fav} {p:.0%} | {fair_moneyline(r.home_win_prob, r.away_win_prob, r.home_team, r.away_team)} "
            f"| {r.pred_away:.1f} – {r.pred_home:.1f} "
            f"| {int(r.away_low)}–{int(r.away_high)} / {int(r.home_low)}–{int(r.home_high)} "
            f"| {_spread(r.model_margin, r.home_team, r.away_team)} / {_spread(r.spread_line, r.home_team, r.away_team)} "
            f"| {r.model_total:.1f} / {_num(r.total_line)} "
            f"| {' | '.join(edge_cell(r, m) for m in MARKETS)} | {', '.join(notes)} |"
        )
    return "\n".join(lines)


def grade(entries: pd.DataFrame) -> pd.DataFrame:
    """Accuracy of logged predictions, next to the line recorded with them."""
    g = entries.dropna(subset=["home_score", "away_score"])
    if g.empty:
        return pd.DataFrame()
    margin = g["home_score"] - g["away_score"]
    total = g["home_score"] + g["away_score"]
    outcome = np.where(margin > 0, 1.0, 0.0)
    p_home = g["home_win_prob"] / (g["home_win_prob"] + g["away_win_prob"])
    inside = np.concatenate([
        g["home_score"].between(g["home_low"], g["home_high"]),
        g["away_score"].between(g["away_low"], g["away_high"]),
    ])
    rows = [{
        "Predictor": "Final prediction",
        "Games": len(g),
        "Margin MAE": np.mean(np.abs(margin - g["pred_margin"])),
        "Total MAE": np.mean(np.abs(total - g["pred_total"])),
        "Team-score MAE": np.mean(np.abs(np.concatenate([g["home_score"] - g["pred_home"],
                                                         g["away_score"] - g["pred_away"]]))),
        "Winners": np.mean(np.sign(g["pred_margin"]) == np.sign(margin)),
        "Brier": np.mean((p_home - outcome) ** 2),
        "80% range hit": np.mean(inside),
    }]
    model_home, model_away = (g["model_total"] + g["model_margin"]) / 2, (g["model_total"] - g["model_margin"]) / 2
    rows.append({
        "Predictor": "Model only (before blending)",
        "Games": len(g),
        "Margin MAE": np.mean(np.abs(margin - g["model_margin"])),
        "Total MAE": np.mean(np.abs(total - g["model_total"])),
        "Team-score MAE": np.mean(np.abs(np.concatenate([g["home_score"] - model_home,
                                                         g["away_score"] - model_away]))),
        "Winners": np.mean(np.sign(g["model_margin"]) == np.sign(margin)),
        "Brier": np.nan,
        "80% range hit": np.nan,
    })
    lined = g.dropna(subset=["spread_line", "total_line"])
    if len(lined):
        lm = lined["home_score"] - lined["away_score"]
        lt = lined["home_score"] + lined["away_score"]
        home_l, away_l = (lined["total_line"] + lined["spread_line"]) / 2, (lined["total_line"] - lined["spread_line"]) / 2
        rows.append({
            "Predictor": "Betting line when predicted",
            "Games": len(lined),
            "Margin MAE": np.mean(np.abs(lm - lined["spread_line"])),
            "Total MAE": np.mean(np.abs(lt - lined["total_line"])),
            "Team-score MAE": np.mean(np.abs(np.concatenate([lined["home_score"] - home_l,
                                                             lined["away_score"] - away_l]))),
            "Winners": np.mean((np.sign(lined["spread_line"]) == np.sign(lm))[lined["spread_line"] != 0]),
            "Brier": np.nan,
            "80% range hit": np.nan,
        })
    return pd.DataFrame(rows)


def edge_table(entries: pd.DataFrame) -> str:
    """Record of the edges logged with live predictions, at the price logged before kickoff."""
    live = entries[entries["source"] == "live"]
    lines = ["| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |",
             "|---|---|---|---|---|---|---|"]
    assumed = 0
    for market in MARKETS:
        res = edge_results(live, market)
        assumed += int(res["assumed"].sum())
        r = record(res)
        roi = f"{r['roi']:+.1%} | {r['expected_roi']:+.1%}" if r["bets"] else "– | –"
        lines.append(f"| {MARKET_NAMES[market]} | {r['bets']} | {r['wins']}-{r['losses']}-{r['pushes']} "
                     f"| {r['staked']:.1f} | {r['units']:+.2f} | {roi} |")
    if assumed:
        lines += ["", f"{assumed} of these edges were priced at an assumed -110 (price not posted)."]
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
            elif c in ("Brier", "Log loss"):
                cells.append(_num(v, "{:.3f}"))
            elif c == "Games":
                cells.append(str(int(v)))
            elif isinstance(v, (float, np.floating)):
                cells.append(_num(v, "{:.2f}"))
            else:
                cells.append(str(v))
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def results_table(rows: pd.DataFrame) -> str:
    lines = ["| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |", "|---|---|---|---|---|"]
    for r in rows.itertuples(index=False):
        home_p = r.home_win_prob / (r.home_win_prob + r.away_win_prob)
        margin = r.home_score - r.away_score
        winner_p = home_p if margin > 0 else 1 - home_p
        inside = (r.home_low <= r.home_score <= r.home_high) and (r.away_low <= r.away_score <= r.away_high)
        lines.append(
            f"| {_matchup(r)} | {int(r.headline_away)}–{int(r.headline_home)} "
            f"| {int(r.away_score)}–{int(r.home_score)} | {winner_p:.0%} | {'yes' if inside else 'no'} |"
        )
    return "\n".join(lines)


def ratings_table(table: pd.DataFrame) -> str:
    lines = ["| # | Team | Conference | Net | Offense | Defense | Special teams | Results (Elo) | Elo rating |",
             "|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(table.itertuples(index=False), 1):
        lines.append(f"| {i} | {r.team} | {r.conference} | {r.net_pts:+.1f} | {r.off_pts:+.1f} "
                     f"| {r.def_pts:+.1f} | {r.st_pts:+.1f} | {_num(r.elo_pts, '{:+.1f}')} "
                     f"| {_num(r.elo, '{:.0f}')} |")
    return "\n".join(lines)


def _backtest_summary() -> dict:
    try:
        return json.loads(BACKTEST_SUMMARY_PATH.read_text())
    except (OSError, ValueError):
        return {}


def _edge_note(summary: dict) -> str:
    """An honest caution drawn from the backtest's edge record (or its older spread-pick record)."""
    tail = ("The live record is tracked below, graded at the price logged with the last prediction "
            "before kickoff.")
    rows = [r for r in summary.get("edges") or []
            if r.get("chances", "final") == "final" and r.get("lines", "closing") == "closing" and "bets" in r]
    if rows:
        parts = [f"{MARKET_NAMES.get(r['market'], r['market']).lower()} {r['roi']:+.1%} on {r['bets']} bets "
                 f"({r['prices']} prices, {r['span']})" for r in rows if r["bets"]]
        none = [MARKET_NAMES.get(r["market"], r["market"]).lower() for r in rows if not r["bets"]]
        clear = [r for r in rows if r["bets"] and r["roi_low"] > 0]
        verdict = ("Only the " + ", ".join(MARKET_NAMES.get(r["market"], r["market"]).lower() for r in clear)
                   + " stayed above zero across its 95% range, and closing lines are the hardest test, "
                   "so treat these edges as an experiment."
                   if clear else "None of these is clearly above zero, so treat these edges as an experiment, "
                   "not a betting system.")
        found = (f"edges returned {'; '.join(parts)}" if parts else "the rule found no edges")
        if parts and none:
            found += f", and found none in the {' or '.join(none)}"
        return f"In the walk-forward backtest against closing lines, {found}. {verdict} " + tail
    picks = summary.get("picks") or {}
    if "closing" in picks:
        c = picks["closing"]
        return (f"Treat them as an experiment: in walk-forward backtests the model's own spread covered "
                f"{c['cover']:.1%} against closing lines ({c['span']}), short of the 52.4% needed to profit "
                f"at -110. " + tail)
    return "Treat them as an experiment. " + tail


def render(entries: pd.DataFrame, upcoming: pd.DataFrame, ratings: pd.DataFrame, model, now,
           season: int) -> str:
    stamp = pd.Timestamp(now).tz_convert(DISPLAY_TZ).strftime("%a %b %d, %Y %I:%M %p ET")
    summary = _backtest_summary()
    parts = [
        "# College football score predictions",
        "",
        f"Updated {stamp}. Refreshed automatically every day of the season and several times on "
        "Saturdays; each game's prediction is locked at kickoff and graded once the final score is "
        "in. Scores are the most likely real scoreline near the expected points; ranges cover 80% "
        "of simulated outcomes for each team. College scores scatter widely, so read the ranges, "
        "not just the headline score.",
        "",
        "Expected points blend the model with the betting line using the weight that has "
        "predicted best in recent seasons (see Current model fit). The spread and total "
        "columns show the model's own numbers next to the line, so you can see where it disagrees. "
        "Games without a line yet use the model alone.",
        "",
        "The fair moneyline is the American odds that match the win chance exactly, with no "
        "bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. "
        "A sportsbook's price will be a little worse on both sides because of its cut, so a book "
        "only offers value on a team when its price beats the fair line.",
        "",
        "The edge columns judge each bet by its expected value per $1 staked at the posted price, "
        "using the final prediction: the model blended with the line, run through the score "
        "simulator, pushes included, and anchored to the market's own chances so that only what the "
        "blend moves off the line counts. The model's own spread and total (shown alongside) sit "
        "several points from the line in most games, but the blend keeps only the share of that "
        "disagreement the model has earned in past seasons, so edges are rare. The side with the "
        f"higher value is shown when it reaches {EDGE_MIN_EV:.0%} (+3 cents per $1), as the team or "
        "side, the price, the expected value, its chance of winning the bet and its stake, a "
        f"{KELLY_FRACTION:.0%} share of the Kelly stake in units of 1% of the bankroll with at most "
        f"{GAME_CAP_UNITS:g} units on one game; anything short is no edge. Where a book posts no price "
        "for a spread or total it is assumed to be -110 and marked -110*; moneylines are never "
        "assumed. " + _edge_note(summary),
        "",
    ]
    if len(upcoming):
        for week, rows in upcoming.groupby("week"):
            label = f"Week {int(week)}" if week < 17 else "Bowls and playoff"
            parts += [f"## {season} {label}", "", upcoming_table(rows), ""]
    else:
        parts += ["No upcoming games on the schedule yet.", ""]

    season_log = entries[entries["season"] == season]
    graded = season_log.dropna(subset=["home_score", "away_score"])
    parts += [f"## How the {season} predictions have done", ""]
    if len(graded):
        parts += [_metrics_table(grade(season_log)), "",
                  "MAE is mean absolute error in points (lower is better). Brier scores the win "
                  "chances (lower is better, 0.25 is a coin flip). Even the closing betting line "
                  "misses the final margin of an FBS game by about 12.5 points.", ""]
        backfilled = int((graded["source"] == "backfill").sum())
        if backfilled:
            parts += [f"{backfilled} of these games were played before the predictor went live. "
                      "They are backfilled walk-forward (each week predicted from earlier weeks only) "
                      "but with closing lines, so they flatter the model slightly. Every game since "
                      "is graded on the prediction logged before kickoff.", ""]
        parts += ["### Betting edges", "", edge_table(season_log), "",
                  "Every edge logged before kickoff at the stake and price logged with it (backfilled "
                  "games, and edges logged before edges were priced from the final prediction, are not "
                  "included). Units are 1% of the bankroll; ROI is units won per unit staked, pushes "
                  "returning the stake, and expected ROI is what the edges' EVs promised.", ""]
        last_week = graded["week"].max()
        label = f"Week {int(last_week)}" if last_week < 17 else "Latest bowl and playoff"
        parts += [f"### {label} results", "",
                  results_table(graded[graded["week"] == last_week]), ""]
    else:
        parts += ["Nothing graded yet; results appear here after the first predicted games finish.", ""]

    parts += ["## FBS power ratings", "",
              "Points per game better than an average FBS team on a neutral field, from "
              "opponent-adjusted EPA (garbage time removed) with this season's games weighted "
              "against a preseason prior, plus the weight the margin model puts on Elo (a rating "
              "built from game results alone). Defense is positive when it holds opponents below "
              "average.", "",
              ratings_table(ratings), ""]

    c = model.coef
    parts += [
        "## Current model fit", "",
        f"- Fitted on {model.fit_games} games from seasons {model.fit_seasons[0]}–{model.fit_seasons[-1]}.",
        f"- Home field on top of the ratings: {c.get('home', 0.0):.1f} points "
        f"({c.get('home', 0.0) + c.get('home_conf', 0.0):.1f} in conference games).",
        f"- Extra FBS edge over FCS opponents beyond their ratings: {c.get('fcs', 0.0) * 2:.1f} points.",
        f"- Elo weight: {c.get('elo', 0.0):.2f} points of margin per point of Elo spread.",
        f"- Weight on the betting line: {1 - model.margin_weight:.0%} for the margin, "
        f"{1 - model.total_weight:.0%} for the total.",
        "",
    ]
    return "\n".join(parts)


def render_backtest(scores: dict, segments: pd.DataFrame, checks: dict, bootstrap: dict,
                    seasons: tuple, edges: list[dict] | None = None,
                    by_segment: pd.DataFrame | None = None) -> str:
    parts = [
        "# Walk-forward backtest",
        "",
        f"Seasons {seasons[0]}–{seasons[-1]}. Every game is predicted using only earlier weeks of its "
        "season plus the preseason prior, with the prior regression, points map, market blend and "
        "simulator fitted on earlier seasons only. Benchmarks are scored on the same games.",
        "",
    ]
    for label, df in scores.items():
        df = df.rename(columns={
            "predictor": "Predictor", "games": "Games", "margin_mae": "Margin MAE",
            "margin_rmse": "Margin RMSE", "total_mae": "Total MAE", "team_score_mae": "Team-score MAE",
            "brier": "Brier", "log_loss": "Log loss", "winner_pct": "Winners",
        })
        parts += [f"## {label}", "", _metrics_table(df), ""]
    parts += ["## By kind of game", "",
              "Mean absolute error in points on games with a closing line.", "",
              _metrics_table(segments), ""]
    parts += ["## Is the difference real?", "",
              "Paired bootstrap of the per-game absolute margin error, FBS vs FBS games "
              "(negative favors the first).", "",
              "| Comparison | Mean difference | 95% interval |", "|---|---|---|"]
    for name, (mean, lo, hi) in bootstrap.items():
        parts.append(f"| {name} | {mean:+.3f} | {lo:+.3f} to {hi:+.3f} |")
    if edges is not None:
        parts += ["", "## Betting edges", "",
                  "Every game with a line, priced with the final prediction (the model blended with the "
                  "line being bet, by the weights fitted on earlier seasons, run through the score "
                  "simulator and anchored to the market's own chances). A bet is an edge when its expected "
                  f"value is at least {EDGE_MIN_EV:.0%} per unit staked, staked at {KELLY_FRACTION:.0%} of the "
                  f"Kelly stake with at most {GAME_CAP_UNITS:g} units (1% of the bankroll each) on one game; "
                  "pushes return the stake. Closing prices are the median of the books quoting the consensus "
                  "line; the odds file has spread and total prices only through 2019, so later seasons are "
                  "scored at an assumed -110 and shown separately. Opening lines are the median opener "
                  "across books and carry no prices, so -110 is assumed there and the moneyline is left "
                  "out. ROI is units won per unit staked, with a 95% bootstrap range over games; expected "
                  "ROI is what the edges' EVs promised. The model-only rows price the same bets with the "
                  "model before the blend, the rule the predictor used before, for comparison.", "",
                  "| Market | Chances | Lines | Prices | Seasons | Games | Edges | Record (W-L-P) | Staked "
                  "| Units won | ROI | 95% range | Expected ROI |",
                  "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in edges:
            name = MARKET_NAMES.get(r["market"], r["market"])
            if not r["games"]:
                parts.append(f"| {name} | {r['chances']} | {r['lines']} | no historical prices "
                             "| – | 0 | – | – | – | – | – | – | – |")
                continue
            roi = (f"{r['roi']:+.1%} | {r['roi_low']:+.1%} to {r['roi_high']:+.1%} | {r['expected_roi']:+.1%}"
                   if r["bets"] else "– | – | –")
            parts.append(f"| {name} | {r['chances']} | {r['lines']} | {r['prices']} | {r['span']} | {r['games']} "
                         f"| {r['bets']} | {r['wins']}-{r['losses']}-{r['pushes']} | {r['staked']:.1f} "
                         f"| {r['units']:+.1f} | {roi} |")
    if by_segment is not None and len(by_segment):
        parts += ["", "### Final-prediction edges by kind of game", "",
                  "The same edges, split where college markets are thought to be softest. Each cell is "
                  "edges, ROI and its 95% range; opening lines have no moneyline.", "",
                  "| Segment | Lines | Games | Spread | Moneyline | Total |", "|---|---|---|---|---|---|"]

        def cell(rec) -> str:
            if not isinstance(rec, dict):
                return "–"
            if not rec["bets"]:
                return "0"
            return f"{rec['bets']}: {rec['roi']:+.1%} ({rec['roi_low']:+.1%} to {rec['roi_high']:+.1%})"
        for r in by_segment.itertuples(index=False):
            parts.append(f"| {r.Segment} | {r.Lines} | {r.Games} | {cell(r.spread)} "
                         f"| {cell(getattr(r, 'moneyline', None))} | {cell(r.total)} |")
    calib = checks["calibration"]
    parts += ["", "## Win-probability calibration", "",
              "| Predicted | Games | Mean predicted | Actual |", "|---|---|---|---|"]
    for idx, r in calib.iterrows():
        parts.append(f"| {idx} | {int(r.games)} | {r.predicted:.1%} | {r.actual:.1%} |")
    parts += ["", "## Score distribution checks", "",
              f"- 80% ranges contained the team's actual score {checks['range_coverage']:.1%} of the time.",
              f"- Predicted chance of a one-score game (8 or fewer): {checks['one_score_predicted']:.1%}; "
              f"actual: {checks['one_score_actual']:.1%}.",
              f"- Headline score exactly right: {checks['headline_exact']:.1%} of games.",
              ""]
    return "\n".join(parts)
