# NFL score predictions

Updated Thu Nov 26, 2026 05:20 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the final prediction, the model blended with the line: its expected points are run through the score simulator against the posted lines, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV, its chance of winning and its stake. Stakes are a 25% share of the Kelly stake, in units of 1% of the bankroll, with at most 3 units on one game. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers (the spread and total columns) often sit several points from the line, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. See the backtest for how they have done on past seasons; the live record is tracked below.

## 2026 Week 12

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 11/26 8:20 PM | KC @ BUF | KC 20, BUF 23 | BUF 59% | KC +145 / BUF -145 | 20.9 – 24.0 | 10–33 / 13–36 | BUF -4.5 / BUF -3.0 | 52.2 / 45.5 | no edge | no edge | no edge | Patrick Mahomes / Josh Allen | wind 14 mph |
| Fri 11/27 3:00 PM | DEN @ PIT | DEN 20, PIT 17 | DEN 64% | DEN -180 / PIT +180 | 20.3 – 15.8 | 9–31 / 6–27 | DEN -4.1 / DEN -4.5 | 40.9 / 36.5 | no edge | no edge | no edge | Bo Nix / Mason Rudolph | wind 13 mph |
| Sun 11/29 1:00 PM | ATL @ MIN | ATL 17, MIN 24 | MIN 72% | ATL +260 / MIN -260 | 17.2 – 24.2 | 6–28 / 13–37 | MIN -7.5 / MIN -7.0 | 39.0 / 41.5 | no edge | no edge | no edge | Michael Penix Jr. / Kirk Cousins |  |
| Sun 11/29 1:00 PM | BAL @ HOU | BAL 20, HOU 27 | HOU 69% | BAL +225 / HOU -225 | 20.5 – 26.9 | 10–32 / 15–40 | HOU -5.9 / HOU -6.5 | 44.2 / 47.5 | no edge | no edge | no edge | Jacoby Brissett / C.J. Stroud |  |
| Sun 11/29 1:00 PM | NO @ CIN | NO 20, CIN 30 | CIN 77% | NO +340 / CIN -340 | 19.9 – 29.6 | 9–31 / 17–42 | CIN -7.5 / CIN -10.0 | 50.1 / 49.5 | no edge | no edge | no edge | Tyler Shough / Joe Burrow |  |
| Sun 11/29 1:00 PM | NYG @ IND | NYG 23, IND 20 | NYG 66% | NYG -200 / IND +200 | 23.5 – 18.0 | 12–36 / 7–29 | NYG -0.1 / NYG -6.0 | 40.6 / 41.5 | no edge | no edge | no edge | J.J. McCarthy / Anthony Richardson |  |
| Sun 11/29 1:00 PM | NYJ @ MIA | NYJ 20, MIA 17 | NYJ 64% | NYJ -175 / MIA +175 | 22.0 – 17.6 | 10–34 / 7–29 | NYJ -2.9 / NYJ -4.5 | 43.5 / 39.5 | no edge | no edge | no edge | Geno Smith / Kyle McCord |  |
| Sun 11/29 1:00 PM | TEN @ JAX | TEN 17, JAX 31 | JAX 87% | TEN +685 / JAX -685 | 17.5 – 31.9 | 7–28 / 20–45 | JAX -12.6 / JAX -14.5 | 46.0 / 49.5 | no edge | no edge | no edge | Cam Ward / Trevor Lawrence |  |
| Sun 11/29 4:05 PM | NE @ LAC | NE 20, LAC 17 | NE 59% | NE -140 / LAC +140 | 19.2 – 16.5 | 9–30 / 6–27 | NE -5.8 / NE -2.5 | 43.0 / 35.5 | no edge | no edge | no edge | Drake Maye / Justin Herbert |  |
| Sun 11/29 4:25 PM | SEA @ SF | SEA 20, SF 23 | SF 59% | SEA +145 / SF -145 | 20.3 – 23.3 | 10–31 / 12–35 | SF -2.7 / SF -3.0 | 49.0 / 43.5 | no edge | no edge | no edge | Sam Darnold / Brock Purdy |  |
| Sun 11/29 4:25 PM | WAS @ ARI | WAS 24, ARI 17 | WAS 68% | WAS -215 / ARI +215 | 23.9 – 17.7 | 13–36 / 7–30 | WAS -2.8 / WAS -6.5 | 46.6 / 41.5 | no edge | no edge | no edge | Jayden Daniels / Gardner Minshew |  |
| Sun 11/29 8:20 PM | LV @ CLE | LV 17, CLE 20 | CLE 66% | LV +190 / CLE -190 | 17.7 – 22.6 | 7–29 / 11–34 | CLE -9.5 / CLE -4.5 | 37.7 / 40.5 | no edge | no edge | no edge | Fernando Mendoza / Deshaun Watson |  |
| Mon 11/30 8:15 PM | CAR @ TB | CAR 20, TB 23 | TB 60% | CAR +150 / TB -150 | 20.2 – 23.3 | 10–32 / 12–35 | TB -3.3 / TB -3.0 | 43.9 / 43.5 | no edge | no edge | no edge | Bryce Young / Baker Mayfield |  |

