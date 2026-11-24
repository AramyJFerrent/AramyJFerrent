# NHL score predictions

Updated Mon Nov 23, 2026 09:59 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Monday, November 23

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10:00 PM | MIN @ SJS | MIN 4, SJS 3 | MIN 65% | MIN -185 / SJS +185 | 3.8 – 2.8 | 1–6 / 1–5 | 21% | MIN -1.5 44% | 6.5 / 6.5 (over 51%) | Filip Gustavsson (confirmed) / Yaroslav Askarov (confirmed) | MIN -180 / SJS +150 | MIN -1.5 (+136): EV +3.8%, 44%, stake 0.7u | no edge | no edge |

## Tuesday, November 24

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8:00 PM | VGK @ EDM | VGK 4, EDM 3 | VGK 52% | VGK -110 / EDM +110 | 3.2 – 3.1 | 1–6 / 1–5 | 22% | VGK -1.5 32% | 6.3 / 6.5 (over 46%) | Carter Hart (expected) / Devon Levi (expected) | VGK -118 / EDM -102 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Wednesday, November 25

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | WPG @ BOS | WPG 3, BOS 4 | BOS 60% | WPG +150 / BOS -150 | 2.8 – 3.4 | 1–5 / 1–6 | 23% | BOS -1.5 38% | 6.3 | Stuart Skinner (expected) / Jeremy Swayman (expected) | – | no line yet (model fair BOS -1.5 +165 / WPG +1.5 -165) | no line yet | no line yet |
| 7:00 PM | NYR @ BUF | NYR 3, BUF 4 | BUF 53% | NYR +110 / BUF -110 | 3.1 – 3.3 | 1–6 / 1–6 | 21% | BUF -1.5 32% | 6.5 | Dylan Garand (expected) / Alex Lyon (expected) | – | no line yet (model fair BUF -1.5 +210 / NYR +1.5 -210) | no line yet | no line yet |
| 7:00 PM | CAR @ TBL | CAR 4, TBL 3 | CAR 53% | CAR -110 / TBL +110 | 3.2 – 3.1 | 1–6 / 1–6 | 22% | CAR -1.5 32% | 6.3 | Pyotr Kochetkov (expected) / Andrei Vasilevskiy (expected) | – | no line yet (model fair TBL +1.5 -215 / CAR -1.5 +215) | no line yet | no line yet |
| 7:00 PM | OTT @ FLA | OTT 3, FLA 2 | OTT 53% | OTT -110 / FLA +110 | 3.0 – 2.9 | 1–5 / 1–5 | 23% | OTT -1.5 31% | 5.9 | Linus Ullmark (expected) / Jacob Markstrom (expected) | – | no line yet (model fair FLA +1.5 -225 / OTT -1.5 +225) | no line yet | no line yet |
| 7:00 PM | STL @ NYI | STL 2, NYI 3 | NYI 50% | STL +100 / NYI -100 | 3.1 – 3.1 | 1–5 / 1–5 | 22% | NYI -1.5 30% | 6.2 | Joel Hofer (expected) / Ilya Sorokin (expected) | – | no line yet (model fair NYI -1.5 +235 / STL +1.5 -235) | no line yet | no line yet |
| 7:00 PM | CGY @ PIT | CGY 3, PIT 4 | PIT 60% | CGY +150 / PIT -150 | 3.0 – 3.6 | 1–5 / 1–6 | 22% | PIT -1.5 39% | 6.6 | Dustin Wolf (expected) / Arturs Silovs (expected) | – | no line yet (model fair PIT -1.5 +160 / CGY +1.5 -160) | no line yet | no line yet |
| 7:00 PM | PHI @ WSH | PHI 3, WSH 4 | WSH 60% | PHI +150 / WSH -150 | 2.8 – 3.4 | 1–5 / 1–6 | 22% | WSH -1.5 37% | 6.2 | Dan Vladar (expected) / Logan Thompson (expected) | – | no line yet (model fair WSH -1.5 +165 / PHI +1.5 -165) | no line yet | no line yet |
| 7:00 PM | NJD @ CBJ | NJD 4, CBJ 3 | NJD 56% | NJD -125 / CBJ +125 | 3.3 – 3.0 | 1–6 / 1–5 | 22% | NJD -1.5 35% | 6.3 | Connor Hellebuyck (expected) / Cam Talbot (expected) | – | no line yet (model fair CBJ +1.5 -185 / NJD -1.5 +185) | no line yet | no line yet |
| 7:30 PM | VAN @ DET | VAN 3, DET 4 | DET 69% | VAN +225 / DET -225 | 2.7 – 3.9 | 1–5 / 2–6 | 19% | DET -1.5 48% | 6.6 | Leevi Meriläinen (expected) / John Gibson (expected) | – | no line yet (model fair DET -1.5 +105 / VAN +1.5 -105) | no line yet | no line yet |
| 8:00 PM | NSH @ DAL | NSH 2, DAL 3 | DAL 60% | NSH +150 / DAL -150 | 2.7 – 3.3 | 1–5 / 1–6 | 23% | DAL -1.5 37% | 6.1 | Juuse Saros (expected) / Jake Oettinger (expected) | – | no line yet (model fair DAL -1.5 +170 / NSH +1.5 -170) | no line yet | no line yet |
| 8:00 PM | UTA @ MIN | UTA 2, MIN 3 | MIN 57% | UTA +135 / MIN -135 | 2.8 – 3.3 | 1–5 / 1–6 | 23% | MIN -1.5 36% | 6.1 | Karel Vejmelka (expected) / Jesper Wallstedt (expected) | – | no line yet (model fair MIN -1.5 +180 / UTA +1.5 -180) | no line yet | no line yet |
| 9:30 PM | MTL @ COL | MTL 3, COL 4 | COL 58% | MTL +140 / COL -140 | 3.0 – 3.5 | 1–5 / 1–6 | 22% | COL -1.5 37% | 6.5 | Jacob Fowler (expected) / Mackenzie Blackwood (expected) | – | no line yet (model fair COL -1.5 +170 / MTL +1.5 -170) | no line yet | no line yet |
| 9:40 PM | CHI @ SEA | CHI 3, SEA 4 | SEA 59% | CHI +145 / SEA -145 | 2.9 – 3.5 | 1–5 / 1–6 | 21% | SEA -1.5 38% | 6.5 | Spencer Knight (expected) / Philipp Grubauer (expected) | – | no line yet (model fair SEA -1.5 +160 / CHI +1.5 -160) | no line yet | no line yet |
| 10:00 PM | SJS @ ANA | SJS 3, ANA 4 | ANA 60% | SJS +150 / ANA -150 | 3.2 – 3.9 | 1–6 / 1–6 | 21% | ANA -1.5 40% | 7.1 | Yaroslav Askarov (expected) / Lukas Dostal (expected) | – | no line yet (model fair ANA -1.5 +150 / SJS +1.5 -150) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 377 | 0.6595 | 0.2336 | 62.1% | 1.38 | 1.84 | 89.5% |
| Model only (before blending) | 377 | 0.6622 | 0.2349 | 60.2% | – | – | – |
| Elo | 377 | 0.6713 | 0.2392 | 58.4% | – | – | – |
| Final prediction, games with a line | 243 | 0.6661 | 0.2366 | 60.5% | 1.38 | 1.89 | 89.5% |
| Model only, games with a line | 243 | 0.6703 | 0.2387 | 57.6% | – | – | – |
| Betting market (de-vigged moneyline) | 243 | 0.6639 | 0.2356 | 60.9% | – | 1.88 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.5% of regular-season games, happened in 22.3%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 5 | 0-5-0 | 5.2 | -5.25 | -100.0% | +8.0% |
| Moneyline | 13 | 8-5-0 | 14.7 | +5.40 | +36.8% | +5.5% |
| Total | 2 | 1-1-0 | 1.7 | +0.04 | +2.4% | +3.4% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 42 of 56 games (75%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Sunday, November 22

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| CAR @ NYR | 4–3 | 5–2 | 59% | yes | Brandon Bussi / Dylan Garand |
| BUF @ TBL | 3–4 | 6–2 | 34% | no | Ukko-Pekka Luukkonen / Dennis Hildeby |
| EDM @ STL | 3–4 | 4–5 (SO) | 54% | yes | Tristan Jarry / Joel Hofer |
| PIT @ DAL | 2–3 | 0–1 | 66% | no | Arturs Silovs / Jake Oettinger |
| CHI @ VAN | 4–3 | 6–3 | 51% | yes | Drew Commesso / Nikita Tolopilo |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.82 | +0.50 | +0.32 | 3.43 | 2.31 | 8.49 | 7.01 | 1598 |
| 2 | TBL | +0.45 | +0.23 | +0.22 | 2.97 | 2.40 | 7.92 | 7.97 | 1549 |
| 3 | UTA | +0.36 | +0.20 | +0.16 | 3.08 | 2.42 | 8.30 | 8.84 | 1500 |
| 4 | VGK | +0.29 | +0.08 | +0.21 | 2.73 | 2.42 | 9.33 | 7.19 | 1524 |
| 5 | MIN | +0.29 | +0.10 | +0.19 | 2.81 | 2.48 | 8.81 | 7.93 | 1568 |
| 6 | OTT | +0.25 | +0.02 | +0.23 | 2.73 | 2.37 | 7.97 | 8.18 | 1529 |
| 7 | COL | +0.24 | +0.21 | +0.03 | 2.84 | 2.68 | 7.99 | 8.02 | 1555 |
| 8 | DAL | +0.21 | -0.07 | +0.28 | 2.56 | 2.34 | 9.35 | 7.20 | 1534 |
| 9 | PIT | +0.21 | +0.14 | +0.06 | 2.99 | 2.56 | 7.67 | 8.03 | 1474 |
| 10 | NJD | +0.18 | +0.06 | +0.12 | 2.79 | 2.49 | 9.20 | 7.88 | 1522 |
| 11 | FLA | +0.12 | -0.05 | +0.17 | 2.50 | 2.47 | 9.51 | 7.68 | 1507 |
| 12 | WSH | +0.12 | +0.16 | -0.04 | 2.95 | 2.70 | 8.17 | 8.06 | 1494 |
| 13 | STL | +0.10 | +0.08 | +0.03 | 2.76 | 2.66 | 7.28 | 8.08 | 1514 |
| 14 | BOS | +0.10 | +0.09 | +0.01 | 2.82 | 2.70 | 7.65 | 8.25 | 1531 |
| 15 | EDM | +0.06 | +0.03 | +0.03 | 2.45 | 2.63 | 9.59 | 8.25 | 1538 |
| 16 | NYR | +0.05 | +0.01 | +0.04 | 2.71 | 2.66 | 8.82 | 7.65 | 1503 |
| 17 | BUF | +0.03 | +0.09 | -0.06 | 2.76 | 2.73 | 8.02 | 8.53 | 1511 |
| 18 | LAK | +0.03 | -0.14 | +0.17 | 2.49 | 2.47 | 8.16 | 8.10 | 1464 |
| 19 | MTL | -0.02 | +0.03 | -0.05 | 2.77 | 2.76 | 7.63 | 8.48 | 1533 |
| 20 | NYI | -0.06 | -0.01 | -0.05 | 2.75 | 2.78 | 7.27 | 8.78 | 1499 |
| 21 | NSH | -0.08 | -0.01 | -0.07 | 2.73 | 2.77 | 8.05 | 7.67 | 1503 |
| 22 | DET | -0.13 | -0.12 | -0.01 | 2.60 | 2.67 | 8.57 | 8.68 | 1471 |
| 23 | CBJ | -0.14 | -0.06 | -0.08 | 2.65 | 2.75 | 7.93 | 8.59 | 1482 |
| 24 | WPG | -0.15 | -0.10 | -0.05 | 2.50 | 2.75 | 8.61 | 9.20 | 1485 |
| 25 | TOR | -0.15 | -0.07 | -0.08 | 2.45 | 2.74 | 8.76 | 8.44 | 1450 |
| 26 | PHI | -0.17 | -0.22 | +0.05 | 2.37 | 2.60 | 7.88 | 7.67 | 1478 |
| 27 | CGY | -0.27 | -0.14 | -0.13 | 2.52 | 2.84 | 7.12 | 7.69 | 1455 |
| 28 | SEA | -0.33 | -0.14 | -0.20 | 2.38 | 2.89 | 7.40 | 8.76 | 1472 |
| 29 | ANA | -0.34 | +0.02 | -0.36 | 2.72 | 3.05 | 7.97 | 8.14 | 1478 |
| 30 | CHI | -0.61 | -0.27 | -0.34 | 2.24 | 3.02 | 7.23 | 8.59 | 1428 |
| 31 | SJS | -0.74 | -0.22 | -0.52 | 2.34 | 3.22 | 7.35 | 9.32 | 1452 |
| 32 | VAN | -0.81 | -0.27 | -0.54 | 2.19 | 3.24 | 7.67 | 8.82 | 1399 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 66% | +0.43 | +0.18 |
| MIN | Jesper Wallstedt | 89% | +0.32 | +0.13 |
| BOS | Jeremy Swayman | 74% | +0.30 | +0.13 |
| MTL | Jacob Fowler | 67% | +0.30 | +0.12 |
| WSH | Logan Thompson | 70% | +0.28 | +0.12 |
| COL | Mackenzie Blackwood | 67% | +0.24 | +0.10 |
| TBL | Andrei Vasilevskiy | 71% | +0.17 | +0.07 |
| OTT | Linus Ullmark | 48% | +0.17 | +0.07 |
| STL | Joel Hofer | 70% | +0.15 | +0.06 |
| DAL | Jake Oettinger | 80% | +0.14 | +0.06 |
| NJD | Connor Hellebuyck | 56% | +0.10 | +0.04 |
| CHI | Spencer Knight | 79% | +0.05 | +0.02 |
| TOR | Anthony Stolarz | 51% | +0.04 | +0.02 |
| WPG | Stuart Skinner | 72% | +0.01 | +0.00 |
| EDM | Devon Levi | 50% | +0.01 | +0.00 |
| NYR | Dylan Garand | 64% | -0.00 | -0.00 |
| CAR | Pyotr Kochetkov | 65% | -0.00 | -0.00 |
| NSH | Juuse Saros | 67% | -0.08 | -0.04 |
| BUF | Ukko-Pekka Luukkonen | 49% | -0.09 | -0.04 |
| PHI | Dan Vladar | 50% | -0.11 | -0.05 |
| SEA | Philipp Grubauer | 60% | -0.14 | -0.06 |
| UTA | Karel Vejmelka | 56% | -0.18 | -0.08 |
| CBJ | Cam Talbot | 59% | -0.18 | -0.08 |
| SJS | Yaroslav Askarov | 62% | -0.20 | -0.08 |
| DET | John Gibson | 56% | -0.21 | -0.09 |
| LAK | Darcy Kuemper | 59% | -0.22 | -0.09 |
| FLA | Jacob Markstrom | 57% | -0.25 | -0.10 |
| CGY | Dustin Wolf | 58% | -0.25 | -0.11 |
| ANA | Lukas Dostal | 41% | -0.28 | -0.12 |
| VGK | Adin Hill | 51% | -0.29 | -0.12 |
| VAN | Leevi Meriläinen | 67% | -0.33 | -0.14 |
| PIT | Arturs Silovs | 58% | -0.34 | -0.14 |

## Current model fit

- Fitted on 5969 games from 2022-23 to 2026-27.
- Home ice: +2.7% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.9% goals scored, +3.0% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 21%.
- Blend: 60% on the betting line wherever there is one (fitted on 243 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.02 goals per five minutes.
