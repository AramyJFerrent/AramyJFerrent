"""Pregame features for every game, using only what was known beforehand.

For each side of a game, from the batting team's point of view:

- ``x_sp``: its lineup against the opposing starter. Each of the nine
  batters meets the starter in a log5 plate appearance with the platoon
  factor for his side and the starter's hand; the outcome probabilities are
  averaged with each lineup slot's share of plate appearances and turned into
  runs with linear weights from the base-out chain. Expressed as the change
  in run rate against a league-average matchup.
- ``x_bp``: the same lineup against the opposing bullpen: every reliever who
  pitched in the team's last 15 games, weighted by how much he has been used
  and marked down when he pitched the day before (more so after a long
  outing) or on consecutive days.
- ``s1``..``s9``: the opposing starter's expected share of each inning,
  from how deep his recent starts went.
- Park run factor, home field, temperature and wind blowing in or out.

Historical games use the actual lineups and starters (what a game-day run
knows once lineups post); upcoming ones use confirmed lineups when posted and
otherwise the lineup the team last used against a starter of the same hand.
Ratings for a game come only from games on earlier days.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import norm

from .config import Hyperparams
from .elo import run_elo
from .parks import COMPONENTS, ParkFactors
from .players import POOL_HALF_LIFE, PlayerRatings, RateEngine, log5, platoon_factors, season_time
from .ratings import TeamRatings
from .simulate import MarkovChain

SLOTS = 9
INNINGS = 9
BULLPEN_GAMES = 15
OUTS_SD = 4.5
# Converts a run value per plate appearance into a relative change in the
# run rate (about 4.25 plate appearances and 0.5 runs per inning).
RV_SCALE = 4.25 / 0.5
DEFAULT_SLOT_PA = np.array([4.65, 4.55, 4.45, 4.35, 4.25, 4.15, 4.05, 3.95, 3.85])
CHAIN_SEASONS = 3
PLATOON_SEASONS = 5
NEUTRAL_TEMP = 70.0

GAME_COLUMNS = ["game_id", "season", "game_type", "playoff", "neutral", "start", "date", "game_number",
                "home_team", "away_team", "park_id", "dome", "temp", "wind", "wind_speed", "sched_innings",
                "tiebreaker", "completed", "status", "home_score", "away_score", "innings",
                "home_line", "away_line"]


def lineup_table(batting: pd.DataFrame) -> pd.DataFrame:
    """Starting lineups: one row per (game, team) with ``p1``..``p9`` and ``pos1``..``pos9``."""
    st = batting[batting["slot"].between(1, SLOTS)].drop_duplicates(["game_id", "team", "slot"])
    players = st.pivot(index=["game_id", "team"], columns="slot", values="player_id")
    pos = st.pivot(index=["game_id", "team"], columns="slot", values="pos")
    players.columns = [f"p{c}" for c in players.columns]
    pos.columns = [f"pos{c}" for c in pos.columns]
    out = players.join(pos).reindex(columns=[f"p{i}" for i in range(1, 10)] + [f"pos{i}" for i in range(1, 10)])
    return out


def slot_weights(batting: pd.DataFrame, games: pd.DataFrame) -> np.ndarray:
    """Average plate appearances per game by lineup slot (starters and their replacements)."""
    b = batting.join(games.set_index("game_id")["sched_innings"], on="game_id")
    b = b[b["sched_innings"].eq(9)]
    # Substitutes inherit the slot of the starter they replace only in the raw
    # files; here each game's slot totals come from team PA by batting order.
    starters = b[b["slot"].between(1, SLOTS)].groupby("slot")["pa"].mean()
    if len(starters) < SLOTS:
        return DEFAULT_SLOT_PA
    return starters.reindex(range(1, 10)).to_numpy(float)


def starter_shares(mean_outs: np.ndarray, sd: float = OUTS_SD) -> np.ndarray:
    """(n, 9) expected share of each inning's outs recorded by the starter."""
    outs = np.arange(28)
    pdf = norm.pdf(outs[None, :], np.asarray(mean_outs, dtype=float)[:, None], sd)
    pdf /= pdf.sum(axis=1, keepdims=True)
    shares = np.stack([np.clip(outs - 3 * i, 0, 3) / 3.0 for i in range(INNINGS)], axis=1)   # (28, 9)
    return pdf @ shares


