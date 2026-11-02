# NHL score predictions

Updated Mon Nov 02, 2026 06:38 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Monday, November 2

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | VGK @ BOS | VGK 4, BOS 3 | VGK 52% | VGK -110 / BOS +110 | 3.2 – 3.1 | 1–6 / 1–5 | 22% | VGK -1.5 31% | 6.3 / 6.5 (over 47%) | Carter Hart (expected) / Jeremy Swayman (confirmed) | VGK -118 / BOS -102 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | DET @ FLA | DET 2, FLA 3 | FLA 61% | DET +155 / FLA -155 | 2.7 – 3.3 | 1–5 / 1–6 | 22% | FLA -1.5 38% | 6.0 / 5.5 (over 52%) | Daniil Tarasov (confirmed) / Jacob Markstrom (confirmed) | DET +154 / FLA -185 | no edge | no edge | no edge |
| 8:00 PM | COL @ CHI | COL 4, CHI 3 | COL 68% | COL -210 / CHI +210 | 3.8 – 2.7 | 1–6 / 1–5 | 19% | COL -1.5 46% | 6.5 / 6.5 (over 49%) | Mackenzie Blackwood (confirmed) / Spencer Knight (confirmed) | COL -230 / CHI +190 | no edge | no edge | no edge |
| 9:00 PM | CGY @ SJS | CGY 4, SJS 3 | CGY 52% | CGY -110 / SJS +110 | 3.4 – 3.2 | 1–6 / 1–6 | 22% | CGY -1.5 32% | 6.6 / 6.5 (over 51%) | Dustin Wolf (confirmed) / Yaroslav Askarov (confirmed) | CGY +105 / SJS -125 | no edge | CGY (+105): EV +6.8%, 52%, stake 1.6u | no edge |

