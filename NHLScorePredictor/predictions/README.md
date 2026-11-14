# NHL score predictions

Updated Sat Nov 14, 2026 03:51 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Saturday, November 14

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | MIN @ BOS | MIN 3, BOS 2 | MIN 53% | MIN -115 / BOS +115 | 3.2 – 3.0 | 1–6 / 1–5 | 22% | MIN -1.5 33% | 6.2 / 6.5 (over 44%) | Jesper Wallstedt (confirmed) / Jeremy Swayman (confirmed) | MIN -130 / BOS +110 | no edge | no edge | no edge |
| 7:00 PM | EDM @ TOR | EDM 4, TOR 3 | EDM 55% | EDM -125 / TOR +125 | 3.5 – 3.1 | 1–6 / 1–6 | 22% | EDM -1.5 35% | 6.6 / 6.5 (over 52%) | Devon Levi (expected) / Anthony Stolarz (confirmed) | EDM -148 / TOR +124 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | COL @ MTL | COL 3, MTL 4 | MTL 52% | COL +110 / MTL -110 | 3.2 – 3.3 | 1–6 / 1–6 | 22% | MTL -1.5 32% | 6.5 / 6.5 (over 50%) | Mackenzie Blackwood (confirmed) / Jakub Dobes (confirmed) | COL +120 / MTL -142 | no edge | COL (+120): EV +5.0%, 48%, stake 1.0u | no edge |
| 7:00 PM | DET @ TBL | DET 2, TBL 3 | TBL 64% | DET +180 / TBL -180 | 2.6 – 3.5 | 1–5 / 1–6 | 21% | TBL -1.5 42% | 6.1 / 6.5 (over 43%) | Daniil Tarasov (confirmed) / Andrei Vasilevskiy (confirmed) | DET +185 / TBL -225 | no edge | no edge | no edge |
| 7:00 PM | OTT @ PIT | OTT 4, PIT 3 | OTT 53% | OTT -115 / PIT +115 | 3.2 – 3.0 | 1–6 / 1–5 | 22% | OTT -1.5 31% | 6.3 / 6.5 (over 46%) | Linus Ullmark (confirmed) / Sergei Murashov (confirmed) | OTT -135 / PIT +114 | no edge | no edge | no edge |
| 7:00 PM | NJD @ WSH | NJD 4, WSH 3 | NJD 54% | NJD -115 / WSH +115 | 3.3 – 3.1 | 1–6 / 1–5 | 22% | NJD -1.5 33% | 6.4 / 6.5 (over 48%) | Connor Hellebuyck (confirmed) / Charlie Lindgren (confirmed) | NJD -135 / WSH +114 | no edge | no edge | no edge |
| 7:00 PM | PHI @ CBJ | PHI 2, CBJ 3 | CBJ 56% | PHI +130 / CBJ -130 | 2.8 – 3.2 | 1–5 / 1–6 | 22% | CBJ -1.5 34% | 6.0 / 5.5 (over 52%) | Joseph Woll (confirmed) / Jet Greaves (confirmed) | PHI +114 / CBJ -135 | no edge | no edge | no edge |
| 7:00 PM | FLA @ STL | FLA 2, STL 3 | STL 53% | FLA +115 / STL -115 | 3.0 – 3.1 | 1–5 / 1–5 | 22% | STL -1.5 32% | 6.1 / 5.5 (over 54%) | Jacob Markstrom (confirmed) / Joel Hofer (confirmed) | FLA -108 / STL -112 | STL -1.5 (+230): EV +5.7%, 32%, stake 0.6u | no edge | no edge |
| 8:00 PM | BUF @ DAL | BUF 2, DAL 3 | DAL 55% | BUF +120 / DAL -120 | 2.9 – 3.2 | 1–5 / 1–6 | 22% | DAL -1.5 33% | 6.1 / 6.5 (over 43%) | Alex Lyon (confirmed) / Jake Oettinger (confirmed) | BUF +114 / DAL -135 | no edge | no edge | no edge |
| 9:00 PM | SJS @ UTA | SJS 3, UTA 4 | UTA 67% | SJS +205 / UTA -205 | 2.7 – 3.8 | 1–5 / 1–6 | 20% | UTA -1.5 46% | 6.5 / 6.5 (over 49%) | Yaroslav Askarov (confirmed) / Karel Vejmelka (confirmed) | SJS +154 / UTA -185 | no edge | no edge | no edge |
| 10:00 PM | NYI @ ANA | NYI 4, ANA 3 | NYI 50% | NYI -100 / ANA +100 | 3.4 – 3.4 | 1–6 / 1–6 | 21% | NYI -1.5 30% | 6.8 / 6.5 (over 55%) | Semyon Varlamov (expected) / Lukas Dostal (expected) | NYI -112 / ANA -108 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | CGY @ LAK | CGY 2, LAK 3 | LAK 60% | CGY +150 / LAK -150 | 2.7 – 3.3 | 1–5 / 1–6 | 22% | LAK -1.5 38% | 6.0 / 5.5 (over 53%) | Dustin Wolf (confirmed) / Anton Forsberg (confirmed) | CGY +145 / LAK -175 | no edge | no edge | no edge |

