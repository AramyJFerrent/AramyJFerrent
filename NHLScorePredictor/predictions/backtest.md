# Walk-forward backtest

Seasons 2016-17 to 2025-26. Every game is predicted using only earlier days of its season plus the preseason prior, with the goal-rate model and simulator fitted on earlier seasons only. Baselines are scored on the same games. No free source has a long history of NHL betting lines, so the market comparison lives on the predictions page, graded live.

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
