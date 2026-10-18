"""Turn two goal rates into a distribution of real NHL scores.

Each game is played minute by minute, 10,000 times. In every minute each team
scores at its expected rate, adjusted for the score and the clock: teams tied
late play for overtime and score less, and trailing teams press. A team down
one or two goals late pulls its goalie as often as teams really do in that
minute, which lets it score six-on-five and lets the leader shoot at an empty
net. Tied regular-season games go to five minutes of three-on-three overtime
and then a shootout; playoff overtime is sudden death until someone scores.
As in the official result, the shootout winner is credited with one goal.

Everything is fitted from the minute-by-minute state tables on recent
seasons: the score-state multipliers, how often the goalie is pulled at each
deficit and minute, empty-net and six-on-five scoring rates, and the overtime
scoring rate. An exponent on the score-state effects and a shift that pushes
games closer are then tuned so the share of games tied after regulation and
the spread of regulation margins match history, and one scale so the
simulated goals with both goalies in match the expected rates.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field, replace

import numpy as np
import pandas as pd

from .config import THREE_ON_THREE_SEASON

PULL_MINUTES = list(range(54, 60))
BUCKETS = ("early", "third", "late")      # periods 1-2, minutes 40-49, last 10 minutes
STATES = ("tie", "lead", "trail")
REGULATION = 60
OT_MINUTES = 5.0


def _bucket(minute: int) -> int:
    return 0 if minute < 40 else 1 if minute < 50 else 2


@dataclass
class SimParams:
    # Rate multiplier for a team by clock bucket and its score state.
    state_mult: dict = field(default_factory=lambda: {b: {s: 1.0 for s in STATES} for b in BUCKETS})
    gamma: float = 1.0                    # exponent on the score-state effects (tuned)
    # Extra push toward closer games: trailing teams' rates times exp(shift),
    # leading teams' times exp(-shift). The raw multipliers understate score
    # effects, because the teams that trail are weaker teams on average (tuned).
    lead_shift: float = 0.0
    # Pulls usually start a little before the first event that shows the net
    # empty, so measured pull time runs short; this factor on the pull chances
    # is tuned so games with an empty-net goal are as common as in history.
    pull_scale: float = 1.0
    scale: float = 1.0                    # keeps simulated goals equal to the expected rates
    # Chance the trailing team has its goalie pulled, by deficit (1, 2, 3+) and minute 54-59.
    pull: dict = field(default_factory=lambda: {1: [0, 0, 0.01, 0.2, 0.65, 0.9],
                                                2: [0.02, 0.07, 0.27, 0.6, 0.65, 0.6],
                                                3: [0.05, 0.08, 0.09, 0.08, 0.05, 0.03]})
    en_rate: float = 0.34                 # empty-net goals per minute for the leader
    extra_rate: float = 0.135             # six-on-five goals per minute for the trailer
    ot_rate: float = 0.21                 # three-on-three goals per minute, both teams
    so_home: float = 0.5                  # home share of shootout wins
    mean_rate: float = 2.75               # league regulation goals per team the rates are relative to

    def mult_table(self) -> np.ndarray:
        """(bucket, state) multipliers with the tuned exponent and shift applied."""
        shift = {"tie": 1.0, "lead": np.exp(-self.lead_shift), "trail": np.exp(self.lead_shift)}
        return np.array([[self.state_mult[b][s] ** self.gamma * shift[s] for s in STATES] for b in BUCKETS])

    def to_dict(self) -> dict:
        d = asdict(self)
        d["pull"] = {str(k): [round(v, 4) for v in vals] for k, vals in self.pull.items()}
        d["state_mult"] = {b: {s: round(v, 4) for s, v in m.items()} for b, m in self.state_mult.items()}
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "SimParams":
        d = dict(d)
        d["pull"] = {int(k): list(v) for k, v in d["pull"].items()}
        return cls(**d)


def simulate(home_rate, away_rate, params: SimParams, n_sims: int = 10000, playoff=False,
             seed: int | None = 0) -> dict:
    """Simulate games. Rates are expected regulation goals with both goalies in.

    Returns (n_games, n_sims) arrays: final ``home`` and ``away`` goals (with
    overtime and the shootout decider), regulation goals ``reg_home`` and
    ``reg_away``, both-goalies-in goals ``even_home``/``even_away``,
    ``empty_net`` (whether an empty-net goal was scored) and ``ended``
    (0 regulation, 1 overtime, 2 shootout).
    """
    rng = np.random.default_rng(seed)
    lam_h = np.atleast_1d(np.asarray(home_rate, dtype=float))
    lam_a = np.atleast_1d(np.asarray(away_rate, dtype=float))
    playoff = np.broadcast_to(np.asarray(playoff, dtype=bool), lam_h.shape)
    n = len(lam_h)
    shape = (n, n_sims)
    base_h = np.broadcast_to((lam_h * params.scale / REGULATION)[:, None], shape)
    base_a = np.broadcast_to((lam_a * params.scale / REGULATION)[:, None], shape)
    # Empty-net and six-on-five rates scale gently with team quality.
    q_h = np.sqrt(np.clip(lam_h / params.mean_rate, 0.3, 3.0))[:, None]
    q_a = np.sqrt(np.clip(lam_a / params.mean_rate, 0.3, 3.0))[:, None]
    mult = params.mult_table()
    pull = {k: np.asarray(v, dtype=float) for k, v in params.pull.items()}

    h = np.zeros(shape, dtype=np.int64)
    a = np.zeros(shape, dtype=np.int64)
    even_h = np.zeros(shape, dtype=np.int64)
    even_a = np.zeros(shape, dtype=np.int64)
    empty_net = np.zeros(shape, dtype=bool)
    for minute in range(REGULATION):
        lead = h - a
        m = mult[_bucket(minute)]
        mh = np.where(lead == 0, m[0], np.where(lead > 0, m[1], m[2]))
        ma = np.where(lead == 0, m[0], np.where(lead < 0, m[1], m[2]))
        rate_h, rate_a = base_h * mh, base_a * ma
        if minute >= PULL_MINUTES[0]:
            deficit = np.minimum(np.abs(lead), 3)
            p = np.zeros(shape)
            for d in (1, 2, 3):
                p = np.where(deficit == d, min(pull[d][minute - PULL_MINUTES[0]] * params.pull_scale, 0.98), p)
            pulled = (lead != 0) & (rng.random(shape) < p)
            home_pulled = pulled & (lead < 0)
            away_pulled = pulled & (lead > 0)
            rate_h = np.where(home_pulled, params.extra_rate * q_h,
                              np.where(away_pulled, params.en_rate * q_h, rate_h))
            rate_a = np.where(away_pulled, params.extra_rate * q_a,
                              np.where(home_pulled, params.en_rate * q_a, rate_a))
        else:
            pulled = home_pulled = away_pulled = np.zeros(shape, dtype=bool)
        gh = rng.poisson(rate_h)
        ga = rng.poisson(rate_a)
        empty_net |= (away_pulled & (gh > 0)) | (home_pulled & (ga > 0))
        h += gh
        a += ga
        even_h += np.where(pulled, 0, gh)
        even_a += np.where(pulled, 0, ga)

    reg_h, reg_a = h.copy(), a.copy()
    tied = h == a
    ended = np.zeros(shape, dtype=np.int8)
    if tied.any():
        share = (lam_h / (lam_h + lam_a))[:, None]
        home_first = rng.random(shape) < share
        ot_total = params.ot_rate * OT_MINUTES * ((lam_h + lam_a) / (2 * params.mean_rate))[:, None]
        ot_goal = playoff[:, None] | (rng.random(shape) < 1.0 - np.exp(-ot_total))
        so_home = rng.random(shape) < params.so_home
        home_wins = np.where(ot_goal, home_first, so_home)
        h = h + (tied & home_wins)
        a = a + (tied & ~home_wins)
        ended = np.where(tied, np.where(ot_goal, 1, 2), 0).astype(np.int8)
    return {"home": h, "away": a, "reg_home": reg_h, "reg_away": reg_a,
            "even_home": even_h, "even_away": even_a, "empty_net": empty_net, "ended": ended}


def headline_score(home: np.ndarray, away: np.ndarray, home_wins: bool, spread: float = 1.0) -> tuple[int, int]:
    """A frequent final score near each team's expected goals in which the more
    likely winner wins (the single most frequent one is almost always 3-2)."""
    pairs, counts = np.unique(np.stack([home, away], axis=1), axis=0, return_counts=True)
    closeness = np.exp(-0.5 * (((pairs[:, 0] - home.mean()) / spread) ** 2
                               + ((pairs[:, 1] - away.mean()) / spread) ** 2))
    winner_ok = pairs[:, 0] > pairs[:, 1] if home_wins else pairs[:, 1] > pairs[:, 0]
    score = np.where(winner_ok, counts * closeness, -1.0)
    best = pairs[int(np.argmax(score))]
    return int(best[0]), int(best[1])


def summarize(sim: dict) -> pd.DataFrame:
    """Win probabilities, ranges and a headline score for each simulated game."""
    home, away, ended = sim["home"], sim["away"], sim["ended"]
    rows = []
    for i in range(home.shape[0]):
        h, a, e = home[i], away[i], ended[i]
        margin = h - a
        total = h + a
        p_home = float(np.mean(margin > 0))
        head_h, head_a = headline_score(h, a, p_home >= 0.5)
        rows.append({
            "home_win_prob": p_home,
            "away_win_prob": 1.0 - p_home,
            "home_reg_win_prob": float(np.mean((e == 0) & (margin > 0))),
            "away_reg_win_prob": float(np.mean((e == 0) & (margin < 0))),
            "ot_prob": float(np.mean(e > 0)),
            "so_prob": float(np.mean(e == 2)),
            "empty_net_prob": float(np.mean(sim["empty_net"][i])),
            "one_goal_reg_prob": float(np.mean(np.abs(sim["reg_home"][i] - sim["reg_away"][i]) == 1)),
            "home_cover_prob": float(np.mean(margin >= 2)),     # home -1.5
            "away_cover_prob": float(np.mean(margin <= -2)),    # away -1.5
            "sim_home": float(h.mean()), "sim_away": float(a.mean()), "sim_total": float(total.mean()),
            "home_low": int(np.percentile(h, 10)), "home_high": int(np.percentile(h, 90)),
            "away_low": int(np.percentile(a, 10)), "away_high": int(np.percentile(a, 90)),
            "headline_home": head_h, "headline_away": head_a,
        })
    return pd.DataFrame(rows)


def over_prob(sim: dict, lines: np.ndarray) -> np.ndarray:
    """Chance each game's total goes over its line (a push counts half)."""
    total = sim["home"] + sim["away"]
    lines = np.asarray(lines, dtype=float)[:, None]
    return np.mean(total > lines, axis=1) + 0.5 * np.mean(total == lines, axis=1)


