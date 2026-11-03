# NFL score predictions

Updated Mon Nov 02, 2026 10:55 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the final prediction, the model blended with the line: its expected points are run through the score simulator against the posted lines, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV, its chance of winning and its stake. Stakes are a 25% share of the Kelly stake, in units of 1% of the bankroll, with at most 3 units on one game. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers (the spread and total columns) often sit several points from the line, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. See the backtest for how they have done on past seasons; the live record is tracked below.

## 2026 Week 9

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 11/05 8:15 PM | JAX @ BAL | JAX 24, BAL 17 | JAX 75% | JAX -295 / BAL +295 | 25.3 – 17.2 | 13–38 / 7–28 | JAX -4.5 / JAX -8.5 | 45.9 / 42.5 | no edge | no edge | no edge | Trevor Lawrence / Tyler Huntley |  |
| Sun 11/08 9:30 AM | CIN @ ATL | CIN 27, ATL 24 | CIN 60% | CIN -150 / ATL +150 | 27.9 – 24.5 | 16–41 / 13–37 | CIN -6.6 / CIN -3.0 | 46.7 / 52.5 | no edge | no edge | no edge | Joe Burrow / Michael Penix Jr. |  |
| Sun 11/08 1:00 PM | CLE @ NO | CLE 20, NO 23 | NO 57% | CLE +135 / NO -135 | 20.5 – 23.0 | 10–32 / 12–35 | NO -2.4 / NO -2.5 | 41.0 / 43.5 | no edge | no edge | no edge | Deshaun Watson / Tyler Shough |  |
| Sun 11/08 1:00 PM | DAL @ IND | DAL 27, IND 24 | DAL 67% | DAL -200 / IND +200 | 28.5 – 23.0 | 16–41 / 12–35 | DAL -0.3 / DAL -6.0 | 51.4 / 51.5 | no edge | no edge | no edge | Dak Prescott / Daniel Jones |  |
| Sun 11/08 1:00 PM | DEN @ CAR | DEN 23, CAR 20 | DEN 58% | DEN -140 / CAR +140 | 23.1 – 20.4 | 12–35 / 10–32 | DEN -0.7 / DEN -3.0 | 45.0 / 43.5 | no edge | no edge | no edge | Bo Nix / Bryce Young |  |
| Sun 11/08 1:00 PM | DET @ MIA | DET 27, MIA 20 | DET 71% | DET -245 / MIA +245 | 28.6 – 21.6 | 16–41 / 10–34 | DET -6.8 / DET -7.0 | 48.6 / 50.5 | no edge | no edge | no edge | Jared Goff / Malik Willis |  |
| Sun 11/08 1:00 PM | LA @ WAS | LA 27, WAS 24 | LA 66% | LA -190 / WAS +190 | 26.4 – 21.2 | 14–38 / 10–33 | LA -2.6 / LA -5.5 | 47.7 / 47.5 | no edge | no edge | no edge | Matthew Stafford / Jayden Daniels |  |
| Sun 11/08 1:00 PM | NYG @ PHI | NYG 20, PHI 17 | NYG 62% | NYG -160 / PHI +160 | 21.9 – 18.5 | 10–34 / 7–30 | NYG -1.7 / NYG -3.5 | 37.1 / 40.5 | no edge | no edge | no edge | J.J. McCarthy / Tanner McKee |  |
| Sun 11/08 1:00 PM | NYJ @ KC | NYJ 20, KC 27 | KC 77% | NYJ +335 / KC -335 | 18.7 – 27.9 | 7–30 / 16–41 | KC -6.3 / KC -9.5 | 50.1 / 46.5 | no edge | no edge | no edge | Geno Smith / Patrick Mahomes |  |
| Sun 11/08 4:05 PM | HOU @ LAC | HOU 20, LAC 17 | HOU 65% | HOU -185 / LAC +185 | 22.5 – 17.9 | 11–34 / 7–29 | HOU -5.4 / HOU -4.5 | 37.2 / 40.5 | no edge | no edge | no edge | C.J. Stroud / Justin Herbert |  |
| Sun 11/08 4:05 PM | LV @ SF | LV 20, SF 30 | SF 80% | LV +395 / SF -395 | 20.7 – 30.8 | 10–32 / 19–44 | SF -11.0 / SF -10.0 | 51.0 / 51.5 | no edge | no edge | no edge | Kirk Cousins / Brock Purdy |  |
| Sun 11/08 4:25 PM | ARI @ SEA | ARI 13, SEA 23 | SEA 82% | ARI +455 / SEA -455 | 13.5 – 24.3 | 3–24 / 13–37 | SEA -10.7 / – | 40.5 / – | no line yet | no line yet | no line yet | Gardner Minshew / Sam Darnold | wind 15 mph |
| Sun 11/08 4:25 PM | GB @ NE | GB 20, NE 23 | NE 59% | GB +145 / NE -145 | 21.8 – 24.7 | 10–34 / 13–37 | NE -1.8 / NE -3.0 | 48.7 / 46.5 | no edge | no edge | no edge | Jordan Love / Drake Maye |  |
| Sun 11/08 8:20 PM | TB @ CHI | TB 20, CHI 23 | CHI 62% | TB +165 / CHI -165 | 20.4 – 24.3 | 10–32 / 13–37 | CHI -3.9 / – | 44.7 / – | no line yet | no line yet | no line yet | Baker Mayfield / Caleb Williams |  |
| Mon 11/09 8:15 PM | BUF @ MIN | BUF 23, MIN 20 | BUF 60% | BUF -150 / MIN +150 | 24.9 – 21.6 | 13–37 / 10–34 | BUF -1.1 / BUF -3.5 | 46.1 / 46.5 | no edge | no edge | no edge | Josh Allen / Kyler Murray |  |

