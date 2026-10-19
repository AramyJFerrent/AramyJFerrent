"""Glicko-2 skill ratings, plus a plain Elo kept as the baseline to beat.

Glicko-2 (Glickman) gives each fighter a rating and a rating deviation (RD),
the uncertainty around it. Fights are irregular, so instead of fixed rating
periods each fight is its own update, and before it the deviation grows with
the time since the fighter's last bout. A debutant starts at the average with
a wide deviation, so a few results move the rating a long way. (Debutants do
lose more often than that implies; the win model has a separate debut term.)

Wins are credited by how clear they were: a finish scores 1, a unanimous or
majority decision ``score_decision`` and a split decision ``score_split``.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

from .config import Hyperparams

SCALE = 173.7178
BASE = 1500.0


def _g(phi: float) -> float:
    return 1.0 / math.sqrt(1.0 + 3.0 * phi * phi / (math.pi * math.pi))


@dataclass
class Player:
    mu: float
    phi: float
    sigma: float
    last: float | None = None   # day number of the last fight
    fights: int = 0


class Glicko2:
    def __init__(self, hp: Hyperparams):
        self.hp = hp
        self.players: dict[str, Player] = {}
        self.max_phi = hp.glicko_debut_rd / SCALE

    def _new(self) -> Player:
        return Player(0.0, self.max_phi, self.hp.glicko_vol)

    def _phi_at(self, p: Player, day: float) -> float:
        if p.last is None:
            return p.phi
        periods = max(day - p.last, 0.0) / self.hp.glicko_period_days
        return min(math.sqrt(p.phi ** 2 + p.sigma ** 2 * periods), self.max_phi)

    def state(self, fid: str, day: float) -> tuple[float, float, int]:
        """Rating, deviation (both on the 1500 scale) and UFC fights before ``day``."""
        p = self.players.get(fid) or self._new()
        return BASE + SCALE * p.mu, SCALE * self._phi_at(p, day), p.fights

    def win_logit(self, a: str, b: str, day: float) -> float:
        """Log-odds that A beats B, discounted for both fighters' uncertainty."""
        pa, pb = self.players.get(a) or self._new(), self.players.get(b) or self._new()
        phi = math.sqrt(self._phi_at(pa, day) ** 2 + self._phi_at(pb, day) ** 2)
        return _g(phi) * (pa.mu - pb.mu)

    def _volatility(self, phi: float, sigma: float, delta: float, v: float) -> float:
        """New volatility by the Illinois iteration in Glickman's paper."""
        tau = self.hp.glicko_tau
        a = math.log(sigma * sigma)

        def f(x):
            ex = math.exp(x)
            return (ex * (delta * delta - phi * phi - v - ex) / (2 * (phi * phi + v + ex) ** 2)
                    - (x - a) / (tau * tau))

        lo = a
        if delta * delta > phi * phi + v:
            hi = math.log(delta * delta - phi * phi - v)
        else:
            k = 1
            while f(a - k * tau) < 0:
                k += 1
            hi = a - k * tau
        flo, fhi = f(lo), f(hi)
        for _ in range(60):
            if abs(hi - lo) < 1e-6:
                break
            c = lo + (lo - hi) * flo / (fhi - flo)
            fc = f(c)
            if fc * fhi <= 0:
                lo, flo = hi, fhi
            else:
                flo /= 2
            hi, fhi = c, fc
        return math.exp(lo / 2)

    def update(self, a: str, b: str, score_a: float, day: float) -> None:
        pa, pb = self.players.setdefault(a, self._new()), self.players.setdefault(b, self._new())
        phis = (self._phi_at(pa, day), self._phi_at(pb, day))
        mus = (pa.mu, pb.mu)
        for i, (p, s) in enumerate(((pa, score_a), (pb, 1.0 - score_a))):
            phi, opp_mu, opp_phi = phis[i], mus[1 - i], phis[1 - i]
            g = _g(opp_phi)
            e = 1.0 / (1.0 + math.exp(-g * (mus[i] - opp_mu)))
            v = 1.0 / (g * g * e * (1 - e))
            delta = v * g * (s - e)
            p.sigma = self._volatility(phi, p.sigma, delta, v)
            new_phi = 1.0 / math.sqrt(1.0 / (phi * phi) + 1.0 / v)
            p.mu = mus[i] + new_phi * new_phi * g * (s - e)
            p.phi = new_phi
            p.last = day
            p.fights += 1


class Elo:
    """UFC-results-only Elo (K = 64, debutants at 1500), the report's baseline."""

    def __init__(self, k: float = 64.0):
        self.k = k
        self.ratings: dict[str, float] = {}

    def get(self, fid: str) -> float:
        return self.ratings.get(fid, BASE)

    def prob(self, a: str, b: str) -> float:
        return 1.0 / (1.0 + 10 ** ((self.get(b) - self.get(a)) / 400.0))

    def update(self, a: str, b: str, score_a: float) -> None:
        p = self.prob(a, b)
        ra, rb = self.get(a), self.get(b)
        self.ratings[a] = ra + self.k * (score_a - p)
        self.ratings[b] = rb - self.k * (score_a - p)


def winner_score(winner: str, method: str, decision, hp: Hyperparams) -> float | None:
    """Score credited to fighter A, or None for a no contest."""
    if winner == "draw":
        return 0.5
    if winner not in ("a", "b"):
        return None
    s = 1.0
    if method == "DEC":
        s = hp.score_split if decision == "split" else hp.score_decision
    return s if winner == "a" else 1.0 - s


def logit(p):
    p = np.clip(np.asarray(p, dtype=float), 1e-6, 1 - 1e-6)
    return np.log(p / (1 - p))


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.asarray(x, dtype=float)))
