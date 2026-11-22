# NFL score predictions

Updated Sun Nov 22, 2026 04:44 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the final prediction, the model blended with the line: its expected points are run through the score simulator against the posted lines, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV, its chance of winning and its stake. Stakes are a 25% share of the Kelly stake, in units of 1% of the bankroll, with at most 3 units on one game. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers (the spread and total columns) often sit several points from the line, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. See the backtest for how they have done on past seasons; the live record is tracked below.

## 2026 Week 11

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 11/22 8:20 PM | MIN @ SF | MIN 20, SF 23 | SF 60% | MIN +150 / SF -150 | 21.6 – 24.9 | 10–34 / 13–37 | SF -0.9 / SF -3.5 | 47.4 / 46.5 | no edge | no edge | no edge | Kirk Cousins / Brock Purdy |  |
| Mon 11/23 8:15 PM | CIN @ WAS | CIN 30, WAS 23 | CIN 66% | CIN -200 / WAS +200 | 29.7 – 24.1 | 17–42 / 13–36 | CIN -1.2 / CIN -6.0 | 53.6 / 54.5 | no edge | no edge | no edge | Joe Burrow / Jayden Daniels | wind 14 mph |

## 2026 Week 12

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wed 11/25 8:00 PM | GB @ LA | GB 20, LA 23 | LA 60% | GB +150 / LA -150 | 21.3 – 24.3 | 10–33 / 13–37 | LA -3.5 / LA -3.0 | 48.5 / 45.5 | no edge | no edge | no edge | Jordan Love / Matthew Stafford |  |
| Thu 11/26 1:00 PM | CHI @ DET | CHI 30, DET 27 | CHI 56% | CHI -130 / DET +130 | 28.2 – 26.1 | 16–41 / 14–38 | DET -1.9 / CHI -2.5 | 50.4 / 54.5 | no edge | no edge | no edge | Caleb Williams / Jared Goff |  |
| Thu 11/26 4:30 PM | PHI @ DAL | PHI 20, DAL 27 | DAL 74% | PHI +290 / DAL -290 | 20.0 – 28.4 | 9–31 / 16–41 | DAL -6.3 / DAL -8.5 | 45.6 / 48.5 | no edge | no edge | no edge | Joe Milton III / Dak Prescott |  |
| Thu 11/26 8:20 PM | KC @ BUF | KC 24, BUF 27 | BUF 60% | KC +155 / BUF -155 | 22.8 – 25.9 | 10–34 / 14–38 | BUF -4.2 / BUF -3.0 | 52.8 / 50.5 | no edge | no edge | Under 50.5 (-104): EV +4.9%, 53%, stake 1.3u | Patrick Mahomes / Josh Allen | wind 19 mph |
| Fri 11/27 3:00 PM | DEN @ PIT | DEN 23, PIT 20 | DEN 52% | DEN -110 / PIT +110 | 21.5 – 20.6 | 10–33 / 10–33 | DEN -0.8 / – | 43.9 / – | no line yet | no line yet | no line yet | Bo Nix / Aaron Rodgers | wind 14 mph |
| Sun 11/29 1:00 PM | ATL @ MIN | ATL 16, MIN 23 | MIN 76% | ATL +320 / MIN -320 | 14.8 – 23.4 | 6–25 / 12–35 | MIN -8.6 / – | 38.2 / – | no line yet | no line yet | no line yet | Michael Penix Jr. / Kirk Cousins |  |
| Sun 11/29 1:00 PM | BAL @ HOU | BAL 20, HOU 23 | HOU 68% | BAL +215 / HOU -215 | 19.1 – 25.1 | 9–31 / 13–37 | HOU -6.0 / – | 44.2 / – | no line yet | no line yet | no line yet | Jacoby Brissett / C.J. Stroud |  |
| Sun 11/29 1:00 PM | NO @ CIN | NO 20, CIN 27 | CIN 73% | NO +265 / CIN -265 | 21.4 – 29.2 | 10–34 / 17–42 | CIN -7.8 / – | 50.6 / – | no line yet | no line yet | no line yet | Tyler Shough / Joe Burrow |  |
| Sun 11/29 1:00 PM | NYG @ IND | NYG 20, IND 23 | IND 52% | NYG +105 / IND -105 | 20.2 – 20.7 | 10–31 / 10–32 | IND -0.5 / – | 40.9 / – | no line yet | no line yet | no line yet | J.J. McCarthy / Anthony Richardson |  |
| Sun 11/29 1:00 PM | NYJ @ MIA | NYJ 23, MIA 20 | NYJ 57% | NYJ -130 / MIA +130 | 21.4 – 19.4 | 10–33 / 9–31 | NYJ -2.0 / – | 43.4 / – | no line yet | no line yet | no line yet | Geno Smith / Kyle McCord | wind 15 mph |
| Sun 11/29 1:00 PM | TEN @ JAX | TEN 17, JAX 31 | JAX 85% | TEN +555 / JAX -555 | 16.5 – 29.5 | 6–27 / 17–42 | JAX -13.0 / – | 46.0 / – | no line yet | no line yet | no line yet | Cam Ward / Trevor Lawrence |  |
| Sun 11/29 4:05 PM | NE @ LAC | NE 23, LAC 17 | NE 67% | NE -210 / LAC +210 | 23.8 – 18.1 | 13–36 / 7–30 | NE -5.7 / – | 41.9 / – | no line yet | no line yet | no line yet | Drake Maye / Justin Herbert |  |
| Sun 11/29 4:25 PM | SEA @ SF | SEA 24, SF 27 | SF 55% | SEA +125 / SF -125 | 23.4 – 25.1 | 13–35 / 13–37 | SF -1.7 / – | 48.6 / – | no line yet | no line yet | no line yet | Sam Darnold / Brock Purdy |  |
| Sun 11/29 4:25 PM | WAS @ ARI | WAS 23, ARI 20 | WAS 57% | WAS -130 / ARI +130 | 24.3 – 22.2 | 13–37 / 10–34 | WAS -2.1 / – | 46.5 / – | no line yet | no line yet | no line yet | Jayden Daniels / Gardner Minshew |  |
| Sun 11/29 8:20 PM | LV @ CLE | LV 13, CLE 23 | CLE 79% | LV +385 / CLE -385 | 12.8 – 22.4 | 3–23 / 10–34 | CLE -9.6 / – | 37.6 / – | no line yet | no line yet | no line yet | Fernando Mendoza / Deshaun Watson | wind 14 mph |
| Mon 11/30 8:15 PM | CAR @ TB | CAR 20, TB 23 | TB 62% | CAR +165 / TB -165 | 18.6 – 22.5 | 7–30 / 10–34 | TB -3.9 / – | 43.2 / – | no line yet | no line yet | no line yet | Bryce Young / Baker Mayfield | wind 14 mph |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 158 | 9.42 | 10.48 | 7.26 | 69.4% | 0.208 | 84.5% |
| Model only (before blending) | 158 | 9.60 | 10.93 | 7.41 | 70.1% | – | – |
| Betting line when predicted | 158 | 9.41 | 10.47 | 7.26 | 69.4% | – | – |

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
| PIT @ PHI | 20–17 | 16–19 | 39% | yes |

