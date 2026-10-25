# NFL score predictions

Updated Sun Oct 25, 2026 01:04 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the final prediction, the model blended with the line: its expected points are run through the score simulator against the posted lines, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV, its chance of winning and its stake. Stakes are a 25% share of the Kelly stake, in units of 1% of the bankroll, with at most 3 units on one game. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers (the spread and total columns) often sit several points from the line, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. See the backtest for how they have done on past seasons; the live record is tracked below.

## 2026 Week 7

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 10/25 4:05 PM | DEN @ ARI | DEN 23, ARI 20 | DEN 63% | DEN -170 / ARI +170 | 24.0 – 19.5 | 13–36 / 9–31 | DEN -4.0 / DEN -4.5 | 45.9 / 43.5 | no edge | no edge | no edge | Bo Nix / Jacoby Brissett |  |
| Sun 10/25 4:25 PM | GB @ DET | GB 27, DET 30 | DET 61% | GB +155 / DET -155 | 25.9 – 29.6 | 14–38 / 17–42 | DET -5.2 / DET -3.5 | 53.3 / 55.5 | no edge | no edge | no edge | Jordan Love / Jared Goff |  |
| Sun 10/25 4:25 PM | LA @ LV | LA 27, LV 24 | LA 60% | LA -150 / LV +150 | 25.9 – 22.5 | 14–38 / 10–34 | LA -2.6 / LA -3.5 | 46.9 / 48.5 | no edge | no edge | no edge | Matthew Stafford / Kirk Cousins |  |
| Sun 10/25 8:20 PM | KC @ SEA | KC 20, SEA 23 | SEA 59% | KC +140 / SEA -140 | 19.9 – 22.6 | 9–31 / 11–35 | SEA -0.9 / SEA -3.0 | 44.6 / 42.5 | no edge | no edge | no edge | Patrick Mahomes / Sam Darnold |  |
| Mon 10/26 8:15 PM | DAL @ PHI | DAL 23, PHI 20 | DAL 62% | DAL -165 / PHI +165 | 23.7 – 19.8 | 13–36 / 9–31 | PHI -0.7 / DAL -4.5 | 49.0 / 43.5 | no edge | no edge | no edge | Dak Prescott / Jalen Hurts |  |

