# NHL score predictions

Updated Fri Oct 23, 2026 09:01 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Saturday, October 24

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1:00 PM | ANA @ PHI | ANA 3, PHI 4 | PHI 52% | ANA +110 / PHI -110 | 3.0 – 3.2 | 1–5 / 1–6 | 22% | PHI -1.5 32% | 6.2 / 5.5 (over 56%) | Lukas Dostal (expected) / Joseph Woll (expected) | ANA +102 / PHI -122 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 3:30 PM | LAK @ NJD | LAK 2, NJD 3 | NJD 57% | LAK +130 / NJD -130 | 2.7 – 3.2 | 1–5 / 1–6 | 22% | NJD -1.5 35% | 5.9 / 5.5 (over 50%) | Darcy Kuemper (expected) / Jake Allen (expected) | LAK +140 / NJD -166 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | SJS @ BOS | SJS 3, BOS 4 | BOS 65% | SJS +185 / BOS -185 | 2.7 – 3.7 | 1–5 / 1–6 | 21% | BOS -1.5 44% | 6.5 / 6.5 (over 49%) | Yaroslav Askarov (expected) / Jeremy Swayman (expected) | SJS +160 / BOS -192 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | NYR @ OTT | NYR 2, OTT 3 | OTT 52% | NYR +105 / OTT -105 | 3.0 – 3.1 | 1–5 / 1–6 | 22% | OTT -1.5 31% | 6.2 / 5.5 (over 56%) | Dylan Garand (expected) / Jonas Johansson (expected) | NYR +102 / OTT -122 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | NSH @ PIT | NSH 3, PIT 4 | PIT 58% | NSH +140 / PIT -140 | 3.0 – 3.6 | 1–5 / 1–6 | 22% | PIT -1.5 38% | 6.6 / 6.5 (over 52%) | Juuse Saros (expected) / Arturs Silovs (expected) | NSH +114 / PIT -135 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | BUF @ WSH | BUF 3, WSH 4 | WSH 52% | BUF +105 / WSH -105 | 3.3 – 3.4 | 1–6 / 1–6 | 21% | WSH -1.5 32% | 6.6 / 6.5 (over 52%) | Ukko-Pekka Luukkonen (expected) / Charlie Lindgren (expected) | BUF +105 / WSH -125 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | VGK @ CBJ | VGK 3, CBJ 2 | VGK 52% | VGK -110 / CBJ +110 | 3.1 – 3.0 | 1–5 / 1–5 | 22% | VGK -1.5 31% | 6.1 / 6.5 (over 43%) | Carter Hart (expected) / Jet Greaves (expected) | VGK -135 / CBJ +114 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | CAR @ STL | CAR 4, STL 3 | CAR 58% | CAR -140 / STL +140 | 3.4 – 2.9 | 1–6 / 1–5 | 23% | CAR -1.5 36% | 6.2 / 6.5 (over 46%) | Pyotr Kochetkov (expected) / Joel Hofer (expected) | CAR -155 / STL +130 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | TOR @ EDM | TOR 3, EDM 4 | EDM 60% | TOR +155 / EDM -155 | 3.1 – 3.8 | 1–5 / 1–6 | 21% | EDM -1.5 40% | 6.9 / 6.5 (over 55%) | Sergei Bobrovsky (expected) / Tristan Jarry (confirmed) | TOR +154 / EDM -185 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:00 PM | TBL @ UTA | TBL 3, UTA 4 | UTA 58% | TBL +135 / UTA -135 | 2.9 – 3.4 | 1–5 / 1–6 | 21% | UTA -1.5 36% | 6.3 / 6.5 (over 47%) | Dennis Hildeby (expected) / Karel Vejmelka (expected) | TBL +120 / UTA -142 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | DET @ CGY | DET 4, CGY 3 | DET 55% | DET -120 / CGY +120 | 3.3 – 3.0 | 1–6 / 1–5 | 22% | DET -1.5 34% | 6.3 / 5.5 (over 57%) | John Gibson (expected) / Dustin Wolf (expected) | DET -148 / CGY +124 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | MIN @ SEA | MIN 4, SEA 3 | MIN 60% | MIN -145 / SEA +145 | 3.5 – 2.9 | 1–6 / 1–5 | 21% | MIN -1.5 38% | 6.3 / 6.5 (over 47%) | Jesper Wallstedt (expected) / Philipp Grubauer (expected) | MIN -155 / SEA +130 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Sunday, October 25

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3:00 PM | FLA @ CHI | FLA 3, CHI 2 | FLA 62% | FLA -165 / CHI +165 | 3.5 – 2.7 | 1–6 / 1–5 | 22% | FLA -1.5 41% | 6.2 | Akira Schmid (expected) / Spencer Knight (expected) | – | no line yet (model fair CHI +1.5 -145 / FLA -1.5 +145) | no line yet | no line yet |
| 6:00 PM | NYI @ DAL | NYI 2, DAL 3 | DAL 59% | NYI +140 / DAL -140 | 2.6 – 3.1 | 1–5 / 1–5 | 23% | DAL -1.5 36% | 5.7 | Ilya Sorokin (expected) / Jake Oettinger (expected) | – | no line yet (model fair DAL -1.5 +175 / NYI +1.5 -175) | no line yet | no line yet |
| 7:00 PM | MTL @ WPG | MTL 4, WPG 3 | MTL 51% | MTL -105 / WPG +105 | 3.2 – 3.1 | 1–6 / 1–6 | 22% | MTL -1.5 31% | 6.3 | Jakub Dobes (expected) / Stuart Skinner (expected) | – | no line yet (model fair WPG +1.5 -225 / MTL -1.5 +225) | no line yet | no line yet |
| 8:00 PM | COL @ NSH | COL 4, NSH 3 | COL 64% | COL -180 / NSH +180 | 3.7 – 2.8 | 1–6 / 1–5 | 21% | COL -1.5 43% | 6.4 | Mackenzie Blackwood (expected) / Justus Annunen (expected) | – | no line yet (model fair NSH +1.5 -135 / COL -1.5 +135) | no line yet | no line yet |
| 10:00 PM | MIN @ VAN | MIN 4, VAN 3 | MIN 63% | MIN -170 / VAN +170 | 3.7 – 2.9 | 1–6 / 1–5 | 20% | MIN -1.5 42% | 6.6 | Calvin Pickard (expected) / Leevi Meriläinen (expected) | – | no line yet (model fair VAN +1.5 -135 / MIN -1.5 +135) | no line yet | no line yet |

