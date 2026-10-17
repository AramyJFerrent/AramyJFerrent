"""Quarterback adjustment.

A team's offensive rating is built from plays run by whichever quarterbacks
played. When the expected starter differs from that mix (an injury, a benching,
a new signing), the rating misstates the offense. Each quarterback gets a value,
EPA per dropback relative to the league that season, shrunk toward a
below-average prior in proportion to how few dropbacks support it. The
adjustment is the starter's value minus the dropback-weighted value of the
quarterbacks behind the current rating.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .config import Hyperparams

WEEKS_PER_SEASON = 22
# Share of a team's plays that are dropbacks, used to weigh the preseason
# prior's quarterbacks against this season's.
DROPBACK_SHARE = 0.6
DROPBACKS_PER_GAME = 36.0


class QBModel:
    def __init__(self, qbs: pd.DataFrame, hp: Hyperparams):
        self.hp = hp
        q = qbs.copy()
        q["widx"] = q["season"] * WEEKS_PER_SEASON + q["week"]
        self.q = q.reset_index(drop=True)

    def _before(self, season: int, week: int) -> pd.DataFrame:
        q = self.q
        return q[(q["season"] < season) | ((q["season"] == season) & (q["week"] < week))]

    def values(self, season: int, week: int) -> pd.Series:
        """Shrunk EPA per dropback above league average, by QB id."""
        q = self._before(season, week)
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

    def value_of(self, values: pd.Series, qb_id) -> float:
        if isinstance(qb_id, str) and qb_id in values.index:
            return float(values[qb_id])
        return self.hp.qb_prior_value

    def mix(self, season: int, week: int, ref_week: float, values: pd.Series) -> pd.Series:
        """Dropback-weighted value of the QBs behind each team's current rating."""
        q = self.q
        cur = q[(q["season"] == season) & (q["week"] < week)]
        cur_w = cur["dropbacks"] * 0.5 ** ((ref_week - cur["week"]) / self.hp.half_life_weeks)
        last = q[q["season"] == season - 1]
        if len(last):
            raw = last["dropbacks"] * 0.5 ** ((last["week"].max() + 1 - last["week"]) / self.hp.half_life_weeks)
            share = raw / raw.groupby(last["team"]).transform("sum")
            last_w = share * self.hp.off_prior_plays * DROPBACK_SHARE
        else:
            last_w = pd.Series(dtype=float)
        both = pd.concat([cur.assign(wt=cur_w), last.assign(wt=last_w)])
        if both.empty:
            return pd.Series(dtype=float)
        v = both["qb_id"].map(values).fillna(self.hp.qb_prior_value)
        return (both["wt"] * v).groupby(both["team"]).sum() / both["wt"].groupby(both["team"]).sum()

    def recent_starters(self, season: int, week: int) -> pd.DataFrame:
        """Each team's QB with the most dropbacks in its latest game before the cutoff."""
        q = self._before(season, week)
        latest = q.sort_values(["widx", "dropbacks"]).groupby("team").tail(1)
        return latest.set_index("team")[["qb_id", "qb_name"]]


def adjustments(model: QBModel, games: pd.DataFrame, season: int, week: int,
                ref_week: float) -> pd.DataFrame:
    """QB ids and adjustments (EPA per dropback) for the home and away sides."""
    values = model.values(season, week)
    mix = model.mix(season, week, ref_week, values)
    fallback = model.recent_starters(season, week)
    out = pd.DataFrame(index=games.index)
    for side in ("home", "away"):
        teams = games[f"{side}_team"]
        ids = games[f"{side}_qb_id"].copy()
        names = games[f"{side}_qb_name"].copy()
        missing = ids.isna()
        if missing.any():
            ids[missing] = teams[missing].map(fallback["qb_id"])
            names[missing] = teams[missing].map(fallback["qb_name"])
        starter = np.array([model.value_of(values, i) for i in ids])
        behind = teams.map(mix).fillna(model.hp.qb_prior_value).to_numpy()
        out[f"{side}_qb_id"] = ids
        out[f"{side}_qb_name"] = names
        out[f"{side}_qb_value"] = starter
        out[f"{side}_qb_adj"] = starter - behind
    return out