## 2026 Week 10

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 11/12 8:15 PM | WAS @ NYG | WAS 20, NYG 23 | NYG 50% | WAS +100 / NYG -100 | 22.4 – 22.3 | 10–34 / 10–34 | WAS -0.1 / – | 44.7 / – | no line yet | no line yet | no line yet | J.Daniels / J.McCarthy |  |
| Sun 11/15 9:30 AM | NE @ DET | NE 27, DET 24 | NE 50% | NE -100 / DET +100 | 25.2 – 25.1 | 13–37 / 13–37 | NE -0.2 / – | 50.3 / – | no line yet | no line yet | no line yet | D.Maye / J.Goff |  |
| Sun 11/15 1:00 PM | BUF @ NYJ | BUF 30, NYJ 24 | BUF 68% | BUF -210 / NYJ +210 | 29.1 – 23.5 | 17–42 / 12–36 | BUF -5.6 / – | 52.7 / – | no line yet | no line yet | no line yet | J.Allen / G.Smith |  |
| Sun 11/15 1:00 PM | CAR @ NO | CAR 20, NO 23 | NO 51% | CAR +105 / NO -105 | 22.9 – 23.4 | 12–34 / 13–35 | NO -0.5 / – | 46.3 / – | no line yet | no line yet | no line yet | B.Young / T.Shough |  |
| Sun 11/15 1:00 PM | HOU @ CLE | HOU 20, CLE 17 | HOU 56% | HOU -125 / CLE +125 | 20.8 – 19.2 | 10–33 / 9–31 | HOU -1.6 / – | 39.9 / – | no line yet | no line yet | no line yet | C.Stroud / D.Watson |  |
| Sun 11/15 1:00 PM | JAX @ TEN | JAX 27, TEN 20 | JAX 74% | JAX -280 / TEN +280 | 26.8 – 18.9 | 15–39 / 9–31 | JAX -7.9 / – | 45.7 / – | no line yet | no line yet | no line yet | T.Lawrence / C.Ward |  |
| Sun 11/15 1:00 PM | KC @ ATL | KC 23, ATL 20 | KC 66% | KC -190 / ATL +190 | 25.0 – 19.9 | 13–37 / 9–31 | KC -5.0 / – | 44.9 / – | no line yet | no line yet | no line yet | P.Mahomes / M.Penix |  |
| Sun 11/15 1:00 PM | MIA @ IND | MIA 20, IND 23 | IND 65% | MIA +180 / IND -180 | 20.4 – 24.9 | 10–32 / 13–37 | IND -4.5 / – | 45.3 / – | no line yet | no line yet | no line yet | M.Willis / D.Jones |  |
| Sun 11/15 1:00 PM | MIN @ GB | MIN 20, GB 23 | GB 55% | MIN +125 / GB -125 | 20.1 – 21.7 | 9–31 / 10–34 | GB -1.6 / – | 41.8 / – | no line yet | no line yet | no line yet | K.Murray / J.Love |  |
| Sun 11/15 4:05 PM | LA @ ARI | LA 23, ARI 20 | LA 67% | LA -205 / ARI +205 | 25.7 – 20.0 | 13–38 / 9–31 | LA -5.7 / – | 45.6 / – | no line yet | no line yet | no line yet | M.Stafford / J.Brissett |  |
| Sun 11/15 4:05 PM | SEA @ LV | SEA 24, LV 17 | SEA 70% | SEA -230 / LV +230 | 23.8 – 17.4 | 13–36 / 7–28 | SEA -6.3 / – | 41.2 / – | no line yet | no line yet | no line yet | S.Darnold / K.Cousins |  |
| Sun 11/15 4:25 PM | SF @ DAL | SF 30, DAL 27 | SF 59% | SF -145 / DAL +145 | 29.9 – 26.9 | 17–42 / 14–39 | SF -3.1 / – | 56.8 / – | no line yet | no line yet | no line yet | B.Purdy / D.Prescott |  |
| Sun 11/15 8:20 PM | PIT @ CIN | PIT 24, CIN 27 | CIN 59% | PIT +145 / CIN -145 | 23.3 – 26.7 | 13–36 / 15–39 | CIN -3.4 / – | 50.0 / – | no line yet | no line yet | no line yet | A.Rodgers / J.Burrow |  |
| Mon 11/16 8:15 PM | LAC @ BAL | LAC 17, BAL 20 | BAL 64% | LAC +175 / BAL -175 | 16.4 – 20.5 | 6–27 / 10–32 | BAL -4.1 / – | 36.8 / – | no line yet | no line yet | no line yet | J.Herbert / J.Fagnano |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 120 | 9.49 | 10.71 | 7.32 | 66.4% | 0.223 | 84.2% |
| Model only (before blending) | 120 | 9.50 | 11.15 | 7.47 | 64.7% | – | – |
| Betting line when predicted | 120 | 9.50 | 10.70 | 7.32 | 66.4% | – | – |

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

