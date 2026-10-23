"""Player impact ratings, projected minutes and lineup strength.

Ratings are regularized adjusted plus-minus (RAPM) fitted on stints, the
stretches of a game with the same ten players on the floor. Each stint gives
one observation per side on offense:

    points per 100 possessions = league level + home edge
                                 + sum of the five offensive ratings
                                 + sum of the five opposing defensive ratings

weighted by possessions, with garbage time and unresolved lineups left out.
The ridge pulls each player toward a prior: last season's rating, regressed,
or a below-average newcomer value for players with no rating yet. Recent
stints count more. Offense is positive when good; defense is positive when it
allows more, so a player's net impact is offense minus defense.

The prior also learns from the box score (a statistical plus-minus, SPM).
Each season, a ridge regression on earlier seasons maps a player's box-score
rates per 36 minutes (points, shots, free throws, threes, assists,
rebounds, steals, blocks, turnovers, fouls) to his final offensive and
defensive ratings. As a player logs minutes, his prior moves from its anchor
(last season's rating, or the newcomer value) toward what his box score this
season says, by ``m / (m + M)`` after ``m`` minutes, with ``M`` set
separately for newcomers and returning players. Box-score rates settle much
faster than plus-minus, so this mostly helps rookies and players with few
minutes, whose plus-minus alone says little.

A team's strength for a game is the minutes-weighted sum of its available
players' ratings, with each player's minutes projected from his recent games
and rescaled so the team plays 240 minutes. Comparing that with the players
behind the team's efficiency rating gives the availability adjustment: how
much better or worse tonight's lineup is than the one the rating has seen.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import scipy.linalg
import scipy.sparse as sp

from .config import REG_MINUTES, Hyperparams
from .ratings import season_day

# Box-score rates the SPM reads, per 36 minutes.
BOX_STATS = ["pts", "fga", "fta", "fg3m", "ast", "oreb", "dreb", "stl", "blk", "tov", "pf"]
# Player-seasons the SPM is fitted on: enough minutes for the rating to mean something, the
# minutes weight capped so stars do not dominate, and a light ridge on the standardized rates.
SPM_MIN_MINUTES = 250.0
SPM_MIN_PLAYERS = 50
SPM_WEIGHT_CAP = 2000.0
SPM_RIDGE = 1.0
LEAGUE_PRIOR_POSS = 200.0
HOME_PRIOR_POSS = 50000.0
TEAM_MINUTES = 5 * REG_MINUTES
# A player's minutes before he has played: about a reserve's share.
DEBUT_MINUTES = 12.0
DEBUT_WEIGHT = 1.0
MAX_MINUTES = 42.0


def stint_rows(stints: pd.DataFrame, games: pd.DataFrame) -> pd.DataFrame:
    """Two observations per usable stint, one for each side on offense."""
    s = stints[(stints["garbage"] == 0) & (stints["valid"] == 1)]
    g = games.set_index("game_id")
    s = s[s["game_id"].isin(g.index)]
    neutral = s["game_id"].map(g["neutral"]).fillna(False).to_numpy(bool)
    season = s["game_id"].map(g["season"]).to_numpy()
    dates = s["game_id"].map(g["date"])
    day = np.zeros(len(s), dtype=int)
    for yr in np.unique(season):
        m = season == yr
        day[m] = season_day(dates[m], int(yr))
    out = []
    for side, other, sign in (("home", "away", 1.0), ("away", "home", -1.0)):
        poss = s[f"{side}_poss"].to_numpy(float)
        out.append(pd.DataFrame({
            "season": season, "day": day,
            "off": s[f"{side}_ids"].to_numpy(), "def": s[f"{other}_ids"].to_numpy(),
            "h": np.where(neutral, 0.0, sign),
            "y": 100.0 * s[f"{side}_pts"].to_numpy(float) / np.where(poss > 0, poss, np.nan),
            "w": poss,
        }))
    rows = pd.concat(out, ignore_index=True)
    return rows[rows["w"] > 0.2].reset_index(drop=True)


class BoxScores:
    """Each player's running box-score totals through a season, by day."""

    def __init__(self, players: pd.DataFrame, games: pd.DataFrame):
        g = games.set_index("game_id")
        b = players[players["minutes"].fillna(0) > 0]
        b = b[b["game_id"].isin(g.index)]
        b = b.assign(season=b["game_id"].map(g["season"]).astype(int), date=b["game_id"].map(g["date"]))
        self.seasons: dict[int, dict] = {}
        for season, d in b.groupby("season"):
            d = d.assign(day=season_day(d["date"], int(season))).sort_values("day", kind="stable")
            cols = ["minutes"] + BOX_STATS
            totals = d.groupby(["player_id", "day"])[cols].sum().groupby(level=0).cumsum()
            self.seasons[int(season)] = {
                pid: (grp.index.get_level_values(1).to_numpy(float), grp.to_numpy(float))
                for pid, grp in totals.groupby(level=0)}

    def before(self, season: int, day: float, ids) -> np.ndarray:
        """Minutes and stat totals (columns as ``["minutes"] + BOX_STATS``) of each of ``ids``
        in ``season`` from games before ``day``; zeros for a player with none."""
        by_player = self.seasons.get(season, {})
        out = np.zeros((len(ids), 1 + len(BOX_STATS)))
        for i, pid in enumerate(ids):
            hit = by_player.get(pid)
            if hit is None:
                continue
            k = int(np.searchsorted(hit[0], day, side="left"))
            if k:
                out[i] = hit[1][k - 1]
        return out


