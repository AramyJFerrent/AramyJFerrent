# NFL score predictions

Updated Mon Oct 26, 2026 03:18 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the final prediction, the model blended with the line: its expected points are run through the score simulator against the posted lines, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV, its chance of winning and its stake. Stakes are a 25% share of the Kelly stake, in units of 1% of the bankroll, with at most 3 units on one game. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers (the spread and total columns) often sit several points from the line, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. See the backtest for how they have done on past seasons; the live record is tracked below.

## 2026 Week 7

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mon 10/26 8:15 PM | DAL @ PHI | DAL 23, PHI 20 | DAL 62% | DAL -165 / PHI +165 | 24.3 – 20.3 | 13–37 / 10–31 | PHI -0.8 / DAL -4.5 | 48.4 / 44.5 | no edge | no edge | no edge | Dak Prescott / Jalen Hurts |  |

## 2026 Week 8

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 10/29 8:15 PM | CAR @ GB | CAR 20, GB 23 | GB 61% | CAR +160 / GB -160 | 22.0 – 25.6 | 10–34 / 14–38 | GB -4.5 / GB -3.5 | 48.7 / 47.5 | no edge | no edge | no edge | Bryce Young / Jordan Love |  |
| Sun 11/01 1:00 PM | ARI @ DAL | ARI 24, DAL 31 | DAL 68% | ARI +215 / DAL -215 | 24.1 – 30.4 | 13–37 / 17–43 | DAL -4.0 / DAL -6.5 | 50.6 / 54.5 | no edge | no edge | no edge | Jacoby Brissett / Dak Prescott |  |
| Sun 11/01 1:00 PM | ATL @ TB | ATL 20, TB 23 | TB 57% | ATL +135 / TB -135 | 21.9 – 24.6 | 10–34 / 13–37 | TB -4.9 / TB -2.5 | 40.8 / 46.5 | no edge | no edge | no edge | Michael Penix Jr. / Baker Mayfield |  |
| Sun 11/01 1:00 PM | BAL @ BUF | BAL 24, BUF 27 | BUF 62% | BAL +165 / BUF -165 | 24.6 – 28.6 | 13–37 / 17–41 | BUF -8.9 / BUF -3.5 | 52.7 / 53.5 | no edge | no edge | no edge | Tyler Huntley / Josh Allen |  |
| Sun 11/01 1:00 PM | CLE @ PIT | CLE 17, PIT 20 | PIT 61% | CLE +155 / PIT -155 | 17.6 – 21.0 | 7–29 / 10–33 | PIT -2.5 / PIT -3.5 | 40.1 / 38.5 | no edge | no edge | no edge | Deshaun Watson / Aaron Rodgers |  |
| Sun 11/01 1:00 PM | IND @ JAX | IND 20, JAX 27 | JAX 72% | IND +260 / JAX -260 | 19.5 – 27.0 | 9–31 / 15–40 | JAX -8.2 / JAX -7.5 | 47.1 / 46.5 | no edge | no edge | no edge | Daniel Jones / Trevor Lawrence |  |
| Sun 11/01 1:00 PM | LV @ NYJ | LV 20, NYJ 23 | NYJ 55% | LV +125 / NYJ -125 | 21.2 – 22.9 | 10–33 / 11–35 | NYJ -3.2 / NYJ -1.5 | 44.3 / 44.5 | no edge | no edge | no edge | Kirk Cousins / Geno Smith | wind 12 mph |
| Sun 11/01 1:00 PM | MIN @ DET | MIN 20, DET 23 | DET 59% | MIN +145 / DET -145 | 21.8 – 24.7 | 10–34 / 13–37 | DET -1.8 / DET -3.0 | 43.9 / 46.5 | no edge | no edge | no edge | Kyler Murray / Jared Goff |  |
| Sun 11/01 1:00 PM | TEN @ CIN | TEN 17, CIN 27 | CIN 79% | TEN +375 / CIN -375 | 18.2 – 28.3 | 7–30 / 16–41 | CIN -11.5 / CIN -10.0 | 47.2 / 46.5 | no edge | no edge | no edge | Cam Ward / Joe Burrow |  |
| Sun 11/01 4:05 PM | LAC @ LA | LAC 17, LA 24 | LA 70% | LAC +230 / LA -230 | 18.5 – 25.0 | 7–30 / 13–37 | LA -6.5 / LA -6.5 | 41.4 / 43.5 | no edge | no edge | no edge | Justin Herbert / Matthew Stafford |  |
| Sun 11/01 4:25 PM | KC @ DEN | KC 23, DEN 20 | KC 56% | KC -125 / DEN +125 | 21.4 – 20.1 | 10–34 / 9–31 | DEN -0.6 / KC -1.5 | 45.7 / 41.5 | no edge | no edge | no edge | Patrick Mahomes / Bo Nix |  |
| Sun 11/01 4:25 PM | NE @ MIA | NE 27, MIA 20 | NE 70% | NE -240 / MIA +240 | 25.7 – 18.8 | 13–38 / 7–30 | NE -6.1 / NE -7.0 | 47.2 / 44.5 | no edge | no edge | no edge | Drake Maye / Malik Willis |  |
| Sun 11/01 8:20 PM | PHI @ WAS | PHI 20, WAS 23 | WAS 60% | PHI +150 / WAS -150 | 18.5 – 21.8 | 8–30 / 10–34 | WAS -1.5 / WAS -3.5 | 44.1 / 40.5 | no edge | no edge | no edge | Jalen Hurts / Jayden Daniels |  |
| Mon 11/02 8:15 PM | CHI @ SEA | CHI 20, SEA 23 | SEA 58% | CHI +140 / SEA -140 | 21.8 – 24.7 | 10–34 / 13–37 | SEA -1.5 / SEA -3.0 | 43.1 / 46.5 | no edge | no edge | no edge | Caleb Williams / Sam Darnold |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 106 | 9.36 | 10.55 | 7.21 | 64.8% | 0.230 | 85.8% |
| Model only (before blending) | 106 | 9.34 | 11.07 | 7.39 | 63.8% | – | – |
| Betting line when predicted | 106 | 9.37 | 10.54 | 7.20 | 64.8% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin by about 10 points per game.

