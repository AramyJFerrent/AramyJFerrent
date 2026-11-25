# NFL score predictions

Updated Wed Nov 25, 2026 05:30 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the final prediction, the model blended with the line: its expected points are run through the score simulator against the posted lines, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV, its chance of winning and its stake. Stakes are a 25% share of the Kelly stake, in units of 1% of the bankroll, with at most 3 units on one game. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers (the spread and total columns) often sit several points from the line, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. See the backtest for how they have done on past seasons; the live record is tracked below.

## 2026 Week 12

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wed 11/25 8:00 PM | GB @ LA | GB 20, LA 23 | LA 59% | GB +145 / LA -145 | 20.5 – 23.1 | 10–31 / 12–35 | LA -3.7 / LA -2.5 | 47.8 / 43.5 | no edge | no edge | no edge | Jordan Love / Matthew Stafford |  |
| Thu 11/26 1:00 PM | CHI @ DET | CHI 30, DET 27 | CHI 54% | CHI -120 / DET +120 | 28.3 – 27.1 | 16–41 / 15–40 | DET -2.3 / CHI -1.5 | 50.6 / 55.5 | no edge | no edge | no edge | Caleb Williams / Jared Goff |  |
| Thu 11/26 4:30 PM | PHI @ DAL | PHI 20, DAL 27 | DAL 76% | PHI +310 / DAL -310 | 19.6 – 27.9 | 9–31 / 16–41 | DAL -6.5 / DAL -8.5 | 45.6 / 47.5 | no edge | no edge | no edge | Joe Milton III / Dak Prescott |  |
| Thu 11/26 8:20 PM | KC @ BUF | KC 20, BUF 23 | BUF 61% | KC +155 / BUF -155 | 20.7 – 23.8 | 10–33 / 13–37 | BUF -3.9 / BUF -3.0 | 52.6 / 46.5 | no edge | no edge | Under 46.5 (-111): EV +7.7%, 57%, stake 2.1u | Patrick Mahomes / Josh Allen | wind 21 mph |
| Fri 11/27 3:00 PM | DEN @ PIT | DEN 20, PIT 17 | DEN 61% | DEN -160 / PIT +160 | 19.9 – 16.3 | 9–31 / 6–27 | DEN -5.1 / DEN -3.5 | 39.7 / 36.5 | no edge | no edge | no edge | Bo Nix / Mason Rudolph | wind 12 mph |
| Sun 11/29 1:00 PM | ATL @ MIN | ATL 17, MIN 23 | MIN 71% | ATL +245 / MIN -245 | 17.2 – 24.2 | 6–28 / 13–37 | MIN -7.6 / MIN -7.0 | 38.9 / 41.5 | no edge | no edge | no edge | Michael Penix Jr. / Kirk Cousins |  |
| Sun 11/29 1:00 PM | BAL @ HOU | BAL 20, HOU 27 | HOU 69% | BAL +230 / HOU -230 | 20.5 – 26.9 | 10–32 / 15–39 | HOU -5.9 / HOU -6.5 | 44.2 / 47.5 | no edge | no edge | no edge | Jacoby Brissett / C.J. Stroud |  |
| Sun 11/29 1:00 PM | NO @ CIN | NO 20, CIN 27 | CIN 78% | NO +355 / CIN -355 | 19.7 – 29.5 | 9–31 / 17–42 | CIN -7.5 / CIN -10.0 | 50.2 / 49.5 | no edge | no edge | no edge | Tyler Shough / Joe Burrow |  |
| Sun 11/29 1:00 PM | NYG @ IND | NYG 23, IND 17 | NYG 68% | NYG -215 / IND +215 | 23.7 – 17.7 | 13–36 / 7–29 | NYG -0.1 / NYG -6.5 | 40.5 / 41.5 | no edge | no edge | no edge | J.J. McCarthy / Anthony Richardson |  |
| Sun 11/29 1:00 PM | NYJ @ MIA | NYJ 20, MIA 17 | NYJ 61% | NYJ -155 / MIA +155 | 22.0 – 18.6 | 10–34 / 9–30 | NYJ -3.0 / NYJ -3.5 | 43.5 / 40.5 | no edge | no edge | no edge | Geno Smith / Kyle McCord |  |
| Sun 11/29 1:00 PM | TEN @ JAX | TEN 17, JAX 31 | JAX 88% | TEN +715 / JAX -715 | 17.0 – 31.4 | 6–28 / 19–44 | JAX -12.7 / JAX -14.5 | 45.9 / 48.5 | no edge | no edge | no edge | Cam Ward / Trevor Lawrence |  |
| Sun 11/29 4:05 PM | NE @ LAC | NE 20, LAC 17 | NE 57% | NE -130 / LAC +130 | 18.8 – 16.9 | 9–30 / 7–28 | NE -5.8 / NE -1.5 | 42.9 / 35.5 | no edge | no edge | no edge | Drake Maye / Justin Herbert |  |
| Sun 11/29 4:25 PM | SEA @ SF | SEA 20, SF 23 | SF 57% | SEA +135 / SF -135 | 21.0 – 23.5 | 10–33 / 12–35 | SF -2.7 / SF -2.5 | 48.9 / 44.5 | no edge | no edge | no edge | Sam Darnold / Brock Purdy |  |
| Sun 11/29 4:25 PM | WAS @ ARI | WAS 24, ARI 17 | WAS 71% | WAS -240 / ARI +240 | 24.2 – 17.5 | 13–37 / 7–28 | WAS -2.8 / WAS -7.0 | 46.6 / 41.5 | no edge | no edge | no edge | Jayden Daniels / Gardner Minshew |  |
| Sun 11/29 8:20 PM | LV @ CLE | LV 17, CLE 20 | CLE 66% | LV +195 / CLE -195 | 17.1 – 22.1 | 7–28 / 10–34 | CLE -9.6 / CLE -4.5 | 37.7 / 39.5 | no edge | no edge | no edge | Fernando Mendoza / Deshaun Watson |  |
| Mon 11/30 8:15 PM | CAR @ TB | CAR 20, TB 23 | TB 59% | CAR +145 / TB -145 | 20.2 – 23.3 | 10–32 / 12–35 | TB -3.3 / TB -3.0 | 43.9 / 43.5 | no edge | no edge | no edge | Bryce Young / Baker Mayfield |  |

