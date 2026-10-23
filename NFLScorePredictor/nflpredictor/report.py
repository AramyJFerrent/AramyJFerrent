"""Markdown pages for the predictions folder."""

from __future__ import annotations

import numpy as np
import pandas as pd

from .config import KICKOFF_TZ
from bettingcore import EDGE_MIN_EV, GAME_CAP_UNITS, KELLY_FRACTION, fair_american, format_american

from .edges import MARKETS, edge_record, has_edge


def _kickoff(ts) -> str:
    t = pd.Timestamp(ts).tz_convert(KICKOFF_TZ)
    return t.strftime("%a %m/%d %I:%M %p").replace(" 0", " ")


def _spread(margin: float, home: str, away: str) -> str:
    if pd.isna(margin):
        return "–"
    if abs(margin) < 0.05:
        return "PK"
    return f"{home} -{margin:.1f}" if margin > 0 else f"{away} -{-margin:.1f}"


def _num(x, fmt="{:.1f}") -> str:
    return "–" if pd.isna(x) else fmt.format(x)


def _qb(name) -> str:
    return "?" if pd.isna(name) else str(name)


def _moneyline(odds: int) -> str:
    return f"+{odds}" if odds > 0 else str(odds)


def fair_moneyline(home_win: float, away_win: float, home: str, away: str) -> str:
    """Both sides' fair moneylines. Ties refund moneyline bets, so they are left out."""
    home_p = home_win / (home_win + away_win)
    return (f"{away} {_moneyline(fair_american(1 - home_p))} / "
            f"{home} {_moneyline(fair_american(home_p))}")


# Which posted price each side of each market is bet at.
SIDE_PRICES = {
    ("spread", "home"): "home_spread_price", ("spread", "away"): "away_spread_price",
    ("total", "over"): "over_price", ("total", "under"): "under_price",
    ("moneyline", "home"): "home_moneyline", ("moneyline", "away"): "away_moneyline",
}
MARKET_NAMES = {"spread": "Spread", "moneyline": "Moneyline", "total": "Total"}


def _has_line(r, market: str) -> bool:
    if market == "moneyline":
        return not (pd.isna(r.home_moneyline) or pd.isna(r.away_moneyline))
    return not pd.isna(r.spread_line if market == "spread" else r.total_line)


def edge_cell(r, market: str) -> str:
    """``KC -3.5 (-110): EV +5.0%, 55%, stake 1.2u``, ``no edge`` or ``no line yet``."""
    pick = getattr(r, f"{market}_edge_pick")
    if not has_edge(pick):
        return "no edge" if _has_line(r, market) else "no line yet"
    side = getattr(r, f"{market}_edge_side")
    assumed = pd.isna(getattr(r, SIDE_PRICES[(market, side)]))
    price = format_american(getattr(r, f"{market}_edge_price"), assumed)
    stake = getattr(r, f"{market}_edge_stake", np.nan)
    return (f"{pick} ({price}): EV {getattr(r, f'{market}_edge_ev'):+.1%}, "
            f"{getattr(r, f'{market}_edge_prob'):.0%}" + ("" if pd.isna(stake) else f", stake {stake:.1f}u"))