80 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines and actual starters, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

Every edge logged with the last prediction before kickoff, graded at the price and stake logged with it (live predictions only; backfilled games, and edges logged before edges were priced from the final prediction, are left out). Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised.

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread line moved toward the model's early spread edge before kickoff: 5 of 5 games (100%). Lines moving toward the edge (closing line value) is the quickest sign that the model knows something the market doesn't yet.

### Week 7 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| NE @ CHI | 24–27 | 24–30 | 59% | yes |
| PIT @ NO | 23–20 | 16–10 | 58% | yes |
| CIN @ BAL | 27–24 | 35–13 | 56% | yes |
| CLE @ TEN | 20–17 | 27–24 | 58% | yes |
| IND @ MIN | 17–24 | 10–16 | 71% | yes |
| MIA @ NYJ | 17–20 | 28–25 | 37% | yes |
| NYG @ HOU | 17–27 | 27–21 | 21% | yes |
| SF @ ATL | 27–24 | 20–29 | 42% | yes |
| TB @ CAR | 20–23 | 43–13 | 39% | no |
| DEN @ ARI | 23–20 | 30–16 | 64% | yes |
| GB @ DET | 24–27 | 17–20 | 61% | yes |
| LA @ LV | 27–24 | 35–21 | 60% | yes |
| KC @ SEA | 20–23 | 3–20 | 59% | no |

## Power ratings

Points per game better than an average team on a neutral field, from opponent-adjusted EPA with this season's games weighted against a preseason prior. Defense is positive when it holds opponents below average.

| # | Team | Net | Offense | Defense | Special teams | Elo |
|---|---|---|---|---|---|---|
| 1 | BUF | +5.2 | +5.7 | -1.3 | +0.8 | 1653 |
| 2 | SEA | +4.5 | -0.9 | +3.6 | +1.7 | 1671 |
| 3 | JAX | +3.9 | +2.5 | +0.8 | +0.6 | 1608 |
| 4 | SF | +3.7 | +4.3 | +0.2 | -0.8 | 1624 |
| 5 | CHI | +3.6 | +2.2 | +0.2 | +1.2 | 1580 |
| 6 | DET | +3.4 | +2.9 | -0.8 | +1.4 | 1565 |
| 7 | NE | +2.9 | +2.2 | +0.5 | +0.1 | 1598 |
| 8 | LA | +2.9 | +3.1 | +1.3 | -1.5 | 1579 |
| 9 | BAL | +2.2 | +2.9 | -0.2 | -0.5 | 1517 |
| 10 | KC | +1.9 | +2.4 | +0.3 | -0.8 | 1565 |
| 11 | MIN | +1.9 | -3.1 | +3.3 | +1.7 | 1636 |
| 12 | GB | +1.9 | +1.9 | +0.5 | -0.5 | 1526 |
| 13 | CIN | +1.8 | +2.3 | -0.7 | +0.2 | 1565 |
| 14 | DEN | +1.4 | -0.4 | +2.1 | -0.3 | 1627 |
| 15 | HOU | +0.6 | -0.8 | +1.0 | +0.3 | 1517 |
| 16 | TB | -0.2 | -1.5 | +1.1 | +0.3 | 1476 |
| 17 | PHI | -0.4 | -2.2 | +1.1 | +0.7 | 1486 |
| 18 | CAR | -0.7 | +0.7 | -1.1 | -0.3 | 1451 |
| 19 | IND | -0.9 | -0.4 | -0.8 | +0.3 | 1419 |
| 20 | PIT | -1.0 | -1.1 | +0.1 | +0.0 | 1558 |
| 21 | NYG | -1.5 | -0.9 | -0.4 | -0.1 | 1464 |
| 22 | DAL | -1.5 | +1.9 | -3.5 | +0.1 | 1433 |
| 23 | ATL | -1.9 | -1.4 | +0.6 | -1.1 | 1489 |
| 24 | WAS | -2.2 | -0.5 | -1.6 | -0.1 | 1415 |
| 25 | CLE | -2.8 | -3.8 | +1.5 | -0.5 | 1469 |
| 26 | NYJ | -3.0 | -2.2 | -1.3 | +0.5 | 1365 |
| 27 | MIA | -3.0 | -0.4 | -2.0 | -0.6 | 1390 |
| 28 | NO | -3.1 | -1.7 | -0.9 | -0.6 | 1413 |
| 29 | LAC | -3.8 | -4.6 | +1.2 | -0.4 | 1409 |
| 30 | ARI | -3.9 | -1.4 | -1.4 | -1.1 | 1379 |
| 31 | LV | -4.9 | -3.3 | -1.1 | -0.5 | 1401 |
| 32 | TEN | -6.8 | -4.5 | -2.3 | +0.0 | 1315 |

## Current model fit

- Fitted on 1799 games from seasons 2020–2026.
- Home field: 1.5 points (1.9 in divisional games).
- QB adjustment: 0.83 points per point of QB value gap.
- Special teams: 0.43 points per point of net special-teams EPA.
- Weight on the betting line: 90% for the margin, 99% for the total.
- Wind: -0.20 total points per mph above 10 mph at open-air stadiums.
