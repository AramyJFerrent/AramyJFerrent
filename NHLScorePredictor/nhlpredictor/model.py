"""From pregame features to goal rates and full score distributions.

Fitted on recent seasons each time it runs:

1. A Poisson regression for each team's regulation goals with both goalies in:
   log rate = log(league scoring level) + its 5-on-5 xG rating against the
   opponent's, both teams' goals ratings, the opposing starter's value, the
   Elo edge, home ice, back-to-backs and playoffs.
2. The score simulator, fitted on minute-by-minute game states and tuned so
   the overtime rate, the spread of regulation margins and the share of
   games with an empty-net goal match history.
3. The market blend weight, once enough logged games have betting lines
   (see ``market.py``).
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace

import numpy as np
import pandas as pd

from .goalies import SHOTS_PER_GAME
from .simulate import SimParams, calibrate, fit_from_states, margin_shares, simulate, summarize

# Power-play and penalty-drawing ratings (``pp_*``, ``draw_*``) are built and
# shown, but in walk-forward tests they added nothing once the goals rating,
# which already carries power-play scoring, was in. Elo's result-based edge did.
RATE_FEATURES = ["ev_off", "ev_def", "goals_off", "goals_def", "goalie", "goalie_adj", "elo",
                 "home", "b2b", "b2b_opp", "playoff"]
RIDGE = 5.0


def team_view(f: pd.DataFrame) -> pd.DataFrame:
    """Two rows per game, one from each team's attacking side, with the rate features."""
    sides = []
    for side, other, sign in (("home", "away", 1.0), ("away", "home", -1.0)):
        sides.append(pd.DataFrame({
            "game_id": f["game_id"].to_numpy(),
            "side": side,
            "ev_off": f[f"off_ev_{side}"].to_numpy(),
            "ev_def": f[f"def_ev_{other}"].to_numpy(),
            "pp_off": f[f"off_pp_{side}"].to_numpy(),
            "pp_def": f[f"def_pp_{other}"].to_numpy(),
            "draw_off": f[f"off_draw_{side}"].to_numpy(),
            "draw_def": f[f"def_draw_{other}"].to_numpy(),
            "goals_off": f[f"off_goals_{side}"].to_numpy(),
            "goals_def": f[f"def_goals_{other}"].to_numpy(),
            "goalie": f[f"{other}_goalie_value"].to_numpy() * SHOTS_PER_GAME / 100.0,
            "goalie_adj": f[f"{other}_goalie_adj"].to_numpy() * SHOTS_PER_GAME / 100.0,
            "elo": sign * f["elo_edge"].to_numpy(),
            "home": np.where(f["neutral"], 0.0, 0.5 * sign),
            "b2b": (f[f"{side}_rest"] <= 1).astype(float).to_numpy(),
            "b2b_opp": (f[f"{other}_rest"] <= 1).astype(float).to_numpy(),
            "playoff": f["playoff"].astype(float).to_numpy(),
            "env": f["env_goals"].to_numpy(),
            "goals": f[f"{side}_reg"].to_numpy() if f"{side}_reg" in f else np.nan,
        }))
    return pd.concat(sides, ignore_index=True)


def fit_poisson(X: np.ndarray, y: np.ndarray, offset: np.ndarray, ridge: float = RIDGE,
                iters: int = 50) -> np.ndarray:
    """Poisson regression with a log link by iteratively reweighted least squares."""
    beta = np.zeros(X.shape[1])
    beta[0] = np.log(y.mean() / np.exp(offset).mean())
    penalty = np.full(X.shape[1], ridge)
    penalty[0] = 0.0
    for _ in range(iters):
        eta = offset + X @ beta
        mu = np.exp(eta)
        z = eta - offset + (y - mu) / mu
        A = (X * mu[:, None]).T @ X + np.diag(penalty)
        new = np.linalg.solve(A, (X * mu[:, None]).T @ z)
        if np.max(np.abs(new - beta)) < 1e-8:
            beta = new
            break
        beta = new
    return beta


@dataclass
class GoalModel:
    coef: dict = field(default_factory=dict)
    intercept: float = 0.0
    sim: SimParams = field(default_factory=SimParams)
    tie_rate: float = 0.224
    fit_games: int = 0
    fit_seasons: tuple = ()

    # ---- fitting -------------------------------------------------------
    @classmethod
    def fit(cls, f: pd.DataFrame, states: pd.DataFrame | None = None, features=RATE_FEATURES,
            calibrate_sim: bool = True) -> "GoalModel":
        f = f[f["completed"] & f["home_reg"].notna()].reset_index(drop=True)
        tv = team_view(f)
        X = np.column_stack([np.ones(len(tv)), tv[features].to_numpy(float)])
        beta = fit_poisson(X, tv["goals"].to_numpy(float), np.log(tv["env"].to_numpy(float)))
        m = cls(coef=dict(zip(features, map(float, beta[1:]))), intercept=float(beta[0]),
                fit_games=len(f), fit_seasons=tuple(sorted(f["season"].unique().tolist())))
        regular = f[~f["playoff"]]
        m.tie_rate = float((regular["periods"] > 3).mean()) if len(regular) else m.tie_rate
        if calibrate_sim and states is not None:
            recent = states[states["season"] >= max(f["season"].max() - 2, states["season"].min())]
            params = fit_from_states(recent)
            rates = m.rates(regular)
            m.sim = calibrate(params, rates["home"], rates["away"], m.tie_rate,
                              margin_shares(regular["home_reg"], regular["away_reg"]),
                              float(((regular["home_en"] + regular["away_en"]) > 0).mean()))
        return m

    # ---- prediction ----------------------------------------------------
    def rates(self, f: pd.DataFrame) -> dict:
        """Expected regulation goals with both goalies in, for each side."""
        tv = team_view(f)
        names = list(self.coef)
        beta = np.array([self.coef[k] for k in names])
        lam = tv["env"].to_numpy(float) * np.exp(self.intercept + tv[names].to_numpy(float) @ beta)
        n = len(f)
        return {"home": lam[:n], "away": lam[n:]}

    def predict(self, f: pd.DataFrame, home_rate=None, away_rate=None, n_sims: int = 10000,
                seed: int = 0) -> pd.DataFrame:
        """Simulated outcomes from the model's rates, or from given (blended) rates."""
        own = self.rates(f)
        lh = own["home"] if home_rate is None else np.asarray(home_rate, dtype=float)
        la = own["away"] if away_rate is None else np.asarray(away_rate, dtype=float)
        sim = simulate(lh, la, self.sim, n_sims=n_sims, playoff=f["playoff"].to_numpy(), seed=seed)
        out = summarize(sim)
        out.insert(0, "game_id", f["game_id"].to_numpy())
        out["model_home_rate"] = own["home"]
        out["model_away_rate"] = own["away"]
        out["home_rate"] = lh
        out["away_rate"] = la
        return out, sim

    # ---- persistence ---------------------------------------------------
    def to_dict(self) -> dict:
        return {"coef": self.coef, "intercept": self.intercept, "sim": self.sim.to_dict(),
                "tie_rate": self.tie_rate, "fit_games": self.fit_games,
                "fit_seasons": list(self.fit_seasons)}

    @classmethod
    def from_dict(cls, d: dict) -> "GoalModel":
        d = dict(d)
        d["sim"] = SimParams.from_dict(d["sim"])
        d["fit_seasons"] = tuple(d.get("fit_seasons", ()))
        return cls(**d)

    def with_sim(self, sim: SimParams) -> "GoalModel":
        return replace(self, sim=sim)
