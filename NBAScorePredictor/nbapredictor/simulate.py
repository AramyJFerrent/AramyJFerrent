"""Turn expected points into a distribution of real NBA scores.

Each team's regulation points are drawn from a bivariate normal around its
expected points: a common spread for both teams and a positive correlation,
because pace and the officiating affect both sides. The two are fitted so the
simulated margin and total scatter like real results around the prediction
(``sd² = (margin sd² + total sd²) / 4`` and ``rho = (total sd² − margin sd²) /
(total sd² + margin sd²)``), and each game's spread grows with its expected
scoring, since more possessions mean more variance.

Late-game play bunches regulation margins at zero: a trailing team plays for
the tie, so real games are tied after 48 minutes about twice as often as a
smooth distribution says, and 1-4 point margins are rarer. Each simulated game
is weighted by its regulation margin so those frequencies match history (the
NFL predictor's key-number weights, applied before overtime). Tied games go to
five-minute overtimes, each team scoring at its regulation rate, until one
leads.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field, replace

import numpy as np
import pandas as pd

from .config import OT_MINUTES, REG_MINUTES

MAX_MARGIN = 40
MAX_OVERTIMES = 6


@dataclass
class SimParams:
    sd: float = 11.0                # regulation points SD per team, at the reference total
    rho: float = 0.3                # correlation of the two teams' regulation points
    ref_total: float = 225.0        # expected total the SD refers to
    ot_scale: float = 1.0           # overtime scoring relative to the regulation rate
    # Weight on each absolute regulation margin, fitted so simulated games end
    # regulation tied, or close, as often as real ones. Margins not listed weigh 1.
    margin_weights: dict = field(default_factory=dict)

    def weights(self, reg_margin: np.ndarray) -> np.ndarray:
        if not self.margin_weights:
            return np.ones(reg_margin.shape)
        table = np.ones(MAX_MARGIN + 1)
        for k, v in self.margin_weights.items():
            table[int(k)] = v
        return table[np.minimum(np.abs(reg_margin), MAX_MARGIN)]

    def to_dict(self) -> dict:
        d = asdict(self)
        d["margin_weights"] = {str(k): round(v, 4) for k, v in self.margin_weights.items()}
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "SimParams":
        d = dict(d)
        d["margin_weights"] = {int(k): v for k, v in d.get("margin_weights", {}).items()}
        return cls(**d)


@dataclass
class Simulation:
    home: np.ndarray        # final points, (n_games, n_sims)
    away: np.ndarray
    reg_margin: np.ndarray  # home minus away after regulation
    periods: np.ndarray     # 4 plus overtimes played
    weights: np.ndarray     # normalized per game


def _bivariate(rng, mu_h, mu_a, sd, rho, n_sims) -> tuple[np.ndarray, np.ndarray]:
    z1 = rng.standard_normal((len(mu_h), n_sims))
    z2 = rng.standard_normal((len(mu_h), n_sims))
    h = mu_h[:, None] + sd[:, None] * z1
    a = mu_a[:, None] + sd[:, None] * (rho * z1 + np.sqrt(1 - rho ** 2) * z2)
    return h, a


def simulate(home_mean, away_mean, params: SimParams, n_sims: int = 10000, seed: int | None = 0) -> Simulation:
    """Simulate final scores from expected regulation points."""
    rng = np.random.default_rng(seed)
    mu_h = np.atleast_1d(np.asarray(home_mean, dtype=float))
    mu_a = np.atleast_1d(np.asarray(away_mean, dtype=float))
    sd = params.sd * np.sqrt(np.clip((mu_h + mu_a) / params.ref_total, 0.5, 2.0))
    h, a = _bivariate(rng, mu_h, mu_a, sd, params.rho, n_sims)
    home = np.rint(h).astype(np.int64)
    away = np.rint(a).astype(np.int64)
    reg_margin = home - away
    periods = np.full(home.shape, 4, dtype=np.int64)
    frac = OT_MINUTES / REG_MINUTES
    ot_sd = sd * np.sqrt(frac)
    for _ in range(MAX_OVERTIMES):
        tied = home == away
        if not tied.any():
            break
        oh, oa = _bivariate(rng, mu_h * frac * params.ot_scale, mu_a * frac * params.ot_scale, ot_sd,
                            params.rho, n_sims)
        home = home + np.where(tied, np.rint(oh).astype(np.int64), 0)
        away = away + np.where(tied, np.rint(oa).astype(np.int64), 0)
        periods = periods + tied
    still = home == away
    if still.any():
        coin = rng.random(home.shape) < 0.5
        home = home + (still & coin)
        away = away + (still & ~coin)
    w = params.weights(reg_margin)
    return Simulation(home, away, reg_margin, periods, w / w.sum(axis=1, keepdims=True))


def _weighted_quantile(values: np.ndarray, weights: np.ndarray, q: float) -> float:
    order = np.argsort(values, kind="stable")
    cum = np.cumsum(weights[order])
    return float(values[order][min(np.searchsorted(cum, q * cum[-1]), len(order) - 1)])


def headline_score(home_mean: float, away_mean: float) -> tuple[int, int]:
    """Expected points rounded, with the favorite ahead (a tie is not a final score)."""
    h, a = int(round(home_mean)), int(round(away_mean))
    if h == a:
        if home_mean >= away_mean:
            h += 1
        else:
            a += 1
    return h, a


def summarize(sim: Simulation) -> pd.DataFrame:
    """Win probability, overtime, ranges and expected points for each game."""
    w = sim.weights
    margin = sim.home - sim.away
    rows = []
    for i in range(sim.home.shape[0]):
        exp_h = float(w[i] @ sim.home[i])
        exp_a = float(w[i] @ sim.away[i])
        head_h, head_a = headline_score(exp_h, exp_a)
        rows.append({
            "home_win_prob": float(w[i][margin[i] > 0].sum()),
            "away_win_prob": float(w[i][margin[i] < 0].sum()),
            "ot_prob": float(w[i][sim.periods[i] > 4].sum()),
            "sim_home": exp_h, "sim_away": exp_a, "sim_total": exp_h + exp_a,
            "home_low": int(_weighted_quantile(sim.home[i], w[i], 0.10)),
            "home_high": int(_weighted_quantile(sim.home[i], w[i], 0.90)),
            "away_low": int(_weighted_quantile(sim.away[i], w[i], 0.10)),
            "away_high": int(_weighted_quantile(sim.away[i], w[i], 0.90)),
            "margin_low": int(_weighted_quantile(margin[i], w[i], 0.10)),
            "margin_high": int(_weighted_quantile(margin[i], w[i], 0.90)),
            "total_low": int(_weighted_quantile(sim.home[i] + sim.away[i], w[i], 0.10)),
            "total_high": int(_weighted_quantile(sim.home[i] + sim.away[i], w[i], 0.90)),
            "headline_home": head_h, "headline_away": head_a,
        })
    return pd.DataFrame(rows)


def cover_prob(sim: Simulation, spread: np.ndarray) -> np.ndarray:
    """Chance the home team beats ``spread`` (its expected margin in the line),
    pushes counted as half."""
    margin = sim.home - sim.away
    s = np.asarray(spread, dtype=float)[:, None]
    return ((sim.weights * (margin > s)).sum(axis=1) + 0.5 * (sim.weights * (margin == s)).sum(axis=1))


def over_prob(sim: Simulation, total: np.ndarray) -> np.ndarray:
    """Chance the combined score goes over ``total``, pushes counted as half."""
    t = sim.home + sim.away
    line = np.asarray(total, dtype=float)[:, None]
    return ((sim.weights * (t > line)).sum(axis=1) + 0.5 * (sim.weights * (t == line)).sum(axis=1))


def line_probs(sim: Simulation, spread, total) -> dict:
    """The chances a bet needs, from one simulation: the home team beating
    ``spread`` (its expected margin in the line) outright and landing on it,
    and the total going over ``total`` and landing on it. NaN where there is no line. Named for its use on
    the model-only simulation, where the betting edges come from."""
    out = {}
    for name, values, line in (("spread", sim.home - sim.away, spread), ("total", sim.home + sim.away, total)):
        line = np.atleast_1d(np.asarray(line, dtype=float))
        at = np.nan_to_num(line)[:, None]
        above = (sim.weights * (values > at)).sum(axis=1)
        on = (sim.weights * (values == at)).sum(axis=1)
        out[name] = (np.where(np.isnan(line), np.nan, above), np.where(np.isnan(line), np.nan, on))
    return {"model_home_cover_prob": out["spread"][0], "model_spread_push_prob": out["spread"][1],
            "model_over_prob": out["total"][0], "model_total_push_prob": out["total"][1]}


def spread_params(margin_sd: float, total_sd: float) -> tuple[float, float]:
    """Per-team SD and correlation that give these margin and total SDs."""
    sd = float(np.sqrt((margin_sd ** 2 + total_sd ** 2) / 4.0))
    rho = float((total_sd ** 2 - margin_sd ** 2) / (total_sd ** 2 + margin_sd ** 2))
    return sd, float(np.clip(rho, -0.5, 0.8))


def fit_margin_weights(params: SimParams, home_mean, away_mean, actual_reg_margin,
                       n_sims: int = 2000, pseudo_count: float = 30.0) -> SimParams:
    """Reweight absolute regulation margins so simulated frequencies match history.

    Each past game is simulated from its own expected points, the expected
    count of every regulation margin is compared with how many games actually
    ended regulation on it, and the ratio (shrunk toward 1) becomes its weight.
    """
    base = replace(params, margin_weights={})
    sim = simulate(home_mean, away_mean, base, n_sims=n_sims, seed=7)
    sim_abs = np.minimum(np.abs(sim.reg_margin), MAX_MARGIN)
    expected = np.bincount(sim_abs.ravel(), minlength=MAX_MARGIN + 1) / n_sims
    actual_abs = np.minimum(np.abs(np.asarray(actual_reg_margin, dtype=int)), MAX_MARGIN)
    actual = np.bincount(actual_abs, minlength=MAX_MARGIN + 1)
    ratio = np.clip((actual + pseudo_count) / (expected + pseudo_count), 0.3, 3.0)
    return replace(params, margin_weights={k: float(ratio[k]) for k in range(MAX_MARGIN + 1)})
