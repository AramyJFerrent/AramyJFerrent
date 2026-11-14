# NFL score predictions

Updated Sat Nov 14, 2026 01:44 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the final prediction, the model blended with the line: its expected points are run through the score simulator against the posted lines, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV, its chance of winning and its stake. Stakes are a 25% share of the Kelly stake, in units of 1% of the bankroll, with at most 3 units on one game. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers (the spread and total columns) often sit several points from the line, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. See the backtest for how they have done on past seasons; the live record is tracked below.

## 2026 Week 10

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 11/15 9:30 AM | NE @ DET | NE 24, DET 27 | DET 56% | NE +130 / DET -130 | 23.6 – 25.9 | 13–35 / 14–38 | DET -0.1 / DET -2.5 | 50.7 / 49.5 | no edge | no edge | no edge | Drake Maye / Jared Goff |  |
| Sun 11/15 1:00 PM | BUF @ NYJ | BUF 27, NYJ 20 | BUF 74% | BUF -280 / NYJ +280 | 29.4 – 21.1 | 17–42 / 10–34 | BUF -6.4 / BUF -8.5 | 50.9 / 50.5 | no edge | no edge | no edge | Josh Allen / Geno Smith |  |
| Sun 11/15 1:00 PM | CAR @ NO | CAR 24, NO 27 | NO 58% | CAR +135 / NO -135 | 23.1 – 25.4 | 12–35 / 13–37 | NO -0.2 / NO -2.5 | 47.2 / 48.5 | no edge | no edge | no edge | Bryce Young / Tyler Shough |  |
| Sun 11/15 1:00 PM | HOU @ CLE | HOU 20, CLE 17 | HOU 63% | HOU -170 / CLE +170 | 22.1 – 18.1 | 10–34 / 7–29 | CLE -0.1 / HOU -4.5 | 41.1 / 40.5 | no edge | no edge | no edge | C.J. Stroud / Deshaun Watson |  |
| Sun 11/15 1:00 PM | JAX @ TEN | JAX 27, TEN 17 | JAX 79% | JAX -375 / TEN +375 | 28.5 – 18.0 | 16–41 / 7–30 | JAX -10.5 / JAX -10.5 | 44.9 / 46.5 | no edge | no edge | no edge | Trevor Lawrence / Cam Ward |  |
| Sun 11/15 1:00 PM | KC @ ATL | KC 26, ATL 23 | KC 60% | KC -150 / ATL +150 | 25.3 – 22.2 | 13–37 / 10–34 | KC -5.0 / KC -3.0 | 47.5 / 47.5 | no edge | no edge | no edge | Patrick Mahomes / Michael Penix Jr. |  |
| Sun 11/15 1:00 PM | MIA @ IND | MIA 17, IND 20 | IND 64% | MIA +180 / IND -180 | 16.7 – 21.0 | 6–27 / 10–33 | IND -2.5 / IND -4.5 | 44.9 / 37.5 | no edge | no edge | no edge | Malik Willis / Daniel Jones |  |
| Sun 11/15 1:00 PM | MIN @ GB | MIN 20, GB 23 | GB 59% | MIN +145 / GB -145 | 20.1 – 22.5 | 9–31 / 10–34 | GB -1.8 / GB -2.5 | 45.3 / 42.5 | no edge | no edge | no edge | Kirk Cousins / Jordan Love |  |
| Sun 11/15 4:05 PM | LA @ ARI | LA 24, ARI 17 | LA 78% | LA -355 / ARI +355 | 24.4 – 15.2 | 13–37 / 6–26 | LA -6.4 / LA -9.5 | 46.0 / 39.5 | no edge | no edge | no edge | Matthew Stafford / Gardner Minshew |  |
| Sun 11/15 4:05 PM | SEA @ LV | SEA 24, LV 17 | SEA 71% | SEA -250 / LV +250 | 23.6 – 16.8 | 13–36 / 6–28 | SEA -8.9 / SEA -6.5 | 37.6 / 40.5 | no edge | no edge | no edge | Sam Darnold / Fernando Mendoza |  |
| Sun 11/15 4:25 PM | SF @ DAL | SF 30, DAL 27 | SF 64% | SF -180 / DAL +180 | 30.0 – 25.6 | 17–42 / 13–38 | SF -4.2 / SF -4.5 | 58.6 / 55.5 | no edge | no edge | no edge | Brock Purdy / Dak Prescott |  |
| Sun 11/15 8:20 PM | PIT @ CIN | PIT 24, CIN 27 | CIN 61% | PIT +155 / CIN -155 | 23.1 – 26.5 | 12–35 / 14–39 | CIN -2.9 / CIN -3.5 | 52.0 / 49.5 | no edge | no edge | no edge | Aaron Rodgers / Joe Burrow |  |
| Mon 11/16 8:15 PM | LAC @ BAL | LAC 17, BAL 20 | BAL 65% | LAC +190 / BAL -190 | 17.0 – 21.5 | 6–28 / 10–34 | BAL -4.6 / BAL -4.5 | 38.0 / 38.5 | no edge | no edge | no edge | Justin Herbert / Tyler Huntley |  |