## 2026 Week 13

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 12/03 8:15 PM | KC @ LA | KC 20, LA 23 | LA 55% | KC +120 / LA -120 | 22.0 – 23.6 | 10–34 / 12–35 | LA -2.2 / LA -1.5 | 49.7 / 45.5 | no edge | no edge | no edge | Patrick Mahomes / Matthew Stafford |  |
| Sun 12/06 1:00 PM | CIN @ CLE | CIN 27, CLE 20 | CIN 67% | CIN -205 / CLE +205 | 26.1 – 20.4 | 14–38 / 10–32 | CIN -3.1 / CIN -6.0 | 47.9 / 46.5 | no edge | no edge | no edge | Joe Burrow / Deshaun Watson |  |
| Sun 12/06 1:00 PM | DET @ ATL | DET 27, ATL 24 | DET 62% | DET -165 / ATL +165 | 26.6 – 22.8 | 15–39 / 10–34 | DET -7.8 / DET -3.5 | 46.5 / 49.5 | no edge | no edge | no edge | Jared Goff / Michael Penix Jr. |  |
| Sun 12/06 1:00 PM | GB @ NO | GB 27, NO 20 | GB 67% | GB -200 / NO +200 | 25.9 – 20.5 | 14–38 / 10–33 | GB -4.4 / GB -5.5 | 45.8 / 46.5 | no edge | no edge | no edge | Jordan Love / Tyler Shough |  |
| Sun 12/06 1:00 PM | JAX @ CHI | JAX 24, CHI 27 | CHI 59% | JAX +140 / CHI -140 | 23.3 – 26.2 | 11–35 / 14–38 | CHI -1.8 / CHI -3.0 | 47.5 / 49.5 | no edge | no edge | no edge | Trevor Lawrence / Caleb Williams |  |
| Sun 12/06 1:00 PM | LAC @ TB | LAC 17, TB 20 | TB 67% | LAC +205 / TB -205 | 17.5 – 23.0 | 7–29 / 10–35 | TB -5.3 / TB -5.5 | 39.0 / 40.5 | no edge | no edge | no edge | Justin Herbert / Baker Mayfield |  |
| Sun 12/06 1:00 PM | SF @ NYG | SF 27, NYG 20 | SF 70% | SF -235 / NYG +235 | 27.0 – 20.5 | 16–40 / 10–32 | SF -6.7 / SF -6.5 | 49.9 / 47.5 | no edge | no edge | no edge | Brock Purdy / J.J. McCarthy |  |
| Sun 12/06 1:00 PM | WAS @ TEN | WAS 27, TEN 24 | WAS 64% | WAS -180 / TEN +180 | 26.0 – 21.5 | 14–38 / 10–34 | WAS -4.0 / WAS -4.5 | 46.7 / 47.5 | no edge | no edge | no edge | Jayden Daniels / Cam Ward |  |
| Sun 12/06 4:05 PM | MIA @ DEN | MIA 13, DEN 27 | DEN 89% | MIA +815 / DEN -815 | 12.6 – 26.9 | 3–23 / 15–40 | DEN -11.5 / DEN -14.5 | 40.4 / 39.5 | no edge | no edge | no edge | Kyle McCord / Bo Nix |  |
| Sun 12/06 4:05 PM | PHI @ ARI | PHI 20, ARI 17 | PHI 59% | PHI -145 / ARI +145 | 19.7 – 16.9 | 9–31 / 6–27 | PHI -0.2 / PHI -3.0 | 38.5 / 36.5 | no edge | no edge | no edge | Joe Milton III / Gardner Minshew |  |
| Sun 12/06 4:25 PM | BUF @ NE | BUF 27, NE 17 | BUF 83% | BUF -480 / NE +480 | 28.2 – 16.5 | 16–41 / 6–27 | BUF -2.9 / BUF -12.5 | 51.1 / 44.5 | no edge | NE (+549): EV +4.0%, 16%, stake 0.2u | no edge | Josh Allen / Drake Maye |  |
| Sun 12/06 4:25 PM | CAR @ MIN | CAR 20, MIN 23 | MIN 67% | CAR +205 / MIN -205 | 18.9 – 24.5 | 9–30 / 13–37 | MIN -6.7 / MIN -5.5 | 42.3 / 43.5 | no edge | no edge | no edge | Bryce Young / Kirk Cousins |  |
| Sun 12/06 8:20 PM | HOU @ PIT | HOU 23, PIT 20 | HOU 61% | HOU -160 / PIT +160 | 22.5 – 18.9 | 10–34 / 7–30 | HOU -4.9 / HOU -3.5 | 39.6 / 41.5 | no edge | no edge | no edge | C.J. Stroud / Mason Rudolph |  |
| Mon 12/07 8:15 PM | DAL @ SEA | DAL 24, SEA 27 | SEA 68% | DAL +215 / SEA -215 | 22.3 – 28.2 | 10–34 / 16–41 | SEA -4.4 / SEA -6.0 | 49.1 / 50.5 | no edge | no edge | no edge | Dak Prescott / Sam Darnold |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 163 | 9.44 | 10.45 | 7.26 | 68.5% | 0.209 | 84.7% |
| Model only (before blending) | 163 | 9.55 | 10.88 | 7.41 | 69.8% | – | – |
| Betting line when predicted | 163 | 9.43 | 10.44 | 7.26 | 68.5% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin by about 10 points per game.

