"""Opponent-adjusted offensive and defensive ratings with conference shrinkage.

Each team-game contributes the offense's EPA per play (garbage time out),
modeled as

    EPA/play = league level + offense + opposing defense + home edge
               + FBS-vs-FCS edge

and fitted by weighted ridge regression. Every team's rating is its
conference's level plus its own deviation, and each part has its own pull
toward the preseason prior: deviations are pulled with the strength of a few
games, conference levels with the strength of many. With 130-plus FBS teams
that mostly play inside their conference, this lets a whole conference move
when its nonconference results say it was misjudged, and lets teams borrow
strength from their conference before they have much data of their own.
FCS teams are rated the same way inside their own conferences.

Ratings are in EPA per play: positive offense is good, positive defense is bad
(it allows more). The special-teams and pace ratings use the same machinery
with per-game values.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from .config import Hyperparams

# The league level, home edge and FBS-vs-FCS edge are nearly free parameters;
# these only keep them stable when a season has just a handful of games.
LEAGUE_PRIOR_PLAYS = 50.0
HOME_PRIOR_PLAYS = 3000.0
FCS_GAP_PRIOR_PLAYS = 3000.0
DEFAULT_HOME_EPA = 0.02
PLAYS_PER_GAME = 65.0


def conference_key(conference, division) -> str:
    """Conference name, with independents grouped by division."""
    if isinstance(conference, str) and conference and conference.lower() != "nan":
        return conference
    return f"{str(division).upper()} Independents"


@dataclass
class Ratings:
    off: dict[str, float] = field(default_factory=dict)
    deff: dict[str, float] = field(default_factory=dict)
    mu: float = 0.0
    hfa: float = DEFAULT_HOME_EPA
    fcs_gap: float = 0.0
    plays: dict[str, float] = field(default_factory=dict)
    conf_off: dict[str, float] = field(default_factory=dict)
    conf_def: dict[str, float] = field(default_factory=dict)

    def table(self) -> pd.DataFrame:
        teams = sorted(set(self.off) | set(self.deff))
        return pd.DataFrame({
            "team": teams,
            "off": [self.off.get(t, 0.0) for t in teams],
            "def": [self.deff.get(t, 0.0) for t in teams],
            "net": [self.off.get(t, 0.0) - self.deff.get(t, 0.0) for t in teams],
        }).sort_values("net", ascending=False, ignore_index=True)


@dataclass(frozen=True)
class Target:
    """One measure to rate offenses and defenses on.

    ``value`` is a team-game column summed over plays and ``weight`` the
    matching play weight, so the rated quantity is value per play; with no
    weight column the value is used per game. Prior strengths are in the same
    units as the weight (plays, or games).
    """

    name: str
    value: str
    weight: str | None
    off_prior: float
    def_prior: float
    conf_prior: float
    league_prior: float = LEAGUE_PRIOR_PLAYS
    home_prior: float = HOME_PRIOR_PLAYS
    fcs_prior: float = FCS_GAP_PRIOR_PLAYS
    garbage_weight: float = 0.0


def targets(hp: Hyperparams) -> dict[str, Target]:
    """The main EPA rating plus special teams and pace.

    Special teams (net EPA per game on kickoffs, punts and field goals) are
    noisy week to week, so they are pulled hard toward the prior. Pace (snaps
    per game) drives totals far more than margins.
    """
    g = PLAYS_PER_GAME
    return {
        "epa": Target("epa", "epa", "w", hp.off_prior_plays, hp.def_prior_plays, hp.conf_prior_plays,
                      garbage_weight=hp.garbage_weight),
        "st": Target("st", "st_epa", None, 10.0, 10.0, 60.0, league_prior=1.0,
                     home_prior=HOME_PRIOR_PLAYS / g, fcs_prior=FCS_GAP_PRIOR_PLAYS / g),
        "pace": Target("pace", "plays", None, 4.0, 6.0, 40.0, league_prior=1.0,
                       home_prior=HOME_PRIOR_PLAYS / g, fcs_prior=FCS_GAP_PRIOR_PLAYS / g),
    }


def prepare_rows(team_games: pd.DataFrame, target: Target) -> pd.DataFrame:
    """Team-game rows with the rated value, its weight, a home indicator and conferences."""
    tg = team_games
    if target.weight:
        value = tg[target.value] + target.garbage_weight * tg["g_epa"].fillna(0.0)
        weight = tg[target.weight] + target.garbage_weight * tg["g_plays"].fillna(0.0)
        rows = tg.assign(y=value / weight.where(weight > 0), w=weight)
        rows = rows[rows["w"] > 0]
    else:
        rows = tg[tg["plays"] > 0].assign(y=tg[target.value].astype(float), w=1.0)
    rows = rows.assign(
        h=np.where(rows["neutral"].astype(bool), 0.0, np.where(rows["home"] == 1, 1.0, -1.0)),
        g=np.where((rows["division"] == "fbs") & (rows["opp_division"] == "fcs"), 1.0,
                   np.where((rows["division"] == "fcs") & (rows["opp_division"] == "fbs"), -1.0, 0.0)),
        conf=[conference_key(c, d) for c, d in zip(rows["conference"], rows["division"])],
        opp_conf=[conference_key(c, d) for c, d in zip(rows["opp_conference"], rows["opp_division"])],
    )
    rows = rows[rows["y"].notna()]
    return rows[["game_id", "season", "week", "team", "opp", "conf", "opp_conf", "division",
                 "h", "g", "y", "w"]].reset_index(drop=True)


def memberships(rows: pd.DataFrame) -> dict[str, str]:
    """Each team's conference in these rows (its most common one)."""
    both = pd.concat([rows[["team", "conf"]],
                      rows[["opp", "opp_conf"]].set_axis(["team", "conf"], axis=1)])
    if both.empty:
        return {}
    return both.groupby("team")["conf"].agg(lambda s: s.value_counts().index[0]).to_dict()


