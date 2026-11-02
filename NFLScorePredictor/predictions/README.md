# NFL score predictions

Updated Sun Nov 01, 2026 09:26 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the final prediction, the model blended with the line: its expected points are run through the score simulator against the posted lines, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV, its chance of winning and its stake. Stakes are a 25% share of the Kelly stake, in units of 1% of the bankroll, with at most 3 units on one game. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers (the spread and total columns) often sit several points from the line, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. See the backtest for how they have done on past seasons; the live record is tracked below.

## 2026 Week 8

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mon 11/02 8:15 PM | CHI @ SEA | CHI 20, SEA 23 | SEA 59% | CHI +140 / SEA -140 | 21.8 – 24.6 | 10–34 / 13–37 | SEA -0.8 / SEA -3.0 | 43.3 / 46.5 | no edge | no edge | no edge | Caleb Williams / Sam Darnold |  |

## 2026 Week 9

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 11/05 8:15 PM | JAX @ BAL | JAX 27, BAL 20 | JAX 74% | JAX -280 / BAL +280 | 25.8 – 17.7 | 13–38 / 7–29 | JAX -4.5 / JAX -8.5 | 45.9 / 43.5 | no edge | no edge | no edge | Trevor Lawrence / Tyler Huntley |  |
| Sun 11/08 9:30 AM | CIN @ ATL | CIN 27, ATL 24 | CIN 62% | CIN -160 / ATL +160 | 27.6 – 23.8 | 16–40 / 12–35 | CIN -6.6 / CIN -3.5 | 46.7 / 51.5 | no edge | no edge | no edge | Joe Burrow / Michael Penix Jr. |  |
| Sun 11/08 1:00 PM | CLE @ NO | CLE 20, NO 23 | NO 60% | CLE +150 / NO -150 | 20.3 – 23.2 | 10–32 / 12–35 | NO -2.4 / NO -3.0 | 40.9 / 43.5 | no edge | no edge | no edge | Deshaun Watson / Tyler Shough |  |
| Sun 11/08 1:00 PM | DAL @ IND | DAL 27, IND 24 | DAL 65% | DAL -190 / IND +190 | 28.7 – 23.7 | 17–41 / 13–35 | DAL -0.4 / DAL -5.5 | 51.4 / 52.5 | no edge | no edge | no edge | Dak Prescott / Daniel Jones |  |
| Sun 11/08 1:00 PM | DEN @ CAR | DEN 23, CAR 20 | DEN 57% | DEN -130 / CAR +130 | 23.4 – 21.1 | 12–36 / 10–33 | DEN -0.7 / DEN -2.5 | 44.9 / 44.5 | no edge | no edge | no edge | Bo Nix / Bryce Young |  |
| Sun 11/08 1:00 PM | DET @ MIA | DET 27, MIA 20 | DET 70% | DET -240 / MIA +240 | 27.7 – 20.7 | 16–41 / 10–33 | DET -6.8 / DET -7.0 | 48.6 / 48.5 | no edge | no edge | no edge | Jared Goff / Malik Willis |  |
| Sun 11/08 1:00 PM | LA @ WAS | LA 26, WAS 23 | LA 59% | LA -145 / WAS +145 | 25.6 – 22.3 | 13–38 / 10–34 | LA -3.3 / – | 47.9 / – | no line yet | no line yet | no line yet | Matthew Stafford / Jayden Daniels |  |
| Sun 11/08 1:00 PM | NYG @ PHI | NYG 20, PHI 23 | PHI 60% | NYG +150 / PHI -150 | 19.2 – 22.2 | 9–31 / 10–34 | PHI -3.1 / – | 41.4 / – | no line yet | no line yet | no line yet | J.J. McCarthy / Jalen Hurts |  |
| Sun 11/08 1:00 PM | NYJ @ KC | NYJ 17, KC 27 | KC 77% | NYJ +340 / KC -340 | 18.0 – 27.6 | 7–30 / 16–40 | KC -6.3 / KC -10.0 | 50.1 / 45.5 | no edge | no edge | no edge | Geno Smith / Patrick Mahomes |  |
| Sun 11/08 4:05 PM | HOU @ LAC | HOU 23, LAC 20 | HOU 64% | HOU -180 / LAC +180 | 23.5 – 18.9 | 12–35 / 9–30 | HOU -5.3 / HOU -4.5 | 37.2 / 42.5 | no edge | no edge | no edge | C.J. Stroud / Justin Herbert |  |
| Sun 11/08 4:05 PM | LV @ SF | LV 20, SF 30 | SF 77% | LV +330 / SF -330 | 20.9 – 30.6 | 10–33 / 17–43 | SF -10.9 / SF -9.5 | 50.9 / 51.5 | no edge | no edge | no edge | Kirk Cousins / Brock Purdy |  |
| Sun 11/08 4:25 PM | ARI @ SEA | ARI 17, SEA 27 | SEA 82% | ARI +460 / SEA -460 | 17.0 – 28.4 | 6–28 / 16–41 | SEA -10.9 / SEA -11.5 | 40.3 / 45.5 | no edge | no edge | no edge | Jacoby Brissett / Sam Darnold |  |
| Sun 11/08 4:25 PM | GB @ NE | GB 24, NE 27 | NE 57% | GB +135 / NE -135 | 22.5 – 24.9 | 10–34 / 13–37 | NE -1.8 / NE -2.5 | 48.7 / 47.5 | no edge | no edge | no edge | Jordan Love / Drake Maye |  |
| Sun 11/08 8:20 PM | TB @ CHI | TB 20, CHI 27 | CHI 68% | TB +210 / CHI -210 | 20.3 – 26.1 | 10–32 / 14–38 | CHI -3.9 / CHI -6.0 | 44.7 / 46.5 | no edge | no edge | no edge | Baker Mayfield / Caleb Williams |  |
| Mon 11/09 8:15 PM | BUF @ MIN | BUF 23, MIN 20 | BUF 58% | BUF -135 / MIN +135 | 24.6 – 21.8 | 13–37 / 10–34 | BUF -1.1 / BUF -3.0 | 46.1 / 46.5 | no edge | no edge | no edge | Josh Allen / Kyler Murray |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 119 | 9.47 | 10.77 | 7.34 | 66.1% | 0.224 | 84.0% |
| Model only (before blending) | 119 | 9.46 | 11.17 | 7.47 | 64.4% | – | – |
| Betting line when predicted | 119 | 9.48 | 10.76 | 7.33 | 66.1% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin by about 10 points per game.

