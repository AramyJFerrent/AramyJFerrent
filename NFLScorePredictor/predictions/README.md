# NFL score predictions

Updated Sun Nov 15, 2026 02:23 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the final prediction, the model blended with the line: its expected points are run through the score simulator against the posted lines, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV, its chance of winning and its stake. Stakes are a 25% share of the Kelly stake, in units of 1% of the bankroll, with at most 3 units on one game. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers (the spread and total columns) often sit several points from the line, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. See the backtest for how they have done on past seasons; the live record is tracked below.

## 2026 Week 10

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 11/15 4:05 PM | LA @ ARI | LA 24, ARI 16 | LA 78% | LA -350 / ARI +350 | 23.9 – 14.7 | 13–37 / 6–25 | LA -6.4 / LA -9.5 | 46.0 / 38.5 | no edge | no edge | no edge | Matthew Stafford / Gardner Minshew |  |
| Sun 11/15 4:05 PM | SEA @ LV | SEA 24, LV 17 | SEA 71% | SEA -240 / LV +240 | 23.6 – 16.8 | 12–36 / 7–28 | SEA -8.9 / SEA -6.5 | 37.6 / 40.5 | no edge | no edge | no edge | Sam Darnold / Fernando Mendoza |  |
| Sun 11/15 4:25 PM | SF @ DAL | SF 30, DAL 27 | SF 64% | SF -175 / DAL +175 | 30.0 – 25.6 | 17–42 / 13–38 | SF -4.1 / SF -4.5 | 58.6 / 55.5 | no edge | no edge | no edge | Brock Purdy / Dak Prescott |  |
| Sun 11/15 8:20 PM | PIT @ CIN | PIT 24, CIN 27 | CIN 60% | PIT +155 / CIN -155 | 23.1 – 26.5 | 11–35 / 15–39 | CIN -2.9 / CIN -3.5 | 52.0 / 49.5 | no edge | no edge | no edge | Aaron Rodgers / Joe Burrow |  |
| Mon 11/16 8:15 PM | LAC @ BAL | LAC 17, BAL 20 | BAL 65% | LAC +190 / BAL -190 | 17.0 – 21.5 | 7–28 / 10–34 | BAL -5.1 / BAL -4.5 | 38.7 / 38.5 | no edge | no edge | no edge | Justin Herbert / Tyler Huntley |  |

## 2026 Week 11

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 11/19 8:15 PM | IND @ HOU | IND 20, HOU 27 | HOU 69% | IND +220 / HOU -220 | 19.1 – 25.2 | 8–30 / 13–38 | HOU -6.1 / – | 44.3 / – | no line yet | no line yet | no line yet | Daniel Jones / C.J. Stroud |  |
| Sun 11/22 1:00 PM | ARI @ KC | ARI 20, KC 27 | KC 77% | ARI +330 / KC -330 | 19.7 – 28.6 | 9–31 / 17–41 | KC -8.9 / – | 48.4 / – | no line yet | no line yet | no line yet | Gardner Minshew / Patrick Mahomes |  |
| Sun 11/22 1:00 PM | BAL @ CAR | BAL 20, CAR 23 | CAR 59% | BAL +140 / CAR -140 | 21.6 – 24.4 | 10–33 / 13–36 | CAR -2.8 / – | 46.0 / – | no line yet | no line yet | no line yet | Tyler Huntley / Bryce Young |  |
| Sun 11/22 1:00 PM | JAX @ NYG | JAX 23, NYG 20 | JAX 67% | JAX -200 / NYG +200 | 25.0 – 19.7 | 13–38 / 9–31 | JAX -5.4 / – | 44.7 / – | no line yet | no line yet | no line yet | Trevor Lawrence / J.J. McCarthy |  |
| Sun 11/22 1:00 PM | MIA @ BUF | MIA 17, BUF 31 | BUF 85% | MIA +580 / BUF -580 | 17.3 – 30.4 | 6–28 / 18–43 | BUF -13.1 / – | 49.6 / – | no line yet | no line yet | no line yet | Malik Willis / Josh Allen | wind 14 mph |
| Sun 11/22 1:00 PM | NO @ CHI | NO 17, CHI 31 | CHI 82% | NO +445 / CHI -445 | 18.0 – 29.2 | 7–30 / 17–42 | CHI -11.3 / – | 47.2 / – | no line yet | no line yet | no line yet | Tyler Shough / Caleb Williams |  |
| Sun 11/22 1:00 PM | TB @ DET | TB 20, DET 23 | DET 58% | TB +140 / DET -140 | 21.0 – 23.6 | 10–33 / 13–36 | DET -2.6 / – | 44.5 / – | no line yet | no line yet | no line yet | Baker Mayfield / Jared Goff |  |
| Sun 11/22 1:00 PM | TEN @ DAL | TEN 20, DAL 27 | DAL 73% | TEN +280 / DAL -280 | 21.3 – 29.2 | 10–33 / 17–42 | DAL -7.9 / – | 50.5 / – | no line yet | no line yet | no line yet | Cam Ward / Dak Prescott |  |
| Sun 11/22 4:05 PM | NYJ @ LAC | NYJ 20, LAC 17 | NYJ 53% | NYJ -115 / LAC +115 | 20.5 – 19.5 | 10–32 / 9–31 | NYJ -0.9 / – | 40.0 / – | no line yet | no line yet | no line yet | Geno Smith / Justin Herbert |  |
| Sun 11/22 4:25 PM | LV @ DEN | LV 13, DEN 27 | DEN 87% | LV +650 / DEN -650 | 13.3 – 26.7 | 3–23 / 14–39 | DEN -13.4 / – | 40.0 / – | no line yet | no line yet | no line yet | Fernando Mendoza / Bo Nix |  |
| Sun 11/22 4:25 PM | PIT @ PHI | PIT 20, PHI 17 | PIT 55% | PIT -120 / PHI +120 | 19.9 – 18.2 | 9–31 / 7–30 | PIT -1.7 / – | 38.1 / – | no line yet | no line yet | no line yet | Aaron Rodgers / Joe Milton III |  |
| Sun 11/22 8:20 PM | MIN @ SF | MIN 20, SF 23 | SF 54% | MIN +120 / SF -120 | 22.1 – 23.5 | 10–34 / 12–35 | SF -1.4 / – | 45.5 / – | no line yet | no line yet | no line yet | Kirk Cousins / Brock Purdy |  |
| Mon 11/23 8:15 PM | CIN @ WAS | CIN 27, WAS 24 | CIN 60% | CIN -150 / WAS +150 | 27.4 – 24.0 | 16–40 / 13–36 | CIN -2.5 / CIN -3.5 | 53.8 / 51.5 | no edge | no edge | no edge | Joe Burrow / Jayden Daniels |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 138 | 9.54 | 10.51 | 7.25 | 68.6% | 0.215 | 84.1% |
| Model only (before blending) | 138 | 9.67 | 11.00 | 7.42 | 67.2% | – | – |
| Betting line when predicted | 138 | 9.54 | 10.51 | 7.25 | 68.6% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin by about 10 points per game.

