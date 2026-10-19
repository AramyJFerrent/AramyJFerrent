"""Turn each team's expected runs per inning into realistic baseball scores.

Innings come from a base-out Markov chain built from Retrosheet
play-by-play. For each of the 24 base-out states it knows how often a plate
appearance ends in each outcome, and where each outcome leaves the runners,
the outs and the score (runner advances, double plays, sacrifice flies,
stolen bases and pickoffs included, since every transition runs from the start
of one plate appearance to the start of the next). Better or worse offense is
one knob, theta, which scales the odds of every way of reaching base. For
each theta the chain gives the exact distribution of runs in an inning, both
from empty bases and from the runner-on-second start of extra innings.

A game is then played inning by inning, 10,000 times. Each team's expected
runs in each inning (the run model's mix of starter and bullpen) is matched
to the theta with that mean, and a game-level shared factor (a gamma
"frailty") lets whole games run hot or cold, as real ones do. The home team
skips the bottom of the ninth when ahead; a walk-off inning stops at the
winning run unless it ends on a home run; regular-season extra innings start
with a runner on second.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field, replace

import numpy as np
import pandas as pd

from .retro import END, EVENTS

ALL_EVENTS = EVENTS + ("none",)
POSITIVE = ("bb", "hbp", "s", "d", "t", "hr")
MAX_RUNS = 30            # largest inning or team total tracked
MAX_STEP_RUNS = 4
GHOST_STATE = 2          # runner on second, nobody out
THETAS = np.exp(np.linspace(np.log(0.2), np.log(5.0), 400))
MAX_INNINGS = 30
TOTAL_LINES = tuple(np.arange(5.5, 13.01, 0.5))
QUANTILES = 8192
LOOKUP = 8192


class MarkovChain:
    """Base-out transitions by plate-appearance outcome, from transition counts."""

    def __init__(self, transitions: pd.DataFrame):
        t = transitions.groupby(["start", "event", "end", "runs"])["n"].sum().reset_index()
        t = t[t["event"].isin(ALL_EVENTS) & t["runs"].between(0, MAX_STEP_RUNS)]
        ev = {e: i for i, e in enumerate(ALL_EVENTS)}
        counts = np.zeros((24, len(ALL_EVENTS), 25, MAX_STEP_RUNS + 1))
        np.add.at(counts, (t["start"].to_numpy(int), t["event"].map(ev).to_numpy(int), t["end"].to_numpy(int),
                           t["runs"].to_numpy(int)), t["n"].to_numpy(float))
        by_event = counts.sum(axis=(2, 3))
        self.event_prob = by_event / np.maximum(by_event.sum(axis=1, keepdims=True), 1.0)
        self.trans = counts / np.maximum(by_event[:, :, None, None], 1.0)
        self.positive = np.array([e in POSITIVE for e in ALL_EVENTS])
        self.event_index = ev
        self._tables = None

    def step_matrix(self, theta: float) -> np.ndarray:
        """(24, 25, runs) probability of the next state and runs scored for one plate appearance."""
        p = self.event_prob * np.where(self.positive, theta, 1.0)
        p = p / np.maximum(p.sum(axis=1, keepdims=True), 1e-12)
        return np.einsum("se,sedr->sdr", p, self.trans)

    def inning(self, theta: float, start: int = 0, tol: float = 1e-11) -> np.ndarray:
        """Distribution of runs in a half-inning from ``start`` (exact, by dynamic programming)."""
        M = self.step_matrix(theta)
        mass = np.zeros((24, MAX_RUNS + 1))
        mass[start, 0] = 1.0
        done = np.zeros(MAX_RUNS + 1)
        for _ in range(500):
            new = np.zeros_like(mass)
            for r in range(MAX_STEP_RUNS + 1):
                moved = mass.T @ M[:, :, r]          # (runs so far, next state)
                if r:
                    shifted = np.zeros_like(moved)
                    shifted[r:] = moved[:-r]
                    shifted[-1] += moved[-r:].sum(axis=0)
                    moved = shifted
                new += moved[:, :24].T
                done += moved[:, END]
            mass = new
            if mass.sum() < tol:
                break
        return done / done.sum()

    def tables(self) -> dict:
        """Run distributions for every theta on the grid, from both starts."""
        if self._tables is None:
            empty = np.array([self.inning(th, 0) for th in THETAS])
            ghost = np.array([self.inning(th, GHOST_STATE) for th in THETAS])
            k = np.arange(MAX_RUNS + 1)
            self._tables = {"empty": empty, "ghost": ghost, "mean": empty @ k, "ghost_mean": ghost @ k,
                            "empty_q": quantile_table(empty), "ghost_q": quantile_table(ghost)}
        return self._tables

    def run_expectancy(self) -> np.ndarray:
        """Expected runs to the end of the inning from each of the 24 states, at theta 1."""
        M = self.step_matrix(1.0)
        P = M.sum(axis=2)[:, :24]
        r = (M * np.arange(MAX_STEP_RUNS + 1)).sum(axis=(1, 2))
        return np.linalg.solve(np.eye(24) - P, r)

    def linear_weights(self) -> dict[str, float]:
        """Average run value of each outcome relative to an out in play."""
        re = np.append(self.run_expectancy(), 0.0)
        runs = np.arange(MAX_STEP_RUNS + 1)
        # Value of an outcome at each state: runs on the play plus the change in run expectancy.
        value = (self.trans * (runs[None, None, None, :] + re[None, None, :, None])).sum(axis=(2, 3)) - re[:24, None]
        freq = self.event_prob * self.state_frequency()[:, None]
        avg = (value * freq).sum(axis=0) / np.maximum(freq.sum(axis=0), 1e-12)
        base = avg[self.event_index["out"]]
        return {e: float(avg[self.event_index[e]] - base) for e in EVENTS}

    def state_frequency(self) -> np.ndarray:
        """How often an inning passes through each state (visits per inning)."""
        P = self.step_matrix(1.0).sum(axis=2)[:, :24]
        start = np.zeros(24)
        start[0] = 1.0
        return np.linalg.solve(np.eye(24) - P.T, start)


@dataclass
class SimParams:
    tables: dict = field(default_factory=dict, repr=False)
    frailty: float = 30.0            # gamma shape of the shared game factor (higher = less spread)
    walkoff_hr: float = 0.3          # share of walk-offs that are home runs (all runs count)
    extra_mult: float = 1.0          # extra-inning run expectation relative to an ordinary inning
    # From the ninth inning on, a team trailing by one to three runs faces the
    # other side's closer: its run expectation is scaled by this (tuned so
    # games reach extra innings as often as real ones). Other ninth innings
    # (blowouts, mop-up relievers) are scaled up to keep the ninth's average,
    # given the share of ninth innings that are closer situations.
    closer_mult: float = 1.0
    closer_share: float = 0.3

    def to_dict(self) -> dict:
        d = asdict(self)
        d.pop("tables")
        return d


def quantile_table(dists: np.ndarray, levels: int = QUANTILES) -> np.ndarray:
    """(thetas, levels) runs at evenly spaced quantiles of each distribution,
    so a draw is one lookup (each outcome's probability is exact to 1/levels)."""
    cdf = np.cumsum(dists, axis=1)
    q = (np.arange(levels) + 0.5) / levels
    return np.stack([np.searchsorted(row, q) for row in cdf]).clip(0, MAX_RUNS).astype(np.uint8)


def simulate(home_mu: np.ndarray, away_mu: np.ndarray, home_extra: np.ndarray, away_extra: np.ndarray,
             params: SimParams, n_sims: int = 10000, ghost=True, sched_innings=9, seed: int | None = 0) -> dict:
    """Simulate games inning by inning.

    ``home_mu`` and ``away_mu`` are (n_games, 9) expected runs for each team
    batting in innings 1-9; ``*_extra`` the expected runs in each extra
    inning (an ordinary inning's worth: the runner on second is added here).
    Returns (n_games, n_sims) arrays of final runs, innings played, five-inning
    runs, whether the home team batted in the last scheduled inning, and walk-offs.
    """
    rng = np.random.default_rng(seed)
    home_mu = np.atleast_2d(np.asarray(home_mu, dtype=float))
    away_mu = np.atleast_2d(np.asarray(away_mu, dtype=float))
    n = home_mu.shape[0]
    shape = (n, n_sims)
    ghost = np.broadcast_to(np.asarray(ghost, dtype=bool), (n,)).astype(np.int64)
    sched = np.broadcast_to(np.asarray(sched_innings, dtype=int), (n,))
    t = params.tables
    table = np.stack([t["empty_q"], t["ghost_q"]])          # (start, theta, quantile)
    # Expected runs -> theta through a lookup on a fine log grid (faster than a search).
    lo, hi = np.log(t["mean"][0]), np.log(t["mean"][-1])
    grid = np.exp(lo + (np.arange(LOOKUP) + 0.5) / LOOKUP * (hi - lo))
    lookup = np.clip(np.searchsorted(t["mean"], grid), 0, len(THETAS) - 1)

    def draw(mu, kind=0):
        pos = ((np.log(np.maximum(mu, 1e-9)) - lo) * (LOOKUP / (hi - lo))).astype(np.int64)
        idx = lookup[np.clip(pos, 0, LOOKUP - 1)]
        return table[kind, idx, rng.integers(0, QUANTILES, size=mu.shape)].astype(np.int32)

    if params.frailty and np.isfinite(params.frailty):
        g_home = rng.gamma(params.frailty, 1.0 / params.frailty, shape)
        g_away = rng.gamma(params.frailty, 1.0 / params.frailty, shape)
    else:
        g_home = g_away = np.ones(shape)
    h = np.zeros(shape, dtype=np.int32)
    a = np.zeros(shape, dtype=np.int32)
    f5_h = f5_a = None
    innings = np.broadcast_to(sched[:, None], shape).copy()
    walkoff = np.zeros(shape, dtype=bool)
    batted_last = np.ones(shape, dtype=bool)

    other = (1 - params.closer_share * params.closer_mult) / (1 - params.closer_share)

    def closer(lead, ninth=True):
        return np.where((lead <= -1) & (lead >= -3), params.closer_mult, other if ninth else 1.0)

    def walk_off(h_before, a_now, r):
        """Home score after a bottom half that may end the game."""
        need = a_now - h_before + 1
        wins = r >= need
        hr = rng.random(r.shape) < params.walkoff_hr
        margin = np.where(hr, np.minimum(r - need + 1, 4), 1)
        return np.where(wins, a_now + margin, h_before + r), wins

    for inning in range(1, 10):
        live = (inning <= sched)[:, None]
        last = (inning == sched)[:, None]
        mu_a = away_mu[:, inning - 1][:, None] * g_away
        mu_h = home_mu[:, inning - 1][:, None] * g_home
        if inning >= 9:
            mu_a = mu_a * closer(a - h)
        a = a + np.where(live, draw(mu_a), 0)
        r = draw(mu_h * closer(h - a) if inning >= 9 else mu_h)
        if last.any():
            bats = ~last | (h <= a)
            ended, wins = walk_off(h, a, r)
            h = np.where(live & bats, np.where(last, ended, h + r), h)
            walkoff |= live & last & bats & wins
            batted_last &= ~(last & ~bats)
        else:
            h = np.where(live, h + r, h)
        if inning == 5:
            f5_h, f5_a = h.copy(), a.copy()
        if inning == 8:
            h8, a8 = h.copy(), a.copy()

    # Extra innings, only for the games still tied.
    tied = np.flatnonzero((h == a).ravel())
    games = tied // n_sims
    hx, ax = h.ravel()[tied], a.ravel()[tied]
    ex_h = (home_extra * params.extra_mult)[games] * g_home.ravel()[tied]
    ex_a = (away_extra * params.extra_mult)[games] * g_away.ravel()[tied]
    kind = ghost[games]
    inn = sched[games].astype(np.int64)
    flat_h, flat_a, flat_inn, flat_wo = h.ravel(), a.ravel(), innings.ravel(), walkoff.ravel()
    for _ in range(MAX_INNINGS):
        if not len(tied):
            break
        inn += 1
        ax = ax + draw(ex_a, kind)
        r = draw(ex_h * closer(hx - ax, ninth=False), kind)
        bats = hx <= ax
        ended, wins = walk_off(hx, ax, r)
        hx = np.where(bats, ended, hx)
        done = hx != ax
        flat_h[tied[done]], flat_a[tied[done]], flat_inn[tied[done]] = hx[done], ax[done], inn[done]
        flat_wo[tied[done]] = (bats & wins)[done]
        keep = ~done
        tied, hx, ax, ex_h, ex_a, kind, inn = (x[keep] for x in (tied, hx, ax, ex_h, ex_a, kind, inn))
    if len(tied):
        # A tie after the cap (vanishingly rare) goes to a coin flip.
        coin = rng.random(len(tied)) < 0.5
        flat_h[tied] = hx + coin
        flat_a[tied] = ax + ~coin
        flat_inn[tied] = inn
    return {"home": flat_h.reshape(shape), "away": flat_a.reshape(shape), "innings": flat_inn.reshape(shape),
            "f5_home": f5_h, "f5_away": f5_a, "r8_home": h8, "r8_away": a8, "walkoff": flat_wo.reshape(shape),
            "home_batted_last": batted_last, "sched": np.broadcast_to(sched[:, None], shape)}


def headline_score(home: np.ndarray, away: np.ndarray, home_wins: bool, spread: float = 1.5) -> tuple[int, int]:
    """A frequent final score near each team's expected runs in which the more likely winner wins."""
    pairs, counts = np.unique(np.stack([home, away], axis=1), axis=0, return_counts=True)
    closeness = np.exp(-0.5 * (((pairs[:, 0] - home.mean()) / spread) ** 2
                               + ((pairs[:, 1] - away.mean()) / spread) ** 2))
    winner_ok = pairs[:, 0] > pairs[:, 1] if home_wins else pairs[:, 1] > pairs[:, 0]
    score = np.where(winner_ok, counts * closeness, -1.0)
    best = pairs[int(np.argmax(score))]
    return int(best[0]), int(best[1])


def headline_scores(home: np.ndarray, away: np.ndarray, spread: float = 1.5) -> tuple[np.ndarray, np.ndarray]:
    """``headline_score`` for every row of (n_games, n_sims) arrays at once."""
    cap = 40
    n = home.shape[0]
    code = np.minimum(home, cap - 1) * cap + np.minimum(away, cap - 1)
    counts = np.bincount((np.arange(n)[:, None] * cap * cap + code).ravel(), minlength=n * cap * cap)
    counts = counts.reshape(n, cap, cap).astype(float)
    k = np.arange(cap)
    close_h = np.exp(-0.5 * ((k[None, :] - home.mean(axis=1)[:, None]) / spread) ** 2)
    close_a = np.exp(-0.5 * ((k[None, :] - away.mean(axis=1)[:, None]) / spread) ** 2)
    score = counts * close_h[:, :, None] * close_a[:, None, :]
    home_wins = (home > away).mean(axis=1) >= 0.5
    winner = np.where(home_wins[:, None, None], k[:, None] > k[None, :], k[:, None] < k[None, :])
    score = np.where(winner, score, -1.0).reshape(n, -1)
    best = score.argmax(axis=1)
    return best // cap, best % cap


def summarize(sim: dict) -> pd.DataFrame:
    """Win probabilities, ranges and a headline score for each simulated game."""
    h, a = sim["home"], sim["away"]
    margin = h - a
    f5 = sim["f5_home"] - sim["f5_away"]
    head_h, head_a = headline_scores(h, a)
    p_home = (margin > 0).mean(axis=1)
    return pd.DataFrame({
        "home_win_prob": p_home, "away_win_prob": 1.0 - p_home,
        "extra_prob": (sim["innings"] > sim["sched"]).mean(axis=1),
        "one_run_prob": (np.abs(margin) == 1).mean(axis=1),
        "home_shutout_prob": (a == 0).mean(axis=1), "away_shutout_prob": (h == 0).mean(axis=1),
        "skip_bottom_prob": (~sim["home_batted_last"]).mean(axis=1),
        "walkoff_prob": sim["walkoff"].mean(axis=1),
        "home_cover_prob": (margin >= 2).mean(axis=1),     # home -1.5
        "away_cover_prob": (margin <= -2).mean(axis=1),    # away -1.5
        "f5_home_win_prob": (f5 > 0).mean(axis=1), "f5_tie_prob": (f5 == 0).mean(axis=1),
        "f5_total": (sim["f5_home"] + sim["f5_away"]).mean(axis=1),
        "sim_home": h.mean(axis=1), "sim_away": a.mean(axis=1), "sim_total": (h + a).mean(axis=1),
        "home_low": np.percentile(h, 10, axis=1).astype(int), "home_high": np.percentile(h, 90, axis=1).astype(int),
        "away_low": np.percentile(a, 10, axis=1).astype(int), "away_high": np.percentile(a, 90, axis=1).astype(int),
        "headline_home": head_h, "headline_away": head_a,
    })


def over_prob(sim: dict, lines: np.ndarray) -> np.ndarray:
    """Chance each game's total goes over its line (a push counts half)."""
    total = sim["home"] + sim["away"]
    lines = np.asarray(lines, dtype=float)[:, None]
    return np.mean(total > lines, axis=1) + 0.5 * np.mean(total == lines, axis=1)


def with_tables(params: SimParams, chain: MarkovChain) -> SimParams:
    return replace(params, tables=chain.tables())
