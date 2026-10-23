# Walk-forward backtest

Seasons 2016-17 to 2025-26. Every game is predicted using only earlier days of its season plus the preseason prior, with the goal-rate model and simulator fitted on earlier seasons only. Baselines are scored on the same games. The betting market (sportsbookreview's archive of opening and closing lines, 2011-12 to 2021-22) is compared on the seasons it covers.

## 2016-17 to 2025-26

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | Total-goals RPS |
|---|---|---|---|---|---|---|---|
| Model + simulator | 13175 | 0.6672 | 0.2374 | 59.0% | 1.37 | 1.84 | 0.0850 |
| Goals-only Poisson | 13175 | 0.6721 | 0.2397 | 58.0% | – | – | – |
| Elo | 13175 | 0.6707 | 0.2390 | 58.4% | – | – | – |
| Home team every time | 13175 | 0.6900 | 0.2484 | 54.0% | – | – | – |

## 2017-18 on (seasons not used for tuning)

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | Total-goals RPS |
|---|---|---|---|---|---|---|---|
| Model + simulator | 11858 | 0.6667 | 0.2372 | 59.1% | 1.37 | 1.85 | 0.0853 |
| Goals-only Poisson | 11858 | 0.6721 | 0.2397 | 58.0% | – | – | – |
| Elo | 11858 | 0.6705 | 0.2389 | 58.5% | – | – | – |
| Home team every time | 11858 | 0.6903 | 0.2486 | 53.8% | – | – | – |

## Is the difference real?

Paired bootstrap of the per-game log loss (negative favors the first).

| Comparison | Mean difference | 95% interval |
|---|---|---|
| Model vs Elo | -0.0035 | -0.0049 to -0.0021 |
| Model vs goals-only Poisson | -0.0049 | -0.0063 to -0.0036 |

## Win-probability calibration

| Predicted home win | Games | Mean predicted | Actual |
|---|---|---|---|
| 10-20% | 5 | 19.1% | 0.0% |
| 20-30% | 112 | 27.2% | 33.0% |
| 30-40% | 814 | 36.4% | 36.2% |
| 40-50% | 3312 | 45.8% | 44.0% |
| 50-60% | 5379 | 55.0% | 54.8% |
| 60-70% | 2904 | 64.1% | 64.0% |
| 70-80% | 603 | 73.5% | 78.6% |
| 80-90% | 46 | 82.3% | 80.4% |

## Score distribution checks (regular season)

| Check | Simulator | Independent Poisson, same rates | Actual |
|---|---|---|---|
| Tied after regulation | 21.8% | 17.2% | 22.5% |
| One-goal regulation margin (empty-netters counted) | 19.7% | 31.1% | 20.6% |
| Game with an empty-net goal | 27.7% | – | 30.3% |
| Home team wins by 2+ (all games) | 32.7% | – | 32.5% |
| Total-goals ranked probability score (lower is better) | 0.0850 | 0.0853 | – |

- 80% ranges contained the team's actual goals 89.0% of the time (goals are whole numbers, so a range covers a little more than 80%).
- Headline score exactly right: 7.6% of games.

## Starting goalies

- Projected starter was the actual starter 65.5% of the time.
- Log loss with projected starters: 0.6667, against 0.6672 with the confirmed starter (difference +0.0004, 95% interval -0.0001 to +0.0010).

## Against the betting market

Sportsbookreview's archived lines on the 6903 games of 2016-17 to 2021-22 that it covers, matched by date, teams and final score. The blend backs each team's goal rate out of the closing moneyline and total through the simulator and mixes it with the model's, with the weight on the model fitted on the archive's earlier seasons only (2016-17 67%, 2017-18 67%, 2018-19 65%, 2019-20 63%, 2020-21 64%, 2021-22 63%). Fitted on all 11663 archived games (2012-13 to 2021-22), the weight is 57%, which is where the live predictor's blend now starts.

| Predictor | Log loss |
|---|---|
| Model + simulator | 0.6677 |
| Opening line (de-vigged) | 0.6685 |
| Closing line (de-vigged) | 0.6660 |
| Model blended with the closing line | 0.6665 |

| Comparison | Mean difference | 95% interval |
|---|---|---|
| Model vs closing line | +0.0017 | -0.0003 to +0.0037 |
| Blend vs closing line | +0.0005 | -0.0009 to +0.0019 |
| Model vs opening line | -0.0008 | -0.0030 to +0.0013 |

## Betting edges

Edges on the same games, priced as on the live page: the final prediction (the walk-forward blend, simulated against the line and anchored to the market's own chances) and, for comparison, the model alone (the rule used before). A side is bet when its EV is at least 3%, at 25% of the Kelly stake with at most 3 units (1% of the bankroll each) on one game. The starting goalies are the actual ones. The archive's moneyline and puck-line prices are used as posted; its totals carry one price whose side is not recorded, so totals are graded at an assumed -110, and it has no opening puck lines. ROI is units won per unit staked, with a 95% bootstrap range over games; expected ROI is what the edges' EVs promised.

| Lines | Chances | Market | Edges | Record (W-L-P) | Staked | Units won | ROI | 95% range | Expected ROI |
|---|---|---|---|---|---|---|---|---|---|
| closing | final | Puck line | 1602 | 791-811-0 | 1913.5 | +14.3 | +0.7% | -4.4% to +5.9% | +6.8% |
| closing | final | Moneyline | 2557 | 1082-1475-0 | 2862.4 | +28.1 | +1.0% | -3.9% to +5.8% | +8.6% |
| closing | final | Total | 1715 | 844-753-118 | 2704.1 | +65.5 | +2.4% | -2.2% to +7.1% | +6.8% |
| closing | model only | Puck line | 2570 | 1330-1240-0 | 3412.7 | -93.0 | -2.7% | -6.5% to +1.0% | +8.6% |
| closing | model only | Moneyline | 3421 | 1414-2007-0 | 3913.0 | -24.1 | -0.6% | -4.7% to +3.4% | +10.9% |
| closing | model only | Total | 2764 | 1361-1216-187 | 4588.8 | +116.4 | +2.5% | -1.2% to +6.3% | +8.6% |
| opening | final | Moneyline | 1921 | 843-1078-0 | 2475.2 | +203.6 | +8.2% | +1.5% to +15.1% | +10.5% |
| opening | final | Total | 1843 | 915-788-140 | 3151.9 | +98.2 | +3.1% | -1.5% to +7.6% | +7.0% |
| opening | model only | Moneyline | 2805 | 1209-1596-0 | 4089.9 | +227.4 | +5.6% | +0.2% to +11.0% | +13.2% |
| opening | model only | Total | 2904 | 1448-1246-210 | 5432.4 | +216.9 | +4.0% | +0.5% to +7.5% | +8.9% |
