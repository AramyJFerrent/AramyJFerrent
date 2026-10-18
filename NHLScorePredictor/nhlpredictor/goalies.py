"""Goalie values and projected starters.

Each goalie's value is goals saved above expected (GSAx) per 100 unblocked
shots, relative to the league that season, shrunk hard toward a slightly
below-average prior: above-expected save performance barely repeats from year
to year, so a hot month should move the number very little.

Two adjustments reach the goal-rate model. The starter's value, converted to
goals per game, and the starter's value minus the shot-weighted value of the
goalies behind the team's goals rating, which already carries their play
(the same idea as the quarterback adjustment in the NFL predictor).

Before a starter is confirmed, each goalie's chance of starting comes from his
recent share of the team's starts, with the previous night's starter marked
down on the second night of a back-to-back by the factor seen historically.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .config import Hyperparams

# Unblocked shots a team faces per game, to turn GSAx per 100 shots into goals.
SHOTS_PER_GAME = 42.0
# Half-life, in days, of the start shares used to project starters.
START_SHARE_HALF_LIFE = 20.0
# Days a goalie stays in a team's projection after his last appearance for it.
ROSTER_DAYS = 45
# Fallback for the back-to-back markdown when there is no history to fit it on.
DEFAULT_REPEAT_FACTOR = 0.2
EPOCH = pd.Timestamp("2000-01-01")


def day_index(dates) -> np.ndarray:
    return (pd.to_datetime(pd.Series(dates)) - EPOCH).dt.days.to_numpy()


class GoalieModel:
    def __init__(self, goalies: pd.DataFrame, hp: Hyperparams):
        self.hp = hp
        g = goalies.copy()
        g["dix"] = day_index(g["date"])
        g["gsax"] = g["xga"] - g["ga"]
        self.g = g.sort_values(["dix", "game_id"]).reset_index(drop=True)
        self.names = self.g.groupby("goalie_id")["goalie_name"].last()
        self.repeat_factor = self._fit_repeat_factor()

    def _before(self, dix: int) -> pd.DataFrame:
        return self.g[self.g["dix"] < dix]

    def values(self, dix: int) -> pd.Series:
        """Shrunk GSAx per 100 unblocked shots, by goalie id, from games before ``dix``."""
        g = self._before(dix)
        if g.empty:
            return pd.Series(dtype=float)
        league = g.groupby("season")[["gsax", "shots"]].sum()
        rate = league["gsax"] / league["shots"].where(league["shots"] > 0)
        rel = g["gsax"] - g["shots"] * g["season"].map(rate).fillna(0.0)
        decay = 0.5 ** ((dix - g["dix"]) / self.hp.goalie_half_life_days)
        num = (decay * rel).groupby(g["goalie_id"]).sum()
        den = (decay * g["shots"]).groupby(g["goalie_id"]).sum()
        k = self.hp.goalie_prior_shots
        return 100.0 * (num + k * self.hp.goalie_prior_value / 100.0) / (den + k)

    def value_of(self, values: pd.Series, goalie_id) -> float:
        if goalie_id is not None and not pd.isna(goalie_id) and int(goalie_id) in values.index:
            return float(values[int(goalie_id)])
        return self.hp.goalie_prior_value

    def mix(self, season: int, dix: int, values: pd.Series, half_life_days: float) -> pd.Series:
        """Shot-weighted value of the goalies behind each team's current goals rating."""
        g = self.g
        cur = g[(g["season"] == season) & (g["dix"] < dix)]
        cur_w = cur["shots"] * 0.5 ** ((dix - cur["dix"]) / half_life_days)
        last = g[g["season"] == season - 1]
        if len(last):
            raw = last["shots"] * 0.5 ** ((last["dix"].max() + 1 - last["dix"]) / half_life_days)
            share = raw / raw.groupby(last["team"]).transform("sum")
            last_w = share * SHOTS_PER_GAME * self.hp.goals_prior_games
        else:
            last_w = pd.Series(dtype=float)
        both = pd.concat([cur.assign(wt=cur_w), last.assign(wt=last_w)])
        if both.empty:
            return pd.Series(dtype=float)
        v = both["goalie_id"].map(values).fillna(self.hp.goalie_prior_value)
        return (both["wt"] * v).groupby(both["team"]).sum() / both["wt"].groupby(both["team"]).sum()

    def _fit_repeat_factor(self) -> float:
        """How much less likely last night's starter is to start again, as a
        multiplier on his usual share of starts."""
        st = self.g[self.g["starter"]][["team", "dix", "goalie_id", "season"]]
        if st.empty:
            return DEFAULT_REPEAT_FACTOR
        st = st.sort_values(["team", "dix"])
        prev_day = st.groupby("team")["dix"].shift()
        prev_goalie = st.groupby("team")["goalie_id"].shift()
        b2b = (st["dix"] - prev_day) == 1
        repeat = (st["goalie_id"] == prev_goalie)[b2b].mean()
        # Compared with how often each team's usual starter starts at all.
        share = st.groupby(["team", "season"])["goalie_id"].agg(
            lambda s: s.value_counts(normalize=True).iloc[0]).mean()
        if np.isnan(repeat) or not share > 0:
            return DEFAULT_REPEAT_FACTOR
        return float(np.clip(repeat / share, 0.05, 1.0))

    def start_probabilities(self, team: str, dix: int) -> pd.Series:
        """Chance each goalie starts the team's game on day ``dix``, by goalie id."""
        g = self._before(dix)
        g = g[(g["team"] == team) & (g["dix"] >= dix - 400)]
        if g.empty:
            return pd.Series(dtype=float)
        last_seen = g.groupby("goalie_id")["dix"].max()
        active = last_seen[last_seen >= g["dix"].max() - ROSTER_DAYS].index
        starts = g[g["starter"] & g["goalie_id"].isin(active)]
        if starts.empty:
            return pd.Series(dtype=float)
        w = 0.5 ** ((dix - starts["dix"]) / START_SHARE_HALF_LIFE)
        share = w.groupby(starts["goalie_id"]).sum() + 1e-3
        last = starts.loc[starts["dix"].idxmax()]
        if last["dix"] == dix - 1:
            share[last["goalie_id"]] *= self.repeat_factor
        return share / share.sum()


