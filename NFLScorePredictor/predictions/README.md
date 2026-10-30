# NFL score predictions

Updated Thu Oct 29, 2026 10:34 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the final prediction, the model blended with the line: its expected points are run through the score simulator against the posted lines, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV, its chance of winning and its stake. Stakes are a 25% share of the Kelly stake, in units of 1% of the bankroll, with at most 3 units on one game. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers (the spread and total columns) often sit several points from the line, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. See the backtest for how they have done on past seasons; the live record is tracked below.

## 2026 Week 8

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun 11/01 1:00 PM | ARI @ DAL | ARI 24, DAL 30 | DAL 71% | ARI +240 / DAL -240 | 23.8 – 30.6 | 13–36 / 19–43 | DAL -5.1 / DAL -7.0 | 51.5 / 54.5 | no edge | no edge | no edge | Jacoby Brissett / Dak Prescott |  |
| Sun 11/01 1:00 PM | ATL @ TB | ATL 20, TB 23 | TB 58% | ATL +135 / TB -135 | 20.6 – 23.3 | 10–33 / 12–35 | TB -4.9 / TB -2.5 | 40.8 / 44.5 | no edge | no edge | no edge | Michael Penix Jr. / Baker Mayfield | wind 13 mph |
| Sun 11/01 1:00 PM | BAL @ BUF | BAL 27, BUF 30 | BUF 61% | BAL +155 / BUF -155 | 25.5 – 29.0 | 13–38 / 17–41 | BUF -8.8 / BUF -3.0 | 52.6 / 54.5 | no edge | no edge | no edge | Tyler Huntley / Josh Allen |  |
| Sun 11/01 1:00 PM | CLE @ PIT | CLE 17, PIT 20 | PIT 61% | CLE +155 / PIT -155 | 18.1 – 21.5 | 7–30 / 10–33 | PIT -2.5 / PIT -3.5 | 40.1 / 39.5 | no edge | no edge | no edge | Deshaun Watson / Aaron Rodgers |  |
| Sun 11/01 1:00 PM | IND @ JAX | IND 17, JAX 27 | JAX 78% | IND +365 / JAX -365 | 18.1 – 27.9 | 7–30 / 16–41 | JAX -8.1 / JAX -10.0 | 47.1 / 46.5 | no edge | no edge | no edge | Daniel Jones / Trevor Lawrence | wind 13 mph |
| Sun 11/01 1:00 PM | LV @ NYJ | LV 20, NYJ 23 | NYJ 56% | LV +125 / NYJ -125 | 21.9 – 23.6 | 10–34 / 13–36 | NYJ -3.1 / NYJ -1.5 | 44.2 / 45.5 | no edge | no edge | no edge | Kirk Cousins / Geno Smith |  |
| Sun 11/01 1:00 PM | MIN @ DET | MIN 20, DET 23 | DET 58% | MIN +140 / DET -140 | 21.8 – 24.7 | 10–34 / 13–37 | DET -1.8 / DET -3.0 | 43.9 / 46.5 | no edge | no edge | no edge | Kyler Murray / Jared Goff |  |
| Sun 11/01 1:00 PM | TEN @ CIN | TEN 17, CIN 27 | CIN 83% | TEN +475 / CIN -475 | 17.5 – 29.0 | 7–28 / 17–42 | CIN -11.5 / CIN -11.5 | 47.2 / 46.5 | no edge | no edge | no edge | Cam Ward / Joe Burrow |  |
| Sun 11/01 4:05 PM | LAC @ LA | LAC 20, LA 26 | LA 70% | LAC +230 / LA -230 | 19.5 – 26.0 | 9–31 / 14–38 | LA -6.5 / LA -6.5 | 41.3 / 45.5 | no edge | no edge | no edge | Justin Herbert / Matthew Stafford |  |
| Sun 11/01 4:25 PM | KC @ DEN | KC 23, DEN 20 | KC 54% | KC -120 / DEN +120 | 20.9 – 19.6 | 10–33 / 9–31 | DEN -0.5 / KC -1.5 | 45.6 / 40.5 | no edge | no edge | no edge | Patrick Mahomes / Bo Nix |  |
| Sun 11/01 4:25 PM | NE @ MIA | NE 24, MIA 17 | NE 71% | NE -250 / MIA +250 | 24.8 – 17.9 | 13–37 / 7–30 | NE -6.1 / NE -7.0 | 47.2 / 43.5 | no edge | no edge | no edge | Drake Maye / Malik Willis | wind 14 mph |
| Sun 11/01 8:20 PM | PHI @ WAS | PHI 17, WAS 23 | WAS 68% | PHI +215 / WAS -215 | 17.5 – 23.1 | 7–28 / 12–35 | WAS -2.0 / WAS -6.0 | 44.9 / 40.5 | no edge | no edge | no edge | Jalen Hurts / Jayden Daniels |  |
| Mon 11/02 8:15 PM | CHI @ SEA | CHI 20, SEA 23 | SEA 60% | CHI +145 / SEA -145 | 21.8 – 24.7 | 10–34 / 13–37 | SEA -1.5 / SEA -3.0 | 43.1 / 46.5 | no edge | no edge | no edge | Caleb Williams / Sam Darnold |  |

