# NHL score predictions

Updated Fri Oct 30, 2026 04:58 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Friday, October 30

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6:00 PM | NJD @ VGK | NJD 2, VGK 3 | VGK 54% | NJD +115 / VGK -115 | 2.9 – 3.2 | 1–5 / 1–6 | 23% | VGK -1.5 32% | 6.1 / 6.5 (over 43%) | Connor Hellebuyck (confirmed) / Carter Hart (expected) | NJD -105 / VGK -115 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | WPG @ FLA | WPG 2, FLA 3 | FLA 65% | WPG +190 / FLA -190 | 2.5 – 3.5 | 1–5 / 1–6 | 22% | FLA -1.5 43% | 6.1 / 6.5 (over 43%) | Nico Daws (expected) / Akira Schmid (confirmed) | WPG +185 / FLA -225 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | SEA @ CGY | SEA 3, CGY 4 | CGY 51% | SEA +105 / CGY -105 | 3.2 – 3.3 | 1–6 / 1–6 | 22% | CGY -1.5 30% | 6.5 / 6.5 (over 50%) | Philipp Grubauer (expected) / Dustin Wolf (confirmed) | SEA -115 / CGY -105 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Saturday, October 31

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1:00 PM | CHI @ BOS | CHI 3, BOS 4 | BOS 71% | CHI +245 / BOS -245 | 2.5 – 3.9 | 1–5 / 1–6 | 20% | BOS -1.5 49% | 6.4 / 5.5 (over 59%) | Arvid Soderblom (expected) / Jeremy Swayman (expected) | CHI +185 / BOS -225 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 1:00 PM | STL @ DET | STL 3, DET 2 | STL 52% | STL -110 / DET +110 | 3.1 – 2.9 | 1–5 / 1–5 | 23% | STL -1.5 31% | 6.0 / 5.5 (over 52%) | Joel Hofer (expected) / John Gibson (confirmed) | STL -118 / DET -102 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 2:00 PM | TBL @ NSH | TBL 4, NSH 3 | TBL 61% | TBL -155 / NSH +155 | 3.5 – 2.8 | 1–6 / 1–5 | 22% | TBL -1.5 39% | 6.3 / 6.5 (over 46%) | Andrei Vasilevskiy (expected) / Juuse Saros (expected) | TBL -170 / NSH +142 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 2:00 PM | EDM @ NYI | EDM 4, NYI 3 | EDM 50% | EDM -100 / NYI +100 | 3.2 – 3.2 | 1–6 / 1–6 | 22% | EDM -1.5 29% | 6.4 / 6.5 (over 49%) | Tristan Jarry (confirmed) / Ilya Sorokin (expected) | EDM -135 / NYI +114 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 4:00 PM | BUF @ LAK | BUF 4, LAK 3 | BUF 52% | BUF -110 / LAK +110 | 3.2 – 3.0 | 1–6 / 1–5 | 22% | BUF -1.5 32% | 6.2 / 5.5 (over 55%) | Colten Ellis (expected) / Darcy Kuemper (expected) | BUF -122 / LAK +102 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 4:00 PM | OTT @ SJS | OTT 4, SJS 3 | OTT 58% | OTT -140 / SJS +140 | 3.5 – 3.0 | 1–6 / 1–5 | 21% | OTT -1.5 37% | 6.5 / 6.5 (over 50%) | Samuel Ersson (expected) / Yaroslav Askarov (expected) | OTT -135 / SJS +114 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | PIT @ MTL | PIT 3, MTL 4 | MTL 55% | PIT +120 / MTL -120 | 3.1 – 3.4 | 1–6 / 1–6 | 22% | MTL -1.5 34% | 6.6 / 6.5 (over 51%) | Arturs Silovs (expected) / Jacob Fowler (expected) | PIT +130 / MTL -155 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | TOR @ VAN | TOR 4, VAN 3 | TOR 61% | TOR -160 / VAN +160 | 3.8 – 3.0 | 1–6 / 1–5 | 21% | TOR -1.5 41% | 6.7 / 6.5 (over 53%) | Anthony Stolarz (confirmed) / Kevin Lankinen (expected) | TOR -162 / VAN +136 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | CBJ @ DAL | CBJ 2, DAL 3 | DAL 61% | CBJ +155 / DAL -155 | 2.5 – 3.2 | 1–5 / 1–6 | 23% | DAL -1.5 38% | 5.7 / 5.5 (over 48%) | Jet Greaves (expected) / Jake Oettinger (expected) | CBJ +154 / DAL -185 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | CGY @ COL | CGY 3, COL 4 | COL 72% | CGY +255 / COL -255 | 2.5 – 4.0 | 1–5 / 2–7 | 18% | COL -1.5 52% | 6.5 / 6.5 (over 50%) | Arsenii Sergeev (expected) / Mackenzie Blackwood (expected) | CGY +310 / COL -395 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Sunday, November 1

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1:00 PM | WPG @ CAR | WPG 3, CAR 4 | CAR 70% | WPG +235 / CAR -235 | 2.5 – 3.8 | 1–5 / 1–6 | 20% | CAR -1.5 48% | 6.3 | Stuart Skinner (expected) / Pyotr Kochetkov (expected) | – | no line yet (model fair CAR -1.5 +110 / WPG +1.5 -110) | no line yet | no line yet |
| 3:30 PM | MIN @ WSH | MIN 4, WSH 3 | MIN 57% | MIN -130 / WSH +130 | 3.4 – 3.0 | 1–6 / 1–5 | 22% | MIN -1.5 36% | 6.4 | Jesper Wallstedt (expected) / Charlie Lindgren (expected) | – | no line yet (model fair WSH +1.5 -180 / MIN -1.5 +180) | no line yet | no line yet |
| 4:00 PM | UTA @ PHI | UTA 3, PHI 2 | UTA 62% | UTA -165 / PHI +165 | 3.4 – 2.7 | 1–6 / 1–5 | 22% | UTA -1.5 40% | 6.1 | Karel Vejmelka (expected) / Dan Vladar (expected) | – | no line yet (model fair PHI +1.5 -150 / UTA -1.5 +150) | no line yet | no line yet |
| 6:00 PM | EDM @ NYR | EDM 3, NYR 4 | NYR 55% | EDM +125 / NYR -125 | 3.0 – 3.4 | 1–5 / 1–6 | 21% | NYR -1.5 34% | 6.4 | Matt Tomkins (expected) / Dylan Garand (expected) | – | no line yet (model fair NYR -1.5 +190 / EDM +1.5 -190) | no line yet | no line yet |
| 8:00 PM | OTT @ ANA | OTT 3, ANA 4 | ANA 50% | OTT +100 / ANA -100 | 3.3 – 3.3 | 1–6 / 1–6 | 22% | ANA -1.5 30% | 6.5 | Jonas Johansson (expected) / Lukas Dostal (expected) | – | no line yet (model fair ANA -1.5 +230 / OTT +1.5 -230) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 213 | 0.6530 | 0.2305 | 61.0% | 1.40 | 1.80 | 89.2% |
| Model only (before blending) | 213 | 0.6546 | 0.2313 | 59.6% | – | – | – |
| Elo | 213 | 0.6675 | 0.2374 | 61.5% | – | – | – |
| Final prediction, games with a line | 79 | 0.6658 | 0.2365 | 57.0% | 1.40 | 1.89 | 88.6% |
| Model only, games with a line | 79 | 0.6700 | 0.2386 | 53.2% | – | – | – |
| Betting market (de-vigged moneyline) | 79 | 0.6675 | 0.2373 | 60.8% | – | 1.87 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.6% of regular-season games, happened in 23.0%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 1 | 0-1-0 | 1.3 | -1.29 | -100.0% | +11.8% |
| Moneyline | 6 | 3-3-0 | 6.2 | +0.98 | +15.8% | +5.8% |
| Total | 1 | 0-1-0 | 0.9 | -0.89 | -100.0% | +3.0% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 10 of 13 games (77%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Thursday, October 29

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| WPG @ TBL | 2–3 | 4–6 | 64% | yes | Stuart Skinner / Andrei Vasilevskiy |
| UTA @ PIT | 4–3 | 4–3 (OT) | 54% | yes | Karel Vejmelka / Arturs Silovs |
| CBJ @ CAR | 3–4 | 2–3 | 70% | yes | Jet Greaves / Pyotr Kochetkov |
| CHI @ DET | 2–3 | 1–4 | 63% | yes | Spencer Knight / John Gibson |
| BOS @ STL | 2–3 | 1–4 | 51% | yes | Jeremy Swayman / Joel Hofer |
| WSH @ NSH | 3–4 | 4–3 | 49% | yes | Charlie Lindgren / Juuse Saros |
| MTL @ DAL | 2–3 | 5–2 | 41% | yes | Jakub Dobes / Jake Oettinger |
| NYI @ MIN | 2–3 | 4–3 (OT) | 37% | yes | Ilya Sorokin / Jesper Wallstedt |
| BUF @ ANA | 4–3 | 7–6 | 58% | no | Colten Ellis / Ville Husso |
| OTT @ LAK | 3–2 | 5–6 (OT) | 49% | no | Jonas Johansson / Darcy Kuemper |
| VAN @ SJS | 3–4 | 2–3 | 57% | yes | Leevi Meriläinen / Yaroslav Askarov |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.67 | +0.39 | +0.28 | 3.39 | 2.39 | 8.16 | 6.88 | 1580 |
| 2 | UTA | +0.47 | +0.24 | +0.23 | 3.18 | 2.38 | 8.04 | 8.42 | 1515 |
| 3 | TBL | +0.37 | +0.19 | +0.19 | 2.92 | 2.49 | 8.29 | 7.85 | 1541 |
| 4 | MIN | +0.36 | +0.14 | +0.22 | 3.03 | 2.45 | 9.25 | 8.16 | 1538 |
| 5 | VGK | +0.35 | +0.10 | +0.26 | 2.80 | 2.39 | 8.89 | 7.42 | 1534 |
| 6 | COL | +0.30 | +0.29 | +0.01 | 3.01 | 2.73 | 7.75 | 7.88 | 1549 |
| 7 | PIT | +0.27 | +0.23 | +0.05 | 3.10 | 2.64 | 8.01 | 7.70 | 1497 |
| 8 | DAL | +0.25 | -0.08 | +0.33 | 2.53 | 2.31 | 9.18 | 7.32 | 1524 |
| 9 | FLA | +0.22 | +0.00 | +0.22 | 2.65 | 2.44 | 9.17 | 7.46 | 1503 |
| 10 | NJD | +0.21 | +0.02 | +0.20 | 2.84 | 2.44 | 9.06 | 7.79 | 1504 |
| 11 | BUF | +0.12 | +0.11 | +0.01 | 2.81 | 2.69 | 7.80 | 8.44 | 1518 |
| 12 | STL | +0.08 | -0.01 | +0.10 | 2.65 | 2.61 | 7.00 | 7.42 | 1505 |
| 13 | EDM | +0.07 | +0.12 | -0.05 | 2.61 | 2.76 | 9.89 | 8.16 | 1523 |
| 14 | BOS | +0.05 | +0.07 | -0.02 | 2.83 | 2.78 | 7.76 | 8.13 | 1528 |
| 15 | WSH | +0.04 | +0.11 | -0.06 | 2.88 | 2.80 | 7.78 | 8.10 | 1523 |
| 16 | NYR | +0.03 | +0.03 | +0.00 | 2.73 | 2.73 | 8.62 | 7.76 | 1493 |
| 17 | OTT | +0.01 | -0.06 | +0.08 | 2.60 | 2.62 | 7.95 | 8.32 | 1514 |
| 18 | LAK | +0.01 | -0.12 | +0.13 | 2.56 | 2.57 | 8.18 | 8.13 | 1474 |
| 19 | DET | -0.00 | -0.09 | +0.08 | 2.69 | 2.59 | 8.42 | 8.63 | 1485 |
| 20 | MTL | -0.05 | +0.04 | -0.09 | 2.85 | 2.84 | 7.11 | 8.32 | 1532 |
| 21 | NYI | -0.08 | -0.05 | -0.03 | 2.73 | 2.78 | 7.62 | 8.65 | 1496 |
| 22 | WPG | -0.11 | -0.11 | +0.00 | 2.60 | 2.74 | 7.99 | 8.70 | 1469 |
| 23 | TOR | -0.12 | -0.01 | -0.11 | 2.51 | 2.84 | 8.75 | 8.19 | 1482 |
| 24 | CBJ | -0.12 | -0.09 | -0.03 | 2.60 | 2.74 | 7.71 | 8.43 | 1491 |
| 25 | NSH | -0.14 | -0.07 | -0.06 | 2.62 | 2.79 | 7.85 | 7.60 | 1479 |
| 26 | CGY | -0.24 | -0.10 | -0.14 | 2.66 | 2.88 | 7.31 | 8.23 | 1462 |
| 27 | SEA | -0.27 | -0.10 | -0.17 | 2.45 | 2.92 | 7.32 | 8.52 | 1485 |
| 28 | PHI | -0.32 | -0.27 | -0.04 | 2.35 | 2.76 | 7.77 | 7.60 | 1471 |
| 29 | ANA | -0.37 | -0.02 | -0.35 | 2.76 | 3.09 | 7.94 | 8.57 | 1474 |
| 30 | VAN | -0.71 | -0.21 | -0.50 | 2.32 | 3.25 | 7.61 | 8.74 | 1415 |
| 31 | CHI | -0.76 | -0.29 | -0.47 | 2.33 | 3.22 | 7.16 | 8.36 | 1432 |
| 32 | SJS | -0.76 | -0.22 | -0.53 | 2.36 | 3.30 | 7.32 | 8.78 | 1467 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| WSH | Logan Thompson | 63% | +0.45 | +0.19 |
| NYI | Ilya Sorokin | 67% | +0.40 | +0.17 |
| MTL | Jacob Fowler | 57% | +0.31 | +0.13 |
| BOS | Jeremy Swayman | 79% | +0.31 | +0.13 |
| CGY | Devin Cooley | 67% | +0.20 | +0.09 |
| MIN | Jesper Wallstedt | 85% | +0.16 | +0.07 |
| COL | Mackenzie Blackwood | 67% | +0.15 | +0.06 |
| TBL | Andrei Vasilevskiy | 73% | +0.14 | +0.06 |
| OTT | Linus Ullmark | 49% | +0.14 | +0.06 |
| CHI | Spencer Knight | 89% | +0.14 | +0.06 |
| DAL | Jake Oettinger | 77% | +0.11 | +0.05 |
| CBJ | Jet Greaves | 51% | +0.10 | +0.04 |
| STL | Joel Hofer | 70% | +0.04 | +0.02 |
| CAR | Pyotr Kochetkov | 66% | -0.02 | -0.01 |
| NYR | Dylan Garand | 63% | -0.06 | -0.03 |
| NJD | Jake Allen | 61% | -0.06 | -0.03 |
| PHI | Joseph Woll | 54% | -0.08 | -0.03 |
| DET | John Gibson | 67% | -0.11 | -0.05 |
| SEA | Philipp Grubauer | 58% | -0.13 | -0.05 |
| SJS | Yaroslav Askarov | 63% | -0.14 | -0.06 |
| WPG | Clay Stevenson | 53% | -0.15 | -0.06 |
| UTA | Karel Vejmelka | 70% | -0.16 | -0.07 |
| BUF | Ukko-Pekka Luukkonen | 58% | -0.17 | -0.07 |
| TOR | Sergei Bobrovsky | 68% | -0.17 | -0.07 |
| ANA | Lukas Dostal | 65% | -0.17 | -0.07 |
| FLA | Akira Schmid | 52% | -0.18 | -0.07 |
| VGK | Carter Hart | 54% | -0.18 | -0.08 |
| LAK | Darcy Kuemper | 65% | -0.21 | -0.09 |
| NSH | Juuse Saros | 74% | -0.25 | -0.10 |
| PIT | Arturs Silovs | 73% | -0.29 | -0.12 |
| VAN | Leevi Meriläinen | 61% | -0.30 | -0.12 |
| EDM | Tristan Jarry | 52% | -0.37 | -0.16 |

## Current model fit

- Fitted on 5805 games from 2022-23 to 2026-27.
- Home ice: +3.1% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.7% goals scored, +3.3% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 23%.
- Blend: 42% on the betting line wherever there is one (fitted on 79 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
