"""Quarterback adjustment.

A team's offensive rating is built from plays run by whichever quarterbacks
played. When the starter changes (an injury, a benching), the rating
misstates the offense until it has seen enough of the new one. Each
quarterback gets a value, EPA per dropback relative to the league that
season, recency weighted and shrunk toward a below-average prior in
proportion to how few dropbacks support it. Values follow the player across
transfers, since they are keyed by athlete id.

No free source names college starters before kickoff, so the starter is the
quarterback with the most dropbacks in the team's latest game. The adjustment
is his value minus the dropback-weighted value of this season's quarterbacks
behind the rating; before a team's first game it is zero, since the
preseason prior already accounts for who returns.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .config import Hyperparams

WEEKS_PER_SEASON = 25
DROPBACKS_PER_GAME = 35.0


class QBModel:
    def __init__(self, qbs: pd.DataFrame, hp: Hyperparams):
        self.hp = hp
        q = qbs.dropna(subset=["qb_id"]).copy()
        q["widx"] = q["season"] * WEEKS_PER_SEASON + q["week"]
        self.q = q.reset_index(drop=True)

    def _before(self, season: int, week: int) -> pd.DataFrame:
        q = self.q
        return q[(q["season"] < season) | ((q["season"] == season) & (q["week"] < week))]

    def values(self, season: int, week: int) -> pd.Series:
        """Shrunk EPA per dropback above league average, by quarterback id."""
        q = self._before(season, week)
        q = q[q["w"] > 0]
        if q.empty:
            return pd.Series(dtype=float)
        league = q.groupby("season")[["epa", "w"]].sum()
        league = league["epa"] / league["w"]
        rel = q["epa"] - q["w"] * q["season"].map(league)
        decay = 0.5 ** ((season * WEEKS_PER_SEASON + week - q["widx"]) / self.hp.qb_half_life_weeks)
        num = (decay * rel).groupby(q["qb_id"]).sum()
        den = (decay * q["w"]).groupby(q["qb_id"]).sum()
        k = self.hp.qb_prior_dropbacks
        return (num + k * self.hp.qb_prior_value) / (den + k)

    def adjustments(self, games: pd.DataFrame, season: int, week: int) -> pd.DataFrame:
        """The projected starter, his value and the adjustment (EPA per dropback) for each side."""
        values = self.values(season, week)
        cur = self.q[(self.q["season"] == season) & (self.q["week"] < week)]
        wt = cur["w"] * 0.5 ** ((week - cur["week"]) / self.hp.half_life_weeks)
        v = cur["qb_id"].map(values).fillna(self.hp.qb_prior_value)
        mix = (wt * v).groupby(cur["team"]).sum() / wt.groupby(cur["team"]).sum().replace(0, np.nan)
        latest = cur.sort_values(["widx", "dropbacks"]).groupby("team").tail(1).set_index("team")
        out = pd.DataFrame(index=games.index)
        for side in ("home", "away"):
            team = games[f"{side}_team"]
            starter = team.map(latest["qb_id"])
            value = starter.map(values).astype(float)
            out[f"{side}_qb_name"] = team.map(latest["qb_name"])
            out[f"{side}_qb_value"] = value
            out[f"{side}_qb_adj"] = (value - team.map(mix)).fillna(0.0)
        return out