# ---- fitting -------------------------------------------------------------

def fit_from_states(states: pd.DataFrame, params: SimParams | None = None) -> SimParams:
    """Score-state multipliers, pull chances and empty-net, six-on-five and
    overtime rates from minute-by-minute state tables (regular season)."""
    params = params or SimParams()
    st = states[states["game_type"].eq("R")]
    reg = st[st["minute"] < REGULATION]
    even = reg[reg["pulled"].eq("none")].copy()
    hours = even["seconds"].sum() / 3600.0
    overall = (even["home_goals"].sum() + even["away_goals"].sum()) / (2 * hours) if hours else 3.0
    even["bucket"] = np.select([even["minute"] < 40, even["minute"] < 50], ["early", "third"], "late")
    mult = {}
    for b, grp in even.groupby("bucket"):
        tied = grp[grp["home_lead"] == 0]
        hl = grp[grp["home_lead"] > 0]   # home leads
        al = grp[grp["home_lead"] < 0]   # away leads
        def rate(goals, secs):
            return goals / (secs / 3600.0) if secs > 0 else overall
        tie_r = rate(tied["home_goals"].sum() + tied["away_goals"].sum(), 2 * tied["seconds"].sum())
        lead_r = rate(hl["home_goals"].sum() + al["away_goals"].sum(), hl["seconds"].sum() + al["seconds"].sum())
        trail_r = rate(hl["away_goals"].sum() + al["home_goals"].sum(), hl["seconds"].sum() + al["seconds"].sum())
        mult[b] = {"tie": tie_r / overall, "lead": lead_r / overall, "trail": trail_r / overall}

    late = reg[reg["minute"].isin(PULL_MINUTES) & reg["home_lead"].ne(0)].copy()
    late["deficit"] = late["home_lead"].abs().clip(upper=3)
    trailer_pulled = ((late["home_lead"] < 0) & late["pulled"].eq("home")) | \
                     ((late["home_lead"] > 0) & late["pulled"].eq("away"))
    late["pulled_secs"] = late["seconds"].where(trailer_pulled, 0.0)
    share = late.groupby(["deficit", "minute"])[["pulled_secs", "seconds"]].sum()
    pull = {}
    for d in (1, 2, 3):
        vals = []
        for minute in PULL_MINUTES:
            try:
                row = share.loc[(d, minute)]
                vals.append(float(row["pulled_secs"] / row["seconds"]) if row["seconds"] > 0 else 0.0)
            except KeyError:
                vals.append(0.0)
        pull[d] = vals

    # Late pulls by a trailing team only: delayed-penalty pulls happen all game
    # and rarely end in an empty-net goal.
    pulled = reg[reg["minute"].isin(PULL_MINUTES)
                 & ((reg["pulled"].eq("home") & (reg["home_lead"] < 0))
                    | (reg["pulled"].eq("away") & (reg["home_lead"] > 0)))]
    mins = pulled["seconds"].sum() / 60.0
    home_out = pulled["pulled"].eq("home")
    en = pulled.loc[home_out, "away_goals"].sum() + pulled.loc[~home_out, "home_goals"].sum()
    extra = pulled.loc[home_out, "home_goals"].sum() + pulled.loc[~home_out, "away_goals"].sum()
    ot = st[(st["minute"] >= REGULATION) & (st["season"] >= THREE_ON_THREE_SEASON)]
    ot_mins = ot["seconds"].sum() / 60.0
    ot_goals = ot["home_goals"].sum() + ot["away_goals"].sum()
    return replace(
        params, state_mult=mult, pull=pull,
        en_rate=float(en / mins) if mins else params.en_rate,
        extra_rate=float(extra / mins) if mins else params.extra_rate,
        ot_rate=float(ot_goals / ot_mins) if ot_mins else params.ot_rate,
        mean_rate=float(overall),
    )


