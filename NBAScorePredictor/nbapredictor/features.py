"""Pregame features for every game, using only what was known beforehand.

For historical games this is a walk-forward pass by date: the features for a
game come from ratings fitted on that season's earlier days plus the
preseason priors. For upcoming games the same features come from every game
played before today.

Availability: in history, a team's available players are the ones who played
(what the final injury report says at tip-off), but their minutes are
projected from earlier games, never taken from the box score. With
``availability="previous"`` the available players are instead the ones who
played the team's previous game, as a morning run before injury news would
assume. Upcoming games take availability from the injury report.
"""

from __future__ import annotations

from collections import defaultdict

import numpy as np
import pandas as pd

from .config import ARENAS_PATH, REG_MINUTES, Hyperparams
from .elo import run_elo
from .players import PlayerRatings, lineup_strength, minutes_history, rescale_minutes
from .ratings import RatingsEngine, prepare_rows, season_day, targets

# League scoring and pace drift, so the baselines are recency-weighted
# averages of recent games rather than fixed numbers.
ENV_HALF_LIFE_DAYS = 60.0
ENV_PRIOR_GAMES = 30.0
MAX_REST = 4
EARTH_KM = 6371.0
EPOCH = pd.Timestamp("2000-01-01")

GAME_COLUMNS = ["game_id", "season", "game_type", "playoff", "neutral", "start", "date",
                "home_team", "away_team", "completed", "home_score", "away_score", "periods"]


def day_index(dates) -> np.ndarray:
    return (pd.to_datetime(pd.Series(dates)) - EPOCH).dt.days.to_numpy()


def _distance_km(lat1, lon1, lat2, lon2) -> np.ndarray:
    p1, p2 = np.radians(lat1), np.radians(lat2)
    dphi, dlmb = p2 - p1, np.radians(lon2) - np.radians(lon1)
    h = np.sin(dphi / 2) ** 2 + np.cos(p1) * np.cos(p2) * np.sin(dlmb / 2) ** 2
    return 2 * EARTH_KM * np.arcsin(np.sqrt(h))


def schedule_context(games: pd.DataFrame) -> pd.DataFrame:
    """Rest days, travel distance and time zones crossed for each side,
    including scheduled games. A team's first game of a season counts as
    rested and travels from home."""
    arenas = pd.read_csv(ARENAS_PATH).set_index("city")
    g = games.copy()

    def mode(v):
        v = v.dropna()
        return v.mode().iloc[0] if len(v) else None
    home_city = g.groupby(["season", "home_team"])["city"].transform(mode)
    city = g["city"].where(g["city"].isin(arenas.index), home_city)
    g["lat"] = city.map(arenas["lat"])
    g["lon"] = city.map(arenas["lon"])
    g["tz"] = city.map(arenas["utc_offset"])
    homes = g.groupby(["season", "home_team"])["city"].agg(mode)
    long = pd.concat([
        pd.DataFrame({"game_id": g["game_id"], "team": g[f"{side}_team"], "side": side, "season": g["season"],
                      "dix": day_index(g["date"]), "start": g["start"], "lat": g["lat"], "lon": g["lon"],
                      "tz": g["tz"]})
        for side in ("home", "away")
    ]).sort_values(["team", "start", "game_id"])
    grp = long.groupby(["team", "season"])
    prev_dix = grp["dix"].shift()
    long["rest"] = (long["dix"] - prev_dix).clip(upper=MAX_REST).fillna(MAX_REST)
    base = pd.Series(list(zip(long["season"], long["team"]))).map(homes).to_numpy()
    base_lat = pd.Series(base).map(arenas["lat"]).to_numpy()
    base_lon = pd.Series(base).map(arenas["lon"]).to_numpy()
    base_tz = pd.Series(base).map(arenas["utc_offset"]).to_numpy()
    prev_lat = grp["lat"].shift().to_numpy()
    prev_lon = grp["lon"].shift().to_numpy()
    prev_tz = grp["tz"].shift().to_numpy()
    prev_lat = np.where(np.isnan(prev_lat), base_lat, prev_lat)
    prev_lon = np.where(np.isnan(prev_lon), base_lon, prev_lon)
    prev_tz = np.where(np.isnan(prev_tz), base_tz, prev_tz)
    long["travel"] = np.nan_to_num(_distance_km(prev_lat, prev_lon, long["lat"].to_numpy(), long["lon"].to_numpy()))
    long["tz_shift"] = np.nan_to_num(long["tz"].to_numpy() - prev_tz)
    wide = long.pivot_table(index="game_id", columns="side", values=["rest", "travel", "tz_shift"])
    wide.columns = [f"{side}_{name}" for name, side in wide.columns]
    return wide


