# NHL score predictions

Updated Thu Nov 05, 2026 10:39 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Friday, November 6

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | CBJ @ BUF | CBJ 3, BUF 4 | BUF 60% | CBJ +150 / BUF -150 | 2.9 – 3.6 | 1–5 / 1–6 | 21% | BUF -1.5 39% | 6.5 / 6.5 (over 50%) | Cam Talbot (expected) / Ukko-Pekka Luukkonen (expected) | CBJ +145 / BUF -175 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | SJS @ MIN | SJS 3, MIN 4 | MIN 74% | SJS +285 / MIN -285 | 2.5 – 4.1 | 1–5 / 2–7 | 18% | MIN -1.5 54% | 6.5 / 6.5 (over 49%) | Yaroslav Askarov (expected) / Jesper Wallstedt (expected) | SJS +210 / MIN -258 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | ANA @ CGY | ANA 3, CGY 4 | CGY 56% | ANA +125 / CGY -125 | 3.1 – 3.4 | 1–5 / 1–6 | 21% | CGY -1.5 35% | 6.5 / 6.5 (over 50%) | Ville Husso (expected) / Dustin Wolf (expected) | ANA +102 / CGY -122 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Saturday, November 7

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 12:30 PM | FLA @ WSH | FLA 2, WSH 3 | WSH 53% | FLA +110 / WSH -110 | 3.0 – 3.2 | 1–5 / 1–6 | 23% | WSH -1.5 32% | 6.2 | Jacob Markstrom (expected) / Logan Thompson (expected) | – | no line yet (model fair WSH -1.5 +215 / FLA +1.5 -215) | no line yet | no line yet |
| 1:00 PM | STL @ NSH | STL 4, NSH 3 | STL 54% | STL -115 / NSH +115 | 3.2 – 3.0 | 1–6 / 1–5 | 22% | STL -1.5 33% | 6.2 | Joel Hofer (expected) / Juuse Saros (expected) | – | no line yet (model fair NSH +1.5 -205 / STL -1.5 +205) | no line yet | no line yet |
| 5:00 PM | NYR @ SEA | NYR 4, SEA 3 | NYR 54% | NYR -115 / SEA +115 | 3.4 – 3.1 | 1–6 / 1–6 | 21% | NYR -1.5 34% | 6.5 | Dylan Garand (expected) / Philipp Grubauer (expected) | – | no line yet (model fair SEA +1.5 -195 / NYR -1.5 +195) | no line yet | no line yet |
| 7:00 PM | MTL @ TOR | MTL 4, TOR 3 | MTL 53% | MTL -110 / TOR +110 | 3.3 – 3.2 | 1–6 / 1–6 | 21% | MTL -1.5 33% | 6.5 | Jacob Fowler (expected) / Sergei Bobrovsky (expected) | – | no line yet (model fair TOR +1.5 -205 / MTL -1.5 +205) | no line yet | no line yet |
| 7:00 PM | UTA @ OTT | UTA 4, OTT 3 | UTA 56% | UTA -125 / OTT +125 | 3.4 – 3.0 | 1–6 / 1–5 | 21% | UTA -1.5 35% | 6.4 | Karel Vejmelka (expected) / Samuel Ersson (expected) | – | no line yet (model fair OTT +1.5 -185 / UTA -1.5 +185) | no line yet | no line yet |
| 7:00 PM | NJD @ NYI | NJD 3, NYI 2 | NJD 54% | NJD -120 / NYI +120 | 3.1 – 2.8 | 1–5 / 1–5 | 22% | NJD -1.5 33% | 5.9 | Connor Hellebuyck (expected) / Ilya Sorokin (expected) | – | no line yet (model fair NYI +1.5 -205 / NJD -1.5 +205) | no line yet | no line yet |
| 8:00 PM | CHI @ CAR | CHI 2, CAR 5 | CAR 80% | CHI +395 / CAR -395 | 2.3 – 4.4 | 0–4 / 2–7 | 16% | CAR -1.5 61% | 6.6 | Spencer Knight (expected) / Pyotr Kochetkov (expected) | – | no line yet (model fair CAR -1.5 -155 / CHI +1.5 +155) | no line yet | no line yet |
| 8:00 PM | SJS @ DAL | SJS 2, DAL 4 | DAL 77% | SJS +335 / DAL -335 | 2.2 – 4.0 | 0–4 / 2–6 | 18% | DAL -1.5 56% | 6.2 | Alex Nedeljkovic (expected) / Jake Oettinger (expected) | – | no line yet (model fair DAL -1.5 -130 / SJS +1.5 +130) | no line yet | no line yet |
| 8:00 PM | TBL @ MIN | TBL 4, MIN 3 | TBL 56% | TBL -125 / MIN +125 | 3.3 – 3.0 | 1–6 / 1–5 | 22% | TBL -1.5 34% | 6.3 | Andrei Vasilevskiy (expected) / Calvin Pickard (expected) | – | no line yet (model fair MIN +1.5 -190 / TBL -1.5 +190) | no line yet | no line yet |
| 9:00 PM | DET @ COL | DET 3, COL 4 | COL 64% | DET +175 / COL -175 | 2.8 – 3.7 | 1–5 / 1–6 | 21% | COL -1.5 42% | 6.5 | John Gibson (expected) / Mackenzie Blackwood (expected) | – | no line yet (model fair COL -1.5 +140 / DET +1.5 -140) | no line yet | no line yet |
| 9:00 PM | PIT @ LAK | PIT 4, LAK 3 | PIT 50% | PIT -100 / LAK +100 | 3.1 – 3.1 | 1–6 / 1–5 | 23% | PIT -1.5 29% | 6.3 | Arturs Silovs (expected) / Anton Forsberg (expected) | – | no line yet (model fair LAK +1.5 -245 / PIT -1.5 +245) | no line yet | no line yet |
| 10:00 PM | VAN @ EDM | VAN 3, EDM 4 | EDM 71% | VAN +240 / EDM -240 | 2.8 – 4.2 | 1–5 / 2–7 | 18% | EDM -1.5 51% | 7.0 | Leevi Meriläinen (expected) / Tristan Jarry (expected) | – | no line yet (model fair EDM -1.5 -105 / VAN +1.5 +105) | no line yet | no line yet |

