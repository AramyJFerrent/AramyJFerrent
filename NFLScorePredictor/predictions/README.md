# NFL score predictions

Updated Sun Nov 22, 2026 10:41 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the final prediction, the model blended with the line: its expected points are run through the score simulator against the posted lines, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV, its chance of winning and its stake. Stakes are a 25% share of the Kelly stake, in units of 1% of the bankroll, with at most 3 units on one game. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers (the spread and total columns) often sit several points from the line, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. See the backtest for how they have done on past seasons; the live record is tracked below.

## 2026 Week 11

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mon 11/23 8:15 PM | CIN @ WAS | CIN 27, WAS 24 | CIN 66% | CIN -195 / WAS +195 | 29.9 – 24.3 | 17–42 / 13–37 | CIN -1.0 / CIN -6.0 | 53.7 / 54.5 | no edge | no edge | no edge | Joe Burrow / Jayden Daniels |  |

## 2026 Week 12

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wed 11/25 8:00 PM | GB @ LA | GB 20, LA 23 | LA 59% | GB +145 / LA -145 | 20.8 – 23.8 | 10–32 / 13–35 | LA -3.4 / LA -3.0 | 48.4 / 44.5 | no edge | no edge | no edge | Jordan Love / Matthew Stafford |  |
| Thu 11/26 1:00 PM | CHI @ DET | CHI 30, DET 27 | CHI 56% | CHI -125 / DET +125 | 28.7 – 26.6 | 17–41 / 15–38 | DET -2.0 / CHI -2.5 | 50.6 / 55.5 | no edge | no edge | no edge | Caleb Williams / Jared Goff |  |
| Thu 11/26 4:30 PM | PHI @ DAL | PHI 20, DAL 27 | DAL 74% | PHI +295 / DAL -295 | 19.6 – 27.9 | 9–31 / 16–41 | DAL -6.5 / DAL -8.5 | 45.7 / 47.5 | no edge | no edge | no edge | Joe Milton III / Dak Prescott |  |
| Thu 11/26 8:20 PM | KC @ BUF | KC 24, BUF 27 | BUF 59% | KC +145 / BUF -145 | 23.3 – 26.4 | 12–35 / 14–38 | BUF -3.9 / BUF -3.0 | 52.7 / 50.5 | no edge | no edge | no edge | Patrick Mahomes / Josh Allen | wind 14 mph |
| Fri 11/27 3:00 PM | DEN @ PIT | DEN 20, PIT 17 | DEN 59% | DEN -145 / PIT +145 | 20.8 – 17.9 | 10–32 / 7–29 | DEN -1.7 / DEN -3.0 | 43.1 / 39.5 | no edge | no edge | no edge | Bo Nix / Aaron Rodgers | wind 15 mph |
| Sun 11/29 1:00 PM | ATL @ MIN | ATL 16, MIN 24 | MIN 77% | ATL +335 / MIN -335 | 14.8 – 23.4 | 6–25 / 12–36 | MIN -8.6 / – | 38.2 / – | no line yet | no line yet | no line yet | Michael Penix Jr. / Kirk Cousins |  |
| Sun 11/29 1:00 PM | BAL @ HOU | BAL 20, HOU 27 | HOU 69% | BAL +225 / HOU -225 | 20.0 – 26.4 | 9–31 / 14–39 | HOU -6.1 / HOU -6.5 | 44.5 / 46.5 | no edge | no edge | no edge | Jacoby Brissett / C.J. Stroud |  |
| Sun 11/29 1:00 PM | NO @ CIN | NO 20, CIN 30 | CIN 78% | NO +355 / CIN -355 | 20.6 – 30.9 | 10–33 / 19–44 | CIN -8.0 / CIN -10.5 | 50.2 / 51.5 | no edge | no edge | no edge | Tyler Shough / Joe Burrow |  |
| Sun 11/29 1:00 PM | NYG @ IND | NYG 24, IND 17 | NYG 69% | NYG -220 / IND +220 | 23.7 – 17.8 | 13–36 / 7–29 | NYG -0.1 / NYG -6.5 | 40.7 / 41.5 | no edge | no edge | no edge | J.J. McCarthy / Anthony Richardson |  |
| Sun 11/29 1:00 PM | NYJ @ MIA | NYJ 23, MIA 20 | NYJ 61% | NYJ -155 / MIA +155 | 22.5 – 19.1 | 10–34 / 9–30 | NYJ -3.1 / NYJ -3.5 | 43.7 / 41.5 | no edge | no edge | no edge | Geno Smith / Kyle McCord |  |
| Sun 11/29 1:00 PM | TEN @ JAX | TEN 17, JAX 31 | JAX 87% | TEN +685 / JAX -685 | 16.6 – 30.9 | 6–27 / 19–44 | JAX -12.8 / JAX -14.5 | 46.1 / 47.5 | no edge | no edge | no edge | Cam Ward / Trevor Lawrence |  |
| Sun 11/29 4:05 PM | NE @ LAC | NE 17, LAC 20 | LAC 54% | NE +115 / LAC -115 | 18.4 – 19.3 | 7–30 / 9–31 | NE -6.0 / LAC -1.5 | 42.8 / 37.5 | no edge | no edge | no edge | Drake Maye / Justin Herbert |  |
| Sun 11/29 4:25 PM | SEA @ SF | SEA 24, SF 27 | SF 56% | SEA +125 / SF -125 | 22.6 – 24.3 | 10–34 / 13–37 | SF -1.7 / – | 48.5 / – | no line yet | no line yet | no line yet | Sam Darnold / Brock Purdy | wind 13 mph |
| Sun 11/29 4:25 PM | WAS @ ARI | WAS 23, ARI 17 | WAS 70% | WAS -235 / ARI +235 | 24.1 – 17.5 | 13–37 / 7–29 | WAS -2.6 / WAS -7.0 | 46.8 / 41.5 | no edge | no edge | no edge | Jayden Daniels / Gardner Minshew |  |
| Sun 11/29 8:20 PM | LV @ CLE | LV 17, CLE 20 | CLE 66% | LV +195 / CLE -195 | 16.9 – 21.9 | 6–27 / 10–34 | CLE -9.9 / CLE -4.5 | 37.5 / 40.5 | no edge | no edge | Under 40.5 (-104): EV +5.6%, 54%, stake 1.5u | Fernando Mendoza / Deshaun Watson | wind 18 mph |
| Mon 11/30 8:15 PM | CAR @ TB | CAR 20, TB 23 | TB 59% | CAR +145 / TB -145 | 20.2 – 23.3 | 10–31 / 13–35 | TB -3.5 / TB -3.0 | 44.1 / 43.5 | no edge | no edge | no edge | Bryce Young / Baker Mayfield |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 161 | 9.37 | 10.49 | 7.25 | 68.8% | 0.209 | 84.8% |
| Model only (before blending) | 161 | 9.50 | 10.93 | 7.39 | 70.0% | – | – |
| Betting line when predicted | 161 | 9.37 | 10.49 | 7.25 | 68.8% | – | – |

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

