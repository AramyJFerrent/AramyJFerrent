# NHL score predictions

Updated Fri Oct 30, 2026 02:33 AM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Friday, October 30

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6:00 PM | NJD @ VGK | NJD 2, VGK 3 | VGK 54% | NJD +115 / VGK -115 | 2.9 – 3.1 | 1–5 / 1–5 | 22% | VGK -1.5 33% | 6.0 / 6.5 (over 42%) | Connor Hellebuyck (expected) / Carter Hart (expected) | NJD -105 / VGK -115 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | WPG @ FLA | WPG 2, FLA 3 | FLA 66% | WPG +190 / FLA -190 | 2.5 – 3.5 | 1–5 / 1–6 | 22% | FLA -1.5 43% | 6.1 / 6.5 (over 43%) | Nico Daws (expected) / Akira Schmid (expected) | WPG +185 / FLA -225 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | SEA @ CGY | SEA 3, CGY 4 | CGY 50% | SEA +100 / CGY -100 | 3.2 – 3.2 | 1–6 / 1–6 | 23% | CGY -1.5 30% | 6.4 / 6.5 (over 48%) | Philipp Grubauer (expected) / Dustin Wolf (expected) | SEA -115 / CGY -105 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Saturday, October 31

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1:00 PM | CHI @ BOS | CHI 3, BOS 4 | BOS 70% | CHI +230 / BOS -230 | 2.5 – 3.8 | 1–5 / 1–6 | 20% | BOS -1.5 48% | 6.4 | Spencer Knight (expected) / Jeremy Swayman (expected) | – | no line yet (model fair BOS -1.5 +105 / CHI +1.5 -105) | no line yet | no line yet |
| 1:00 PM | STL @ DET | STL 3, DET 2 | STL 50% | STL -100 / DET +100 | 3.0 – 3.0 | 1–5 / 1–5 | 23% | STL -1.5 30% | 5.9 | Joel Hofer (expected) / John Gibson (expected) | – | no line yet (model fair DET +1.5 -235 / STL -1.5 +235) | no line yet | no line yet |
| 2:00 PM | TBL @ NSH | TBL 3, NSH 2 | TBL 60% | TBL -145 / NSH +145 | 3.4 – 2.8 | 1–6 / 1–5 | 21% | TBL -1.5 39% | 6.3 | Andrei Vasilevskiy (expected) / Juuse Saros (expected) | – | no line yet (model fair NSH +1.5 -160 / TBL -1.5 +160) | no line yet | no line yet |
| 2:00 PM | EDM @ NYI | EDM 3, NYI 4 | NYI 52% | EDM +110 / NYI -110 | 3.1 – 3.3 | 1–5 / 1–6 | 22% | NYI -1.5 32% | 6.4 | Tristan Jarry (expected) / Ilya Sorokin (expected) | – | no line yet (model fair NYI -1.5 +215 / EDM +1.5 -215) | no line yet | no line yet |
| 4:00 PM | BUF @ LAK | BUF 3, LAK 2 | BUF 52% | BUF -110 / LAK +110 | 3.1 – 3.0 | 1–6 / 1–5 | 22% | BUF -1.5 31% | 6.1 | Colten Ellis (expected) / Darcy Kuemper (expected) | – | no line yet (model fair LAK +1.5 -225 / BUF -1.5 +225) | no line yet | no line yet |
| 4:00 PM | OTT @ SJS | OTT 4, SJS 3 | OTT 60% | OTT -150 / SJS +150 | 3.7 – 3.0 | 1–6 / 1–5 | 21% | OTT -1.5 38% | 6.7 | Samuel Ersson (expected) / Yaroslav Askarov (expected) | – | no line yet (model fair SJS +1.5 -160 / OTT -1.5 +160) | no line yet | no line yet |
| 7:00 PM | PIT @ MTL | PIT 3, MTL 4 | MTL 53% | PIT +115 / MTL -115 | 3.1 – 3.3 | 1–6 / 1–6 | 22% | MTL -1.5 32% | 6.4 | Arturs Silovs (expected) / Jacob Fowler (expected) | – | no line yet (model fair MTL -1.5 +210 / PIT +1.5 -210) | no line yet | no line yet |
| 7:00 PM | TOR @ VAN | TOR 4, VAN 3 | TOR 62% | TOR -165 / VAN +165 | 3.8 – 3.0 | 1–6 / 1–5 | 20% | TOR -1.5 41% | 6.8 | Sergei Bobrovsky (expected) / Kevin Lankinen (expected) | – | no line yet (model fair VAN +1.5 -145 / TOR -1.5 +145) | no line yet | no line yet |
| 8:00 PM | CBJ @ DAL | CBJ 2, DAL 3 | DAL 61% | CBJ +155 / DAL -155 | 2.5 – 3.2 | 1–5 / 1–6 | 22% | DAL -1.5 38% | 5.7 | Jet Greaves (expected) / Jake Oettinger (expected) | – | no line yet (model fair DAL -1.5 +165 / CBJ +1.5 -165) | no line yet | no line yet |
| 10:00 PM | CGY @ COL | CGY 3, COL 4 | COL 68% | CGY +215 / COL -215 | 2.6 – 3.8 | 1–5 / 1–6 | 20% | COL -1.5 47% | 6.4 | Devin Cooley (expected) / Mackenzie Blackwood (expected) | – | no line yet (model fair COL -1.5 +115 / CGY +1.5 -115) | no line yet | no line yet |

