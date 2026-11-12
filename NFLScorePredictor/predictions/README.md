# NFL score predictions

Updated Thu Nov 12, 2026 03:49 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the final prediction, the model blended with the line: its expected points are run through the score simulator against the posted lines, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV, its chance of winning and its stake. Stakes are a 25% share of the Kelly stake, in units of 1% of the bankroll, with at most 3 units on one game. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers (the spread and total columns) often sit several points from the line, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. See the backtest for how they have done on past seasons; the live record is tracked below.

## 2026 Week 10

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 11/12 8:15 PM | WAS @ NYG | WAS 20, NYG 23 | NYG 57% | WAS +135 / NYG -135 | 19.1 – 21.5 | 9–30 / 10–33 | NYG -1.2 / NYG -2.5 | 43.8 / 40.5 | no edge | no edge | no edge | Jayden Daniels / J.J. McCarthy |  |
| Sun 11/15 9:30 AM | NE @ DET | NE 24, DET 27 | DET 57% | NE +135 / DET -135 | 24.5 – 26.9 | 13–37 / 16–39 | DET -1.4 / DET -2.5 | 49.8 / 51.5 | no edge | no edge | no edge | Drake Maye / Jared Goff |  |
| Sun 11/15 1:00 PM | BUF @ NYJ | BUF 27, NYJ 20 | BUF 75% | BUF -300 / NYJ +300 | 29.1 – 20.8 | 17–41 / 10–33 | BUF -6.3 / BUF -8.5 | 51.1 / 50.5 | no edge | no edge | no edge | Josh Allen / Geno Smith | wind 13 mph |
| Sun 11/15 1:00 PM | CAR @ NO | CAR 24, NO 27 | NO 57% | CAR +135 / NO -135 | 23.1 – 25.4 | 12–35 / 14–38 | NO -0.1 / NO -2.5 | 46.8 / 48.5 | no edge | no edge | no edge | Bryce Young / Tyler Shough |  |
| Sun 11/15 1:00 PM | HOU @ CLE | HOU 20, CLE 17 | HOU 64% | HOU -175 / CLE +175 | 22.3 – 18.0 | 10–34 / 7–30 | HOU -2.6 / HOU -4.5 | 40.5 / 40.5 | no edge | no edge | no edge | C.J. Stroud / Deshaun Watson |  |
| Sun 11/15 1:00 PM | JAX @ TEN | JAX 27, TEN 17 | JAX 79% | JAX -385 / TEN +385 | 28.4 – 18.1 | 16–41 / 7–30 | JAX -8.8 / JAX -10.5 | 45.6 / 46.5 | no edge | no edge | no edge | Trevor Lawrence / Cam Ward |  |
| Sun 11/15 1:00 PM | KC @ ATL | KC 23, ATL 20 | KC 59% | KC -145 / ATL +145 | 24.9 – 21.6 | 13–37 / 10–34 | KC -5.5 / KC -3.0 | 46.4 / 46.5 | no edge | no edge | no edge | Patrick Mahomes / Michael Penix Jr. |  |
| Sun 11/15 1:00 PM | MIA @ IND | MIA 17, IND 20 | IND 62% | MIA +165 / IND -165 | 17.5 – 21.1 | 7–28 / 10–33 | IND -4.4 / IND -3.5 | 44.6 / 38.5 | no edge | no edge | no edge | Malik Willis / Daniel Jones |  |
| Sun 11/15 1:00 PM | MIN @ GB | MIN 17, GB 20 | GB 58% | MIN +140 / GB -140 | 19.3 – 22.2 | 9–31 / 10–34 | GB -1.9 / GB -3.0 | 42.5 / 41.5 | no edge | no edge | no edge | Kirk Cousins / Jordan Love |  |
| Sun 11/15 4:05 PM | LA @ ARI | LA 24, ARI 16 | LA 77% | LA -345 / ARI +345 | 24.4 – 15.3 | 13–37 / 6–26 | LA -6.0 / LA -9.5 | 45.8 / 39.5 | no edge | no edge | no edge | Matthew Stafford / Gardner Minshew |  |
| Sun 11/15 4:05 PM | SEA @ LV | SEA 24, LV 17 | SEA 71% | SEA -245 / LV +245 | 23.7 – 16.8 | 13–36 / 6–28 | SEA -10.5 / SEA -6.5 | 37.3 / 40.5 | no edge | no edge | no edge | Sam Darnold / Fernando Mendoza |  |
| Sun 11/15 4:25 PM | SF @ DAL | SF 30, DAL 27 | SF 60% | SF -150 / DAL +150 | 29.5 – 26.0 | 17–42 / 14–38 | SF -3.3 / SF -3.5 | 56.8 / 55.5 | no edge | no edge | no edge | Brock Purdy / Dak Prescott |  |
| Sun 11/15 8:20 PM | PIT @ CIN | PIT 24, CIN 27 | CIN 62% | PIT +165 / CIN -165 | 23.0 – 26.6 | 12–35 / 15–39 | CIN -4.1 / CIN -3.5 | 51.6 / 49.5 | no edge | no edge | no edge | Aaron Rodgers / Joe Burrow |  |
| Mon 11/16 8:15 PM | LAC @ BAL | LAC 17, BAL 20 | BAL 64% | LAC +180 / BAL -180 | 17.0 – 21.5 | 6–28 / 10–34 | BAL -4.7 / BAL -4.5 | 37.9 / 38.5 | no edge | no edge | no edge | Justin Herbert / Tyler Huntley |  |

