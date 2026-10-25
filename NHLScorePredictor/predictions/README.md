# NHL score predictions

Updated Sun Oct 25, 2026 03:10 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Sunday, October 25

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6:00 PM | NYI @ DAL | NYI 2, DAL 3 | DAL 61% | NYI +160 / DAL -160 | 2.5 – 3.2 | 1–5 / 1–5 | 22% | DAL -1.5 38% | 5.7 / 5.5 (over 47%) | Ilya Sorokin (expected) / Jake Oettinger (expected) | NYI +164 / DAL -198 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | MTL @ WPG | MTL 3, WPG 2 | MTL 51% | MTL -105 / WPG +105 | 3.1 – 3.0 | 1–5 / 1–5 | 23% | MTL -1.5 30% | 6.1 / 5.5 (over 55%) | Jakub Dobes (expected) / Stuart Skinner (expected) | MTL -118 / WPG -102 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | COL @ NSH | COL 4, NSH 3 | COL 65% | COL -185 / NSH +185 | 3.7 – 2.8 | 1–6 / 1–5 | 20% | COL -1.5 44% | 6.5 / 6.5 (over 50%) | Scott Wedgewood (confirmed) / Justus Annunen (expected) | COL -238 / NSH +195 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | MIN @ VAN | MIN 4, VAN 3 | MIN 66% | MIN -190 / VAN +190 | 3.8 – 2.8 | 1–6 / 1–5 | 21% | MIN -1.5 44% | 6.6 / 6.5 (over 52%) | Calvin Pickard (confirmed) / Leevi Meriläinen (confirmed) | MIN -192 / VAN +160 | no edge | no edge | no edge |