def margin_shares(home: np.ndarray, away: np.ndarray) -> np.ndarray:
    """Shares of absolute margins 0, 1, 2 and 3 or more."""
    m = np.minimum(np.abs(np.asarray(home) - np.asarray(away)), 3)
    return np.array([np.mean(m == k) for k in range(4)])


def calibrate(params: SimParams, home_rate: np.ndarray, away_rate: np.ndarray, tie_rate: float,
              even_margins: np.ndarray | None = None, en_share: float | None = None,
              n_sims: int = 120, max_games: int = 1200, seed: int = 3) -> SimParams:
    """Tune the score-state exponent and the lead shift so simulated games are
    tied after regulation as often as real ones and end with the real spread of
    regulation margins (goals with both goalies in); then the pull factor so
    as many games have an empty-net goal; then the scale so simulated
    both-goalies-in goals match the expected rates.

    ``even_margins`` are the historical shares of absolute both-goalies-in
    regulation margins 0, 1, 2 and 3+; without them only the tie rate is used.
    """
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(home_rate))[:max_games]
    lh, la = np.asarray(home_rate)[idx], np.asarray(away_rate)[idx]
    target = float(np.mean(lh + la))
    shifts = (0.0, 0.05, 0.1, 0.15, 0.2, 0.25) if even_margins is not None else (params.lead_shift,)
    best, best_err, scale = params, np.inf, params.scale
    for gamma in (0.5, 1.0, 1.5, 2.0, 2.5, 3.0):
        for shift in shifts:
            trial = replace(params, gamma=gamma, lead_shift=shift, scale=scale)
            sim = simulate(lh, la, trial, n_sims=n_sims, seed=seed)
            # Rescale from this run rather than rerunning: the shares barely move.
            scale = trial.scale * target / float(np.mean(sim["even_home"] + sim["even_away"]))
            err = (float(np.mean(sim["reg_home"] == sim["reg_away"])) - tie_rate) ** 2
            if even_margins is not None:
                err += float(np.sum((margin_shares(sim["even_home"], sim["even_away"]) - even_margins) ** 2))
            if err < best_err:
                best, best_err = replace(trial, scale=scale), err
    if en_share is not None:
        errs = {}
        for factor in (1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6):
            sim = simulate(lh, la, replace(best, pull_scale=factor), n_sims=n_sims, seed=seed + 2)
            errs[factor] = abs(float(np.mean(sim["empty_net"])) - en_share)
        best = replace(best, pull_scale=min(errs, key=errs.get))
    for _ in range(2):
        sim = simulate(lh, la, best, n_sims=n_sims, seed=seed + 1)
        best = replace(best, scale=best.scale * target / float(np.mean(sim["even_home"] + sim["even_away"])))
    return best
