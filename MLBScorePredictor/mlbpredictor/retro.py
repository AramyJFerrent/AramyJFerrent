"""Parse Retrosheet event files into per-game summaries.

Retrosheet's event files record every play of every game: the starting
lineups, each substitution and each plate appearance with its pitch sequence,
outcome and runner advances. One pass over a game tracks the bases, the outs
and the pitcher on the mound, and produces:

- a game row: teams, park, weather, starting pitchers, line score and score;
- one row per batter: plate appearances by outcome and his lineup slot;
- one row per pitcher: batters faced by outcome, outs, pitches and runs;
- base-out transition counts (state at the start of a plate appearance, its
  outcome, the state at the start of the next one and the runs in between),
  which the inning simulator is built from;
- plate-appearance outcomes by batter and pitcher handedness, for the
  platoon adjustment.

The information used here was obtained free of charge from and is
copyrighted by Retrosheet. Interested parties may contact Retrosheet at
www.retrosheet.org.
"""

from __future__ import annotations

import csv
import datetime as dt
import io
import logging
import re
from collections import Counter
from dataclasses import dataclass, field
from zoneinfo import ZoneInfo

from .config import RETRO_TEAMS, TEAM_TZ

log = logging.getLogger(__name__)

# Plate-appearance outcomes. ``out`` is every other way a plate appearance
# ends: balls in play turned into outs, errors, fielder's choices, sacrifices
# and catcher's interference.
EVENTS = ("k", "bb", "hbp", "s", "d", "t", "hr", "out")
PITCH_CHARS = frozenset("BCFHIKLMOPQRSTUVXY")
DEST = {"1": 1, "2": 2, "3": 3, "H": 4}
STEAL_FROM = {"2": 1, "3": 2, "H": 3}
END = 24          # transition end state: the half-inning is over
# Postseason event files by series, with the MLB Stats API game type.
POSTSEASON_FILES = {"WS": "W", "ALCS": "L", "NLCS": "L", "ALD1": "D", "ALD2": "D", "NLD1": "D",
                    "NLD2": "D", "ALWC": "F", "NLWC": "F", "ALW1": "F", "ALW2": "F", "ALW3": "F",
                    "ALW4": "F", "NLW1": "F", "NLW2": "F", "NLW3": "F", "NLW4": "F"}
WIND_OUT = {"tolf", "tocf", "torf"}
WIND_IN = {"fromlf", "fromcf", "fromrf"}

_ADVANCE = re.compile(r"^([B123])([-X])([123H])(.*)$")
_ERROR = re.compile(r"E\d")
_RUNNER_OUT = re.compile(r"\(([B123])\)")
_MARKS = str.maketrans("", "", "!?#")
_GROUP = re.compile(r"\(([^)]*)\)")


def state_code(bases, outs: int) -> int:
    """Base-out state 0-23: bases as bits (first 1, second 2, third 4) plus 8 per out."""
    return sum(1 << (b - 1) for b in bases) + 8 * outs


def _split_outside(text: str, sep: str) -> list[str]:
    parts, depth, cur = [], 0, []
    for ch in text:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(depth - 1, 0)
        if ch == sep and depth == 0:
            parts.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
    parts.append("".join(cur))
    return parts


@dataclass
class Play:
    """One event record. Destinations are bases 1-4 (4 = scored) or -1 (out);
    origin 0 is the batter."""

    pa: str | None = None              # outcome category when the play ends the plate appearance
    ibb: bool = False
    moves: dict = field(default_factory=dict)      # explicit runner advances
    implicit: dict = field(default_factory=dict)   # implied by the play itself
    all_score: bool = False                        # home run: runners not mentioned score


def _safe(rest: str) -> bool:
    """Whether a putout notation was negated by an error: some parenthetical
    has an error and none is a clean fielding sequence. ``1X3(4E6)`` is
    safe; ``1XH(82)(E3/TH)`` and ``1XH(E1/TH)(525)`` are outs, the error
    having only let the runner try for the extra base."""
    groups = _GROUP.findall(rest)
    return any(_ERROR.search(g) for g in groups) and not any(g.isdigit() for g in groups)


def _runner_event(code: str, p: Play) -> None:
    """Stolen bases, caught stealing and pickoffs (other runner events carry
    their advances explicitly)."""
    for part in code.split(";"):
        if part.startswith("SB") and len(part) > 2 and part[2] in STEAL_FROM:
            p.implicit[STEAL_FROM[part[2]]] = DEST[part[2]]
        elif part.startswith("POCS") and len(part) > 4 and part[4] in STEAL_FROM:
            p.implicit[STEAL_FROM[part[4]]] = DEST[part[4]] if _safe(part) else -1
        elif part.startswith("CS") and len(part) > 2 and part[2] in STEAL_FROM:
            p.implicit[STEAL_FROM[part[2]]] = DEST[part[2]] if _safe(part) else -1
        elif part.startswith("PO") and len(part) > 2 and part[2] in "123":
            if not _safe(part):
                p.implicit[int(part[2])] = -1