80 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines and actual starters, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

Every edge logged with the last prediction before kickoff, graded at the price and stake logged with it (live predictions only; backfilled games, and edges logged before edges were priced from the final prediction, are left out). Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised.

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread line moved toward the model's early spread edge before kickoff: 5 of 7 games (71%). Lines moving toward the edge (closing line value) is the quickest sign that the model knows something the market doesn't yet.

### Week 10 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| WAS @ NYG | 20–23 | 24–21 | 43% | yes |
| NE @ DET | 24–27 | 10–35 | 56% | no |

## Power ratings

Points per game better than an average team on a neutral field, from opponent-adjusted EPA with this season's games weighted against a preseason prior. Defense is positive when it holds opponents below average.

| # | Team | Net | Offense | Defense | Special teams | Elo |
|---|---|---|---|---|---|---|
| 1 | BUF | +5.8 | +4.8 | +0.1 | +0.9 | 1697 |
| 2 | JAX | +5.7 | +3.1 | +1.8 | +0.8 | 1645 |
| 3 | CHI | +4.7 | +2.6 | +0.6 | +1.5 | 1629 |
| 4 | SF | +4.1 | +4.7 | +0.4 | -1.0 | 1635 |
| 5 | SEA | +3.8 | -0.7 | +3.2 | +1.4 | 1636 |
| 6 | DET | +3.7 | +2.6 | -0.5 | +1.5 | 1625 |
| 7 | LA | +3.3 | +2.8 | +2.0 | -1.5 | 1604 |
| 8 | GB | +3.2 | +3.1 | +1.1 | -1.0 | 1581 |
| 9 | NE | +2.7 | +2.2 | +0.3 | +0.1 | 1537 |
| 10 | CIN | +2.2 | +3.7 | -1.9 | +0.5 | 1590 |
| 11 | KC | +2.1 | +3.0 | +0.4 | -1.3 | 1565 |
| 12 | DEN | +1.5 | +0.1 | +1.4 | +0.1 | 1647 |
| 13 | HOU | +1.5 | +0.0 | +1.2 | +0.3 | 1541 |
| 14 | MIN | +0.9 | -4.3 | +3.5 | +1.7 | 1590 |
| 15 | BAL | +0.4 | +1.4 | -0.1 | -0.9 | 1477 |
| 16 | DAL | +0.3 | +3.2 | -2.8 | -0.1 | 1467 |
| 17 | TB | +0.1 | -2.2 | +2.0 | +0.3 | 1494 |
| 18 | PIT | -0.5 | -0.5 | +0.2 | -0.2 | 1576 |
| 19 | NYG | -0.7 | -0.4 | +0.1 | -0.4 | 1467 |
| 20 | CAR | -1.1 | +0.4 | -1.4 | -0.1 | 1427 |
| 21 | WAS | -1.7 | -0.5 | -1.6 | +0.4 | 1447 |
| 22 | IND | -2.1 | -1.4 | -1.3 | +0.6 | 1389 |
| 23 | PHI | -2.4 | -3.0 | +0.5 | +0.1 | 1397 |
| 24 | NO | -3.3 | -1.5 | -0.8 | -1.0 | 1419 |
| 25 | CLE | -3.4 | -4.4 | +1.0 | +0.1 | 1444 |
| 26 | NYJ | -3.4 | -1.9 | -2.0 | +0.6 | 1335 |
| 27 | ATL | -3.4 | -1.8 | -0.0 | -1.6 | 1445 |
| 28 | MIA | -3.8 | -1.2 | -2.0 | -0.6 | 1367 |
| 29 | ARI | -4.5 | -1.9 | -1.5 | -1.1 | 1392 |
| 30 | LAC | -4.8 | -5.5 | +0.9 | -0.2 | 1374 |
| 31 | LV | -5.0 | -3.1 | -2.0 | +0.0 | 1409 |
| 32 | TEN | -6.0 | -3.4 | -2.6 | -0.1 | 1309 |

## Current model fit

- Fitted on 1831 games from seasons 2020–2026.
- Home field: 1.5 points (2.0 in divisional games).
- QB adjustment: 0.85 points per point of QB value gap.
- Special teams: 0.43 points per point of net special-teams EPA.
- Weight on the betting line: 90% for the margin, 97% for the total.
- Wind: -0.20 total points per mph above 10 mph at open-air stadiums.
