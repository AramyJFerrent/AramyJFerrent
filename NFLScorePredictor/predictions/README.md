# NFL score predictions

Updated Sun Nov 22, 2026 03:21 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the final prediction, the model blended with the line: its expected points are run through the score simulator against the posted lines, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV, its chance of winning and its stake. Stakes are a 25% share of the Kelly stake, in units of 1% of the bankroll, with at most 3 units on one game. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers (the spread and total columns) often sit several points from the line, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. See the backtest for how they have done on past seasons; the live record is tracked below.

## 2026 Week 11

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 11/22 4:05 PM | NYJ @ LAC | NYJ 20, LAC 23 | LAC 58% | NYJ +140 / LAC -140 | 20.4 – 23.1 | 10–32 / 12–35 | NYJ -0.2 / LAC -3.0 | 42.7 / 43.5 | no edge | no edge | no edge | Geno Smith / Justin Herbert |  |
| Sun 11/22 4:25 PM | JAX @ NYG | JAX 27, NYG 20 | JAX 68% | JAX -210 / NYG +210 | 25.7 – 19.8 | 14–38 / 9–31 | JAX -4.6 / JAX -6.0 | 44.9 / 45.5 | no edge | no edge | no edge | Trevor Lawrence / J.J. McCarthy |  |
| Sun 11/22 4:25 PM | LV @ DEN | LV 17, DEN 27 | DEN 81% | LV +435 / DEN -435 | 14.9 – 25.6 | 6–26 / 13–38 | DEN -13.7 / DEN -10.5 | 40.5 / 40.5 | no edge | no edge | no edge | Fernando Mendoza / Bo Nix |  |
| Sun 11/22 8:20 PM | MIN @ SF | MIN 20, SF 23 | SF 60% | MIN +150 / SF -150 | 21.6 – 24.9 | 10–34 / 13–37 | SF -0.9 / SF -3.5 | 47.4 / 46.5 | no edge | no edge | no edge | Kirk Cousins / Brock Purdy |  |
| Mon 11/23 8:15 PM | CIN @ WAS | CIN 27, WAS 24 | CIN 67% | CIN -205 / WAS +205 | 29.6 – 24.1 | 17–42 / 13–36 | CIN -1.2 / CIN -6.0 | 53.5 / 54.5 | no edge | no edge | no edge | Joe Burrow / Jayden Daniels | wind 14 mph |