def _primary(c: str, p: Play) -> None:
    if not c or c.startswith("NP"):
        return
    if c.startswith("HP"):
        p.pa, p.implicit[0] = "hbp", 1
    elif c.startswith("H"):
        p.pa, p.implicit[0], p.all_score = "hr", 4, True
    elif c.startswith("K"):
        p.pa, p.implicit[0] = "k", -1
    elif c.startswith("I"):
        p.pa, p.ibb, p.implicit[0] = "bb", True, 1
    elif c.startswith("W") and not c.startswith("WP"):
        p.pa, p.implicit[0] = "bb", 1
    elif c.startswith(("SB", "CS", "PO", "WP", "PB", "BK", "DI", "OA", "FLE", "OBS")):
        _runner_event(c, p)
    elif c.startswith("S"):
        p.pa, p.implicit[0] = "s", 1
    elif c.startswith("D"):
        p.pa, p.implicit[0] = "d", 2
    elif c.startswith("T"):
        p.pa, p.implicit[0] = "t", 3
    elif c.startswith(("E", "FC", "C")):
        p.pa, p.implicit[0] = "out", 1
    elif c[0].isdigit():
        p.pa = "out"
        for m in _RUNNER_OUT.finditer(c):
            p.implicit[0 if m.group(1) == "B" else int(m.group(1))] = -1
        # The batter is out when named or when the play ends on a fielder
        # (``63``, ``64(1)3``); a force play on a runner (``64(1)``) or an
        # error on the throw (``2E3``) leaves him on first.
        if 0 not in p.implicit:
            p.implicit[0] = -1 if c[-1].isdigit() and not _ERROR.search(_RUNNER_OUT.sub("", c)) else 1
    else:
        log.debug("Unrecognized play %r", c)


def parse_play(event: str) -> Play:
    # ``!`` marks an exceptional play, ``?`` and ``#`` uncertain ones.
    main, _, adv = event.translate(_MARKS).partition(".")
    p = Play()
    basic = _split_outside(main, "/")[0]
    first, *extras = basic.split("+")
    _primary(first, p)
    for extra in extras:
        _runner_event(extra, p)
    for a in adv.split(";") if adv else []:
        m = _ADVANCE.match(a.strip())
        if not m:
            continue
        origin = 0 if m.group(1) == "B" else int(m.group(1))
        out = m.group(2) == "X" and not _safe(m.group(4))
        p.moves[origin] = -1 if out else DEST[m.group(3)]
    return p


def advance(bases: dict, play: Play, pitcher) -> tuple[dict, int, list]:
    """Apply a play to ``bases`` (base -> responsible pitcher).

    Returns the new bases, the outs made and the responsible pitcher of each
    run scored. A runner the play does not mention stays put unless another
    runner or the batter needs his base, in which case he is forced ahead.
    """
    moving = []   # (destination, explicit, responsible pitcher)
    for origin in (3, 2, 1):
        if origin not in bases:
            continue
        if origin in play.moves:
            moving.append((play.moves[origin], True, bases[origin]))
        elif origin in play.implicit:
            moving.append((play.implicit[origin], True, bases[origin]))
        elif play.all_score:
            moving.append((4, True, bases[origin]))
        else:
            moving.append((origin, False, bases[origin]))
    if play.pa is not None or 0 in play.moves:
        dest = play.moves.get(0, play.implicit.get(0, 1))
        moving.append((dest, True, pitcher))
    outs = sum(1 for d, _, _ in moving if d == -1)
    runners = [[d, e, rp] for d, e, rp in moving if d != -1]
    for base in (1, 2, 3):
        here = [r for r in runners if r[0] == base]
        while len(here) > 1:
            stay = next((r for r in here if not r[1]), here[-1])
            stay[0] += 1
            here.remove(stay)
    scored = [rp for d, _, rp in runners if d >= 4]
    return {d: rp for d, _, rp in runners if d < 4}, outs, scored


def _new_counts(keys) -> dict:
    return {k: 0 for k in keys}


BAT_KEYS = ("pa",) + EVENTS + ("ibb",)
PITCH_KEYS = ("outs", "bf", "pitches") + EVENTS + ("ibb", "r", "er")