\* price not posted; assumed -110.

## Sunday, November 1

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1:00 PM | WPG @ CAR | WPG 3, CAR 4 | CAR 70% | WPG +235 / CAR -235 | 2.5 – 3.9 | 1–5 / 1–6 | 19% | CAR -1.5 49% | 6.4 | Stuart Skinner (expected) / Pyotr Kochetkov (expected) | – | no line yet (model fair CAR -1.5 +105 / WPG +1.5 -105) | no line yet | no line yet |
| 3:30 PM | MIN @ WSH | MIN 4, WSH 3 | MIN 58% | MIN -140 / WSH +140 | 3.4 – 2.9 | 1–6 / 1–5 | 22% | MIN -1.5 36% | 6.3 | Jesper Wallstedt (expected) / Charlie Lindgren (expected) | – | no line yet (model fair WSH +1.5 -175 / MIN -1.5 +175) | no line yet | no line yet |
| 4:00 PM | UTA @ PHI | UTA 3, PHI 2 | UTA 62% | UTA -160 / PHI +160 | 3.4 – 2.6 | 1–6 / 1–5 | 21% | UTA -1.5 40% | 6.0 | Karel Vejmelka (expected) / Dan Vladar (expected) | – | no line yet (model fair PHI +1.5 -150 / UTA -1.5 +150) | no line yet | no line yet |
| 6:00 PM | EDM @ NYR | EDM 3, NYR 4 | NYR 56% | EDM +125 / NYR -125 | 3.0 – 3.4 | 1–5 / 1–6 | 22% | NYR -1.5 35% | 6.4 | Matt Tomkins (expected) / Dylan Garand (expected) | – | no line yet (model fair NYR -1.5 +185 / EDM +1.5 -185) | no line yet | no line yet |
| 8:00 PM | OTT @ ANA | OTT 4, ANA 3 | OTT 51% | OTT -105 / ANA +105 | 3.3 – 3.2 | 1–6 / 1–6 | 22% | OTT -1.5 31% | 6.4 | Jonas Johansson (expected) / Lukas Dostal (expected) | – | no line yet (model fair ANA +1.5 -225 / OTT -1.5 +225) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 202 | 0.6541 | 0.2310 | 60.9% | 1.40 | 1.79 | 89.1% |
| Model only (before blending) | 202 | 0.6554 | 0.2317 | 59.9% | – | – | – |
| Elo | 202 | 0.6686 | 0.2379 | 61.9% | – | – | – |
| Final prediction, games with a line | 68 | 0.6710 | 0.2390 | 55.9% | 1.41 | 1.85 | 88.2% |
| Model only, games with a line | 68 | 0.6748 | 0.2409 | 52.9% | – | – | – |
| Betting market (de-vigged moneyline) | 68 | 0.6731 | 0.2399 | 58.8% | – | 1.84 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.6% of regular-season games, happened in 22.8%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 1 | 0-1-0 | 1.3 | -1.29 | -100.0% | +11.8% |
| Moneyline | 5 | 3-2-0 | 5.6 | +1.52 | +27.0% | +5.9% |
| Total | 1 | 0-1-0 | 0.9 | -0.89 | -100.0% | +3.0% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 10 of 13 games (77%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Wednesday, October 28

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| PHI @ WSH | 2–3 | 2–5 | 65% | yes | Joseph Woll / Logan Thompson |
| CGY @ EDM | 3–4 | 0–4 | 58% | no | Devin Cooley / Tristan Jarry |
| NJD @ COL | 3–4 | 2–5 | 58% | yes | Jake Allen / Mackenzie Blackwood |
| TOR @ SEA | 4–3 | 4–5 | 47% | yes | Sergei Bobrovsky / Philipp Grubauer |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.68 | +0.41 | +0.27 | 3.44 | 2.42 | 8.12 | 6.77 | 1578 |
| 2 | UTA | +0.47 | +0.24 | +0.23 | 3.18 | 2.39 | 8.03 | 8.41 | 1512 |
| 3 | MIN | +0.40 | +0.16 | +0.24 | 3.10 | 2.44 | 9.28 | 8.12 | 1541 |
| 4 | VGK | +0.36 | +0.09 | +0.26 | 2.80 | 2.40 | 8.85 | 7.38 | 1534 |
| 5 | TBL | +0.35 | +0.18 | +0.17 | 2.95 | 2.53 | 7.87 | 7.87 | 1538 |
| 6 | COL | +0.31 | +0.29 | +0.02 | 3.02 | 2.74 | 7.71 | 7.85 | 1549 |
| 7 | PIT | +0.28 | +0.22 | +0.06 | 3.11 | 2.64 | 7.99 | 7.70 | 1500 |
| 8 | DAL | +0.28 | -0.05 | +0.33 | 2.61 | 2.32 | 9.16 | 7.31 | 1530 |
| 9 | FLA | +0.23 | +0.00 | +0.23 | 2.66 | 2.44 | 9.13 | 7.43 | 1503 |
| 10 | NJD | +0.21 | +0.01 | +0.20 | 2.85 | 2.45 | 9.02 | 7.74 | 1504 |
| 11 | STL | +0.09 | -0.01 | +0.10 | 2.68 | 2.61 | 6.97 | 7.40 | 1499 |
| 12 | BUF | +0.08 | +0.07 | +0.01 | 2.79 | 2.71 | 7.64 | 8.32 | 1515 |
| 13 | EDM | +0.07 | +0.12 | -0.04 | 2.62 | 2.77 | 9.85 | 8.12 | 1523 |
| 14 | BOS | +0.06 | +0.08 | -0.02 | 2.84 | 2.80 | 7.75 | 8.09 | 1534 |
| 15 | WSH | +0.05 | +0.11 | -0.06 | 2.91 | 2.81 | 7.76 | 8.12 | 1521 |
| 16 | NYR | +0.03 | +0.02 | +0.01 | 2.74 | 2.74 | 8.57 | 7.74 | 1493 |
| 17 | OTT | +0.01 | -0.07 | +0.08 | 2.62 | 2.63 | 7.94 | 8.04 | 1517 |
| 18 | LAK | +0.00 | -0.13 | +0.13 | 2.58 | 2.59 | 7.88 | 8.11 | 1471 |
| 19 | DET | -0.02 | -0.11 | +0.09 | 2.64 | 2.59 | 8.45 | 8.62 | 1481 |
| 20 | MTL | -0.10 | +0.04 | -0.14 | 2.87 | 2.92 | 7.12 | 8.30 | 1526 |
| 21 | WPG | -0.10 | -0.10 | -0.00 | 2.64 | 2.77 | 8.01 | 8.26 | 1472 |
| 22 | TOR | -0.12 | -0.01 | -0.11 | 2.51 | 2.85 | 8.71 | 8.15 | 1482 |
| 23 | NYI | -0.14 | -0.06 | -0.08 | 2.72 | 2.86 | 7.57 | 8.69 | 1493 |
| 24 | NSH | -0.15 | -0.08 | -0.07 | 2.63 | 2.82 | 7.86 | 7.57 | 1481 |
| 25 | CBJ | -0.15 | -0.08 | -0.07 | 2.64 | 2.80 | 7.60 | 8.39 | 1493 |
| 26 | CGY | -0.23 | -0.10 | -0.14 | 2.67 | 2.89 | 7.28 | 8.18 | 1462 |
| 27 | SEA | -0.27 | -0.10 | -0.17 | 2.46 | 2.93 | 7.27 | 8.49 | 1485 |
| 28 | PHI | -0.31 | -0.27 | -0.04 | 2.36 | 2.77 | 7.74 | 7.57 | 1471 |
| 29 | ANA | -0.34 | -0.02 | -0.32 | 2.78 | 3.07 | 7.82 | 8.41 | 1476 |
| 30 | CHI | -0.70 | -0.29 | -0.41 | 2.32 | 3.17 | 7.17 | 8.38 | 1436 |
| 31 | SJS | -0.71 | -0.20 | -0.51 | 2.42 | 3.28 | 7.32 | 8.82 | 1465 |
| 32 | VAN | -0.76 | -0.22 | -0.54 | 2.30 | 3.31 | 7.65 | 8.74 | 1417 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| WSH | Logan Thompson | 72% | +0.44 | +0.19 |
| NYI | Ilya Sorokin | 62% | +0.42 | +0.17 |
| BOS | Jeremy Swayman | 76% | +0.33 | +0.14 |
| MTL | Jacob Fowler | 65% | +0.31 | +0.13 |
| CGY | Devin Cooley | 67% | +0.20 | +0.08 |
| MIN | Jesper Wallstedt | 84% | +0.18 | +0.08 |
| TBL | Andrei Vasilevskiy | 69% | +0.18 | +0.07 |
| DAL | Jake Oettinger | 74% | +0.14 | +0.06 |
| COL | Mackenzie Blackwood | 67% | +0.14 | +0.06 |
| OTT | Linus Ullmark | 55% | +0.13 | +0.06 |
| CHI | Spencer Knight | 88% | +0.10 | +0.04 |
| WPG | Stuart Skinner | 66% | +0.03 | +0.01 |
| STL | Joel Hofer | 66% | +0.00 | +0.00 |
| CAR | Pyotr Kochetkov | 62% | -0.03 | -0.01 |
| NJD | Jake Allen | 61% | -0.07 | -0.03 |
| NYR | Dylan Garand | 63% | -0.07 | -0.03 |
| PHI | Joseph Woll | 54% | -0.08 | -0.04 |
| DET | John Gibson | 63% | -0.14 | -0.06 |
| SEA | Philipp Grubauer | 58% | -0.14 | -0.06 |
| LAK | Darcy Kuemper | 60% | -0.16 | -0.07 |
| UTA | Karel Vejmelka | 80% | -0.16 | -0.07 |
| SJS | Yaroslav Askarov | 59% | -0.17 | -0.07 |
| BUF | Ukko-Pekka Luukkonen | 66% | -0.18 | -0.07 |
| TOR | Sergei Bobrovsky | 68% | -0.18 | -0.07 |
| ANA | Lukas Dostal | 73% | -0.18 | -0.08 |
| FLA | Akira Schmid | 52% | -0.18 | -0.08 |
| VGK | Carter Hart | 54% | -0.19 | -0.08 |
| NSH | Juuse Saros | 71% | -0.23 | -0.10 |
| CBJ | Cam Talbot | 57% | -0.25 | -0.11 |
| VAN | Leevi Meriläinen | 56% | -0.29 | -0.12 |
| PIT | Arturs Silovs | 69% | -0.30 | -0.13 |
| EDM | Tristan Jarry | 52% | -0.38 | -0.16 |

## Current model fit

- Fitted on 5794 games from 2022-23 to 2026-27.
- Home ice: +3.1% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.7% goals scored, +3.3% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 23%.
- Blend: 37% on the betting line wherever there is one (fitted on 68 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
