# NFL score predictions

Updated Sun Nov 08, 2026 01:21 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the final prediction, the model blended with the line: its expected points are run through the score simulator against the posted lines, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV, its chance of winning and its stake. Stakes are a 25% share of the Kelly stake, in units of 1% of the bankroll, with at most 3 units on one game. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers (the spread and total columns) often sit several points from the line, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. See the backtest for how they have done on past seasons; the live record is tracked below.

## 2026 Week 9

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 11/08 4:05 PM | HOU @ LAC | HOU 20, LAC 17 | HOU 66% | HOU -200 / LAC +200 | 23.0 – 17.4 | 12–35 / 7–28 | HOU -6.1 / HOU -5.5 | 38.0 / 40.5 | no edge | no edge | no edge | C.J. Stroud / Justin Herbert |  |
| Sun 11/08 4:05 PM | LV @ SF | LV 20, SF 30 | SF 77% | LV +335 / SF -335 | 20.9 – 30.6 | 10–33 / 18–44 | SF -10.7 / SF -9.5 | 50.9 / 51.5 | no edge | no edge | no edge | Kirk Cousins / Brock Purdy |  |
| Sun 11/08 4:25 PM | ARI @ SEA | ARI 17, SEA 23 | SEA 75% | ARI +300 / SEA -300 | 15.6 – 23.9 | 6–27 / 13–37 | SEA -5.9 / SEA -8.5 | 39.4 / 39.5 | no edge | no edge | no edge | Gardner Minshew / Drew Lock |  |
| Sun 11/08 4:25 PM | GB @ NE | GB 20, NE 23 | NE 60% | GB +150 / NE -150 | 20.8 – 23.8 | 10–33 / 13–36 | NE -3.7 / NE -3.0 | 49.2 / 44.5 | no edge | no edge | no edge | Jordan Love / Drake Maye |  |
| Sun 11/08 8:20 PM | TB @ CHI | TB 20, CHI 27 | CHI 68% | TB +215 / CHI -215 | 20.8 – 26.7 | 10–33 / 14–39 | CHI -5.1 / CHI -6.0 | 45.8 / 47.5 | no edge | no edge | no edge | Baker Mayfield / Caleb Williams |  |
| Mon 11/09 8:15 PM | BUF @ MIN | BUF 23, MIN 20 | BUF 59% | BUF -145 / MIN +145 | 23.2 – 20.4 | 12–35 / 10–31 | BUF -1.0 / BUF -3.0 | 45.3 / 43.5 | no edge | no edge | no edge | Josh Allen / Kyler Murray |  |

