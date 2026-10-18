"""Preseason priors: where each team should start before it plays.

With about 12 games per team and heavy roster turnover, the prior carries most
of the weight for the first month. It is a regression, fitted on earlier
seasons only, of each team's rating for a season on what was known before it:

- last season's rating,
- program history (the average rating of the three seasons before that),
- returning production (shares of last season's yards and defensive plays on
  this season's roster, transfers included), on its own and interacted with
  last season's rating, so a team that returns little regresses further,
- an FCS indicator.

Offense and defense are fitted separately. The ratings regressed on are
"season-only" ratings: each season's games on their own, lightly shrunk
toward the team's conference, so the prior is never fitted on itself.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .ratings import Ratings, Target, conference_key, fit

# Season-only fits: light shrinkage, toward the conference rather than zero.
SEASON_ONLY_TEAM = {"epa": 250.0, "st": 4.0, "pace": 2.0}
SEASON_ONLY_CONF = {"epa": 400.0, "st": 6.0, "pace": 4.0}
HISTORY_SEASONS = 3
# Used before there is a season of history to fit on.
DEFAULT_KEEP = {"off": 0.6, "def": 0.5}
# Shrinkage of the prior regression's coefficients, in team-seasons.
COEF_RIDGE = 5.0


def _side_features(side: str, with_returning: bool) -> list[str]:
    feats = [f"last_{side}", f"hist_{side}", "fcs"]
    if with_returning:
        ret = "ret_off" if side == "off" else "ret_def"
        feats += [ret, f"last_{side}_x_ret"]
        if side == "off":
            feats.append("ret_pass")
    return feats


class PriorModel:
    """Season-only ratings and the preseason prior regression for one target."""

    def __init__(self, rows: pd.DataFrame, target: Target, returning: pd.DataFrame | None,
                 members: dict[int, dict[str, tuple[str, str]]], ridge: float = COEF_RIDGE):
        self.target = target
        self.by_season = {s: r.reset_index(drop=True) for s, r in rows.groupby("season")}
        self.returning = returning if returning is not None and len(returning) else None
        self.members = members
        self.ridge = ridge
        self._season_only: dict[int, Ratings] = {}
        self._features: dict[int, pd.DataFrame] = {}
        self._coefs: dict[int, dict] = {}
        self._priors: dict[int, Ratings] = {}

    # ---- season-only ratings --------------------------------------------
    def season_only(self, season: int) -> Ratings | None:
        if season not in self.by_season:
            return None
        if season not in self._season_only:
            rows = self.by_season[season]
            name = self.target.name
            loose = Target(name, self.target.value, self.target.weight,
                           SEASON_ONLY_TEAM[name], SEASON_ONLY_TEAM[name], SEASON_ONLY_CONF[name],
                           self.target.league_prior, self.target.home_prior, self.target.fcs_prior)
            conferences = {t: c for t, (c, _) in self.members.get(season, {}).items()}
            self._season_only[season] = fit(rows, rows["week"].max() + 1, Ratings(), loose,
                                            half_life_weeks=1e9, conferences=conferences)
        return self._season_only[season]

    # ---- features -------------------------------------------------------
    def features(self, season: int) -> pd.DataFrame:
        """One row per team known in ``season`` with what was known before it."""
        if season in self._features:
            return self._features[season]
        teams = set(self.members.get(season, {}))
        if season in self.by_season:
            rows = self.by_season[season]
            teams |= set(rows["team"]) | set(rows["opp"])
        f = pd.DataFrame({"team": sorted(teams)})
        last = self.season_only(season - 1)
        for side, attr in (("off", "off"), ("def", "deff")):
            f[f"last_{side}"] = f["team"].map(getattr(last, attr)) if last else np.nan
            hist = []
            for k in range(2, 2 + HISTORY_SEASONS):
                r = self.season_only(season - k)
                if r is not None:
                    hist.append(f["team"].map(getattr(r, attr)))
            f[f"hist_{side}"] = pd.concat(hist, axis=1).mean(axis=1) if hist else np.nan
            f[f"hist_{side}"] = f[f"hist_{side}"].fillna(f[f"last_{side}"])
        division = {t: d for t, (_, d) in self.members.get(season, {}).items()}
        f["fcs"] = f["team"].map(division).eq("fcs").astype(float)
        if self.returning is not None:
            ret = self.returning[self.returning["season"] == season].set_index("team")
            for col in ("ret_off", "ret_def", "ret_pass"):
                values = f["team"].map(ret[col]) if len(ret) else pd.Series(np.nan, index=f.index)
                # Centered on the season's typical team; unknown counts as typical.
                f[col] = (values - values.median()).fillna(0.0).clip(-1.0, 1.0)
            f["last_off_x_ret"] = f["last_off"] * f["ret_off"]
            f["last_def_x_ret"] = f["last_def"] * f["ret_def"]
        self._features[season] = f
        return f

    # ---- regression -----------------------------------------------------
    def _training(self, season: int, side: str) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        attr = "off" if side == "off" else "deff"
        cols = _side_features(side, self.returning is not None)
        X, y, w = [], [], []
        for s in sorted(self.by_season):
            if s >= season:
                break
            f = self.features(s)
            target = self.season_only(s)
            have = f[f"last_{side}"].notna()
            if not have.any():
                continue
            f = f[have]
            X.append(f[cols].to_numpy(float))
            y.append(f["team"].map(getattr(target, attr)).to_numpy(float))
            w.append(np.minimum(f["team"].map(target.plays).fillna(0.0).to_numpy(float)
                                / (12 * (65.0 if self.target.weight else 1.0)), 1.0))
        if not X:
            return np.empty((0, len(cols))), np.empty(0), np.empty(0)
        return np.vstack(X), np.concatenate(y), np.concatenate(w)

    def coefficients(self, season: int) -> dict:
        """Prior regression fitted on seasons before ``season``."""
        if season in self._coefs:
            return self._coefs[season]
        out = {}
        for side in ("off", "def"):
            cols = _side_features(side, self.returning is not None)
            X, y, w = self._training(season, side)
            ok = ~np.isnan(X).any(axis=1) & ~np.isnan(y) & (w > 0)
            if ok.sum() < 100:
                coef = {c: 0.0 for c in cols}
                coef[f"last_{side}"] = DEFAULT_KEEP[side]
                out[side] = {"intercept": 0.0, **coef}
                continue
            X, y, w = X[ok], y[ok], w[ok]
            Xc = np.column_stack([np.ones(len(X)), X])
            scale = np.concatenate([[0.0], X.var(axis=0) * self.ridge])
            A = (Xc * w[:, None]).T @ Xc + np.diag(scale * w.sum() / len(w))
            beta = np.linalg.solve(A, (Xc * w[:, None]).T @ y)
            out[side] = {"intercept": float(beta[0]), **dict(zip(cols, map(float, beta[1:])))}
        self._coefs[season] = out
        return out

    def prior(self, season: int) -> Ratings:
        if season in self._priors:
            return self._priors[season]
        last = self.season_only(season - 1)
        f = self.features(season)
        coefs = self.coefficients(season)
        r = Ratings(mu=last.mu if last else 0.0, hfa=last.hfa if last else (0.02 if self.target.weight else 0.0),
                    fcs_gap=last.fcs_gap if last else 0.0)
        for side, attr in (("off", "off"), ("def", "deff")):
            c = coefs[side]
            pred = np.full(len(f), c["intercept"])
            for k, v in c.items():
                if k != "intercept":
                    pred = pred + v * f[k].to_numpy(float)
            # Teams with no rating last season start at their conference's level.
            known = f[f"last_{side}"].notna().to_numpy()
            setattr(r, attr, dict(zip(f.loc[known, "team"], map(float, pred[known]))))
        self._priors[season] = r
        return r


def members_from(team_games: pd.DataFrame, games: pd.DataFrame) -> dict[int, dict[str, tuple[str, str]]]:
    """Conference and division of every team in every season, as of that season."""
    parts = [
        team_games[["season", "team", "conference", "division"]],
        games[["season", "home_team", "home_conference", "home_division"]].set_axis(
            ["season", "team", "conference", "division"], axis=1),
        games[["season", "away_team", "away_conference", "away_division"]].set_axis(
            ["season", "team", "conference", "division"], axis=1),
    ]
    m = pd.concat(parts, ignore_index=True).dropna(subset=["team"])
    m = m.drop_duplicates(["season", "team"], keep="last")
    out: dict[int, dict[str, tuple[str, str]]] = {}
    for s, grp in m.groupby("season"):
        out[int(s)] = {t: (conference_key(c, d), d) for t, c, d in
                       zip(grp["team"], grp["conference"], grp["division"])}
    return out