## Monday, October 26

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | LAK @ NYR | LAK 2, NYR 3 | NYR 55% | LAK +125 / NYR -125 | 2.8 – 3.2 | 1–5 / 1–5 | 23% | NYR -1.5 33% | 6.0 / 5.5 (over 52%) | Darcy Kuemper (expected) / Dylan Garand (expected) | LAK +120 / NYR -142 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:30 PM | TOR @ CGY | TOR 4, CGY 3 | TOR 56% | TOR -130 / CGY +130 | 3.5 – 3.1 | 1–6 / 1–6 | 21% | TOR -1.5 36% | 6.7 / 6.5 (over 53%) | Sergei Bobrovsky (expected) / Dustin Wolf (expected) | TOR -162 / CGY +136 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:30 PM | DET @ EDM | DET 3, EDM 4 | EDM 57% | DET +135 / EDM -135 | 3.0 – 3.5 | 1–5 / 1–6 | 22% | EDM -1.5 37% | 6.5 / 6.5 (over 50%) | John Gibson (expected) / Tristan Jarry (expected) | DET +154 / EDM -185 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Tuesday, October 27

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | CBJ @ PHI | CBJ 3, PHI 2 | CBJ 54% | CBJ -120 / PHI +120 | 3.1 – 2.9 | 1–5 / 1–5 | 23% | CBJ -1.5 32% | 6.0 | Jet Greaves (expected) / Dan Vladar (expected) | – | no line yet (model fair PHI +1.5 -210 / CBJ -1.5 +210) | no line yet | no line yet |
| 8:00 PM | BOS @ CAR | BOS 3, CAR 4 | CAR 61% | BOS +160 / CAR -160 | 2.9 – 3.6 | 1–5 / 1–6 | 21% | CAR -1.5 40% | 6.4 | Jeremy Swayman (expected) / Pyotr Kochetkov (expected) | – | no line yet (model fair CAR -1.5 +150 / BOS +1.5 -150) | no line yet | no line yet |
| 8:00 PM | LAK @ CHI | LAK 3, CHI 2 | LAK 55% | LAK -125 / CHI +125 | 3.1 – 2.8 | 1–5 / 1–5 | 23% | LAK -1.5 33% | 5.8 | Anton Forsberg (expected) / Spencer Knight (expected) | – | no line yet (model fair CHI +1.5 -205 / LAK -1.5 +205) | no line yet | no line yet |
| 8:00 PM | MTL @ STL | MTL 3, STL 4 | STL 55% | MTL +120 / STL -120 | 2.9 – 3.2 | 1–5 / 1–6 | 23% | STL -1.5 34% | 6.2 | Jacob Fowler (expected) / Joel Hofer (expected) | – | no line yet (model fair STL -1.5 +200 / MTL +1.5 -200) | no line yet | no line yet |
| 8:00 PM | NYI @ NSH | NYI 3, NSH 2 | NYI 54% | NYI -115 / NSH +115 | 3.2 – 2.9 | 1–6 / 1–5 | 22% | NYI -1.5 33% | 6.1 | Ilya Sorokin (expected) / Juuse Saros (expected) | – | no line yet (model fair NSH +1.5 -200 / NYI -1.5 +200) | no line yet | no line yet |
| 8:00 PM | NJD @ DAL | NJD 2, DAL 3 | DAL 55% | NJD +120 / DAL -120 | 2.7 – 3.0 | 1–5 / 1–5 | 23% | DAL -1.5 33% | 5.7 | Jake Allen (expected) / Jake Oettinger (expected) | – | no line yet (model fair DAL -1.5 +205 / NJD +1.5 -205) | no line yet | no line yet |
| 8:00 PM | FLA @ WPG | FLA 3, WPG 2 | FLA 53% | FLA -110 / WPG +110 | 3.1 – 2.9 | 1–5 / 1–5 | 23% | FLA -1.5 31% | 6.0 | Akira Schmid (expected) / Stuart Skinner (expected) | – | no line yet (model fair WPG +1.5 -225 / FLA -1.5 +225) | no line yet | no line yet |
| 9:00 PM | MIN @ UTA | MIN 3, UTA 4 | UTA 54% | MIN +115 / UTA -115 | 3.0 – 3.3 | 1–5 / 1–6 | 23% | UTA -1.5 33% | 6.3 | Jesper Wallstedt (expected) / Karel Vejmelka (expected) | – | no line yet (model fair UTA -1.5 +205 / MIN +1.5 -205) | no line yet | no line yet |
| 10:00 PM | OTT @ VGK | OTT 2, VGK 3 | VGK 59% | OTT +140 / VGK -140 | 2.8 – 3.3 | 1–5 / 1–6 | 22% | VGK -1.5 36% | 6.1 | Samuel Ersson (expected) / Carter Hart (expected) | – | no line yet (model fair VGK -1.5 +175 / OTT +1.5 -175) | no line yet | no line yet |
| 10:00 PM | VAN @ ANA | VAN 3, ANA 4 | ANA 62% | VAN +160 / ANA -160 | 3.1 – 3.8 | 1–5 / 1–6 | 21% | ANA -1.5 41% | 6.9 | Leevi Meriläinen (expected) / Lukas Dostal (expected) | – | no line yet (model fair ANA -1.5 +145 / VAN +1.5 -145) | no line yet | no line yet |
| 10:30 PM | BUF @ SJS | BUF 4, SJS 3 | BUF 61% | BUF -160 / SJS +160 | 3.7 – 3.0 | 1–6 / 1–5 | 20% | BUF -1.5 40% | 6.7 | Ukko-Pekka Luukkonen (expected) / Yaroslav Askarov (expected) | – | no line yet (model fair SJS +1.5 -145 / BUF -1.5 +145) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 179 | 0.6527 | 0.2303 | 62.0% | 1.39 | 1.76 | 89.7% |
| Model only (before blending) | 179 | 0.6539 | 0.2310 | 61.5% | – | – | – |
| Elo | 179 | 0.6659 | 0.2366 | 63.1% | – | – | – |
| Final prediction, games with a line | 45 | 0.6741 | 0.2405 | 57.8% | 1.39 | 1.79 | 90.0% |
| Model only, games with a line | 45 | 0.6787 | 0.2429 | 55.6% | – | – | – |
| Betting market (de-vigged moneyline) | 45 | 0.6754 | 0.2411 | 57.8% | – | 1.72 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.6% of regular-season games, happened in 23.5%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 1 | 0-1-0 | 1.3 | -1.29 | -100.0% | +11.8% |
| Moneyline | 1 | 1-0-0 | 1.7 | +1.36 | +80.0% | +6.6% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Moneyline moved toward the model's edge on the first line seen before puck drop: 3 of 7 games (43%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Saturday, October 24

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| ANA @ PHI | 2–3 | 5–4 | 48% | yes | Lukas Dostal / Joseph Woll |
| LAK @ NJD | 2–3 | 1–3 | 60% | yes | Darcy Kuemper / Jake Allen |
| SJS @ BOS | 3–4 | 4–6 | 65% | yes | Alex Nedeljkovic / Jeremy Swayman |
| NYR @ OTT | 2–3 | 4–7 | 54% | no | Dylan Garand / Jonas Johansson |
| NSH @ PIT | 3–4 | 2–3 (OT) | 57% | yes | Juuse Saros / Arturs Silovs |
| BUF @ WSH | 3–4 | 3–4 (OT) | 51% | yes | Ukko-Pekka Luukkonen / Charlie Lindgren |
| VGK @ CBJ | 4–3 | 1–2 (OT) | 46% | yes | Carter Hart / Cam Talbot |
| CAR @ STL | 4–3 | 4–0 | 56% | no | Pyotr Kochetkov / Joel Hofer |
| TOR @ EDM | 3–4 | 7–2 | 40% | no | Sergei Bobrovsky / Tristan Jarry |
| TBL @ UTA | 3–4 | 4–5 (OT) | 58% | yes | Dennis Hildeby / Karel Vejmelka |
| DET @ CGY | 4–3 | 1–4 | 47% | yes | John Gibson / Devin Cooley |
| MIN @ SEA | 4–3 | 5–1 | 61% | yes | Jesper Wallstedt / Joey Daccord |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.67 | +0.43 | +0.25 | 3.44 | 2.43 | 8.11 | 6.80 | 1576 |
| 2 | UTA | +0.51 | +0.28 | +0.22 | 3.21 | 2.37 | 8.03 | 8.27 | 1516 |
| 3 | TBL | +0.34 | +0.19 | +0.16 | 2.94 | 2.52 | 7.81 | 7.81 | 1538 |
| 4 | VGK | +0.31 | +0.08 | +0.24 | 2.73 | 2.41 | 8.70 | 7.26 | 1529 |
| 5 | MIN | +0.31 | +0.11 | +0.20 | 2.98 | 2.47 | 9.09 | 8.18 | 1534 |
| 6 | NJD | +0.29 | +0.05 | +0.24 | 2.93 | 2.36 | 8.85 | 7.54 | 1500 |
| 7 | PIT | +0.27 | +0.23 | +0.04 | 3.09 | 2.64 | 7.92 | 7.65 | 1500 |
| 8 | COL | +0.27 | +0.27 | -0.00 | 2.96 | 2.76 | 7.67 | 7.66 | 1552 |
| 9 | FLA | +0.24 | -0.01 | +0.24 | 2.66 | 2.40 | 8.94 | 7.32 | 1493 |
| 10 | DAL | +0.19 | -0.08 | +0.27 | 2.54 | 2.41 | 9.12 | 7.23 | 1533 |
| 11 | OTT | +0.08 | -0.05 | +0.12 | 2.64 | 2.55 | 7.82 | 7.87 | 1522 |
| 12 | EDM | +0.07 | +0.14 | -0.07 | 2.65 | 2.77 | 9.62 | 8.27 | 1521 |
| 13 | BOS | +0.06 | +0.10 | -0.03 | 2.85 | 2.80 | 7.78 | 8.07 | 1536 |
| 14 | LAK | +0.06 | -0.14 | +0.19 | 2.53 | 2.47 | 7.62 | 7.93 | 1467 |
| 15 | BUF | +0.05 | +0.05 | -0.00 | 2.71 | 2.69 | 7.55 | 8.31 | 1511 |
| 16 | STL | +0.05 | -0.04 | +0.09 | 2.55 | 2.60 | 7.04 | 7.44 | 1504 |
| 17 | NYR | +0.02 | +0.02 | +0.01 | 2.69 | 2.73 | 8.53 | 7.61 | 1499 |
| 18 | WSH | +0.01 | +0.10 | -0.09 | 2.88 | 2.82 | 7.72 | 8.09 | 1516 |
| 19 | NYI | -0.01 | -0.05 | +0.03 | 2.76 | 2.71 | 7.54 | 8.70 | 1494 |
| 20 | MTL | -0.04 | +0.04 | -0.08 | 2.84 | 2.81 | 7.15 | 8.25 | 1519 |
| 21 | DET | -0.04 | -0.10 | +0.06 | 2.64 | 2.61 | 8.54 | 8.37 | 1478 |
| 22 | CBJ | -0.05 | -0.06 | +0.01 | 2.68 | 2.67 | 7.57 | 8.45 | 1490 |
| 23 | TOR | -0.08 | +0.03 | -0.11 | 2.58 | 2.84 | 8.63 | 8.22 | 1490 |
| 24 | WPG | -0.10 | -0.08 | -0.02 | 2.62 | 2.77 | 7.86 | 7.98 | 1481 |
| 25 | CGY | -0.24 | -0.10 | -0.14 | 2.61 | 2.87 | 7.34 | 8.15 | 1462 |
| 26 | NSH | -0.25 | -0.12 | -0.12 | 2.55 | 2.87 | 7.79 | 7.63 | 1477 |
| 27 | SEA | -0.33 | -0.09 | -0.24 | 2.48 | 2.99 | 7.28 | 8.42 | 1482 |
| 28 | ANA | -0.34 | -0.01 | -0.34 | 2.82 | 3.07 | 7.73 | 8.24 | 1480 |
| 29 | PHI | -0.36 | -0.30 | -0.06 | 2.26 | 2.78 | 7.83 | 7.57 | 1478 |
| 30 | SJS | -0.66 | -0.19 | -0.47 | 2.40 | 3.20 | 7.29 | 8.74 | 1470 |
| 31 | CHI | -0.68 | -0.31 | -0.37 | 2.26 | 3.10 | 6.89 | 8.25 | 1435 |
| 32 | VAN | -0.71 | -0.21 | -0.49 | 2.29 | 3.24 | 7.51 | 8.61 | 1417 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 67% | +0.47 | +0.20 |
| WSH | Logan Thompson | 68% | +0.46 | +0.19 |
| BOS | Jeremy Swayman | 73% | +0.32 | +0.13 |
| CGY | Devin Cooley | 56% | +0.20 | +0.08 |
| TBL | Andrei Vasilevskiy | 69% | +0.18 | +0.08 |
| DAL | Jake Oettinger | 82% | +0.17 | +0.07 |
| MIN | Jesper Wallstedt | 81% | +0.15 | +0.07 |
| OTT | Linus Ullmark | 63% | +0.14 | +0.06 |
| COL | Mackenzie Blackwood | 71% | +0.13 | +0.06 |
| CBJ | Jet Greaves | 51% | +0.11 | +0.05 |
| MTL | Jacob Fowler | 54% | +0.09 | +0.04 |
| CHI | Spencer Knight | 84% | +0.05 | +0.02 |
| WPG | Stuart Skinner | 71% | +0.02 | +0.01 |
| STL | Joel Hofer | 75% | +0.01 | +0.00 |
| CAR | Pyotr Kochetkov | 57% | -0.05 | -0.02 |
| NYR | Dylan Garand | 71% | -0.05 | -0.02 |
| PHI | Joseph Woll | 54% | -0.06 | -0.02 |
| NJD | Jake Allen | 64% | -0.06 | -0.02 |
| EDM | Devon Levi | 62% | -0.07 | -0.03 |
| SEA | Philipp Grubauer | 52% | -0.08 | -0.03 |
| TOR | Sergei Bobrovsky | 60% | -0.13 | -0.05 |
| DET | John Gibson | 71% | -0.13 | -0.05 |
| ANA | Lukas Dostal | 70% | -0.15 | -0.06 |
| UTA | Karel Vejmelka | 77% | -0.16 | -0.07 |
| LAK | Darcy Kuemper | 64% | -0.17 | -0.07 |
| BUF | Ukko-Pekka Luukkonen | 76% | -0.17 | -0.07 |
| VGK | Carter Hart | 61% | -0.18 | -0.08 |
| NSH | Juuse Saros | 56% | -0.23 | -0.09 |
| SJS | Yaroslav Askarov | 53% | -0.25 | -0.10 |
| FLA | Jacob Markstrom | 49% | -0.26 | -0.11 |
| PIT | Arturs Silovs | 69% | -0.30 | -0.12 |
| VAN | Kevin Lankinen | 56% | -0.63 | -0.26 |

## Current model fit

- Fitted on 5771 games from 2022-23 to 2026-27.
- Home ice: +3.2% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.8% goals scored, +3.3% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 23%.
- Blend: 39% on the betting line wherever there is one (fitted on 45 logged games, shrunk toward the backtest value).
- Simulator: 22.4% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.41 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
