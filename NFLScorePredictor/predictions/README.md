# NFL score predictions

Updated Sun Nov 01, 2026 03:28 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the final prediction, the model blended with the line: its expected points are run through the score simulator against the posted lines, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV, its chance of winning and its stake. Stakes are a 25% share of the Kelly stake, in units of 1% of the bankroll, with at most 3 units on one game. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers (the spread and total columns) often sit several points from the line, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. See the backtest for how they have done on past seasons; the live record is tracked below.

## 2026 Week 8

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 11/01 4:05 PM | LAC @ LA | LAC 20, LA 27 | LA 70% | LAC +230 / LA -230 | 19.9 – 26.5 | 9–31 / 14–38 | LA -7.6 / LA -6.5 | 42.4 / 46.5 | no edge | no edge | no edge | Justin Herbert / Matthew Stafford |  |
| Sun 11/01 4:25 PM | KC @ DEN | KC 23, DEN 20 | KC 54% | KC -120 / DEN +120 | 21.5 – 20.1 | 10–34 / 9–31 | KC -0.7 / KC -1.5 | 47.5 / 41.5 | no edge | no edge | no edge | Patrick Mahomes / Bo Nix |  |
| Sun 11/01 4:25 PM | NE @ MIA | NE 23, MIA 17 | NE 71% | NE -250 / MIA +250 | 24.2 – 17.3 | 13–37 / 7–29 | NE -6.0 / NE -7.0 | 47.1 / 41.5 | no edge | no edge | no edge | Drake Maye / Malik Willis |  |
| Sun 11/01 8:20 PM | PHI @ WAS | PHI 17, WAS 23 | WAS 68% | PHI +210 / WAS -210 | 17.5 – 23.1 | 7–28 / 12–35 | WAS -2.2 / WAS -6.0 | 46.2 / 40.5 | no edge | no edge | no edge | Jalen Hurts / Jayden Daniels |  |
| Mon 11/02 8:15 PM | CHI @ SEA | CHI 20, SEA 23 | SEA 59% | CHI +140 / SEA -140 | 21.8 – 24.6 | 10–34 / 13–37 | SEA -0.8 / SEA -3.0 | 43.1 / 46.5 | no edge | no edge | no edge | Caleb Williams / Sam Darnold |  |

## 2026 Week 9

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 11/05 8:15 PM | JAX @ BAL | JAX 24, BAL 27 | BAL 55% | JAX +120 / BAL -120 | 24.9 – 26.6 | 13–37 / 14–39 | BAL -1.7 / – | 51.5 / – | no line yet | no line yet | no line yet | Trevor Lawrence / Lamar Jackson |  |
| Sun 11/08 9:30 AM | CIN @ ATL | CIN 27, ATL 20 | CIN 67% | CIN -200 / ATL +200 | 26.4 – 20.8 | 14–39 / 10–33 | CIN -5.6 / – | 47.1 / – | no line yet | no line yet | no line yet | Joe Burrow / Michael Penix Jr. |  |
| Sun 11/08 1:00 PM | CLE @ NO | CLE 20, NO 23 | NO 56% | CLE +125 / NO -125 | 19.5 – 21.3 | 9–31 / 10–33 | NO -1.8 / – | 40.8 / – | no line yet | no line yet | no line yet | Deshaun Watson / Tyler Shough |  |
| Sun 11/08 1:00 PM | DAL @ IND | DAL 24, IND 27 | IND 53% | DAL +115 / IND -115 | 25.6 – 26.4 | 13–38 / 14–38 | IND -0.8 / – | 52.0 / – | no line yet | no line yet | no line yet | Dak Prescott / Daniel Jones |  |
| Sun 11/08 1:00 PM | DEN @ CAR | DEN 23, CAR 20 | DEN 52% | DEN -110 / CAR +110 | 22.2 – 21.7 | 10–34 / 10–34 | DEN -0.5 / – | 44.0 / – | no line yet | no line yet | no line yet | Bo Nix / Bryce Young |  |
| Sun 11/08 1:00 PM | DET @ MIA | DET 27, MIA 20 | DET 68% | DET -215 / MIA +215 | 27.6 – 21.4 | 16–40 / 10–34 | DET -6.2 / – | 49.0 / – | no line yet | no line yet | no line yet | Jared Goff / Malik Willis |  |
| Sun 11/08 1:00 PM | LA @ WAS | LA 27, WAS 24 | LA 58% | LA -140 / WAS +140 | 25.8 – 22.9 | 14–38 / 12–35 | LA -2.9 / – | 48.6 / – | no line yet | no line yet | no line yet | Matthew Stafford / Jayden Daniels |  |
| Sun 11/08 1:00 PM | NYG @ PHI | NYG 20, PHI 23 | PHI 58% | NYG +140 / PHI -140 | 19.0 – 22.1 | 9–30 / 10–34 | PHI -3.1 / – | 41.1 / – | no line yet | no line yet | no line yet | J.J. McCarthy / Jalen Hurts |  |
| Sun 11/08 1:00 PM | NYJ @ KC | NYJ 20, KC 27 | KC 69% | NYJ +225 / KC -225 | 19.4 – 25.7 | 9–31 / 13–38 | KC -6.2 / – | 48.1 / – | no line yet | no line yet | no line yet | Geno Smith / Patrick Mahomes | wind 16 mph |
| Sun 11/08 4:05 PM | HOU @ LAC | HOU 20, LAC 17 | HOU 64% | HOU -180 / LAC +180 | 21.4 – 16.9 | 10–34 / 6–28 | HOU -4.5 / – | 38.3 / – | no line yet | no line yet | no line yet | C.J. Stroud / Justin Herbert |  |
| Sun 11/08 4:05 PM | LV @ SF | LV 20, SF 30 | SF 81% | LV +435 / SF -435 | 19.1 – 30.3 | 9–31 / 18–43 | SF -11.2 / – | 49.4 / – | no line yet | no line yet | no line yet | Kirk Cousins / Brock Purdy |  |
| Sun 11/08 4:25 PM | ARI @ SEA | ARI 17, SEA 27 | SEA 80% | ARI +395 / SEA -395 | 15.2 – 25.5 | 6–26 / 13–38 | SEA -10.2 / – | 40.7 / – | no line yet | no line yet | no line yet | Jacoby Brissett / Sam Darnold |  |
| Sun 11/08 4:25 PM | GB @ NE | GB 24, NE 27 | NE 54% | GB +120 / NE -120 | 23.6 – 24.9 | 12–36 / 13–38 | NE -1.3 / – | 48.5 / – | no line yet | no line yet | no line yet | Jordan Love / Drake Maye |  |
| Sun 11/08 8:20 PM | TB @ CHI | TB 20, CHI 23 | CHI 65% | TB +185 / CHI -185 | 20.5 – 25.2 | 10–31 / 13–37 | CHI -4.7 / – | 45.7 / – | no line yet | no line yet | no line yet | Baker Mayfield / Caleb Williams |  |
| Mon 11/09 8:15 PM | BUF @ MIN | BUF 23, MIN 20 | BUF 51% | BUF -105 / MIN +105 | 23.9 – 23.5 | 13–36 / 13–35 | BUF -0.4 / – | 47.4 / – | no line yet | no line yet | no line yet | Josh Allen / Kyler Murray |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 108 | 9.35 | 10.49 | 7.16 | 65.4% | 0.228 | 85.6% |
| Model only (before blending) | 108 | 9.36 | 11.01 | 7.36 | 63.6% | – | – |
| Betting line when predicted | 108 | 9.36 | 10.48 | 7.16 | 65.4% | – | – |

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