def box_rates(totals: np.ndarray) -> np.ndarray:
    """Per-36-minute rates from ``BoxScores`` totals (zeros without minutes)."""
    minutes = totals[:, :1]
    return np.where(minutes > 0, 36.0 * totals[:, 1:] / np.where(minutes > 0, minutes, 1.0), 0.0)


class SPM:
    """Linear map from box-score rates to offensive and defensive ratings."""

    def __init__(self, center: np.ndarray, scale: np.ndarray, coef: np.ndarray):
        self.center, self.scale, self.coef = center, scale, coef   # coef: (1 + stats) x 2 (offense, defense)

    @classmethod
    def fit(cls, rates: np.ndarray, minutes: np.ndarray, off: np.ndarray, de: np.ndarray) -> "SPM | None":
        keep = minutes >= SPM_MIN_MINUTES
        if keep.sum() < SPM_MIN_PLAYERS:
            return None
        X, w = rates[keep], np.minimum(minutes[keep], SPM_WEIGHT_CAP)
        center = np.average(X, axis=0, weights=w)
        scale = np.sqrt(np.average((X - center) ** 2, axis=0, weights=w)) + 1e-9
        Z = np.column_stack([np.ones(len(X)), (X - center) / scale])
        pen = np.full(Z.shape[1], SPM_RIDGE * w.sum() / len(w))
        pen[0] = 0.0
        A = Z.T @ (Z * w[:, None]) + np.diag(pen)
        Y = np.column_stack([off[keep], de[keep]])
        return cls(center, scale, np.linalg.solve(A, Z.T @ (Y * w[:, None])))

    def predict(self, rates: np.ndarray) -> np.ndarray:
        """Offense and defense (columns) for each row of rates."""
        Z = np.column_stack([np.ones(len(rates)), (rates - self.center) / self.scale])
        return Z @ self.coef