## 2026 Week 11

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 11/19 8:15 PM | IND @ HOU | IND 17, HOU 27 | HOU 78% | IND +365 / HOU -365 | 17.4 – 27.1 | 7–28 / 15–40 | HOU -6.2 / HOU -10.0 | 44.3 / 44.5 | no edge | no edge | no edge | Daniel Jones / C.J. Stroud |  |
| Sun 11/22 1:00 PM | ARI @ KC | ARI 13, KC 27 | KC 87% | ARI +655 / KC -655 | 14.4 – 27.9 | 6–24 / 16–41 | KC -9.0 / KC -14.0 | 48.4 / 42.5 | no edge | no edge | no edge | Gardner Minshew / Patrick Mahomes | wind 12 mph |
| Sun 11/22 1:00 PM | BAL @ CAR | BAL 20, CAR 23 | CAR 55% | BAL +120 / CAR -120 | 21.5 – 23.1 | 10–34 / 12–35 | CAR -2.9 / CAR -1.5 | 46.1 / 44.5 | no edge | no edge | no edge | Tyler Huntley / Bryce Young |  |
| Sun 11/22 1:00 PM | JAX @ NYG | JAX 27, NYG 20 | JAX 68% | JAX -215 / NYG +215 | 25.2 – 19.2 | 13–38 / 9–31 | JAX -5.8 / JAX -6.0 | 43.9 / 44.5 | no edge | no edge | no edge | Trevor Lawrence / J.J. McCarthy |  |
| Sun 11/22 1:00 PM | MIA @ BUF | MIA 13, BUF 30 | BUF 91% | MIA +1005 / BUF -1005 | 14.7 – 30.9 | 6–25 / 19–44 | BUF -13.1 / BUF -16.5 | 49.6 / 46.5 | no edge | no edge | no edge | Malik Willis / Josh Allen | wind 15 mph |
| Sun 11/22 1:00 PM | NO @ CHI | NO 20, CHI 30 | CHI 78% | NO +350 / CHI -350 | 19.4 – 29.1 | 9–31 / 17–42 | CHI -11.3 / CHI -9.5 | 47.3 / 48.5 | no edge | no edge | no edge | Tyler Shough / Caleb Williams |  |
| Sun 11/22 1:00 PM | TB @ DET | TB 23, DET 26 | DET 61% | TB +160 / DET -160 | 22.0 – 25.4 | 10–34 / 13–38 | DET -2.6 / DET -3.5 | 44.5 / 47.5 | no edge | no edge | no edge | Baker Mayfield / Jared Goff |  |
| Sun 11/22 1:00 PM | TEN @ DAL | TEN 24, DAL 30 | DAL 72% | TEN +255 / DAL -255 | 22.0 – 29.5 | 10–34 / 17–42 | DAL -7.9 / DAL -7.5 | 50.6 / 51.5 | no edge | no edge | no edge | Cam Ward / Dak Prescott |  |
| Sun 11/22 4:05 PM | NYJ @ LAC | NYJ 20, LAC 23 | LAC 54% | NYJ +120 / LAC -120 | 20.6 – 21.8 | 10–32 / 10–34 | NYJ -1.0 / LAC -1.5 | 40.0 / 42.5 | no edge | no edge | no edge | Geno Smith / Justin Herbert |  |
| Sun 11/22 4:25 PM | LV @ DEN | LV 17, DEN 24 | DEN 77% | LV +330 / DEN -330 | 16.2 – 25.2 | 6–27 / 13–38 | DEN -13.4 / DEN -8.5 | 40.0 / 41.5 | no edge | no edge | no edge | Fernando Mendoza / Bo Nix |  |
| Sun 11/22 4:25 PM | PIT @ PHI | PIT 20, PHI 17 | PIT 63% | PIT -170 / PHI +170 | 21.4 – 17.1 | 10–33 / 7–28 | PIT -1.8 / PIT -4.5 | 38.1 / 38.5 | no edge | no edge | no edge | Aaron Rodgers / Joe Milton III |  |
| Sun 11/22 8:20 PM | MIN @ SF | MIN 20, SF 23 | SF 60% | MIN +150 / SF -150 | 21.6 – 24.9 | 10–34 / 13–37 | SF -1.3 / SF -3.5 | 45.6 / 46.5 | no edge | no edge | no edge | Kirk Cousins / Brock Purdy |  |
| Mon 11/23 8:15 PM | CIN @ WAS | CIN 27, WAS 24 | CIN 61% | CIN -155 / WAS +155 | 27.5 – 24.1 | 16–40 / 13–37 | CIN -2.6 / CIN -3.5 | 53.6 / 51.5 | no edge | no edge | no edge | Joe Burrow / Jayden Daniels |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 136 | 9.47 | 10.60 | 7.26 | 68.9% | 0.214 | 84.2% |
| Model only (before blending) | 136 | 9.60 | 11.12 | 7.42 | 67.4% | – | – |
| Betting line when predicted | 136 | 9.47 | 10.60 | 7.25 | 68.9% | – | – |

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
| CLE @ NO | 20–23 | 22–23 | 62% | yes |
| DAL @ IND | 27–24 | 27–23 | 62% | yes |
| DEN @ CAR | 23–20 | 26–21 | 59% | yes |
| DET @ MIA | 27–20 | 19–9 | 68% | no |
| LA @ WAS | 27–24 | 20–13 | 63% | yes |
| NYG @ PHI | 20–17 | 19–11 | 60% | yes |
| NYJ @ KC | 20–27 | 12–35 | 76% | yes |
| HOU @ LAC | 23–17 | 44–22 | 67% | no |
| LV @ SF | 20–30 | 17–38 | 75% | yes |
| ARI @ SEA | 17–24 | 3–17 | 75% | no |
| GB @ NE | 20–23 | 45–27 | 40% | no |
| TB @ CHI | 20–27 | 24–27 | 68% | yes |
| BUF @ MIN | 23–20 | 23–6 | 61% | no |

