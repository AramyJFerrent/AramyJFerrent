# MLB score predictions

Updated Mon Oct 19, 2026 12:39 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at first pitch and graded once the final score is in.

Each game is simulated 10,000 times inning by inning from tonight's starting pitchers, lineups and bullpens, with the home team skipping the bottom of the ninth when ahead, walk-offs, and the runner on second in regular-season extra innings. The predicted score is a common final score in which the likelier winner wins. Baseball is the most luck-driven of the major sports, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Lineups marked ✓ are the posted ones; "proj." is the lineup the team last used against a starter of the same hand, replaced once the real one posts (usually a few hours before first pitch).

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The run line is the favorite's chance to win by two or more.

The model pick is the side where the model's own win chance (before blending with the market) beats the de-vigged moneyline by 3% or more. Treat it as an experiment: its record is tracked live below.

## Monday, October 19 — League Championship Series

| Time (ET) | Game | Starting pitchers | Predicted score | Win chance | Fair moneyline | Expected runs | 80% range | Run line | Total: model / line | Extra innings | Lineups | Moneyline / model pick (edge) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8:08 PM | CLE @ TB | Shawn Armstrong / Freddy Peralta | CLE 3, TB 4 | TB 60% | CLE +150 / TB -150 | 3.3 – 3.9 | 0–7 / 1–8 | TB -1.5 39% | 7.2 / 6.5 (over 53%) | 10% | proj. / proj. | CLE +129 / TB -156; no edge |

## Tuesday, October 20 — League Championship Series

| Time (ET) | Game | Starting pitchers | Predicted score | Win chance | Fair moneyline | Expected runs | 80% range | Run line | Total: model / line | Extra innings | Lineups | Moneyline / model pick (edge) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8:08 PM | CLE @ TB | TBD / TBD | CLE 3, TB 4 | TB 57% | CLE +135 / TB -135 | 3.9 – 4.4 | 1–8 / 1–9 | TB -1.5 39% | 8.4 | 9% | proj. / proj. | no line yet |

## How the 2026 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Runs MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 2463 | 0.6817 | 0.2444 | 55.8% | 2.48 | 3.51 | 85.7% |
| Elo with starting pitchers | 2463 | 0.6805 | 0.2438 | 56.7% | – | – | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250, and Pinnacle's closing moneyline scored 0.673 in 2016). Baseball edges are thin, so differences in the third decimal matter, and only over hundreds of games. Runs MAE is the average miss on each team's runs.

Extra innings: predicted in 8.6% of regular-season games, happened in 8.6%.

2463 of these games were played before the predictor went live (or while it was not running). They are backfilled walk-forward (each day predicted from earlier days only, with the run model fitted on earlier seasons) with the actual lineups and starting pitchers and no betting line. Every other game is graded on the prediction logged before first pitch.

### Results, Sunday, October 18

| Game | Starting pitchers | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|---|
| TB @ CLE | Drew Rasmussen / Parker Messick | 4–3 | 3–1 | 54% | yes |

## Power ratings

Runs per game better than an average team against an average opponent at a neutral park, from the run model. The lineup is the team's latest one against average pitching; the rotation is its last five starters, weighted by how deep they go, and the bullpen its relievers by recent use; "fielding and the rest" is what the team's runs allowed say beyond its pitchers' own numbers. Positive is better on every side of the ball.