class SeasonRAPM:
    """RAPM solves for chosen days of one season, from running sums."""

    def __init__(self, rows: pd.DataFrame, half_life: float):
        self.rows = rows.sort_values("day", kind="stable").reset_index(drop=True)
        ids = np.array([[int(p) for p in s.split()] for s in self.rows["off"]] +
                       [[int(p) for p in s.split()] for s in self.rows["def"]], dtype=np.int64)
        self.players = sorted(set(ids.ravel().tolist())) if len(ids) else []
        self.index = {p: i for i, p in enumerate(self.players)}
        self.n = len(self.players)
        lookup = pd.Index(self.players)
        n_rows = len(self.rows)
        self.off_idx = lookup.get_indexer(ids[:n_rows].ravel()).reshape(-1, 5) if n_rows else np.zeros((0, 5), int)
        self.def_idx = lookup.get_indexer(ids[n_rows:].ravel()).reshape(-1, 5) if n_rows else np.zeros((0, 5), int)
        self.days = self.rows["day"].to_numpy(float)
        self.half_life = half_life
        self.n_params = 2 + 2 * self.n
        self.solved: dict[float, np.ndarray] = {}
        self._reset()

    def _reset(self) -> None:
        self.A = np.zeros((self.n_params, self.n_params))
        self.b = np.zeros(self.n_params)
        self._pos = 0
        self._day = -np.inf

    def _design(self, lo: int, hi: int) -> sp.csr_matrix:
        n = hi - lo
        r = np.repeat(np.arange(n), 12)
        c = np.column_stack([np.zeros(n, int), np.ones(n, int), 2 + self.off_idx[lo:hi],
                             2 + self.n + self.def_idx[lo:hi]]).ravel()
        v = np.column_stack([np.ones(n), self.rows["h"].to_numpy()[lo:hi], np.ones((n, 10))]).ravel()
        return sp.csr_matrix((v, (r, c)), shape=(n, self.n_params))

    def _advance(self, day: float) -> None:
        """Add every stint played before ``day`` to the running sums (starting
        over if an earlier day is asked for, since sums only grow)."""
        if day < self._day:
            self._reset()
        self._day = day
        end = int(np.searchsorted(self.days, day, side="left"))
        if end <= self._pos:
            return
        X = self._design(self._pos, end)
        w = self.rows["w"].to_numpy()[self._pos:end] * 2.0 ** (self.days[self._pos:end] / self.half_life)
        Xw = X.multiply(w[:, None]).tocsr()
        self.A += (X.T @ Xw).toarray()
        self.b += Xw.T @ self.rows["y"].to_numpy()[self._pos:end]
        self._pos = end

    def solve_days(self, days, lam: np.ndarray, beta0) -> None:
        """Solve each of ``days``; ``beta0`` is the prior, or a function of the day giving it."""
        for day in sorted(set(float(d) for d in days) - set(self.solved)):
            self._advance(day)
            c = 2.0 ** (-day / self.half_life)
            M = c * self.A
            M[np.diag_indices_from(M)] += lam
            b0 = beta0(day) if callable(beta0) else beta0
            self.solved[day] = scipy.linalg.solve(M, lam * b0 + c * self.b, assume_a="pos")