## 2026 Week 10

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 11/12 8:15 PM | WAS @ NYG | WAS 23, NYG 20 | WAS 51% | WAS -105 / NYG +105 | 22.5 – 22.4 | 10–34 / 10–34 | WAS -0.1 / – | 44.9 / – | no line yet | no line yet | no line yet | Jayden Daniels / J.J. McCarthy |  |
| Sun 11/15 9:30 AM | NE @ DET | NE 27, DET 24 | DET 50% | NE +100 / DET -100 | 25.1 – 25.1 | 13–37 / 13–37 | PK / – | 50.3 / – | no line yet | no line yet | no line yet | Drake Maye / Jared Goff |  |
| Sun 11/15 1:00 PM | BUF @ NYJ | BUF 27, NYJ 24 | BUF 67% | BUF -205 / NYJ +205 | 27.7 – 22.1 | 16–41 / 10–34 | BUF -5.6 / – | 52.7 / – | no line yet | no line yet | no line yet | Josh Allen / Geno Smith | wind 16 mph |
| Sun 11/15 1:00 PM | CAR @ NO | CAR 20, NO 23 | CAR 50% | CAR -100 / NO +100 | 23.0 – 23.3 | 13–35 / 12–35 | NO -0.3 / – | 46.2 / – | no line yet | no line yet | no line yet | Bryce Young / Tyler Shough |  |
| Sun 11/15 1:00 PM | HOU @ CLE | HOU 20, CLE 17 | HOU 55% | HOU -125 / CLE +125 | 19.2 – 17.4 | 9–30 / 7–28 | HOU -1.8 / – | 40.0 / – | no line yet | no line yet | no line yet | C.J. Stroud / Deshaun Watson | wind 17 mph |
| Sun 11/15 1:00 PM | JAX @ TEN | JAX 27, TEN 17 | JAX 76% | JAX -315 / TEN +315 | 27.2 – 18.3 | 14–40 / 7–30 | JAX -8.9 / – | 45.5 / – | no line yet | no line yet | no line yet | Trevor Lawrence / Cam Ward |  |
| Sun 11/15 1:00 PM | KC @ ATL | KC 23, ATL 20 | KC 66% | KC -190 / ATL +190 | 25.0 – 19.9 | 13–37 / 9–31 | KC -5.1 / – | 44.8 / – | no line yet | no line yet | no line yet | Patrick Mahomes / Michael Penix Jr. |  |
| Sun 11/15 1:00 PM | MIA @ IND | MIA 20, IND 23 | IND 65% | MIA +185 / IND -185 | 20.4 – 24.9 | 9–32 / 13–37 | IND -4.5 / – | 45.3 / – | no line yet | no line yet | no line yet | Malik Willis / Daniel Jones |  |
| Sun 11/15 1:00 PM | MIN @ GB | MIN 20, GB 23 | GB 55% | MIN +120 / GB -120 | 20.0 – 21.7 | 10–31 / 10–34 | GB -1.7 / – | 41.9 / – | no line yet | no line yet | no line yet | Kyler Murray / Jordan Love |  |
| Sun 11/15 4:05 PM | LA @ ARI | LA 27, ARI 20 | LA 67% | LA -200 / ARI +200 | 25.7 – 20.1 | 14–38 / 9–32 | LA -5.6 / – | 45.8 / – | no line yet | no line yet | no line yet | Matthew Stafford / Gardner Minshew |  |
| Sun 11/15 4:05 PM | SEA @ LV | SEA 23, LV 20 | SEA 67% | SEA -205 / LV +205 | 23.4 – 18.0 | 12–36 / 7–30 | SEA -5.4 / – | 41.5 / – | no line yet | no line yet | no line yet | Sam Darnold / Kirk Cousins |  |
| Sun 11/15 4:25 PM | SF @ DAL | SF 30, DAL 27 | SF 59% | SF -140 / DAL +140 | 29.9 – 26.8 | 17–42 / 15–40 | SF -3.1 / – | 56.7 / – | no line yet | no line yet | no line yet | Brock Purdy / Dak Prescott |  |
| Sun 11/15 8:20 PM | PIT @ CIN | PIT 24, CIN 27 | CIN 60% | PIT +150 / CIN -150 | 23.4 – 26.8 | 12–35 / 15–39 | CIN -3.4 / – | 50.2 / – | no line yet | no line yet | no line yet | Aaron Rodgers / Joe Burrow |  |
| Mon 11/16 8:15 PM | LAC @ BAL | LAC 17, BAL 20 | BAL 63% | LAC +175 / BAL -175 | 16.7 – 20.7 | 6–27 / 10–33 | BAL -4.1 / – | 37.4 / – | no line yet | no line yet | no line yet | Justin Herbert / Tyler Huntley |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 123 | 9.64 | 10.52 | 7.34 | 66.4% | 0.222 | 84.1% |
| Model only (before blending) | 123 | 9.63 | 11.00 | 7.47 | 64.8% | – | – |
| Betting line when predicted | 123 | 9.65 | 10.52 | 7.33 | 66.4% | – | – |

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

### Week 9 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| JAX @ BAL | 24–17 | 33–10 | 79% | yes |
| CIN @ ATL | 27–24 | 34–17 | 62% | yes |

