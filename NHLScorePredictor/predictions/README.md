# NHL score predictions

Updated Sat Oct 31, 2026 10:33 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Sunday, November 1

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1:00 PM | WPG @ CAR | WPG 3, CAR 4 | CAR 70% | WPG +240 / CAR -240 | 2.5 – 3.8 | 1–5 / 1–6 | 20% | CAR -1.5 49% | 6.3 / 6.5 (over 47%) | Stuart Skinner (expected) / Pyotr Kochetkov (expected) | WPG +225 / CAR -278 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 3:30 PM | MIN @ WSH | MIN 4, WSH 3 | MIN 53% | MIN -110 / WSH +110 | 3.2 – 3.0 | 1–6 / 1–5 | 22% | MIN -1.5 32% | 6.2 / 6.5 (over 45%) | Jesper Wallstedt (confirmed) / Logan Thompson (expected) | MIN -108 / WSH -112 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 4:00 PM | UTA @ PHI | UTA 3, PHI 2 | UTA 61% | UTA -160 / PHI +160 | 3.5 – 2.7 | 1–6 / 1–5 | 21% | UTA -1.5 40% | 6.2 / 6.5 (over 44%) | Karel Vejmelka (expected) / Dan Vladar (expected) | UTA -162 / PHI +136 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 6:00 PM | EDM @ NYR | EDM 3, NYR 4 | NYR 54% | EDM +115 / NYR -115 | 3.1 – 3.4 | 1–5 / 1–6 | 22% | NYR -1.5 33% | 6.5 / 6.5 (over 50%) | Matt Tomkins (confirmed) / Dylan Garand (expected) | EDM +105 / NYR -125 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | OTT @ ANA | OTT 3, ANA 4 | ANA 51% | OTT +105 / ANA -105 | 3.3 – 3.4 | 1–6 / 1–6 | 22% | ANA -1.5 30% | 6.7 / 6.5 (over 52%) | Jonas Johansson (expected) / Laurent Brossoit (confirmed) | OTT -118 / ANA -102 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Monday, November 2

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | VGK @ BOS | VGK 2, BOS 3 | BOS 52% | VGK +110 / BOS -110 | 3.0 – 3.1 | 1–5 / 1–5 | 23% | BOS -1.5 31% | 6.1 | Carter Hart (expected) / Jeremy Swayman (expected) | – | no line yet (model fair BOS -1.5 +225 / VGK +1.5 -225) | no line yet | no line yet |
| 7:00 PM | DET @ FLA | DET 2, FLA 3 | FLA 59% | DET +145 / FLA -145 | 2.6 – 3.3 | 1–5 / 1–6 | 23% | FLA -1.5 37% | 5.9 | John Gibson (expected) / Akira Schmid (expected) | – | no line yet (model fair FLA -1.5 +170 / DET +1.5 -170) | no line yet | no line yet |
| 8:00 PM | COL @ CHI | COL 4, CHI 3 | COL 70% | COL -235 / CHI +235 | 4.0 – 2.7 | 2–7 / 1–5 | 19% | COL -1.5 49% | 6.7 | Mackenzie Blackwood (expected) / Spencer Knight (expected) | – | no line yet (model fair CHI +1.5 -105 / COL -1.5 +105) | no line yet | no line yet |
| 9:00 PM | CGY @ SJS | CGY 4, SJS 3 | CGY 55% | CGY -125 / SJS +125 | 3.5 – 3.2 | 1–6 / 1–6 | 21% | CGY -1.5 35% | 6.7 | Dustin Wolf (expected) / Yaroslav Askarov (expected) | – | no line yet (model fair SJS +1.5 -185 / CGY -1.5 +185) | no line yet | no line yet |

\* price not posted; assumed -110.