80 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines and actual starters, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

Every edge logged with the last prediction before kickoff, graded at the price and stake logged with it (live predictions only; backfilled games, and edges logged before edges were priced from the final prediction, are left out). Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised.

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread line moved toward the model's early spread edge before kickoff: 5 of 6 games (83%). Lines moving toward the edge (closing line value) is the quickest sign that the model knows something the market doesn't yet.

### Week 8 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| CAR @ GB | 20–23 | 19–27 | 61% | yes |
| ARI @ DAL | 24–30 | 33–30 | 30% | yes |
| ATL @ TB | 20–23 | 0–16 | 58% | no |
| BAL @ BUF | 27–30 | 10–36 | 60% | no |
| CLE @ PIT | 17–20 | 6–27 | 61% | no |
| IND @ JAX | 17–27 | 7–42 | 78% | no |
| LV @ NYJ | 20–23 | 38–33 | 45% | no |
| MIN @ DET | 21–24 | 15–19 | 58% | yes |
| TEN @ CIN | 17–31 | 36–43 | 84% | no |
| LAC @ LA | 20–27 | 9–24 | 70% | yes |
| KC @ DEN | 23–20 | 24–28 | 46% | yes |
| NE @ MIA | 23–17 | 24–19 | 71% | yes |

## Power ratings

