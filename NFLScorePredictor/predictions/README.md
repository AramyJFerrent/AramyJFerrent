# NFL score predictions

Updated Thu Nov 19, 2026 04:31 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the final prediction, the model blended with the line: its expected points are run through the score simulator against the posted lines, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV, its chance of winning and its stake. Stakes are a 25% share of the Kelly stake, in units of 1% of the bankroll, with at most 3 units on one game. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers (the spread and total columns) often sit several points from the line, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. See the backtest for how they have done on past seasons; the live record is tracked below.

## 2026 Week 11

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 11/19 8:15 PM | IND @ HOU | IND 17, HOU 27 | HOU 83% | IND +485 / HOU -485 | 16.3 – 28.2 | 6–27 / 16–41 | HOU -5.9 / HOU -12.5 | 44.0 / 44.5 | no edge | IND (+498): EV +5.6%, 18%, stake 0.3u | no edge | Daniel Jones / C.J. Stroud |  |
| Sun 11/22 1:00 PM | ARI @ KC | ARI 13, KC 27 | KC 90% | ARI +865 / KC -865 | 12.9 – 27.8 | 3–23 / 16–41 | KC -9.1 / KC -15.5 | 47.5 / 40.5 | no edge | no edge | no edge | Gardner Minshew / Patrick Mahomes |  |
| Sun 11/22 1:00 PM | BAL @ CAR | BAL 20, CAR 23 | CAR 59% | BAL +145 / CAR -145 | 20.3 – 23.2 | 10–32 / 12–35 | CAR -2.4 / CAR -3.0 | 45.2 / 43.5 | no edge | no edge | no edge | Tyler Huntley / Bryce Young |  |
| Sun 11/22 1:00 PM | JAX @ NYG | JAX 27, NYG 20 | JAX 68% | JAX -210 / NYG +210 | 26.2 – 20.3 | 14–38 / 10–32 | JAX -5.4 / JAX -6.0 | 45.0 / 46.5 | no edge | no edge | no edge | Trevor Lawrence / J.J. McCarthy |  |
| Sun 11/22 1:00 PM | MIA @ BUF | MIA 13, BUF 30 | BUF 91% | MIA +1015 / BUF -1015 | 14.2 – 30.4 | 3–24 / 18–44 | BUF -14.2 / BUF -16.5 | 46.9 / 44.5 | no edge | MIA (+850): EV +4.0%, 11%, stake 0.1u | no edge | Kyle McCord / Josh Allen |  |
| Sun 11/22 1:00 PM | NO @ CHI | NO 20, CHI 30 | CHI 82% | NO +455 / CHI -455 | 18.5 – 29.9 | 7–30 / 17–43 | CHI -10.2 / CHI -11.5 | 46.3 / 48.5 | no edge | no edge | no edge | Tyler Shough / Caleb Williams |  |
| Sun 11/22 1:00 PM | TB @ DET | TB 20, DET 23 | DET 68% | TB +210 / DET -210 | 19.9 – 25.6 | 9–31 / 13–38 | DET -3.5 / DET -6.0 | 45.3 / 45.5 | no edge | no edge | no edge | Baker Mayfield / Jared Goff |  |
| Sun 11/22 1:00 PM | TEN @ DAL | TEN 24, DAL 31 | DAL 73% | TEN +275 / DAL -275 | 23.5 – 31.8 | 12–37 / 20–45 | DAL -7.0 / DAL -8.5 | 51.0 / 55.5 | no edge | no edge | no edge | Cam Ward / Dak Prescott |  |
| Sun 11/22 4:05 PM | NYJ @ LAC | NYJ 20, LAC 23 | LAC 59% | NYJ +145 / LAC -145 | 19.4 – 22.1 | 9–30 / 10–34 | LAC -0.4 / LAC -3.0 | 41.1 / 41.5 | no edge | no edge | no edge | Geno Smith / Justin Herbert |  |
| Sun 11/22 4:25 PM | LV @ DEN | LV 17, DEN 24 | DEN 81% | LV +425 / DEN -425 | 15.1 – 25.4 | 6–26 / 13–38 | DEN -13.2 / DEN -10.0 | 40.0 / 40.5 | no edge | no edge | no edge | Fernando Mendoza / Bo Nix |  |
| Sun 11/22 4:25 PM | PIT @ PHI | PIT 20, PHI 17 | PIT 63% | PIT -170 / PHI +170 | 20.9 – 16.7 | 10–32 / 6–27 | PIT -0.9 / PIT -4.5 | 39.0 / 37.5 | no edge | no edge | no edge | Aaron Rodgers / Joe Milton III |  |
| Sun 11/22 8:20 PM | MIN @ SF | MIN 20, SF 23 | SF 58% | MIN +140 / SF -140 | 21.9 – 24.7 | 10–34 / 13–37 | SF -0.9 / SF -3.0 | 47.2 / 46.5 | no edge | no edge | no edge | Kirk Cousins / Brock Purdy |  |
| Mon 11/23 8:15 PM | CIN @ WAS | CIN 31, WAS 24 | CIN 67% | CIN -200 / WAS +200 | 30.1 – 24.4 | 17–43 / 13–37 | CIN -2.6 / CIN -6.0 | 53.5 / 54.5 | no edge | no edge | no edge | Joe Burrow / Jayden Daniels |  |