## 2026 Week 11

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 11/19 8:15 PM | IND @ HOU | IND 17, HOU 27 | HOU 78% | IND +365 / HOU -365 | 17.4 – 27.1 | 7–28 / 16–40 | HOU -6.2 / HOU -10.0 | 44.3 / 44.5 | no edge | no edge | no edge | Daniel Jones / C.J. Stroud |  |
| Sun 11/22 1:00 PM | ARI @ KC | ARI 13, KC 27 | KC 87% | ARI +660 / KC -660 | 14.6 – 28.1 | 6–25 / 16–41 | KC -8.9 / KC -14.0 | 48.3 / 42.5 | no edge | ARI (+600): EV +4.1%, 15%, stake 0.2u | no edge | Gardner Minshew / Patrick Mahomes |  |
| Sun 11/22 1:00 PM | BAL @ CAR | BAL 20, CAR 23 | CAR 55% | BAL +120 / CAR -120 | 21.5 – 23.1 | 10–33 / 12–35 | CAR -2.8 / CAR -1.5 | 46.0 / 44.5 | no edge | no edge | no edge | Tyler Huntley / Bryce Young |  |
| Sun 11/22 1:00 PM | JAX @ NYG | JAX 27, NYG 20 | JAX 68% | JAX -210 / NYG +210 | 25.2 – 19.2 | 13–37 / 9–31 | JAX -5.3 / JAX -6.0 | 44.7 / 44.5 | no edge | no edge | no edge | Trevor Lawrence / J.J. McCarthy |  |
| Sun 11/22 1:00 PM | MIA @ BUF | MIA 13, BUF 30 | BUF 91% | MIA +995 / BUF -995 | 14.1 – 30.3 | 3–24 / 17–43 | BUF -13.0 / BUF -16.5 | 49.5 / 46.5 | no edge | no edge | Under 46.5 (-110): EV +8.9%, 57%, stake 2.4u | Malik Willis / Josh Allen | wind 21 mph |
| Sun 11/22 1:00 PM | NO @ CHI | NO 20, CHI 30 | CHI 77% | NO +345 / CHI -345 | 19.3 – 29.0 | 9–31 / 17–42 | CHI -11.2 / CHI -9.5 | 47.2 / 48.5 | no edge | no edge | no edge | Tyler Shough / Caleb Williams |  |
| Sun 11/22 1:00 PM | TB @ DET | TB 24, DET 27 | DET 60% | TB +150 / DET -150 | 22.0 – 25.4 | 10–34 / 13–38 | DET -2.6 / DET -3.5 | 44.5 / 47.5 | no edge | no edge | no edge | Baker Mayfield / Jared Goff |  |
| Sun 11/22 1:00 PM | TEN @ DAL | TEN 24, DAL 30 | DAL 72% | TEN +260 / DAL -260 | 22.0 – 29.5 | 10–34 / 17–42 | DAL -7.9 / DAL -7.5 | 50.4 / 51.5 | no edge | no edge | no edge | Cam Ward / Dak Prescott |  |
| Sun 11/22 4:05 PM | NYJ @ LAC | NYJ 20, LAC 23 | LAC 54% | NYJ +115 / LAC -115 | 20.6 – 21.8 | 10–32 / 10–34 | NYJ -0.9 / LAC -1.5 | 40.0 / 42.5 | no edge | no edge | no edge | Geno Smith / Justin Herbert |  |
| Sun 11/22 4:25 PM | LV @ DEN | LV 17, DEN 24 | DEN 77% | LV +335 / DEN -335 | 16.2 – 25.2 | 6–27 / 13–38 | DEN -13.4 / DEN -8.5 | 39.9 / 41.5 | no edge | no edge | no edge | Fernando Mendoza / Bo Nix |  |
| Sun 11/22 4:25 PM | PIT @ PHI | PIT 20, PHI 17 | PIT 63% | PIT -175 / PHI +175 | 21.4 – 17.1 | 10–34 / 7–28 | PIT -1.7 / PIT -4.5 | 38.1 / 38.5 | no edge | no edge | no edge | Aaron Rodgers / Joe Milton III |  |
| Sun 11/22 8:20 PM | MIN @ SF | MIN 20, SF 23 | SF 61% | MIN +155 / SF -155 | 21.1 – 24.4 | 10–33 / 13–37 | SF -1.4 / SF -3.5 | 45.5 / 45.5 | no edge | no edge | no edge | Kirk Cousins / Brock Purdy |  |
| Mon 11/23 8:15 PM | CIN @ WAS | CIN 27, WAS 24 | CIN 60% | CIN -150 / WAS +150 | 27.3 – 23.9 | 16–40 / 13–36 | CIN -2.5 / CIN -3.5 | 53.8 / 51.5 | no edge | no edge | no edge | Joe Burrow / Jayden Daniels |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 137 | 9.44 | 10.56 | 7.22 | 68.4% | 0.215 | 84.3% |
| Model only (before blending) | 137 | 9.56 | 11.04 | 7.38 | 66.9% | – | – |
| Betting line when predicted | 137 | 9.44 | 10.55 | 7.22 | 68.4% | – | – |

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