## 2026 Week 9

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 11/05 8:15 PM | JAX @ BAL | JAX 24, BAL 27 | BAL 58% | JAX +135 / BAL -135 | 23.0 – 25.5 | 12–35 / 13–38 | JAX -2.8 / BAL -3.0 | 47.0 / 48.5 | no edge | no edge | no edge | T.Lawrence / T.Huntley |  |
| Sun 11/08 9:30 AM | CIN @ ATL | CIN 27, ATL 24 | CIN 60% | CIN -150 / ATL +150 | 26.4 – 23.1 | 14–38 / 12–35 | CIN -5.6 / CIN -3.0 | 47.1 / 49.5 | no edge | no edge | no edge | J.Burrow / M.Penix |  |
| Sun 11/08 1:00 PM | CLE @ NO | CLE 20, NO 23 | NO 58% | CLE +135 / NO -135 | 20.5 – 22.9 | 10–32 / 12–35 | NO -1.7 / NO -2.5 | 40.8 / 43.5 | no edge | no edge | no edge | D.Watson / T.Shough |  |
| Sun 11/08 1:00 PM | DAL @ IND | DAL 27, IND 24 | DAL 61% | DAL -160 / IND +160 | 27.8 – 23.8 | 16–40 / 13–36 | IND -0.8 / DAL -4.5 | 52.0 / 51.5 | no edge | no edge | no edge | D.Prescott / D.Jones |  |
| Sun 11/08 1:00 PM | DEN @ CAR | DEN 20, CAR 23 | DEN 50% | DEN -100 / CAR +100 | 22.3 – 22.2 | 10–34 / 10–34 | PK / – | 44.5 / – | no line yet | no line yet | no line yet | B.Nix / B.Young |  |
| Sun 11/08 1:00 PM | DET @ MIA | DET 27, MIA 20 | DET 70% | DET -235 / MIA +235 | 27.7 – 20.8 | 16–41 / 10–33 | DET -6.3 / DET -7.0 | 49.0 / 48.5 | no edge | no edge | no edge | J.Goff / M.Willis |  |
| Sun 11/08 1:00 PM | LA @ WAS | LA 27, WAS 24 | LA 65% | LA -190 / WAS +190 | 26.9 – 21.6 | 15–40 / 10–34 | LA -3.0 / LA -5.5 | 48.6 / 48.5 | no edge | no edge | no edge | M.Stafford / J.Daniels |  |
| Sun 11/08 1:00 PM | NYG @ PHI | NYG 20, PHI 17 | NYG 55% | NYG -120 / PHI +120 | 21.0 – 19.5 | 10–33 / 9–31 | NYG -1.1 / NYG -1.5 | 36.9 / 40.5 | no edge | no edge | no edge | J.McCarthy / T.McKee |  |
| Sun 11/08 1:00 PM | NYJ @ KC | NYJ 17, KC 27 | KC 77% | NYJ +335 / KC -335 | 17.2 – 26.4 | 7–28 / 14–38 | KC -6.3 / KC -9.5 | 48.0 / 43.5 | no edge | no edge | no edge | G.Smith / P.Mahomes |  |
| Sun 11/08 4:05 PM | HOU @ LAC | HOU 23, LAC 20 | HOU 61% | HOU -160 / LAC +160 | 23.0 – 19.4 | 12–35 / 9–31 | HOU -4.5 / HOU -3.5 | 38.2 / 42.5 | no edge | no edge | no edge | C.Stroud / J.Herbert |  |
| Sun 11/08 4:05 PM | LV @ SF | LV 20, SF 27 | SF 78% | LV +350 / SF -350 | 19.4 – 29.1 | 9–31 / 17–42 | SF -11.3 / SF -9.5 | 49.4 / 48.5 | no edge | no edge | no edge | K.Cousins / B.Purdy |  |
| Sun 11/08 4:25 PM | ARI @ SEA | ARI 17, SEA 27 | SEA 79% | ARI +375 / SEA -375 | 17.0 – 27.5 | 6–28 / 16–40 | SEA -10.3 / SEA -10.5 | 40.6 / 44.5 | no edge | no edge | no edge | J.Brissett / S.Darnold |  |
| Sun 11/08 4:25 PM | GB @ NE | GB 24, NE 27 | NE 55% | GB +120 / NE -120 | 23.5 – 25.1 | 13–35 / 13–37 | NE -1.6 / – | 48.6 / – | no line yet | no line yet | no line yet | J.Love / D.Maye |  |
| Sun 11/08 8:20 PM | TB @ CHI | TB 20, CHI 27 | CHI 67% | TB +210 / CHI -210 | 20.5 – 26.4 | 10–32 / 14–38 | CHI -4.7 / CHI -6.0 | 45.6 / 47.5 | no edge | no edge | no edge | B.Mayfield / C.Williams | wind 13 mph |
| Mon 11/09 8:15 PM | BUF @ MIN | BUF 27, MIN 24 | BUF 57% | BUF -135 / MIN +135 | 24.9 – 22.6 | 13–37 / 10–34 | BUF -0.4 / BUF -2.5 | 47.4 / 47.5 | no edge | no edge | no edge | J.Allen / K.Murray |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 107 | 9.40 | 10.59 | 7.21 | 65.1% | 0.229 | 85.5% |
| Model only (before blending) | 107 | 9.42 | 11.07 | 7.41 | 63.2% | – | – |
| Betting line when predicted | 107 | 9.40 | 10.57 | 7.20 | 65.1% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin by about 10 points per game.

