# NHL score predictions

Updated Mon Nov 02, 2026 01:55 AM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Monday, November 2

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | VGK @ BOS | VGK 4, BOS 3 | VGK 51% | VGK -100 / BOS +100 | 3.2 – 3.1 | 1–6 / 1–6 | 22% | VGK -1.5 31% | 6.4 / 6.5 (over 47%) | Carter Hart (expected) / Jeremy Swayman (expected) | VGK -112 / BOS -108 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | DET @ FLA | DET 2, FLA 3 | FLA 58% | DET +140 / FLA -140 | 2.7 – 3.3 | 1–5 / 1–6 | 22% | FLA -1.5 37% | 6.0 / 5.5 (over 53%) | John Gibson (expected) / Akira Schmid (expected) | DET +145 / FLA -175 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | COL @ CHI | COL 4, CHI 3 | COL 67% | COL -205 / CHI +205 | 3.8 – 2.7 | 1–6 / 1–5 | 20% | COL -1.5 46% | 6.5 / 6.5 (over 50%) | Mackenzie Blackwood (expected) / Spencer Knight (expected) | COL -230 / CHI +190 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:00 PM | CGY @ SJS | CGY 4, SJS 3 | CGY 51% | CGY -105 / SJS +105 | 3.3 – 3.3 | 1–6 / 1–6 | 22% | CGY -1.5 31% | 6.6 / 6.5 (over 52%) | Dustin Wolf (expected) / Yaroslav Askarov (expected) | CGY +114 / SJS -135 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Tuesday, November 3

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | UTA @ TOR | UTA 4, TOR 3 | UTA 60% | UTA -150 / TOR +150 | 3.6 – 3.0 | 1–6 / 1–5 | 21% | UTA -1.5 39% | 6.6 | Karel Vejmelka (expected) / Sergei Bobrovsky (expected) | – | no line yet (model fair TOR +1.5 -155 / UTA -1.5 +155) | no line yet | no line yet |
| 7:00 PM | WPG @ MTL | WPG 2, MTL 3 | MTL 59% | WPG +140 / MTL -140 | 2.8 – 3.4 | 1–5 / 1–6 | 22% | MTL -1.5 36% | 6.2 | Stuart Skinner (expected) / Jacob Fowler (expected) | – | no line yet (model fair MTL -1.5 +175 / WPG +1.5 -175) | no line yet | no line yet |
| 7:00 PM | DET @ TBL | DET 2, TBL 3 | TBL 67% | DET +205 / TBL -205 | 2.5 – 3.6 | 1–5 / 1–6 | 21% | TBL -1.5 45% | 6.1 | Daniil Tarasov (expected) / Andrei Vasilevskiy (expected) | – | no line yet (model fair TBL -1.5 +125 / DET +1.5 -125) | no line yet | no line yet |
| 7:00 PM | STL @ NYR | STL 4, NYR 3 | STL 51% | STL -105 / NYR +105 | 3.2 – 3.1 | 1–6 / 1–6 | 22% | STL -1.5 30% | 6.3 | Joel Hofer (expected) / James Reimer (expected) | – | no line yet (model fair NYR +1.5 -235 / STL -1.5 +235) | no line yet | no line yet |
| 7:00 PM | MIN @ PHI | MIN 3, PHI 2 | MIN 63% | MIN -170 / PHI +170 | 3.4 – 2.6 | 1–6 / 1–5 | 22% | MIN -1.5 41% | 6.0 | Jesper Wallstedt (expected) / Joseph Woll (expected) | – | no line yet (model fair PHI +1.5 -145 / MIN -1.5 +145) | no line yet | no line yet |
| 7:00 PM | VGK @ PIT | VGK 3, PIT 4 | PIT 56% | VGK +125 / PIT -125 | 3.0 – 3.4 | 1–5 / 1–6 | 22% | PIT -1.5 35% | 6.5 | Adin Hill (expected) / Arturs Silovs (expected) | – | no line yet (model fair PIT -1.5 +180 / VGK +1.5 -180) | no line yet | no line yet |
| 7:00 PM | DAL @ WSH | DAL 2, WSH 3 | WSH 51% | DAL +105 / WSH -105 | 2.9 – 2.9 | 1–5 / 1–5 | 23% | WSH -1.5 29% | 5.8 | Jake Oettinger (expected) / Logan Thompson (expected) | – | no line yet (model fair WSH -1.5 +240 / DAL +1.5 -240) | no line yet | no line yet |
| 7:00 PM | COL @ CBJ | COL 4, CBJ 3 | COL 52% | COL -110 / CBJ +110 | 3.2 – 3.1 | 1–6 / 1–5 | 22% | COL -1.5 31% | 6.3 | Scott Wedgewood (expected) / Jet Greaves (expected) | – | no line yet (model fair CBJ +1.5 -220 / COL -1.5 +220) | no line yet | no line yet |
| 7:30 PM | EDM @ NJD | EDM 3, NJD 4 | NJD 59% | EDM +145 / NJD -145 | 2.9 – 3.5 | 1–5 / 1–6 | 21% | NJD -1.5 38% | 6.3 | Tristan Jarry (expected) / Connor Hellebuyck (expected) | – | no line yet (model fair NJD -1.5 +165 / EDM +1.5 -165) | no line yet | no line yet |
| 8:00 PM | CAR @ NSH | CAR 4, NSH 3 | CAR 67% | CAR -200 / NSH +200 | 3.8 – 2.7 | 1–6 / 1–5 | 20% | CAR -1.5 45% | 6.5 | Pyotr Kochetkov (expected) / Juuse Saros (expected) | – | no line yet (model fair NSH +1.5 -125 / CAR -1.5 +125) | no line yet | no line yet |
| 9:00 PM | ANA @ VAN | ANA 4, VAN 3 | ANA 58% | ANA -135 / VAN +135 | 3.8 – 3.3 | 1–6 / 1–6 | 21% | ANA -1.5 37% | 7.1 | Lukas Dostal (expected) / Leevi Meriläinen (expected) | – | no line yet (model fair VAN +1.5 -170 / ANA -1.5 +170) | no line yet | no line yet |