class PlayerRatings:
    """Offensive and defensive RAPM for any day of any season, chaining priors."""

    def __init__(self, stints: pd.DataFrame, games: pd.DataFrame, hp: Hyperparams,
                 box: pd.DataFrame | None = None):
        self.hp = hp
        use_box = box is not None and (hp.box_prior_minutes_new > 0 or hp.box_prior_minutes > 0)
        self.box = BoxScores(box, games) if use_box else None
        self._spm: dict[int, SPM | None] = {}
        rows = stint_rows(stints, games)
        self.by_season = {int(s): r.reset_index(drop=True) for s, r in rows.groupby("season")}
        self.first_season = min(self.by_season) if self.by_season else None
        self.game_days = {int(s): season_day(pd.Series(sorted(d["date"].unique())), int(s))
                          for s, d in games.groupby("season")}
        self.newcomer = (hp.newcomer_net / 2.0, -hp.newcomer_net / 2.0)
        self._seasons: dict[int, SeasonRAPM] = {}
        self._priors: dict[int, tuple[dict, dict, float]] = {}
        self._final: dict[int, tuple[dict, dict, float]] = {}

    # ---- priors ----------------------------------------------------------
    def prior(self, season: int) -> tuple[dict, dict, float]:
        """Offense and defense priors by player id, and the league level:
        last season's ratings, regressed toward average."""
        if season not in self._priors:
            if self.first_season is None or season <= self.first_season:
                rows = self.by_season.get(self.first_season)
                mu = float(np.average(rows["y"], weights=rows["w"])) if rows is not None and len(rows) else 110.0
                self._priors[season] = ({}, {}, mu)
            else:
                off, de, mu = self.final(season - 1)
                keep = self.hp.player_carryover
                self._priors[season] = ({p: keep * v for p, v in off.items()},
                                        {p: keep * v for p, v in de.items()}, mu)
        return self._priors[season]

    def _season(self, season: int) -> SeasonRAPM:
        if season not in self._seasons:
            rows = self.by_season.get(season, pd.DataFrame(columns=["day", "off", "def", "h", "y", "w"]))
            self._seasons[season] = SeasonRAPM(rows, self.hp.player_half_life_days)
        return self._seasons[season]

    def spm(self, season: int) -> SPM | None:
        """The box-score model for ``season``, fitted on every earlier season's final ratings."""
        if season not in self._spm:
            rates, minutes, off, de = [], [], [], []
            for past in sorted(s for s in (self.box.seasons if self.box else {}) if s < season):
                if past not in self.by_season:
                    continue
                o, d, _ = self.final(past)
                ids = [p for p in self.box.seasons[past] if p in o]
                totals = self.box.before(past, np.inf, ids)
                rates.append(box_rates(totals))
                minutes.append(totals[:, 0])
                off.append([o[p] for p in ids])
                de.append([d[p] for p in ids])
            self._spm[season] = SPM.fit(np.concatenate(rates), np.concatenate(minutes), np.concatenate(off),
                                        np.concatenate(de)) if rates else None
        return self._spm[season]

    def _penalty(self, season: int, sr: SeasonRAPM) -> tuple[np.ndarray, object]:
        off0, def0, mu0 = self.prior(season)
        o_new, d_new = self.newcomer
        lam = np.concatenate([[LEAGUE_PRIOR_POSS, HOME_PRIOR_POSS],
                              np.full(sr.n, self.hp.player_off_prior_poss),
                              np.full(sr.n, self.hp.player_def_prior_poss)])
        anchor_o = np.array([off0.get(p, o_new) for p in sr.players])
        anchor_d = np.array([def0.get(p, d_new) for p in sr.players])
        beta0 = np.concatenate([[mu0, 1.5], anchor_o, anchor_d])
        spm = self.spm(season) if self.box is not None else None
        if spm is None or sr.n == 0:
            return lam, beta0
        # Each player's prior moves toward his box-score ratings as his minutes this season build.
        half = np.array([self.hp.box_prior_minutes if p in off0 else self.hp.box_prior_minutes_new
                         for p in sr.players])

        def at(day: float) -> np.ndarray:
            totals = self.box.before(season, day, sr.players)
            m = totals[:, 0]
            k = np.where(half > 0, m / (m + np.where(half > 0, half, 1.0)), 0.0)
            box = spm.predict(box_rates(totals))
            return np.concatenate([[mu0, 1.5], anchor_o + k * (box[:, 0] - anchor_o),
                                   anchor_d + k * (box[:, 1] - anchor_d)])
        return lam, at

    def prepare(self, season: int, days=None, all_game_days: bool = True) -> None:
        """Solve every game day of ``season`` (and any extra ``days``) in one pass."""
        sr = self._season(season)
        want = list(self.game_days.get(season, [])) if all_game_days else []
        want += list(days) if days is not None else []
        if not want:
            return
        lam, beta0 = self._penalty(season, sr)
        sr.solve_days(want, lam, beta0)

    def _unpack(self, season: int, beta: np.ndarray) -> tuple[dict, dict, float]:
        sr = self._season(season)
        off0, def0, _ = self.prior(season)
        off, de = dict(off0), dict(def0)
        off.update(zip(sr.players, beta[2:2 + sr.n].tolist()))
        de.update(zip(sr.players, beta[2 + sr.n:].tolist()))
        return off, de, float(beta[0])

    def before(self, season: int, day: float) -> tuple[dict, dict, float]:
        """Ratings from ``season`` stints before ``day``; players without a
        stint yet keep their prior."""
        sr = self._season(season)
        day = float(day)
        if day not in sr.solved:
            self.prepare(season, [day], all_game_days=False)
        return self._unpack(season, sr.solved[day])

    def final(self, season: int) -> tuple[dict, dict, float]:
        if season not in self._final:
            sr = self._season(season)
            last = float(sr.days.max() + 1) if len(sr.days) else 400.0
            self._final[season] = self.before(season, last)
        return self._final[season]


