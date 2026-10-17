"""Turn expected points into a distribution of real NFL scores.

Each team gets a number of scoring chances (shared by both teams, since
possessions alternate). Every chance ends in a touchdown, a field goal or
nothing, touchdowns are followed by an extra point or two-point try, and a
tied game goes to overtime. Simulating drives this way reproduces the key
margins (3, 7, 10, 14) that a smooth distribution misses, and the number of
chances is calibrated so the spread of simulated scores matches how far real
scores land from the prediction.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field, replace

import numpy as np
import pandas as pd
from scipy.stats import norm

# Final margin of non-tied overtime games, 2015 to 2025 (nflverse games file).
OT_MARGINS = {3: 0.62, 6: 0.36, 7: 0.02}
# Margins beyond this share one key-number weight.
MAX_MARGIN = 40


@dataclass
class ScoringModel:
    chances: float = 10.0           # mean scoring chances per team per game
    pace_sd: float = 1.0            # game-to-game spread in chances (shared)
    fg_intercept: float = 1.27      # field goals per game = a + b * expected points
    fg_slope: float = 0.0167
    xp_rate: float = 0.944
    two_point_rate: float = 0.090   # share of touchdowns followed by a 2-pt try
    two_point_success: float = 0.477
    safety_rate: float = 0.028
    ot_tie_prob: float = 0.057      # regular season only
    ot_margins: dict = field(default_factory=lambda: dict(OT_MARGINS))
    # Weight on each absolute final margin, fitted so simulated games land on
    # 3, 7, 10 and 14 as often as real ones do (late-game play to the score
    # that independent drives cannot produce). Margins not listed weigh 1.
    margin_weights: dict = field(default_factory=dict)

    @property
    def points_per_td(self) -> float:
        extra = (1 - self.two_point_rate) * self.xp_rate + 2 * self.two_point_rate * self.two_point_success
        return 6.0 + extra

    def rates(self, mean_points: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """Expected touchdowns and field goals that add up to ``mean_points``."""
        mu = np.maximum(np.asarray(mean_points, dtype=float), 1.0)
        fg = np.minimum(self.fg_intercept + self.fg_slope * mu, 0.6 * mu / 3.0)
        td = (mu - 3.0 * fg - 2.0 * self.safety_rate) / self.points_per_td
        return np.maximum(td, 0.02), fg

    def weights(self, home: np.ndarray, away: np.ndarray) -> np.ndarray:
        """Per-simulation weights from the key-number calibration."""
        if not self.margin_weights:
            return np.ones(home.shape)
        table = np.ones(MAX_MARGIN + 1)
        for k, v in self.margin_weights.items():
            table[int(k)] = v
        return table[np.minimum(np.abs(home - away), MAX_MARGIN)]

    def to_dict(self) -> dict:
        d = asdict(self)
        d["ot_margins"] = {str(k): v for k, v in self.ot_margins.items()}
        d["margin_weights"] = {str(k): round(v, 4) for k, v in self.margin_weights.items()}
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "ScoringModel":
        d = dict(d)
        for key in ("ot_margins", "margin_weights"):
            if key in d:
                d[key] = {int(k): v for k, v in d[key].items()}
        return cls(**d)


def _team_points(rng, chances, p_td, p_fg, model: ScoringModel) -> np.ndarray:
    tds = rng.binomial(chances, p_td)
    fgs = rng.binomial(chances - tds, np.clip(p_fg / (1.0 - p_td), 0.0, 1.0))
    two_att = rng.binomial(tds, model.two_point_rate)
    two_made = rng.binomial(two_att, model.two_point_success)
    xp_made = rng.binomial(tds - two_att, model.xp_rate)
    safeties = rng.poisson(model.safety_rate, size=tds.shape)
    return 6 * tds + 3 * fgs + xp_made + 2 * two_made + 2 * safeties


def simulate(home_mean, away_mean, model: ScoringModel, n_sims: int = 10000,
             playoff=False, seed: int | None = 0) -> tuple[np.ndarray, np.ndarray]:
    """Simulate final scores. Returns two (n_games, n_sims) integer arrays."""
    rng = np.random.default_rng(seed)
    home_mean = np.atleast_1d(np.asarray(home_mean, dtype=float))
    away_mean = np.atleast_1d(np.asarray(away_mean, dtype=float))
    playoff = np.broadcast_to(np.asarray(playoff, dtype=bool), home_mean.shape)
    n = len(home_mean)

    pace = rng.normal(model.chances, model.pace_sd, size=(n, n_sims))
    chances = np.maximum(np.rint(pace), 3).astype(np.int64)

    def probs(mean):
        td, fg = model.rates(mean)
        p_td = np.minimum(td / model.chances, 0.85)
        p_fg = np.minimum(fg / model.chances, 0.95 - p_td)
        return p_td[:, None], p_fg[:, None]

    home = _team_points(rng, chances, *probs(home_mean), model)
    away = _team_points(rng, chances, *probs(away_mean), model)

    tied = home == away
    if tied.any():
        p_home = norm.cdf((home_mean - away_mean) / 13.0)[:, None]
        u = rng.random((n, n_sims))
        stays_tied = (u < model.ot_tie_prob) & ~playoff[:, None]
        home_wins = rng.random((n, n_sims)) < p_home
        margins = np.array(list(model.ot_margins.keys()))
        weights = np.array(list(model.ot_margins.values()), dtype=float)
        extra = rng.choice(margins, size=(n, n_sims), p=weights / weights.sum())
        decided = tied & ~stays_tied
        home = home + np.where(decided & home_wins, extra, 0)
        away = away + np.where(decided & ~home_wins, extra, 0)
    return home, away


def _weighted_quantile(values: np.ndarray, weights: np.ndarray, q: float) -> float:
    order = np.argsort(values, kind="stable")
    cum = np.cumsum(weights[order])
    return float(values[order][np.searchsorted(cum, q * cum[-1])])


def summarize(home: np.ndarray, away: np.ndarray, home_mean, away_mean,
              model: ScoringModel) -> pd.DataFrame:
    """Win probability, ranges and a headline scoreline for each simulated game."""
    home_mean = np.atleast_1d(np.asarray(home_mean, dtype=float))
    away_mean = np.atleast_1d(np.asarray(away_mean, dtype=float))
    weights = model.weights(home, away)
    margin = home - away
    rows = []
    for i in range(home.shape[0]):
        w = weights[i] / weights[i].sum()
        head_h, head_a = headline_score(home[i], away[i], home_mean[i], away_mean[i], w)
        rows.append({
            "home_win_prob": float(w[margin[i] > 0].sum()),
            "away_win_prob": float(w[margin[i] < 0].sum()),
            "tie_prob": float(w[margin[i] == 0].sum()),
            "one_score_prob": float(w[np.abs(margin[i]) <= 8].sum()),
            "home_low": int(_weighted_quantile(home[i], w, 0.10)),
            "home_high": int(_weighted_quantile(home[i], w, 0.90)),
            "away_low": int(_weighted_quantile(away[i], w, 0.10)),
            "away_high": int(_weighted_quantile(away[i], w, 0.90)),
            "headline_home": head_h, "headline_away": head_a,
        })
    return pd.DataFrame(rows)


def headline_score(home: np.ndarray, away: np.ndarray, home_mean: float, away_mean: float,
                   weights: np.ndarray | None = None, candidates: int = 40) -> tuple[int, int]:
    """The most frequent scoreline whose margin and total sit near the means."""
    margin_mean, total_mean = home_mean - away_mean, home_mean + away_mean
    pairs, inverse = np.unique(np.stack([home, away], axis=1), axis=0, return_inverse=True)
    counts = np.bincount(inverse.ravel(), weights=weights, minlength=len(pairs))
    order = np.argsort(-counts)[:candidates]
    pairs, counts = pairs[order], counts[order]
    m = pairs[:, 0] - pairs[:, 1]
    t = pairs[:, 0] + pairs[:, 1]
    score = counts * np.exp(-0.5 * ((m - margin_mean) / 2.5) ** 2 - 0.5 * ((t - total_mean) / 4.0) ** 2)
    if abs(margin_mean) >= 1.0:
        # The headline winner must be the predicted favorite.
        score = np.where(np.sign(m) == np.sign(margin_mean), score, -1.0)
    best = pairs[int(np.argmax(score))]
    return int(best[0]), int(best[1])


def calibrate(model: ScoringModel, target_margin_sd: float, target_total_sd: float,
              mean_points: float = 22.5, n_sims: int = 40000) -> ScoringModel:
    """Pick scoring chances and pace spread so simulated scores scatter like real ones."""
    best, best_err = model, np.inf
    for chances in np.arange(6.0, 14.01, 0.5):
        for pace_sd in (0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0):
            trial = replace(model, chances=float(chances), pace_sd=pace_sd, margin_weights={})
            h, a = simulate([mean_points], [mean_points], trial, n_sims=n_sims, seed=1)
            err = (np.std(h - a) - target_margin_sd) ** 2 + (np.std(h + a) - target_total_sd) ** 2
            if err < best_err:
                best, best_err = trial, err
    return best


def fit_margin_weights(model: ScoringModel, home_mean, away_mean, actual_margin,
                       playoff=False, n_sims: int = 2000, pseudo_count: float = 15.0) -> ScoringModel:
    """Reweight absolute margins so simulated key-number frequencies match history.

    Each past game is simulated from its own predicted means, the expected count
    of every final margin is compared with how many games actually ended on it,
    and the ratio (shrunk toward 1 for rare margins) becomes that margin's weight.
    """
    base = replace(model, margin_weights={})
    home, away = simulate(home_mean, away_mean, base, n_sims=n_sims, playoff=playoff, seed=7)
    sim_abs = np.minimum(np.abs(home - away), MAX_MARGIN)
    expected = np.bincount(sim_abs.ravel(), minlength=MAX_MARGIN + 1) / n_sims
    actual_abs = np.minimum(np.abs(np.asarray(actual_margin, dtype=int)), MAX_MARGIN)
    actual = np.bincount(actual_abs, minlength=MAX_MARGIN + 1)
    ratio = np.clip((actual + pseudo_count) / (expected + pseudo_count), 0.4, 2.5)
    return replace(model, margin_weights={k: float(ratio[k]) for k in range(MAX_MARGIN + 1)})
