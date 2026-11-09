# NHL score predictions

Updated Mon Nov 09, 2026 02:16 AM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Monday, November 9

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8:00 PM | NYR @ EDM | NYR 3, EDM 4 | EDM 57% | NYR +135 / EDM -135 | 3.0 – 3.5 | 1–5 / 1–6 | 22% | EDM -1.5 36% | 6.5 / 6.5 (over 50%) | Joonas Korpisalo (expected) / Devon Levi (expected) | NYR +130 / EDM -155 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:30 PM | PHI @ VAN | PHI 4, VAN 3 | PHI 56% | PHI -125 / VAN +125 | 3.3 – 2.9 | 1–6 / 1–5 | 23% | PHI -1.5 34% | 6.2 / 6.5 (over 46%) | Joseph Woll (expected) / Leevi Meriläinen (expected) | PHI -135 / VAN +114 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | NYI @ SJS | NYI 4, SJS 3 | NYI 60% | NYI -150 / SJS +150 | 3.6 – 2.9 | 1–6 / 1–5 | 21% | NYI -1.5 39% | 6.5 / 6.5 (over 51%) | Ilya Sorokin (expected) / Yaroslav Askarov (expected) | NYI -135 / SJS +114 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Tuesday, November 10

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | COL @ TOR | COL 4, TOR 3 | COL 59% | COL -145 / TOR +145 | 3.7 – 3.0 | 1–6 / 1–5 | 21% | COL -1.5 39% | 6.7 | Mackenzie Blackwood (expected) / Sergei Bobrovsky (expected) | – | no line yet (model fair TOR +1.5 -155 / COL -1.5 +155) | no line yet | no line yet |
| 7:00 PM | MIN @ MTL | MIN 3, MTL 2 | MIN 54% | MIN -115 / MTL +115 | 3.2 – 2.9 | 1–5 / 1–5 | 23% | MIN -1.5 32% | 6.1 | Jesper Wallstedt (expected) / Jacob Fowler (expected) | – | no line yet (model fair MTL +1.5 -215 / MIN -1.5 +215) | no line yet | no line yet |
| 7:00 PM | WSH @ OTT | WSH 3, OTT 4 | OTT 51% | WSH +105 / OTT -105 | 3.1 – 3.1 | 1–5 / 1–5 | 23% | OTT -1.5 30% | 6.2 | Logan Thompson (expected) / Linus Ullmark (expected) | – | no line yet (model fair OTT -1.5 +230 / WSH +1.5 -230) | no line yet | no line yet |
| 7:00 PM | NJD @ WPG | NJD 3, WPG 2 | NJD 56% | NJD -125 / WPG +125 | 3.3 – 2.9 | 1–6 / 1–5 | 23% | NJD -1.5 34% | 6.2 | Jake Allen (expected) / Stuart Skinner (expected) | – | no line yet (model fair WPG +1.5 -190 / NJD -1.5 +190) | no line yet | no line yet |
| 7:30 PM | FLA @ CBJ | FLA 3, CBJ 2 | FLA 51% | FLA -105 / CBJ +105 | 3.1 – 3.0 | 1–5 / 1–5 | 23% | FLA -1.5 29% | 6.1 | Jacob Markstrom (expected) / Jet Greaves (expected) | – | no line yet (model fair CBJ +1.5 -240 / FLA -1.5 +240) | no line yet | no line yet |
| 8:00 PM | DET @ STL | DET 2, STL 3 | STL 57% | DET +135 / STL -135 | 2.8 – 3.3 | 1–5 / 1–6 | 22% | STL -1.5 35% | 6.1 | John Gibson (expected) / Joel Hofer (expected) | – | no line yet (model fair STL -1.5 +190 / DET +1.5 -190) | no line yet | no line yet |
| 10:00 PM | NSH @ LAK | NSH 2, LAK 3 | LAK 53% | NSH +115 / LAK -115 | 2.9 – 3.2 | 1–5 / 1–6 | 23% | LAK -1.5 32% | 6.1 | Juuse Saros (expected) / Darcy Kuemper (expected) | – | no line yet (model fair LAK -1.5 +215 / NSH +1.5 -215) | no line yet | no line yet |

