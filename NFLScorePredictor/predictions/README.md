# NFL score predictions

Updated Wed Nov 04, 2026 03:26 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the final prediction, the model blended with the line: its expected points are run through the score simulator against the posted lines, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV, its chance of winning and its stake. Stakes are a 25% share of the Kelly stake, in units of 1% of the bankroll, with at most 3 units on one game. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers (the spread and total columns) often sit several points from the line, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. See the backtest for how they have done on past seasons; the live record is tracked below.

## 2026 Week 9

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 11/05 8:15 PM | JAX @ BAL | JAX 24, BAL 16 | JAX 79% | JAX -375 / BAL +375 | 24.6 – 15.1 | 13–37 / 6–26 | JAX -5.4 / JAX -10.0 | 45.0 / 39.5 | no edge | no edge | no edge | Trevor Lawrence / Joe Fagnano |  |
| Sun 11/08 9:30 AM | CIN @ ATL | CIN 27, ATL 24 | CIN 59% | CIN -145 / ATL +145 | 27.9 – 24.5 | 16–40 / 13–37 | CIN -6.6 / CIN -3.0 | 46.7 / 52.5 | no edge | no edge | no edge | Joe Burrow / Michael Penix Jr. |  |
| Sun 11/08 1:00 PM | CLE @ NO | CLE 20, NO 23 | NO 60% | CLE +150 / NO -150 | 19.6 – 22.8 | 9–31 / 11–34 | NO -5.3 / NO -3.0 | 38.1 / 42.5 | no edge | no edge | no edge | Shedeur Sanders / Tyler Shough |  |
| Sun 11/08 1:00 PM | DAL @ IND | DAL 27, IND 24 | DAL 65% | DAL -185 / IND +185 | 28.2 – 23.3 | 16–41 / 12–35 | DAL -0.4 / DAL -5.5 | 51.4 / 51.5 | no edge | no edge | no edge | Dak Prescott / Daniel Jones |  |
| Sun 11/08 1:00 PM | DEN @ CAR | DEN 23, CAR 20 | DEN 57% | DEN -135 / CAR +135 | 23.4 – 21.1 | 12–36 / 10–34 | DEN -0.6 / DEN -2.5 | 44.9 / 44.5 | no edge | no edge | no edge | Bo Nix / Bryce Young |  |
| Sun 11/08 1:00 PM | DET @ MIA | DET 27, MIA 20 | DET 70% | DET -240 / MIA +240 | 28.5 – 21.5 | 16–41 / 10–34 | DET -6.8 / DET -7.0 | 48.6 / 50.5 | no edge | no edge | no edge | Jared Goff / Malik Willis | wind 12 mph |
| Sun 11/08 1:00 PM | LA @ WAS | LA 27, WAS 20 | LA 65% | LA -185 / WAS +185 | 26.0 – 20.8 | 13–38 / 10–33 | LA -2.6 / LA -5.5 | 47.7 / 47.5 | no edge | no edge | no edge | Matthew Stafford / Jayden Daniels | wind 13 mph |
| Sun 11/08 1:00 PM | NYG @ PHI | NYG 20, PHI 17 | NYG 61% | NYG -155 / PHI +155 | 20.5 – 17.2 | 10–31 / 7–28 | NYG -1.4 / NYG -3.5 | 37.4 / 38.5 | no edge | no edge | no edge | J.J. McCarthy / Joe Milton III | wind 13 mph |
| Sun 11/08 1:00 PM | NYJ @ KC | NYJ 20, KC 30 | KC 78% | NYJ +345 / KC -345 | 19.0 – 28.6 | 7–30 / 17–41 | KC -6.1 / KC -10.0 | 50.1 / 47.5 | no edge | no edge | no edge | Geno Smith / Patrick Mahomes |  |
| Sun 11/08 4:05 PM | HOU @ LAC | HOU 20, LAC 17 | HOU 65% | HOU -185 / LAC +185 | 22.5 – 17.9 | 10–34 / 7–29 | HOU -5.5 / HOU -4.5 | 37.2 / 40.5 | no edge | no edge | no edge | C.J. Stroud / Justin Herbert |  |
| Sun 11/08 4:05 PM | LV @ SF | LV 20, SF 30 | SF 79% | LV +375 / SF -375 | 21.2 – 31.3 | 10–33 / 20–44 | SF -11.0 / SF -10.0 | 50.9 / 52.5 | no edge | no edge | no edge | Kirk Cousins / Brock Purdy |  |
| Sun 11/08 4:25 PM | ARI @ SEA | ARI 16, SEA 24 | SEA 75% | ARI +310 / SEA -310 | 16.0 – 24.4 | 6–27 / 13–37 | SEA -7.9 / SEA -8.5 | 38.9 / 40.5 | no edge | no edge | no edge | Gardner Minshew / Drew Lock |  |
| Sun 11/08 4:25 PM | GB @ NE | GB 20, NE 23 | NE 59% | GB +145 / NE -145 | 21.7 – 24.6 | 10–34 / 13–37 | NE -1.7 / NE -3.0 | 48.6 / 46.5 | no edge | no edge | no edge | Jordan Love / Drake Maye |  |
| Sun 11/08 8:20 PM | TB @ CHI | TB 20, CHI 27 | CHI 68% | TB +215 / CHI -215 | 20.8 – 26.7 | 10–32 / 14–39 | CHI -4.9 / CHI -6.0 | 45.2 / 47.5 | no edge | no edge | no edge | Baker Mayfield / Caleb Williams |  |
| Mon 11/09 8:15 PM | BUF @ MIN | BUF 23, MIN 20 | BUF 61% | BUF -155 / MIN +155 | 24.4 – 21.1 | 13–37 / 10–33 | BUF -1.1 / BUF -3.5 | 46.2 / 45.5 | no edge | no edge | no edge | Josh Allen / Kyler Murray |  |