## 2026 Week 12

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wed 11/25 8:00 PM | GB @ LA | GB 20, LA 23 | LA 59% | GB +145 / LA -145 | 21.3 – 24.3 | 10–33 / 13–37 | LA -3.4 / LA -3.0 | 48.4 / 45.5 | no edge | no edge | no edge | Jordan Love / Matthew Stafford |  |
| Thu 11/26 1:00 PM | CHI @ DET | CHI 24, DET 27 | DET 57% | CHI +130 / DET -130 | 24.2 – 26.1 | 13–36 / 14–38 | DET -1.9 / – | 50.3 / – | no line yet | no line yet | no line yet | Caleb Williams / Jared Goff |  |
| Thu 11/26 4:30 PM | PHI @ DAL | PHI 20, DAL 27 | DAL 68% | PHI +215 / DAL -215 | 19.6 – 25.9 | 9–31 / 14–38 | DAL -6.3 / – | 45.5 / – | no line yet | no line yet | no line yet | Joe Milton III / Dak Prescott |  |
| Thu 11/26 8:20 PM | KC @ BUF | KC 24, BUF 27 | BUF 63% | KC +170 / BUF -170 | 21.9 – 26.0 | 10–34 / 14–38 | BUF -4.1 / – | 52.7 / – | no line yet | no line yet | no line yet | Patrick Mahomes / Josh Allen | wind 19 mph |
| Fri 11/27 3:00 PM | DEN @ PIT | DEN 23, PIT 20 | DEN 52% | DEN -105 / PIT +105 | 21.5 – 20.6 | 10–34 / 10–33 | DEN -0.8 / – | 43.9 / – | no line yet | no line yet | no line yet | Bo Nix / Aaron Rodgers | wind 14 mph |
| Sun 11/29 1:00 PM | ATL @ MIN | ATL 13, MIN 23 | MIN 77% | ATL +330 / MIN -330 | 14.9 – 23.4 | 6–26 / 12–35 | MIN -8.5 / – | 38.2 / – | no line yet | no line yet | no line yet | Michael Penix Jr. / Kirk Cousins |  |
| Sun 11/29 1:00 PM | BAL @ HOU | BAL 20, HOU 27 | HOU 71% | BAL +245 / HOU -245 | 18.2 – 25.1 | 7–30 / 13–37 | HOU -6.9 / – | 43.3 / – | no line yet | no line yet | no line yet | Tyler Huntley / C.J. Stroud |  |
| Sun 11/29 1:00 PM | NO @ CIN | NO 20, CIN 27 | CIN 73% | NO +270 / CIN -270 | 21.4 – 29.2 | 10–34 / 17–42 | CIN -7.8 / – | 50.5 / – | no line yet | no line yet | no line yet | Tyler Shough / Joe Burrow |  |
| Sun 11/29 1:00 PM | NYG @ IND | NYG 20, IND 23 | IND 51% | NYG +105 / IND -105 | 20.2 – 20.7 | 10–31 / 10–32 | IND -0.5 / – | 40.9 / – | no line yet | no line yet | no line yet | J.J. McCarthy / Anthony Richardson |  |
| Sun 11/29 1:00 PM | NYJ @ MIA | NYJ 20, MIA 17 | NYJ 56% | NYJ -130 / MIA +130 | 21.3 – 19.4 | 10–33 / 9–31 | NYJ -2.0 / – | 43.3 / – | no line yet | no line yet | no line yet | Geno Smith / Kyle McCord | wind 15 mph |
| Sun 11/29 1:00 PM | TEN @ JAX | TEN 17, JAX 31 | JAX 85% | TEN +575 / JAX -575 | 16.5 – 29.5 | 6–27 / 17–42 | JAX -12.9 / – | 46.0 / – | no line yet | no line yet | no line yet | Cam Ward / Trevor Lawrence |  |
| Sun 11/29 4:05 PM | NE @ LAC | NE 24, LAC 17 | NE 68% | NE -210 / LAC +210 | 23.8 – 18.1 | 13–36 / 7–30 | NE -5.7 / – | 41.9 / – | no line yet | no line yet | no line yet | Drake Maye / Justin Herbert |  |
| Sun 11/29 4:25 PM | SEA @ SF | SEA 24, SF 27 | SF 56% | SEA +125 / SF -125 | 23.4 – 25.1 | 12–35 / 13–37 | SF -1.7 / – | 48.5 / – | no line yet | no line yet | no line yet | Sam Darnold / Brock Purdy |  |
| Sun 11/29 4:25 PM | WAS @ ARI | WAS 23, ARI 20 | WAS 57% | WAS -130 / ARI +130 | 24.3 – 22.1 | 13–37 / 10–34 | WAS -2.1 / – | 46.4 / – | no line yet | no line yet | no line yet | Jayden Daniels / Gardner Minshew |  |
| Sun 11/29 8:20 PM | LV @ CLE | LV 13, CLE 23 | CLE 79% | LV +370 / CLE -370 | 12.9 – 22.4 | 3–23 / 10–35 | CLE -9.5 / – | 37.6 / – | no line yet | no line yet | no line yet | Fernando Mendoza / Deshaun Watson | wind 14 mph |
| Mon 11/30 8:15 PM | CAR @ TB | CAR 20, TB 23 | TB 62% | CAR +165 / TB -165 | 18.6 – 22.5 | 7–30 / 10–34 | TB -3.9 / – | 43.2 / – | no line yet | no line yet | no line yet | Bryce Young / Baker Mayfield | wind 14 mph |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 151 | 9.57 | 10.41 | 7.27 | 68.7% | 0.212 | 84.4% |
| Model only (before blending) | 151 | 9.67 | 10.82 | 7.40 | 69.3% | – | – |
| Betting line when predicted | 151 | 9.57 | 10.41 | 7.27 | 68.7% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin by about 10 points per game.

80 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines and actual starters, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

