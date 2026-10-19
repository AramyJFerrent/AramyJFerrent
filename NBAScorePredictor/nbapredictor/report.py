"""Markdown pages for the predictions folder."""

from __future__ import annotations

import math

import numpy as np
import pandas as pd

from .config import DISPLAY_TZ, season_label

# Smallest gap, in points, between the model's own spread and the line that counts as a pick.
PICK_MIN_EDGE = 1.0


def _time(ts) -> str:
    t = pd.Timestamp(ts).tz_convert(DISPLAY_TZ)
    return t.strftime("%I:%M %p").lstrip("0")


def _day(date) -> str:
    return pd.Timestamp(date).strftime("%A, %B %d").replace(" 0", " ")


def _num(x, fmt="{:.1f}") -> str:
    return "–" if x is None or pd.isna(x) else fmt.format(x)


def _signed(x: float) -> str:
    """One decimal with a sign, without a negative zero."""
    x = round(float(x), 1)
    return f"{x + 0.0:+.1f}"


def american_odds(p: float) -> int:
    """Fair (no-vig) American moneyline for win probability ``p``, rounded to 5."""
    p = min(max(p, 0.01), 0.99)
    raw = -100.0 * p / (1.0 - p) if p > 0.5 else 100.0 * (1.0 - p) / p
    return int(5 * math.floor(raw / 5 + 0.5))


def _moneyline(odds) -> str:
    if odds is None or pd.isna(odds):
        return "–"
    odds = int(round(odds))
    return f"+{odds}" if odds > 0 else str(odds)


def fair_moneyline(home_win: float, home: str, away: str) -> str:
    return f"{away} {_moneyline(american_odds(1 - home_win))} / {home} {_moneyline(american_odds(home_win))}"


def spread_text(margin: float, home: str, away: str) -> str:
    """A home margin as a betting spread on the favorite: 4.5 -> 'BOS -4.5'."""
    if margin is None or pd.isna(margin):
        return "–"
    if abs(margin) < 0.25:
        return "pick'em"
    fav = home if margin > 0 else away
    return f"{fav} -{round(abs(margin), 1):g}"


def model_pick(model_margin: float, spread: float, home: str, away: str) -> str:
    """The side the model's own spread favors against the line, with the gap in points."""
    if pd.isna(spread) or pd.isna(model_margin):
        return "–"
    edge = model_margin - spread
    if abs(edge) < PICK_MIN_EDGE:
        return "no edge"
    team = home if edge > 0 else away
    line = spread if edge > 0 else -spread
    return f"{team} {'+' if line < 0 else '-' if line > 0 else ''}{abs(line):g} ({abs(edge):.1f})"


