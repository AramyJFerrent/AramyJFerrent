"""Betting lines for past games: consensus closing and opening numbers.

Two sources, both from cfbfastR:

- The multi-book odds file (2006-2025, several books per game). The consensus
  is the median across books, which is what the techniques report benchmarks
  against. Until 2020 the books name teams by their own abbreviations, which
  are resolved to schools by finding the one team common to every game an
  abbreviation appears in.
- The single line attached to each game's play-by-play (one provider), used
  for games the odds file lacks, which includes the season in progress.

Lines are stored as the expected home margin (positive when the home team is
favored) and the expected total, like the model's own predictions.

Prices for the betting-edge backtest come from the same file: each side's
spread and total price is the median price of the books quoting exactly the
consensus (median) line, and each moneyline is the median across books.
Medians of prices are taken on break-even probability (American odds jump
from -100 to +100). The file has spread and total prices through 2019 and
moneylines in most seasons; the play-by-play line has no prices.
"""

from __future__ import annotations

import logging

import numpy as np
import pandas as pd

from .config import CACHE_DIR, LINES_PATH, LINES_URL
from .data import fetch, summary_paths
from .edges import median_price

log = logging.getLogger(__name__)

# Projection sites listed alongside the books; they are models, not markets.
NOT_BOOKS = {"teamrankings", "numberfire"}
PRICE_COLUMNS = ["home_spread_price", "away_spread_price", "over_price", "under_price"]
LINE_COLUMNS = ["game_id", "season", "spread_line", "total_line", "home_moneyline", "away_moneyline",
                "spread_open", "total_open", "books", *PRICE_COLUMNS]


def _resolve_sides(odds: pd.DataFrame) -> pd.Series:
    """'home', 'away' or NaN for each spread and moneyline row."""
    desc = odds["game_desc"].str.split("@", n=1, expand=True)
    away, home = desc[0].str.strip(), desc[1].str.strip()
    abbr = odds["abbr"].astype(str).str.strip()
    side = pd.Series(np.where(abbr == home, "home", np.where(abbr == away, "away", None)),
                     index=odds.index, dtype=object)
    unresolved = side.isna()
    if unresolved.any():
        # Each abbreviation names the one team present in all of its games.
        rows = pd.DataFrame({"season": odds["season"], "abbr": abbr, "away": away, "home": home})[unresolved]
        names: dict[tuple, str] = {}
        for (season, code), grp in rows.groupby(["season", "abbr"]):
            common = None
            for a, h in zip(grp["away"], grp["home"]):
                common = {a, h} if common is None else common & {a, h}
                if not common:
                    break
            if common and len(common) == 1:
                names[(season, code)] = next(iter(common))
        team = pd.Series([names.get(k) for k in zip(rows["season"], rows["abbr"])], index=rows.index)
        side[unresolved] = np.where(team == rows["home"], "home",
                                    np.where(team == rows["away"], "away", None))
    return side


def consensus_lines(odds: pd.DataFrame) -> pd.DataFrame:
    """Median closing and opening spread, total and moneylines per game."""
    o = odds[~odds["book"].isin(NOT_BOOKS) & odds["game_id"].notna()].copy()
    o["game_id"] = o["game_id"].astype(int)
    sided = o["market_type"].isin(["spread", "money_line"])
    o.loc[sided, "side"] = _resolve_sides(o[sided])

    sp = o[o["market_type"].eq("spread") & o["side"].notna()].copy()
    sign = np.where(sp["side"] == "home", -1.0, 1.0)     # a home line of -7 is a 7-point home edge
    sp["close"] = sign * sp["lines"]
    sp["open"] = sign * sp["opening_lines"]
    spread = sp.groupby(["game_id", "book"])[["close", "open"]].mean().groupby("game_id").agg(
        spread_line=("close", "median"), spread_open=("open", "median"), books=("close", "count"))

    side = o["abbr"].astype(str).str.lower()
    tot = o[o["market_type"].eq("total") & side.eq("over")]
    total = tot.groupby(["game_id", "book"])[["lines", "opening_lines"]].mean().groupby("game_id").agg(
        total_line=("lines", "median"), total_open=("opening_lines", "median"))

    ml = o[o["market_type"].eq("money_line") & o["side"].notna()]
    money = ml.pivot_table(index="game_id", columns="side", values="odds", aggfunc=median_price)
    money = money.rename(columns={"home": "home_moneyline", "away": "away_moneyline"})

    seasons = o.groupby("game_id")["season"].first().astype(int)
    out = spread.join(total, how="outer").join(money, how="left").join(seasons)
    out = out.reset_index().rename(columns={"index": "game_id"})
    for col in LINE_COLUMNS:
        if col not in out:
            out[col] = np.nan
    out["books"] = out["books"].fillna(0).astype(int)
    # A median of a single quarter-point quote can land on .25; real lines move in halves.
    for col in ("spread_line", "total_line", "spread_open", "total_open"):
        out[col] = (out[col] * 2).round() / 2

    # Prices: books quoting exactly the consensus line, per side.
    sp_line = sp["game_id"].map(out.set_index("game_id")["spread_line"])
    at = sp[(sp["close"] - sp_line).abs() < 0.01]
    tot_all = o[o["market_type"].eq("total") & side.isin(["over", "under"])]
    at_total = tot_all[(tot_all["lines"] - tot_all["game_id"].map(out.set_index("game_id")["total_line"])).abs() < 0.01]
    prices = pd.concat([
        at.assign(col=at["side"] + "_spread_price"),
        at_total.assign(col=side[at_total.index] + "_price"),
    ])
    if len(prices):
        table = prices.pivot_table(index="game_id", columns="col", values="odds", aggfunc=median_price)
        for col in PRICE_COLUMNS:
            if col in table:
                out[col] = out["game_id"].map(table[col])
    return out[LINE_COLUMNS].sort_values(["season", "game_id"], ignore_index=True)


def build_consensus(max_age_hours: float = 24.0) -> pd.DataFrame:
    """Consensus lines for every game in the multi-book odds file."""
    path = fetch(LINES_URL, CACHE_DIR / "lines.csv.gz", max_age_hours)
    odds = pd.read_csv(path, low_memory=False)
    return consensus_lines(odds[odds["season"] >= 2013])


def load_lines(first: int, last: int) -> pd.DataFrame:
    """Consensus lines where the odds file has them, else the play-by-play line."""
    frames = [pd.read_csv(LINES_PATH)] if LINES_PATH.exists() else []
    for season in range(first, last + 1):
        path = summary_paths(season)[2]
        if path.exists():
            frames.append(pd.read_csv(path).assign(books=0))
    if not frames:
        return pd.DataFrame(columns=LINE_COLUMNS)
    lines = pd.concat(frames, ignore_index=True).reindex(columns=LINE_COLUMNS)
    lines = lines[lines["season"].between(first, last)]
    consensus = lines.drop_duplicates("game_id", keep="first").set_index("game_id")
    single = lines[lines["books"] == 0].drop_duplicates("game_id", keep="last").set_index("game_id")
    for col in ("spread_line", "total_line"):
        consensus[col] = consensus[col].fillna(single[col].reindex(consensus.index))
    return consensus.reset_index()[LINE_COLUMNS]