Every edge logged with the last prediction before kickoff, graded at the price and stake logged with it (live predictions only; backfilled games, and edges logged before edges were priced from the final prediction, are left out). Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised.

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 1 | 0-1-0 | 0.3 | -0.28 | -100.0% | +5.6% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread line moved toward the model's early spread edge before kickoff: 5 of 7 games (71%). Lines moving toward the edge (closing line value) is the quickest sign that the model knows something the market doesn't yet.

### Week 11 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| IND @ HOU | 17–27 | 3–26 | 83% | no |

## Power ratings

Points per game better than an average team on a neutral field, from opponent-adjusted EPA with this season's games weighted against a preseason prior. Defense is positive when it holds opponents below average.

| # | Team | Net | Offense | Defense | Special teams | Elo |
|---|---|---|---|---|---|---|
| 1 | BUF | +5.4 | +4.6 | +0.1 | +0.6 | 1705 |
| 2 | JAX | +5.3 | +2.9 | +1.5 | +0.9 | 1654 |
| 3 | SF | +4.6 | +5.2 | +0.1 | -0.7 | 1647 |
| 4 | DET | +4.3 | +2.9 | -0.0 | +1.4 | 1625 |
| 5 | SEA | +4.0 | +0.0 | +3.0 | +0.9 | 1647 |
| 6 | CHI | +3.9 | +2.3 | +0.3 | +1.4 | 1629 |
| 7 | LA | +3.8 | +3.1 | +2.1 | -1.4 | 1622 |
| 8 | CIN | +2.6 | +3.8 | -1.5 | +0.3 | 1615 |
| 9 | HOU | +2.1 | -0.0 | +1.5 | +0.7 | 1541 |
| 10 | KC | +2.1 | +2.8 | +0.8 | -1.5 | 1589 |
| 11 | MIN | +2.0 | -3.3 | +3.6 | +1.6 | 1625 |
| 12 | DEN | +1.6 | +0.2 | +1.4 | +0.0 | 1647 |
| 13 | GB | +1.6 | +2.1 | +0.4 | -1.0 | 1546 |
| 14 | NE | +1.5 | +1.4 | -0.0 | +0.1 | 1537 |
| 15 | BAL | +0.4 | +1.4 | -0.2 | -0.8 | 1456 |
| 16 | TB | -0.0 | -1.8 | +1.5 | +0.3 | 1494 |
| 17 | DAL | -0.3 | +2.9 | -3.3 | +0.1 | 1455 |
| 18 | PIT | -0.8 | -0.6 | -0.2 | +0.1 | 1551 |
| 19 | NYG | -0.9 | -0.4 | -0.2 | -0.2 | 1467 |
| 20 | CAR | -1.4 | -0.2 | -0.9 | -0.4 | 1443 |
| 21 | WAS | -1.5 | -0.3 | -1.5 | +0.3 | 1447 |
| 22 | PHI | -1.5 | -2.2 | +0.7 | -0.0 | 1397 |
| 23 | IND | -2.1 | -1.8 | -0.7 | +0.4 | 1382 |
| 24 | CLE | -2.8 | -3.8 | +0.9 | +0.1 | 1460 |
| 25 | NO | -3.1 | -2.0 | -0.3 | -0.8 | 1404 |
| 26 | ATL | -3.4 | -2.3 | -0.1 | -1.0 | 1421 |
| 27 | LAC | -3.9 | -4.4 | +0.9 | -0.4 | 1395 |
| 28 | NYJ | -3.9 | -2.2 | -2.3 | +0.5 | 1328 |
| 29 | MIA | -4.0 | -1.6 | -1.4 | -0.9 | 1359 |
| 30 | ARI | -4.6 | -2.2 | -1.6 | -0.9 | 1374 |
| 31 | LV | -5.1 | -3.3 | -2.0 | +0.2 | 1399 |
| 32 | TEN | -5.8 | -3.1 | -2.6 | -0.1 | 1301 |

## Current model fit

- Fitted on 1844 games from seasons 2020–2026.
- Home field: 1.4 points (1.9 in divisional games).
- QB adjustment: 0.86 points per point of QB value gap.
- Special teams: 0.46 points per point of net special-teams EPA.
- Weight on the betting line: 91% for the margin, 96% for the total.
- Wind: -0.20 total points per mph above 10 mph at open-air stadiums.