## Power ratings

Points per game better than an average team on a neutral field, from opponent-adjusted EPA with this season's games weighted against a preseason prior. Defense is positive when it holds opponents below average.

| # | Team | Net | Offense | Defense | Special teams | Elo |
|---|---|---|---|---|---|---|
| 1 | BUF | +5.4 | +4.7 | +0.1 | +0.6 | 1709 |
| 2 | JAX | +5.3 | +2.9 | +1.5 | +0.9 | 1654 |
| 3 | SF | +4.6 | +5.2 | +0.1 | -0.7 | 1647 |
| 4 | DET | +4.3 | +2.9 | -0.0 | +1.4 | 1636 |
| 5 | SEA | +4.0 | +0.0 | +3.1 | +0.9 | 1647 |
| 6 | CHI | +3.9 | +2.3 | +0.3 | +1.4 | 1636 |
| 7 | LA | +3.9 | +3.1 | +2.2 | -1.4 | 1622 |
| 8 | CIN | +2.5 | +3.8 | -1.5 | +0.3 | 1615 |
| 9 | HOU | +2.2 | -0.0 | +1.5 | +0.7 | 1541 |
| 10 | KC | +2.2 | +2.8 | +0.9 | -1.5 | 1600 |
| 11 | MIN | +2.0 | -3.3 | +3.7 | +1.6 | 1625 |
| 12 | DEN | +1.6 | +0.2 | +1.4 | +0.0 | 1647 |
| 13 | GB | +1.6 | +2.2 | +0.4 | -1.0 | 1546 |
| 14 | NE | +1.5 | +1.4 | -0.0 | +0.1 | 1537 |
| 15 | BAL | +0.4 | +1.4 | -0.2 | -0.8 | 1446 |
| 16 | TB | -0.0 | -1.8 | +1.5 | +0.3 | 1482 |
| 17 | DAL | -0.4 | +2.9 | -3.4 | +0.1 | 1468 |
| 18 | PIT | -0.8 | -0.6 | -0.2 | +0.1 | 1533 |
| 19 | NYG | -0.9 | -0.4 | -0.2 | -0.2 | 1467 |
| 20 | CAR | -1.4 | -0.2 | -0.9 | -0.4 | 1453 |
| 21 | WAS | -1.5 | -0.3 | -1.5 | +0.3 | 1447 |
| 22 | PHI | -1.5 | -2.2 | +0.7 | -0.0 | 1416 |
| 23 | IND | -2.1 | -1.8 | -0.7 | +0.4 | 1382 |
| 24 | CLE | -2.8 | -3.8 | +0.9 | +0.1 | 1460 |
| 25 | NO | -3.1 | -2.0 | -0.3 | -0.8 | 1397 |
| 26 | ATL | -3.4 | -2.3 | -0.1 | -1.0 | 1421 |
| 27 | LAC | -3.9 | -4.5 | +1.0 | -0.4 | 1395 |
| 28 | NYJ | -3.9 | -2.2 | -2.3 | +0.5 | 1328 |
| 29 | MIA | -4.0 | -1.6 | -1.4 | -0.9 | 1354 |
| 30 | ARI | -4.7 | -2.2 | -1.6 | -0.9 | 1363 |
| 31 | LV | -5.1 | -3.4 | -2.0 | +0.2 | 1399 |
| 32 | TEN | -5.8 | -3.2 | -2.6 | -0.1 | 1287 |

## Current model fit

- Fitted on 1851 games from seasons 2020–2026.
- Home field: 1.5 points (1.9 in divisional games).
- QB adjustment: 0.86 points per point of QB value gap.
- Special teams: 0.46 points per point of net special-teams EPA.
- Weight on the betting line: 92% for the margin, 97% for the total.
- Wind: -0.20 total points per mph above 10 mph at open-air stadiums.