## 2026 Week 10

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 11/12 8:15 PM | WAS @ NYG | WAS 20, NYG 23 | NYG 54% | WAS +115 / NYG -115 | 21.4 – 22.7 | 10–33 / 12–35 | PK / NYG -1.5 | 44.6 / 44.5 | no edge | no edge | no edge | Jayden Daniels / J.J. McCarthy |  |
| Sun 11/15 9:30 AM | NE @ DET | NE 27, DET 24 | NE 55% | NE -120 / DET +120 | 25.4 – 24.1 | 13–38 / 13–36 | NE -0.1 / NE -1.5 | 50.3 / 49.5 | no edge | no edge | no edge | Drake Maye / Jared Goff |  |
| Sun 11/15 1:00 PM | BUF @ NYJ | BUF 27, NYJ 20 | BUF 71% | BUF -245 / NYJ +245 | 28.9 – 21.6 | 17–41 / 10–34 | BUF -5.6 / BUF -7.5 | 52.6 / 50.5 | no edge | no edge | no edge | Josh Allen / Geno Smith |  |
| Sun 11/15 1:00 PM | CAR @ NO | CAR 26, NO 23 | CAR 54% | CAR -115 / NO +115 | 24.4 – 23.1 | 13–37 / 12–35 | NO -0.4 / CAR -1.5 | 46.3 / 47.5 | no edge | no edge | no edge | Bryce Young / Tyler Shough |  |
| Sun 11/15 1:00 PM | HOU @ CLE | HOU 20, CLE 17 | HOU 64% | HOU -175 / CLE +175 | 21.9 – 17.7 | 10–34 / 7–29 | HOU -1.6 / HOU -4.5 | 39.9 / 39.5 | no edge | no edge | no edge | C.J. Stroud / Deshaun Watson |  |
| Sun 11/15 1:00 PM | JAX @ TEN | JAX 27, TEN 17 | JAX 77% | JAX -340 / TEN +340 | 27.4 – 18.1 | 16–41 / 7–30 | JAX -7.9 / JAX -9.5 | 45.7 / 45.5 | no edge | no edge | no edge | Trevor Lawrence / Cam Ward |  |
| Sun 11/15 1:00 PM | KC @ ATL | KC 23, ATL 20 | KC 61% | KC -155 / ATL +155 | 24.8 – 21.6 | 13–37 / 10–33 | KC -5.0 / KC -3.0 | 44.8 / 46.5 | no edge | no edge | no edge | Patrick Mahomes / Michael Penix Jr. |  |
| Sun 11/15 1:00 PM | MIA @ IND | MIA 20, IND 23 | IND 58% | MIA +140 / IND -140 | 20.4 – 23.1 | 10–32 / 12–35 | IND -4.5 / IND -2.5 | 45.3 / 43.5 | no edge | no edge | no edge | Malik Willis / Daniel Jones |  |
| Sun 11/15 1:00 PM | MIN @ GB | MIN 20, GB 23 | GB 58% | MIN +135 / GB -135 | 19.5 – 22.0 | 9–31 / 10–34 | GB -1.7 / GB -2.5 | 41.8 / 41.5 | no edge | no edge | no edge | Kyler Murray / Jordan Love |  |
| Sun 11/15 4:05 PM | LA @ ARI | LA 27, ARI 20 | LA 71% | LA -250 / ARI +250 | 27.4 – 20.1 | 16–40 / 9–31 | LA -5.6 / LA -7.5 | 45.8 / 47.5 | no edge | no edge | no edge | Matthew Stafford / Gardner Minshew |  |
| Sun 11/15 4:05 PM | SEA @ LV | SEA 23, LV 20 | SEA 66% | SEA -200 / LV +200 | 23.4 – 18.0 | 13–36 / 7–29 | SEA -5.3 / – | 41.4 / – | no line yet | no line yet | no line yet | Sam Darnold / Kirk Cousins |  |
| Sun 11/15 4:25 PM | SF @ DAL | SF 27, DAL 24 | SF 60% | SF -155 / DAL +155 | 28.5 – 25.1 | 16–41 / 13–38 | SF -3.0 / SF -3.5 | 56.7 / 53.5 | no edge | no edge | no edge | Brock Purdy / Dak Prescott |  |
| Sun 11/15 8:20 PM | PIT @ CIN | PIT 24, CIN 27 | CIN 61% | PIT +155 / CIN -155 | 22.0 – 25.5 | 10–34 / 13–38 | CIN -3.4 / CIN -3.5 | 50.0 / 47.5 | no edge | no edge | no edge | Aaron Rodgers / Joe Burrow |  |
| Mon 11/16 8:15 PM | LAC @ BAL | LAC 17, BAL 20 | BAL 57% | LAC +135 / BAL -135 | 18.3 – 20.2 | 7–30 / 10–31 | BAL -5.1 / BAL -1.5 | 37.7 / 38.5 | no edge | no edge | no edge | Justin Herbert / Tyler Huntley |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 121 | 9.58 | 10.66 | 7.35 | 65.8% | 0.224 | 84.3% |
| Model only (before blending) | 121 | 9.57 | 11.12 | 7.48 | 64.2% | – | – |
| Betting line when predicted | 121 | 9.59 | 10.65 | 7.34 | 65.8% | – | – |

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

