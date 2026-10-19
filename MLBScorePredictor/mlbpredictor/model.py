"""From pregame features to expected runs per inning and full score distributions.

Fitted on recent seasons each time it runs:

1. The run model. A team's expected runs in inning ``i`` are

       env × exp(c + a_i + b · other terms)
           × [s_i · exp(b_sp·x_sp) + (1 − s_i) · exp(b_bp·x_bp)]

   where ``env`` is the league's current runs per inning, ``a_i`` the inning's
   own level (the first inning, with the top of the order up, scores most),
   ``s_i`` the opposing starter's expected share of the inning, ``x_sp``
   and ``x_bp`` the lineup's matchups against the starter and the bullpen,
   and the other terms (in ``FEATURES``) park, home field, weather, the team
   ratings and the Elo edge.
   It is fitted by Poisson likelihood on runs in innings 1-8, which both
   teams always bat.
2. The simulator's game-level spread and walk-off settings, tuned so
   simulated scores match the same seasons' real ones.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace

import numpy as np
import pandas as pd
from scipy.optimize import minimize

from .simulate import SimParams, simulate, summarize

INNINGS = 9
# Team ratings and the Elo edge catch what the player ratings miss (fielding,
# baserunning, how a staff is used); bullpen workload added nothing once the
# bullpen weights already mark tired relievers down.
FEATURES = ["log_pf", "h", "temp_x", "wind_x", "team_off", "team_def", "elo"]
FRAILTY_GRID = (8.0, 12.0, 20.0, 35.0, 60.0, 120.0, np.inf)
CLOSER_GRID = (0.5, 0.6, 0.7, 0.8, 0.9, 1.0)
WALKOFF_GRID = (0.15, 0.25, 0.35, 0.45, 0.55)


def team_view(f: pd.DataFrame) -> pd.DataFrame:
    """Two rows per game, one for each batting side."""
    sides = []
    for side in ("home", "away"):
        d = pd.DataFrame({
            "game_id": f["game_id"].to_numpy(), "side": side,
            "env": f["env"].to_numpy(float), "log_pf": f["log_pf"].to_numpy(float),
            "h": f[f"{side}_h"].to_numpy(float), "temp_x": f["temp_x"].to_numpy(float),
            "wind_x": f["wind_x"].to_numpy(float),
            "x_sp": f[f"{side}_x_sp"].to_numpy(float), "x_bp": f[f"{side}_x_bp"].to_numpy(float),
            "team_off": f[f"{side}_team_off"].to_numpy(float) if f"{side}_team_off" in f else 0.0,
            "team_def": f[f"{side}_team_def"].to_numpy(float) if f"{side}_team_def" in f else 0.0,
            "elo": (0.5 if side == "home" else -0.5) * f["elo_logit"].to_numpy(float) if "elo_logit" in f else 0.0,
            "bp_load": f[f"{side}_opp_bp_load"].to_numpy(float) if f"{side}_opp_bp_load" in f else 0.0,
            "innings": (f["sched_innings"].fillna(9).astype(int) - 1).to_numpy(),
            "runs": f[f"{side}_r8"].to_numpy(float) if f"{side}_r8" in f else np.nan,
        })
        shares = np.column_stack([f[f"{side}_s{i}"].to_numpy(float) for i in range(1, INNINGS + 1)])
        sides.append((d, shares))
    return pd.concat([s[0] for s in sides], ignore_index=True), np.vstack([s[1] for s in sides])


@dataclass
class RunModel:
    coef: dict = field(default_factory=dict)
    inning: list = field(default_factory=lambda: [0.0] * INNINGS)
    sim: SimParams = field(default_factory=SimParams)
    fit_games: int = 0
    fit_seasons: tuple = ()
    targets: dict = field(default_factory=dict)

    # ---- fitting -------------------------------------------------------
    @classmethod
    def fit(cls, f: pd.DataFrame, chain=None, features=FEATURES, calibrate_sim: bool = True) -> "RunModel":
        f = f[f["completed"] & f["home_r8"].notna() & f["away_r8"].notna()].reset_index(drop=True)
        tv, shares = team_view(f)
        side_lines = pd.concat([f["home_line"], f["away_line"]], ignore_index=True).fillna("").str.split()
        runs = np.full((len(tv), 8), np.nan)
        for r, parts in enumerate(side_lines):
            for i, v in enumerate(parts[:8]):
                if v != "x":
                    runs[r, i] = float(v)
        upto = ((np.arange(8)[None, :] < tv["innings"].to_numpy()[:, None]) & np.isfinite(runs)).astype(float)
        y = np.nan_to_num(runs)
        s8 = shares[:, :8]
        X = tv[list(features)].to_numpy(float)
        x_sp, x_bp = tv["x_sp"].to_numpy(float), tv["x_bp"].to_numpy(float)
        env = tv["env"].to_numpy(float)
        n_a = 8 - 1
        n_obs = upto.sum()

        def nll(params):
            """Poisson likelihood of each inning's runs, with its gradient."""
            c, b_sp, b_bp = params[:3]
            a = np.concatenate([[0.0], params[3:3 + n_a]])
            z = c + X @ params[3 + n_a:]
            A, B = np.exp(b_sp * x_sp), np.exp(b_bp * x_bp)
            base = env[:, None] * np.exp(z[:, None] + a[None, :])            # (n, 8)
            mu = base * (s8 * A[:, None] + (1 - s8) * B[:, None])
            g = (1.0 - y / mu) * upto / n_obs
            grad = np.empty_like(params)
            grad[0] = np.sum(g * mu)
            grad[1] = np.sum(g * base * s8 * (A * x_sp)[:, None])
            grad[2] = np.sum(g * base * (1 - s8) * (B * x_bp)[:, None])
            grad[3:3 + n_a] = (g * mu).sum(axis=0)[1:]
            grad[3 + n_a:] = (g * mu).sum(axis=1) @ X
            return float(np.sum((mu - y * np.log(mu)) * upto) / n_obs), grad

        x0 = np.zeros(3 + n_a + len(features))
        x0[1] = x0[2] = 1.0
        res = minimize(nll, x0, jac=True, method="L-BFGS-B")
        p = res.x
        a = np.concatenate([[0.0], p[3:3 + INNINGS - 2]])
        # The ninth inning (and extras) from line scores: the visitors' ninth relative to their eighth.
        away9 = f["away_line"].fillna("").str.split().map(lambda s: float(s[8]) if len(s) > 8 and s[8] != "x" else np.nan)
        away8 = f["away_line"].fillna("").str.split().map(lambda s: float(s[7]) if len(s) > 7 and s[7] != "x" else np.nan)
        ok = away9.notna() & away8.notna() & f["sched_innings"].eq(9)
        a9 = a[7] + np.log(max(away9[ok].mean(), 1e-3) / max(away8[ok].mean(), 1e-3)) if ok.any() else a[7]
        m = cls(coef={"const": float(p[0]), "x_sp": float(p[1]), "x_bp": float(p[2]),
                      **{k: float(v) for k, v in zip(features, p[3 + INNINGS - 2:])}},
                inning=[float(v) for v in a] + [float(a9)],
                fit_games=len(f), fit_seasons=tuple(sorted(int(s) for s in f["season"].unique())))
        if calibrate_sim and chain is not None:
            m.sim = m.calibrate(f, SimParams(tables=chain.tables()))
        return m

    # ---- prediction ----------------------------------------------------
    def inning_rates(self, f: pd.DataFrame) -> dict:
        """Expected runs by inning for each batting side, plus each side's extra-inning rate."""
        tv, shares = team_view(f)
        features = [k for k in self.coef if k not in ("const", "x_sp", "x_bp")]
        betas = np.array([self.coef[k] for k in features])
        z = self.coef["const"] + (tv[features].to_numpy(float) @ betas if features else 0.0)
        a = np.asarray(self.inning)
        sp = np.exp(self.coef["x_sp"] * tv["x_sp"].to_numpy())[:, None]
        bp = np.exp(self.coef["x_bp"] * tv["x_bp"].to_numpy())[:, None]
        mu = tv["env"].to_numpy()[:, None] * np.exp(z[:, None] + a[None, :]) * (shares * sp + (1 - shares) * bp)
        extra = tv["env"].to_numpy() * np.exp(z + a[-1]) * bp[:, 0]
        n = len(f)
        return {"home": mu[:n], "away": mu[n:], "home_extra": extra[:n], "away_extra": extra[n:]}

    def expected_runs(self, f: pd.DataFrame) -> dict:
        """Expected runs over nine full innings for each side (before game structure)."""
        r = self.inning_rates(f)
        return {"home": r["home"].sum(axis=1), "away": r["away"].sum(axis=1)}

    def predict(self, f: pd.DataFrame, home_scale=None, away_scale=None, n_sims: int = 10000,
                seed: int = 0) -> tuple[pd.DataFrame, dict]:
        """Simulated outcomes from the model's inning rates, optionally scaled
        (the market blend scales each side's whole profile)."""
        r = self.inning_rates(f)
        hs = np.ones(len(f)) if home_scale is None else np.asarray(home_scale, dtype=float)
        as_ = np.ones(len(f)) if away_scale is None else np.asarray(away_scale, dtype=float)
        ghost = (f["tiebreaker"].fillna(0).astype(int) == 1).to_numpy()
        sim = simulate(r["home"] * hs[:, None], r["away"] * as_[:, None], r["home_extra"] * hs,
                       r["away_extra"] * as_, self.sim, n_sims=n_sims, ghost=ghost,
                       sched_innings=f["sched_innings"].fillna(9).astype(int).to_numpy(), seed=seed)
        out = summarize(sim)
        out.insert(0, "game_id", f["game_id"].to_numpy())
        out["model_home_runs"] = r["home"].sum(axis=1)
        out["model_away_runs"] = r["away"].sum(axis=1)
        out["home_runs9"] = out["model_home_runs"] * hs
        out["away_runs9"] = out["model_away_runs"] * as_
        return out, sim

    # ---- simulator calibration ----------------------------------------------
    def calibrate(self, f: pd.DataFrame, params: SimParams, max_games: int = 1500, n_sims: int = 200,
                  seed: int = 3) -> SimParams:
        """Pick the game-level spread so simulated team scores spread like real
        ones, the closer effect so as many games reach extra innings, then the
        walk-off home-run share so walk-off margins match."""
        rng = np.random.default_rng(seed)
        f = f.iloc[rng.permutation(len(f))[:max_games]].reset_index(drop=True)
        actual = np.concatenate([f["home_score"], f["away_score"]]).astype(float)
        target_var = float(np.var(actual))
        target_zero = float(np.mean(actual == 0))
        best, best_err = params, np.inf
        for k in FRAILTY_GRID:
            trial = replace(params, frailty=k)
            _, sim = replace(self, sim=trial).predict(f, n_sims=n_sims, seed=seed)
            pooled = np.concatenate([sim["home"].ravel(), sim["away"].ravel()]).astype(float)
            err = (np.var(pooled) / target_var - 1) ** 2 + ((np.mean(pooled == 0) - target_zero) / 0.02) ** 2 * 0.1
            if err < best_err:
                best, best_err = trial, err
        # The closer effect, so as many regular-season games go to extra innings as in history.
        reg = f[(f["game_type"] == "R") & (f["sched_innings"] == 9)]
        extra = float((reg["innings"] > 9).mean()) if len(reg) else float("nan")
        if np.isfinite(extra):
            best = replace(best, closer_share=closer_share(reg))
            errs = {}
            for c in CLOSER_GRID:
                trial = replace(best, closer_mult=c)
                _, sim = replace(self, sim=trial).predict(reg.reset_index(drop=True), n_sims=n_sims, seed=seed + 2)
                errs[c] = abs(float((sim["innings"] > 9).mean()) - extra)
            best = replace(best, closer_mult=min(errs, key=errs.get))
            self.targets["extra_innings"] = extra
        target = self.targets.get("walkoff_multi")
        walk = walkoff_margins(f)
        self.targets.update({"team_runs_var": target_var, "shutout": target_zero,
                             "walkoff_multi": walk if target is None else target})
        if np.isfinite(walk):
            errs = {}
            for q in WALKOFF_GRID:
                trial = replace(best, walkoff_hr=q)
                _, sim = replace(self, sim=trial).predict(f, n_sims=n_sims, seed=seed + 1)
                wo = sim["walkoff"]
                margin = sim["home"] - sim["away"]
                share = float(np.sum(wo & (margin >= 2)) / max(np.sum(wo), 1))
                errs[q] = abs(share - walk)
            best = replace(best, walkoff_hr=min(errs, key=errs.get))
        return best

    # ---- persistence ---------------------------------------------------
    def to_dict(self) -> dict:
        return {"coef": self.coef, "inning": self.inning, "sim": self.sim.to_dict(), "fit_games": self.fit_games,
                "fit_seasons": list(self.fit_seasons), "targets": self.targets}


def walkoff_margins(f: pd.DataFrame) -> float:
    """Share of walk-off wins decided by two or more runs (home runs with men on)."""
    lines = f["home_line"].fillna("").str.split()
    batted_last = lines.map(lambda s: len(s) > 0 and s[-1] != "x")
    innings = lines.map(len)
    walk = f["completed"] & batted_last & (f["home_score"] > f["away_score"]) & (innings >= f["sched_innings"])
    if not walk.any():
        return float("nan")
    return float(((f["home_score"] - f["away_score"])[walk] >= 2).mean())


def closer_share(f: pd.DataFrame) -> float:
    """Share of top-of-the-ninth half-innings that start with the visitors behind by one to three."""
    away = f["away_line"].fillna("").str.split()
    home = f["home_line"].fillna("").str.split()
    margins = [sum(int(v) for v in a[:8] if v != "x") - sum(int(v) for v in h[:8] if v != "x")
               for a, h in zip(away, home) if len(a) >= 9]
    m = np.asarray(margins)
    return float(np.mean((m <= -1) & (m >= -3))) if len(m) else 0.3