class _Game:
    def __init__(self, gid: str, hands: dict, game_type: str):
        self.gid = gid
        self.hands = hands
        self.game_type = game_type
        self.info: dict[str, str] = {}
        self.pitcher = {0: None, 1: None}
        self.starter = {0: None, 1: None}
        self.batting: dict[tuple, dict] = {}
        self.pitching: dict[tuple, dict] = {}
        self.er: dict[str, int] = {}
        self.lines: dict[int, Counter] = {0: Counter(), 1: Counter()}
        self.batted: dict[int, set] = {0: set(), 1: set()}
        self.half = None
        self.bases: dict = {}
        self.outs = 0
        self.batter = None
        self.counted = 0
        self.pa_start = None          # (state, runs) when the current plate appearance began
        self.pending = None           # (state, event, runs at its start) awaiting its end state
        self.ghost = None
        self.badj: dict = {}
        self.padj: dict = {}
        self.transitions: Counter = Counter()
        self.platoon: Counter = Counter()
        self.bad = False

    # ---- records ---------------------------------------------------------
    def lineup(self, kind: str, row: list[str]) -> None:
        pid, team, order, pos = row[1], int(row[3]), int(row[4]), int(row[5])
        if kind == "start" and order > 0:
            self.batting.setdefault((team, pid), {"slot": order, "pos": pos, **_new_counts(BAT_KEYS)})
        if pos == 1:
            if self.starter[team] is None:
                self.starter[team] = pid
            self.pitcher[team] = pid
            if (team, pid) not in self.pitching:
                seq = sum(1 for t, _ in self.pitching if t == team)
                self.pitching[(team, pid)] = {"starter": int(seq == 0), "seq": seq, **_new_counts(PITCH_KEYS)}

    def _state(self) -> int:
        return state_code(self.bases, min(self.outs, 2))

    def _runs(self) -> int:
        return sum(self.lines[self.half[1]].values()) if self.half else 0

    def _close(self, end_state: int) -> None:
        if self.pending is not None:
            state, event, runs = self.pending
            self.transitions[(state, event, end_state, self._runs() - runs)] += 1
            self.pending = None

    def _end_half(self) -> None:
        """Close the half-inning; incomplete ones (walk-offs, shortened games) record nothing."""
        if self.half is None:
            return
        if self.outs >= 3:
            self._close(END)
            if self.pa_start is not None:
                # The third out came on the bases before this plate appearance ended.
                self.transitions[(self.pa_start[0], "none", END, self._runs() - self.pa_start[1])] += 1
        self.pending = None
        self.pa_start = None

    def play(self, row: list[str]) -> None:
        inning, team, batter, pitches, event = int(row[1]), int(row[2]), row[3], row[5], row[6]
        if (inning, team) != self.half:
            self._end_half()
            self.half = (inning, team)
            self.bases, self.outs, self.batter = {}, 0, None
            self.batted[team].add(inning)
        defense = 1 - team
        pitcher = self.pitcher[defense]
        if self.ghost is not None:
            self.bases[self.ghost] = pitcher
            self.ghost = None
        if batter != self.batter:
            self.batter, self.counted = batter, 0
            self._close(self._state())
            self.pa_start = (self._state(), self._runs())
        n = sum(ch in PITCH_CHARS for ch in pitches)
        if pitcher is not None and (defense, pitcher) in self.pitching:
            self.pitching[(defense, pitcher)]["pitches"] += max(n - self.counted, 0)
        self.counted = max(n, self.counted)

        p = parse_play(event)
        self.bases, outs, scored = advance(self.bases, p, pitcher)
        for rp in scored:
            if (defense, rp) in self.pitching:
                self.pitching[(defense, rp)]["r"] += 1
        self.lines[team][inning] += len(scored)
        pstats = self.pitching.get((defense, pitcher))
        if pstats is not None:
            pstats["outs"] += outs
        if p.pa is not None:
            bstats = self.batting.setdefault((team, batter), {"slot": 0, "pos": 0, **_new_counts(BAT_KEYS)})
            for stats in (bstats, pstats):
                if stats is None:
                    continue
                stats["bf" if stats is pstats else "pa"] += 1
                stats[p.pa] += 1
                stats["ibb"] += int(p.ibb)
            bats = self.badj.pop(batter, None) or self.hands.get(batter, ("?", "?"))[0]
            throws = self.padj.get(pitcher) or self.hands.get(pitcher, ("?", "?"))[1]
            self.platoon[(bats, throws, p.pa)] += 1
            if self.pa_start is not None:
                self.pending = (self.pa_start[0], p.pa, self.pa_start[1])
            self.pa_start = None
            self.batter = None
        self.outs += outs

    # ---- output ----------------------------------------------------------
    def finish(self, season: int) -> dict:
        self._end_half()
        info = self.info
        home, away = RETRO_TEAMS.get(info.get("hometeam")), RETRO_TEAMS.get(info.get("visteam"))
        date = dt.date.fromisoformat(info["date"].replace("/", "-"))
        last = max(max(self.lines[0], default=0), max(self.lines[1], default=0), max(self.batted[0], default=0))
        line = {side: " ".join(str(self.lines[t][i]) if i in self.batted[t] else "x" for i in range(1, last + 1))
                for side, t in (("away", 0), ("home", 1))}
        temp = _int(info.get("temp"))
        wind = info.get("winddir", "unknown")
        game = {
            "game_id": self.gid, "season": season, "game_type": self.game_type, "date": date.isoformat(),
            "start": _start_utc(date, info.get("starttime"), home), "game_number": _int(info.get("number")) or 0,
            "home_team": home, "away_team": away,
            "home_score": sum(self.lines[1].values()), "away_score": sum(self.lines[0].values()),
            "innings": last, "sched_innings": _int(info.get("innings")) or 9,
            "tiebreaker": int((_int(info.get("tiebreaker")) or 0) == 2),
            "park_id": info.get("site"), "daynight": info.get("daynight"), "dome": int(info.get("sky") == "dome"),
            "temp": temp if temp else None,
            "wind": "out" if wind in WIND_OUT else "in" if wind in WIND_IN else "cross" if wind in ("ltor", "rtol")
            else "none" if wind == "none" else None,
            "wind_speed": _int(info.get("windspeed")) if (_int(info.get("windspeed")) or -1) >= 0 else None,
            "home_starter": self.starter[1], "away_starter": self.starter[0],
            "home_line": line["home"], "away_line": line["away"],
            "htbf": int(info.get("htbf", "false") == "true"),
        }
        batting = []
        for (team, pid), s in self.batting.items():
            batting.append({"game_id": self.gid, "team": home if team else away, "player_id": pid, **s})
        pitching = []
        for (team, pid), s in self.pitching.items():
            s = dict(s)
            s["er"] = self.er.get(pid, 0)
            pitching.append({"game_id": self.gid, "team": home if team else away, "player_id": pid, **s})
        return {"game": game, "batting": batting, "pitching": pitching}