## 2026 Week 13

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 12/03 8:15 PM | KC @ LA | KC 20, LA 23 | LA 55% | KC +125 / LA -125 | 21.5 – 23.1 | 10–34 / 12–35 | LA -2.2 / LA -1.5 | 49.2 / 44.5 | no edge | no edge | no edge | Patrick Mahomes / Matthew Stafford |  |
| Sun 12/06 1:00 PM | CIN @ CLE | CIN 26, CLE 20 | CIN 68% | CIN -215 / CLE +215 | 25.8 – 20.1 | 13–38 / 9–31 | CIN -3.1 / CIN -6.0 | 47.9 / 46.5 | no edge | no edge | no edge | Joe Burrow / Deshaun Watson | wind 13 mph |
| Sun 12/06 1:00 PM | DET @ ATL | DET 27, ATL 20 | DET 72% | DET -255 / ATL +255 | 27.3 – 19.7 | 16–40 / 9–31 | DET -7.5 / – | 47.0 / – | no line yet | no line yet | no line yet | Jared Goff / Michael Penix Jr. |  |
| Sun 12/06 1:00 PM | GB @ NO | GB 23, NO 20 | GB 64% | GB -175 / NO +175 | 25.5 – 21.0 | 13–38 / 10–33 | GB -4.1 / GB -4.5 | 45.3 / 46.5 | no edge | no edge | no edge | Jordan Love / Tyler Shough |  |
| Sun 12/06 1:00 PM | JAX @ CHI | JAX 24, CHI 27 | CHI 56% | JAX +125 / CHI -125 | 23.1 – 25.1 | 12–35 / 13–37 | CHI -2.0 / – | 48.1 / – | no line yet | no line yet | no line yet | Trevor Lawrence / Caleb Williams |  |
| Sun 12/06 1:00 PM | LAC @ TB | LAC 20, TB 23 | TB 67% | LAC +205 / TB -205 | 17.5 – 23.0 | 7–29 / 12–35 | TB -5.2 / TB -5.5 | 39.1 / 40.5 | no edge | no edge | no edge | Justin Herbert / Baker Mayfield |  |
| Sun 12/06 1:00 PM | SF @ NYG | SF 27, NYG 20 | SF 69% | SF -220 / NYG +220 | 26.3 – 19.8 | 14–38 / 9–31 | SF -6.6 / SF -6.5 | 50.0 / 47.5 | no edge | no edge | Under 47.5 (-110): EV +3.2%, 54%, stake 0.9u | Brock Purdy / J.J. McCarthy | wind 17 mph |
| Sun 12/06 1:00 PM | WAS @ TEN | WAS 23, TEN 20 | WAS 64% | WAS -180 / TEN +180 | 26.0 – 21.5 | 14–38 / 10–33 | WAS -4.0 / WAS -4.5 | 46.7 / 47.5 | no edge | no edge | no edge | Jayden Daniels / Cam Ward |  |
| Sun 12/06 4:05 PM | MIA @ DEN | MIA 13, DEN 27 | DEN 89% | MIA +855 / DEN -855 | 12.6 – 26.9 | 3–23 / 15–40 | DEN -11.5 / DEN -14.5 | 40.5 / 39.5 | no edge | no edge | no edge | Kyle McCord / Bo Nix |  |
| Sun 12/06 4:05 PM | PHI @ ARI | PHI 20, ARI 17 | PHI 59% | PHI -145 / ARI +145 | 19.7 – 16.9 | 9–31 / 7–28 | PHI -0.2 / PHI -3.0 | 38.5 / 36.5 | no edge | no edge | no edge | Joe Milton III / Gardner Minshew |  |
| Sun 12/06 4:25 PM | BUF @ NE | BUF 27, NE 17 | BUF 83% | BUF -490 / NE +490 | 27.4 – 15.7 | 16–40 / 6–27 | BUF -2.9 / BUF -12.5 | 51.2 / 44.5 | no edge | NE (+548): EV +5.2%, 16%, stake 0.2u | Under 44.5 (-110): EV +7.1%, 56%, stake 1.9u | Josh Allen / Drake Maye | wind 18 mph |
| Sun 12/06 4:25 PM | CAR @ MIN | CAR 20, MIN 23 | MIN 68% | CAR +210 / MIN -210 | 18.9 – 24.5 | 7–30 / 13–37 | MIN -6.7 / MIN -5.5 | 42.5 / 43.5 | no edge | no edge | no edge | Bryce Young / Kirk Cousins |  |
| Sun 12/06 8:20 PM | HOU @ PIT | HOU 23, PIT 20 | HOU 64% | HOU -180 / PIT +180 | 23.0 – 18.5 | 12–35 / 7–30 | HOU -4.9 / HOU -4.5 | 39.7 / 41.5 | no edge | no edge | no edge | C.J. Stroud / Mason Rudolph |  |
| Mon 12/07 8:15 PM | DAL @ SEA | DAL 24, SEA 27 | SEA 67% | DAL +205 / SEA -205 | 22.3 – 28.2 | 10–34 / 16–41 | SEA -4.5 / SEA -6.0 | 49.2 / 50.5 | no edge | no edge | no edge | Dak Prescott / Sam Darnold |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 165 | 9.40 | 10.46 | 7.26 | 68.9% | 0.209 | 84.8% |
| Model only (before blending) | 165 | 9.53 | 10.94 | 7.42 | 69.5% | – | – |
| Betting line when predicted | 165 | 9.40 | 10.46 | 7.26 | 68.9% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin by about 10 points per game.