\* price not posted; assumed -110.

## Wednesday, November 11

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | TBL @ BUF | TBL 4, BUF 3 | TBL 55% | TBL -125 / BUF +125 | 3.4 – 3.0 | 1–6 / 1–5 | 21% | TBL -1.5 34% | 6.4 | Andrei Vasilevskiy (expected) / Ukko-Pekka Luukkonen (expected) | – | no line yet (model fair BUF +1.5 -190 / TBL -1.5 +190) | no line yet | no line yet |
| 7:30 PM | NYR @ CGY | NYR 4, CGY 3 | NYR 55% | NYR -120 / CGY +120 | 3.4 – 3.1 | 1–6 / 1–6 | 21% | NYR -1.5 35% | 6.6 | Dylan Garand (expected) / Dustin Wolf (expected) | – | no line yet (model fair CGY +1.5 -190 / NYR -1.5 +190) | no line yet | no line yet |
| 9:00 PM | PHI @ EDM | PHI 2, EDM 3 | EDM 60% | PHI +150 / EDM -150 | 2.7 – 3.3 | 1–5 / 1–6 | 23% | EDM -1.5 37% | 6.1 | Dan Vladar (expected) / Devon Levi (expected) | – | no line yet (model fair EDM -1.5 +170 / PHI +1.5 -170) | no line yet | no line yet |
| 9:30 PM | UTA @ VGK | UTA 2, VGK 3 | VGK 52% | UTA +105 / VGK -105 | 3.0 – 3.2 | 1–5 / 1–6 | 22% | VGK -1.5 32% | 6.2 | Karel Vejmelka (expected) / Carter Hart (expected) | – | no line yet (model fair VGK -1.5 +215 / UTA +1.5 -215) | no line yet | no line yet |
| 10:00 PM | NSH @ ANA | NSH 3, ANA 4 | ANA 52% | NSH +110 / ANA -110 | 3.2 – 3.4 | 1–6 / 1–6 | 21% | ANA -1.5 32% | 6.6 | Justus Annunen (expected) / Laurent Brossoit (expected) | – | no line yet (model fair ANA -1.5 +210 / NSH +1.5 -210) | no line yet | no line yet |
| 10:00 PM | PIT @ SJS | PIT 4, SJS 3 | PIT 65% | PIT -190 / SJS +190 | 4.0 – 2.9 | 1–7 / 1–5 | 20% | PIT -1.5 45% | 6.9 | Arturs Silovs (expected) / Yaroslav Askarov (expected) | – | no line yet (model fair SJS +1.5 -120 / PIT -1.5 +120) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 276 | 0.6438 | 0.2262 | 62.0% | 1.37 | 1.79 | 90.0% |
| Model only (before blending) | 276 | 0.6466 | 0.2277 | 60.5% | – | – | – |
| Elo | 276 | 0.6603 | 0.2339 | 61.6% | – | – | – |
| Final prediction, games with a line | 142 | 0.6421 | 0.2255 | 60.6% | 1.34 | 1.83 | 90.5% |
| Model only, games with a line | 142 | 0.6475 | 0.2283 | 57.7% | – | – | – |
| Betting market (de-vigged moneyline) | 142 | 0.6419 | 0.2254 | 61.3% | – | 1.81 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.5% of regular-season games, happened in 22.1%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 1 | 0-1-0 | 1.3 | -1.29 | -100.0% | +11.8% |
| Moneyline | 8 | 4-4-0 | 8.7 | +1.83 | +21.2% | +6.4% |
| Total | 1 | 0-1-0 | 0.9 | -0.89 | -100.0% | +3.0% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 26 of 31 games (84%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Saturday, November 7

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| FLA @ WSH | 3–4 | 3–4 | 53% | yes | Jacob Markstrom / Logan Thompson |
| STL @ NSH | 3–2 | 1–3 | 49% | yes | Joel Hofer / Juuse Saros |
| NYR @ SEA | 4–3 | 4–3 | 56% | yes | Joonas Korpisalo / Philipp Grubauer |
| MTL @ TOR | 4–3 | 4–2 | 52% | yes | Jacob Fowler / Sergei Bobrovsky |
| UTA @ OTT | 4–3 | 2–4 | 45% | yes | Karel Vejmelka / Samuel Ersson |
| NJD @ NYI | 3–2 | 5–4 (OT) | 56% | yes | Jake Allen / Ilya Sorokin |
| CHI @ CAR | 2–5 | 2–9 | 79% | no | Spencer Knight / Pyotr Kochetkov |
| SJS @ DAL | 2–3 | 3–4 | 74% | yes | Alex Nedeljkovic / Jake Oettinger |
| TBL @ MIN | 4–3 | 4–3 (OT) | 55% | yes | Dennis Hildeby / Calvin Pickard |
| DET @ COL | 3–4 | 0–4 | 64% | no | Daniil Tarasov / Mackenzie Blackwood |
| PIT @ LAK | 3–4 | 5–2 | 49% | yes | Sergei Murashov / Darcy Kuemper |
| VAN @ EDM | 3–4 | 2–4 | 73% | yes | Leevi Meriläinen / Devon Levi |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.78 | +0.49 | +0.29 | 3.48 | 2.38 | 8.66 | 7.26 | 1585 |
| 2 | UTA | +0.45 | +0.24 | +0.21 | 3.17 | 2.39 | 8.24 | 8.79 | 1506 |
| 3 | TBL | +0.42 | +0.20 | +0.22 | 2.95 | 2.44 | 8.31 | 7.90 | 1547 |
| 4 | VGK | +0.33 | +0.04 | +0.29 | 2.70 | 2.35 | 9.21 | 7.36 | 1530 |
| 5 | MIN | +0.27 | +0.09 | +0.18 | 2.88 | 2.53 | 9.31 | 8.16 | 1549 |
| 6 | COL | +0.24 | +0.27 | -0.03 | 2.97 | 2.79 | 7.83 | 8.03 | 1549 |
| 7 | NJD | +0.24 | +0.07 | +0.17 | 2.90 | 2.47 | 9.21 | 7.95 | 1518 |
| 8 | PIT | +0.24 | +0.18 | +0.06 | 3.00 | 2.61 | 7.88 | 7.96 | 1492 |
| 9 | DAL | +0.23 | -0.08 | +0.30 | 2.54 | 2.35 | 9.65 | 7.43 | 1529 |
| 10 | FLA | +0.17 | -0.02 | +0.20 | 2.59 | 2.47 | 9.60 | 7.84 | 1502 |
| 11 | STL | +0.10 | +0.01 | +0.10 | 2.70 | 2.60 | 7.05 | 7.78 | 1497 |
| 12 | EDM | +0.10 | +0.08 | +0.02 | 2.57 | 2.68 | 9.72 | 8.18 | 1531 |
| 13 | OTT | +0.09 | -0.02 | +0.11 | 2.71 | 2.57 | 8.16 | 8.34 | 1521 |
| 14 | BUF | +0.09 | +0.11 | -0.02 | 2.84 | 2.73 | 8.16 | 8.52 | 1522 |
| 15 | WSH | +0.09 | +0.14 | -0.06 | 2.96 | 2.78 | 7.95 | 8.17 | 1516 |
| 16 | LAK | +0.05 | -0.10 | +0.15 | 2.59 | 2.53 | 8.38 | 8.28 | 1471 |
| 17 | NYR | +0.02 | +0.03 | -0.01 | 2.76 | 2.75 | 8.83 | 7.92 | 1497 |
| 18 | BOS | +0.02 | +0.04 | -0.02 | 2.74 | 2.78 | 7.85 | 8.20 | 1539 |
| 19 | MTL | -0.05 | +0.06 | -0.11 | 2.83 | 2.87 | 7.64 | 8.56 | 1537 |
| 20 | DET | -0.05 | -0.10 | +0.05 | 2.67 | 2.63 | 8.44 | 8.84 | 1477 |
| 21 | CBJ | -0.09 | -0.03 | -0.06 | 2.74 | 2.78 | 7.77 | 8.78 | 1494 |
| 22 | NSH | -0.11 | -0.08 | -0.04 | 2.61 | 2.77 | 8.40 | 7.80 | 1496 |
| 23 | WPG | -0.13 | -0.12 | -0.01 | 2.57 | 2.74 | 8.29 | 9.14 | 1468 |
| 24 | TOR | -0.14 | -0.03 | -0.11 | 2.51 | 2.84 | 8.87 | 8.51 | 1479 |
| 25 | NYI | -0.14 | -0.02 | -0.13 | 2.83 | 2.90 | 7.64 | 8.65 | 1483 |
| 26 | CGY | -0.24 | -0.12 | -0.11 | 2.59 | 2.85 | 7.36 | 8.13 | 1461 |
| 27 | PHI | -0.26 | -0.25 | -0.00 | 2.38 | 2.71 | 7.83 | 7.52 | 1471 |
| 28 | SEA | -0.31 | -0.12 | -0.19 | 2.45 | 2.93 | 7.31 | 8.71 | 1478 |
| 29 | ANA | -0.35 | +0.01 | -0.36 | 2.72 | 3.09 | 8.09 | 8.57 | 1490 |
| 30 | CHI | -0.69 | -0.30 | -0.39 | 2.31 | 3.12 | 7.27 | 8.55 | 1416 |
| 31 | VAN | -0.70 | -0.26 | -0.45 | 2.24 | 3.17 | 7.76 | 8.79 | 1402 |
| 32 | SJS | -0.77 | -0.25 | -0.52 | 2.35 | 3.26 | 7.38 | 9.39 | 1447 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 67% | +0.39 | +0.16 |
| WSH | Logan Thompson | 75% | +0.37 | +0.16 |
| MTL | Jacob Fowler | 64% | +0.34 | +0.14 |
| BOS | Jeremy Swayman | 66% | +0.32 | +0.13 |
| MIN | Jesper Wallstedt | 81% | +0.25 | +0.11 |
| COL | Mackenzie Blackwood | 73% | +0.21 | +0.09 |
| TBL | Andrei Vasilevskiy | 73% | +0.15 | +0.06 |
| CBJ | Jet Greaves | 50% | +0.11 | +0.05 |
| DAL | Jake Oettinger | 76% | +0.09 | +0.04 |
| STL | Joel Hofer | 71% | +0.05 | +0.02 |
| CAR | Pyotr Kochetkov | 69% | +0.04 | +0.02 |
| CHI | Spencer Knight | 77% | +0.03 | +0.01 |
| NYR | Dylan Garand | 66% | +0.01 | +0.00 |
| WPG | Stuart Skinner | 73% | -0.04 | -0.02 |
| PHI | Dan Vladar | 51% | -0.04 | -0.02 |
| NJD | Jake Allen | 49% | -0.07 | -0.03 |
| BUF | Ukko-Pekka Luukkonen | 60% | -0.10 | -0.04 |
| VGK | Carter Hart | 53% | -0.12 | -0.05 |
| FLA | Akira Schmid | 52% | -0.15 | -0.06 |
| NSH | Juuse Saros | 66% | -0.16 | -0.07 |
| TOR | Sergei Bobrovsky | 69% | -0.16 | -0.07 |
| DET | John Gibson | 55% | -0.17 | -0.07 |
| SEA | Joey Daccord | 51% | -0.19 | -0.08 |
| ANA | Lukas Dostal | 51% | -0.20 | -0.08 |
| SJS | Yaroslav Askarov | 62% | -0.21 | -0.09 |
| UTA | Karel Vejmelka | 63% | -0.22 | -0.09 |
| LAK | Darcy Kuemper | 67% | -0.23 | -0.10 |
| CGY | Dustin Wolf | 54% | -0.25 | -0.11 |
| EDM | Tristan Jarry | 46% | -0.31 | -0.13 |
| PIT | Arturs Silovs | 64% | -0.37 | -0.15 |
| VAN | Leevi Meriläinen | 66% | -0.38 | -0.16 |
| OTT | Samuel Ersson | 40% | -0.48 | -0.20 |

## Current model fit

- Fitted on 5868 games from 2022-23 to 2026-27.
- Home ice: +3.1% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.8% goals scored, +3.4% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 22%.
- Blend: 47% on the betting line wherever there is one (fitted on 142 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.04 goals per five minutes.