## Sunday, November 15

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:30 PM | EDM @ PHI | EDM 3, PHI 2 | EDM 56% | EDM -130 / PHI +130 | 3.3 – 2.9 | 1–6 / 1–5 | 22% | EDM -1.5 35% | 6.2 / 6.5 (over 46%) | Tristan Jarry (expected) / Dan Vladar (confirmed) | EDM -155 / PHI +130 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | FLA @ DAL | FLA 2, DAL 3 | DAL 55% | FLA +125 / DAL -125 | 2.8 – 3.1 | 1–5 / 1–5 | 23% | DAL -1.5 33% | 5.9 / 5.5 (over 51%) | Akira Schmid (expected) / Casey DeSmith (expected) | FLA +114 / DAL -135 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | CGY @ ANA | CGY 3, ANA 4 | ANA 54% | CGY +115 / ANA -115 | 3.2 – 3.4 | 1–6 / 1–6 | 22% | ANA -1.5 33% | 6.6 / 6.5 (over 51%) | Devin Cooley (expected) / Ville Husso (expected) | CGY +130 / ANA -155 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:00 PM | VAN @ VGK | VAN 3, VGK 4 | VGK 77% | VAN +325 / VGK -325 | 2.4 – 4.2 | 0–5 / 2–7 | 17% | VGK -1.5 57% | 6.6 / 6.5 (over 51%) | Leevi Meriläinen (expected) / Carter Hart (expected) | VAN +320 / VGK -410 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:00 PM | NSH @ SJS | NSH 4, SJS 3 | NSH 63% | NSH -170 / SJS +170 | 3.7 – 2.9 | 1–6 / 1–5 | 21% | NSH -1.5 42% | 6.6 / 6.5 (over 51%) | Juuse Saros (expected) / Alex Nedeljkovic (expected) | NSH -170 / SJS +142 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Monday, November 16

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:30 PM | MTL @ NYR | MTL 4, NYR 3 | MTL 50% | MTL -100 / NYR +100 | 3.2 – 3.2 | 1–6 / 1–6 | 22% | MTL -1.5 30% | 6.4 | Jacob Fowler (expected) / Joonas Korpisalo (expected) | – | no line yet (model fair NYR +1.5 -230 / MTL -1.5 +230) | no line yet | no line yet |
| 9:30 PM | VAN @ UTA | VAN 2, UTA 5 | UTA 78% | VAN +355 / UTA -355 | 2.4 – 4.4 | 0–5 / 2–7 | 16% | UTA -1.5 60% | 6.8 | Kevin Lankinen (expected) / Karel Vejmelka (expected) | – | no line yet (model fair UTA -1.5 -145 / VAN +1.5 +145) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 311 | 0.6462 | 0.2274 | 63.3% | 1.35 | 1.79 | 90.4% |
| Model only (before blending) | 311 | 0.6492 | 0.2289 | 61.4% | – | – | – |
| Elo | 311 | 0.6620 | 0.2348 | 60.1% | – | – | – |
| Final prediction, games with a line | 177 | 0.6451 | 0.2269 | 62.1% | 1.33 | 1.82 | 91.0% |
| Model only, games with a line | 177 | 0.6504 | 0.2296 | 58.8% | – | – | – |
| Betting market (de-vigged moneyline) | 177 | 0.6435 | 0.2262 | 62.7% | – | 1.81 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.5% of regular-season games, happened in 22.8%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 3 | 0-3-0 | 3.3 | -3.29 | -100.0% | +8.7% |
| Moneyline | 10 | 5-5-0 | 11.3 | +2.30 | +20.4% | +6.0% |
| Total | 2 | 1-1-0 | 1.7 | +0.04 | +2.4% | +3.4% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 33 of 43 games (77%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Friday, November 13

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| NYR @ VAN | 4–3 | 5–1 | 65% | yes | Dylan Garand / Leevi Meriläinen |
| NSH @ VGK | 2–3 | 3–2 (SO) | 41% | yes | Juuse Saros / Adin Hill |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.79 | +0.49 | +0.30 | 3.46 | 2.34 | 8.64 | 7.19 | 1589 |
| 2 | TBL | +0.45 | +0.23 | +0.23 | 2.94 | 2.41 | 8.09 | 7.99 | 1555 |
| 3 | UTA | +0.41 | +0.22 | +0.18 | 3.15 | 2.42 | 8.18 | 8.93 | 1499 |
| 4 | VGK | +0.32 | +0.07 | +0.25 | 2.74 | 2.40 | 9.23 | 7.27 | 1536 |
| 5 | MIN | +0.28 | +0.10 | +0.18 | 2.88 | 2.50 | 9.09 | 8.12 | 1556 |
| 6 | PIT | +0.25 | +0.17 | +0.08 | 3.00 | 2.56 | 7.82 | 8.00 | 1490 |
| 7 | COL | +0.24 | +0.25 | -0.01 | 2.90 | 2.75 | 7.94 | 7.87 | 1551 |
| 8 | NJD | +0.22 | +0.02 | +0.20 | 2.77 | 2.42 | 9.10 | 7.97 | 1525 |
| 9 | DAL | +0.20 | -0.04 | +0.24 | 2.59 | 2.40 | 9.63 | 7.56 | 1520 |
| 10 | OTT | +0.15 | -0.02 | +0.17 | 2.69 | 2.48 | 7.98 | 8.24 | 1521 |
| 11 | STL | +0.14 | +0.02 | +0.12 | 2.75 | 2.57 | 7.10 | 8.08 | 1502 |
| 12 | BUF | +0.12 | +0.11 | +0.01 | 2.83 | 2.66 | 7.98 | 8.47 | 1506 |
| 13 | FLA | +0.11 | -0.02 | +0.12 | 2.59 | 2.55 | 9.67 | 7.56 | 1506 |
| 14 | NYR | +0.07 | +0.03 | +0.04 | 2.76 | 2.69 | 8.96 | 7.80 | 1503 |
| 15 | WSH | +0.06 | +0.11 | -0.05 | 2.89 | 2.76 | 7.84 | 8.06 | 1514 |
| 16 | BOS | +0.05 | +0.07 | -0.02 | 2.80 | 2.77 | 7.62 | 8.29 | 1537 |
| 17 | EDM | +0.04 | +0.05 | -0.01 | 2.52 | 2.71 | 9.73 | 8.32 | 1536 |
| 18 | LAK | +0.02 | -0.12 | +0.14 | 2.56 | 2.53 | 8.35 | 8.17 | 1460 |
| 19 | MTL | -0.05 | +0.07 | -0.12 | 2.84 | 2.87 | 7.65 | 8.40 | 1540 |
| 20 | WPG | -0.09 | -0.07 | -0.02 | 2.58 | 2.73 | 8.51 | 8.84 | 1485 |
| 21 | DET | -0.09 | -0.09 | +0.00 | 2.65 | 2.67 | 8.67 | 8.74 | 1473 |
| 22 | NSH | -0.10 | -0.03 | -0.07 | 2.70 | 2.81 | 8.19 | 7.74 | 1510 |
| 23 | TOR | -0.12 | -0.04 | -0.07 | 2.50 | 2.77 | 8.68 | 8.53 | 1464 |
| 24 | CBJ | -0.12 | -0.04 | -0.08 | 2.73 | 2.78 | 7.74 | 8.75 | 1484 |
| 25 | NYI | -0.15 | -0.03 | -0.11 | 2.76 | 2.88 | 7.54 | 8.73 | 1486 |
| 26 | PHI | -0.21 | -0.24 | +0.03 | 2.40 | 2.66 | 7.79 | 7.60 | 1470 |
| 27 | CGY | -0.21 | -0.13 | -0.08 | 2.56 | 2.80 | 7.31 | 8.00 | 1459 |
| 28 | SEA | -0.32 | -0.13 | -0.19 | 2.41 | 2.91 | 7.26 | 8.68 | 1474 |
| 29 | ANA | -0.39 | +0.00 | -0.39 | 2.70 | 3.12 | 8.15 | 8.39 | 1490 |
| 30 | CHI | -0.67 | -0.31 | -0.36 | 2.25 | 3.07 | 7.28 | 8.43 | 1419 |
| 31 | SJS | -0.74 | -0.25 | -0.49 | 2.33 | 3.23 | 7.38 | 9.32 | 1447 |
| 32 | VAN | -0.76 | -0.28 | -0.48 | 2.18 | 3.20 | 7.73 | 8.83 | 1393 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 73% | +0.41 | +0.17 |
| MTL | Jacob Fowler | 70% | +0.35 | +0.15 |
| WSH | Logan Thompson | 80% | +0.35 | +0.15 |
| BOS | Jeremy Swayman | 73% | +0.32 | +0.14 |
| MIN | Jesper Wallstedt | 84% | +0.30 | +0.13 |
| COL | Mackenzie Blackwood | 68% | +0.19 | +0.08 |
| CGY | Devin Cooley | 49% | +0.17 | +0.07 |
| STL | Joel Hofer | 77% | +0.15 | +0.06 |
| TBL | Andrei Vasilevskiy | 71% | +0.13 | +0.06 |
| CBJ | Jet Greaves | 51% | +0.10 | +0.04 |
| DAL | Jake Oettinger | 78% | +0.04 | +0.02 |
| CAR | Pyotr Kochetkov | 62% | +0.03 | +0.01 |
| CHI | Spencer Knight | 80% | +0.03 | +0.01 |
| NYR | Dylan Garand | 67% | +0.01 | +0.00 |
| WPG | Stuart Skinner | 71% | -0.03 | -0.01 |
| NSH | Juuse Saros | 67% | -0.06 | -0.02 |
| PHI | Dan Vladar | 55% | -0.08 | -0.03 |
| NJD | Jake Allen | 45% | -0.10 | -0.04 |
| UTA | Karel Vejmelka | 61% | -0.16 | -0.07 |
| SJS | Yaroslav Askarov | 68% | -0.16 | -0.07 |
| BUF | Ukko-Pekka Luukkonen | 53% | -0.17 | -0.07 |
| SEA | Philipp Grubauer | 55% | -0.18 | -0.08 |
| ANA | Lukas Dostal | 42% | -0.20 | -0.08 |
| TOR | Sergei Bobrovsky | 60% | -0.20 | -0.08 |
| DET | John Gibson | 63% | -0.21 | -0.09 |
| VGK | Adin Hill | 52% | -0.25 | -0.10 |
| FLA | Jacob Markstrom | 48% | -0.26 | -0.11 |
| EDM | Tristan Jarry | 47% | -0.28 | -0.12 |
| LAK | Darcy Kuemper | 64% | -0.28 | -0.12 |
| VAN | Leevi Meriläinen | 72% | -0.39 | -0.16 |
| PIT | Arturs Silovs | 61% | -0.40 | -0.17 |
| OTT | Samuel Ersson | 41% | -0.51 | -0.22 |

## Current model fit

- Fitted on 5903 games from 2022-23 to 2026-27.
- Home ice: +2.8% goals for the home team relative to the visitor.
- Second night of a back-to-back: -6.0% goals scored, +3.4% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 21%.
- Blend: 50% on the betting line wherever there is one (fitted on 177 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
