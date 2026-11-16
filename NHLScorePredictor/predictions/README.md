# NHL score predictions

Updated Mon Nov 16, 2026 02:23 AM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Monday, November 16

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:30 PM | MTL @ NYR | MTL 2, NYR 3 | NYR 51% | MTL +105 / NYR -105 | 3.1 – 3.1 | 1–5 / 1–6 | 22% | NYR -1.5 30% | 6.2 / 6.5 (over 45%) | Jacob Fowler (expected) / Joonas Korpisalo (expected) | MTL -110 / NYR -110 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:30 PM | VAN @ UTA | VAN 2, UTA 5 | UTA 78% | VAN +355 / UTA -355 | 2.4 – 4.3 | 0–5 / 2–7 | 17% | UTA -1.5 58% | 6.7 / 6.5 (over 53%) | Kevin Lankinen (expected) / Karel Vejmelka (expected) | VAN +270 / UTA -340 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Tuesday, November 17

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | LAK @ BOS | LAK 2, BOS 3 | BOS 63% | LAK +170 / BOS -170 | 2.6 – 3.4 | 1–5 / 1–6 | 22% | BOS -1.5 41% | 6.1 | Darcy Kuemper (expected) / Jeremy Swayman (expected) | – | no line yet (model fair BOS -1.5 +145 / LAK +1.5 -145) | no line yet | no line yet |
| 7:00 PM | EDM @ FLA | EDM 2, FLA 3 | FLA 51% | EDM +105 / FLA -105 | 3.1 – 3.1 | 1–5 / 1–6 | 22% | FLA -1.5 30% | 6.2 | Devon Levi (expected) / Jacob Markstrom (expected) | – | no line yet (model fair FLA -1.5 +235 / EDM +1.5 -235) | no line yet | no line yet |
| 7:00 PM | CBJ @ NYI | CBJ 2, NYI 3 | NYI 55% | CBJ +120 / NYI -120 | 3.0 – 3.2 | 1–5 / 1–6 | 22% | NYI -1.5 33% | 6.2 | Jet Greaves (expected) / Ilya Sorokin (expected) | – | no line yet (model fair NYI -1.5 +200 / CBJ +1.5 -200) | no line yet | no line yet |
| 7:00 PM | BUF @ PHI | BUF 3, PHI 2 | BUF 52% | BUF -110 / PHI +110 | 3.2 – 3.1 | 1–6 / 1–5 | 22% | BUF -1.5 31% | 6.2 | Ukko-Pekka Luukkonen (expected) / Dan Vladar (expected) | – | no line yet (model fair PHI +1.5 -225 / BUF -1.5 +225) | no line yet | no line yet |
| 7:00 PM | OTT @ WPG | OTT 3, WPG 2 | OTT 55% | OTT -120 / WPG +120 | 3.1 – 2.9 | 1–5 / 1–5 | 23% | OTT -1.5 33% | 6.0 | Linus Ullmark (expected) / Stuart Skinner (expected) | – | no line yet (model fair WPG +1.5 -200 / OTT -1.5 +200) | no line yet | no line yet |
| 7:30 PM | WSH @ TBL | WSH 3, TBL 4 | TBL 56% | WSH +125 / TBL -125 | 2.9 – 3.3 | 1–5 / 1–6 | 21% | TBL -1.5 35% | 6.2 | Logan Thompson (expected) / Andrei Vasilevskiy (expected) | – | no line yet (model fair TBL -1.5 +190 / WSH +1.5 -190) | no line yet | no line yet |
| 7:30 PM | TOR @ CHI | TOR 4, CHI 3 | TOR 58% | TOR -140 / CHI +140 | 3.4 – 2.9 | 1–6 / 1–5 | 22% | TOR -1.5 37% | 6.3 | Sergei Bobrovsky (expected) / Spencer Knight (expected) | – | no line yet (model fair CHI +1.5 -175 / TOR -1.5 +175) | no line yet | no line yet |
| 8:00 PM | ANA @ STL | ANA 3, STL 4 | STL 63% | ANA +175 / STL -175 | 2.8 – 3.7 | 1–5 / 1–6 | 21% | STL -1.5 42% | 6.6 | Lukas Dostal (expected) / Joel Hofer (expected) | – | no line yet (model fair STL -1.5 +135 / ANA +1.5 -135) | no line yet | no line yet |
| 8:00 PM | NSH @ MIN | NSH 3, MIN 4 | MIN 63% | NSH +170 / MIN -170 | 2.7 – 3.5 | 1–5 / 1–6 | 21% | MIN -1.5 41% | 6.2 | Juuse Saros (expected) / Jesper Wallstedt (expected) | – | no line yet (model fair MIN -1.5 +145 / NSH +1.5 -145) | no line yet | no line yet |
| 10:00 PM | DAL @ VGK | DAL 2, VGK 3 | VGK 53% | DAL +110 / VGK -110 | 2.9 – 3.1 | 1–5 / 1–5 | 22% | VGK -1.5 32% | 5.9 | Jake Oettinger (expected) / Adin Hill (expected) | – | no line yet (model fair VGK -1.5 +215 / DAL +1.5 -215) | no line yet | no line yet |
| 10:00 PM | CGY @ SJS | CGY 4, SJS 3 | CGY 56% | CGY -130 / SJS +130 | 3.5 – 3.1 | 1–6 / 1–6 | 21% | CGY -1.5 36% | 6.6 | Dustin Wolf (expected) / Yaroslav Askarov (expected) | – | no line yet (model fair SJS +1.5 -180 / CGY -1.5 +180) | no line yet | no line yet |