def weather_features(g: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
    """Temperature above 70°F (per 10°F) and wind blowing out (+) or in (-) (per 10 mph),
    both zero under a roof or when unknown."""
    open_air = ~g["dome"].fillna(0).astype(bool).to_numpy()
    temp = pd.to_numeric(g["temp"], errors="coerce").to_numpy(float)
    temp = np.where(open_air & np.isfinite(temp), (temp - NEUTRAL_TEMP) / 10.0, 0.0)
    speed = pd.to_numeric(g["wind_speed"], errors="coerce").fillna(0.0).to_numpy(float)
    sign = g["wind"].map({"out": 1.0, "in": -1.0}).fillna(0.0).to_numpy(float)
    return temp, np.where(open_air, sign * speed / 10.0, 0.0)


class FeatureBuilder:
    def __init__(self, summaries: dict, hp: Hyperparams):
        self.hp = hp
        self.games = summaries["games"]
        self.batting = summaries["batting"]
        self.pitching = summaries["pitching"]
        self.transitions = summaries["transitions"]
        self.platoon_counts = summaries["platoon"]
        players = summaries["players"].drop_duplicates("player_id", keep="last").set_index("player_id")
        self.bats = players["bats"]
        self.throws = players["throws"]
        self.names = players["name"]
        self.parks = ParkFactors(self.games, self.batting, hp)
        self.ratings = PlayerRatings(summaries, self.parks, hp)
        self.lineups = lineup_table(self.batting)
        self.slot_pa = slot_weights(self.batting, self.games)

        g = self.games.set_index("game_id")
        st = self.pitching[self.pitching["starter"] == 1].join(g[["date", "season"]], on="game_id", how="inner")
        tau = season_time(st["date"], st["season"])
        ones = np.ones(len(st))
        self.starts = RateEngine(st["player_id"], tau, ones, st[["outs"]].to_numpy(float), hp.starter_outs_half_life)
        self.start_pool = RateEngine(np.full(len(st), "_SP"), tau, ones, st[["outs"]].to_numpy(float), POOL_HALF_LIFE)

        done = self.games[self.games["completed"]]
        env_rows = []
        for side in ("home", "away"):
            n = (done["sched_innings"] - 1).to_numpy()
            runs = [sum(int(v) for v in str(line).split()[:k] if v != "x") for line, k in zip(done[f"{side}_line"], n)]
            env_rows.append(pd.DataFrame({"tau": season_time(done["date"], done["season"]), "n": n, "runs": runs}))
        env = pd.concat(env_rows, ignore_index=True)
        self.env = RateEngine(np.full(len(env), "_ENV"), env["tau"], env["n"], env[["runs"]].to_numpy(float),
                              POOL_HALF_LIFE)

        self.team_games = self._team_game_order(self.games)
        relief = self.pitching[self.pitching["starter"] == 0].join(g[["date"]], on="game_id", how="inner")
        relief = relief.join(self.team_games.set_index(["game_id", "team"])["seq"].rename("team_seq"),
                             on=["game_id", "team"])
        self.relief = relief.dropna(subset=["team_seq"]).sort_values(["team", "team_seq"])
        self.teams = TeamRatings(self.games, hp.team_prior_games, hp.team_carryover, hp.team_half_life)
        elo, self.elo_ratings = run_elo(self.games, self.pitching)
        self.elo = elo.set_index("game_id")
        self._chains: dict[int, MarkovChain] = {}
        self._platoon: dict[int, dict] = {}

    # ---- season-level tables ----------------------------------------------
    def chain(self, season: int) -> MarkovChain:
        """Base-out chain from the (up to) three Retrosheet seasons before ``season``."""
        if season not in self._chains:
            t = self.transitions
            have = sorted(t["season"].unique())
            before = [s for s in have if s < season][-CHAIN_SEASONS:] or have[:CHAIN_SEASONS]
            self._chains[season] = MarkovChain(t[t["season"].isin(before)])
        return self._chains[season]

    def platoon(self, season: int) -> dict:
        if season not in self._platoon:
            p = self.platoon_counts
            have = sorted(p["season"].unique())
            before = [s for s in have if s < season][-PLATOON_SEASONS:] or have[:PLATOON_SEASONS]
            self._platoon[season] = platoon_factors(p[p["season"].isin(before)])
        return self._platoon[season]

    def linear_weights(self, season: int) -> np.ndarray:
        lw = self.chain(season).linear_weights()
        return np.array([lw[e] for e in COMPONENTS] + [0.0])

    @staticmethod
    def _team_game_order(games: pd.DataFrame) -> pd.DataFrame:
        rows = pd.concat([
            pd.DataFrame({"game_id": games["game_id"], "team": games["home_team"], "start": games["start"],
                          "date": games["date"]}),
            pd.DataFrame({"game_id": games["game_id"], "team": games["away_team"], "start": games["start"],
                          "date": games["date"]}),
        ], ignore_index=True)
        rows = rows.sort_values(["team", "date", "start", "game_id"]).reset_index(drop=True)
        rows["seq"] = rows.groupby("team").cumcount()
        return rows

    # ---- components ------------------------------------------------------
    def environment(self, tau) -> np.ndarray:
        """League runs per half-inning (innings both teams bat), recency-weighted."""
        s = self.env.sums(np.full(len(tau), "_ENV"), tau)
        return (s[:, 1] + 50 * 0.5) / (s[:, 0] + 50)

    def expected_outs(self, pitchers, tau) -> np.ndarray:
        """Outs the starter is expected to record, from his recent starts."""
        own = self.starts.sums(pitchers, tau)
        pool = self.start_pool.sums(np.full(len(tau), "_SP"), tau)
        prior = np.where(pool[:, 0] > 0, pool[:, 1] / np.maximum(pool[:, 0], 1e-9), 16.0)
        k = self.hp.starter_outs_prior
        known = pd.notna(pd.Series(pitchers)).to_numpy()
        return np.where(known, (own[:, 1] + k * prior) / (own[:, 0] + k), prior)

    def bullpens(self, queries: pd.DataFrame) -> pd.DataFrame:
        """Composite reliever rates for each (game, pitching team) in ``queries``
        (columns game_id, team, date, tau), from the team's previous games."""
        order = self.team_games
        out_rates = np.zeros((len(queries), len(COMPONENTS)))
        lefty = np.full(len(queries), 0.3)
        load = np.zeros(len(queries))
        q = queries.reset_index(drop=True)
        pairs = []
        for team, idx in q.groupby("team").groups.items():
            tg = order[order["team"] == team]
            dates = pd.to_datetime(tg["date"]).to_numpy()
            qd = pd.to_datetime(q.loc[idx, "date"]).to_numpy()
            hi = np.searchsorted(dates, qd, side="left")     # team games strictly before the date
            lo = np.maximum(hi - BULLPEN_GAMES, 0)
            apps = self.relief[self.relief["team"] == team]
            aseq = apps["team_seq"].to_numpy()
            a_lo = np.searchsorted(aseq, lo, side="left")
            a_hi = np.searchsorted(aseq, hi, side="left")
            counts = a_hi - a_lo
            if counts.sum() == 0:
                continue
            qi = np.repeat(np.asarray(idx), counts)
            ai = np.concatenate([np.arange(s, e) for s, e in zip(a_lo, a_hi)])
            sel = apps.iloc[ai]
            pairs.append(pd.DataFrame({"q": qi, "player_id": sel["player_id"].to_numpy(),
                                       "bf": sel["bf"].to_numpy(float), "pitches": sel["pitches"].to_numpy(float),
                                       "days": (np.repeat(qd, counts) - pd.to_datetime(sel["date"]).to_numpy())
                                       .astype("timedelta64[D]").astype(int)}))
        if pairs:
            p = pd.concat(pairs, ignore_index=True)
            p["d1"] = p["days"].eq(1)
            p["d2"] = p["days"].eq(2)
            p["p1"] = np.where(p["d1"], p["pitches"], 0.0)
            p["recent"] = p["days"].le(4)
            p["p3"] = np.where(p["days"].le(3), p["pitches"], 0.0)
            per = p.groupby(["q", "player_id"]).agg(bf=("bf", "sum"), d1=("d1", "any"), d2=("d2", "any"),
                                                   p1=("p1", "sum"), recent=("recent", "sum"),
                                                   p3=("p3", "sum")).reset_index()
            avail = np.ones(len(per))
            avail *= np.where(per["d1"], np.where(per["p1"] >= 25, 0.25, 0.5), 1.0)
            avail *= np.where(per["d1"] & per["d2"], 0.3, 1.0)
            avail *= np.where(per["recent"] >= 3, 0.3, 1.0)
            w = per["bf"].to_numpy(float) * avail
            tau = q.loc[per["q"], "tau"].to_numpy()
            rates, _ = self.ratings.pitchers(per["player_id"].to_numpy(), tau, np.zeros(len(per), dtype=bool))
            num = pd.DataFrame(rates * w[:, None]).groupby(per["q"].to_numpy()).sum()
            den = pd.Series(w).groupby(per["q"].to_numpy()).sum()
            left = pd.Series(w * per["player_id"].map(self.throws).eq("L").to_numpy()).groupby(per["q"].to_numpy()).sum()
            load_q = per.groupby("q")["p3"].sum()
            has = den.index.to_numpy()
            out_rates[has] = num.loc[has].to_numpy() / den.loc[has].to_numpy()[:, None]
            lefty[has] = (left.loc[has] / den.loc[has]).to_numpy()
            load[load_q.index.to_numpy()] = load_q.to_numpy()
        else:
            has = np.array([], dtype=int)
        missing = np.setdiff1d(np.arange(len(q)), has)
        if len(missing):
            prior, _ = self.ratings.pitchers(np.full(len(missing), None), q.loc[missing, "tau"].to_numpy(),
                                             np.zeros(len(missing), dtype=bool))
            out_rates[missing] = prior
        return pd.DataFrame({"bp_rates": list(out_rates), "bp_lefty": lefty, "bp_load": load / 100.0})

    def projected_lineups(self, queries: pd.DataFrame) -> pd.DataFrame:
        """The lineup each team last used against a starter of the same hand
        (any hand when it has none yet). ``queries``: team, date, opp_throws."""
        known = self.lineups.reset_index().join(
            self.games.set_index("game_id")[["date", "start", "home_team", "home_starter", "away_starter"]],
            on="game_id", how="inner")
        opp_sp = np.where(known["team"] == known["home_team"], known["away_starter"], known["home_starter"])
        known["opp_throws"] = pd.Series(opp_sp).map(self.throws).fillna("R").to_numpy()
        known["when"] = pd.to_datetime(known["date"])
        known = known.sort_values("when")
        cols = [f"p{i}" for i in range(1, 10)] + [f"pos{i}" for i in range(1, 10)]
        q = queries.reset_index(drop=True).copy()
        q["when"] = pd.to_datetime(q["date"])
        q["_i"] = np.arange(len(q))
        q = q.sort_values("when")
        same = pd.merge_asof(q, known[["when", "team", "opp_throws"] + cols], on="when", by=["team", "opp_throws"],
                             allow_exact_matches=False)
        anyhand = pd.merge_asof(q, known[["when", "team"] + cols], on="when", by="team", allow_exact_matches=False)
        same = same.set_index("_i").sort_index()
        anyhand = anyhand.set_index("_i").sort_index()
        return same[cols].where(same["p1"].notna(), anyhand[cols])

    # ---- features --------------------------------------------------------
    def side_features(self, q: pd.DataFrame, season: int) -> pd.DataFrame:
        """Features for batting-side queries of one season. ``q`` columns:
        game_id, team, opp, date, tau, opp_starter, p1..p9, pos1..pos9."""
        n = len(q)
        tau = q["tau"].to_numpy()
        league = self.ratings.league(tau)
        lw = self.linear_weights(season)
        factors = self.platoon(season)
        ones = np.ones(len(COMPONENTS) + 1)

        sp = q["opp_starter"].to_numpy(object)
        sp_rates, sp_n = self.ratings.pitchers(sp, tau, np.ones(n, dtype=bool))
        sp_throws = pd.Series(sp).map(self.throws).fillna("R").to_numpy()
        pen = self.bullpens(pd.DataFrame({"game_id": q["game_id"], "team": q["opp"], "date": q["date"], "tau": tau}))
        bp_rates = np.stack(pen["bp_rates"].to_numpy())
        lefty = pen["bp_lefty"].to_numpy()

        weights = self.slot_pa / self.slot_pa.sum()
        probs_sp = np.zeros((n, len(COMPONENTS) + 1))
        probs_bp = np.zeros_like(probs_sp)
        probs_lg = np.zeros_like(probs_sp)
        for i in range(SLOTS):
            pid = q[f"p{i + 1}"].to_numpy(object)
            pitcher_bat = pd.to_numeric(q[f"pos{i + 1}"], errors="coerce").eq(1).to_numpy()
            b_rates, _ = self.ratings.batters(pid, tau, pitcher_bat)
            bats = pd.Series(pid).map(self.bats).fillna("R").to_numpy()
            f_sp = np.stack([factors.get((b, t), ones) for b, t in zip(bats, sp_throws)])
            f_l = np.stack([factors.get((b, "L"), ones) for b in bats])
            f_r = np.stack([factors.get((b, "R"), ones) for b in bats])
            f_bp = lefty[:, None] * f_l + (1 - lefty[:, None]) * f_r
            probs_sp += weights[i] * log5(b_rates, sp_rates, league, f_sp)
            probs_bp += weights[i] * log5(b_rates, bp_rates, league, f_bp)
            probs_lg += weights[i] * log5(b_rates, league, league)
        base = log5(league, league, league)
        rv_lg = base @ lw
        outs = self.expected_outs(sp, tau)
        shares = starter_shares(outs)
        out = pd.DataFrame({
            "x_sp": (probs_sp @ lw - rv_lg) * RV_SCALE,
            "x_bp": (probs_bp @ lw - rv_lg) * RV_SCALE,
            "opp_starter_outs": outs,
            "opp_starter_bf": sp_n,
            "opp_starter_x": (log5(league, sp_rates, league) @ lw - rv_lg) * RV_SCALE,
            "opp_bp_x": (log5(league, bp_rates, league) @ lw - rv_lg) * RV_SCALE,
            "opp_bp_load": pen["bp_load"].to_numpy(),
            "lineup_x": (probs_lg @ lw - rv_lg) * RV_SCALE,
        })
        for i in range(INNINGS):
            out[f"s{i + 1}"] = shares[:, i]
        return out

    def build(self, games: pd.DataFrame, lineups: pd.DataFrame | None = None, known_lineups: bool = True) -> pd.DataFrame:
        """Feature rows for ``games`` (one season or several), each from earlier days only.

        ``lineups`` (indexed by game_id and team) overrides the stored lineups,
        for confirmed lineups of upcoming games. Without ``known_lineups`` every
        lineup is projected from earlier games, as a morning run would.
        """
        if games.empty:
            return pd.DataFrame()
        frames = []
        for season, sg in games.groupby("season", sort=True):
            sg = sg.reset_index(drop=True)
            tau = season_time(sg["date"], sg["season"])
            temp, wind = weather_features(sg)
            log_pf = np.log(self.parks.lookup(sg["season"], sg["park_id"], "runs"))
            rows = sg[[c for c in GAME_COLUMNS if c in sg]].copy()
            rows["env"] = self.environment(tau)
            rows["log_pf"] = log_pf
            rows["temp_x"] = temp
            rows["wind_x"] = wind
            for side, other in (("home", "away"), ("away", "home")):
                q = pd.DataFrame({"game_id": sg["game_id"], "team": sg[f"{side}_team"], "opp": sg[f"{other}_team"],
                                  "date": sg["date"], "tau": tau, "opp_starter": sg[f"{other}_starter"]})
                q["opp_throws"] = q["opp_starter"].map(self.throws).fillna("R")
                cols = [f"p{i}" for i in range(1, 10)] + [f"pos{i}" for i in range(1, 10)]
                key = pd.MultiIndex.from_arrays([q["game_id"], q["team"]])
                given = pd.DataFrame(index=key, columns=cols, dtype=object)
                status = np.full(len(q), "projected", dtype=object)
                if lineups is not None and len(lineups):
                    given = lineups.reindex(key)[cols].astype(object)
                if known_lineups:
                    stored = self.lineups.reindex(key)[cols].astype(object)
                    missing = given["p1"].isna().to_numpy()
                    given.iloc[missing] = stored.iloc[missing].to_numpy()
                have = given["p1"].notna().to_numpy()
                status[have] = "confirmed"
                filled = given.reset_index(drop=True)
                if (~have).any():
                    proj = self.projected_lineups(q)
                    filled.iloc[~have] = proj.iloc[~have].to_numpy()
                q = pd.concat([q, filled[cols]], axis=1)
                f = self.side_features(q, int(season))
                f.columns = [f"{side}_{c}" for c in f.columns]
                rows = pd.concat([rows, f], axis=1)
                rows[f"{side}_lineup"] = status
                rows[f"{side}_starter"] = sg[f"{side}_starter"].to_numpy()
                rows[f"{side}_h"] = np.where(sg["neutral"], 0.0, 0.5 if side == "home" else -0.5)
            team = {d: self.teams.before(int(season), d) for d in sg["date"].unique()}
            for side, other in (("home", "away"), ("away", "home")):
                rows[f"{side}_team_off"] = [team[d].off.get(t, 0.0) / team[d].mu
                                            for d, t in zip(sg["date"], sg[f"{side}_team"])]
                rows[f"{side}_team_def"] = [team[d].deff.get(t, 0.0) / team[d].mu
                                            for d, t in zip(sg["date"], sg[f"{other}_team"])]
            elo = self.elo.reindex(sg["game_id"])
            rows["elo_home_prob"] = elo["elo_home_prob"].to_numpy()
            rows["elo_logit"] = elo["elo_diff"].to_numpy() * np.log(10) / 400.0
            frames.append(rows)
        out = pd.concat(frames, ignore_index=True)
        for side in ("home", "away"):
            n = out["sched_innings"].fillna(9).astype(int) - 1
            lines = out[f"{side}_line"].fillna("").astype(str).str.split()
            out[f"{side}_r8"] = [sum(int(v) for v in parts[:k] if v != "x") if len(parts) >= k else np.nan
                                 for parts, k in zip(lines, n)]
            out.loc[~out["completed"], f"{side}_r8"] = np.nan
        return out

    # ---- team summary ----------------------------------------------------
    def team_table(self, season: int, today) -> pd.DataFrame:
        """Each team's current lineup, rotation and bullpen against league average,
        as changes in run rate (same units as ``x_sp``), plus team ratings and Elo."""
        tau0 = int(season_time([today], [season])[0])
        g = self.games
        played = g[g["completed"] & (pd.to_datetime(g["date"]) < pd.Timestamp(today))
                   & g["season"].between(season - 1, season)]
        teams = sorted(set(g.loc[g["season"] == season, "home_team"]) | set(g.loc[g["season"] == season, "away_team"]))
        if not teams:
            teams = sorted(set(played["home_team"]))
        league = self.ratings.league(np.array([tau0]))
        lw = self.linear_weights(season)
        rv_lg = (log5(league, league, league) @ lw)[0]
        weights = self.slot_pa / self.slot_pa.sum()
        lineups = self.lineups.reset_index().merge(played[["game_id", "date"]], on="game_id")
        starts = self.pitching[self.pitching["starter"] == 1].merge(played[["game_id", "date"]], on="game_id")
        pen = self.bullpens(pd.DataFrame({"game_id": "next", "team": teams, "date": today, "tau": tau0}))
        ratings = self.teams.before(season, today) if season in self.teams.by_season else self.teams.prior(season)
        rows = []
        for i, team in enumerate(teams):
            row = {"team": team}
            lu = lineups[lineups["team"] == team].sort_values("date")
            if len(lu):
                last = lu.iloc[-1]
                x = 0.0
                for j in range(SLOTS):
                    pid = np.array([last[f"p{j + 1}"]], dtype=object)
                    b, _ = self.ratings.batters(pid, np.array([tau0]), [pd.to_numeric(last[f"pos{j + 1}"]) == 1])
                    x += weights[j] * (log5(b, league, league) @ lw)[0]
                row["lineup_x"] = (x - rv_lg) * RV_SCALE
            else:
                row["lineup_x"] = 0.0
            st = starts[starts["team"] == team].sort_values("date").drop_duplicates("player_id", keep="last").tail(5)
            if len(st):
                r, _ = self.ratings.pitchers(st["player_id"].to_numpy(object), np.full(len(st), tau0),
                                             np.ones(len(st), dtype=bool))
                row["rotation_x"] = float(np.mean((log5(np.repeat(league, len(st), 0), r,
                                                        np.repeat(league, len(st), 0)) @ lw - rv_lg) * RV_SCALE))
                row["rotation_outs"] = float(np.mean(self.expected_outs(st["player_id"].to_numpy(object),
                                                                         np.full(len(st), tau0))))
            else:
                row["rotation_x"], row["rotation_outs"] = 0.0, 16.0
            bp = np.stack([pen["bp_rates"].iloc[i]])
            row["bullpen_x"] = float(((log5(league, bp, league) @ lw)[0] - rv_lg) * RV_SCALE)
            row["team_off"] = ratings.off.get(team, 0.0) / max(ratings.mu, 1e-9)
            row["team_def"] = ratings.deff.get(team, 0.0) / max(ratings.mu, 1e-9)
            row["elo"] = self.elo_ratings.get(team, np.nan)
            rows.append(row)
        return pd.DataFrame(rows)