\* price not posted; assumed -110.

## Monday, October 26

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | LAK @ NYR | LAK 2, NYR 3 | NYR 54% | LAK +115 / NYR -115 | 2.9 – 3.1 | 1–5 / 1–6 | 22% | NYR -1.5 33% | 6.0 | Darcy Kuemper (expected) / Dylan Garand (expected) | – | no line yet (model fair NYR -1.5 +205 / LAK +1.5 -205) | no line yet | no line yet |
| 8:30 PM | TOR @ CGY | TOR 4, CGY 3 | TOR 53% | TOR -110 / CGY +110 | 3.3 – 3.2 | 1–6 / 1–6 | 21% | TOR -1.5 32% | 6.5 | Sergei Bobrovsky (expected) / Dustin Wolf (expected) | – | no line yet (model fair CGY +1.5 -210 / TOR -1.5 +210) | no line yet | no line yet |
| 9:30 PM | DET @ EDM | DET 3, EDM 4 | EDM 57% | DET +135 / EDM -135 | 3.0 – 3.5 | 1–5 / 1–6 | 22% | EDM -1.5 36% | 6.5 | John Gibson (expected) / Tristan Jarry (expected) | – | no line yet (model fair EDM -1.5 +175 / DET +1.5 -175) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 165 | 0.6552 | 0.2316 | 61.2% | 1.38 | 1.72 | 89.7% |
| Model only (before blending) | 165 | 0.6562 | 0.2321 | 61.2% | – | – | – |
| Elo | 165 | 0.6675 | 0.2373 | 61.8% | – | – | – |
| Final prediction, games with a line | 31 | 0.6971 | 0.2517 | 51.6% | 1.34 | 1.60 | 90.3% |
| Model only, games with a line | 31 | 0.7026 | 0.2546 | 51.6% | – | – | – |
| Betting market (de-vigged moneyline) | 31 | 0.6980 | 0.2521 | 51.6% | – | 1.50 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.6% of regular-season games, happened in 23.0%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Moneyline moved toward the model's edge on the first line seen before puck drop: 3 of 4 games (75%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Thursday, October 22

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| NSH @ BOS | 2–3 | 0–6 | 58% | no | Juuse Saros / Jeremy Swayman |
| NYR @ TOR | 4–3 | 4–5 | 49% | yes | Dylan Garand / Sergei Bobrovsky |
| SJS @ OTT | 3–4 | 6–2 | 44% | no | Yaroslav Askarov / Samuel Ersson |
| ANA @ NJD | 3–4 | 1–4 | 63% | yes | Lukas Dostal / Jake Allen |
| FLA @ PIT | 3–4 | 0–4 | 53% | no | Jacob Markstrom / Sergei Murashov |
| LAK @ NYI | 2–3 | 3–2 (OT) | 48% | yes | Darcy Kuemper / Ilya Sorokin |
| VGK @ STL | 3–2 | 2–6 | 49% | no | Carter Hart / Joel Hofer |
| WPG @ DAL | 2–3 | 2–3 (OT) | 62% | yes | Stuart Skinner / Jake Oettinger |
| MIN @ CGY | 4–3 | 1–2 | 37% | yes | Jesper Wallstedt / Dustin Wolf |
| CAR @ EDM | 4–3 | 5–6 (SO) | 46% | yes | Brandon Bussi / Devon Levi |
| UTA @ SEA | 4–3 | 3–5 | 38% | yes | Karel Vejmelka / Joey Daccord |
| DET @ VAN | 4–3 | 5–2 | 62% | yes | John Gibson / Kevin Lankinen |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.64 | +0.41 | +0.24 | 3.40 | 2.44 | 8.07 | 6.77 | 1570 |
| 2 | UTA | +0.51 | +0.26 | +0.25 | 3.18 | 2.35 | 8.02 | 8.13 | 1514 |
| 3 | TBL | +0.31 | +0.15 | +0.16 | 2.88 | 2.53 | 7.78 | 7.78 | 1545 |
| 4 | COL | +0.29 | +0.27 | +0.02 | 3.00 | 2.74 | 7.64 | 7.74 | 1547 |
| 5 | VGK | +0.29 | +0.10 | +0.20 | 2.75 | 2.47 | 8.73 | 7.27 | 1532 |
| 6 | PIT | +0.27 | +0.22 | +0.05 | 3.06 | 2.63 | 7.88 | 7.67 | 1498 |
| 7 | MIN | +0.26 | +0.09 | +0.17 | 2.94 | 2.51 | 8.92 | 8.21 | 1527 |
| 8 | NJD | +0.26 | +0.05 | +0.20 | 2.95 | 2.42 | 8.74 | 7.63 | 1497 |
| 9 | FLA | +0.25 | -0.00 | +0.25 | 2.67 | 2.39 | 8.93 | 7.30 | 1493 |
| 10 | DAL | +0.19 | -0.08 | +0.27 | 2.55 | 2.40 | 9.10 | 7.20 | 1533 |
| 11 | EDM | +0.13 | +0.16 | -0.03 | 2.68 | 2.73 | 9.62 | 8.24 | 1530 |
| 12 | STL | +0.10 | -0.02 | +0.12 | 2.57 | 2.56 | 7.02 | 7.38 | 1510 |
| 13 | OTT | +0.08 | -0.06 | +0.15 | 2.63 | 2.53 | 7.80 | 7.70 | 1517 |
| 14 | LAK | +0.08 | -0.11 | +0.19 | 2.60 | 2.49 | 7.69 | 7.81 | 1470 |
| 15 | BUF | +0.07 | +0.07 | -0.00 | 2.76 | 2.69 | 7.59 | 8.26 | 1513 |
| 16 | NYR | +0.00 | -0.01 | +0.01 | 2.65 | 2.73 | 8.36 | 7.59 | 1504 |
| 17 | NYI | -0.01 | -0.05 | +0.03 | 2.76 | 2.71 | 7.52 | 8.68 | 1494 |
| 18 | BOS | -0.03 | +0.03 | -0.07 | 2.72 | 2.86 | 7.69 | 8.09 | 1533 |
| 19 | CBJ | -0.04 | -0.03 | -0.01 | 2.75 | 2.70 | 7.58 | 8.49 | 1487 |
| 20 | WSH | -0.05 | +0.09 | -0.14 | 2.88 | 2.90 | 7.66 | 8.14 | 1514 |
| 21 | DET | -0.06 | -0.08 | +0.02 | 2.67 | 2.67 | 8.51 | 8.33 | 1483 |
| 22 | MTL | -0.07 | +0.05 | -0.12 | 2.87 | 2.86 | 7.11 | 8.31 | 1514 |
| 23 | WPG | -0.10 | -0.08 | -0.02 | 2.62 | 2.78 | 7.83 | 7.96 | 1481 |
| 24 | TOR | -0.13 | -0.01 | -0.12 | 2.54 | 2.85 | 8.60 | 8.21 | 1481 |
| 25 | NSH | -0.23 | -0.12 | -0.11 | 2.55 | 2.85 | 7.81 | 7.60 | 1479 |
| 26 | CGY | -0.24 | -0.08 | -0.16 | 2.68 | 2.89 | 7.29 | 8.12 | 1456 |
| 27 | SEA | -0.27 | -0.07 | -0.20 | 2.51 | 2.95 | 7.33 | 8.22 | 1488 |
| 28 | ANA | -0.34 | -0.02 | -0.32 | 2.82 | 3.05 | 7.48 | 8.39 | 1477 |
| 29 | PHI | -0.37 | -0.31 | -0.06 | 2.24 | 2.80 | 7.99 | 7.36 | 1481 |
| 30 | SJS | -0.52 | -0.18 | -0.34 | 2.45 | 3.07 | 7.31 | 8.64 | 1473 |
| 31 | CHI | -0.67 | -0.28 | -0.39 | 2.31 | 3.13 | 6.95 | 8.22 | 1440 |
| 32 | VAN | -0.71 | -0.21 | -0.49 | 2.29 | 3.24 | 7.48 | 8.60 | 1417 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 67% | +0.47 | +0.20 |
| WSH | Logan Thompson | 79% | +0.45 | +0.19 |
| BOS | Jeremy Swayman | 70% | +0.36 | +0.15 |
| TBL | Andrei Vasilevskiy | 76% | +0.24 | +0.10 |
| MTL | Jakub Dobes | 54% | +0.17 | +0.07 |
| DAL | Jake Oettinger | 82% | +0.17 | +0.07 |
| OTT | Linus Ullmark | 71% | +0.14 | +0.06 |
| MIN | Jesper Wallstedt | 91% | +0.13 | +0.06 |
| COL | Mackenzie Blackwood | 67% | +0.12 | +0.05 |
| CBJ | Jet Greaves | 61% | +0.11 | +0.05 |
| CHI | Spencer Knight | 81% | +0.06 | +0.02 |
| PHI | Dan Vladar | 52% | +0.02 | +0.01 |
| WPG | Stuart Skinner | 71% | +0.02 | +0.01 |
| STL | Joel Hofer | 72% | +0.02 | +0.01 |
| NYR | Dylan Garand | 67% | +0.02 | +0.01 |
| NJD | Jake Allen | 58% | -0.07 | -0.03 |
| EDM | Devon Levi | 72% | -0.07 | -0.03 |
| SEA | Philipp Grubauer | 60% | -0.08 | -0.03 |
| DET | John Gibson | 67% | -0.08 | -0.03 |
| CAR | Pyotr Kochetkov | 51% | -0.11 | -0.05 |
| ANA | Lukas Dostal | 65% | -0.13 | -0.05 |
| TOR | Sergei Bobrovsky | 68% | -0.13 | -0.05 |
| UTA | Karel Vejmelka | 73% | -0.16 | -0.07 |
| BUF | Ukko-Pekka Luukkonen | 72% | -0.17 | -0.07 |
| LAK | Darcy Kuemper | 76% | -0.17 | -0.07 |
| VGK | Carter Hart | 56% | -0.18 | -0.07 |
| NSH | Juuse Saros | 73% | -0.25 | -0.11 |
| SJS | Yaroslav Askarov | 60% | -0.25 | -0.11 |
| FLA | Jacob Markstrom | 49% | -0.26 | -0.11 |
| CGY | Dustin Wolf | 52% | -0.28 | -0.12 |
| PIT | Arturs Silovs | 64% | -0.30 | -0.13 |
| VAN | Kevin Lankinen | 56% | -0.63 | -0.27 |

## Current model fit

- Fitted on 5757 games from 2022-23 to 2026-27.
- Home ice: +3.2% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.8% goals scored, +3.2% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 23%.
- Blend: 40% on the betting line wherever there is one (fitted on 31 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