## 2026 Week 8

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 10/29 8:15 PM | CAR @ GB | CAR 24, GB 27 | GB 60% | CAR +150 / GB -150 | 22.2 – 25.3 | 10–34 / 13–37 | GB -3.7 / GB -3.0 | 49.4 / 47.5 | no edge | no edge | no edge | Bryce Young / Jordan Love |  |
| Sun 11/01 1:00 PM | ARI @ DAL | ARI 24, DAL 27 | DAL 67% | ARI +205 / DAL -205 | 22.7 – 28.8 | 10–35 / 17–41 | DAL -3.4 / DAL -6.5 | 50.9 / 51.5 | no edge | no edge | no edge | Jacoby Brissett / Dak Prescott |  |
| Sun 11/01 1:00 PM | ATL @ TB | ATL 20, TB 23 | TB 54% | ATL +120 / TB -120 | 21.3 – 22.8 | 10–33 / 11–34 | TB -1.1 / TB -1.5 | 37.3 / 44.5 | no edge | no edge | no edge | Michael Penix Jr. / Jalon Daniels |  |
| Sun 11/01 1:00 PM | BAL @ BUF | BAL 24, BUF 27 | BUF 61% | BAL +155 / BUF -155 | 24.4 – 28.1 | 13–37 / 16–40 | BUF -8.6 / BUF -3.0 | 52.7 / 52.5 | no edge | no edge | no edge | Tyler Huntley / Josh Allen |  |
| Sun 11/01 1:00 PM | CLE @ PIT | CLE 17, PIT 20 | PIT 56% | CLE +130 / PIT -130 | 18.5 – 20.8 | 7–30 / 10–32 | PIT -2.3 / – | 39.3 / – | no line yet | no line yet | no line yet | Deshaun Watson / Aaron Rodgers |  |
| Sun 11/01 1:00 PM | IND @ JAX | IND 20, JAX 27 | JAX 72% | IND +255 / JAX -255 | 19.8 – 27.3 | 9–31 / 16–40 | JAX -7.5 / JAX -7.5 | 48.1 / 47.5 | no edge | no edge | no edge | Daniel Jones / Trevor Lawrence |  |
| Sun 11/01 1:00 PM | LV @ NYJ | LV 23, NYJ 20 | LV 53% | LV -115 / NYJ +115 | 21.8 – 20.7 | 10–34 / 10–32 | NYJ -1.9 / LV -1.5 | 43.7 / 42.5 | no edge | no edge | no edge | Kirk Cousins / Geno Smith |  |
| Sun 11/01 1:00 PM | MIN @ DET | MIN 20, DET 23 | DET 57% | MIN +135 / DET -135 | 22.0 – 24.5 | 10–34 / 13–37 | DET -2.2 / DET -2.5 | 45.4 / 46.5 | no edge | no edge | no edge | Kyler Murray / Jared Goff |  |
| Sun 11/01 1:00 PM | TEN @ CIN | TEN 17, CIN 27 | CIN 78% | TEN +345 / CIN -345 | 18.2 – 28.3 | 7–30 / 16–41 | CIN -10.9 / CIN -10.0 | 46.6 / 46.5 | no edge | no edge | no edge | Cam Ward / Joe Burrow |  |
| Sun 11/01 4:05 PM | LAC @ LA | LAC 20, LA 27 | LA 71% | LAC +240 / LA -240 | 19.3 – 26.2 | 9–31 / 14–39 | LA -5.7 / LA -7.0 | 41.5 / 45.5 | no edge | no edge | no edge | Justin Herbert / Matthew Stafford |  |
| Sun 11/01 4:25 PM | KC @ DEN | KC 23, DEN 20 | KC 55% | KC -125 / DEN +125 | 22.0 – 20.5 | 10–34 / 10–32 | KC -1.2 / KC -1.5 | 45.7 / 42.5 | no edge | no edge | no edge | Patrick Mahomes / Bo Nix |  |
| Sun 11/01 4:25 PM | NE @ MIA | NE 27, MIA 20 | NE 74% | NE -290 / MIA +290 | 26.4 – 18.1 | 14–38 / 7–30 | NE -7.0 / NE -8.5 | 45.7 / 44.5 | no edge | no edge | no edge | Drake Maye / Malik Willis |  |
| Sun 11/01 8:20 PM | PHI @ WAS | PHI 20, WAS 23 | WAS 61% | PHI +155 / WAS -155 | 19.1 – 22.4 | 9–31 / 10–34 | WAS -1.5 / WAS -3.5 | 44.6 / 41.5 | no edge | no edge | no edge | Jalen Hurts / Jayden Daniels |  |
| Mon 11/02 8:15 PM | CHI @ SEA | CHI 20, SEA 23 | SEA 58% | CHI +140 / SEA -140 | 21.9 – 24.6 | 10–34 / 13–37 | SEA -0.5 / SEA -3.0 | 43.4 / 46.5 | no edge | no edge | no edge | Caleb Williams / Sam Darnold |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 95 | 9.13 | 10.62 | 7.08 | 64.9% | 0.227 | 85.3% |
| Model only (before blending) | 95 | 9.00 | 11.21 | 7.28 | 63.8% | – | – |
| Betting line when predicted | 95 | 9.15 | 10.61 | 7.08 | 64.9% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin by about 10 points per game.

80 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines and actual starters, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

Every edge logged with the last prediction before kickoff, graded at the price and stake logged with it (live predictions only; backfilled games, and edges logged before edges were priced from the final prediction, are left out). Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised.

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread line moved toward the model's early spread edge before kickoff: 2 of 3 games (67%). Lines moving toward the edge (closing line value) is the quickest sign that the model knows something the market doesn't yet.

