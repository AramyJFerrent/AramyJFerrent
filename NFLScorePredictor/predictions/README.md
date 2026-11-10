# NFL score predictions

Updated Mon Nov 09, 2026 11:36 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the final prediction, the model blended with the line: its expected points are run through the score simulator against the posted lines, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV, its chance of winning and its stake. Stakes are a 25% share of the Kelly stake, in units of 1% of the bankroll, with at most 3 units on one game. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers (the spread and total columns) often sit several points from the line, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. See the backtest for how they have done on past seasons; the live record is tracked below.

## 2026 Week 10

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 11/12 8:15 PM | WAS @ NYG | WAS 20, NYG 23 | NYG 58% | WAS +140 / NYG -140 | 20.1 – 22.4 | 9–31 / 10–34 | NYG -0.9 / NYG -2.5 | 44.1 / 42.5 | no edge | no edge | no edge | Jayden Daniels / J.J. McCarthy |  |
| Sun 11/15 9:30 AM | NE @ DET | NE 24, DET 27 | DET 56% | NE +130 / DET -130 | 24.6 – 26.9 | 13–37 / 16–39 | DET -1.0 / DET -2.5 | 50.0 / 51.5 | no edge | no edge | no edge | Drake Maye / Jared Goff |  |
| Sun 11/15 1:00 PM | BUF @ NYJ | BUF 27, NYJ 24 | BUF 69% | BUF -225 / NYJ +225 | 28.1 – 22.2 | 16–41 / 10–34 | BUF -6.0 / – | 52.4 / – | no line yet | no line yet | no line yet | Josh Allen / Geno Smith | wind 14 mph |
| Sun 11/15 1:00 PM | CAR @ NO | CAR 20, NO 23 | NO 55% | CAR +120 / NO -120 | 23.1 – 24.4 | 12–35 / 13–37 | NO -0.2 / NO -1.5 | 46.7 / 47.5 | no edge | no edge | no edge | Bryce Young / Tyler Shough |  |
| Sun 11/15 1:00 PM | HOU @ CLE | HOU 20, CLE 17 | HOU 64% | HOU -175 / CLE +175 | 21.7 – 17.4 | 10–34 / 7–28 | HOU -2.6 / HOU -4.5 | 40.4 / 39.5 | no edge | no edge | no edge | C.J. Stroud / Deshaun Watson |  |
| Sun 11/15 1:00 PM | JAX @ TEN | JAX 27, TEN 17 | JAX 79% | JAX -365 / TEN +365 | 28.2 – 18.3 | 16–41 / 7–30 | JAX -8.8 / JAX -10.0 | 45.6 / 46.5 | no edge | no edge | no edge | Trevor Lawrence / Cam Ward |  |
| Sun 11/15 1:00 PM | KC @ ATL | KC 23, ATL 20 | KC 62% | KC -160 / ATL +160 | 24.6 – 20.9 | 13–37 / 10–33 | KC -5.4 / KC -3.5 | 46.3 / 45.5 | no edge | no edge | no edge | Patrick Mahomes / Michael Penix Jr. |  |
| Sun 11/15 1:00 PM | MIA @ IND | MIA 20, IND 23 | IND 59% | MIA +145 / IND -145 | 19.0 – 21.6 | 9–30 / 10–34 | IND -4.4 / IND -2.5 | 44.4 / 40.5 | no edge | no edge | no edge | Malik Willis / Daniel Jones |  |
| Sun 11/15 1:00 PM | MIN @ GB | MIN 20, GB 23 | GB 58% | MIN +135 / GB -135 | 20.0 – 22.6 | 9–31 / 10–34 | GB -2.6 / – | 42.6 / – | no line yet | no line yet | no line yet | Kyler Murray / Jordan Love |  |
| Sun 11/15 4:05 PM | LA @ ARI | LA 24, ARI 17 | LA 77% | LA -335 / ARI +335 | 24.9 – 15.7 | 13–37 / 6–27 | LA -6.0 / LA -9.5 | 45.6 / 40.5 | no edge | no edge | no edge | Matthew Stafford / Gardner Minshew |  |
| Sun 11/15 4:05 PM | SEA @ LV | SEA 23, LV 20 | SEA 61% | SEA -160 / LV +160 | 23.6 – 19.8 | 13–36 / 9–32 | SEA -6.4 / SEA -3.5 | 41.3 / 43.5 | no edge | no edge | no edge | Sam Darnold / Kirk Cousins |  |
| Sun 11/15 4:25 PM | SF @ DAL | SF 30, DAL 27 | SF 60% | SF -150 / DAL +150 | 29.5 – 26.0 | 17–42 / 14–38 | SF -3.3 / SF -3.5 | 56.7 / 55.5 | no edge | no edge | no edge | Brock Purdy / Dak Prescott |  |
| Sun 11/15 8:20 PM | PIT @ CIN | PIT 24, CIN 27 | CIN 61% | PIT +160 / CIN -160 | 22.5 – 26.1 | 10–34 / 14–38 | CIN -4.1 / CIN -3.5 | 51.6 / 48.5 | no edge | no edge | no edge | Aaron Rodgers / Joe Burrow |  |
| Mon 11/16 8:15 PM | LAC @ BAL | LAC 17, BAL 20 | BAL 67% | LAC +200 / BAL -200 | 16.5 – 21.9 | 6–27 / 10–34 | BAL -4.7 / BAL -5.5 | 37.7 / 38.5 | no edge | no edge | no edge | Justin Herbert / Tyler Huntley |  |

