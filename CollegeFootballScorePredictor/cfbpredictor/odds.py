"""Current betting lines for upcoming games.

Two sources, tried in order:

1. CollegeFootballData (CFBD) lines, the median across its books, when a
   ``CFBD_API_KEY`` environment variable is set (free keys allow 1,000 calls a
   month; each update uses one or two).
2. ESPN's public scoreboard, which needs no key and lists the line ESPN
   shows for every FBS game.

Game ids are shared by cfbfastR, CFBD and ESPN, so lines join on them
directly. Any failure leaves the affected games without a line, and the
prediction falls back to the model alone.

Prices (the American odds on each side of the spread and total, and the
moneylines) are kept for the betting-edge columns. CFBD's consensus spread
and total are medians across books, so each side's price is the median price
of the books quoting exactly that consensus line (none at that line leaves it
missing); its moneylines are the median across books. Medians of prices are
taken on break-even probability, since American odds jump from -100 to +100.
ESPN gives one book's line and prices.
"""

from __future__ import annotations

import logging
import os
import re

import numpy as np
import pandas as pd
import requests

from .edges import median_price, valid_price

log = logging.getLogger(__name__)

ESPN_SCOREBOARD = "https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard"
CFBD_LINES = "https://api.collegefootballdata.com/lines"
FBS_GROUP = "80"
PRICE_COLUMNS = ["home_spread_price", "away_spread_price", "over_price", "under_price"]
ODDS_COLUMNS = ["game_id", "spread_line", "total_line", "home_moneyline", "away_moneyline", *PRICE_COLUMNS,
                "line_source"]
NUMERIC = ["spread_line", "total_line", "home_moneyline", "away_moneyline", *PRICE_COLUMNS]


def _frame(rows: list[dict]) -> pd.DataFrame:
    """Odds rows with numeric columns typed as numbers even when there are none."""
    out = pd.DataFrame(rows, columns=ODDS_COLUMNS)
    out["game_id"] = out["game_id"].astype("int64")
    out[NUMERIC] = out[NUMERIC].astype(float)
    return out


def _num(x) -> float:
    try:
        v = float(x)
    except (TypeError, ValueError):
        return np.nan
    return v if np.isfinite(v) else np.nan


def _espn_home_margin(odds: dict, home_abbr: str, away_abbr: str) -> float:
    """Expected home margin from one ESPN odds entry (positive = home favored)."""
    details = str(odds.get("details") or "").strip()
    if details.upper() in ("EVEN", "PK", "PICK", "PICK'EM"):
        return 0.0
    size = abs(_num(odds.get("spread")))
    match = re.match(r"^(\S+)\s+([+-]?\d+(?:\.\d+)?)$", details)
    if np.isnan(size) and match:
        size = abs(float(match.group(2)))
    if np.isnan(size):
        return np.nan
    home_fav = (odds.get("homeTeamOdds") or {}).get("favorite")
    away_fav = (odds.get("awayTeamOdds") or {}).get("favorite")
    if home_fav is True:
        return size
    if away_fav is True:
        return -size
    if match:
        team = match.group(1)
        if team == home_abbr:
            return size
        if team == away_abbr:
            return -size
    # ESPN's spread number is the home team's line: negative when it is favored.
    raw = _num(odds.get("spread"))
    return -raw if not np.isnan(raw) else np.nan


def _american(x) -> float:
    """An American price from ESPN's numbers or strings ("-110", "+150", "EVEN"); NaN if unusable."""
    if isinstance(x, str) and x.strip().upper() in ("EVEN", "EV"):
        return 100.0
    v = _num(str(x).strip().replace("+", "") if isinstance(x, str) else x)
    return v if valid_price(v) else np.nan


def _points(x) -> float:
    """A line from ESPN's numbers or strings ("-10.5", "o60.5", "u60.5", "PK")."""
    if isinstance(x, str):
        x = x.strip()
        if x.upper() in ("PK", "EVEN", "PICK", "PICK'EM"):
            return 0.0
        x = x.lstrip("oOuU").replace("+", "")
    return _num(x)


def _quote(block) -> list[tuple[float, float]]:
    """(line, price) for the close then current quote of one side in ESPN's newer odds format."""
    out = []
    for key in ("close", "current"):
        q = (block or {}).get(key) or {}
        if q:
            out.append((_points(q.get("line")), _american(q.get("odds"))))
    return out