def starter_columns(model: GoalieModel, games: pd.DataFrame, season: int, dix: int,
                    ratings_half_life: float) -> pd.DataFrame:
    """Starting goalie and adjustments for each side of ``games``.

    ``games`` may carry ``home_goalie_id`` / ``away_goalie_id`` (known starters,
    such as the actual starter in history or a confirmed one today); other games
    get the probability-weighted value of the likely starters, computed for the
    day of each game.
    """
    values = model.values(dix)
    mix = model.mix(season, dix, values, ratings_half_life)
    cols: dict[str, object] = {}
    game_dix = day_index(games["date"]) if "date" in games else np.full(len(games), dix)
    for side in ("home", "away"):
        teams = games[f"{side}_team"].tolist()
        known = games[f"{side}_goalie_id"].tolist() if f"{side}_goalie_id" in games else [np.nan] * len(teams)
        ids, names, vals, status = [], [], [], []
        for team, gid, gdix in zip(teams, known, game_dix):
            if not pd.isna(gid):
                ids.append(int(gid))
                names.append(model.names.get(int(gid), str(gid)))
                vals.append(model.value_of(values, gid))
                status.append("known")
                continue
            probs = model.start_probabilities(team, int(gdix))
            if probs.empty:
                ids.append(np.nan)
                names.append(None)
                vals.append(model.hp.goalie_prior_value)
                status.append("unknown")
                continue
            top = int(probs.idxmax())
            ids.append(top)
            names.append(model.names.get(top, str(top)))
            vals.append(float(sum(p * model.value_of(values, i) for i, p in probs.items())))
            status.append(f"projected {probs.max():.0%}")
        vals = np.array(vals, dtype=float)
        behind = np.array([mix.get(t, model.hp.goalie_prior_value) for t in teams], dtype=float)
        cols[f"{side}_goalie_id"] = ids
        cols[f"{side}_goalie_name"] = names
        cols[f"{side}_goalie_status"] = status
        cols[f"{side}_goalie_value"] = vals
        cols[f"{side}_goalie_adj"] = vals - behind
    return pd.DataFrame(cols, index=games.index)