Points per game better than an average team on a neutral field, from opponent-adjusted EPA with this season's games weighted against a preseason prior. Defense is positive when it holds opponents below average.

| # | Team | Net | Offense | Defense | Special teams | Elo |
|---|---|---|---|---|---|---|
| 1 | BUF | +5.6 | +5.2 | -0.7 | +1.1 | 1669 |
| 2 | JAX | +4.8 | +2.8 | +1.4 | +0.6 | 1621 |
| 3 | SEA | +4.5 | -0.8 | +3.6 | +1.7 | 1671 |
| 4 | SF | +3.6 | +4.4 | +0.0 | -0.8 | 1624 |
| 5 | NE | +3.5 | +2.6 | +0.9 | +0.1 | 1607 |
| 6 | DET | +3.5 | +2.7 | -0.7 | +1.5 | 1582 |
| 7 | CHI | +3.5 | +2.2 | +0.1 | +1.2 | 1580 |
| 8 | LA | +3.2 | +2.8 | +2.0 | -1.6 | 1590 |
| 9 | GB | +2.3 | +2.3 | +1.0 | -1.0 | 1539 |
| 10 | KC | +1.9 | +2.8 | +0.1 | -1.0 | 1554 |
| 11 | MIN | +1.8 | -3.2 | +3.4 | +1.5 | 1619 |
| 12 | DEN | +1.6 | -0.0 | +1.7 | -0.1 | 1637 |
| 13 | BAL | +1.4 | +2.0 | +0.1 | -0.7 | 1502 |
| 14 | CIN | +1.4 | +2.6 | -1.5 | +0.3 | 1571 |
| 15 | HOU | +0.7 | -0.7 | +1.0 | +0.4 | 1517 |
| 16 | TB | +0.6 | -1.7 | +1.9 | +0.4 | 1501 |
| 17 | DAL | -0.1 | +2.8 | -3.2 | +0.3 | 1451 |
| 18 | PIT | -0.6 | -0.5 | +0.2 | -0.2 | 1576 |
| 19 | PHI | -1.1 | -2.1 | +0.4 | +0.5 | 1447 |
| 20 | CAR | -1.2 | +0.0 | -1.4 | +0.1 | 1437 |
| 21 | NYG | -1.4 | -0.9 | -0.4 | -0.1 | 1464 |
| 22 | IND | -1.8 | -0.9 | -1.1 | +0.2 | 1405 |
| 23 | WAS | -2.2 | -0.5 | -1.7 | -0.1 | 1415 |
| 24 | NYJ | -3.1 | -1.4 | -1.8 | +0.1 | 1346 |
| 25 | ATL | -3.1 | -2.5 | +0.7 | -1.3 | 1464 |
| 26 | NO | -3.2 | -1.6 | -0.9 | -0.6 | 1413 |
| 27 | CLE | -3.2 | -4.1 | +1.1 | -0.2 | 1450 |
| 28 | MIA | -3.6 | -0.9 | -2.1 | -0.6 | 1380 |
| 29 | LAC | -4.3 | -5.5 | +1.5 | -0.3 | 1398 |
| 30 | ARI | -4.4 | -1.8 | -1.4 | -1.2 | 1400 |
| 31 | LV | -4.4 | -2.6 | -1.7 | -0.2 | 1420 |
| 32 | TEN | -6.1 | -3.5 | -2.5 | -0.1 | 1309 |

## Current model fit

- Fitted on 1812 games from seasons 2020–2026.
- Home field: 1.5 points (1.9 in divisional games).
- QB adjustment: 0.83 points per point of QB value gap.
- Special teams: 0.44 points per point of net special-teams EPA.
- Weight on the betting line: 90% for the margin, 98% for the total.
- Wind: -0.20 total points per mph above 10 mph at open-air stadiums.