## 2026 Week 12

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wed 11/25 8:00 PM | GB @ LA | GB 20, LA 23 | LA 60% | GB +150 / LA -150 | 21.1 – 24.5 | 10–33 / 13–37 | LA -3.4 / LA -3.5 | 48.4 / 45.5 | no edge | no edge | no edge | J.Love / M.Stafford |  |
| Thu 11/26 1:00 PM | CHI @ DET | CHI 30, DET 27 | CHI 56% | CHI -125 / DET +125 | 28.7 – 26.6 | 17–41 / 14–38 | DET -1.9 / CHI -2.5 | 50.4 / 55.5 | no edge | no edge | no edge | C.Williams / J.Goff |  |
| Thu 11/26 4:30 PM | PHI @ DAL | PHI 20, DAL 27 | DAL 74% | PHI +285 / DAL -285 | 19.6 – 27.9 | 9–31 / 16–41 | DAL -6.3 / DAL -8.5 | 45.5 / 47.5 | no edge | no edge | no edge | J.Milton / D.Prescott |  |
| Thu 11/26 8:20 PM | KC @ BUF | KC 24, BUF 27 | BUF 59% | KC +140 / BUF -140 | 23.7 – 26.8 | 13–36 / 15–39 | BUF -4.1 / BUF -3.0 | 52.7 / 50.5 | no edge | no edge | no edge | P.Mahomes / J.Allen |  |
| Fri 11/27 3:00 PM | DEN @ PIT | DEN 23, PIT 20 | DEN 54% | DEN -120 / PIT +120 | 21.0 – 19.6 | 10–33 / 9–31 | DEN -0.8 / DEN -1.5 | 43.9 / 40.5 | no edge | no edge | no edge | B.Nix / A.Rodgers |  |
| Sun 11/29 1:00 PM | ATL @ MIN | ATL 17, MIN 24 | MIN 72% | ATL +255 / MIN -255 | 17.6 – 24.7 | 7–29 / 13–37 | MIN -8.6 / MIN -7.0 | 38.2 / 42.5 | no edge | no edge | no edge | M.Penix / K.Cousins |  |
| Sun 11/29 1:00 PM | BAL @ HOU | BAL 20, HOU 27 | HOU 68% | BAL +210 / HOU -210 | 19.3 – 25.2 | 9–31 / 13–37 | HOU -5.3 / HOU -6.0 | 44.4 / 44.5 | no edge | no edge | no edge | J.Brissett / C.Stroud |  |
| Sun 11/29 1:00 PM | NO @ CIN | NO 20, CIN 30 | CIN 78% | NO +360 / CIN -360 | 21.3 – 31.1 | 10–34 / 19–44 | CIN -7.8 / CIN -10.0 | 50.6 / 52.5 | no edge | no edge | no edge | T.Shough / J.Burrow |  |
| Sun 11/29 1:00 PM | NYG @ IND | NYG 23, IND 20 | NYG 59% | NYG -145 / IND +145 | 23.7 – 20.8 | 13–36 / 10–33 | IND -3.0 / NYG -3.5 | 42.8 / 44.5 | no edge | no edge | no edge | J.McCarthy / D.Jones |  |
| Sun 11/29 1:00 PM | NYJ @ MIA | NYJ 23, MIA 20 | NYJ 58% | NYJ -140 / MIA +140 | 22.1 – 19.4 | 10–34 / 9–31 | MIA -0.1 / NYJ -3.0 | 41.2 / 41.5 | no edge | no edge | no edge | C.Klubnik / K.McCord |  |
| Sun 11/29 1:00 PM | TEN @ JAX | TEN 17, JAX 31 | JAX 88% | TEN +715 / JAX -715 | 16.5 – 30.9 | 6–27 / 19–44 | JAX -13.0 / JAX -14.5 | 46.0 / 47.5 | no edge | no edge | no edge | C.Ward / T.Lawrence |  |
| Sun 11/29 4:05 PM | NE @ LAC | NE 17, LAC 20 | LAC 63% | NE +175 / LAC -175 | 17.7 – 21.7 | 7–29 / 10–34 | NE -0.4 / LAC -4.5 | 36.5 / 39.5 | no edge | no edge | no edge | T.DeVito / J.Herbert |  |
| Sun 11/29 4:25 PM | SEA @ SF | SEA 20, SF 23 | SF 57% | SEA +135 / SF -135 | 22.0 – 24.5 | 10–34 / 13–37 | SF -3.2 / SF -2.5 | 47.0 / 46.5 | no edge | no edge | no edge | D.Lock / B.Purdy |  |
| Sun 11/29 4:25 PM | WAS @ ARI | WAS 23, ARI 17 | WAS 70% | WAS -235 / ARI +235 | 23.9 – 17.7 | 13–37 / 7–29 | WAS -4.2 / WAS -6.5 | 44.4 / 41.5 | no edge | no edge | no edge | J.Daniels / C.Beck |  |
| Sun 11/29 8:20 PM | LV @ CLE | LV 17, CLE 20 | CLE 66% | LV +200 / CLE -200 | 17.7 – 22.7 | 7–29 / 11–35 | CLE -9.5 / CLE -4.5 | 37.6 / 40.5 | no edge | no edge | no edge | F.Mendoza / D.Watson |  |
| Mon 11/30 8:15 PM | CAR @ TB | CAR 20, TB 23 | TB 59% | CAR +145 / TB -145 | 20.4 – 23.1 | 10–32 / 12–35 | TB -3.9 / TB -2.5 | 43.2 / 43.5 | no edge | no edge | no edge | B.Young / B.Mayfield |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 150 | 9.56 | 10.38 | 7.27 | 68.5% | 0.213 | 84.7% |
| Model only (before blending) | 150 | 9.62 | 10.79 | 7.39 | 69.1% | – | – |
| Betting line when predicted | 150 | 9.57 | 10.37 | 7.26 | 68.5% | – | – |

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
| BUF @ NYJ | 27–20 | 31–12 | 74% | yes |
| CAR @ NO | 24–27 | 20–17 | 42% | yes |
| HOU @ CLE | 20–17 | 24–27 | 37% | yes |
| JAX @ TEN | 27–17 | 40–23 | 79% | yes |
| KC @ ATL | 26–23 | 35–13 | 60% | yes |
| MIA @ IND | 17–20 | 22–24 | 64% | yes |
| MIN @ GB | 20–23 | 30–10 | 41% | yes |
| LA @ ARI | 23–13 | 34–6 | 79% | yes |
| SEA @ LV | 23–17 | 21–13 | 71% | yes |
| SF @ DAL | 30–27 | 46–40 | 63% | no |
| PIT @ CIN | 24–27 | 18–38 | 61% | yes |
| LAC @ BAL | 17–20 | 23–20 | 36% | yes |