def _int(x) -> int | None:
    try:
        return int(x)
    except (TypeError, ValueError):
        return None


def _start_utc(date: dt.date, local: str | None, home: str | None) -> str | None:
    """Retrosheet's local start time (``7:05PM``) as UTC, in the home team's time zone."""
    m = re.match(r"^\s*(\d{1,2}):(\d{2})\s*([AP]M)?", local or "")
    if not m:
        return None
    hour = int(m.group(1)) % 12 + (12 if (m.group(3) or "PM") == "PM" else 0)
    t = dt.datetime(date.year, date.month, date.day, hour, int(m.group(2)),
                    tzinfo=ZoneInfo(TEAM_TZ.get(home, "America/New_York")))
    return t.astimezone(dt.timezone.utc).isoformat()


def parse_events(text: str, season: int, hands: dict, game_type: str = "R") -> tuple[list, Counter, Counter]:
    """Every game in one event file: summaries plus transition and platoon counts."""
    games, transitions, platoon = [], Counter(), Counter()
    game = None

    def done(g):
        if g is None:
            return
        out = g.finish(season)
        if out["game"]["home_team"] and out["game"]["away_team"]:
            games.append(out)
            transitions.update(g.transitions)
            platoon.update(g.platoon)

    for row in csv.reader(io.StringIO(text)):
        if not row:
            continue
        kind = row[0]
        if kind == "id":
            done(game)
            game = _Game(row[1], hands, game_type)
        elif game is None:
            continue
        elif kind == "info" and len(row) >= 2:
            game.info[row[1]] = row[2] if len(row) > 2 else ""
        elif kind in ("start", "sub") and len(row) >= 6:
            game.lineup(kind, row)
        elif kind == "play" and len(row) >= 7:
            game.play(row)
        elif kind == "data" and len(row) >= 4 and row[1] == "er":
            game.er[row[2]] = int(row[3])
        elif kind == "radj" and len(row) >= 3 and row[2] in "123":
            game.ghost = int(row[2])
        elif kind == "badj" and len(row) >= 3:
            game.badj[row[1]] = row[2]
        elif kind == "padj" and len(row) >= 3:
            game.padj[row[1]] = row[2]
    done(game)
    return games, transitions, platoon


def parse_roster(text: str) -> dict[str, tuple[str, str, str]]:
    """Retrosheet roster file: player id -> (bats, throws, full name)."""
    out = {}
    for row in csv.reader(io.StringIO(text)):
        if len(row) >= 5:
            out[row[0]] = (row[3], row[4], f"{row[2]} {row[1]}".strip())
    return out


def parse_teams(text: str) -> dict[str, str]:
    """TEAM file: Retrosheet team code -> league (A or N), All-Star teams dropped."""
    out = {}
    for row in csv.reader(io.StringIO(text)):
        if len(row) >= 2 and row[0] in RETRO_TEAMS:
            out[row[0]] = row[1]
    return out