def fit(rows: pd.DataFrame, ref_week: float, prior: Ratings, target: Target, half_life_weeks: float,
        conferences: dict[str, str] | None = None) -> Ratings:
    """Ridge fit of one season's rows toward ``prior``.

    ``conferences`` maps teams to this season's conference; teams missing from
    it (and from the rows) keep their prior.
    """
    conferences = {**memberships(rows), **(conferences or {})}
    seen = set(rows["team"]) | set(rows["opp"]) if len(rows) else set()
    teams = sorted(set(prior.off) | seen | set(conferences))
    confs = sorted({conferences.get(t, "Unknown") for t in teams})
    t_index = {t: i for i, t in enumerate(teams)}
    c_index = {c: i for i, c in enumerate(confs)}
    team_conf = np.array([c_index[conferences.get(t, "Unknown")] for t in teams])
    n_t, n_c = len(teams), len(confs)
    base = 3
    co, cd, do, dd = base, base + n_c, base + 2 * n_c, base + 2 * n_c + n_t
    n_params = dd + n_t

    # Prior: conference level = mean prior rating of its teams; team = the rest.
    p_off = np.array([prior.off.get(t, np.nan) for t in teams])
    p_def = np.array([prior.deff.get(t, np.nan) for t in teams])
    c_off = np.array([np.nanmean(np.where(team_conf == c, p_off, np.nan)) if np.any(
        (team_conf == c) & ~np.isnan(p_off)) else 0.0 for c in range(n_c)])
    c_def = np.array([np.nanmean(np.where(team_conf == c, p_def, np.nan)) if np.any(
        (team_conf == c) & ~np.isnan(p_def)) else 0.0 for c in range(n_c)])
    d_off = np.nan_to_num(p_off - c_off[team_conf])
    d_def = np.nan_to_num(p_def - c_def[team_conf])

    lam = np.concatenate([[target.league_prior, target.home_prior, target.fcs_prior],
                          np.full(n_c, target.conf_prior), np.full(n_c, target.conf_prior),
                          np.full(n_t, target.off_prior), np.full(n_t, target.def_prior)])
    beta0 = np.concatenate([[prior.mu, prior.hfa, prior.fcs_gap], c_off, c_def, d_off, d_def])
    A = np.diag(lam)
    b = lam * beta0
    plays = {t: 0.0 for t in teams}
    if len(rows):
        n = len(rows)
        ti = rows["team"].map(t_index).to_numpy()
        oi = rows["opp"].map(t_index).to_numpy()
        X = np.zeros((n, n_params))
        X[:, 0] = 1.0
        X[:, 1] = rows["h"].to_numpy()
        X[:, 2] = rows["g"].to_numpy()
        r = np.arange(n)
        X[r, co + team_conf[ti]] = 1.0
        X[r, cd + team_conf[oi]] = 1.0
        X[r, do + ti] = 1.0
        X[r, dd + oi] = 1.0
        recency = 0.5 ** ((ref_week - rows["week"].to_numpy()) / half_life_weeks)
        wts = rows["w"].to_numpy() * recency
        Xw = X * wts[:, None]
        A = A + Xw.T @ X
        b = b + Xw.T @ rows["y"].to_numpy()
        for team, weight in pd.Series(wts).groupby(rows["team"].to_numpy()).sum().items():
            plays[team] = float(weight)
    beta = np.linalg.solve(A, b)
    conf_o, conf_d = beta[co:co + n_c], beta[cd:cd + n_c]
    off = conf_o[team_conf] + beta[do:do + n_t]
    deff = conf_d[team_conf] + beta[dd:dd + n_t]
    return Ratings(
        off=dict(zip(teams, map(float, off))), deff=dict(zip(teams, map(float, deff))),
        mu=float(beta[0]), hfa=float(beta[1]), fcs_gap=float(beta[2]), plays=plays,
        conf_off=dict(zip(confs, map(float, conf_o))), conf_def=dict(zip(confs, map(float, conf_d))),
    )


class RatingsEngine:
    """Fits ratings for any point in any season, starting from preseason priors.

    ``priors`` supplies each season's prior (see ``prior.PriorModel``) and
    ``members`` each season's conference memberships.
    """

    def __init__(self, rows: pd.DataFrame, target: Target, half_life_weeks: float, priors,
                 members: dict[int, dict[str, tuple[str, str]]]):
        self.target = target
        self.half_life_weeks = half_life_weeks
        self.priors = priors
        self.members = members
        self.by_season = {s: r.reset_index(drop=True) for s, r in rows.groupby("season")}

    def prior(self, season: int) -> Ratings:
        return self.priors.prior(season)

    def before(self, season: int, week: int, ref_week: float | None = None) -> Ratings:
        """Ratings using only ``season`` games played before ``week``."""
        rows = self.by_season.get(season)
        rows = rows[rows["week"] < week] if rows is not None else pd.DataFrame(columns=["week"])
        conferences = {t: c for t, (c, _) in self.members.get(season, {}).items()}
        if rows.empty:
            rows = pd.DataFrame(columns=["team", "opp", "week", "h", "g", "y", "w", "conf", "opp_conf"])
        return fit(rows, week if ref_week is None else ref_week, self.prior(season), self.target,
                   self.half_life_weeks, conferences)