\* price not posted; assumed -110.

## Sunday, November 8

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1:00 PM | FLA @ BOS | FLA 2, BOS 3 | BOS 55% | FLA +125 / BOS -125 | 2.9 – 3.2 | 1–5 / 1–6 | 22% | BOS -1.5 34% | 6.1 | Akira Schmid (expected) / Jeremy Swayman (expected) | – | no line yet (model fair BOS -1.5 +200 / FLA +1.5 -200) | no line yet | no line yet |
| 3:30 PM | VGK @ BUF | VGK 4, BUF 3 | VGK 52% | VGK -110 / BUF +110 | 3.2 – 3.0 | 1–6 / 1–5 | 22% | VGK -1.5 32% | 6.2 | Carter Hart (expected) / Ukko-Pekka Luukkonen (expected) | – | no line yet (model fair BUF +1.5 -215 / VGK -1.5 +215) | no line yet | no line yet |
| 6:00 PM | TBL @ WPG | TBL 3, WPG 2 | TBL 56% | TBL -130 / WPG +130 | 3.3 – 2.9 | 1–6 / 1–5 | 23% | TBL -1.5 34% | 6.1 | Dennis Hildeby (expected) / Stuart Skinner (expected) | – | no line yet (model fair WPG +1.5 -195 / TBL -1.5 +195) | no line yet | no line yet |
| 7:00 PM | NJD @ TOR | NJD 3, TOR 2 | NJD 55% | NJD -120 / TOR +120 | 3.2 – 2.9 | 1–6 / 1–5 | 23% | NJD -1.5 33% | 6.0 | Jake Allen (expected) / Anthony Stolarz (expected) | – | no line yet (model fair TOR +1.5 -200 / NJD -1.5 +200) | no line yet | no line yet |
| 7:00 PM | PHI @ CGY | PHI 2, CGY 3 | CGY 53% | PHI +110 / CGY -110 | 3.0 – 3.2 | 1–5 / 1–6 | 23% | CGY -1.5 31% | 6.2 | Joseph Woll (expected) / Dustin Wolf (expected) | – | no line yet (model fair CGY -1.5 +220 / PHI +1.5 -220) | no line yet | no line yet |
| 8:00 PM | PIT @ ANA | PIT 4, ANA 3 | PIT 52% | PIT -110 / ANA +110 | 3.5 – 3.3 | 1–6 / 1–6 | 21% | PIT -1.5 32% | 6.8 | Sergei Murashov (expected) / Lukas Dostal (expected) | – | no line yet (model fair ANA +1.5 -210 / PIT -1.5 +210) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 250 | 0.6495 | 0.2289 | 61.2% | 1.39 | 1.81 | 89.4% |
| Model only (before blending) | 250 | 0.6517 | 0.2300 | 59.6% | – | – | – |
| Elo | 250 | 0.6661 | 0.2367 | 60.8% | – | – | – |
| Final prediction, games with a line | 116 | 0.6542 | 0.2311 | 58.6% | 1.40 | 1.87 | 89.2% |
| Model only, games with a line | 116 | 0.6588 | 0.2334 | 55.2% | – | – | – |
| Betting market (de-vigged moneyline) | 116 | 0.6554 | 0.2317 | 59.5% | – | 1.85 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.6% of regular-season games, happened in 22.0%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 1 | 0-1-0 | 1.3 | -1.29 | -100.0% | +11.8% |
| Moneyline | 8 | 4-4-0 | 8.7 | +1.83 | +21.2% | +6.4% |
| Total | 1 | 0-1-0 | 0.9 | -0.89 | -100.0% | +3.0% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 20 of 24 games (83%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Wednesday, November 4

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| OTT @ BUF | 3–4 | 2–1 | 45% | yes | Samuel Ersson / Colten Ellis |
| CHI @ FLA | 2–3 | 3–5 | 69% | yes | Spencer Knight / Jacob Markstrom |
| SJS @ LAK | 3–4 | 2–7 | 64% | no | Yaroslav Askarov / Darcy Kuemper |
| CGY @ SEA | 3–4 | 1–2 (OT) | 55% | yes | Dustin Wolf / Joey Daccord |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.69 | +0.41 | +0.28 | 3.37 | 2.36 | 8.62 | 7.17 | 1578 |
| 2 | UTA | +0.46 | +0.23 | +0.23 | 3.13 | 2.34 | 8.14 | 8.37 | 1512 |
| 3 | TBL | +0.39 | +0.21 | +0.18 | 2.94 | 2.47 | 8.21 | 7.80 | 1541 |
| 4 | VGK | +0.33 | +0.05 | +0.28 | 2.69 | 2.33 | 9.08 | 7.25 | 1527 |
| 5 | MIN | +0.31 | +0.14 | +0.17 | 2.97 | 2.49 | 9.13 | 8.14 | 1548 |
| 6 | PIT | +0.28 | +0.22 | +0.06 | 3.06 | 2.58 | 7.89 | 7.82 | 1492 |
| 7 | NJD | +0.28 | +0.02 | +0.26 | 2.79 | 2.32 | 9.13 | 7.78 | 1513 |
| 8 | COL | +0.26 | +0.30 | -0.04 | 2.99 | 2.76 | 7.74 | 7.98 | 1548 |
| 9 | DAL | +0.25 | -0.08 | +0.33 | 2.49 | 2.27 | 9.28 | 7.33 | 1530 |
| 10 | FLA | +0.24 | -0.01 | +0.25 | 2.58 | 2.36 | 9.51 | 7.66 | 1505 |
| 11 | EDM | +0.10 | +0.09 | +0.01 | 2.54 | 2.67 | 9.67 | 8.09 | 1532 |
| 12 | OTT | +0.08 | -0.02 | +0.11 | 2.67 | 2.55 | 8.11 | 8.29 | 1517 |
| 13 | STL | +0.08 | -0.01 | +0.09 | 2.62 | 2.58 | 6.91 | 7.59 | 1503 |
| 14 | BUF | +0.06 | +0.09 | -0.03 | 2.76 | 2.71 | 7.91 | 8.46 | 1517 |
| 15 | WSH | +0.03 | +0.11 | -0.08 | 2.87 | 2.77 | 7.74 | 8.05 | 1514 |
| 16 | LAK | +0.03 | -0.09 | +0.12 | 2.56 | 2.55 | 8.24 | 8.26 | 1477 |
| 17 | NYR | +0.01 | +0.01 | -0.01 | 2.71 | 2.72 | 8.74 | 7.78 | 1491 |
| 18 | CBJ | -0.04 | -0.03 | -0.00 | 2.67 | 2.67 | 7.72 | 8.52 | 1496 |
| 19 | DET | -0.04 | -0.07 | +0.03 | 2.66 | 2.62 | 8.45 | 8.67 | 1485 |
| 20 | BOS | -0.04 | +0.03 | -0.07 | 2.72 | 2.81 | 7.74 | 8.14 | 1532 |
| 21 | MTL | -0.05 | +0.06 | -0.11 | 2.81 | 2.83 | 7.15 | 8.39 | 1530 |
| 22 | NYI | -0.09 | -0.07 | -0.02 | 2.70 | 2.73 | 7.54 | 8.56 | 1490 |
| 23 | NSH | -0.13 | -0.06 | -0.07 | 2.60 | 2.77 | 8.12 | 7.77 | 1489 |
| 24 | TOR | -0.14 | -0.02 | -0.12 | 2.49 | 2.83 | 8.75 | 8.41 | 1483 |
| 25 | WPG | -0.16 | -0.13 | -0.03 | 2.55 | 2.73 | 8.25 | 9.07 | 1464 |
| 26 | CGY | -0.23 | -0.10 | -0.13 | 2.60 | 2.83 | 7.24 | 8.06 | 1466 |
| 27 | PHI | -0.26 | -0.25 | -0.01 | 2.34 | 2.68 | 7.74 | 7.47 | 1473 |
| 28 | SEA | -0.29 | -0.11 | -0.18 | 2.43 | 2.89 | 7.16 | 8.55 | 1481 |
| 29 | ANA | -0.37 | -0.01 | -0.36 | 2.68 | 3.06 | 8.07 | 8.45 | 1482 |
| 30 | CHI | -0.66 | -0.27 | -0.39 | 2.32 | 3.10 | 7.17 | 8.43 | 1423 |
| 31 | VAN | -0.71 | -0.22 | -0.49 | 2.27 | 3.20 | 7.62 | 8.82 | 1409 |
| 32 | SJS | -0.81 | -0.25 | -0.56 | 2.31 | 3.28 | 7.27 | 8.93 | 1452 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 71% | +0.39 | +0.16 |
| WSH | Logan Thompson | 72% | +0.36 | +0.15 |
| BOS | Jeremy Swayman | 74% | +0.32 | +0.14 |
| MTL | Jacob Fowler | 66% | +0.30 | +0.12 |
| MIN | Jesper Wallstedt | 88% | +0.24 | +0.10 |
| COL | Mackenzie Blackwood | 66% | +0.16 | +0.07 |
| OTT | Linus Ullmark | 36% | +0.14 | +0.06 |
| TBL | Andrei Vasilevskiy | 80% | +0.14 | +0.06 |
| CBJ | Jet Greaves | 50% | +0.10 | +0.04 |
| CHI | Spencer Knight | 65% | +0.10 | +0.04 |
| DAL | Jake Oettinger | 82% | +0.09 | +0.04 |
| CAR | Pyotr Kochetkov | 72% | +0.05 | +0.02 |
| STL | Joel Hofer | 76% | +0.04 | +0.02 |
| NYR | Dylan Garand | 71% | -0.01 | -0.01 |
| WPG | Stuart Skinner | 70% | -0.03 | -0.01 |
| PHI | Dan Vladar | 57% | -0.04 | -0.02 |
| NJD | Jake Allen | 48% | -0.06 | -0.02 |
| BUF | Ukko-Pekka Luukkonen | 55% | -0.13 | -0.05 |
| TOR | Sergei Bobrovsky | 65% | -0.14 | -0.06 |
| ANA | Lukas Dostal | 51% | -0.17 | -0.07 |
| DET | John Gibson | 67% | -0.17 | -0.07 |
| LAK | Darcy Kuemper | 63% | -0.18 | -0.08 |
| NSH | Juuse Saros | 70% | -0.19 | -0.08 |
| SEA | Philipp Grubauer | 55% | -0.19 | -0.08 |
| SJS | Yaroslav Askarov | 65% | -0.20 | -0.09 |
| UTA | Karel Vejmelka | 66% | -0.21 | -0.09 |
| CGY | Dustin Wolf | 49% | -0.23 | -0.10 |
| VAN | Leevi Meriläinen | 58% | -0.29 | -0.12 |
| PIT | Arturs Silovs | 68% | -0.29 | -0.12 |
| FLA | Jacob Markstrom | 47% | -0.30 | -0.12 |
| EDM | Tristan Jarry | 56% | -0.31 | -0.13 |
| VGK | Adin Hill | 52% | -0.33 | -0.14 |

## Current model fit

- Fitted on 5842 games from 2022-23 to 2026-27.
- Home ice: +3.1% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.8% goals scored, +3.4% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 22%.
- Blend: 49% on the betting line wherever there is one (fitted on 116 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
