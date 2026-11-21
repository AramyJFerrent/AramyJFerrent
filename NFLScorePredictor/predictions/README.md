# NFL score predictions

Updated Sat Nov 21, 2026 03:05 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the final prediction, the model blended with the line: its expected points are run through the score simulator against the posted lines, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV, its chance of winning and its stake. Stakes are a 25% share of the Kelly stake, in units of 1% of the bankroll, with at most 3 units on one game. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers (the spread and total columns) often sit several points from the line, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. See the backtest for how they have done on past seasons; the live record is tracked below.

## 2026 Week 11

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 11/22 1:00 PM | ARI @ KC | ARI 13, KC 27 | KC 90% | ARI +880 / KC -880 | 12.5 – 27.3 | 3–23 / 16–40 | KC -8.0 / KC -15.5 | 46.9 / 40.5 | no edge | ARI (+880): EV +3.9%, 11%, stake 0.1u | no edge | Gardner Minshew / Patrick Mahomes | wind 14 mph |
| Sun 11/22 1:00 PM | BAL @ CAR | BAL 20, CAR 23 | CAR 59% | BAL +145 / CAR -145 | 20.3 – 23.3 | 10–32 / 12–35 | CAR -2.8 / CAR -3.0 | 48.0 / 43.5 | no edge | no edge | no edge | Tyler Huntley / Bryce Young |  |
| Sun 11/22 1:00 PM | JAX @ NYG | JAX 27, NYG 20 | JAX 67% | JAX -200 / NYG +200 | 26.2 – 20.3 | 14–38 / 10–32 | JAX -4.6 / JAX -6.0 | 44.9 / 46.5 | no edge | no edge | no edge | Trevor Lawrence / J.J. McCarthy |  |
| Sun 11/22 1:00 PM | MIA @ BUF | MIA 13, BUF 30 | BUF 91% | MIA +975 / BUF -975 | 13.9 – 30.0 | 3–24 / 17–43 | BUF -12.2 / BUF -16.5 | 47.8 / 44.5 | no edge | no edge | no edge | Kyle McCord / Josh Allen | wind 13 mph |
| Sun 11/22 1:00 PM | NO @ CHI | NO 20, CHI 30 | CHI 82% | NO +455 / CHI -455 | 18.2 – 29.8 | 7–30 / 17–42 | CHI -12.5 / CHI -11.5 | 47.5 / 48.5 | no edge | no edge | no edge | Tyler Shough / Caleb Williams |  |
| Sun 11/22 1:00 PM | TB @ DET | TB 20, DET 23 | DET 65% | TB +180 / DET -180 | 21.0 – 25.5 | 10–33 / 13–38 | DET -3.4 / DET -4.5 | 46.4 / 46.5 | no edge | no edge | no edge | Baker Mayfield / Jared Goff |  |
| Sun 11/22 1:00 PM | TEN @ DAL | TEN 24, DAL 30 | DAL 71% | TEN +250 / DAL -250 | 23.5 – 30.8 | 12–36 / 19–44 | DAL -5.2 / DAL -7.5 | 51.0 / 54.5 | no edge | no edge | no edge | Cam Ward / Dak Prescott |  |
| Sun 11/22 4:05 PM | NYJ @ LAC | NYJ 20, LAC 23 | LAC 59% | NYJ +140 / LAC -140 | 19.9 – 22.6 | 9–31 / 10–34 | NYJ -0.2 / LAC -3.0 | 42.7 / 42.5 | no edge | no edge | no edge | Geno Smith / Justin Herbert |  |
| Sun 11/22 4:25 PM | LV @ DEN | LV 17, DEN 27 | DEN 82% | LV +445 / DEN -445 | 14.9 – 25.6 | 6–26 / 13–38 | DEN -13.7 / DEN -10.5 | 40.5 / 40.5 | no edge | no edge | no edge | Fernando Mendoza / Bo Nix |  |
| Sun 11/22 4:25 PM | PIT @ PHI | PIT 20, PHI 17 | PIT 61% | PIT -155 / PHI +155 | 20.5 – 17.1 | 10–32 / 7–28 | PIT -1.9 / PIT -3.5 | 39.9 / 37.5 | no edge | no edge | no edge | Aaron Rodgers / Joe Milton III |  |
| Sun 11/22 8:20 PM | MIN @ SF | MIN 20, SF 23 | SF 59% | MIN +145 / SF -145 | 21.9 – 24.7 | 10–34 / 13–37 | SF -0.9 / SF -3.0 | 47.4 / 46.5 | no edge | no edge | no edge | Kirk Cousins / Brock Purdy |  |
| Mon 11/23 8:15 PM | CIN @ WAS | CIN 27, WAS 24 | CIN 67% | CIN -200 / WAS +200 | 30.1 – 24.4 | 17–43 / 13–37 | CIN -2.6 / CIN -6.0 | 53.5 / 54.5 | no edge | no edge | no edge | Joe Burrow / Jayden Daniels |  |

