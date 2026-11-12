# NHL score predictions

Updated Wed Nov 11, 2026 09:59 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Wednesday, November 11

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10:00 PM | NSH @ ANA | NSH 3, ANA 4 | ANA 54% | NSH +120 / ANA -120 | 3.2 – 3.5 | 1–6 / 1–6 | 21% | ANA -1.5 34% | 6.8 / 6.5 (over 54%) | Justus Annunen (confirmed) / Laurent Brossoit (confirmed) | NSH +124 / ANA -148 | no edge | no edge | Under 6.5 (+120): EV +3.7%, 47%, stake 0.8u |
| 10:00 PM | PIT @ SJS | PIT 4, SJS 3 | PIT 62% | PIT -165 / SJS +165 | 3.8 – 3.1 | 1–6 / 1–5 | 21% | PIT -1.5 41% | 6.9 / 6.5 (over 56%) | Sergei Murashov (confirmed) / Yaroslav Askarov (confirmed) | PIT -148 / SJS +124 | PIT -1.5 (+160): EV +7.3%, 41%, stake 1.1u | PIT (-148): EV +5.0%, 63%, stake 1.8u | no edge |

## Thursday, November 12

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 12:00 PM | CAR @ SEA | CAR 4, SEA 3 | CAR 72% | CAR -255 / SEA +255 | 4.1 – 2.6 | 2–7 / 1–5 | 19% | CAR -1.5 51% | 6.6 / 6.5 (over 51%) | Pyotr Kochetkov (expected) / Philipp Grubauer (expected) | CAR -290 / SEA +235 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | MTL @ BOS | MTL 3, BOS 4 | BOS 55% | MTL +120 / BOS -120 | 3.0 – 3.3 | 1–5 / 1–6 | 21% | BOS -1.5 33% | 6.3 / 6.5 (over 46%) | Jacob Fowler (confirmed) / Jeremy Swayman (expected) | MTL +100 / BOS -120 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | MIN @ TOR | MIN 4, TOR 3 | MIN 61% | MIN -155 / TOR +155 | 3.5 – 2.8 | 1–6 / 1–5 | 22% | MIN -1.5 39% | 6.3 / 6.5 (over 47%) | Jesper Wallstedt (expected) / Sergei Bobrovsky (expected) | MIN -170 / TOR +142 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | COL @ OTT | COL 4, OTT 3 | COL 51% | COL -105 / OTT +105 | 3.2 – 3.2 | 1–6 / 1–6 | 23% | COL -1.5 31% | 6.4 / 6.5 (over 48%) | Mackenzie Blackwood (expected) / Linus Ullmark (expected) | COL -120 / OTT +100 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | WSH @ NJD | WSH 2, NJD 3 | NJD 55% | WSH +125 / NJD -125 | 2.9 – 3.2 | 1–5 / 1–6 | 22% | NJD -1.5 34% | 6.1 / 6.5 (over 44%) | Logan Thompson (expected) / Connor Hellebuyck (expected) | WSH +124 / NJD -148 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | TBL @ CBJ | TBL 4, CBJ 3 | TBL 51% | TBL -105 / CBJ +105 | 3.2 – 3.1 | 1–6 / 1–5 | 23% | TBL -1.5 31% | 6.2 / 6.5 (over 46%) | Dennis Hildeby (expected) / Jet Greaves (expected) | TBL -118 / CBJ -102 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:30 PM | DET @ FLA | DET 2, FLA 3 | FLA 58% | DET +140 / FLA -140 | 2.8 – 3.3 | 1–5 / 1–6 | 23% | FLA -1.5 36% | 6.1 / 5.5 (over 53%) | John Gibson (expected) / Jacob Markstrom (expected) | DET +142 / FLA -170 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | BUF @ CHI | BUF 4, CHI 3 | BUF 60% | BUF -150 / CHI +150 | 3.5 – 2.9 | 1–6 / 1–5 | 21% | BUF -1.5 39% | 6.4 / 6.5 (over 48%) | Colten Ellis (expected) / Spencer Knight (expected) | BUF -148 / CHI +124 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | WPG @ DAL | WPG 2, DAL 3 | DAL 61% | WPG +160 / DAL -160 | 2.6 – 3.3 | 1–5 / 1–6 | 22% | DAL -1.5 39% | 5.8 / 5.5 (over 49%) | Stuart Skinner (expected) / Jake Oettinger (expected) | WPG +154 / DAL -185 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:00 PM | STL @ UTA | STL 3, UTA 4 | UTA 54% | STL +115 / UTA -115 | 3.0 – 3.2 | 1–5 / 1–6 | 22% | UTA -1.5 32% | 6.2 / 6.5 (over 46%) | Joel Hofer (expected) / Karel Vejmelka (expected) | STL +114 / UTA -135 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | NYI @ LAK | NYI 2, LAK 3 | LAK 52% | NYI +110 / LAK -110 | 3.0 – 3.2 | 1–5 / 1–6 | 22% | LAK -1.5 32% | 6.2 / 5.5 (over 55%) | Ilya Sorokin (expected) / Darcy Kuemper (expected) | NYI +105 / LAK -125 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Friday, November 13

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9:00 PM | NYR @ VAN | NYR 4, VAN 3 | NYR 67% | NYR -205 / VAN +205 | 3.9 – 2.8 | 1–6 / 1–5 | 20% | NYR -1.5 46% | 6.6 | Dylan Garand (expected) / Leevi Meriläinen (expected) | – | no line yet (model fair VAN +1.5 -120 / NYR -1.5 +120) | no line yet | no line yet |
| 10:00 PM | NSH @ VGK | NSH 2, VGK 3 | VGK 61% | NSH +155 / VGK -155 | 2.7 – 3.4 | 1–5 / 1–6 | 22% | VGK -1.5 39% | 6.0 | Juuse Saros (expected) / Carter Hart (expected) | – | no line yet (model fair VGK -1.5 +155 / NSH +1.5 -155) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 292 | 0.6452 | 0.2269 | 62.7% | 1.36 | 1.78 | 90.2% |
| Model only (before blending) | 292 | 0.6479 | 0.2283 | 60.6% | – | – | – |
| Elo | 292 | 0.6610 | 0.2343 | 61.0% | – | – | – |
| Final prediction, games with a line | 158 | 0.6449 | 0.2268 | 62.0% | 1.33 | 1.81 | 90.8% |
| Model only, games with a line | 158 | 0.6500 | 0.2295 | 58.2% | – | – | – |
| Betting market (de-vigged moneyline) | 158 | 0.6441 | 0.2264 | 62.0% | – | 1.80 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.5% of regular-season games, happened in 22.3%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 2 | 0-2-0 | 2.2 | -2.16 | -100.0% | +9.4% |
| Moneyline | 8 | 4-4-0 | 8.7 | +1.83 | +21.2% | +6.4% |
| Total | 1 | 0-1-0 | 0.9 | -0.89 | -100.0% | +3.0% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 30 of 36 games (83%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Tuesday, November 10

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| COL @ TOR | 4–3 | 6–3 | 61% | yes | Mackenzie Blackwood / Sergei Bobrovsky |
| MIN @ MTL | 3–2 | 2–1 (OT) | 53% | yes | Jesper Wallstedt / Jacob Fowler |
| WSH @ OTT | 4–3 | 3–2 (OT) | 51% | yes | Logan Thompson / Samuel Ersson |
| NJD @ WPG | 3–2 | 2–4 | 45% | yes | Jake Allen / Nico Daws |
| FLA @ CBJ | 3–2 | 4–1 | 50% | yes | Jacob Markstrom / Cam Talbot |
| DET @ STL | 2–3 | 2–3 | 58% | yes | John Gibson / Joel Hofer |
| NSH @ LAK | 2–3 | 3–0 | 46% | no | Juuse Saros / Anton Forsberg |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.78 | +0.49 | +0.29 | 3.48 | 2.38 | 8.65 | 7.24 | 1585 |
| 2 | UTA | +0.45 | +0.25 | +0.21 | 3.18 | 2.39 | 8.20 | 8.77 | 1506 |
| 3 | TBL | +0.40 | +0.19 | +0.21 | 2.93 | 2.44 | 8.12 | 8.00 | 1544 |
| 4 | VGK | +0.29 | +0.04 | +0.25 | 2.68 | 2.40 | 9.18 | 7.27 | 1536 |
| 5 | MIN | +0.26 | +0.09 | +0.17 | 2.88 | 2.53 | 9.17 | 8.23 | 1552 |
| 6 | PIT | +0.24 | +0.17 | +0.07 | 3.00 | 2.58 | 7.82 | 8.01 | 1487 |
| 7 | COL | +0.23 | +0.27 | -0.04 | 2.96 | 2.80 | 7.86 | 7.95 | 1554 |
| 8 | DAL | +0.23 | -0.07 | +0.30 | 2.54 | 2.35 | 9.62 | 7.41 | 1529 |
| 9 | NJD | +0.22 | +0.03 | +0.19 | 2.82 | 2.45 | 9.14 | 7.90 | 1520 |
| 10 | STL | +0.14 | +0.04 | +0.11 | 2.76 | 2.59 | 7.03 | 8.13 | 1499 |
| 11 | BUF | +0.13 | +0.13 | -0.00 | 2.89 | 2.70 | 8.06 | 8.50 | 1516 |
| 12 | OTT | +0.13 | -0.00 | +0.13 | 2.75 | 2.54 | 8.07 | 8.16 | 1518 |
| 13 | FLA | +0.12 | -0.02 | +0.14 | 2.61 | 2.54 | 9.72 | 7.66 | 1504 |
| 14 | EDM | +0.09 | +0.06 | +0.03 | 2.53 | 2.67 | 9.57 | 8.36 | 1534 |
| 15 | BOS | +0.06 | +0.07 | -0.02 | 2.80 | 2.78 | 7.65 | 8.33 | 1543 |
| 16 | WSH | +0.04 | +0.13 | -0.08 | 2.92 | 2.82 | 7.77 | 8.08 | 1519 |
| 17 | NYR | +0.04 | +0.02 | +0.02 | 2.75 | 2.71 | 9.01 | 7.78 | 1493 |
| 18 | LAK | +0.01 | -0.10 | +0.12 | 2.59 | 2.58 | 8.30 | 8.22 | 1465 |
| 19 | MTL | -0.05 | +0.06 | -0.11 | 2.84 | 2.87 | 7.70 | 8.44 | 1534 |
| 20 | CBJ | -0.09 | -0.03 | -0.06 | 2.75 | 2.77 | 7.77 | 8.75 | 1488 |
| 21 | NSH | -0.09 | -0.06 | -0.03 | 2.65 | 2.76 | 8.33 | 7.73 | 1502 |
| 22 | TOR | -0.09 | -0.04 | -0.05 | 2.51 | 2.76 | 8.80 | 8.59 | 1468 |
| 23 | WPG | -0.10 | -0.12 | +0.02 | 2.54 | 2.69 | 8.37 | 8.82 | 1476 |
| 24 | DET | -0.11 | -0.11 | -0.00 | 2.66 | 2.70 | 8.77 | 8.79 | 1475 |
| 25 | NYI | -0.16 | -0.02 | -0.14 | 2.81 | 2.91 | 7.59 | 8.67 | 1480 |
| 26 | PHI | -0.22 | -0.25 | +0.03 | 2.36 | 2.66 | 7.83 | 7.43 | 1472 |
| 27 | CGY | -0.24 | -0.12 | -0.12 | 2.57 | 2.85 | 7.26 | 8.10 | 1464 |
| 28 | SEA | -0.31 | -0.12 | -0.20 | 2.44 | 2.94 | 7.29 | 8.68 | 1478 |
| 29 | ANA | -0.36 | +0.01 | -0.36 | 2.69 | 3.10 | 8.13 | 8.50 | 1495 |
| 30 | CHI | -0.68 | -0.29 | -0.39 | 2.30 | 3.11 | 7.27 | 8.52 | 1416 |
| 31 | VAN | -0.71 | -0.27 | -0.44 | 2.21 | 3.17 | 7.75 | 8.79 | 1398 |
| 32 | SJS | -0.73 | -0.24 | -0.49 | 2.35 | 3.23 | 7.38 | 9.34 | 1450 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 70% | +0.40 | +0.17 |
| WSH | Logan Thompson | 78% | +0.38 | +0.16 |
| BOS | Jeremy Swayman | 69% | +0.36 | +0.15 |
| MTL | Jacob Fowler | 67% | +0.33 | +0.14 |
| MIN | Jesper Wallstedt | 83% | +0.30 | +0.12 |
| COL | Mackenzie Blackwood | 75% | +0.19 | +0.08 |
| TBL | Andrei Vasilevskiy | 76% | +0.13 | +0.06 |
| STL | Joel Hofer | 74% | +0.09 | +0.04 |
| DAL | Jake Oettinger | 76% | +0.08 | +0.03 |
| EDM | Devon Levi | 43% | +0.03 | +0.01 |
| CAR | Pyotr Kochetkov | 69% | +0.03 | +0.01 |
| CHI | Spencer Knight | 77% | +0.02 | +0.01 |
| NYR | Dylan Garand | 70% | -0.03 | -0.01 |
| NSH | Justus Annunen | 47% | -0.06 | -0.02 |
| WPG | Stuart Skinner | 68% | -0.06 | -0.03 |
| PHI | Dan Vladar | 51% | -0.08 | -0.03 |
| NJD | Jake Allen | 49% | -0.10 | -0.04 |
| BUF | Ukko-Pekka Luukkonen | 54% | -0.11 | -0.05 |
| DET | John Gibson | 59% | -0.16 | -0.07 |
| CBJ | Cam Talbot | 55% | -0.18 | -0.08 |
| SEA | Joey Daccord | 51% | -0.20 | -0.08 |
| SJS | Yaroslav Askarov | 65% | -0.20 | -0.08 |
| TOR | Sergei Bobrovsky | 66% | -0.20 | -0.08 |
| ANA | Lukas Dostal | 46% | -0.20 | -0.08 |
| UTA | Karel Vejmelka | 63% | -0.22 | -0.09 |
| LAK | Darcy Kuemper | 59% | -0.23 | -0.10 |
| CGY | Dustin Wolf | 49% | -0.26 | -0.11 |
| FLA | Jacob Markstrom | 53% | -0.26 | -0.11 |
| VGK | Adin Hill | 52% | -0.27 | -0.11 |
| VAN | Leevi Meriläinen | 69% | -0.38 | -0.16 |
| PIT | Arturs Silovs | 68% | -0.40 | -0.17 |
| OTT | Samuel Ersson | 46% | -0.52 | -0.22 |

## Current model fit

- Fitted on 5884 games from 2022-23 to 2026-27.
- Home ice: +3.0% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.9% goals scored, +3.5% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 21%.
- Blend: 45% on the betting line wherever there is one (fitted on 158 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.04 goals per five minutes.