80 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines and actual starters, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

Every edge logged with the last prediction before kickoff, graded at the price and stake logged with it (live predictions only; backfilled games, and edges logged before edges were priced from the final prediction, are left out). Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised.

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread line moved toward the model's early spread edge before kickoff: 5 of 6 games (83%). Lines moving toward the edge (closing line value) is the quickest sign that the model knows something the market doesn't yet.

### Week 7 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| NE @ CHI | 24–27 | 24–30 | 59% | yes |
| PIT @ NO | 23–20 | 16–10 | 58% | yes |
| CIN @ BAL | 27–24 | 35–13 | 56% | yes |
| CLE @ TEN | 20–17 | 27–24 | 58% | yes |
| IND @ MIN | 17–24 | 10–16 | 71% | yes |
| MIA @ NYJ | 17–20 | 28–25 | 37% | yes |
| NYG @ HOU | 17–27 | 27–21 | 21% | yes |
| SF @ ATL | 27–24 | 20–29 | 42% | yes |
| TB @ CAR | 20–23 | 43–13 | 39% | no |
| DEN @ ARI | 23–20 | 30–16 | 64% | yes |
| GB @ DET | 24–27 | 17–20 | 61% | yes |
| LA @ LV | 27–24 | 35–21 | 60% | yes |
| KC @ SEA | 20–23 | 3–20 | 59% | no |
| DAL @ PHI | 23–20 | 38–21 | 62% | no |