### Week 8 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| CAR @ GB | 20–23 | 19–27 | 61% | yes |
| ARI @ DAL | 24–30 | 33–30 | 30% | yes |
| ATL @ TB | 20–23 | 0–16 | 58% | no |
| BAL @ BUF | 27–30 | 10–36 | 60% | no |
| CLE @ PIT | 17–20 | 6–27 | 61% | no |
| IND @ JAX | 17–27 | 7–42 | 78% | no |
| LV @ NYJ | 20–23 | 38–33 | 45% | no |
| MIN @ DET | 21–24 | 15–19 | 58% | yes |
| TEN @ CIN | 17–31 | 36–43 | 84% | no |
| LAC @ LA | 20–27 | 9–24 | 70% | yes |
| KC @ DEN | 23–20 | 24–28 | 46% | yes |
| NE @ MIA | 23–17 | 24–19 | 71% | yes |
| PHI @ WAS | 17–23 | 10–27 | 68% | yes |
| CHI @ SEA | 20–23 | 34–17 | 40% | yes |

## Power ratings

Points per game better than an average team on a neutral field, from opponent-adjusted EPA with this season's games weighted against a preseason prior. Defense is positive when it holds opponents below average.

| # | Team | Net | Offense | Defense | Special teams | Elo |
|---|---|---|---|---|---|---|
| 1 | BUF | +5.6 | +5.3 | -0.7 | +1.1 | 1669 |
| 2 | JAX | +4.7 | +2.8 | +1.3 | +0.5 | 1621 |
| 3 | CHI | +4.5 | +2.8 | +0.3 | +1.4 | 1622 |
| 4 | SF | +3.6 | +4.4 | +0.0 | -0.8 | 1624 |
| 5 | SEA | +3.6 | -1.0 | +3.1 | +1.4 | 1628 |
| 6 | NE | +3.5 | +2.5 | +0.9 | +0.1 | 1607 |
| 7 | DET | +3.5 | +2.7 | -0.7 | +1.5 | 1582 |
| 8 | LA | +3.1 | +2.8 | +1.9 | -1.6 | 1590 |
| 9 | GB | +2.3 | +2.3 | +1.0 | -0.9 | 1539 |
| 10 | KC | +1.9 | +2.8 | +0.1 | -1.0 | 1554 |
| 11 | MIN | +1.7 | -3.1 | +3.4 | +1.5 | 1619 |
| 12 | DEN | +1.5 | -0.1 | +1.7 | -0.1 | 1637 |
| 13 | BAL | +1.4 | +2.0 | +0.1 | -0.7 | 1502 |
| 14 | CIN | +1.4 | +2.6 | -1.5 | +0.3 | 1571 |
| 15 | HOU | +0.7 | -0.7 | +1.0 | +0.4 | 1517 |
| 16 | TB | +0.6 | -1.7 | +1.9 | +0.4 | 1501 |
| 17 | DAL | -0.1 | +2.8 | -3.2 | +0.3 | 1451 |
| 18 | PIT | -0.5 | -0.5 | +0.2 | -0.2 | 1576 |
| 19 | CAR | -1.2 | +0.0 | -1.3 | +0.1 | 1437 |
| 20 | NYG | -1.4 | -0.8 | -0.4 | -0.1 | 1464 |
| 21 | WAS | -1.6 | -0.5 | -1.4 | +0.3 | 1443 |
| 22 | IND | -1.8 | -0.9 | -1.1 | +0.2 | 1405 |
| 23 | PHI | -1.8 | -2.4 | +0.4 | +0.2 | 1420 |
| 24 | NYJ | -3.0 | -1.4 | -1.7 | +0.2 | 1346 |
| 25 | ATL | -3.1 | -2.5 | +0.7 | -1.3 | 1464 |
| 26 | NO | -3.1 | -1.6 | -0.9 | -0.6 | 1413 |
| 27 | CLE | -3.2 | -4.1 | +1.1 | -0.2 | 1450 |
| 28 | MIA | -3.6 | -0.9 | -2.1 | -0.6 | 1380 |
| 29 | LAC | -4.3 | -5.5 | +1.5 | -0.3 | 1398 |
| 30 | ARI | -4.4 | -1.8 | -1.4 | -1.2 | 1400 |
| 31 | LV | -4.4 | -2.6 | -1.7 | -0.2 | 1420 |
| 32 | TEN | -6.1 | -3.5 | -2.5 | -0.1 | 1309 |

## Current model fit

- Fitted on 1814 games from seasons 2020–2026.
- Home field: 1.5 points (2.0 in divisional games).
- QB adjustment: 0.84 points per point of QB value gap.
- Special teams: 0.44 points per point of net special-teams EPA.
- Weight on the betting line: 90% for the margin, 98% for the total.
- Wind: -0.20 total points per mph above 10 mph at open-air stadiums.
