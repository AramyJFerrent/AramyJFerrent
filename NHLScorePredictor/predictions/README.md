# NHL score predictions

Updated Sun Nov 22, 2026 04:56 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Sunday, November 22

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5:00 PM | BUF @ TBL | BUF 3, TBL 4 | TBL 66% | BUF +195 / TBL -195 | 2.7 – 3.8 | 1–5 / 1–6 | 20% | TBL -1.5 45% | 6.5 / 6.5 (over 50%) | Ukko-Pekka Luukkonen (confirmed) / Dennis Hildeby (confirmed) | BUF +180 / TBL -218 | no edge | no edge | no edge |
| 7:00 PM | EDM @ STL | EDM 3, STL 4 | STL 54% | EDM +115 / STL -115 | 3.0 – 3.2 | 1–5 / 1–6 | 22% | STL -1.5 33% | 6.2 / 6.5 (over 45%) | Tristan Jarry (confirmed) / Joel Hofer (confirmed) | EDM +105 / STL -125 | no edge | no edge | no edge |
| 7:00 PM | PIT @ DAL | PIT 2, DAL 3 | DAL 66% | PIT +195 / DAL -195 | 2.6 – 3.6 | 1–5 / 1–6 | 21% | DAL -1.5 43% | 6.2 / 6.5 (over 45%) | Arturs Silovs (expected) / Jake Oettinger (confirmed) | PIT +190 / DAL -230 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | CHI @ VAN | CHI 4, VAN 3 | CHI 51% | CHI -105 / VAN +105 | 3.2 – 3.2 | 1–6 / 1–6 | 22% | CHI -1.5 31% | 6.4 / 6.5 (over 48%) | Drew Commesso (expected) / Nikita Tolopilo (expected) | CHI -115 / VAN -105 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Monday, November 23

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | CBJ @ NJD | CBJ 2, NJD 3 | NJD 62% | CBJ +160 / NJD -160 | 2.7 – 3.5 | 1–5 / 1–6 | 22% | NJD -1.5 40% | 6.3 / 6.5 (over 46%) | Jet Greaves (expected) / Connor Hellebuyck (expected) | CBJ +170 / NJD -205 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:30 PM | LAK @ MTL | LAK 2, MTL 3 | MTL 58% | LAK +140 / MTL -140 | 2.8 – 3.3 | 1–5 / 1–6 | 22% | MTL -1.5 37% | 6.2 / 6.5 (over 44%) | Darcy Kuemper (expected) / Jacob Fowler (expected) | LAK +124 / MTL -148 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:30 PM | CGY @ OTT | CGY 2, OTT 3 | OTT 66% | CGY +190 / OTT -190 | 2.5 – 3.5 | 1–5 / 1–6 | 20% | OTT -1.5 44% | 6.1 / 5.5 (over 54%) | Dustin Wolf (expected) / Linus Ullmark (expected) | CGY +180 / OTT -218 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:30 PM | TOR @ NYI | TOR 3, NYI 4 | NYI 58% | TOR +140 / NYI -140 | 3.0 – 3.5 | 1–5 / 1–6 | 22% | NYI -1.5 37% | 6.4 / 6.5 (over 49%) | Sergei Bobrovsky (expected) / Ilya Sorokin (expected) | TOR +124 / NYI -148 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:30 PM | UTA @ WPG | UTA 4, WPG 3 | UTA 52% | UTA -105 / WPG +105 | 3.3 – 3.2 | 1–6 / 1–6 | 22% | UTA -1.5 31% | 6.4 / 6.5 (over 48%) | Karel Vejmelka (expected) / Stuart Skinner (expected) | UTA -112 / WPG -108 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:40 PM | ANA @ SEA | ANA 3, SEA 4 | SEA 52% | ANA +110 / SEA -110 | 3.3 – 3.5 | 1–6 / 1–6 | 21% | SEA -1.5 32% | 6.7 / 6.5 (over 54%) | Lukas Dostal (expected) / Philipp Grubauer (expected) | ANA -105 / SEA -115 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | MIN @ SJS | MIN 4, SJS 3 | MIN 70% | MIN -235 / SJS +235 | 3.9 – 2.6 | 1–6 / 1–5 | 20% | MIN -1.5 49% | 6.5 / 6.5 (over 50%) | Jesper Wallstedt (expected) / Yaroslav Askarov (expected) | MIN -218 / SJS +180 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Tuesday, November 24

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8:00 PM | VGK @ EDM | VGK 3, EDM 2 | VGK 51% | VGK -100 / EDM +100 | 3.1 – 3.1 | 1–5 / 1–5 | 23% | VGK -1.5 30% | 6.2 | Carter Hart (expected) / Devon Levi (expected) | – | no line yet (model fair EDM +1.5 -235 / VGK -1.5 +235) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 372 | 0.6595 | 0.2335 | 61.8% | 1.38 | 1.83 | 89.7% |
| Model only (before blending) | 372 | 0.6623 | 0.2349 | 59.9% | – | – | – |
| Elo | 372 | 0.6712 | 0.2392 | 58.3% | – | – | – |
| Final prediction, games with a line | 238 | 0.6661 | 0.2366 | 60.1% | 1.37 | 1.88 | 89.7% |
| Model only, games with a line | 238 | 0.6705 | 0.2388 | 57.1% | – | – | – |
| Betting market (de-vigged moneyline) | 238 | 0.6640 | 0.2356 | 60.5% | – | 1.87 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.5% of regular-season games, happened in 22.3%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 5 | 0-5-0 | 5.2 | -5.25 | -100.0% | +8.0% |
| Moneyline | 13 | 8-5-0 | 14.7 | +5.40 | +36.8% | +5.5% |
| Total | 2 | 1-1-0 | 1.7 | +0.04 | +2.4% | +3.4% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 40 of 53 games (75%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Saturday, November 21

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| EDM @ CAR | 3–4 | 4–7 | 63% | no | Devon Levi / Pyotr Kochetkov |
| CHI @ CGY | 2–3 | 4–3 (OT) | 40% | yes | Spencer Knight / Dustin Wolf |
| BUF @ FLA | 3–4 | 3–4 | 55% | yes | Alex Lyon / Jacob Markstrom |
| PIT @ NSH | 3–4 | 3–4 | 51% | yes | Sergei Murashov / Juuse Saros |
| WSH @ BOS | 3–4 | 5–7 | 56% | no | Charlie Lindgren / Jeremy Swayman |
| CBJ @ TOR | 3–4 | 4–3 | 46% | yes | Cam Talbot / Anthony Stolarz |
| PHI @ MTL | 2–3 | 4–3 | 40% | yes | Dan Vladar / Jacob Fowler |
| LAK @ OTT | 2–3 | 2–4 | 61% | yes | Anton Forsberg / Linus Ullmark |
| NYI @ DET | 3–2 | 3–2 | 53% | yes | Ilya Sorokin / John Gibson |
| NJD @ STL | 3–2 | 6–9 | 48% | no | Connor Hellebuyck / Joel Hofer |
| VGK @ WPG | 4–3 | 5–4 (SO) | 56% | yes | Carter Hart / Stuart Skinner |
| ANA @ UTA | 3–4 | 2–3 | 63% | yes | Ville Husso / Sebastian Cossa |
| MIN @ VAN | 4–3 | 3–4 (SO) | 27% | yes | Jesper Wallstedt / Leevi Meriläinen |
| SEA @ SJS | 4–3 | 3–4 | 49% | yes | Philipp Grubauer / Alex Nedeljkovic |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.81 | +0.49 | +0.32 | 3.41 | 2.30 | 8.59 | 7.08 | 1594 |
| 2 | TBL | +0.47 | +0.22 | +0.25 | 2.94 | 2.36 | 8.04 | 8.02 | 1557 |
| 3 | UTA | +0.36 | +0.20 | +0.16 | 3.08 | 2.42 | 8.34 | 8.88 | 1500 |
| 4 | VGK | +0.29 | +0.08 | +0.21 | 2.73 | 2.41 | 9.37 | 7.23 | 1524 |
| 5 | MIN | +0.29 | +0.10 | +0.18 | 2.81 | 2.48 | 8.85 | 7.97 | 1568 |
| 6 | OTT | +0.25 | +0.02 | +0.23 | 2.72 | 2.36 | 8.01 | 8.22 | 1529 |
| 7 | COL | +0.24 | +0.21 | +0.03 | 2.84 | 2.68 | 8.02 | 8.06 | 1555 |
| 8 | DAL | +0.22 | -0.06 | +0.28 | 2.58 | 2.33 | 9.40 | 7.30 | 1532 |
| 9 | PIT | +0.20 | +0.16 | +0.05 | 2.98 | 2.57 | 7.79 | 8.08 | 1476 |
| 10 | NJD | +0.18 | +0.06 | +0.12 | 2.79 | 2.48 | 9.24 | 7.92 | 1522 |
| 11 | STL | +0.15 | +0.09 | +0.06 | 2.80 | 2.61 | 7.36 | 8.22 | 1511 |
| 12 | FLA | +0.12 | -0.04 | +0.16 | 2.50 | 2.47 | 9.55 | 7.72 | 1507 |
| 13 | WSH | +0.11 | +0.16 | -0.05 | 2.95 | 2.70 | 8.21 | 8.10 | 1494 |
| 14 | BOS | +0.10 | +0.09 | +0.01 | 2.82 | 2.69 | 7.69 | 8.29 | 1531 |
| 15 | NYR | +0.08 | +0.02 | +0.06 | 2.70 | 2.64 | 8.90 | 7.74 | 1507 |
| 16 | LAK | +0.02 | -0.14 | +0.16 | 2.49 | 2.47 | 8.20 | 8.14 | 1464 |
| 17 | BUF | +0.02 | +0.07 | -0.04 | 2.71 | 2.70 | 8.07 | 8.66 | 1503 |
| 18 | EDM | +0.00 | +0.01 | -0.01 | 2.41 | 2.67 | 9.72 | 8.32 | 1541 |
| 19 | MTL | -0.02 | +0.03 | -0.05 | 2.77 | 2.76 | 7.66 | 8.52 | 1533 |
| 20 | NYI | -0.06 | -0.00 | -0.05 | 2.74 | 2.78 | 7.31 | 8.82 | 1499 |
| 21 | NSH | -0.08 | -0.01 | -0.07 | 2.73 | 2.76 | 8.09 | 7.71 | 1503 |
| 22 | DET | -0.13 | -0.12 | -0.01 | 2.60 | 2.66 | 8.61 | 8.72 | 1471 |
| 23 | CBJ | -0.14 | -0.06 | -0.08 | 2.65 | 2.75 | 7.96 | 8.64 | 1482 |
| 24 | WPG | -0.15 | -0.09 | -0.05 | 2.50 | 2.75 | 8.65 | 9.25 | 1485 |
| 25 | TOR | -0.16 | -0.07 | -0.08 | 2.44 | 2.74 | 8.80 | 8.48 | 1450 |
| 26 | PHI | -0.17 | -0.22 | +0.04 | 2.36 | 2.60 | 7.92 | 7.71 | 1478 |
| 27 | CGY | -0.27 | -0.14 | -0.13 | 2.52 | 2.83 | 7.16 | 7.72 | 1455 |
| 28 | SEA | -0.34 | -0.14 | -0.20 | 2.38 | 2.89 | 7.45 | 8.80 | 1472 |
| 29 | ANA | -0.34 | +0.02 | -0.36 | 2.72 | 3.04 | 8.01 | 8.17 | 1478 |
| 30 | CHI | -0.64 | -0.30 | -0.35 | 2.20 | 3.02 | 7.26 | 8.75 | 1422 |
| 31 | SJS | -0.74 | -0.22 | -0.52 | 2.33 | 3.22 | 7.38 | 9.36 | 1452 |
| 32 | VAN | -0.78 | -0.27 | -0.51 | 2.18 | 3.20 | 7.82 | 8.86 | 1405 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 66% | +0.44 | +0.18 |
| MIN | Jesper Wallstedt | 89% | +0.32 | +0.13 |
| BOS | Jeremy Swayman | 74% | +0.31 | +0.13 |
| MTL | Jacob Fowler | 67% | +0.30 | +0.13 |
| WSH | Logan Thompson | 70% | +0.28 | +0.12 |
| COL | Mackenzie Blackwood | 67% | +0.24 | +0.10 |
| TBL | Andrei Vasilevskiy | 78% | +0.18 | +0.07 |
| OTT | Linus Ullmark | 48% | +0.17 | +0.07 |
| STL | Joel Hofer | 85% | +0.16 | +0.07 |
| NJD | Connor Hellebuyck | 56% | +0.10 | +0.04 |
| DAL | Jake Oettinger | 78% | +0.08 | +0.03 |
| CHI | Spencer Knight | 71% | +0.05 | +0.02 |
| TOR | Anthony Stolarz | 51% | +0.04 | +0.02 |
| NYR | Dylan Garand | 60% | +0.02 | +0.01 |
| WPG | Stuart Skinner | 72% | +0.01 | +0.00 |
| NSH | Juuse Saros | 67% | -0.08 | -0.04 |
| PHI | Dan Vladar | 50% | -0.11 | -0.05 |
| CAR | Brandon Bussi | 50% | -0.13 | -0.05 |
| BUF | Ukko-Pekka Luukkonen | 55% | -0.13 | -0.05 |
| SEA | Philipp Grubauer | 60% | -0.14 | -0.06 |
| EDM | Tristan Jarry | 55% | -0.18 | -0.08 |
| UTA | Karel Vejmelka | 56% | -0.18 | -0.08 |
| CBJ | Cam Talbot | 59% | -0.18 | -0.08 |
| SJS | Yaroslav Askarov | 62% | -0.20 | -0.08 |
| DET | John Gibson | 56% | -0.21 | -0.09 |
| LAK | Darcy Kuemper | 59% | -0.22 | -0.09 |
| FLA | Jacob Markstrom | 57% | -0.25 | -0.10 |
| CGY | Dustin Wolf | 58% | -0.25 | -0.11 |
| ANA | Lukas Dostal | 41% | -0.28 | -0.12 |
| VGK | Adin Hill | 51% | -0.29 | -0.12 |
| VAN | Leevi Meriläinen | 51% | -0.33 | -0.14 |
| PIT | Arturs Silovs | 75% | -0.38 | -0.16 |

## Current model fit

- Fitted on 5964 games from 2022-23 to 2026-27.
- Home ice: +2.8% goals for the home team relative to the visitor.
- Second night of a back-to-back: -6.0% goals scored, +3.0% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 21%.
- Blend: 58% on the betting line wherever there is one (fitted on 238 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