def upcoming_table(rows: pd.DataFrame) -> str:
    lines = [
        "| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | "
        "80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge "
        "| QBs | Notes |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for r in rows.itertuples(index=False):
        home_p = r.home_win_prob + 0.5 * r.tie_prob
        fav, p = (r.home_team, home_p) if home_p >= 0.5 else (r.away_team, 1 - home_p)
        notes = []
        if not pd.isna(r.wind_forecast) and r.wind_forecast >= 12:
            notes.append(f"wind {r.wind_forecast:.0f} mph")
        lines.append(
            f"| {_kickoff(r.kickoff)} | {r.away_team} @ {r.home_team} "
            f"| {r.away_team} {int(r.headline_away)}, {r.home_team} {int(r.headline_home)} "
            f"| {fav} {p:.0%} | {fair_moneyline(r.home_win_prob, r.away_win_prob, r.home_team, r.away_team)} "
            f"| {r.pred_away:.1f} – {r.pred_home:.1f} "
            f"| {int(r.away_low)}–{int(r.away_high)} / {int(r.home_low)}–{int(r.home_high)} "
            f"| {_spread(r.model_margin, r.home_team, r.away_team)} / {_spread(r.spread_line, r.home_team, r.away_team)} "
            f"| {r.model_total:.1f} / {_num(r.total_line)} "
            f"| {edge_cell(r, 'spread')} | {edge_cell(r, 'moneyline')} | {edge_cell(r, 'total')} "
            f"| {_qb(r.away_qb)} / {_qb(r.home_qb)} | {', '.join(notes)} |"
        )
    return "\n".join(lines)


def grade(entries: pd.DataFrame) -> pd.DataFrame:
    """Accuracy of logged predictions, next to the line recorded with them."""
    g = entries.dropna(subset=["home_score", "away_score"])
    if g.empty:
        return pd.DataFrame()
    margin = g["home_score"] - g["away_score"]
    total = g["home_score"] + g["away_score"]
    outcome = np.where(margin > 0, 1.0, np.where(margin < 0, 0.0, 0.5))
    p_home = g["home_win_prob"] + 0.5 * g["tie_prob"]
    inside = np.concatenate([
        g["home_score"].between(g["home_low"], g["home_high"]),
        g["away_score"].between(g["away_low"], g["away_high"]),
    ])
    decided = margin != 0
    rows = [{
        "Predictor": "Final prediction",
        "Games": len(g),
        "Margin MAE": np.mean(np.abs(margin - g["pred_margin"])),
        "Total MAE": np.mean(np.abs(total - g["pred_total"])),
        "Team-score MAE": np.mean(np.abs(np.concatenate([g["home_score"] - g["pred_home"],
                                                         g["away_score"] - g["pred_away"]]))),
        "Winners": np.mean((np.sign(g["pred_margin"]) == np.sign(margin))[decided]),
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
        "Winners": np.mean((np.sign(g["model_margin"]) == np.sign(margin))[decided]),
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
            "Winners": np.mean((np.sign(lined["spread_line"]) == np.sign(lm))[lm != 0]),
            "Brier": np.nan,
            "80% range hit": np.nan,
        })
    return pd.DataFrame(rows)


def edge_table(entries: pd.DataFrame) -> str:
    """Record of the logged edges in each market, at the price and stake logged with the last prediction."""
    lines = ["| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |",
             "|---|---|---|---|---|---|---|"]
    for market in MARKETS:
        rec = edge_record(entries, market)
        roi = f"{rec['roi']:+.1%} | {rec['expected_roi']:+.1%}" if rec["bets"] else "– | –"
        lines.append(f"| {MARKET_NAMES[market]} | {rec['bets']} | {rec['wins']}-{rec['losses']}-{rec['pushes']} "
                     f"| {rec['staked']:.1f} | {rec['units']:+.2f} | {roi} |")
    return "\n".join(lines)


def line_moves(entries: pd.DataFrame) -> tuple[int, int]:
    """Of the early spread edges whose line later moved, how many moved toward the pick.

    The home side is favored more as ``spread_line`` (expected home margin)
    rises, so a move toward a home pick is an increase.
    """
    e = entries[entries["first_spread_edge_side"].isin(["home", "away"]) & entries["spread_line"].notna()]
    move = e["spread_line"] - e["first_spread_line"]
    sign = np.where(e["first_spread_edge_side"] == "home", 1.0, -1.0)
    moved = move != 0
    return int((np.sign(move[moved]) == sign[moved]).sum()), int(moved.sum())


def _metrics_table(df: pd.DataFrame) -> str:
    cols = list(df.columns)
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for _, r in df.iterrows():
        cells = []
        for c in cols:
            v = r[c]
            if c in ("Winners", "80% range hit"):
                cells.append(_num(v, "{:.1%}"))
            elif c == "Brier":
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
        home_p = r.home_win_prob + 0.5 * r.tie_prob
        margin = r.home_score - r.away_score
        winner_p = home_p if margin > 0 else 1 - home_p if margin < 0 else np.nan
        inside = (r.home_low <= r.home_score <= r.home_high) and (r.away_low <= r.away_score <= r.away_high)
        lines.append(
            f"| {r.away_team} @ {r.home_team} | {int(r.headline_away)}–{int(r.headline_home)} "
            f"| {int(r.away_score)}–{int(r.home_score)} | {_num(winner_p, '{:.0%}') if margin else 'tie'} "
            f"| {'yes' if inside else 'no'} |"
        )
    return "\n".join(lines)


def ratings_table(table: pd.DataFrame) -> str:
    lines = ["| # | Team | Net | Offense | Defense | Special teams | Elo |", "|---|---|---|---|---|---|---|"]
    for i, r in enumerate(table.itertuples(index=False), 1):
        st = getattr(r, "st_pts", 0.0)
        lines.append(f"| {i} | {r.team} | {r.net_pts:+.1f} | {r.off_pts:+.1f} | {r.def_pts:+.1f} "
                     f"| {st:+.1f} | {_num(r.elo, '{:.0f}')} |")
    return "\n".join(lines)


def render(entries: pd.DataFrame, upcoming: pd.DataFrame, ratings: pd.DataFrame, model, now,
           season: int) -> str:
    stamp = pd.Timestamp(now).tz_convert(KICKOFF_TZ).strftime("%a %b %d, %Y %I:%M %p ET")
    parts = [
        "# NFL score predictions",
        "",
        f"Updated {stamp}. Refreshed automatically every day of the season; each game's "
        "prediction is locked at kickoff and graded once the final score is in. "
        "Scores are the most likely real scoreline near the expected points; ranges cover "
        "80% of simulated outcomes for each team.",
        "",
        "Expected points blend the model with the betting line using the weight that has "
        "predicted best in recent seasons (see Current model fit). The spread and total "
        "columns show the model's own numbers next to the line, so you can see where it disagrees.",
        "",
        "The fair moneyline is the American odds that match the win chance exactly, with no "
        "bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. "
        "A sportsbook's price will be a little worse on both sides because of its cut, so a book "
        "only offers value on a team when its price beats the fair line. Ties refund moneyline "
        "bets, so they are left out of these odds.",
        "",
        "The edge columns price every side of the spread, moneyline and total with the final "
        "prediction, the model blended with the line: its expected points are run through the score "
        "simulator against the posted lines, and each side's expected value (EV) is what $1 staked "
        "returns on average at the posted price (pushes on whole-number lines and moneyline ties "
        f"refund the stake). A side is an edge when its EV is at least {EDGE_MIN_EV:+.0%}; the cell "
        "shows the best side, its price, its EV, its chance of winning and its stake. Stakes are a "
        f"{KELLY_FRACTION:.0%} share of the Kelly stake, in units of 1% of the bankroll, with at most "
        f"{GAME_CAP_UNITS:g} units on one game. Prices come from the nflverse schedule; a spread or "
        "total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. "
        "Treat the edges as an experiment, not betting advice. The model's own numbers (the spread "
        "and total columns) often sit several points from the line, but the blend keeps only the share "
        "of that disagreement the model has earned in past seasons, so edges are rare. See the "
        "backtest for how they have done on past seasons; the live record is tracked below.",
        "",
    ]
    if len(upcoming):
        for week, rows in upcoming.groupby("week"):
            parts += [f"## {season} Week {int(week)}", "", upcoming_table(rows), ""]
    else:
        parts += ["No upcoming games on the schedule yet.", ""]

    season_log = entries[entries["season"] == season]
    graded = season_log.dropna(subset=["home_score", "away_score"])
    parts += [f"## How the {season} predictions have done", ""]
    if len(graded):
        parts += [_metrics_table(grade(season_log)), "",
                  "MAE is mean absolute error in points (lower is better). Brier scores the win "
                  "chances (lower is better, 0.25 is a coin flip). Even the closing betting line "
                  "misses the final margin by about 10 points per game.", ""]
        backfilled = int((graded["source"] == "backfill").sum())
        if backfilled:
            parts += [f"{backfilled} of these games were played before the predictor went live. "
                      "They are backfilled walk-forward (each week predicted from earlier weeks only) "
                      "but with closing lines and actual starters, so they flatter the model "
                      "slightly. Every game since is graded on the prediction logged before kickoff.", ""]
        live = season_log[season_log["source"] == "live"]
        toward, moved = line_moves(live)
        parts += ["### Betting edges", "",
                  "Every edge logged with the last prediction before kickoff, graded at the price and "
                  "stake logged with it (live predictions only; backfilled games, and edges logged "
                  "before edges were priced from the final prediction, are left out). Units are 1% of "
                  "the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' "
                  "EVs promised.", "",
                  edge_table(live), "",
                  f"Spread line moved toward the model's early spread edge before kickoff: {toward} of "
                  f"{moved} games" + (f" ({toward / moved:.0%})." if moved else ".")
                  + " Lines moving toward the edge (closing line value) is the quickest sign that the "
                  "model knows something the market doesn't yet.", ""]
        last_week = graded["week"].max()
        parts += [f"### Week {int(last_week)} results", "",
                  results_table(graded[graded["week"] == last_week]), ""]
    else:
        parts += ["Nothing graded yet; results appear here after the first predicted games finish.", ""]

    parts += ["## Power ratings", "",
              "Points per game better than an average team on a neutral field, from "
              "opponent-adjusted EPA with this season's games weighted against a preseason prior. "
              "Defense is positive when it holds opponents below average.", "",
              ratings_table(ratings), ""]

    c = model.coef
    parts += [
        "## Current model fit", "",
        f"- Fitted on {model.fit_games} games from seasons {model.fit_seasons[0]}–{model.fit_seasons[-1]}.",
        f"- Home field: {c['home']:.1f} points ({c['home'] + c['home_div']:.1f} in divisional games).",
        f"- QB adjustment: {c['qb']:.2f} points per point of QB value gap.",
        f"- Special teams: {c.get('st', 0.0):.2f} points per point of net special-teams EPA.",
        f"- Weight on the betting line: {1 - model.margin_weight:.0%} for the margin, "
        f"{1 - model.total_weight:.0%} for the total.",
        f"- Wind: {model.wind_blend:+.2f} total points per mph above 10 mph at open-air stadiums.",
        "",
    ]
    return "\n".join(parts)


def render_backtest(scores: dict, checks: dict, bootstrap: dict, seasons: tuple,
                    edges: list | None = None) -> str:
    parts = [
        "# Walk-forward backtest",
        "",
        f"Seasons {seasons[0]}–{seasons[-1]}. Every game is predicted using only earlier weeks of its "
        "season plus the preseason prior, with the points map, market blend and simulator fitted on "
        "earlier seasons only. Benchmarks are scored on the same games.",
        "",
    ]
    for label, df in scores.items():
        df = df.rename(columns={
            "predictor": "Predictor", "games": "Games", "margin_mae": "Margin MAE",
            "margin_rmse": "Margin RMSE", "total_mae": "Total MAE", "team_score_mae": "Team-score MAE",
            "brier": "Brier", "log_loss": "Log loss", "winner_pct": "Winners",
        })
        parts += [f"## {label}", "", _metrics_table(df), ""]
    parts += ["## Is the difference real?", "",
              "Paired bootstrap of the per-game absolute margin error (negative favors the first).", "",
              "| Comparison | Mean difference | 95% interval |", "|---|---|---|"]
    for name, (mean, lo, hi) in bootstrap.items():
        parts.append(f"| {name} | {mean:+.3f} | {lo:+.3f} to {hi:+.3f} |")
    if edges:
        parts += ["", "## Betting edges", "",
                  "Each side of each market priced with the final prediction (the model blended with the "
                  "line being bet, by the weight fitted on earlier seasons, run through the score "
                  f"simulator), betting the best side whenever its expected value is at least {EDGE_MIN_EV:+.0%} "
                  f"at the price, at {KELLY_FRACTION:.0%} of the Kelly stake with at most {GAME_CAP_UNITS:g} "
                  "units (1% of the bankroll each) on one game. Pushes return the stake. Starting QBs here "
                  "are each team's previous starter, so nothing is used that a Wednesday line could not know. "
                  "Closing lines and prices come from the nflverse schedule. The Wednesday lines (Westgate "
                  "SuperContest spreads) and the opening spreads and totals (sportsbookreview's archive, "
                  "matched by date, teams and final score) carry no prices, so -110 is assumed for them; the "
                  "opening moneyline is not archived. ROI is units won per unit "
                  "staked, with a 95% bootstrap range over games; expected ROI is what the edges' EVs "
                  "promised, so a gap between the two shows how far the chances behind the edges are off. "
                  "The model-only rows price the same bets with the model before the blend, the rule the "
                  "predictor used before, for comparison.", "",
                  "| Market | Lines | Chances | Edges | Record (W-L-P) | Staked | Units won | ROI | 95% range "
                  "| Expected ROI | Line moved toward edge by kickoff |",
                  "|---|---|---|---|---|---|---|---|---|---|---|"]
        for market, label, chances, r in edges:
            if r is None:
                parts.append(f"| {market} | {label} | {chances} | no historical prices | | | | | | | |")
                continue
            moved = f"{r['moved_toward']:.1%} of {r['moved_games']}" if r.get("moved_games") else "–"
            roi = (f"{r['roi']:+.1%} | {r['roi_low']:+.1%} to {r['roi_high']:+.1%} | {r['expected_roi']:+.1%}"
                   if r["bets"] else "– | – | –")
            parts.append(f"| {market} | {label} | {chances} | {r['bets']} | {r['wins']}-{r['losses']}-{r['pushes']} "
                         f"| {r['staked']:.1f} | {r['units']:+.1f} | {roi} | {moved} |")
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
