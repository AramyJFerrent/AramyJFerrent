# MLB score predictions

Updated Wed Oct 21, 2026 02:12 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at first pitch and graded once the final score is in.

Each game is simulated 10,000 times inning by inning from tonight's starting pitchers, lineups and bullpens, with the home team skipping the bottom of the ninth when ahead, walk-offs, and the runner on second in regular-season extra innings. The predicted score is a common final score in which the likelier winner wins. Baseball is the most luck-driven of the major sports, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Lineups marked ✓ are the posted ones; "proj." is the lineup the team last used against a starter of the same hand, replaced once the real one posts (usually a few hours before first pitch).

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The run line is the favorite's chance to win by two or more.

The edge columns give the expected value of a bet per $1 staked at the posted price, from the model's own numbers before they are blended with the betting line: its win chance for the moneyline, and its own simulation's chance of covering the posted run line and of going over or under the total (a push on a whole-number total returns the stake). A side counts as an edge when its EV is 3% or more; each market shows its best side, as "pick (price): EV, the model's chance". A total with no posted price is assumed to be -110 on both sides and marked -110*; run-line and moneyline prices are never assumed, so without one the run line shows the model's fair odds instead. Treat the edges as an experiment: the model alone was 0.003 log loss behind Pinnacle's 2016 closing moneyline, and in the backtest its moneyline edges against those closing prices lost 4.5% per bet (95% range -10.8% to +1.7%) while its total edges broke even, so an apparent edge against a sharp line is more often the model's error than the market's. Their record is tracked live below.

## Friday, October 23 — World Series

| Time (ET) | Game | Starting pitchers | Predicted score | Win chance | Fair moneyline | Moneyline | Expected runs | 80% range | Run line | Total: model / line | Extra innings | Lineups | Run line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8:00 PM | TB @ MIL | TBD / Jacob Misiorowski | TB 2, MIL 3 | MIL 60% | TB +150 / MIL -150 | TB +133 / MIL -161 | 3.0 – 3.7 | 0–6 / 1–7 | MIL -1.5 39% | 6.7 / 6 (over 52%) | 10% | proj. / proj. | MIL -1.5 (+152): EV +6.7%, model 42% | no edge | Over 6 (-110): EV +21.9%, model 60% |

## Saturday, October 24 — World Series

| Time (ET) | Game | Starting pitchers | Predicted score | Win chance | Fair moneyline | Moneyline | Expected runs | 80% range | Run line | Total: model / line | Extra innings | Lineups | Run line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8:00 PM | TB @ MIL | TBD / TBD | TB 4, MIL 5 | MIL 56% | TB +125 / MIL -125 | – | 4.1 – 4.4 | 1–8 / 1–9 | MIL -1.5 38% | 8.5 | 9% | proj. / proj. | no line yet; fair MIL -1.5 +160, TB +1.5 -160 | no line yet | no line yet |

## How the 2026 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Runs MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 2464 | 0.6817 | 0.2444 | 55.8% | 2.48 | 3.51 | 85.7% |
| Model only (before blending) | 2464 | 0.6817 | 0.2444 | 55.8% | – | – | – |
| Elo with starting pitchers | 2464 | 0.6805 | 0.2438 | 56.7% | – | – | – |
| Final prediction, games with a line | 1 | 0.5152 | 0.1621 | 100.0% | 1.67 | 2.77 | 100.0% |
| Model only, games with a line | 1 | 0.5614 | 0.1846 | 100.0% | – | – | – |
| Betting market (de-vigged moneyline) | 1 | 0.5404 | 0.1743 | 100.0% | – | 3.50 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250, and Pinnacle's closing moneyline scored 0.673 in 2016). Baseball edges are thin, so differences in the third decimal matter, and only over hundreds of games. Runs MAE is the average miss on each team's runs.

Extra innings: predicted in 8.6% of regular-season games, happened in 8.6%.

2463 of these games were played before the predictor went live (or while it was not running). They are backfilled walk-forward (each day predicted from earlier days only, with the run model fitted on earlier seasons) with the actual lineups and starting pitchers and no betting line. Every other game is graded on the prediction logged before first pitch.

### Betting edges

| Market | Edges | Record (W-L-P) | Units | ROI |
|---|---|---|---|---|
| Run line | 0 | 0-0-0 | +0.00 | – |
| Moneyline | 0 | 0-0-0 | +0.00 | – |
| Total | 0 | 0-0-0 | +0.00 | – |

Moneyline moved toward the model's edge at the first line seen, before first pitch: 0 of 0 games.

One unit on each edge at the price logged with the last prediction before first pitch (live predictions only; ROI is units per bet). The market moving toward the model's side (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Monday, October 19

| Game | Starting pitchers | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|---|
| CLE @ TB | Shawn Armstrong / Freddy Peralta | 3–4 | 3–7 | 60% | yes |

## Power ratings