## Power ratings

Points per game better than an average team on a neutral field, from opponent-adjusted EPA with this season's games weighted against a preseason prior. Defense is positive when it holds opponents below average.

| # | Team | Net | Offense | Defense | Special teams | Elo |
|---|---|---|---|---|---|---|
| 1 | BUF | +5.9 | +4.9 | +0.1 | +0.9 | 1697 |
| 2 | JAX | +5.7 | +3.1 | +1.8 | +0.8 | 1645 |
| 3 | CHI | +4.7 | +2.7 | +0.6 | +1.4 | 1629 |
| 4 | SF | +4.2 | +4.8 | +0.4 | -1.0 | 1635 |
| 5 | SEA | +3.8 | -0.7 | +3.2 | +1.3 | 1636 |
| 6 | DET | +3.7 | +2.7 | -0.5 | +1.5 | 1595 |
| 7 | LA | +3.3 | +2.8 | +2.0 | -1.5 | 1604 |
| 8 | GB | +3.2 | +3.1 | +1.1 | -1.0 | 1581 |
| 9 | NE | +2.7 | +2.3 | +0.3 | +0.1 | 1566 |
| 10 | CIN | +2.3 | +3.7 | -1.9 | +0.5 | 1590 |
| 11 | KC | +2.1 | +3.1 | +0.3 | -1.3 | 1565 |
| 12 | DEN | +1.6 | +0.1 | +1.4 | +0.1 | 1647 |
| 13 | HOU | +1.5 | +0.0 | +1.2 | +0.3 | 1541 |
| 14 | MIN | +0.9 | -4.3 | +3.6 | +1.7 | 1590 |
| 15 | BAL | +0.4 | +1.4 | -0.1 | -0.9 | 1477 |
| 16 | DAL | +0.3 | +3.2 | -2.9 | -0.1 | 1467 |
| 17 | TB | +0.2 | -2.2 | +2.0 | +0.3 | 1494 |
| 18 | PIT | -0.5 | -0.5 | +0.2 | -0.2 | 1576 |
| 19 | NYG | -0.7 | -0.8 | +0.1 | -0.1 | 1486 |
| 20 | CAR | -1.0 | +0.5 | -1.4 | -0.1 | 1427 |
| 21 | WAS | -1.8 | -0.5 | -1.4 | +0.1 | 1428 |
| 22 | IND | -2.1 | -1.4 | -1.3 | +0.6 | 1389 |
| 23 | PHI | -2.4 | -3.0 | +0.5 | +0.1 | 1397 |
| 24 | NO | -3.3 | -1.5 | -0.8 | -0.9 | 1419 |
| 25 | CLE | -3.3 | -4.4 | +0.9 | +0.1 | 1444 |
| 26 | NYJ | -3.4 | -1.9 | -2.1 | +0.6 | 1335 |
| 27 | ATL | -3.4 | -1.8 | -0.0 | -1.6 | 1445 |
| 28 | MIA | -3.9 | -1.2 | -2.0 | -0.6 | 1367 |
| 29 | ARI | -4.6 | -1.9 | -1.6 | -1.1 | 1392 |
| 30 | LAC | -4.9 | -5.6 | +0.9 | -0.2 | 1374 |
| 31 | LV | -5.1 | -3.1 | -2.0 | +0.0 | 1409 |
| 32 | TEN | -6.1 | -3.4 | -2.6 | -0.0 | 1309 |

## Current model fit

- Fitted on 1829 games from seasons 2020–2026.
- Home field: 1.5 points (2.0 in divisional games).
- QB adjustment: 0.85 points per point of QB value gap.
- Special teams: 0.43 points per point of net special-teams EPA.
- Weight on the betting line: 90% for the margin, 97% for the total.
- Wind: -0.20 total points per mph above 10 mph at open-air stadiums.