## Power ratings

Points per game better than an average team on a neutral field, from opponent-adjusted EPA with this season's games weighted against a preseason prior. Defense is positive when it holds opponents below average.

| # | Team | Net | Offense | Defense | Special teams | Elo |
|---|---|---|---|---|---|---|
| 1 | JAX | +5.7 | +3.1 | +1.9 | +0.8 | 1645 |
| 2 | BUF | +5.6 | +5.2 | -0.7 | +1.1 | 1669 |
| 3 | CHI | +4.5 | +2.8 | +0.2 | +1.4 | 1622 |
| 4 | SEA | +3.6 | -1.0 | +3.1 | +1.5 | 1628 |
| 5 | DET | +3.6 | +2.7 | -0.7 | +1.5 | 1582 |
| 6 | SF | +3.5 | +4.3 | +0.0 | -0.8 | 1624 |
| 7 | NE | +3.5 | +2.5 | +0.9 | +0.1 | 1607 |
| 8 | LA | +3.1 | +2.8 | +1.9 | -1.6 | 1590 |
| 9 | GB | +2.3 | +2.4 | +0.9 | -0.9 | 1539 |
| 10 | KC | +1.9 | +2.8 | +0.1 | -1.0 | 1554 |
| 11 | MIN | +1.7 | -3.1 | +3.4 | +1.5 | 1619 |
| 12 | DEN | +1.5 | -0.0 | +1.7 | -0.1 | 1637 |
| 13 | CIN | +1.4 | +2.7 | -1.5 | +0.3 | 1590 |
| 14 | HOU | +0.8 | -0.7 | +1.1 | +0.4 | 1517 |
| 15 | TB | +0.6 | -1.7 | +1.9 | +0.4 | 1501 |
| 16 | BAL | +0.3 | +1.3 | -0.1 | -0.9 | 1477 |
| 17 | DAL | -0.1 | +2.8 | -3.2 | +0.3 | 1451 |
| 18 | PIT | -0.5 | -0.5 | +0.2 | -0.2 | 1576 |
| 19 | CAR | -1.2 | +0.0 | -1.3 | +0.1 | 1437 |
| 20 | NYG | -1.4 | -0.8 | -0.4 | -0.1 | 1464 |
| 21 | WAS | -1.5 | -0.4 | -1.4 | +0.3 | 1443 |
| 22 | PHI | -1.7 | -2.4 | +0.5 | +0.2 | 1420 |
| 23 | IND | -1.7 | -0.9 | -1.1 | +0.3 | 1405 |
| 24 | NYJ | -3.0 | -1.4 | -1.8 | +0.2 | 1346 |
| 25 | ATL | -3.2 | -2.5 | +0.7 | -1.3 | 1445 |
| 26 | NO | -3.3 | -1.7 | -0.9 | -0.7 | 1413 |
| 27 | CLE | -3.3 | -4.1 | +1.1 | -0.2 | 1450 |
| 28 | MIA | -3.6 | -0.9 | -2.1 | -0.6 | 1380 |
| 29 | LAC | -4.3 | -5.4 | +1.4 | -0.3 | 1398 |
| 30 | ARI | -4.4 | -1.8 | -1.4 | -1.2 | 1400 |
| 31 | LV | -4.4 | -2.6 | -1.7 | -0.2 | 1420 |
| 32 | TEN | -6.1 | -3.5 | -2.6 | -0.1 | 1309 |

## Current model fit

- Fitted on 1816 games from seasons 2020–2026.
- Home field: 1.5 points (2.0 in divisional games).
- QB adjustment: 0.84 points per point of QB value gap.
- Special teams: 0.45 points per point of net special-teams EPA.
- Weight on the betting line: 89% for the margin, 97% for the total.
- Wind: -0.20 total points per mph above 10 mph at open-air stadiums.