80 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines and actual starters, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

Every edge logged with the last prediction before kickoff, graded at the price and stake logged with it (live predictions only; backfilled games, and edges logged before edges were priced from the final prediction, are left out). Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised.

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 2 | 0-2-0 | 0.4 | -0.39 | -100.0% | +5.1% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread line moved toward the model's early spread edge before kickoff: 5 of 7 games (71%). Lines moving toward the edge (closing line value) is the quickest sign that the model knows something the market doesn't yet.

### Week 11 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| IND @ HOU | 17–27 | 3–26 | 83% | no |
| ARI @ KC | 13–27 | 7–34 | 90% | yes |
| BAL @ CAR | 20–23 | 33–35 | 59% | no |
| MIA @ BUF | 13–30 | 9–26 | 91% | yes |
| NO @ CHI | 20–30 | 13–21 | 82% | yes |
| TB @ DET | 20–23 | 21–31 | 65% | yes |
| TEN @ DAL | 24–30 | 30–51 | 71% | no |
| NYJ @ LAC | 20–23 | 27–24 | 42% | yes |
| JAX @ NYG | 27–20 | 18–23 | 32% | yes |
| LV @ DEN | 17–27 | 24–38 | 81% | yes |
| PIT @ PHI | 20–17 | 16–19 | 39% | yes |
| MIN @ SF | 20–23 | 10–35 | 60% | yes |
| CIN @ WAS | 30–24 | 20–22 | 33% | yes |