\* price not posted; assumed -110.

## Wednesday, November 4

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:30 PM | OTT @ BUF | OTT 3, BUF 4 | BUF 55% | OTT +120 / BUF -120 | 3.0 – 3.4 | 1–5 / 1–6 | 21% | BUF -1.5 35% | 6.5 | Samuel Ersson (expected) / Ukko-Pekka Luukkonen (expected) | – | no line yet (model fair BUF -1.5 +185 / OTT +1.5 -185) | no line yet | no line yet |
| 7:30 PM | CHI @ FLA | CHI 3, FLA 4 | FLA 71% | CHI +245 / FLA -245 | 2.4 – 3.8 | 1–5 / 1–6 | 20% | FLA -1.5 49% | 6.2 | Spencer Knight (expected) / Akira Schmid (expected) | – | no line yet (model fair FLA -1.5 +100 / CHI +1.5 -100) | no line yet | no line yet |
| 10:00 PM | SJS @ LAK | SJS 3, LAK 4 | LAK 65% | SJS +185 / LAK -185 | 2.7 – 3.7 | 1–5 / 1–6 | 21% | LAK -1.5 44% | 6.4 | Yaroslav Askarov (expected) / Darcy Kuemper (expected) | – | no line yet (model fair LAK -1.5 +130 / SJS +1.5 -130) | no line yet | no line yet |
| 10:00 PM | CGY @ SEA | CGY 3, SEA 4 | SEA 53% | CGY +115 / SEA -115 | 3.1 – 3.4 | 1–5 / 1–6 | 22% | SEA -1.5 33% | 6.5 | Dustin Wolf (expected) / Philipp Grubauer (expected) | – | no line yet (model fair SEA -1.5 +205 / CGY +1.5 -205) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 226 | 0.6489 | 0.2285 | 61.9% | 1.39 | 1.79 | 89.6% |
| Model only (before blending) | 226 | 0.6509 | 0.2295 | 60.6% | – | – | – |
| Elo | 226 | 0.6648 | 0.2360 | 61.9% | – | – | – |
| Final prediction, games with a line | 92 | 0.6537 | 0.2307 | 59.8% | 1.38 | 1.85 | 89.7% |
| Model only, games with a line | 92 | 0.6588 | 0.2333 | 56.5% | – | – | – |
| Betting market (de-vigged moneyline) | 92 | 0.6553 | 0.2315 | 62.0% | – | 1.82 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.6% of regular-season games, happened in 22.6%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 1 | 0-1-0 | 1.3 | -1.29 | -100.0% | +11.8% |
| Moneyline | 7 | 3-4-0 | 7.0 | +0.13 | +1.9% | +6.3% |
| Total | 1 | 0-1-0 | 0.9 | -0.89 | -100.0% | +3.0% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 14 of 17 games (82%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Saturday, October 31

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| CHI @ BOS | 3–4 | 4–5 (OT) | 70% | yes | Arvid Soderblom / Jeremy Swayman |
| STL @ DET | 3–2 | 5–4 | 52% | yes | Joel Hofer / John Gibson |
| TBL @ NSH | 4–3 | 4–5 (SO) | 39% | yes | Andrei Vasilevskiy / Juuse Saros |
| EDM @ NYI | 3–4 | 4–0 | 49% | no | Tristan Jarry / Ilya Sorokin |
| BUF @ LAK | 3–2 | 3–2 | 53% | yes | Colten Ellis / Darcy Kuemper |
| OTT @ SJS | 4–3 | 5–1 | 60% | yes | Samuel Ersson / Yaroslav Askarov |
| PIT @ MTL | 3–4 | 4–5 | 52% | yes | Sergei Murashov / Jacob Fowler |
| TOR @ VAN | 4–3 | 4–2 | 64% | yes | Anthony Stolarz / Kevin Lankinen |
| CBJ @ DAL | 2–3 | 1–3 | 64% | yes | Jet Greaves / Jake Oettinger |
| CGY @ COL | 3–4 | 2–5 | 72% | yes | Arsenii Sergeev / Mackenzie Blackwood |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.67 | +0.40 | +0.27 | 3.38 | 2.39 | 8.13 | 6.86 | 1580 |
| 2 | UTA | +0.47 | +0.25 | +0.22 | 3.17 | 2.38 | 8.01 | 8.40 | 1515 |
| 3 | TBL | +0.36 | +0.20 | +0.16 | 2.92 | 2.51 | 8.18 | 7.82 | 1538 |
| 4 | MIN | +0.35 | +0.14 | +0.21 | 3.01 | 2.45 | 9.21 | 8.14 | 1538 |
| 5 | VGK | +0.33 | +0.07 | +0.26 | 2.74 | 2.38 | 8.89 | 7.36 | 1527 |
| 6 | COL | +0.29 | +0.30 | -0.00 | 2.99 | 2.74 | 7.75 | 7.86 | 1552 |
| 7 | FLA | +0.27 | +0.01 | +0.26 | 2.64 | 2.38 | 9.23 | 7.59 | 1507 |
| 8 | PIT | +0.26 | +0.22 | +0.04 | 3.07 | 2.62 | 7.98 | 7.66 | 1495 |
| 9 | NJD | +0.26 | +0.03 | +0.23 | 2.83 | 2.38 | 9.01 | 7.79 | 1511 |
| 10 | DAL | +0.21 | -0.11 | +0.32 | 2.47 | 2.31 | 9.26 | 7.30 | 1527 |
| 11 | STL | +0.11 | +0.00 | +0.10 | 2.65 | 2.58 | 6.86 | 7.39 | 1508 |
| 12 | BUF | +0.10 | +0.10 | -0.00 | 2.78 | 2.69 | 7.87 | 8.33 | 1521 |
| 13 | EDM | +0.08 | +0.11 | -0.03 | 2.58 | 2.72 | 9.71 | 8.03 | 1529 |
| 14 | OTT | +0.06 | -0.04 | +0.10 | 2.64 | 2.58 | 8.05 | 8.23 | 1520 |
| 15 | WSH | +0.04 | +0.11 | -0.07 | 2.88 | 2.79 | 7.76 | 8.08 | 1523 |
| 16 | NYR | +0.03 | +0.03 | -0.00 | 2.72 | 2.72 | 8.59 | 7.75 | 1493 |
| 17 | LAK | +0.02 | -0.11 | +0.14 | 2.57 | 2.54 | 8.08 | 8.21 | 1471 |
| 18 | DET | -0.01 | -0.08 | +0.07 | 2.67 | 2.59 | 8.38 | 8.49 | 1483 |
| 19 | MTL | -0.03 | +0.05 | -0.08 | 2.82 | 2.81 | 7.09 | 8.29 | 1534 |
| 20 | BOS | -0.03 | +0.05 | -0.08 | 2.77 | 2.84 | 7.69 | 8.07 | 1530 |
| 21 | CBJ | -0.08 | -0.09 | +0.02 | 2.61 | 2.66 | 7.69 | 8.51 | 1488 |
| 22 | NYI | -0.08 | -0.07 | -0.01 | 2.70 | 2.74 | 7.48 | 8.49 | 1490 |
| 23 | TOR | -0.11 | -0.01 | -0.11 | 2.51 | 2.82 | 8.76 | 8.20 | 1486 |
| 24 | WPG | -0.14 | -0.13 | -0.01 | 2.53 | 2.73 | 8.13 | 8.78 | 1465 |
| 25 | NSH | -0.14 | -0.06 | -0.08 | 2.64 | 2.80 | 7.82 | 7.50 | 1482 |
| 26 | CGY | -0.22 | -0.09 | -0.13 | 2.62 | 2.85 | 7.28 | 8.09 | 1465 |
| 27 | SEA | -0.26 | -0.10 | -0.15 | 2.43 | 2.87 | 7.17 | 8.49 | 1478 |
| 28 | PHI | -0.31 | -0.27 | -0.04 | 2.35 | 2.75 | 7.75 | 7.57 | 1471 |
| 29 | ANA | -0.38 | -0.02 | -0.37 | 2.75 | 3.09 | 7.92 | 8.54 | 1474 |
| 30 | CHI | -0.69 | -0.26 | -0.43 | 2.39 | 3.17 | 7.10 | 8.29 | 1430 |
| 31 | VAN | -0.73 | -0.22 | -0.51 | 2.30 | 3.25 | 7.63 | 8.75 | 1411 |
| 32 | SJS | -0.83 | -0.24 | -0.59 | 2.32 | 3.33 | 7.24 | 8.88 | 1461 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| WSH | Logan Thompson | 63% | +0.45 | +0.19 |
| NYI | Ilya Sorokin | 71% | +0.39 | +0.16 |
| BOS | Jeremy Swayman | 71% | +0.31 | +0.13 |
| MTL | Jacob Fowler | 62% | +0.30 | +0.13 |
| CGY | Devin Cooley | 52% | +0.21 | +0.09 |
| MIN | Jesper Wallstedt | 85% | +0.17 | +0.07 |
| COL | Mackenzie Blackwood | 71% | +0.16 | +0.07 |
| OTT | Linus Ullmark | 44% | +0.14 | +0.06 |
| CHI | Spencer Knight | 79% | +0.14 | +0.06 |
| DAL | Jake Oettinger | 80% | +0.14 | +0.06 |
| TBL | Andrei Vasilevskiy | 77% | +0.13 | +0.05 |
| CBJ | Jet Greaves | 57% | +0.10 | +0.04 |
| WPG | Stuart Skinner | 62% | +0.02 | +0.01 |
| STL | Joel Hofer | 73% | +0.00 | +0.00 |
| CAR | Pyotr Kochetkov | 66% | -0.02 | -0.01 |
| NYR | Dylan Garand | 63% | -0.05 | -0.02 |
| NJD | Jake Allen | 54% | -0.06 | -0.02 |
| PHI | Joseph Woll | 54% | -0.07 | -0.03 |
| BUF | Ukko-Pekka Luukkonen | 63% | -0.13 | -0.05 |
| SJS | Yaroslav Askarov | 57% | -0.13 | -0.06 |
| UTA | Karel Vejmelka | 70% | -0.15 | -0.06 |
| DET | John Gibson | 71% | -0.16 | -0.07 |
| FLA | Akira Schmid | 58% | -0.16 | -0.07 |
| TOR | Sergei Bobrovsky | 61% | -0.16 | -0.07 |
| ANA | Lukas Dostal | 65% | -0.17 | -0.07 |
| SEA | Philipp Grubauer | 63% | -0.19 | -0.08 |
| LAK | Darcy Kuemper | 58% | -0.21 | -0.09 |
| NSH | Juuse Saros | 66% | -0.24 | -0.10 |
| PIT | Arturs Silovs | 64% | -0.29 | -0.12 |
| VAN | Leevi Meriläinen | 65% | -0.29 | -0.12 |
| EDM | Tristan Jarry | 57% | -0.32 | -0.14 |
| VGK | Adin Hill | 52% | -0.35 | -0.15 |

## Current model fit

- Fitted on 5818 games from 2022-23 to 2026-27.
- Home ice: +3.1% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.7% goals scored, +3.3% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 23%.
- Blend: 50% on the betting line wherever there is one (fitted on 92 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