## Power ratings

Points per game better than an average team on a neutral field, from opponent-adjusted EPA with this season's games weighted against a preseason prior. Defense is positive when it holds opponents below average.

| # | Team | Net | Offense | Defense | Special teams | Elo |
|---|---|---|---|---|---|---|
| 1 | BUF | +5.2 | +5.6 | -1.3 | +0.8 | 1653 |
| 2 | SEA | +4.4 | -0.8 | +3.6 | +1.7 | 1671 |
| 3 | JAX | +3.8 | +2.4 | +0.8 | +0.6 | 1608 |
| 4 | SF | +3.7 | +4.3 | +0.2 | -0.8 | 1624 |
| 5 | CHI | +3.5 | +2.2 | +0.1 | +1.2 | 1580 |
| 6 | DET | +3.4 | +2.9 | -0.8 | +1.3 | 1565 |
| 7 | NE | +2.9 | +2.2 | +0.5 | +0.1 | 1598 |
| 8 | LA | +2.9 | +3.0 | +1.3 | -1.5 | 1579 |
| 9 | BAL | +2.3 | +2.9 | -0.2 | -0.5 | 1517 |
| 10 | GB | +2.3 | +2.2 | +1.0 | -0.9 | 1539 |
| 11 | KC | +1.9 | +2.3 | +0.3 | -0.8 | 1565 |
| 12 | MIN | +1.9 | -3.0 | +3.2 | +1.6 | 1636 |
| 13 | CIN | +1.7 | +2.3 | -0.7 | +0.2 | 1565 |
| 14 | DEN | +1.3 | -0.4 | +2.0 | -0.3 | 1627 |
| 15 | HOU | +0.6 | -0.8 | +1.1 | +0.3 | 1517 |
| 16 | TB | -0.1 | -1.5 | +1.1 | +0.3 | 1476 |
| 17 | DAL | -0.4 | +2.9 | -3.5 | +0.2 | 1472 |
| 18 | IND | -0.9 | -0.4 | -0.8 | +0.2 | 1419 |
| 19 | PIT | -1.0 | -1.1 | +0.1 | +0.0 | 1558 |
| 20 | PHI | -1.2 | -2.2 | +0.5 | +0.5 | 1447 |
| 21 | CAR | -1.2 | -0.1 | -1.3 | +0.1 | 1437 |
| 22 | NYG | -1.4 | -0.9 | -0.4 | -0.1 | 1464 |
| 23 | ATL | -1.9 | -1.3 | +0.5 | -1.1 | 1489 |
| 24 | WAS | -2.2 | -0.5 | -1.6 | -0.1 | 1415 |
| 25 | CLE | -2.9 | -3.9 | +1.4 | -0.5 | 1469 |
| 26 | MIA | -3.0 | -0.4 | -1.9 | -0.6 | 1390 |
| 27 | NYJ | -3.0 | -2.2 | -1.2 | +0.4 | 1365 |
| 28 | NO | -3.1 | -1.7 | -0.8 | -0.6 | 1413 |
| 29 | LAC | -3.7 | -4.6 | +1.2 | -0.4 | 1409 |
| 30 | ARI | -3.9 | -1.4 | -1.4 | -1.1 | 1379 |
| 31 | LV | -4.9 | -3.3 | -1.1 | -0.5 | 1401 |
| 32 | TEN | -6.7 | -4.5 | -2.2 | +0.0 | 1315 |

## Current model fit

- Fitted on 1801 games from seasons 2020–2026.
- Home field: 1.5 points (1.8 in divisional games).
- QB adjustment: 0.83 points per point of QB value gap.
- Special teams: 0.43 points per point of net special-teams EPA.
- Weight on the betting line: 91% for the margin, 99% for the total.
- Wind: -0.20 total points per mph above 10 mph at open-air stadiums.