Runs per game better than an average team against an average opponent at a neutral park, from the run model. The lineup is the team's latest one against average pitching; the rotation is its last five starters, weighted by how deep they go, and the bullpen its relievers by recent use; "fielding and the rest" is what the team's runs allowed say beyond its pitchers' own numbers. Positive is better on every side of the ball.

| # | Team | Net | Lineup | Rotation | Bullpen | Fielding and the rest | Starter innings | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | LAD | +1.38 | +0.66 | +0.36 | +0.10 | +0.27 | 5.2 | 1576 |
| 2 | MIL | +0.94 | +0.48 | +0.14 | +0.09 | +0.23 | 4.9 | 1606 |
| 3 | TB | +0.86 | +0.35 | +0.22 | +0.09 | +0.20 | 5.2 | 1559 |
| 4 | CHC | +0.74 | +0.61 | +0.06 | +0.01 | +0.07 | 5.3 | 1539 |
| 5 | NYY | +0.66 | +0.16 | +0.20 | +0.08 | +0.23 | 5.2 | 1560 |
| 6 | ATL | +0.66 | +0.26 | +0.14 | +0.10 | +0.16 | 5.1 | 1529 |
| 7 | SD | +0.62 | +0.38 | +0.01 | +0.11 | +0.13 | 5.0 | 1546 |
| 8 | PHI | +0.52 | +0.19 | +0.16 | +0.07 | +0.09 | 5.6 | 1531 |
| 9 | HOU | +0.49 | +0.45 | +0.03 | +0.06 | -0.05 | 4.9 | 1489 |
| 10 | ARI | +0.45 | +0.31 | +0.07 | +0.10 | -0.03 | 5.2 | 1512 |
| 11 | SEA | +0.41 | +0.39 | +0.09 | +0.03 | -0.09 | 5.3 | 1475 |
| 12 | NYM | +0.41 | +0.46 | -0.04 | +0.02 | -0.04 | 5.2 | 1497 |
| 13 | CLE | +0.36 | +0.01 | +0.11 | +0.12 | +0.12 | 4.6 | 1514 |
| 14 | BOS | +0.27 | -0.04 | +0.08 | +0.06 | +0.17 | 5.0 | 1531 |
| 15 | CWS | +0.26 | +0.26 | -0.03 | +0.05 | -0.02 | 4.3 | 1507 |
| 16 | DET | +0.23 | +0.09 | -0.01 | +0.08 | +0.07 | 5.0 | 1512 |
| 17 | PIT | +0.22 | +0.02 | +0.10 | +0.05 | +0.04 | 4.6 | 1508 |
| 18 | TOR | +0.17 | +0.02 | +0.03 | +0.03 | +0.08 | 4.8 | 1502 |
| 19 | TEX | +0.16 | +0.06 | +0.05 | +0.07 | -0.02 | 5.0 | 1489 |
| 20 | MIN | +0.06 | +0.06 | +0.08 | +0.03 | -0.10 | 5.3 | 1470 |
| 21 | BAL | +0.02 | +0.00 | -0.08 | +0.05 | +0.04 | 5.4 | 1496 |
| 22 | KC | -0.19 | -0.09 | +0.03 | -0.03 | -0.10 | 5.2 | 1460 |
| 23 | WSH | -0.28 | +0.03 | -0.10 | -0.05 | -0.16 | 4.6 | 1475 |
| 24 | MIA | -0.29 | -0.24 | -0.03 | +0.00 | -0.02 | 4.8 | 1502 |
| 25 | STL | -0.34 | -0.26 | -0.05 | +0.00 | -0.03 | 5.1 | 1481 |
| 26 | CIN | -0.47 | -0.09 | -0.17 | +0.01 | -0.23 | 5.0 | 1456 |
| 27 | SF | -0.48 | -0.43 | -0.05 | -0.00 | -0.00 | 4.8 | 1461 |
| 28 | LAA | -0.62 | -0.48 | -0.06 | -0.03 | -0.05 | 5.3 | 1434 |
| 29 | ATH | -0.73 | +0.06 | -0.24 | -0.06 | -0.49 | 4.8 | 1405 |
| 30 | COL | -0.93 | -0.20 | -0.15 | +0.01 | -0.59 | 4.9 | 1379 |

## Current model fit

- Fitted on 9874 games from 2023 to 2026.
- Home field: +6.2% runs for the home team relative to the visitor.
- Park: each 10% of park run factor moves runs by +6.7%.
- Weather: +4.5% runs per 10°F above 70°F, +3.6% per 10 mph of wind blowing out (open-air parks).
- Matchups: a lineup's edge over the starter counts 0.83 times its face value and over the bullpen 0.70 times.
- Blend: 81% on the betting line wherever there is one (fitted on 1 logged games, shrunk toward the 2016 backtest value).
- Simulator: games share a hot-or-cold factor with spread 1/√20, and 25% of walk-offs are home runs that count in full.