## Power ratings

Points per game better than an average team on a neutral field, from opponent-adjusted EPA with this season's games weighted against a preseason prior. Defense is positive when it holds opponents below average.

| # | Team | Net | Offense | Defense | Special teams | Elo |
|---|---|---|---|---|---|---|
| 1 | BUF | +5.4 | +4.6 | +0.1 | +0.7 | 1705 |
| 2 | JAX | +5.3 | +2.9 | +1.5 | +0.9 | 1654 |
| 3 | SF | +4.6 | +5.2 | +0.1 | -0.7 | 1647 |
| 4 | DET | +4.3 | +2.9 | -0.0 | +1.4 | 1625 |
| 5 | CHI | +4.0 | +2.3 | +0.3 | +1.4 | 1629 |
| 6 | SEA | +4.0 | -0.0 | +3.1 | +0.9 | 1647 |
| 7 | LA | +3.8 | +3.1 | +2.2 | -1.4 | 1622 |
| 8 | CIN | +2.6 | +3.8 | -1.5 | +0.3 | 1615 |
| 9 | KC | +2.2 | +2.8 | +0.9 | -1.5 | 1589 |
| 10 | MIN | +2.0 | -3.3 | +3.6 | +1.7 | 1625 |
| 11 | DEN | +1.6 | +0.2 | +1.4 | +0.0 | 1647 |
| 12 | GB | +1.5 | +2.1 | +0.4 | -1.0 | 1546 |
| 13 | NE | +1.5 | +1.4 | -0.0 | +0.1 | 1537 |
| 14 | HOU | +1.4 | -0.2 | +1.2 | +0.4 | 1525 |
| 15 | BAL | +0.4 | +1.4 | -0.2 | -0.8 | 1456 |
| 16 | TB | -0.0 | -1.8 | +1.5 | +0.3 | 1494 |
| 17 | DAL | -0.3 | +2.9 | -3.3 | +0.1 | 1455 |
| 18 | PIT | -0.8 | -0.7 | -0.2 | +0.1 | 1551 |
| 19 | NYG | -0.9 | -0.5 | -0.2 | -0.2 | 1467 |
| 20 | IND | -1.3 | -1.4 | -0.6 | +0.7 | 1398 |
| 21 | CAR | -1.4 | -0.2 | -0.9 | -0.4 | 1443 |
| 22 | WAS | -1.5 | -0.3 | -1.5 | +0.3 | 1447 |
| 23 | PHI | -1.6 | -2.3 | +0.7 | -0.0 | 1397 |
| 24 | CLE | -2.8 | -3.8 | +0.9 | +0.1 | 1460 |
| 25 | NO | -3.1 | -2.0 | -0.3 | -0.8 | 1404 |
| 26 | ATL | -3.4 | -2.3 | -0.1 | -1.0 | 1421 |
| 27 | NYJ | -3.9 | -2.2 | -2.3 | +0.5 | 1328 |
| 28 | LAC | -4.0 | -4.5 | +0.9 | -0.4 | 1395 |
| 29 | MIA | -4.0 | -1.7 | -1.4 | -0.9 | 1359 |
| 30 | ARI | -4.7 | -2.2 | -1.6 | -0.9 | 1374 |
| 31 | LV | -5.1 | -3.3 | -2.0 | +0.2 | 1399 |
| 32 | TEN | -5.8 | -3.1 | -2.6 | -0.1 | 1301 |

## Current model fit

- Fitted on 1843 games from seasons 2020–2026.
- Home field: 1.4 points (1.9 in divisional games).
- QB adjustment: 0.86 points per point of QB value gap.
- Special teams: 0.46 points per point of net special-teams EPA.
- Weight on the betting line: 90% for the margin, 96% for the total.
- Wind: -0.20 total points per mph above 10 mph at open-air stadiums.