## 2026 Week 11

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 11/19 8:15 PM | IND @ HOU | IND 20, HOU 23 | HOU 69% | IND +225 / HOU -225 | 19.0 – 25.2 | 7–30 / 13–38 | HOU -6.1 / – | 44.2 / – | no line yet | no line yet | no line yet | D.Jones / C.Stroud |  |
| Sun 11/22 1:00 PM | ARI @ KC | ARI 20, KC 27 | KC 76% | ARI +320 / KC -320 | 19.7 – 28.6 | 9–31 / 16–41 | KC -9.0 / – | 48.3 / – | no line yet | no line yet | no line yet | G.Minshew II / P.Mahomes |  |
| Sun 11/22 1:00 PM | BAL @ CAR | BAL 20, CAR 23 | CAR 63% | BAL +170 / CAR -170 | 20.2 – 24.4 | 9–32 / 13–37 | CAR -4.2 / – | 44.6 / – | no line yet | no line yet | no line yet | J.Fagnano / B.Young |  |
| Sun 11/22 1:00 PM | JAX @ NYG | JAX 26, NYG 20 | JAX 67% | JAX -205 / NYG +205 | 24.9 – 19.0 | 13–37 / 9–31 | JAX -5.8 / – | 43.9 / – | no line yet | no line yet | no line yet | T.Lawrence / J.McCarthy |  |
| Sun 11/22 1:00 PM | MIA @ BUF | MIA 17, BUF 31 | BUF 85% | MIA +570 / BUF -570 | 19.0 – 31.8 | 7–30 / 20–44 | BUF -12.8 / – | 50.8 / – | no line yet | no line yet | no line yet | M.Willis / J.Allen |  |
| Sun 11/22 1:00 PM | NO @ CHI | NO 17, CHI 27 | CHI 82% | NO +450 / CHI -450 | 17.9 – 29.2 | 7–29 / 17–42 | CHI -11.3 / – | 47.1 / – | no line yet | no line yet | no line yet | T.Shough / C.Williams |  |
| Sun 11/22 1:00 PM | TB @ DET | TB 20, DET 23 | DET 59% | TB +145 / DET -145 | 20.9 – 23.5 | 10–33 / 13–35 | DET -2.6 / – | 44.3 / – | no line yet | no line yet | no line yet | B.Mayfield / J.Goff |  |
| Sun 11/22 1:00 PM | TEN @ DAL | TEN 20, DAL 27 | DAL 72% | TEN +265 / DAL -265 | 21.3 – 29.2 | 10–34 / 17–42 | DAL -7.9 / – | 50.5 / – | no line yet | no line yet | no line yet | C.Ward / D.Prescott |  |
| Sun 11/22 4:05 PM | NYJ @ LAC | NYJ 20, LAC 17 | NYJ 53% | NYJ -115 / LAC +115 | 20.4 – 19.4 | 10–32 / 9–31 | NYJ -1.0 / – | 39.9 / – | no line yet | no line yet | no line yet | G.Smith / J.Herbert |  |
| Sun 11/22 4:25 PM | LV @ DEN | LV 17, DEN 27 | DEN 77% | LV +340 / DEN -340 | 17.3 – 26.7 | 6–28 / 14–39 | DEN -9.3 / – | 44.0 / – | no line yet | no line yet | no line yet | K.Cousins / B.Nix |  |
| Sun 11/22 4:25 PM | PIT @ PHI | PIT 20, PHI 17 | PIT 54% | PIT -120 / PHI +120 | 19.9 – 18.1 | 9–31 / 7–30 | PIT -1.8 / – | 38.1 / – | no line yet | no line yet | no line yet | A.Rodgers / J.Milton |  |
| Sun 11/22 8:20 PM | MIN @ SF | MIN 20, SF 23 | SF 55% | MIN +125 / SF -125 | 21.9 – 23.8 | 10–34 / 13–36 | SF -2.0 / – | 45.7 / – | no line yet | no line yet | no line yet | K.Murray / B.Purdy |  |
| Mon 11/23 8:15 PM | CIN @ WAS | CIN 27, WAS 24 | CIN 59% | CIN -140 / WAS +140 | 28.0 – 25.5 | 16–41 / 13–38 | CIN -2.6 / – | 53.5 / – | no line yet | no line yet | no line yet | J.Burrow / J.Daniels |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 135 | 9.44 | 10.56 | 7.25 | 68.7% | 0.215 | 84.1% |
| Model only (before blending) | 135 | 9.54 | 11.07 | 7.41 | 67.2% | – | – |
| Betting line when predicted | 135 | 9.44 | 10.55 | 7.25 | 68.7% | – | – |

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