| # | Team | Net | Lineup | Rotation | Bullpen | Fielding and the rest | Starter innings | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | LAD | +1.39 | +0.66 | +0.36 | +0.10 | +0.27 | 5.2 | 1576 |
| 2 | MIL | +0.94 | +0.48 | +0.14 | +0.09 | +0.23 | 4.9 | 1606 |
| 3 | CHC | +0.74 | +0.61 | +0.06 | +0.01 | +0.07 | 5.3 | 1539 |
| 4 | TB | +0.72 | +0.22 | +0.22 | +0.08 | +0.20 | 5.2 | 1556 |
| 5 | NYY | +0.66 | +0.16 | +0.20 | +0.08 | +0.23 | 5.2 | 1560 |
| 6 | ATL | +0.66 | +0.26 | +0.14 | +0.10 | +0.17 | 5.1 | 1529 |
| 7 | SD | +0.62 | +0.38 | +0.01 | +0.11 | +0.13 | 5.0 | 1546 |
| 8 | PHI | +0.52 | +0.19 | +0.16 | +0.07 | +0.09 | 5.6 | 1531 |
| 9 | HOU | +0.49 | +0.45 | +0.03 | +0.06 | -0.05 | 4.9 | 1489 |
| 10 | ARI | +0.45 | +0.31 | +0.07 | +0.10 | -0.03 | 5.2 | 1512 |
| 11 | NYM | +0.41 | +0.46 | -0.04 | +0.02 | -0.04 | 5.2 | 1497 |
| 12 | SEA | +0.41 | +0.39 | +0.09 | +0.03 | -0.09 | 5.3 | 1475 |
| 13 | CLE | +0.35 | +0.02 | +0.10 | +0.10 | +0.14 | 4.7 | 1516 |
| 14 | BOS | +0.27 | -0.04 | +0.08 | +0.06 | +0.17 | 5.0 | 1531 |
| 15 | CWS | +0.26 | +0.26 | -0.03 | +0.05 | -0.02 | 4.3 | 1507 |
| 16 | DET | +0.23 | +0.09 | -0.01 | +0.08 | +0.07 | 5.0 | 1512 |
| 17 | PIT | +0.22 | +0.03 | +0.10 | +0.05 | +0.04 | 4.6 | 1508 |
| 18 | TOR | +0.17 | +0.02 | +0.03 | +0.03 | +0.08 | 4.8 | 1502 |
| 19 | TEX | +0.16 | +0.06 | +0.05 | +0.07 | -0.02 | 5.0 | 1489 |
| 20 | MIN | +0.06 | +0.06 | +0.08 | +0.03 | -0.10 | 5.3 | 1470 |
| 21 | BAL | +0.02 | +0.00 | -0.08 | +0.05 | +0.04 | 5.4 | 1496 |
| 22 | KC | -0.20 | -0.09 | +0.03 | -0.03 | -0.10 | 5.2 | 1460 |
| 23 | WSH | -0.28 | +0.03 | -0.10 | -0.05 | -0.16 | 4.6 | 1475 |
| 24 | MIA | -0.29 | -0.24 | -0.03 | +0.00 | -0.02 | 4.8 | 1502 |
| 25 | STL | -0.34 | -0.26 | -0.05 | +0.00 | -0.03 | 5.1 | 1481 |
| 26 | CIN | -0.48 | -0.09 | -0.17 | +0.01 | -0.23 | 5.0 | 1456 |
| 27 | SF | -0.49 | -0.43 | -0.05 | -0.00 | -0.00 | 4.8 | 1461 |
| 28 | LAA | -0.62 | -0.48 | -0.06 | -0.03 | -0.05 | 5.3 | 1434 |
| 29 | ATH | -0.74 | +0.06 | -0.24 | -0.06 | -0.50 | 4.8 | 1405 |
| 30 | COL | -0.94 | -0.20 | -0.15 | +0.01 | -0.59 | 4.9 | 1379 |

## Current model fit

- Fitted on 9873 games from 2023 to 2026.
- Home field: +6.2% runs for the home team relative to the visitor.
- Park: each 10% of park run factor moves runs by +6.7%.
- Weather: +4.6% runs per 10°F above 70°F, +3.6% per 10 mph of wind blowing out (open-air parks).
- Matchups: a lineup's edge over the starter counts 0.83 times its face value and over the bullpen 0.70 times.
- Blend: 81% on the betting line wherever there is one (the value fitted on Pinnacle's 2016 closing lines, until enough logged games with lines exist to refit it).
- Simulator: games share a hot-or-cold factor with spread 1/√20, and 25% of walk-offs are home runs that count in full.