80 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines and actual starters, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

Every edge logged with the last prediction before kickoff, graded at the price and stake logged with it (live predictions only; backfilled games, and edges logged before edges were priced from the final prediction, are left out). Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised.

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 2 | 0-2-0 | 0.4 | -0.39 | -100.0% | +5.1% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread line moved toward the model's early spread edge before kickoff: 5 of 7 games (71%). Lines moving toward the edge (closing line value) is the quickest sign that the model knows something the market doesn't yet.

### Week 12 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| GB @ LA | 20–23 | 13–26 | 59% | yes |
| CHI @ DET | 30–27 | 39–35 | 54% | yes |

## Power ratings

Points per game better than an average team on a neutral field, from opponent-adjusted EPA with this season's games weighted against a preseason prior. Defense is positive when it holds opponents below average.

| # | Team | Net | Offense | Defense | Special teams | Elo |
|---|---|---|---|---|---|---|
| 1 | BUF | +5.7 | +4.6 | +0.5 | +0.6 | 1709 |
| 2 | SF | +5.5 | +5.7 | +0.2 | -0.4 | 1677 |
| 3 | JAX | +4.6 | +2.3 | +1.6 | +0.7 | 1627 |
| 4 | DET | +4.3 | +3.8 | -0.5 | +1.0 | 1618 |
| 5 | LA | +4.1 | +3.0 | +2.2 | -1.2 | 1638 |
| 6 | CHI | +4.0 | +2.2 | +0.5 | +1.4 | 1655 |
| 7 | SEA | +3.8 | -0.1 | +3.1 | +0.9 | 1647 |
| 8 | KC | +2.9 | +3.2 | +1.0 | -1.3 | 1600 |
| 9 | DEN | +2.1 | +0.3 | +1.6 | +0.2 | 1655 |
| 10 | CIN | +2.1 | +3.4 | -1.6 | +0.3 | 1599 |
| 11 | HOU | +2.0 | -0.2 | +1.6 | +0.6 | 1541 |
| 12 | NE | +1.5 | +1.3 | +0.1 | +0.0 | 1537 |
| 13 | GB | +1.4 | +1.7 | +0.7 | -1.0 | 1530 |
| 14 | MIN | +1.3 | -3.2 | +3.1 | +1.4 | 1595 |
| 15 | DAL | +0.2 | +3.5 | -3.3 | +0.0 | 1468 |
| 16 | BAL | +0.2 | +1.3 | -0.3 | -0.9 | 1446 |
| 17 | TB | -0.3 | -1.7 | +1.1 | +0.3 | 1482 |
| 18 | NYG | -0.4 | -0.6 | +0.2 | -0.0 | 1494 |
| 19 | CAR | -1.2 | -0.1 | -0.9 | -0.2 | 1453 |
| 20 | WAS | -1.2 | -0.3 | -1.3 | +0.3 | 1463 |
| 21 | PHI | -1.2 | -2.4 | +1.2 | -0.0 | 1416 |
| 22 | PIT | -1.3 | -1.2 | -0.0 | -0.0 | 1533 |
| 23 | IND | -2.1 | -1.8 | -0.8 | +0.4 | 1382 |
| 24 | CLE | -2.9 | -4.0 | +1.0 | +0.1 | 1460 |
| 25 | ATL | -3.3 | -2.2 | -0.2 | -0.9 | 1421 |
| 26 | NO | -3.3 | -2.2 | -0.3 | -0.8 | 1397 |
| 27 | NYJ | -3.5 | -1.6 | -2.4 | +0.4 | 1347 |
| 28 | LAC | -4.0 | -4.0 | +0.3 | -0.2 | 1376 |
| 29 | MIA | -4.4 | -2.2 | -1.4 | -0.9 | 1354 |
| 30 | ARI | -5.1 | -2.2 | -1.9 | -1.0 | 1363 |
| 31 | LV | -5.3 | -3.3 | -2.1 | +0.0 | 1391 |
| 32 | TEN | -6.1 | -3.2 | -3.0 | +0.0 | 1287 |

## Current model fit

- Fitted on 1858 games from seasons 2020–2026.
- Home field: 1.5 points (1.9 in divisional games).
- QB adjustment: 0.85 points per point of QB value gap.
- Special teams: 0.46 points per point of net special-teams EPA.
- Weight on the betting line: 92% for the margin, 97% for the total.
- Wind: -0.20 total points per mph above 10 mph at open-air stadiums.