## Tuesday, November 3

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | UTA @ TOR | UTA 4, TOR 3 | UTA 56% | UTA -125 / TOR +125 | 3.5 – 3.1 | 1–6 / 1–5 | 21% | UTA -1.5 35% | 6.6 / 6.5 (over 50%) | Karel Vejmelka (expected) / Sergei Bobrovsky (confirmed) | UTA -130 / TOR +110 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | WPG @ MTL | WPG 2, MTL 3 | MTL 60% | WPG +155 / MTL -155 | 2.8 – 3.4 | 1–5 / 1–6 | 22% | MTL -1.5 39% | 6.2 / 5.5 (over 55%) | Stuart Skinner (expected) / Jacob Fowler (expected) | WPG +150 / MTL -180 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | DET @ TBL | DET 2, TBL 3 | TBL 70% | DET +230 / TBL -230 | 2.5 – 3.8 | 1–5 / 1–6 | 20% | TBL -1.5 48% | 6.2 / 6.5 (over 45%) | John Gibson (expected) / Andrei Vasilevskiy (expected) | DET +225 / TBL -278 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | STL @ NYR | STL 3, NYR 4 | NYR 52% | STL +105 / NYR -105 | 3.0 – 3.1 | 1–5 / 1–5 | 22% | NYR -1.5 31% | 6.2 / 5.5 (over 56%) | Joel Hofer (expected) / Dylan Garand (expected) | STL +105 / NYR -125 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | MIN @ PHI | MIN 3, PHI 2 | MIN 61% | MIN -155 / PHI +155 | 3.4 – 2.7 | 1–6 / 1–5 | 22% | MIN -1.5 39% | 6.1 / 5.5 (over 53%) | Jesper Wallstedt (expected) / Joseph Woll (expected) | MIN -170 / PHI +142 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | VGK @ PIT | VGK 3, PIT 4 | PIT 53% | VGK +115 / PIT -115 | 3.2 – 3.4 | 1–6 / 1–6 | 21% | PIT -1.5 33% | 6.5 / 6.5 (over 50%) | Adin Hill (expected) / Arturs Silovs (expected) | VGK -112 / PIT -108 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | DAL @ WSH | DAL 2, WSH 3 | WSH 51% | DAL +100 / WSH -100 | 2.9 – 2.9 | 1–5 / 1–5 | 23% | WSH -1.5 29% | 5.8 / 5.5 (over 49%) | Jake Oettinger (expected) / Logan Thompson (expected) | DAL -108 / WSH -112 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | COL @ CBJ | COL 4, CBJ 3 | COL 54% | COL -115 / CBJ +115 | 3.3 – 3.0 | 1–6 / 1–5 | 23% | COL -1.5 32% | 6.3 / 6.5 (over 47%) | Scott Wedgewood (confirmed) / Jet Greaves (expected) | COL -130 / CBJ +110 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:30 PM | EDM @ NJD | EDM 3, NJD 4 | NJD 59% | EDM +145 / NJD -145 | 2.9 – 3.5 | 1–5 / 1–6 | 22% | NJD -1.5 38% | 6.3 / 6.5 (over 47%) | Tristan Jarry (expected) / Connor Hellebuyck (expected) | EDM +130 / NJD -155 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | CAR @ NSH | CAR 4, NSH 3 | CAR 65% | CAR -190 / NSH +190 | 3.7 – 2.7 | 1–6 / 1–5 | 20% | CAR -1.5 45% | 6.5 / 6.5 (over 49%) | Pyotr Kochetkov (expected) / Juuse Saros (expected) | CAR -192 / NSH +160 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:00 PM | ANA @ VAN | ANA 4, VAN 3 | ANA 58% | ANA -140 / VAN +140 | 3.8 – 3.2 | 1–6 / 1–6 | 21% | ANA -1.5 38% | 6.9 / 6.5 (over 57%) | Lukas Dostal (expected) / Leevi Meriläinen (expected) | ANA -148 / VAN +124 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Wednesday, November 4

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:30 PM | OTT @ BUF | OTT 3, BUF 4 | BUF 55% | OTT +125 / BUF -125 | 3.1 – 3.4 | 1–5 / 1–6 | 21% | BUF -1.5 34% | 6.5 | Samuel Ersson (expected) / Ukko-Pekka Luukkonen (expected) | – | no line yet (model fair BUF -1.5 +190 / OTT +1.5 -190) | no line yet | no line yet |
| 7:30 PM | CHI @ FLA | CHI 2, FLA 3 | FLA 70% | CHI +235 / FLA -235 | 2.5 – 3.8 | 1–5 / 1–6 | 19% | FLA -1.5 49% | 6.3 | Spencer Knight (expected) / Jacob Markstrom (expected) | – | no line yet (model fair FLA -1.5 +105 / CHI +1.5 -105) | no line yet | no line yet |
| 10:00 PM | SJS @ LAK | SJS 3, LAK 4 | LAK 65% | SJS +185 / LAK -185 | 2.7 – 3.7 | 1–5 / 1–6 | 20% | LAK -1.5 44% | 6.4 | Yaroslav Askarov (expected) / Darcy Kuemper (expected) | – | no line yet (model fair LAK -1.5 +130 / SJS +1.5 -130) | no line yet | no line yet |
| 10:00 PM | CGY @ SEA | CGY 3, SEA 4 | SEA 53% | CGY +115 / SEA -115 | 3.2 – 3.4 | 1–6 / 1–6 | 21% | SEA -1.5 33% | 6.5 | Dustin Wolf (expected) / Philipp Grubauer (expected) | – | no line yet (model fair SEA -1.5 +200 / CGY +1.5 -200) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 231 | 0.6500 | 0.2291 | 61.5% | 1.40 | 1.79 | 89.2% |
| Model only (before blending) | 231 | 0.6519 | 0.2300 | 60.2% | – | – | – |
| Elo | 231 | 0.6645 | 0.2359 | 61.5% | – | – | – |
| Final prediction, games with a line | 97 | 0.6562 | 0.2320 | 58.8% | 1.41 | 1.84 | 88.7% |
| Model only, games with a line | 97 | 0.6607 | 0.2343 | 55.7% | – | – | – |
| Betting market (de-vigged moneyline) | 97 | 0.6575 | 0.2326 | 60.8% | – | 1.80 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.6% of regular-season games, happened in 22.1%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 1 | 0-1-0 | 1.3 | -1.29 | -100.0% | +11.8% |
| Moneyline | 7 | 3-4-0 | 7.0 | +0.13 | +1.9% | +6.3% |
| Total | 1 | 0-1-0 | 0.9 | -0.89 | -100.0% | +3.0% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 15 of 18 games (83%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Sunday, November 1

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| WPG @ CAR | 3–4 | 0–7 | 69% | no | Stuart Skinner / Pyotr Kochetkov |
| MIN @ WSH | 4–3 | 5–1 | 51% | yes | Jesper Wallstedt / Logan Thompson |
| UTA @ PHI | 4–3 | 3–6 | 38% | no | Karel Vejmelka / Dan Vladar |
| EDM @ NYR | 3–4 | 4–1 | 45% | yes | Matt Tomkins / Dylan Garand |
| OTT @ ANA | 4–3 | 3–6 | 49% | yes | Jonas Johansson / Laurent Brossoit |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.70 | +0.43 | +0.27 | 3.39 | 2.39 | 8.38 | 6.88 | 1585 |
| 2 | UTA | +0.45 | +0.22 | +0.23 | 3.12 | 2.35 | 7.93 | 8.37 | 1509 |
| 3 | TBL | +0.35 | +0.20 | +0.16 | 2.92 | 2.51 | 8.18 | 7.82 | 1538 |
| 4 | MIN | +0.33 | +0.14 | +0.20 | 2.98 | 2.47 | 9.16 | 8.11 | 1545 |
| 5 | VGK | +0.32 | +0.07 | +0.25 | 2.74 | 2.38 | 8.89 | 7.36 | 1527 |
| 6 | COL | +0.29 | +0.30 | -0.00 | 2.99 | 2.74 | 7.75 | 7.86 | 1552 |
| 7 | FLA | +0.26 | +0.01 | +0.26 | 2.64 | 2.37 | 9.23 | 7.58 | 1507 |
| 8 | PIT | +0.26 | +0.22 | +0.04 | 3.07 | 2.63 | 7.97 | 7.65 | 1495 |
| 9 | NJD | +0.26 | +0.03 | +0.23 | 2.84 | 2.38 | 9.01 | 7.79 | 1511 |
| 10 | DAL | +0.21 | -0.11 | +0.32 | 2.46 | 2.31 | 9.25 | 7.30 | 1527 |
| 11 | STL | +0.11 | +0.00 | +0.10 | 2.64 | 2.57 | 6.85 | 7.38 | 1508 |
| 12 | EDM | +0.10 | +0.11 | -0.01 | 2.60 | 2.71 | 9.68 | 7.98 | 1535 |
| 13 | BUF | +0.10 | +0.10 | -0.00 | 2.78 | 2.69 | 7.88 | 8.33 | 1521 |
| 14 | WSH | +0.07 | +0.11 | -0.04 | 2.91 | 2.75 | 7.73 | 8.01 | 1517 |
| 15 | OTT | +0.07 | -0.03 | +0.10 | 2.64 | 2.56 | 7.98 | 8.27 | 1514 |
| 16 | LAK | +0.02 | -0.11 | +0.14 | 2.57 | 2.54 | 8.07 | 8.21 | 1471 |
| 17 | NYR | -0.01 | +0.01 | -0.02 | 2.70 | 2.74 | 8.54 | 7.72 | 1487 |
| 18 | DET | -0.01 | -0.08 | +0.07 | 2.66 | 2.59 | 8.38 | 8.49 | 1483 |
| 19 | MTL | -0.02 | +0.05 | -0.08 | 2.82 | 2.80 | 7.09 | 8.28 | 1534 |
| 20 | BOS | -0.03 | +0.05 | -0.08 | 2.77 | 2.84 | 7.69 | 8.06 | 1530 |
| 21 | CBJ | -0.08 | -0.09 | +0.01 | 2.60 | 2.67 | 7.68 | 8.51 | 1488 |
| 22 | NYI | -0.08 | -0.07 | -0.01 | 2.70 | 2.74 | 7.48 | 8.49 | 1490 |
| 23 | TOR | -0.12 | -0.01 | -0.11 | 2.51 | 2.82 | 8.76 | 8.20 | 1486 |
| 24 | NSH | -0.14 | -0.06 | -0.08 | 2.63 | 2.80 | 7.81 | 7.50 | 1482 |
| 25 | WPG | -0.16 | -0.14 | -0.02 | 2.53 | 2.74 | 8.15 | 9.03 | 1460 |
| 26 | CGY | -0.22 | -0.09 | -0.13 | 2.62 | 2.84 | 7.28 | 8.09 | 1465 |
| 27 | SEA | -0.26 | -0.10 | -0.15 | 2.43 | 2.87 | 7.17 | 8.49 | 1478 |
| 28 | PHI | -0.27 | -0.26 | -0.01 | 2.32 | 2.70 | 7.72 | 7.49 | 1477 |
| 29 | ANA | -0.37 | -0.01 | -0.37 | 2.73 | 3.08 | 7.97 | 8.47 | 1480 |
| 30 | CHI | -0.69 | -0.26 | -0.43 | 2.39 | 3.17 | 7.09 | 8.29 | 1430 |
| 31 | VAN | -0.73 | -0.22 | -0.51 | 2.29 | 3.24 | 7.63 | 8.74 | 1411 |
| 32 | SJS | -0.82 | -0.24 | -0.58 | 2.32 | 3.33 | 7.24 | 8.87 | 1461 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| WSH | Logan Thompson | 68% | +0.42 | +0.18 |
| NYI | Ilya Sorokin | 71% | +0.39 | +0.16 |
| BOS | Jeremy Swayman | 71% | +0.31 | +0.13 |
| MTL | Jacob Fowler | 62% | +0.30 | +0.13 |
| MIN | Jesper Wallstedt | 87% | +0.22 | +0.09 |
| CGY | Devin Cooley | 52% | +0.21 | +0.09 |
| COL | Mackenzie Blackwood | 71% | +0.16 | +0.07 |
| OTT | Linus Ullmark | 40% | +0.14 | +0.06 |
| CHI | Spencer Knight | 79% | +0.14 | +0.06 |
| DAL | Jake Oettinger | 80% | +0.14 | +0.06 |
| TBL | Andrei Vasilevskiy | 77% | +0.13 | +0.05 |
| CBJ | Jet Greaves | 57% | +0.10 | +0.04 |
| CAR | Pyotr Kochetkov | 69% | +0.05 | +0.02 |
| STL | Joel Hofer | 73% | +0.01 | +0.00 |
| WPG | Stuart Skinner | 66% | -0.01 | -0.01 |
| PHI | Dan Vladar | 52% | -0.03 | -0.01 |
| NJD | Jake Allen | 54% | -0.06 | -0.02 |
| NYR | Dylan Garand | 67% | -0.06 | -0.02 |
| BUF | Ukko-Pekka Luukkonen | 63% | -0.13 | -0.05 |
| SJS | Yaroslav Askarov | 57% | -0.13 | -0.05 |
| DET | John Gibson | 71% | -0.16 | -0.07 |
| FLA | Akira Schmid | 58% | -0.16 | -0.07 |
| TOR | Sergei Bobrovsky | 61% | -0.16 | -0.07 |
| ANA | Lukas Dostal | 57% | -0.17 | -0.07 |
| SEA | Philipp Grubauer | 63% | -0.19 | -0.08 |
| LAK | Darcy Kuemper | 58% | -0.20 | -0.09 |
| UTA | Karel Vejmelka | 74% | -0.21 | -0.09 |
| NSH | Juuse Saros | 66% | -0.24 | -0.10 |
| PIT | Arturs Silovs | 64% | -0.29 | -0.12 |
| VAN | Leevi Meriläinen | 65% | -0.29 | -0.12 |
| EDM | Tristan Jarry | 51% | -0.32 | -0.14 |
| VGK | Adin Hill | 52% | -0.35 | -0.15 |

## Current model fit

- Fitted on 5823 games from 2022-23 to 2026-27.
- Home ice: +3.1% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.7% goals scored, +3.3% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 23%.
- Blend: 50% on the betting line wherever there is one (fitted on 97 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