\* price not posted; assumed -110.

## Wednesday, November 18

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:30 PM | BOS @ DET | BOS 3, DET 4 | DET 51% | BOS +105 / DET -105 | 3.1 – 3.2 | 1–6 / 1–6 | 22% | DET -1.5 30% | 6.3 | Michael DiPietro (expected) / John Gibson (expected) | – | no line yet (model fair DET -1.5 +235 / BOS +1.5 -235) | no line yet | no line yet |
| 7:30 PM | MTL @ NJD | MTL 2, NJD 3 | NJD 56% | MTL +130 / NJD -130 | 2.9 – 3.3 | 1–5 / 1–6 | 22% | NJD -1.5 35% | 6.2 | Jacob Fowler (expected) / Connor Hellebuyck (expected) | – | no line yet (model fair NJD -1.5 +190 / MTL +1.5 -190) | no line yet | no line yet |
| 10:00 PM | COL @ UTA | COL 3, UTA 4 | UTA 52% | COL +105 / UTA -105 | 3.2 – 3.3 | 1–6 / 1–6 | 23% | UTA -1.5 31% | 6.5 | Mackenzie Blackwood (expected) / Karel Vejmelka (expected) | – | no line yet (model fair UTA -1.5 +225 / COL +1.5 -225) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 325 | 0.6488 | 0.2287 | 63.1% | 1.37 | 1.82 | 90.0% |
| Model only (before blending) | 325 | 0.6520 | 0.2303 | 60.9% | – | – | – |
| Elo | 325 | 0.6651 | 0.2363 | 59.1% | – | – | – |
| Final prediction, games with a line | 191 | 0.6496 | 0.2291 | 61.8% | 1.35 | 1.87 | 90.3% |
| Model only, games with a line | 191 | 0.6550 | 0.2319 | 58.1% | – | – | – |
| Betting market (de-vigged moneyline) | 191 | 0.6475 | 0.2281 | 62.3% | – | 1.86 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.5% of regular-season games, happened in 22.5%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 4 | 0-4-0 | 3.9 | -3.91 | -100.0% | +8.2% |
| Moneyline | 11 | 6-5-0 | 12.3 | +3.56 | +28.8% | +5.9% |
| Total | 2 | 1-1-0 | 1.7 | +0.04 | +2.4% | +3.4% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 34 of 44 games (77%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Saturday, November 14

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| SEA @ CAR | 3–4 | 1–5 | 75% | yes | Joey Daccord / Pyotr Kochetkov |
| WPG @ CHI | 4–3 | 5–4 (SO) | 61% | yes | Stuart Skinner / Spencer Knight |
| MIN @ BOS | 3–2 | 6–2 | 53% | yes | Jesper Wallstedt / Jeremy Swayman |
| EDM @ TOR | 4–3 | 1–0 | 55% | no | Devon Levi / Anthony Stolarz |
| COL @ MTL | 3–4 | 4–1 | 48% | yes | Mackenzie Blackwood / Jakub Dobes |
| DET @ TBL | 2–3 | 2–0 | 36% | no | Daniil Tarasov / Andrei Vasilevskiy |
| OTT @ PIT | 4–3 | 4–1 | 53% | yes | Linus Ullmark / Sergei Murashov |
| NJD @ WSH | 4–3 | 7–4 | 54% | no | Connor Hellebuyck / Charlie Lindgren |
| PHI @ CBJ | 2–3 | 4–3 | 44% | yes | Joseph Woll / Jet Greaves |
| FLA @ STL | 2–3 | 4–1 | 47% | yes | Jacob Markstrom / Joel Hofer |
| BUF @ DAL | 2–3 | 0–2 | 55% | no | Alex Lyon / Jake Oettinger |
| SJS @ UTA | 3–4 | 6–5 (SO) | 34% | no | Yaroslav Askarov / Karel Vejmelka |
| NYI @ ANA | 4–3 | 6–2 | 50% | yes | Semyon Varlamov / Lukas Dostal |
| CGY @ LAK | 2–3 | 3–2 | 41% | yes | Dustin Wolf / Anton Forsberg |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.84 | +0.51 | +0.33 | 3.47 | 2.30 | 8.72 | 7.15 | 1593 |
| 2 | TBL | +0.43 | +0.21 | +0.22 | 2.92 | 2.41 | 8.06 | 7.98 | 1549 |
| 3 | UTA | +0.40 | +0.24 | +0.16 | 3.14 | 2.43 | 8.24 | 8.94 | 1495 |
| 4 | VGK | +0.31 | +0.07 | +0.24 | 2.73 | 2.39 | 9.24 | 7.28 | 1536 |
| 5 | COL | +0.25 | +0.23 | +0.02 | 2.88 | 2.71 | 8.17 | 7.92 | 1557 |
| 6 | DAL | +0.25 | -0.02 | +0.27 | 2.65 | 2.36 | 9.52 | 7.55 | 1524 |
| 7 | PIT | +0.25 | +0.16 | +0.08 | 2.99 | 2.54 | 7.71 | 7.94 | 1484 |
| 8 | MIN | +0.25 | +0.09 | +0.16 | 2.83 | 2.53 | 9.04 | 8.10 | 1563 |
| 9 | NJD | +0.17 | +0.03 | +0.14 | 2.76 | 2.49 | 9.20 | 7.93 | 1531 |
| 10 | OTT | +0.15 | -0.02 | +0.17 | 2.68 | 2.47 | 7.93 | 8.14 | 1526 |
| 11 | STL | +0.13 | +0.00 | +0.12 | 2.71 | 2.54 | 7.23 | 8.08 | 1496 |
| 12 | FLA | +0.12 | -0.02 | +0.14 | 2.57 | 2.52 | 9.67 | 7.68 | 1512 |
| 13 | BOS | +0.10 | +0.09 | +0.01 | 2.84 | 2.71 | 7.59 | 8.24 | 1530 |
| 14 | WSH | +0.10 | +0.16 | -0.06 | 2.97 | 2.75 | 7.80 | 8.17 | 1508 |
| 15 | NYR | +0.07 | +0.04 | +0.03 | 2.75 | 2.68 | 8.96 | 7.80 | 1503 |
| 16 | BUF | +0.05 | +0.08 | -0.04 | 2.80 | 2.71 | 7.98 | 8.38 | 1502 |
| 17 | EDM | +0.03 | +0.03 | +0.01 | 2.48 | 2.68 | 9.70 | 8.28 | 1539 |
| 18 | LAK | +0.02 | -0.11 | +0.14 | 2.57 | 2.53 | 8.23 | 8.08 | 1457 |
| 19 | MTL | -0.05 | +0.06 | -0.11 | 2.80 | 2.85 | 7.71 | 8.63 | 1534 |
| 20 | WPG | -0.09 | -0.08 | -0.00 | 2.54 | 2.70 | 8.56 | 8.83 | 1488 |
| 21 | DET | -0.09 | -0.09 | +0.01 | 2.65 | 2.66 | 8.65 | 8.71 | 1479 |
| 22 | NSH | -0.10 | -0.02 | -0.08 | 2.70 | 2.80 | 8.19 | 7.73 | 1510 |
| 23 | CBJ | -0.11 | -0.04 | -0.07 | 2.71 | 2.76 | 7.87 | 8.66 | 1481 |
| 24 | NYI | -0.12 | -0.03 | -0.10 | 2.72 | 2.84 | 7.50 | 8.68 | 1493 |
| 25 | TOR | -0.13 | -0.07 | -0.06 | 2.46 | 2.74 | 8.63 | 8.48 | 1461 |
| 26 | PHI | -0.20 | -0.23 | +0.03 | 2.38 | 2.64 | 7.72 | 7.71 | 1473 |
| 27 | CGY | -0.23 | -0.12 | -0.10 | 2.56 | 2.82 | 7.22 | 7.88 | 1462 |
| 28 | SEA | -0.36 | -0.16 | -0.21 | 2.36 | 2.92 | 7.22 | 8.79 | 1470 |
| 29 | ANA | -0.38 | -0.01 | -0.38 | 2.66 | 3.08 | 8.11 | 8.37 | 1483 |
| 30 | CHI | -0.64 | -0.31 | -0.33 | 2.22 | 3.02 | 7.28 | 8.49 | 1417 |
| 31 | SJS | -0.73 | -0.23 | -0.50 | 2.34 | 3.22 | 7.42 | 9.40 | 1451 |
| 32 | VAN | -0.77 | -0.28 | -0.49 | 2.18 | 3.20 | 7.74 | 8.82 | 1393 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 66% | +0.41 | +0.17 |
| MTL | Jacob Fowler | 64% | +0.35 | +0.15 |
| WSH | Logan Thompson | 72% | +0.34 | +0.14 |
| MIN | Jesper Wallstedt | 86% | +0.33 | +0.14 |
| BOS | Jeremy Swayman | 76% | +0.27 | +0.11 |
| COL | Mackenzie Blackwood | 71% | +0.22 | +0.09 |
| NJD | Connor Hellebuyck | 47% | +0.16 | +0.07 |
| TBL | Andrei Vasilevskiy | 73% | +0.15 | +0.06 |
| OTT | Linus Ullmark | 42% | +0.14 | +0.06 |
| STL | Joel Hofer | 79% | +0.11 | +0.05 |
| EDM | Devon Levi | 45% | +0.09 | +0.04 |
| DAL | Jake Oettinger | 81% | +0.08 | +0.03 |
| CBJ | Jet Greaves | 56% | +0.05 | +0.02 |
| CAR | Pyotr Kochetkov | 65% | +0.03 | +0.01 |
| CHI | Spencer Knight | 82% | +0.02 | +0.01 |
| NYR | Dylan Garand | 67% | +0.00 | +0.00 |
| NSH | Juuse Saros | 67% | -0.06 | -0.02 |
| WPG | Stuart Skinner | 74% | -0.07 | -0.03 |
| PHI | Dan Vladar | 50% | -0.08 | -0.03 |
| BUF | Ukko-Pekka Luukkonen | 48% | -0.17 | -0.07 |
| SJS | Yaroslav Askarov | 71% | -0.18 | -0.08 |
| UTA | Karel Vejmelka | 64% | -0.18 | -0.08 |
| TOR | Sergei Bobrovsky | 54% | -0.20 | -0.08 |
| DET | John Gibson | 57% | -0.21 | -0.09 |
| FLA | Jacob Markstrom | 53% | -0.22 | -0.09 |
| SEA | Joey Daccord | 51% | -0.23 | -0.09 |
| CGY | Dustin Wolf | 50% | -0.24 | -0.10 |
| VGK | Adin Hill | 52% | -0.25 | -0.10 |
| ANA | Lukas Dostal | 47% | -0.27 | -0.11 |
| LAK | Darcy Kuemper | 57% | -0.28 | -0.12 |
| VAN | Leevi Meriläinen | 72% | -0.39 | -0.16 |
| PIT | Arturs Silovs | 55% | -0.40 | -0.17 |

## Current model fit

- Fitted on 5917 games from 2022-23 to 2026-27.
- Home ice: +2.7% goals for the home team relative to the visitor.
- Second night of a back-to-back: -6.0% goals scored, +3.4% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 21%.
- Blend: 49% on the betting line wherever there is one (fitted on 191 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