## Tuesday, November 3

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | UTA @ TOR | UTA 4, TOR 3 | UTA 62% | UTA -160 / TOR +160 | 3.6 – 2.9 | 1–6 / 1–5 | 21% | UTA -1.5 40% | 6.5 | Karel Vejmelka (expected) / Sergei Bobrovsky (expected) | – | no line yet (model fair TOR +1.5 -150 / UTA -1.5 +150) | no line yet | no line yet |
| 7:00 PM | WPG @ MTL | WPG 3, MTL 4 | MTL 59% | WPG +145 / MTL -145 | 2.8 – 3.4 | 1–5 / 1–6 | 21% | MTL -1.5 38% | 6.2 | Stuart Skinner (expected) / Jacob Fowler (expected) | – | no line yet (model fair MTL -1.5 +165 / WPG +1.5 -165) | no line yet | no line yet |
| 7:00 PM | DET @ TBL | DET 2, TBL 3 | TBL 66% | DET +200 / TBL -200 | 2.5 – 3.5 | 1–5 / 1–6 | 20% | TBL -1.5 45% | 6.0 | Daniil Tarasov (expected) / Andrei Vasilevskiy (expected) | – | no line yet (model fair TBL -1.5 +125 / DET +1.5 -125) | no line yet | no line yet |
| 7:00 PM | STL @ NYR | STL 2, NYR 3 | NYR 51% | STL +105 / NYR -105 | 3.1 – 3.1 | 1–5 / 1–5 | 22% | NYR -1.5 30% | 6.2 | Joel Hofer (expected) / James Reimer (expected) | – | no line yet (model fair NYR -1.5 +235 / STL +1.5 -235) | no line yet | no line yet |
| 7:00 PM | MIN @ PHI | MIN 3, PHI 2 | MIN 63% | MIN -170 / PHI +170 | 3.4 – 2.6 | 1–6 / 1–5 | 22% | MIN -1.5 41% | 6.0 | Jesper Wallstedt (expected) / Dan Vladar (expected) | – | no line yet (model fair PHI +1.5 -145 / MIN -1.5 +145) | no line yet | no line yet |
| 7:00 PM | VGK @ PIT | VGK 3, PIT 4 | PIT 54% | VGK +120 / PIT -120 | 3.1 – 3.4 | 1–5 / 1–6 | 22% | PIT -1.5 34% | 6.4 | Adin Hill (expected) / Arturs Silovs (expected) | – | no line yet (model fair PIT -1.5 +195 / VGK +1.5 -195) | no line yet | no line yet |
| 7:00 PM | DAL @ WSH | DAL 3, WSH 2 | DAL 50% | DAL -100 / WSH +100 | 2.9 – 2.9 | 1–5 / 1–5 | 23% | DAL -1.5 28% | 5.9 | Jake Oettinger (expected) / Logan Thompson (expected) | – | no line yet (model fair WSH +1.5 -255 / DAL -1.5 +255) | no line yet | no line yet |
| 7:00 PM | COL @ CBJ | COL 4, CBJ 3 | COL 53% | COL -115 / CBJ +115 | 3.3 – 3.1 | 1–6 / 1–5 | 22% | COL -1.5 32% | 6.4 | Scott Wedgewood (expected) / Jet Greaves (expected) | – | no line yet (model fair CBJ +1.5 -210 / COL -1.5 +210) | no line yet | no line yet |
| 7:30 PM | EDM @ NJD | EDM 3, NJD 4 | NJD 60% | EDM +150 / NJD -150 | 2.9 – 3.5 | 1–5 / 1–6 | 22% | NJD -1.5 39% | 6.4 | Tristan Jarry (expected) / Connor Hellebuyck (expected) | – | no line yet (model fair NJD -1.5 +155 / EDM +1.5 -155) | no line yet | no line yet |
| 8:00 PM | CAR @ NSH | CAR 4, NSH 3 | CAR 66% | CAR -190 / NSH +190 | 3.8 – 2.7 | 1–6 / 1–5 | 21% | CAR -1.5 44% | 6.5 | Pyotr Kochetkov (expected) / Juuse Saros (expected) | – | no line yet (model fair NSH +1.5 -125 / CAR -1.5 +125) | no line yet | no line yet |
| 9:00 PM | ANA @ VAN | ANA 4, VAN 3 | ANA 57% | ANA -130 / VAN +130 | 3.8 – 3.3 | 1–6 / 1–6 | 21% | ANA -1.5 37% | 7.0 | Lukas Dostal (expected) / Leevi Meriläinen (expected) | – | no line yet (model fair VAN +1.5 -175 / ANA -1.5 +175) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 216 | 0.6526 | 0.2303 | 61.1% | 1.40 | 1.79 | 89.4% |
| Model only (before blending) | 216 | 0.6543 | 0.2311 | 59.7% | – | – | – |
| Elo | 216 | 0.6679 | 0.2375 | 61.6% | – | – | – |
| Final prediction, games with a line | 82 | 0.6642 | 0.2357 | 57.3% | 1.41 | 1.86 | 89.0% |
| Model only, games with a line | 82 | 0.6685 | 0.2379 | 53.7% | – | – | – |
| Betting market (de-vigged moneyline) | 82 | 0.6655 | 0.2363 | 59.8% | – | 1.83 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.6% of regular-season games, happened in 22.7%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 1 | 0-1-0 | 1.3 | -1.29 | -100.0% | +11.8% |
| Moneyline | 6 | 3-3-0 | 6.2 | +0.98 | +15.8% | +5.8% |
| Total | 1 | 0-1-0 | 0.9 | -0.89 | -100.0% | +3.0% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 14 of 17 games (82%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Friday, October 30

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| NJD @ VGK | 2–3 | 5–2 | 46% | yes | Connor Hellebuyck / Carter Hart |
| WPG @ FLA | 2–3 | 2–5 | 65% | yes | Nico Daws / Akira Schmid |
| SEA @ CGY | 3–4 | 2–6 | 51% | yes | Philipp Grubauer / Dustin Wolf |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.67 | +0.39 | +0.28 | 3.38 | 2.39 | 8.17 | 6.90 | 1580 |
| 2 | UTA | +0.47 | +0.25 | +0.22 | 3.18 | 2.38 | 8.05 | 8.44 | 1515 |
| 3 | TBL | +0.37 | +0.19 | +0.18 | 2.92 | 2.48 | 8.31 | 7.87 | 1541 |
| 4 | MIN | +0.36 | +0.14 | +0.22 | 3.02 | 2.45 | 9.26 | 8.17 | 1538 |
| 5 | VGK | +0.32 | +0.07 | +0.25 | 2.74 | 2.39 | 8.93 | 7.41 | 1527 |
| 6 | COL | +0.30 | +0.29 | +0.01 | 3.01 | 2.73 | 7.77 | 7.90 | 1549 |
| 7 | PIT | +0.27 | +0.23 | +0.04 | 3.10 | 2.64 | 8.03 | 7.71 | 1497 |
| 8 | FLA | +0.27 | +0.01 | +0.26 | 2.64 | 2.38 | 9.29 | 7.63 | 1507 |
| 9 | NJD | +0.26 | +0.03 | +0.24 | 2.84 | 2.38 | 9.05 | 7.83 | 1511 |
| 10 | DAL | +0.24 | -0.08 | +0.32 | 2.53 | 2.30 | 9.20 | 7.33 | 1524 |
| 11 | BUF | +0.12 | +0.11 | +0.01 | 2.81 | 2.68 | 7.82 | 8.45 | 1518 |
| 12 | STL | +0.08 | -0.01 | +0.09 | 2.64 | 2.60 | 7.02 | 7.44 | 1505 |
| 13 | EDM | +0.07 | +0.12 | -0.05 | 2.61 | 2.75 | 9.90 | 8.18 | 1523 |
| 14 | BOS | +0.04 | +0.07 | -0.02 | 2.82 | 2.78 | 7.78 | 8.15 | 1528 |
| 15 | WSH | +0.04 | +0.11 | -0.07 | 2.88 | 2.80 | 7.80 | 8.12 | 1523 |
| 16 | NYR | +0.03 | +0.03 | +0.00 | 2.73 | 2.72 | 8.63 | 7.78 | 1493 |
| 17 | OTT | +0.01 | -0.06 | +0.07 | 2.60 | 2.61 | 7.96 | 8.33 | 1514 |
| 18 | LAK | +0.01 | -0.11 | +0.12 | 2.56 | 2.57 | 8.19 | 8.14 | 1474 |
| 19 | DET | -0.00 | -0.08 | +0.08 | 2.69 | 2.59 | 8.44 | 8.65 | 1485 |
| 20 | MTL | -0.05 | +0.04 | -0.09 | 2.84 | 2.83 | 7.13 | 8.34 | 1532 |
| 21 | NYI | -0.08 | -0.05 | -0.03 | 2.73 | 2.77 | 7.63 | 8.67 | 1496 |
| 22 | CBJ | -0.12 | -0.09 | -0.04 | 2.60 | 2.74 | 7.73 | 8.45 | 1491 |
| 23 | TOR | -0.13 | -0.01 | -0.12 | 2.50 | 2.84 | 8.76 | 8.21 | 1482 |
| 24 | WPG | -0.13 | -0.13 | -0.00 | 2.53 | 2.73 | 8.18 | 8.82 | 1465 |
| 25 | NSH | -0.14 | -0.07 | -0.07 | 2.62 | 2.79 | 7.87 | 7.62 | 1479 |
| 26 | CGY | -0.23 | -0.09 | -0.14 | 2.61 | 2.87 | 7.32 | 8.11 | 1469 |
| 27 | SEA | -0.25 | -0.10 | -0.15 | 2.43 | 2.87 | 7.20 | 8.53 | 1478 |
| 28 | PHI | -0.31 | -0.27 | -0.05 | 2.35 | 2.76 | 7.78 | 7.62 | 1471 |
| 29 | ANA | -0.38 | -0.02 | -0.36 | 2.76 | 3.09 | 7.96 | 8.58 | 1474 |
| 30 | VAN | -0.71 | -0.21 | -0.50 | 2.31 | 3.24 | 7.63 | 8.75 | 1415 |
| 31 | SJS | -0.76 | -0.22 | -0.54 | 2.35 | 3.29 | 7.34 | 8.79 | 1467 |
| 32 | CHI | -0.76 | -0.29 | -0.47 | 2.33 | 3.22 | 7.17 | 8.37 | 1432 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| WSH | Logan Thompson | 63% | +0.45 | +0.19 |
| NYI | Ilya Sorokin | 67% | +0.40 | +0.17 |
| MTL | Jacob Fowler | 57% | +0.32 | +0.13 |
| BOS | Jeremy Swayman | 79% | +0.31 | +0.13 |
| CGY | Devin Cooley | 79% | +0.21 | +0.09 |
| MIN | Jesper Wallstedt | 85% | +0.16 | +0.07 |
| COL | Mackenzie Blackwood | 67% | +0.15 | +0.06 |
| TBL | Andrei Vasilevskiy | 73% | +0.14 | +0.06 |
| OTT | Linus Ullmark | 49% | +0.14 | +0.06 |
| CHI | Spencer Knight | 89% | +0.14 | +0.06 |
| DAL | Jake Oettinger | 77% | +0.11 | +0.05 |
| CBJ | Jet Greaves | 51% | +0.10 | +0.04 |
| STL | Joel Hofer | 70% | +0.05 | +0.02 |
| WPG | Stuart Skinner | 62% | +0.02 | +0.01 |
| CAR | Pyotr Kochetkov | 66% | -0.02 | -0.01 |
| NYR | Dylan Garand | 63% | -0.06 | -0.02 |
| NJD | Jake Allen | 54% | -0.06 | -0.03 |
| PHI | Joseph Woll | 54% | -0.07 | -0.03 |
| DET | John Gibson | 67% | -0.11 | -0.05 |
| SJS | Yaroslav Askarov | 63% | -0.14 | -0.06 |
| UTA | Karel Vejmelka | 70% | -0.15 | -0.06 |
| FLA | Akira Schmid | 58% | -0.17 | -0.07 |
| TOR | Sergei Bobrovsky | 68% | -0.17 | -0.07 |
| BUF | Ukko-Pekka Luukkonen | 58% | -0.17 | -0.07 |
| ANA | Lukas Dostal | 65% | -0.17 | -0.07 |
| SEA | Philipp Grubauer | 63% | -0.19 | -0.08 |
| LAK | Darcy Kuemper | 65% | -0.21 | -0.09 |
| NSH | Juuse Saros | 74% | -0.25 | -0.10 |
| PIT | Arturs Silovs | 73% | -0.29 | -0.12 |
| VAN | Leevi Meriläinen | 61% | -0.29 | -0.12 |
| VGK | Adin Hill | 52% | -0.35 | -0.15 |
| EDM | Tristan Jarry | 52% | -0.37 | -0.16 |

## Current model fit

- Fitted on 5808 games from 2022-23 to 2026-27.
- Home ice: +3.1% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.7% goals scored, +3.3% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 23%.
- Blend: 42% on the betting line wherever there is one (fitted on 82 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