### Week 7 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| NE @ CHI | 24–27 | 24–30 | 59% | yes |
| PIT @ NO | 23–20 | 16–10 | 58% | yes |

## Power ratings

Points per game better than an average team on a neutral field, from opponent-adjusted EPA with this season's games weighted against a preseason prior. Defense is positive when it holds opponents below average.

| # | Team | Net | Offense | Defense | Special teams | Elo |
|---|---|---|---|---|---|---|
| 1 | BUF | +5.3 | +5.9 | -1.4 | +0.8 | 1653 |
| 2 | SF | +4.2 | +4.7 | +0.2 | -0.7 | 1659 |
| 3 | JAX | +3.9 | +2.6 | +0.7 | +0.6 | 1608 |
| 4 | CHI | +3.7 | +2.4 | +0.1 | +1.2 | 1580 |
| 5 | SEA | +3.5 | -1.3 | +3.3 | +1.6 | 1652 |
| 6 | DET | +3.4 | +3.3 | -1.0 | +1.1 | 1554 |
| 7 | NE | +3.0 | +2.5 | +0.4 | +0.1 | 1598 |
| 8 | KC | +2.9 | +2.8 | +0.7 | -0.6 | 1583 |
| 9 | BAL | +2.8 | +3.3 | +0.1 | -0.6 | 1557 |
| 10 | GB | +2.2 | +2.2 | +0.3 | -0.3 | 1537 |
| 11 | LA | +1.9 | +2.7 | +0.9 | -1.6 | 1559 |
| 12 | MIN | +1.5 | -2.8 | +2.9 | +1.4 | 1630 |
| 13 | CIN | +1.1 | +1.9 | -0.9 | +0.2 | 1526 |
| 14 | HOU | +0.9 | -0.4 | +1.5 | -0.2 | 1547 |
| 15 | DEN | +0.5 | -0.8 | +1.7 | -0.3 | 1613 |
| 16 | CAR | +0.4 | +1.1 | -0.8 | +0.2 | 1499 |
| 17 | IND | -0.4 | +0.1 | -1.0 | +0.5 | 1425 |
| 18 | PHI | -0.5 | -2.1 | +1.0 | +0.7 | 1486 |
| 19 | TB | -1.3 | -1.9 | +0.7 | -0.2 | 1427 |
| 20 | DAL | -1.4 | +2.1 | -3.5 | +0.0 | 1433 |
| 21 | PIT | -1.5 | -1.4 | +0.1 | -0.2 | 1558 |
| 22 | NYG | -1.9 | -1.7 | -0.6 | +0.4 | 1434 |
| 23 | WAS | -2.2 | -0.4 | -1.7 | -0.1 | 1415 |
| 24 | ATL | -2.4 | -1.5 | +0.3 | -1.2 | 1454 |
| 25 | NO | -2.8 | -1.8 | -0.6 | -0.4 | 1413 |
| 26 | NYJ | -2.8 | -2.7 | -0.7 | +0.5 | 1381 |
| 27 | CLE | -3.0 | -4.4 | +1.5 | -0.1 | 1459 |
| 28 | ARI | -3.2 | -1.1 | -1.2 | -1.0 | 1393 |
| 29 | MIA | -3.6 | -1.4 | -1.6 | -0.7 | 1373 |
| 30 | LV | -3.7 | -2.7 | -0.7 | -0.3 | 1421 |
| 31 | LAC | -3.7 | -4.5 | +1.2 | -0.4 | 1409 |
| 32 | TEN | -6.8 | -4.6 | -1.9 | -0.3 | 1325 |

## Current model fit

- Fitted on 1788 games from seasons 2020–2026.
- Home field: 1.5 points (2.0 in divisional games).
- QB adjustment: 0.84 points per point of QB value gap.
- Special teams: 0.45 points per point of net special-teams EPA.
- Weight on the betting line: 89% for the margin, 99% for the total.
- Wind: -0.20 total points per mph above 10 mph at open-air stadiums.
