# NHL score predictions

Updated Sun Nov 08, 2026 01:46 AM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Sunday, November 8

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1:00 PM | FLA @ BOS | FLA 3, BOS 4 | BOS 56% | FLA +130 / BOS -130 | 2.9 – 3.3 | 1–5 / 1–6 | 23% | BOS -1.5 34% | 6.2 / 6.5 (over 46%) | Jacob Markstrom (expected) / Jeremy Swayman (expected) | FLA +114 / BOS -135 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 3:30 PM | VGK @ BUF | VGK 4, BUF 3 | VGK 51% | VGK -105 / BUF +105 | 3.2 – 3.2 | 1–6 / 1–6 | 22% | VGK -1.5 30% | 6.4 / 6.5 (over 48%) | Carter Hart (expected) / Colten Ellis (expected) | VGK -112 / BUF -108 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 6:00 PM | TBL @ WPG | TBL 3, WPG 2 | TBL 56% | TBL -130 / WPG +130 | 3.3 – 2.9 | 1–6 / 1–5 | 22% | TBL -1.5 35% | 6.2 / 6.5 (over 45%) | Andrei Vasilevskiy (expected) / Stuart Skinner (expected) | TBL -142 / WPG +120 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | NJD @ TOR | NJD 3, TOR 2 | NJD 57% | NJD -130 / TOR +130 | 3.3 – 2.8 | 1–6 / 1–5 | 22% | NJD -1.5 36% | 6.1 / 6.5 (over 44%) | Connor Hellebuyck (expected) / Anthony Stolarz (expected) | NJD -148 / TOR +124 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | PHI @ CGY | PHI 2, CGY 3 | CGY 51% | PHI +105 / CGY -105 | 3.0 – 3.1 | 1–5 / 1–5 | 22% | CGY -1.5 31% | 6.1 / 5.5 (over 54%) | Dan Vladar (expected) / Dustin Wolf (expected) | PHI -112 / CGY -108 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | PIT @ ANA | PIT 3, ANA 4 | ANA 50% | PIT +100 / ANA -100 | 3.4 – 3.5 | 1–6 / 1–6 | 20% | ANA -1.5 31% | 6.9 / 6.5 (over 56%) | Arturs Silovs (expected) / Laurent Brossoit (expected) | PIT +100 / ANA -120 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Monday, November 9

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8:00 PM | NYR @ EDM | NYR 3, EDM 4 | EDM 56% | NYR +125 / EDM -125 | 3.0 – 3.4 | 1–5 / 1–6 | 22% | EDM -1.5 35% | 6.5 | Dylan Garand (expected) / Devon Levi (expected) | – | no line yet (model fair EDM -1.5 +185 / NYR +1.5 -185) | no line yet | no line yet |
| 9:30 PM | PHI @ VAN | PHI 4, VAN 3 | PHI 54% | PHI -120 / VAN +120 | 3.3 – 3.0 | 1–6 / 1–5 | 22% | PHI -1.5 34% | 6.4 | Joseph Woll (expected) / Leevi Meriläinen (expected) | – | no line yet (model fair VAN +1.5 -200 / PHI -1.5 +200) | no line yet | no line yet |
| 10:00 PM | NYI @ SJS | NYI 4, SJS 3 | NYI 63% | NYI -175 / SJS +175 | 3.7 – 2.8 | 1–6 / 1–5 | 20% | NYI -1.5 43% | 6.5 | Ilya Sorokin (expected) / Yaroslav Askarov (expected) | – | no line yet (model fair SJS +1.5 -135 / NYI -1.5 +135) | no line yet | no line yet |

\* price not posted; assumed -110.