## Power ratings

Points per game better than an average team on a neutral field, from opponent-adjusted EPA with this season's games weighted against a preseason prior. Defense is positive when it holds opponents below average.

| # | Team | Net | Offense | Defense | Special teams | Elo |
|---|---|---|---|---|---|---|
| 1 | BUF | +5.6 | +5.3 | -0.7 | +1.1 | 1669 |
| 2 | JAX | +4.7 | +2.8 | +1.4 | +0.6 | 1621 |
| 3 | SEA | +4.5 | -0.8 | +3.6 | +1.7 | 1671 |
| 4 | SF | +3.6 | +4.4 | +0.0 | -0.8 | 1624 |
| 5 | NE | +3.5 | +2.6 | +0.9 | +0.1 | 1607 |
| 6 | DET | +3.5 | +2.7 | -0.7 | +1.5 | 1582 |
| 7 | CHI | +3.4 | +2.2 | +0.1 | +1.1 | 1580 |
| 8 | LA | +3.1 | +2.8 | +1.9 | -1.6 | 1590 |
| 9 | GB | +2.3 | +2.3 | +0.9 | -0.9 | 1539 |
| 10 | KC | +2.0 | +2.8 | +0.1 | -1.0 | 1554 |
| 11 | MIN | +1.7 | -3.1 | +3.4 | +1.5 | 1619 |
| 12 | DEN | +1.6 | -0.0 | +1.7 | -0.1 | 1637 |
| 13 | BAL | +1.4 | +2.1 | +0.1 | -0.7 | 1502 |
| 14 | CIN | +1.4 | +2.6 | -1.5 | +0.3 | 1571 |
| 15 | HOU | +0.7 | -0.7 | +1.0 | +0.4 | 1517 |
| 16 | TB | +0.6 | -1.7 | +1.9 | +0.4 | 1501 |
| 17 | DAL | -0.1 | +2.8 | -3.2 | +0.3 | 1451 |
| 18 | PIT | -0.5 | -0.5 | +0.2 | -0.2 | 1576 |
| 19 | CAR | -1.2 | +0.0 | -1.4 | +0.1 | 1437 |
| 20 | NYG | -1.4 | -0.8 | -0.4 | -0.1 | 1464 |
| 21 | WAS | -1.6 | -0.4 | -1.4 | +0.3 | 1443 |
| 22 | IND | -1.8 | -0.9 | -1.1 | +0.3 | 1405 |
| 23 | PHI | -1.8 | -2.4 | +0.4 | +0.2 | 1420 |
| 24 | NYJ | -3.1 | -1.4 | -1.8 | +0.1 | 1346 |
| 25 | ATL | -3.1 | -2.5 | +0.7 | -1.3 | 1464 |
| 26 | NO | -3.2 | -1.6 | -0.9 | -0.6 | 1413 |
| 27 | CLE | -3.2 | -4.1 | +1.1 | -0.2 | 1450 |
| 28 | MIA | -3.6 | -0.9 | -2.1 | -0.6 | 1380 |
| 29 | LAC | -4.3 | -5.5 | +1.5 | -0.3 | 1398 |
| 30 | ARI | -4.4 | -1.8 | -1.4 | -1.2 | 1400 |
| 31 | LV | -4.4 | -2.6 | -1.7 | -0.2 | 1420 |
| 32 | TEN | -6.1 | -3.5 | -2.5 | -0.1 | 1309 |

## Current model fit

- Fitted on 1813 games from seasons 2020–2026.
- Home field: 1.5 points (2.0 in divisional games).
- QB adjustment: 0.84 points per point of QB value gap.
- Special teams: 0.44 points per point of net special-teams EPA.
- Weight on the betting line: 90% for the margin, 98% for the total.
- Wind: -0.20 total points per mph above 10 mph at open-air stadiums.