## Power ratings

Points per game better than an average team on a neutral field, from opponent-adjusted EPA with this season's games weighted against a preseason prior. Defense is positive when it holds opponents below average.

| # | Team | Net | Offense | Defense | Special teams | Elo |
|---|---|---|---|---|---|---|
| 1 | BUF | +5.8 | +4.8 | +0.1 | +0.9 | 1697 |
| 2 | JAX | +5.7 | +3.1 | +1.8 | +0.8 | 1645 |
| 3 | CHI | +4.7 | +2.6 | +0.6 | +1.4 | 1629 |
| 4 | SF | +4.1 | +4.7 | +0.4 | -1.0 | 1635 |
| 5 | SEA | +3.8 | -0.7 | +3.2 | +1.3 | 1636 |
| 6 | DET | +3.7 | +2.6 | -0.5 | +1.5 | 1595 |
| 7 | LA | +3.3 | +2.8 | +2.0 | -1.4 | 1604 |
| 8 | GB | +3.2 | +3.1 | +1.1 | -1.0 | 1581 |
| 9 | NE | +2.7 | +2.2 | +0.3 | +0.1 | 1566 |
| 10 | CIN | +2.2 | +3.7 | -1.9 | +0.5 | 1590 |
| 11 | KC | +2.1 | +3.1 | +0.4 | -1.3 | 1565 |
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
| 24 | NO | -3.3 | -1.5 | -0.8 | -0.9 | 1419 |
| 25 | CLE | -3.4 | -4.4 | +1.0 | +0.1 | 1444 |
| 26 | ATL | -3.4 | -1.8 | -0.0 | -1.6 | 1445 |
| 27 | NYJ | -3.4 | -1.9 | -2.1 | +0.6 | 1335 |
| 28 | MIA | -3.8 | -1.2 | -2.0 | -0.6 | 1367 |
| 29 | ARI | -4.5 | -1.9 | -1.5 | -1.1 | 1392 |
| 30 | LAC | -4.8 | -5.5 | +0.9 | -0.2 | 1374 |
| 31 | LV | -5.0 | -3.1 | -2.0 | +0.0 | 1409 |
| 32 | TEN | -6.0 | -3.4 | -2.6 | -0.1 | 1309 |

## Current model fit

- Fitted on 1830 games from seasons 2020–2026.
- Home field: 1.5 points (2.0 in divisional games).
- QB adjustment: 0.85 points per point of QB value gap.
- Special teams: 0.43 points per point of net special-teams EPA.
- Weight on the betting line: 90% for the margin, 97% for the total.
- Wind: -0.20 total points per mph above 10 mph at open-air stadiums.