def upcoming_table(rows: pd.DataFrame) -> str:
    lines = [
        "| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | "
        "Total: model / line | 80% range | Overtime | Missing (effect on margin) | Model pick vs line (edge) |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for r in rows.itertuples(index=False):
        fav, p = (r.home_team, r.home_win_prob) if r.home_win_prob >= 0.5 else (r.away_team, r.away_win_prob)
        spread = spread_text(r.pred_margin, r.home_team, r.away_team)
        if not pd.isna(r.spread):
            spread += f" / {spread_text(r.spread, r.home_team, r.away_team)}"
            if not pd.isna(r.home_cover_prob):
                cover = r.home_cover_prob if r.spread >= 0 else 1 - r.home_cover_prob
                spread += f" (fav covers {cover:.0%})"
        total = f"{r.pred_total:.1f}"
        if not pd.isna(r.total):
            total += f" / {r.total:g}" + (f" (over {r.over_prob:.0%})" if not pd.isna(r.over_prob) else "")
        missing = []
        for side in ("away", "home"):
            names, cost = getattr(r, f"{side}_missing"), getattr(r, f"{side}_injury_cost")
            if isinstance(names, str) and names:
                missing.append(f"{getattr(r, f'{side}_team')}: {names} ({_signed(-cost)})" if not pd.isna(cost)
                               else f"{getattr(r, f'{side}_team')}: {names}")
        pick = model_pick(r.model_margin, r.spread, r.home_team, r.away_team) if not pd.isna(r.spread) \
            else "no line yet"
        lines.append(
            f"| {_time(r.start)} | {r.away_team} @ {r.home_team} "
            f"| {r.away_team} {int(r.headline_away)}, {r.home_team} {int(r.headline_home)} "
            f"| {fav} {p:.0%} | {fair_moneyline(r.home_win_prob, r.home_team, r.away_team)} "
            f"| {spread} | {total} "
            f"| {int(r.away_low)}–{int(r.away_high)} / {int(r.home_low)}–{int(r.home_high)} "
            f"| {r.ot_prob:.0%} | {'<br>'.join(missing) if missing else '–'} | {pick} |"
        )
    return "\n".join(lines)


def _log_loss(p, y) -> float:
    p = np.clip(np.asarray(p, dtype=float), 1e-4, 1 - 1e-4)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def grade(entries: pd.DataFrame) -> pd.DataFrame:
    """Accuracy of logged predictions, next to the betting line and Elo on the same games."""
    g = entries.dropna(subset=["home_score", "away_score"])
    if g.empty:
        return pd.DataFrame()

    def row(name, d, margin, total, prob, points=True):
        actual_m = (d["home_score"] - d["away_score"]).to_numpy(float)
        actual_t = (d["home_score"] + d["away_score"]).to_numpy(float)
        y = (actual_m > 0).astype(float)
        m, t, p = (np.asarray(x, dtype=float) for x in (margin, total, prob))
        out = {"Predictor": name, "Games": len(d),
               "Margin MAE": float(np.mean(np.abs(actual_m - m))),
               "Total MAE": float(np.nanmean(np.abs(actual_t - t))) if not np.all(np.isnan(t)) else np.nan,
               "Team-points MAE": np.nan,
               "Log loss": _log_loss(p, y) if not np.all(np.isnan(p)) else np.nan,
               "Brier": float(np.mean((p - y) ** 2)) if not np.all(np.isnan(p)) else np.nan,
               "Winners": float(np.mean((m > 0) == (actual_m > 0))), "80% range hit": np.nan}
        if points and not np.all(np.isnan(t)):
            home, away = (t + m) / 2, (t - m) / 2
            out["Team-points MAE"] = float(np.mean(np.concatenate([np.abs(d["home_score"] - home),
                                                                   np.abs(d["away_score"] - away)])))
        if name.startswith("Final"):
            out["80% range hit"] = float(np.mean(np.concatenate([
                d["home_score"].between(d["home_low"], d["home_high"]),
                d["away_score"].between(d["away_low"], d["away_high"])])))
        return out

    rows = [row("Final prediction", g, g["pred_margin"], g["pred_total"], g["home_win_prob"]),
            row("Model only (before blending)", g, g["model_margin"], g["model_total"], g["model_home_prob"]),
            row("Elo", g, g["elo_spread"], np.full(len(g), np.nan), g["elo_home_prob"], points=False)]
    lined = g[g["spread"].notna() & g["total"].notna()]
    if len(lined):
        rows += [row("Final prediction, games with a line", lined, lined["pred_margin"], lined["pred_total"],
                     lined["home_win_prob"]),
                 row("Model only, games with a line", lined, lined["model_margin"], lined["model_total"],
                     lined["model_home_prob"]),
                 row("Betting line", lined, lined["spread"], lined["total"], lined["market_home_prob"])]
    return pd.DataFrame(rows)


def pick_record(d: pd.DataFrame, model_col: str, line_col: str) -> dict:
    """Against-the-spread record of the model's picks."""
    d = d.dropna(subset=[model_col, line_col, "home_score", "away_score"])
    edge = d[model_col] - d[line_col]
    res = d["home_score"] - d["away_score"] - d[line_col]
    picked = edge.abs() >= PICK_MIN_EDGE
    push = picked & (res == 0)
    win = picked & ~push & (np.sign(edge) == np.sign(res))
    w, l = int(win.sum()), int((picked & ~push & ~win).sum())
    return {"picks": int(picked.sum()), "wins": w, "losses": l, "pushes": int(push.sum()),
            "cover": w / (w + l) if w + l else float("nan")}


def pick_table(entries: pd.DataFrame) -> str:
    g = entries[entries["source"] == "live"]
    first = pick_record(g, "first_model_margin", "first_spread")
    last = pick_record(g, "model_margin", "spread")
    lines = ["| Picks against | Picks | Record (W-L-P) | Cover rate |", "|---|---|---|---|"]
    for label, r in (("First line seen", first), ("Last line before tip-off", last)):
        rate = f"{r['cover']:.1%}" if r["wins"] + r["losses"] else "–"
        lines.append(f"| {label} | {r['picks']} | {r['wins']}-{r['losses']}-{r['pushes']} | {rate} |")
    e = g.dropna(subset=["first_spread", "spread", "first_model_margin"])
    edge = e["first_model_margin"] - e["first_spread"]
    move = e["spread"] - e["first_spread"]
    moved = (edge.abs() >= PICK_MIN_EDGE) & (move != 0)
    toward = int((np.sign(move[moved]) == np.sign(edge[moved])).sum())
    lines += ["", f"Line moved toward the model's first pick before tip-off: {toward} of {int(moved.sum())} games"
              + (f" ({toward / moved.sum():.0%})." if moved.sum() else ".")]
    return "\n".join(lines)


def _metrics_table(df: pd.DataFrame) -> str:
    cols = list(df.columns)
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for _, r in df.iterrows():
        cells = []
        for c in cols:
            v = r[c]
            if c in ("Winners", "80% range hit", "Cover rate"):
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
    lines = ["| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |",
             "|---|---|---|---|---|---|"]
    for r in rows.itertuples(index=False):
        home_won = r.home_score > r.away_score
        winner_p = r.home_win_prob if home_won else r.away_win_prob
        inside = (r.home_low <= r.home_score <= r.home_high) and (r.away_low <= r.away_score <= r.away_high)
        ot = f" ({int(r.periods) - 4}OT)".replace("(1OT)", "(OT)") if not pd.isna(r.periods) and r.periods > 4 else ""
        spread = spread_text(r.pred_margin, r.home_team, r.away_team)
        if not pd.isna(r.spread):
            spread += f" / {spread_text(r.spread, r.home_team, r.away_team)}"
        lines.append(
            f"| {r.away_team} @ {r.home_team} | {int(r.headline_away)}–{int(r.headline_home)} "
            f"| {int(r.away_score)}–{int(r.home_score)}{ot} | {winner_p:.0%} | {spread} "
            f"| {'yes' if inside else 'no'} |"
        )
    return "\n".join(lines)


def ratings_table(table: pd.DataFrame) -> str:
    lines = ["| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |",
             "|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(table.itertuples(index=False), 1):
        lines.append(f"| {i} | {r.team} | {_signed(r.net)} | {_signed(r.net_per_game)} | {_signed(r.offense)} "
                     f"| {_signed(r.defense)} | {r.pace:.1f} | {_signed(-r.injury_cost)} | {_num(r.elo, '{:.0f}')} |")
    return "\n".join(lines)


def players_table(table: pd.DataFrame) -> str:
    lines = ["| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |",
             "|---|---|---|---|---|---|---|"]
    for i, r in enumerate(table.itertuples(index=False), 1):
        lines.append(f"| {i} | {r.name} | {r.team} | {_signed(r.net)} | {_signed(r.offense)} | {_signed(r.defense)} "
                     f"| {r.minutes:.0f} |")
    return "\n".join(lines)


def render(entries: pd.DataFrame, upcoming: pd.DataFrame, ratings: pd.DataFrame, stars: pd.DataFrame,
           model, now, season: int) -> str:
    stamp = pd.Timestamp(now).tz_convert(DISPLAY_TZ).strftime("%a %b %d, %Y %I:%M %p ET")
    parts = [
        "# NBA score predictions",
        "",
        f"Updated {stamp}. Refreshed automatically several times a day during the season, around the "
        "injury report's deadlines; each game's prediction is locked at tip-off and graded once the final "
        "score is in.",
        "",
        "Each team's expected points are its expected possessions times its expected points per possession, "
        "from team efficiency ratings and the ratings of the players expected to play, blended with the "
        "betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is "
        "the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. "
        "Basketball is the most predictable major sport, but a team's score still varies by about ±14 "
        "points around the forecast, so read the win chance and the ranges too.",
        "",
        "Missing players come from the injury report: out players are left out, and doubtful, questionable "
        "and probable ones count with the share of their minutes their chance of playing implies, and their "
        "minutes go mostly to the bench. The effect is how many points of margin the team gains or loses "
        "against its full-strength roster: negative when it is missing good players, positive when the "
        "minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.",
        "",
        "The fair moneyline is the American odds that match the win chance exactly, with no bookmaker "
        "margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. The model pick is the "
        f"side the model's own spread (before blending with the line) favors by {PICK_MIN_EDGE:g} point or "
        "more; treat it as an experiment, since the backtest found no edge against closing lines.",
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
                  "MAE is the average miss in points; team-points MAE is the average miss on each team's score. "
                  "Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and "
                  "0.250). The closing line misses margins by about 10 points and totals by about 14.", ""]
        reg = graded[graded["game_type"] != "P"]
        if len(reg) and reg["periods"].notna().any():
            parts += [f"Overtime: predicted in {reg['ot_prob'].mean():.1%} of games, happened in "
                      f"{(reg['periods'] > 4).mean():.1%}.", ""]
        backfilled = int((graded["source"] == "backfill").sum())
        if backfilled:
            parts += [f"{backfilled} of these games were played before the predictor went live. They are "
                      "backfilled walk-forward (each day predicted from earlier days only) knowing who played, "
                      "with any archived closing line. Every game since is graded on the prediction logged "
                      "before tip-off.", ""]
        if (graded["source"] == "live").any() and graded["spread"].notna().any():
            parts += ["### Model picks against the spread", "", pick_table(season_log), "",
                      "Break-even at standard -110 prices is 52.4%. The line moving toward the model's pick "
                      "before tip-off is the quickest sign that it knows something the market doesn't yet.", ""]
        last_day = graded["date"].max()
        parts += [f"### Results, {_day(last_day)}", "", results_table(graded[graded["date"] == last_day]), ""]
    else:
        parts += ["Nothing graded yet; results appear here after the first predicted games finish.", ""]

    parts += ["## Power ratings", "",
              "Points per 100 possessions better than an average team on a neutral floor, combining "
              "opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy "
              "roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is "
              "what its current injury report does to its margin, in points.", "",
              ratings_table(ratings), ""]
    if len(stars):
        parts += ["## Top players", "",
                  "Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 "
                  "possessions a player adds on offense and saves on defense, against an average player, "
                  "shrunk toward last season's rating. Players expected to play 20 minutes or more.", "",
                  players_table(stars), ""]

    c = model.eff_coef
    parts += [
        "## Current model fit", "",
        f"- Fitted on {model.fit_games} games from {season_label(model.fit_seasons[0])} to "
        f"{season_label(model.fit_seasons[-1])}.",
        f"- Home court: {c.get('home', 0.0):+.1f} points per 100 possessions for the home team over the visitor "
        f"(about {c.get('home', 0.0):.1f} points a game).",
        f"- Second night of a back-to-back: {c.get('b2b', 0.0):+.1f} points per 100 scored, "
        f"{c.get('b2b_opp', 0.0):+.1f} allowed.",
        f"- Weights: team efficiency ratings {c.get('eff_off', 0.0):.2f} (offense) and {c.get('eff_def', 0.0):.2f} "
        f"(defense); player lineup ratings {c.get('p_off', 0.0):.2f} and {c.get('p_def', 0.0):.2f}.",
        f"- Blend: {1 - model.margin_weight:.0%} on the betting line for the margin and "
        f"{1 - model.total_weight:.0%} for the total, wherever there is a line (fitted on past closing lines).",
        f"- Simulator: each team's points vary by {model.sim.sd:.1f} with correlation {model.sim.rho:.2f}; "
        f"{model.ot_rate:.1%} of recent games went to overtime.",
        "",
    ]
    return "\n".join(parts)


def render_backtest(scores: dict, checks: dict, bootstrap: dict, seasons: tuple, picks: dict, extra: dict) -> str:
    parts = [
        "# Walk-forward backtest",
        "",
        f"Seasons {season_label(seasons[0])} to {season_label(seasons[-1])}. Every game is predicted using only "
        "earlier days of its season plus the preseason priors, with the points map, blend and simulator fitted "
        "on earlier seasons only. Who played is known (the final injury report); minutes are projected. "
        "Benchmarks are scored on the same games, all of which have an archived closing line.",
        "",
    ]
    for label, df in scores.items():
        df = df.rename(columns={
            "predictor": "Predictor", "games": "Games", "margin_mae": "Margin MAE", "margin_rmse": "Margin RMSE",
            "total_mae": "Total MAE", "team_points_mae": "Team-points MAE", "log_loss": "Log loss",
            "brier": "Brier", "winner_pct": "Winners",
        })
        parts += [f"## {label}", "", _metrics_table(df), ""]
    parts += ["## Is the difference real?", "",
              "Paired bootstrap of the per-game absolute margin error (negative favors the first).", "",
              "| Comparison | Mean difference | 95% interval |", "|---|---|---|"]
    for name, (mean, lo, hi) in bootstrap.items():
        parts.append(f"| {name} | {mean:+.3f} | {lo:+.3f} to {hi:+.3f} |")
    calib = checks["calibration"]
    parts += ["", "## Win-probability calibration", "",
              "| Predicted home win | Games | Mean predicted | Actual |", "|---|---|---|---|"]
    for idx, r in calib.iterrows():
        parts.append(f"| {idx} | {int(r.games)} | {r.predicted:.1%} | {r.actual:.1%} |")
    parts += ["", "## Score distribution checks", "",
              f"- 80% ranges contained each team's points {checks['range_coverage']:.1%} of the time, the margin "
              f"{checks['margin_coverage']:.1%} and the total {checks['total_coverage']:.1%}.",
              f"- Overtime (regular season): predicted {checks['ot_predicted']:.1%}, actual {checks['ot_actual']:.1%}.",
              f"- Spread of real results around the prediction: margin {checks['margin_sd']:.1f} points, total "
              f"{checks['total_sd']:.1f}.",
              f"- The headline score picked the winner {checks['headline_winner']:.1%} of the time.",
              ""]
    if picks:
        parts += ["## Model picks against the spread", "",
                  f"Picking a side whenever the model's own spread and the line differ by {PICK_MIN_EDGE:g} point "
                  "or more. Break-even at standard -110 prices is 52.4%.", "",
                  "| Picks against | Record (W-L-P) | Cover rate | 95% range | Line moved toward the pick |",
                  "|---|---|---|---|---|"]
        for label, r in picks.items():
            moved = f"{r['moved_toward']:.1%} of {r['moved_games']}" if r.get("moved_games") else "–"
            parts.append(f"| {label} | {r['wins']}-{r['losses']}-{r['pushes']} | {r['cover']:.1%} "
                         f"| {r['cover_low']:.1%}–{r['cover_high']:.1%} | {moved} |")
        parts.append("")
    for title, lines in extra.items():
        parts += [f"## {title}", ""] + [f"- {line}" for line in lines] + [""]
    return "\n".join(parts)