def _side_price(quotes: list[tuple[float, float]], line: float, old) -> float:
    """The price quoted at ``line``: close, then current, then the older flat field."""
    for q_line, price in quotes:
        if not np.isnan(price) and (np.isnan(q_line) or np.isnan(line) or abs(q_line - line) < 0.01):
            return price
    return _american(old)


def espn_prices(odds: dict, spread_line: float, total_line: float) -> dict:
    """Spread, total and moneyline prices from one ESPN odds entry, matched to the parsed lines.

    The newer format nests ``pointSpread.{home,away}``, ``total.{over,under}``
    and ``moneyline.{home,away}``, each with ``open``/``close`` quotes of
    ``line`` and ``odds``; older payloads carry ``homeTeamOdds.spreadOdds``,
    ``overOdds``, ``underOdds`` and ``homeTeamOdds.moneyLine``. A spread or
    total quote is used only when its line is the one being predicted.
    """
    home_old, away_old = odds.get("homeTeamOdds") or {}, odds.get("awayTeamOdds") or {}
    spread, total, money = odds.get("pointSpread") or {}, odds.get("total") or {}, odds.get("moneyline") or {}
    # pointSpread lines are each team's own line: the home team's is minus the home margin.
    home_line = -spread_line if not np.isnan(spread_line) else np.nan
    away_line = spread_line
    return {
        "home_spread_price": _side_price(_quote(spread.get("home")), home_line, home_old.get("spreadOdds")),
        "away_spread_price": _side_price(_quote(spread.get("away")), away_line, away_old.get("spreadOdds")),
        "over_price": _side_price(_quote(total.get("over")), total_line, odds.get("overOdds")),
        "under_price": _side_price(_quote(total.get("under")), total_line, odds.get("underOdds")),
        "home_moneyline": _side_price(_quote(money.get("home")), np.nan, home_old.get("moneyLine")),
        "away_moneyline": _side_price(_quote(money.get("away")), np.nan, away_old.get("moneyLine")),
    }


def _espn_lines_new(odds: dict) -> tuple[float, float]:
    """Home margin and total from the newer ``pointSpread``/``total`` blocks (close, then current)."""
    margin = total = np.nan
    for line, _ in _quote((odds.get("pointSpread") or {}).get("home")):
        if not np.isnan(line):
            margin = -line
            break
    for line, _ in _quote((odds.get("total") or {}).get("over")):
        if not np.isnan(line):
            total = line
            break
    return margin, total


def parse_espn(payload: dict) -> pd.DataFrame:
    rows = []
    for event in payload.get("events") or []:
        comps = event.get("competitions") or [{}]
        comp = comps[0]
        teams = {c.get("homeAway"): (c.get("team") or {}) for c in comp.get("competitors") or []}
        odds_list = comp.get("odds") or []
        if not odds_list or "home" not in teams or "away" not in teams:
            continue
        odds = odds_list[0]
        home, away = teams["home"], teams["away"]
        spread = _espn_home_margin(odds, home.get("abbreviation", ""), away.get("abbreviation", ""))
        total = _num(odds.get("overUnder"))
        new_spread, new_total = _espn_lines_new(odds)
        spread = new_spread if np.isnan(spread) else spread
        total = new_total if np.isnan(total) else total
        rows.append({
            "game_id": int(event.get("id") or comp.get("id")),
            "spread_line": spread,
            "total_line": total,
            **espn_prices(odds, spread, total),
            "line_source": "ESPN" + (f" ({odds['provider']['name']})" if (odds.get("provider") or {}).get("name") else ""),
        })
    return _frame(rows)


# Price fields a CFBD line object may carry (the documented schema has none
# for spreads and totals; read them if they appear).
CFBD_PRICE_KEYS = {
    "home_spread_price": ("homeSpreadOdds", "homeSpreadPrice", "spreadHomeOdds"),
    "away_spread_price": ("awaySpreadOdds", "awaySpreadPrice", "spreadAwayOdds"),
    "over_price": ("overOdds", "overPrice", "overUnderOverOdds"),
    "under_price": ("underOdds", "underPrice", "overUnderUnderOdds"),
}