## Power ratings

Points per game better than an average team on a neutral field, from opponent-adjusted EPA with this season's games weighted against a preseason prior. Defense is positive when it holds opponents below average.

| # | Team | Net | Offense | Defense | Special teams | Elo |
|---|---|---|---|---|---|---|
| 1 | BUF | +5.2 | +5.7 | -1.3 | +0.8 | 1653 |
| 2 | SEA | +4.4 | -0.9 | +3.6 | +1.7 | 1671 |
| 3 | JAX | +3.8 | +2.4 | +0.9 | +0.6 | 1608 |
| 4 | SF | +3.7 | +4.3 | +0.2 | -0.8 | 1624 |
| 5 | CHI | +3.5 | +2.2 | +0.2 | +1.2 | 1580 |
| 6 | DET | +3.4 | +2.9 | -0.8 | +1.4 | 1565 |
| 7 | NE | +2.9 | +2.2 | +0.5 | +0.1 | 1598 |
| 8 | LA | +2.8 | +3.0 | +1.4 | -1.5 | 1579 |
| 9 | BAL | +2.3 | +2.9 | -0.2 | -0.5 | 1517 |
| 10 | KC | +1.9 | +2.4 | +0.3 | -0.8 | 1565 |
| 11 | GB | +1.9 | +1.9 | +0.6 | -0.5 | 1526 |
| 12 | MIN | +1.9 | -3.1 | +3.3 | +1.7 | 1636 |
| 13 | CIN | +1.8 | +2.3 | -0.7 | +0.2 | 1565 |
| 14 | DEN | +1.3 | -0.5 | +2.1 | -0.3 | 1627 |
| 15 | HOU | +0.6 | -0.8 | +1.1 | +0.3 | 1517 |
| 16 | TB | -0.1 | -1.5 | +1.1 | +0.3 | 1476 |
| 17 | DAL | -0.4 | +2.8 | -3.5 | +0.2 | 1472 |
| 18 | CAR | -0.7 | +0.7 | -1.1 | -0.3 | 1451 |
| 19 | IND | -1.0 | -0.4 | -0.8 | +0.3 | 1419 |
| 20 | PIT | -1.0 | -1.1 | +0.1 | +0.0 | 1558 |
| 21 | PHI | -1.2 | -2.2 | +0.5 | +0.5 | 1447 |
| 22 | NYG | -1.4 | -1.0 | -0.3 | -0.1 | 1464 |
| 23 | ATL | -1.9 | -1.4 | +0.6 | -1.1 | 1489 |
| 24 | WAS | -2.3 | -0.6 | -1.6 | -0.1 | 1415 |
| 25 | CLE | -2.8 | -3.9 | +1.5 | -0.5 | 1469 |
| 26 | NYJ | -3.0 | -2.2 | -1.2 | +0.5 | 1365 |
| 27 | MIA | -3.0 | -0.4 | -2.0 | -0.6 | 1390 |
| 28 | NO | -3.1 | -1.7 | -0.8 | -0.6 | 1413 |
| 29 | LAC | -3.8 | -4.6 | +1.3 | -0.4 | 1409 |
| 30 | ARI | -4.0 | -1.5 | -1.4 | -1.1 | 1379 |
| 31 | LV | -4.9 | -3.3 | -1.1 | -0.5 | 1401 |
| 32 | TEN | -6.8 | -4.6 | -2.2 | +0.0 | 1315 |

## Current model fit

- Fitted on 1800 games from seasons 2020–2026.
- Home field: 1.5 points (1.8 in divisional games).
- QB adjustment: 0.83 points per point of QB value gap.
- Special teams: 0.43 points per point of net special-teams EPA.
- Weight on the betting line: 91% for the margin, 98% for the total.
- Wind: -0.20 total points per mph above 10 mph at open-air stadiums.