## Power ratings

Points per game better than an average team on a neutral field, from opponent-adjusted EPA with this season's games weighted against a preseason prior. Defense is positive when it holds opponents below average.

| # | Team | Net | Offense | Defense | Special teams | Elo |
|---|---|---|---|---|---|---|
| 1 | JAX | +5.7 | +3.1 | +1.9 | +0.8 | 1645 |
| 2 | BUF | +5.6 | +5.3 | -0.8 | +1.1 | 1669 |
| 3 | CHI | +4.7 | +2.6 | +0.7 | +1.4 | 1629 |
| 4 | SF | +4.1 | +4.7 | +0.4 | -1.0 | 1635 |
| 5 | SEA | +3.8 | -0.8 | +3.2 | +1.3 | 1636 |
| 6 | DET | +3.7 | +2.6 | -0.4 | +1.5 | 1595 |
| 7 | LA | +3.3 | +2.7 | +2.0 | -1.5 | 1604 |
| 8 | GB | +3.2 | +3.0 | +1.2 | -1.0 | 1581 |
| 9 | NE | +2.7 | +2.2 | +0.3 | +0.2 | 1566 |
| 10 | CIN | +2.2 | +3.7 | -1.9 | +0.5 | 1590 |
| 11 | KC | +2.1 | +3.1 | +0.4 | -1.3 | 1565 |
| 12 | MIN | +1.7 | -3.0 | +3.3 | +1.5 | 1619 |
| 13 | DEN | +1.5 | +0.1 | +1.4 | +0.1 | 1647 |
| 14 | HOU | +1.5 | -0.1 | +1.2 | +0.3 | 1541 |
| 15 | BAL | +0.4 | +1.3 | -0.1 | -0.9 | 1477 |
| 16 | DAL | +0.3 | +3.2 | -2.8 | -0.1 | 1467 |
| 17 | TB | +0.2 | -2.3 | +2.1 | +0.3 | 1494 |
| 18 | PIT | -0.6 | -0.5 | +0.2 | -0.2 | 1576 |
| 19 | NYG | -0.8 | -0.8 | +0.1 | -0.1 | 1486 |
| 20 | CAR | -1.1 | +0.4 | -1.4 | -0.1 | 1427 |
| 21 | WAS | -1.8 | -0.5 | -1.4 | +0.1 | 1428 |
| 22 | IND | -2.1 | -1.4 | -1.3 | +0.6 | 1389 |
| 23 | PHI | -2.4 | -3.1 | +0.5 | +0.1 | 1397 |
| 24 | NO | -3.3 | -1.6 | -0.8 | -0.9 | 1419 |
| 25 | CLE | -3.3 | -4.4 | +1.0 | +0.1 | 1444 |
| 26 | NYJ | -3.4 | -1.9 | -2.0 | +0.6 | 1335 |
| 27 | ATL | -3.4 | -1.9 | +0.0 | -1.6 | 1445 |
| 28 | MIA | -3.9 | -1.3 | -2.0 | -0.6 | 1367 |
| 29 | ARI | -4.6 | -1.9 | -1.5 | -1.1 | 1392 |
| 30 | LAC | -4.9 | -5.7 | +1.0 | -0.2 | 1374 |
| 31 | LV | -5.1 | -3.2 | -2.0 | +0.0 | 1409 |
| 32 | TEN | -6.1 | -3.4 | -2.6 | -0.0 | 1309 |

## Current model fit

- Fitted on 1828 games from seasons 2020–2026.
- Home field: 1.5 points (2.0 in divisional games).
- QB adjustment: 0.85 points per point of QB value gap.
- Special teams: 0.44 points per point of net special-teams EPA.
- Weight on the betting line: 90% for the margin, 97% for the total.
- Wind: -0.20 total points per mph above 10 mph at open-air stadiums.