def _cfbd_price(book: dict, col: str) -> float:
    for key in CFBD_PRICE_KEYS[col]:
        if valid_price(_num(book.get(key))):
            return _num(book.get(key))
    return np.nan


def parse_cfbd(payload: list) -> pd.DataFrame:
    rows = []
    for game in payload or []:
        books = game.get("lines") or []
        spread = [-_num(b.get("spread")) for b in books]      # CFBD spreads are the home line
        total = [_num(b.get("overUnder")) for b in books]

        def median(values):
            v = [x for x in values if not np.isnan(x)]
            return float(np.median(v)) if v else np.nan

        def at_line(col, lines, line):
            # Prices only from the books quoting the consensus line itself.
            return median_price([_cfbd_price(b, col) for b, x in zip(books, lines) if abs(x - line) < 0.01])
        spread_line, total_line = median(spread), median(total)
        rows.append({"game_id": int(game["id"]), "spread_line": spread_line, "total_line": total_line,
                     "home_moneyline": median_price([_num(b.get("homeMoneyline")) for b in books]),
                     "away_moneyline": median_price([_num(b.get("awayMoneyline")) for b in books]),
                     "home_spread_price": at_line("home_spread_price", spread, spread_line),
                     "away_spread_price": at_line("away_spread_price", spread, spread_line),
                     "over_price": at_line("over_price", total, total_line),
                     "under_price": at_line("under_price", total, total_line),
                     "line_source": f"CFBD ({len(books)} books)"})
    return _frame(rows)


def _espn_lines(games: pd.DataFrame, session: requests.Session) -> pd.DataFrame:
    """One scoreboard request per game day (ESPN rejects date ranges for college)."""
    days = sorted(set(games["kickoff"].dropna().dt.tz_convert("America/New_York").dt.strftime("%Y%m%d")))
    frames, errors = [], []
    for day in days:
        try:
            resp = session.get(ESPN_SCOREBOARD, params={"dates": day, "groups": FBS_GROUP, "limit": 300},
                               timeout=30)
            resp.raise_for_status()
            day_lines = parse_espn(resp.json())
            if len(day_lines):
                frames.append(day_lines)
        except requests.ConnectionError:
            raise
        except (requests.RequestException, ValueError) as exc:
            errors.append(f"{day}: {exc}")
    if errors:
        log.warning("ESPN scoreboard failed for %d of %d days: %s", len(errors), len(days), "; ".join(errors[:3]))
    if not frames:
        return _frame([])
    return pd.concat(frames, ignore_index=True).drop_duplicates("game_id")


def _cfbd_lines(games: pd.DataFrame, session: requests.Session, key: str) -> pd.DataFrame:
    frames = []
    for (season, kind), _ in games.groupby(["season", "season_type"]):
        resp = session.get(CFBD_LINES, params={"year": int(season), "seasonType": kind},
                           headers={"Authorization": f"Bearer {key}"}, timeout=30)
        resp.raise_for_status()
        frames.append(parse_cfbd(resp.json()))
    frames = [f for f in frames if len(f)]
    return pd.concat(frames, ignore_index=True) if frames else _frame([])


def live_lines(games: pd.DataFrame, session: requests.Session | None = None) -> pd.DataFrame:
    """Current lines for ``games`` (upcoming), best source first; empty on failure."""
    session = session or requests.Session()
    found = []
    key = os.environ.get("CFBD_API_KEY", "").strip()
    sources = ([("CFBD", lambda: _cfbd_lines(games, session, key))] if key else []) + \
        [("ESPN", lambda: _espn_lines(games, session))]
    for name, get in sources:
        try:
            lines = get()
        except (requests.RequestException, ValueError, KeyError, TypeError) as exc:
            log.warning("No lines from %s: %s", name, exc)
            continue
        lines = lines[lines["game_id"].isin(set(games["game_id"]))]
        lines = lines[lines["spread_line"].notna() | lines["total_line"].notna()]
        log.info("%s lines for %d of %d games", name, len(lines), len(games))
        found.append(lines)
    found = [f for f in found if len(f)]
    if not found:
        return _frame([])
    return pd.concat(found, ignore_index=True).drop_duplicates("game_id", keep="first").reset_index(drop=True)