# ---- minutes ---------------------------------------------------------------

def minutes_history(players: pd.DataFrame, games: pd.DataFrame, half_life_games: float) -> pd.DataFrame:
    """Each listed player-game with two projections made before it, from the
    player's earlier games for any team: minutes when he plays
    (``proj_minutes``) and expected minutes counting healthy scratches as zero
    (``proj_expected``), plus both running averages after it. Games he was out
    for injury, rest or suspension count for neither."""
    g = games.set_index("game_id")
    cols = ["game_id", "team", "player_id", "minutes", "starter"] + (["status"] if "status" in players else [])
    p = players[cols].copy()
    if "status" not in p:
        p["status"] = np.where(p["minutes"] > 0, "played", "out")
    p = p[p["status"] != "out"]
    p["start"] = p["game_id"].map(g["start"])
    p = p.sort_values(["player_id", "start", "game_id"]).reset_index(drop=True)
    decay = 0.5 ** (1.0 / half_life_games)
    n = len(p)
    out = {k: np.empty(n) for k in ("proj_minutes", "proj_expected", "avg_after", "exp_after")}
    mins = p["minutes"].to_numpy(float)
    played = (p["status"] == "played").to_numpy()
    pid = p["player_id"].to_numpy()
    last = None
    for i in range(n):
        if pid[i] != last:
            # Seed each player's averages with a reserve's minutes worth one game.
            nc = ne = DEBUT_MINUTES * DEBUT_WEIGHT
            dc = de = DEBUT_WEIGHT
            last = pid[i]
        out["proj_minutes"][i] = nc / dc
        out["proj_expected"][i] = ne / de
        if played[i]:
            nc, dc = decay * nc + mins[i], decay * dc + 1.0
        ne, de = decay * ne + mins[i], decay * de + 1.0
        out["avg_after"][i] = nc / dc
        out["exp_after"][i] = ne / de
    for k, v in out.items():
        p[k] = v
    return p


# How a team's minutes are made to add up to 240: "headroom" hands missing
# minutes to each player in proportion to how far he is below the cap (the
# bench absorbs most of an absent starter's minutes); "proportional" scales
# everyone alike. Too many minutes are always scaled down proportionally.
REDISTRIBUTION = "headroom"


def rescale_minutes(proj: np.ndarray, total: float = TEAM_MINUTES, cap: float = MAX_MINUTES,
                    how: str | None = None) -> np.ndarray:
    """Scale projected minutes to the team's total without anyone above the cap."""
    m = np.clip(np.asarray(proj, dtype=float), 0.0, None)
    if len(m) == 0:
        return m
    if m.sum() <= 0 or len(m) * cap <= total:
        return np.full(len(m), total / len(m))
    how = how or REDISTRIBUTION
    if how == "headroom" and m.sum() < total:
        m = np.minimum(m, cap)
        room = cap - m
        return m + (total - m.sum()) * room / room.sum()
    m = m * total / m.sum()
    fixed = np.zeros(len(m), dtype=bool)
    for _ in range(len(m)):
        over = (m > cap) & ~fixed
        if not over.any():
            break
        fixed |= over
        m[fixed] = cap
        free = ~fixed
        m[free] *= (total - cap * fixed.sum()) / m[free].sum()
    return m


def lineup_strength(ids, minutes, off: dict, de: dict, newcomer: tuple[float, float]) -> tuple[float, float]:
    """Offensive and defensive strength (points per 100) of players with these
    minutes: each counts in proportion to his share of the floor time."""
    share = np.asarray(minutes, dtype=float) / REG_MINUTES
    o = np.array([off.get(int(p), newcomer[0]) for p in ids])
    d = np.array([de.get(int(p), newcomer[1]) for p in ids])
    return float(share @ o), float(share @ d)