def regulation_scores(games: pd.DataFrame, stints: pd.DataFrame) -> pd.DataFrame:
    """Each finished game's score after 48 minutes: the final score when it
    ended in regulation, otherwise summed from the first four periods' stints."""
    g = games[games["completed"]].set_index("game_id")
    reg = stints[stints["period"] <= 4].groupby("game_id")[["home_pts", "away_pts"]].sum().reindex(g.index)
    in_reg = g["periods"].fillna(4) <= 4
    home = g["home_score"].where(in_reg, reg["home_pts"])
    away = g["away_score"].where(in_reg, reg["away_pts"])
    # An overtime game must have been tied after regulation.
    bad = ~in_reg & (home != away)
    return pd.DataFrame({"home_reg": home.mask(bad), "away_reg": away.mask(bad)})


class FeatureBuilder:
    def __init__(self, summaries: dict, hp: Hyperparams, lines: pd.DataFrame | None = None):
        self.hp = hp
        self.games = summaries["games"]
        games = self.games
        self.team_games = summaries["teams"]
        self.engines = {
            name: RatingsEngine(prepare_rows(self.team_games, games, target), target,
                                hp.pace_half_life_days if name == "pace" else hp.half_life_days)
            for name, target in targets(hp).items()
        }
        self.players = PlayerRatings(summaries["stints"], games, hp, summaries["players"])
        self.names = summaries["names"].drop_duplicates("player_id").set_index("player_id")["name"]
        self.minutes = minutes_history(summaries["players"], games, hp.minutes_half_life_games)
        elo, self.elo_ratings = run_elo(games)
        self.elo = elo.set_index("game_id")
        self.context = schedule_context(games)
        self._game_day = {gid: float(d) for season, grp in games.groupby("season")
                          for gid, d in zip(grp["game_id"], season_day(grp["date"], int(season)))}
        self.lines = lines
        tg = self.team_games
        self.outcomes = tg[tg["home"] == 1].drop_duplicates("game_id").set_index("game_id")[["poss", "minutes"]]
        self.outcomes = self.outcomes.join(regulation_scores(games, summaries["stints"]))
        self._env_dix = day_index(tg["date"])
        self._env_ppp = (100.0 * tg["pts"] / tg["poss"]).to_numpy(float)
        self._env_pace = (tg["poss"] / tg["minutes"] * REG_MINUTES).to_numpy(float)
        self._compositions()

    # ---- league level --------------------------------------------------
    def environment(self, dix: int) -> tuple[float, float]:
        """Recency-weighted league points per 100 possessions and pace before day ``dix``."""
        mask = self._env_dix < dix
        if not mask.any():
            return 108.0, 96.0
        decay = 0.5 ** ((dix - self._env_dix[mask]) / ENV_HALF_LIFE_DAYS)
        # The prior is the long-run average of the most recent games, so it
        # only steadies the first days after a long break.
        recent = np.argsort(self._env_dix[mask])[-200:]
        prior_ppp = float(self._env_ppp[mask][recent].mean())
        prior_pace = float(self._env_pace[mask][recent].mean())
        ppp = (decay @ self._env_ppp[mask] + ENV_PRIOR_GAMES * prior_ppp) / (decay.sum() + ENV_PRIOR_GAMES)
        pace = (decay @ self._env_pace[mask] + ENV_PRIOR_GAMES * prior_pace) / (decay.sum() + ENV_PRIOR_GAMES)
        return float(ppp), float(pace)

    # ---- who played ------------------------------------------------------
    def _compositions(self) -> None:
        """Each team-game's players with their share of the floor (five per
        game) and projected minutes, plus the team's possession weight."""
        m = self.minutes[self.minutes["status"] == "played"].copy()
        g = self.games.set_index("game_id")
        mins = self.team_games.set_index(["game_id", "team"])["minutes"]
        m["game_minutes"] = pd.Series(list(zip(m["game_id"], m["team"]))).map(mins).to_numpy()
        m["game_minutes"] = m["game_minutes"].fillna(REG_MINUTES)
        m["share"] = m["minutes"] / m["game_minutes"]
        m["season"] = m["game_id"].map(g["season"])
        m["date"] = m["game_id"].map(g["date"])
        self.comp = m
        # Plain arrays per team-game: player ids, projected minutes, floor shares.
        self.by_game = {k: (v["player_id"].to_numpy(), v["proj_minutes"].to_numpy(float), v["share"].to_numpy(float))
                        for k, v in m.groupby(["game_id", "team"])}
        # Each team's listed games in order, with the healthy players and their
        # expected minutes after the game, for projecting from the previous game.
        listed = self.minutes.sort_values(["team", "start", "game_id"])
        self.listed = {}
        for team, grp in listed.groupby("team"):
            starts = grp.drop_duplicates("game_id")[["start", "game_id"]]
            players = {gid: (v["player_id"].to_numpy(), v["exp_after"].to_numpy(float))
                       for gid, v in grp.groupby("game_id")}
            naive = pd.to_datetime(starts["start"], utc=True).dt.tz_convert(None).to_numpy("datetime64[ns]")
            self.listed[team] = (naive, starts["game_id"].to_numpy(), players)
        poss = self.team_games.set_index(["game_id", "team"])["clean_poss"]
        self.poss = poss[~poss.index.duplicated()]

    def _projected(self, game_id, team, start, mode: str):
        """Available players and projected minutes for one team in one game."""
        if mode == "actual":
            rows = self.by_game.get((game_id, team))
            if rows is None:
                return np.zeros(0, dtype=np.int64), np.zeros(0)
            return rows[0], rows[1]
        # The players listed healthy in the team's previous game, with their
        # expected minutes as of that game.
        if team not in self.listed:
            return np.zeros(0, dtype=np.int64), np.zeros(0)
        starts, gids, players = self.listed[team]
        k = int(np.searchsorted(starts, pd.Timestamp(start).tz_convert(None).to_datetime64(), side="left"))
        if k == 0:
            return np.zeros(0, dtype=np.int64), np.zeros(0)
        return players[gids[k - 1]]

    def latest_minutes(self, before, column: str = "exp_after") -> pd.Series:
        """Each player's running average after his last listed game before
        ``before``: expected minutes by default, or minutes when he plays."""
        m = self.minutes[self.minutes["start"] < before]
        return m.drop_duplicates("player_id", keep="last").set_index("player_id")[column]

    def strength(self, ids, minutes, ratings) -> tuple[float, float]:
        off, de, _ = ratings
        return lineup_strength(ids, rescale_minutes(minutes), off, de, self.players.newcomer)

    # ---- the walk-forward pass -----------------------------------------
    def _prior_exposure(self, season: int) -> dict[str, dict[int, float]]:
        """The players behind each team's preseason prior: last season's floor
        shares, recency weighted to its end, scaled to the prior's strength."""
        m = self.comp[self.comp["season"] == season - 1]
        out: dict[str, dict[int, float]] = defaultdict(dict)
        if m.empty:
            return out
        day = season_day(m["date"], season - 1)
        w = 0.5 ** ((day.max() + 1 - day) / self.hp.half_life_days)
        m = m.assign(w=w * m["share"])
        tot = m.groupby("team")["w"].sum()
        for (team, pid), v in m.groupby(["team", "player_id"])["w"].sum().items():
            out[team][pid] = 5.0 * v / tot[team] * self.hp.team_prior_poss
        return out

    def _mix(self, team: str, exposure: dict, weight: dict, ratings, day: float) -> tuple[float, float]:
        off, de, _ = ratings
        c = 2.0 ** (-day / self.hp.half_life_days)
        cur = exposure["cur"].get(team, {})
        pri = exposure["prior"].get(team, {})
        o_new, d_new = self.players.newcomer
        num_o = sum(v * off.get(p, o_new) for p, v in pri.items()) + c * sum(v * off.get(p, o_new) for p, v in cur.items())
        num_d = sum(v * de.get(p, d_new) for p, v in pri.items()) + c * sum(v * de.get(p, d_new) for p, v in cur.items())
        den = self.hp.team_prior_poss + c * weight.get(team, 0.0)
        return num_o / den, num_d / den

    def _add_games(self, day_games: pd.DataFrame, season: int, exposure: dict, weight: dict) -> None:
        for gid, home, away, done, date in day_games[["game_id", "home_team", "away_team", "completed",
                                                      "date"]].itertuples(index=False):
            if not done:
                continue
            scale = 2.0 ** (self._game_day[gid] / self.hp.half_life_days)
            for team in (home, away):
                rows = self.by_game.get((gid, team))
                poss = float(self.poss.get((gid, team), np.nan))
                if rows is None or not np.isfinite(poss):
                    continue
                w = poss * scale
                cur = exposure["cur"].setdefault(team, defaultdict(float))
                for pid, share in zip(rows[0].tolist(), rows[2].tolist()):
                    cur[pid] += w * share
                weight[team] = weight.get(team, 0.0) + w

    def _rows(self, games: pd.DataFrame, season: int, date, exposure: dict, weight: dict, mode: str,
              availability: pd.DataFrame | None = None, ratings_day: float | None = None) -> pd.DataFrame:
        day = float(season_day(pd.Series([date]), season)[0]) if ratings_day is None else ratings_day
        team_r = {name: engine.before(season, day) for name, engine in self.engines.items()}
        player_r = self.players.before(season, day)
        ppp, pace = self.environment(int(day_index([date])[0]))
        cols: dict[str, list] = defaultdict(list)
        for g in games.itertuples(index=False):
            for side in ("home", "away"):
                team = getattr(g, f"{side}_team")
                for name, r in team_r.items():
                    cols[f"off_{name}_{side}"].append(r.off.get(team, 0.0))
                    cols[f"def_{name}_{side}"].append(r.deff.get(team, 0.0))
                if availability is not None:
                    a = availability[(availability["game_id"] == g.game_id) & (availability["team"] == team)]
                    ids = a["player_id"].to_numpy()
                    mins = (a["proj_minutes"] * a["play_prob"]).to_numpy(float)
                else:
                    ids, mins = self._projected(g.game_id, team, g.start, mode)
                if len(ids):
                    p_off, p_def = self.strength(ids, mins, player_r)
                else:
                    p_off, p_def = np.nan, np.nan
                mix_off, mix_def = self._mix(team, exposure, weight, player_r, day)
                cols[f"p_off_{side}"].append(p_off)
                cols[f"p_def_{side}"].append(p_def)
                cols[f"mix_off_{side}"].append(mix_off)
                cols[f"mix_def_{side}"].append(mix_def)
        out = pd.concat([games[GAME_COLUMNS].reset_index(drop=True), pd.DataFrame(cols)], axis=1)
        for side in ("home", "away"):
            # A team with no player data falls back to no adjustment.
            out[f"p_off_{side}"] = out[f"p_off_{side}"].fillna(out[f"mix_off_{side}"])
            out[f"p_def_{side}"] = out[f"p_def_{side}"].fillna(out[f"mix_def_{side}"])
            out[f"adj_off_{side}"] = out[f"p_off_{side}"] - out[f"mix_off_{side}"]
            out[f"adj_def_{side}"] = out[f"p_def_{side}"] - out[f"mix_def_{side}"]
        out["league_eff"] = team_r["eff"].mu
        out["league_pace"] = team_r["pace"].mu
        out["env_ppp"] = ppp
        out["env_pace"] = pace
        return out

    def _finish(self, out: pd.DataFrame) -> pd.DataFrame:
        """Schedule context, Elo and outcomes, joined once per batch of rows."""
        out = out.join(self.context, on="game_id").join(self.elo, on="game_id").join(self.outcomes, on="game_id")
        for side in ("home", "away"):
            out[f"{side}_rest"] = out[f"{side}_rest"].fillna(MAX_REST)
            out[f"{side}_travel"] = out[f"{side}_travel"].fillna(0.0)
            out[f"{side}_tz_shift"] = out[f"{side}_tz_shift"].fillna(0.0)
        return out

    def _season_pass(self, season: int, mode: str, until=None):
        """Features for each completed game day of ``season`` before ``until``,
        and the exposure state at the end."""
        season_games = self.games[self.games["season"] == season]
        exposure = {"prior": self._prior_exposure(season), "cur": {}}
        weight: dict[str, float] = {}
        frames = []
        days = sorted(season_games["date"].unique())
        if until is not None:
            days = [d for d in days if d < until]
        self.players.prepare(season, season_day(pd.Series(days), season) if days else None)
        for date in days:
            day_games = season_games[season_games["date"] == date]
            frames.append(self._rows(day_games, season, date, exposure, weight, mode))
            self._add_games(day_games, season, exposure, weight)
        return frames, exposure, weight

    def walk_forward(self, seasons, availability: str = "actual", until=None) -> pd.DataFrame:
        """Features for every game in ``seasons``, each built from earlier days
        only. Dates on or after ``until`` are skipped."""
        frames = []
        for season in seasons:
            f, _, _ = self._season_pass(season, availability, until)
            frames += f
        out = self._finish(pd.concat(frames, ignore_index=True)) if frames else pd.DataFrame()
        return self._attach_lines(out)

    def current(self, games: pd.DataFrame, season: int, today, availability: pd.DataFrame | None = None,
                scenarios: dict[str, pd.DataFrame] | None = None):
        """Features for upcoming ``games`` from every game played before
        ``today``, with players from ``availability``. With ``scenarios``
        (name to availability) the same pass also returns features under each
        alternative, as a dict."""
        _, exposure, weight = self._season_pass(season, "actual", until=today)
        day = float(season_day(pd.Series([today]), season)[0])

        def rows(avail):
            if games.empty:
                return games.copy()
            return self._finish(self._rows(games, season, today, exposure, weight, "actual",
                                           availability=avail, ratings_day=day))
        main = rows(availability)
        if scenarios is None:
            return main
        return main, {name: rows(a) for name, a in scenarios.items()}

    def ratings_now(self, season: int, today) -> dict:
        """Team and player ratings as of ``today``."""
        day = float(season_day(pd.Series([today]), season)[0])
        return {"team": {name: engine.before(season, day) for name, engine in self.engines.items()},
                "players": self.players.before(season, day)}

    def _attach_lines(self, feats: pd.DataFrame) -> pd.DataFrame:
        from .lines import attach_lines
        if self.lines is None or feats.empty:
            return feats
        return attach_lines(feats, self.lines)