## 2026 Week 12

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wed 11/25 8:00 PM | GB @ LA | GB 20, LA 23 | LA 60% | GB +150 / LA -150 | 21.3 – 24.3 | 10–33 / 13–37 | LA -3.4 / LA -3.0 | 48.4 / 45.5 | no edge | no edge | no edge | Jordan Love / Matthew Stafford |  |
| Thu 11/26 1:00 PM | CHI @ DET | CHI 30, DET 27 | CHI 56% | CHI -125 / DET +125 | 28.7 – 26.6 | 16–41 / 14–39 | DET -1.9 / CHI -2.5 | 50.3 / 55.5 | no edge | no edge | no edge | Caleb Williams / Jared Goff |  |
| Thu 11/26 4:30 PM | PHI @ DAL | PHI 20, DAL 27 | DAL 74% | PHI +290 / DAL -290 | 19.6 – 27.9 | 9–31 / 16–41 | DAL -6.3 / DAL -8.5 | 45.5 / 47.5 | no edge | no edge | no edge | Joe Milton III / Dak Prescott |  |
| Thu 11/26 8:20 PM | KC @ BUF | KC 24, BUF 27 | BUF 60% | KC +150 / BUF -150 | 23.1 – 26.2 | 12–35 / 14–38 | BUF -4.1 / BUF -3.0 | 52.7 / 51.5 | no edge | no edge | Under 51.5 (-117): EV +6.5%, 57%, stake 1.9u | Patrick Mahomes / Josh Allen | wind 21 mph |
| Fri 11/27 3:00 PM | DEN @ PIT | DEN 20, PIT 17 | DEN 57% | DEN -130 / PIT +130 | 21.1 – 18.7 | 10–33 / 8–30 | DEN -0.8 / DEN -2.5 | 43.9 / 40.5 | no edge | no edge | no edge | Bo Nix / Aaron Rodgers | wind 14 mph |
| Sun 11/29 1:00 PM | ATL @ MIN | ATL 17, MIN 24 | MIN 71% | ATL +250 / MIN -250 | 17.6 – 24.7 | 7–29 / 13–37 | MIN -8.5 / MIN -7.0 | 38.2 / 42.5 | no edge | no edge | no edge | Michael Penix Jr. / Kirk Cousins |  |
| Sun 11/29 1:00 PM | BAL @ HOU | BAL 20, HOU 27 | HOU 70% | BAL +240 / HOU -240 | 19.0 – 25.5 | 8–31 / 13–38 | HOU -6.9 / HOU -6.5 | 43.3 / 44.5 | no edge | no edge | no edge | Tyler Huntley / C.J. Stroud |  |
| Sun 11/29 1:00 PM | NO @ CIN | NO 20, CIN 30 | CIN 78% | NO +350 / CIN -350 | 21.3 – 31.1 | 10–34 / 19–44 | CIN -7.8 / CIN -10.0 | 50.5 / 52.5 | no edge | no edge | no edge | Tyler Shough / Joe Burrow |  |
| Sun 11/29 1:00 PM | NYG @ IND | NYG 23, IND 20 | NYG 69% | NYG -220 / IND +220 | 24.6 – 18.8 | 13–37 / 7–30 | IND -0.5 / NYG -6.5 | 40.9 / 43.5 | no edge | no edge | no edge | J.J. McCarthy / Anthony Richardson |  |
| Sun 11/29 1:00 PM | NYJ @ MIA | NYJ 23, MIA 20 | NYJ 59% | NYJ -145 / MIA +145 | 22.2 – 19.3 | 10–34 / 9–31 | NYJ -2.0 / NYJ -3.0 | 43.3 / 41.5 | no edge | no edge | no edge | Geno Smith / Kyle McCord |  |
| Sun 11/29 1:00 PM | TEN @ JAX | TEN 17, JAX 31 | JAX 88% | TEN +715 / JAX -715 | 16.1 – 30.4 | 6–27 / 17–44 | JAX -12.9 / JAX -14.5 | 46.0 / 46.5 | no edge | no edge | no edge | Cam Ward / Trevor Lawrence |  |
| Sun 11/29 4:05 PM | NE @ LAC | NE 17, LAC 20 | LAC 61% | NE +155 / LAC -155 | 18.0 – 21.6 | 7–29 / 10–34 | NE -5.7 / LAC -4.5 | 41.9 / 39.5 | no edge | NE (+189): EV +5.0%, 36%, stake 0.7u | no edge | Drake Maye / Justin Herbert |  |
| Sun 11/29 4:25 PM | SEA @ SF | SEA 20, SF 23 | SF 57% | SEA +130 / SF -130 | 22.1 – 24.5 | 10–34 / 13–37 | SF -1.7 / SF -2.5 | 48.5 / 46.5 | no edge | no edge | no edge | Sam Darnold / Brock Purdy |  |
| Sun 11/29 4:25 PM | WAS @ ARI | WAS 23, ARI 20 | WAS 69% | WAS -225 / ARI +225 | 24.4 – 18.3 | 13–37 / 7–30 | WAS -2.1 / WAS -6.5 | 46.4 / 42.5 | no edge | no edge | no edge | Jayden Daniels / Gardner Minshew |  |
| Sun 11/29 8:20 PM | LV @ CLE | LV 17, CLE 20 | CLE 66% | LV +195 / CLE -195 | 17.4 – 22.3 | 7–28 / 10–34 | CLE -9.5 / CLE -4.5 | 37.6 / 40.5 | no edge | no edge | no edge | Fernando Mendoza / Deshaun Watson | wind 13 mph |
| Mon 11/30 8:15 PM | CAR @ TB | CAR 20, TB 23 | TB 59% | CAR +140 / TB -140 | 20.4 – 23.1 | 10–32 / 12–35 | TB -3.9 / TB -2.5 | 43.2 / 43.5 | no edge | no edge | no edge | Bryce Young / Baker Mayfield |  |

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
