# BettingCore

The betting math shared by the six predictors, so every sport prices, stakes
and grades its edges the same way. Each predictor installs it from its own
`requirements.txt` (`-e ../BettingCore`).

| Module | What it does |
|---|---|
| `odds.py` | American and decimal prices, implied chances, de-vigging a two-way market, fair prices, and expected value per unit staked: `EV = p × (decimal price − 1) − (1 − p − push)` |
| `anchor.py` | Anchors a forecast's chance to the market: the market's de-vigged chance plus the difference between the forecast simulated at the blend and the same simulation (same random draws) at the line, so a simulator's shape cannot pose as an edge |
| `edges.py` | The best side of a market (an edge at `EDGE_MIN_EV`, 3%), its Kelly stake at `KELLY_FRACTION` (a quarter) in units of 1% of the bankroll, and a cap of `GAME_CAP_UNITS` (3) shared by one game's edges; settling a bet from the final margin |
| `records.py` | A market's record: bets, W-L-P, units staked and won, ROI with a 95% bootstrap range over games (bets on one game resampled together), expected ROI, and a paired bootstrap for comparing two forecasts' losses |
| `sbr.py` | Sportsbookreview's 2011-2021 odds archive (opening and closing moneylines, closing spreads with prices, opening and closing totals), as collected by [sportsbookreview-scraper](https://github.com/flancast90/sportsbookreview-scraper): parsing (zeros are missing values; the baseball file's rows are realigned, since each pairs one game's visitors with the previous game's home team) and matching to a predictor's games by date, teams and final score |
| `io.py` | Cached downloads that fall back to the last good copy, and writing a file only when it changed |

```bash
cd BettingCore
pip install -e . pytest
python -m pytest -q tests
```
