"""Markdown pages for the predictions folder."""

from __future__ import annotations

import math

import numpy as np
import pandas as pd

from .config import KICKOFF_TZ


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


def american_odds(p: float) -> int:
    """Fair (no-vig) American moneyline for win probability ``p``, rounded to 5."""
    p = min(max(p, 0.01), 0.99)
    raw = -100.0 * p / (1.0 - p) if p > 0.5 else 100.0 * (1.0 - p) / p
    return int(5 * math.floor(raw / 5 + 0.5))


def _moneyline(odds: int) -> str:
    return f"+{odds}" if odds > 0 else str(odds)


def fair_moneyline(home_win: float, away_win: float, home: str, away: str) -> str:
    """Both sides' fair moneylines. Ties refund moneyline bets, so they are left out."""
    home_p = home_win / (home_win + away_win)
    return (f"{away} {_moneyline(american_odds(1 - home_p))} / "
            f"{home} {_moneyline(american_odds(home_p))}")


# Smallest gap between the model's spread and the line that counts as a pick.
PICK_MIN_EDGE = 0.5
# Cover rate needed to profit at standard -110 odds.
BREAK_EVEN = 110 / 210


def _line(points: float) -> str:
    return "PK" if abs(points) < 0.05 else f"{points:+.1f}"


def model_pick(model_margin: float, line: float, home: str, away: str) -> str:
    """The side the model's own spread favors against ``line`` (home margin), with the gap."""
    if pd.isna(line) or pd.isna(model_margin):
        return "–"
    edge = model_margin - line
    if abs(edge) < PICK_MIN_EDGE:
        return "no edge"
    team, spread = (home, -line) if edge > 0 else (away, line)
    return f"{team} {_line(spread)} ({abs(edge):.1f})"


def upcoming_table(rows: pd.DataFrame) -> str:
    lines = [
        "| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | "
        "80% range | Spread: model / line | Model pick (edge) | Total: model / line | QBs | Notes |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for r in rows.itertuples(index=False):
        home_p = r.home_win_prob + 0.5 * r.tie_prob
        fav, p = (r.home_team, home_p) if home_p >= 0.5 else (r.away_team, 1 - home_p)
        notes = []
        if not pd.isna(r.wind_forecast) and r.wind_forecast >= 12:
            notes.append(f"wind {r.wind_forecast:.0f} mph")
        if pd.isna(r.spread_line):
            notes.append("no line yet")
        lines.append(
            f"| {_kickoff(r.kickoff)} | {r.away_team} @ {r.home_team} "
            f"| {r.away_team} {int(r.headline_away)}, {r.home_team} {int(r.headline_home)} "
            f"| {fav} {p:.0%} | {fair_moneyline(r.home_win_prob, r.away_win_prob, r.home_team, r.away_team)} "
            f"| {r.pred_away:.1f} – {r.pred_home:.1f} "
            f"| {int(r.away_low)}–{int(r.away_high)} / {int(r.home_low)}–{int(r.home_high)} "
            f"| {_spread(r.model_margin, r.home_team, r.away_team)} / {_spread(r.spread_line, r.home_team, r.away_team)} "
            f"| {model_pick(r.model_margin, r.spread_line, r.home_team, r.away_team)} "
            f"| {r.model_total:.1f} / {_num(r.total_line)} "
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


def _record(margin: pd.Series, line: pd.Series, model: pd.Series) -> tuple[int, int, int]:
    """Wins, losses and pushes for model picks against ``line``."""
    edge, res = model - line, margin - line
    picked = line.notna() & model.notna() & (edge.abs() >= PICK_MIN_EDGE)
    push = picked & (res == 0)
    win = picked & ~push & (np.sign(edge) == np.sign(res))
    return int(win.sum()), int((picked & ~push & ~win).sum()), int(push.sum())


def pick_table(entries: pd.DataFrame) -> str:
    """Against-the-spread record of the model's picks, and whether lines moved toward them."""
    g = entries.dropna(subset=["home_score", "away_score"])
    margin = g["home_score"] - g["away_score"]
    early = g["first_spread_line"].notna()
    rows = [
        ("Early-week line (first prediction with a line)",
         _record(margin[early], g.loc[early, "first_spread_line"], g.loc[early, "first_model_margin"])),
        ("Line at kickoff (last prediction)", _record(margin, g["spread_line"], g["model_margin"])),
    ]
    backfilled = int((g["source"] == "backfill").sum())
    if backfilled:
        rows[1] = (f"Line at kickoff (last prediction; includes {backfilled} backfilled games)", rows[1][1])
    lines = ["| Picks against | Record (W-L-P) | Cover rate |", "|---|---|---|"]
    for label, (w, l, p) in rows:
        rate = f"{w / (w + l):.1%}" if w + l else "–"
        lines.append(f"| {label} | {w}-{l}-{p} | {rate} |")
    e = entries[entries["first_spread_line"].notna() & entries["spread_line"].notna()]
    edge = e["first_model_margin"] - e["first_spread_line"]
    move = e["spread_line"] - e["first_spread_line"]
    moved = (edge.abs() >= PICK_MIN_EDGE) & (move != 0)
    toward = int((np.sign(move[moved]) == np.sign(edge[moved])).sum())
    lines += ["", f"Line moved toward the model's early pick before kickoff: "
              f"{toward} of {int(moved.sum())} games"
              + (f" ({toward / moved.sum():.0%})." if moved.sum() else ".")]
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
        "The model pick is the side the model's own spread favors against the current line, with "
        "the gap in points (under half a point is no edge). Treat it as an experiment: in "
        "walk-forward backtests these picks covered 53.7% against Wednesday lines (2015–2020) but "
        "only 51.7% against closing lines (2015–2025), and 52.4% is break-even at standard -110 odds. "
        "The live record is tracked below, graded against the first line each game had.",
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
        parts += ["### Model picks against the spread", "", pick_table(season_log), "",
                  f"Break-even at standard -110 odds is {BREAK_EVEN:.1%}. Lines moving toward the "
                  "model's pick (closing line value) is the quickest sign that it knows something "
                  "the market doesn't yet.", ""]
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
                    picks: dict | None = None) -> str:
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
    if picks:
        parts += ["", "## Model picks against the spread", "",
                  "The model's own spread (no market blend) against the line, picking whenever they "
                  "differ by half a point or more. Starting QBs here are each team's previous starter, "
                  "so nothing is used that a Wednesday line could not know. "
                  f"Break-even at standard -110 odds is {BREAK_EVEN:.1%}.", "",
                  "| Picks against | Record (W-L-P) | Cover rate | 95% range | Line moved toward pick by kickoff |",
                  "|---|---|---|---|---|"]
        for label, r in picks.items():
            moved = f"{r['moved_toward']:.1%} of {r['moved_games']}" if "moved_toward" in r else "–"
            parts.append(f"| {label} | {r['wins']}-{r['losses']}-{r['pushes']} | {r['cover']:.1%} "
                         f"| {r['cover_low']:.1%}–{r['cover_high']:.1%} | {moved} |")
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
