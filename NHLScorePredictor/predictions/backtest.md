# Walk-forward backtest

Seasons 2016-17 to 2025-26. Every game is predicted using only earlier days of its season plus the preseason prior, with the goal-rate model and simulator fitted on earlier seasons only. Baselines are scored on the same games. The betting market (sportsbookreview's archive of opening and closing lines, 2011-12 to 2021-22) is compared on the seasons it covers.

## 2016-17 to 2025-26

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | Total-goals RPS |
|---|---|---|---|---|---|---|---|
| Model + simulator | 13175 | 0.6665 | 0.2371 | 58.9% | 1.37 | 1.84 | 0.0851 |
| Goals-only Poisson | 13175 | 0.6721 | 0.2397 | 58.0% | – | – | – |
| Elo | 13175 | 0.6707 | 0.2390 | 58.4% | – | – | – |
| Home team every time | 13175 | 0.6900 | 0.2484 | 54.0% | – | – | – |

## 2017-18 on (seasons not used for tuning)

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | Total-goals RPS |
|---|---|---|---|---|---|---|---|
| Model + simulator | 11858 | 0.6662 | 0.2369 | 59.0% | 1.37 | 1.85 | 0.0854 |
| Goals-only Poisson | 11858 | 0.6721 | 0.2397 | 58.0% | – | – | – |
| Elo | 11858 | 0.6705 | 0.2389 | 58.5% | – | – | – |
| Home team every time | 11858 | 0.6903 | 0.2486 | 53.8% | – | – | – |

## Is the difference real?

Paired bootstrap of the per-game log loss (negative favors the first).

| Comparison | Mean difference | 95% interval |
|---|---|---|
| Model vs Elo | -0.0041 | -0.0056 to -0.0027 |
| Model vs goals-only Poisson | -0.0056 | -0.0070 to -0.0042 |

## Win-probability calibration

| Predicted home win | Games | Mean predicted | Actual |
|---|---|---|---|
| 10-20% | 4 | 19.1% | 25.0% |
| 20-30% | 115 | 27.1% | 31.3% |
| 30-40% | 801 | 36.3% | 34.3% |
| 40-50% | 3326 | 45.8% | 44.6% |
| 50-60% | 5373 | 55.0% | 54.4% |
| 60-70% | 2910 | 64.1% | 64.9% |
| 70-80% | 600 | 73.6% | 76.8% |
| 80-90% | 46 | 82.3% | 82.6% |

## Score distribution checks (regular season)

| Check | Simulator | Independent Poisson, same rates | Actual |
|---|---|---|---|
| Tied after regulation | 21.7% | 17.2% | 22.5% |
| One-goal regulation margin (empty-netters counted) | 19.7% | 31.1% | 20.6% |
| Game with an empty-net goal | 27.7% | – | 30.3% |
| Home team wins by 2+ (all games) | 32.8% | – | 32.5% |
| Total-goals ranked probability score (lower is better) | 0.0851 | 0.0854 | – |

- 80% ranges contained the team's actual goals 89.0% of the time (goals are whole numbers, so a range covers a little more than 80%).
- Headline score exactly right: 7.4% of games.

## Starting goalies

- Projected starter was the actual starter 65.5% of the time.
- Log loss with projected starters: 0.6666, against 0.6665 with the confirmed starter (difference -0.0001, 95% interval -0.0006 to +0.0004).

## Against the betting market

Sportsbookreview's archived lines on the 6903 games of 2016-17 to 2021-22 that it covers, matched by date, teams and final score. The blend backs each team's goal rate out of the closing moneyline and total through the simulator and mixes it with the model's, with the weight on the model fitted on the archive's earlier seasons only (2016-17 66%, 2017-18 66%, 2018-19 64%, 2019-20 63%, 2020-21 65%, 2021-22 63%). Fitted on all 11663 archived games (2012-13 to 2021-22), the weight is 57%, which is where the live predictor's blend now starts.

| Predictor | Log loss |
|---|---|
| Model + simulator | 0.6668 |
| Opening line (de-vigged) | 0.6685 |
| Closing line (de-vigged) | 0.6660 |
| Model blended with the closing line | 0.6665 |

| Comparison | Mean difference | 95% interval |
|---|---|---|
| Model vs closing line | +0.0008 | -0.0012 to +0.0028 |
| Blend vs closing line | +0.0005 | -0.0008 to +0.0019 |
| Model vs opening line | -0.0017 | -0.0039 to +0.0005 |

## Betting edges

Edges on the same games, priced as on the live page: the final prediction (the walk-forward blend, simulated against the line and anchored to the market's own chances) and, for comparison, the model alone (the rule used before). A side is bet when its EV is at least 3%, at 25% of the Kelly stake with at most 3 units (1% of the bankroll each) on one game. The starting goalies are the actual ones. The archive's moneyline and puck-line prices are used as posted; its totals carry one price whose side is not recorded, so totals are graded at an assumed -110, and it has no opening puck lines. ROI is units won per unit staked, with a 95% bootstrap range over games; expected ROI is what the edges' EVs promised.

| Lines | Chances | Market | Edges | Record (W-L-P) | Staked | Units won | ROI | 95% range | Expected ROI |
|---|---|---|---|---|---|---|---|---|---|
| closing | final | Puck line | 1616 | 798-818-0 | 1890.5 | +29.2 | +1.5% | -3.4% to +6.5% | +6.8% |
| closing | final | Moneyline | 2587 | 1075-1512-0 | 2931.5 | -63.1 | -2.2% | -6.7% to +2.7% | +8.6% |
| closing | final | Total | 1832 | 899-806-127 | 2914.0 | +0.7 | +0.0% | -4.5% to +4.5% | +7.0% |
| closing | model only | Puck line | 2463 | 1264-1199-0 | 3098.4 | -43.9 | -1.4% | -5.3% to +2.7% | +8.8% |
| closing | model only | Moneyline | 3452 | 1462-1990-0 | 3971.3 | +41.7 | +1.0% | -3.2% to +5.2% | +10.8% |
| closing | model only | Total | 2825 | 1391-1245-189 | 4739.8 | +63.1 | +1.3% | -2.5% to +5.0% | +8.8% |
| opening | final | Moneyline | 1907 | 838-1069-0 | 2479.6 | +220.0 | +8.9% | +1.7% to +16.2% | +10.4% |
| opening | final | Total | 1877 | 955-786-136 | 3199.9 | +123.4 | +3.9% | -0.5% to +8.1% | +7.0% |
| opening | model only | Moneyline | 2803 | 1235-1568-0 | 4088.5 | +259.0 | +6.3% | +1.1% to +11.8% | +13.2% |
| opening | model only | Total | 2903 | 1454-1241-208 | 5474.5 | +190.9 | +3.5% | -0.0% to +7.0% | +9.1% |