## Tuesday, November 10

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | COL @ TOR | COL 4, TOR 3 | COL 59% | COL -140 / TOR +140 | 3.7 – 3.1 | 1–6 / 1–6 | 21% | COL -1.5 38% | 6.8 | Mackenzie Blackwood (expected) / Sergei Bobrovsky (expected) | – | no line yet (model fair TOR +1.5 -165 / COL -1.5 +165) | no line yet | no line yet |
| 7:00 PM | MIN @ MTL | MIN 3, MTL 2 | MIN 55% | MIN -120 / MTL +120 | 3.2 – 2.9 | 1–6 / 1–5 | 22% | MIN -1.5 33% | 6.2 | Jesper Wallstedt (expected) / Jacob Fowler (expected) | – | no line yet (model fair MTL +1.5 -200 / MIN -1.5 +200) | no line yet | no line yet |
| 7:00 PM | WSH @ OTT | WSH 4, OTT 3 | WSH 52% | WSH -110 / OTT +110 | 3.3 – 3.1 | 1–6 / 1–6 | 22% | WSH -1.5 32% | 6.4 | Logan Thompson (expected) / Samuel Ersson (expected) | – | no line yet (model fair OTT +1.5 -215 / WSH -1.5 +215) | no line yet | no line yet |
| 7:00 PM | NJD @ WPG | NJD 3, WPG 2 | NJD 57% | NJD -135 / WPG +135 | 3.2 – 2.8 | 1–6 / 1–5 | 23% | NJD -1.5 34% | 6.0 | Connor Hellebuyck (expected) / Stuart Skinner (expected) | – | no line yet (model fair WPG +1.5 -190 / NJD -1.5 +190) | no line yet | no line yet |
| 7:30 PM | FLA @ CBJ | FLA 3, CBJ 2 | FLA 53% | FLA -115 / CBJ +115 | 3.2 – 3.0 | 1–5 / 1–5 | 22% | FLA -1.5 32% | 6.1 | Jacob Markstrom (expected) / Jet Greaves (expected) | – | no line yet (model fair CBJ +1.5 -215 / FLA -1.5 +215) | no line yet | no line yet |
| 8:00 PM | DET @ STL | DET 2, STL 3 | STL 55% | DET +125 / STL -125 | 2.9 – 3.2 | 1–5 / 1–6 | 22% | STL -1.5 34% | 6.1 | Daniil Tarasov (expected) / Joel Hofer (expected) | – | no line yet (model fair STL -1.5 +195 / DET +1.5 -195) | no line yet | no line yet |
| 10:00 PM | NSH @ LAK | NSH 2, LAK 3 | LAK 54% | NSH +120 / LAK -120 | 2.9 – 3.2 | 1–5 / 1–6 | 22% | LAK -1.5 33% | 6.1 | Juuse Saros (expected) / Darcy Kuemper (expected) | – | no line yet (model fair LAK -1.5 +205 / NSH +1.5 -205) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 264 | 0.6480 | 0.2282 | 61.4% | 1.38 | 1.81 | 90.0% |
| Model only (before blending) | 264 | 0.6502 | 0.2293 | 59.5% | – | – | – |
| Elo | 264 | 0.6639 | 0.2356 | 61.4% | – | – | – |
| Final prediction, games with a line | 130 | 0.6506 | 0.2295 | 59.2% | 1.37 | 1.87 | 90.4% |
| Model only, games with a line | 130 | 0.6550 | 0.2318 | 55.4% | – | – | – |
| Betting market (de-vigged moneyline) | 130 | 0.6514 | 0.2299 | 59.2% | – | 1.85 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.5% of regular-season games, happened in 22.3%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 1 | 0-1-0 | 1.3 | -1.29 | -100.0% | +11.8% |
| Moneyline | 8 | 4-4-0 | 8.7 | +1.83 | +21.2% | +6.4% |
| Total | 1 | 0-1-0 | 0.9 | -0.89 | -100.0% | +3.0% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 25 of 30 games (83%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Friday, November 6

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| CBJ @ BUF | 3–4 | 2–5 | 59% | yes | Jet Greaves / Ukko-Pekka Luukkonen |
| SJS @ MIN | 3–4 | 1–4 | 74% | yes | Yaroslav Askarov / Jesper Wallstedt |
| ANA @ CGY | 3–4 | 5–3 | 42% | yes | Lukas Dostal / Dustin Wolf |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.71 | +0.44 | +0.27 | 3.44 | 2.40 | 8.64 | 7.22 | 1581 |
| 2 | UTA | +0.47 | +0.24 | +0.23 | 3.14 | 2.35 | 8.23 | 8.80 | 1510 |
| 3 | TBL | +0.37 | +0.20 | +0.18 | 2.91 | 2.49 | 8.30 | 7.87 | 1544 |
| 4 | VGK | +0.33 | +0.04 | +0.29 | 2.70 | 2.34 | 9.17 | 7.32 | 1530 |
| 5 | MIN | +0.30 | +0.11 | +0.19 | 2.92 | 2.49 | 9.29 | 8.15 | 1552 |
| 6 | NJD | +0.25 | +0.03 | +0.22 | 2.83 | 2.39 | 9.16 | 7.90 | 1516 |
| 7 | PIT | +0.25 | +0.19 | +0.06 | 3.02 | 2.59 | 7.91 | 7.87 | 1486 |
| 8 | FLA | +0.24 | -0.01 | +0.26 | 2.59 | 2.37 | 9.55 | 7.71 | 1505 |
| 9 | COL | +0.23 | +0.28 | -0.04 | 2.97 | 2.78 | 7.75 | 8.11 | 1545 |
| 10 | DAL | +0.23 | -0.08 | +0.31 | 2.52 | 2.32 | 9.31 | 7.35 | 1527 |
| 11 | EDM | +0.10 | +0.11 | -0.01 | 2.60 | 2.70 | 9.74 | 8.10 | 1528 |
| 12 | OTT | +0.09 | -0.03 | +0.12 | 2.68 | 2.55 | 8.17 | 8.34 | 1517 |
| 13 | BUF | +0.09 | +0.12 | -0.03 | 2.83 | 2.73 | 8.12 | 8.48 | 1522 |
| 14 | STL | +0.09 | +0.02 | +0.07 | 2.69 | 2.62 | 7.01 | 7.63 | 1501 |
| 15 | WSH | +0.04 | +0.10 | -0.07 | 2.87 | 2.78 | 7.81 | 8.11 | 1514 |
| 16 | LAK | +0.04 | -0.09 | +0.13 | 2.57 | 2.55 | 8.29 | 8.32 | 1477 |
| 17 | BOS | +0.02 | +0.04 | -0.02 | 2.73 | 2.77 | 7.81 | 8.16 | 1539 |
| 18 | NYR | +0.00 | +0.02 | -0.01 | 2.74 | 2.74 | 8.73 | 7.83 | 1494 |
| 19 | DET | -0.05 | -0.09 | +0.04 | 2.66 | 2.63 | 8.52 | 8.75 | 1482 |
| 20 | MTL | -0.05 | +0.06 | -0.11 | 2.82 | 2.85 | 7.58 | 8.48 | 1533 |
| 21 | CBJ | -0.09 | -0.03 | -0.06 | 2.74 | 2.77 | 7.72 | 8.74 | 1494 |
| 22 | NSH | -0.10 | -0.06 | -0.04 | 2.63 | 2.75 | 8.24 | 7.77 | 1492 |
| 23 | NYI | -0.13 | -0.06 | -0.07 | 2.74 | 2.82 | 7.60 | 8.59 | 1486 |
| 24 | WPG | -0.13 | -0.12 | -0.01 | 2.57 | 2.73 | 8.25 | 9.10 | 1468 |
| 25 | TOR | -0.14 | -0.02 | -0.12 | 2.49 | 2.83 | 8.79 | 8.45 | 1483 |
| 26 | CGY | -0.24 | -0.12 | -0.12 | 2.58 | 2.84 | 7.32 | 8.09 | 1461 |
| 27 | PHI | -0.27 | -0.25 | -0.02 | 2.37 | 2.71 | 7.79 | 7.47 | 1471 |
| 28 | SEA | -0.30 | -0.12 | -0.18 | 2.44 | 2.91 | 7.22 | 8.60 | 1481 |
| 29 | ANA | -0.36 | +0.01 | -0.37 | 2.71 | 3.08 | 8.05 | 8.53 | 1490 |
| 30 | CHI | -0.64 | -0.28 | -0.36 | 2.33 | 3.07 | 7.23 | 8.52 | 1420 |
| 31 | VAN | -0.72 | -0.23 | -0.49 | 2.26 | 3.20 | 7.68 | 8.82 | 1404 |
| 32 | SJS | -0.77 | -0.26 | -0.51 | 2.32 | 3.24 | 7.30 | 9.09 | 1449 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 62% | +0.38 | +0.16 |
| WSH | Logan Thompson | 72% | +0.36 | +0.15 |
| BOS | Jeremy Swayman | 66% | +0.32 | +0.13 |
| MTL | Jacob Fowler | 59% | +0.29 | +0.12 |
| MIN | Jesper Wallstedt | 89% | +0.25 | +0.11 |
| COL | Mackenzie Blackwood | 70% | +0.17 | +0.07 |
| TBL | Andrei Vasilevskiy | 82% | +0.15 | +0.06 |
| OTT | Linus Ullmark | 36% | +0.14 | +0.06 |
| CBJ | Jet Greaves | 50% | +0.11 | +0.05 |
| CHI | Spencer Knight | 75% | +0.10 | +0.04 |
| DAL | Jake Oettinger | 73% | +0.09 | +0.04 |
| CAR | Pyotr Kochetkov | 65% | +0.05 | +0.02 |
| STL | Joel Hofer | 68% | +0.03 | +0.01 |
| NYR | Dylan Garand | 74% | +0.01 | +0.00 |
| WPG | Stuart Skinner | 73% | -0.04 | -0.02 |
| PHI | Dan Vladar | 51% | -0.04 | -0.02 |
| NJD | Jake Allen | 43% | -0.06 | -0.02 |
| BUF | Ukko-Pekka Luukkonen | 60% | -0.10 | -0.04 |
| VGK | Carter Hart | 53% | -0.12 | -0.05 |
| TOR | Sergei Bobrovsky | 65% | -0.14 | -0.06 |
| DET | John Gibson | 60% | -0.17 | -0.07 |
| LAK | Darcy Kuemper | 63% | -0.19 | -0.08 |
| NSH | Juuse Saros | 62% | -0.19 | -0.08 |
| SEA | Philipp Grubauer | 55% | -0.19 | -0.08 |
| ANA | Lukas Dostal | 51% | -0.20 | -0.08 |
| SJS | Yaroslav Askarov | 68% | -0.21 | -0.09 |
| UTA | Karel Vejmelka | 59% | -0.21 | -0.09 |
| CGY | Dustin Wolf | 54% | -0.25 | -0.11 |
| FLA | Jacob Markstrom | 47% | -0.30 | -0.12 |
| EDM | Tristan Jarry | 51% | -0.31 | -0.13 |
| VAN | Leevi Meriläinen | 62% | -0.36 | -0.15 |
| PIT | Arturs Silovs | 72% | -0.37 | -0.15 |

## Current model fit

- Fitted on 5856 games from 2022-23 to 2026-27.
- Home ice: +3.1% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.8% goals scored, +3.5% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 22%.
- Blend: 46% on the betting line wherever there is one (fitted on 130 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