## Power ratings

Points per game better than an average team on a neutral field, from opponent-adjusted EPA with this season's games weighted against a preseason prior. Defense is positive when it holds opponents below average.

| # | Team | Net | Offense | Defense | Special teams | Elo |
|---|---|---|---|---|---|---|
| 1 | BUF | +5.8 | +4.6 | +0.5 | +0.6 | 1709 |
| 2 | SF | +5.5 | +5.7 | +0.2 | -0.4 | 1677 |
| 3 | JAX | +4.6 | +2.4 | +1.6 | +0.7 | 1627 |
| 4 | DET | +4.5 | +3.6 | -0.2 | +1.1 | 1636 |
| 5 | LA | +4.0 | +3.3 | +2.0 | -1.3 | 1622 |
| 6 | SEA | +3.8 | -0.1 | +3.1 | +0.8 | 1647 |
| 7 | CHI | +3.8 | +1.8 | +0.6 | +1.4 | 1636 |
| 8 | KC | +2.9 | +3.2 | +1.0 | -1.3 | 1600 |
| 9 | CIN | +2.1 | +3.4 | -1.6 | +0.3 | 1599 |
| 10 | DEN | +2.1 | +0.3 | +1.6 | +0.2 | 1655 |
| 11 | HOU | +2.0 | -0.2 | +1.6 | +0.6 | 1541 |
| 12 | GB | +1.6 | +2.0 | +0.5 | -0.9 | 1546 |
| 13 | NE | +1.5 | +1.3 | +0.1 | +0.1 | 1537 |
| 14 | MIN | +1.3 | -3.2 | +3.1 | +1.4 | 1595 |
| 15 | DAL | +0.2 | +3.5 | -3.3 | +0.0 | 1468 |
| 16 | BAL | +0.2 | +1.3 | -0.3 | -0.9 | 1446 |
| 17 | TB | -0.3 | -1.8 | +1.1 | +0.3 | 1482 |
| 18 | NYG | -0.4 | -0.6 | +0.2 | -0.0 | 1494 |
| 19 | CAR | -1.2 | -0.1 | -0.9 | -0.2 | 1453 |
| 20 | WAS | -1.2 | -0.3 | -1.3 | +0.3 | 1463 |
| 21 | PIT | -1.3 | -1.2 | -0.0 | -0.0 | 1533 |
| 22 | PHI | -1.3 | -2.5 | +1.2 | -0.0 | 1416 |
| 23 | IND | -2.2 | -1.8 | -0.8 | +0.4 | 1382 |
| 24 | CLE | -2.9 | -4.0 | +1.0 | +0.1 | 1460 |
| 25 | NO | -3.3 | -2.2 | -0.3 | -0.8 | 1397 |
| 26 | ATL | -3.3 | -2.2 | -0.2 | -0.9 | 1421 |
| 27 | NYJ | -3.5 | -1.5 | -2.4 | +0.4 | 1347 |
| 28 | LAC | -4.0 | -4.0 | +0.3 | -0.2 | 1376 |
| 29 | MIA | -4.5 | -2.2 | -1.4 | -0.9 | 1354 |
| 30 | ARI | -5.1 | -2.2 | -1.9 | -1.0 | 1363 |
| 31 | LV | -5.3 | -3.3 | -2.1 | +0.0 | 1391 |
| 32 | TEN | -6.2 | -3.2 | -3.0 | +0.0 | 1287 |

## Current model fit

- Fitted on 1856 games from seasons 2020–2026.
- Home field: 1.5 points (1.9 in divisional games).
- QB adjustment: 0.85 points per point of QB value gap.
- Special teams: 0.44 points per point of net special-teams EPA.
- Weight on the betting line: 92% for the margin, 97% for the total.
- Wind: -0.20 total points per mph above 10 mph at open-air stadiums.