### Week 11 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| IND @ HOU | 17–27 | 3–26 | 83% | no |
| ARI @ KC | 13–27 | 7–34 | 90% | yes |
| BAL @ CAR | 20–23 | 33–35 | 59% | no |
| MIA @ BUF | 13–30 | 9–26 | 91% | yes |
| NO @ CHI | 20–30 | 13–21 | 82% | yes |
| TB @ DET | 20–23 | 21–31 | 65% | yes |
| TEN @ DAL | 24–30 | 30–51 | 71% | no |
| NYJ @ LAC | 20–23 | 27–24 | 42% | yes |
| JAX @ NYG | 27–20 | 18–23 | 32% | yes |
| LV @ DEN | 17–27 | 24–38 | 81% | yes |
| PIT @ PHI | 20–17 | 16–19 | 39% | yes |

## Power ratings

Points per game better than an average team on a neutral field, from opponent-adjusted EPA with this season's games weighted against a preseason prior. Defense is positive when it holds opponents below average.

| # | Team | Net | Offense | Defense | Special teams | Elo |
|---|---|---|---|---|---|---|
| 1 | BUF | +5.8 | +4.6 | +0.5 | +0.7 | 1709 |
| 2 | JAX | +4.6 | +2.4 | +1.5 | +0.7 | 1627 |
| 3 | SF | +4.6 | +5.1 | +0.1 | -0.7 | 1647 |
| 4 | DET | +4.5 | +3.4 | -0.2 | +1.3 | 1636 |
| 5 | CHI | +4.0 | +2.0 | +0.6 | +1.4 | 1636 |
| 6 | SEA | +4.0 | -0.0 | +3.1 | +0.9 | 1647 |
| 7 | LA | +3.9 | +3.1 | +2.2 | -1.4 | 1622 |
| 8 | KC | +2.8 | +3.3 | +1.0 | -1.4 | 1600 |
| 9 | CIN | +2.4 | +3.7 | -1.6 | +0.3 | 1615 |
| 10 | HOU | +2.1 | -0.1 | +1.5 | +0.7 | 1541 |
| 11 | MIN | +2.0 | -3.3 | +3.7 | +1.6 | 1625 |
| 12 | DEN | +2.0 | +0.3 | +1.6 | +0.1 | 1655 |
| 13 | GB | +1.6 | +2.1 | +0.5 | -1.0 | 1546 |
| 14 | NE | +1.5 | +1.4 | -0.0 | +0.1 | 1537 |
| 15 | BAL | +0.2 | +1.4 | -0.3 | -0.9 | 1446 |
| 16 | DAL | +0.2 | +3.5 | -3.3 | -0.0 | 1468 |
| 17 | TB | -0.1 | -1.6 | +1.1 | +0.4 | 1482 |
| 18 | NYG | -0.4 | -0.5 | +0.1 | -0.0 | 1494 |
| 19 | CAR | -1.2 | -0.0 | -0.9 | -0.2 | 1453 |
| 20 | PHI | -1.3 | -2.4 | +1.1 | +0.0 | 1416 |
| 21 | PIT | -1.3 | -1.3 | -0.1 | +0.0 | 1533 |
| 22 | WAS | -1.5 | -0.3 | -1.5 | +0.3 | 1447 |
| 23 | IND | -2.1 | -1.8 | -0.7 | +0.4 | 1382 |
| 24 | CLE | -2.9 | -3.8 | +0.9 | +0.1 | 1460 |
| 25 | NO | -3.4 | -2.3 | -0.2 | -0.8 | 1397 |
| 26 | NYJ | -3.4 | -1.5 | -2.4 | +0.5 | 1347 |
| 27 | ATL | -3.4 | -2.3 | -0.1 | -1.0 | 1421 |
| 28 | LAC | -4.2 | -4.2 | +0.4 | -0.4 | 1376 |
| 29 | MIA | -4.5 | -2.1 | -1.4 | -1.0 | 1354 |
| 30 | ARI | -5.1 | -2.3 | -2.0 | -0.9 | 1363 |
| 31 | LV | -5.5 | -3.6 | -2.0 | +0.1 | 1391 |
| 32 | TEN | -6.2 | -3.2 | -3.1 | +0.0 | 1287 |

## Current model fit

- Fitted on 1854 games from seasons 2020–2026.
- Home field: 1.5 points (1.9 in divisional games).
- QB adjustment: 0.86 points per point of QB value gap.
- Special teams: 0.46 points per point of net special-teams EPA.
- Weight on the betting line: 91% for the margin, 97% for the total.
- Wind: -0.20 total points per mph above 10 mph at open-air stadiums.
