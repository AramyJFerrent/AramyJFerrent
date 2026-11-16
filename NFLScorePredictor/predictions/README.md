# NFL score predictions

Updated Sun Nov 15, 2026 09:42 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the final prediction, the model blended with the line: its expected points are run through the score simulator against the posted lines, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV, its chance of winning and its stake. Stakes are a 25% share of the Kelly stake, in units of 1% of the bankroll, with at most 3 units on one game. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers (the spread and total columns) often sit several points from the line, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. See the backtest for how they have done on past seasons; the live record is tracked below.

## 2026 Week 10

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mon 11/16 8:15 PM | LAC @ BAL | LAC 17, BAL 20 | BAL 65% | LAC +185 / BAL -185 | 17.0 – 21.5 | 6–28 / 10–33 | BAL -5.0 / BAL -4.5 | 38.8 / 38.5 | no edge | no edge | no edge | Justin Herbert / Tyler Huntley |  |

## 2026 Week 11

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 11/19 8:15 PM | IND @ HOU | IND 17, HOU 27 | HOU 77% | IND +340 / HOU -340 | 17.5 – 27.0 | 7–28 / 14–40 | HOU -5.2 / HOU -10.0 | 43.4 / 44.5 | no edge | no edge | no edge | Daniel Jones / C.J. Stroud |  |
| Sun 11/22 1:00 PM | ARI @ KC | ARI 13, KC 30 | KC 90% | ARI +920 / KC -920 | 13.0 – 28.8 | 3–23 / 16–42 | KC -9.7 / KC -16.5 | 47.9 / 41.5 | no edge | ARI (+850): EV +8.9%, 11%, stake 0.3u | no edge | Gardner Minshew / Patrick Mahomes |  |
| Sun 11/22 1:00 PM | BAL @ CAR | BAL 20, CAR 23 | CAR 57% | BAL +135 / CAR -135 | 21.0 – 23.5 | 10–33 / 13–36 | CAR -2.7 / CAR -2.5 | 45.1 / 44.5 | no edge | no edge | no edge | Tyler Huntley / Bryce Young |  |
| Sun 11/22 1:00 PM | JAX @ NYG | JAX 27, NYG 20 | JAX 68% | JAX -215 / NYG +215 | 26.2 – 20.2 | 14–38 / 9–31 | JAX -5.5 / JAX -6.0 | 45.1 / 46.5 | no edge | no edge | no edge | Trevor Lawrence / J.J. McCarthy |  |
| Sun 11/22 1:00 PM | MIA @ BUF | MIA 13, BUF 30 | BUF 91% | MIA +1015 / BUF -1015 | 15.2 – 31.4 | 6–26 / 20–44 | BUF -14.1 / BUF -16.5 | 49.3 / 46.5 | no edge | no edge | no edge | Malik Willis / Josh Allen |  |
| Sun 11/22 1:00 PM | NO @ CHI | NO 20, CHI 30 | CHI 79% | NO +375 / CHI -375 | 19.1 – 29.3 | 9–31 / 17–42 | CHI -11.5 / CHI -10.0 | 46.2 / 48.5 | no edge | no edge | no edge | Tyler Shough / Caleb Williams |  |
| Sun 11/22 1:00 PM | TB @ DET | TB 20, DET 23 | DET 67% | TB +200 / DET -200 | 20.6 – 25.9 | 10–32 / 13–38 | DET -3.7 / DET -5.5 | 44.9 / 46.5 | no edge | no edge | no edge | Baker Mayfield / Jared Goff |  |
| Sun 11/22 1:00 PM | TEN @ DAL | TEN 23, DAL 30 | DAL 72% | TEN +260 / DAL -260 | 23.0 – 30.5 | 11–35 / 18–43 | DAL -7.3 / DAL -7.5 | 52.0 / 53.5 | no edge | no edge | no edge | Cam Ward / Dak Prescott |  |
| Sun 11/22 4:05 PM | NYJ @ LAC | NYJ 20, LAC 23 | LAC 59% | NYJ +145 / LAC -145 | 18.9 – 21.6 | 9–30 / 10–34 | NYJ -0.7 / LAC -3.0 | 40.5 / 40.5 | no edge | no edge | no edge | Geno Smith / Justin Herbert |  |
| Sun 11/22 4:25 PM | LV @ DEN | LV 13, DEN 23 | DEN 79% | LV +385 / DEN -385 | 14.8 – 24.7 | 6–25 / 13–38 | DEN -13.7 / DEN -9.5 | 40.2 / 39.5 | no edge | no edge | no edge | Fernando Mendoza / Bo Nix |  |
| Sun 11/22 4:25 PM | PIT @ PHI | PIT 20, PHI 17 | PIT 57% | PIT -130 / PHI +130 | 20.0 – 18.3 | 9–31 / 7–29 | PIT -1.8 / – | 38.3 / – | no line yet | no line yet | no line yet | Aaron Rodgers / Joe Milton III |  |
| Sun 11/22 8:20 PM | MIN @ SF | MIN 20, SF 23 | SF 58% | MIN +140 / SF -140 | 21.4 – 24.2 | 10–33 / 13–37 | SF -0.9 / SF -3.0 | 47.1 / 45.5 | no edge | no edge | no edge | Kirk Cousins / Brock Purdy |  |
| Mon 11/23 8:15 PM | CIN @ WAS | CIN 30, WAS 27 | CIN 58% | CIN -140 / WAS +140 | 28.2 – 25.8 | 16–41 / 13–38 | CIN -2.4 / – | 54.0 / – | no line yet | no line yet | no line yet | Joe Burrow / Jayden Daniels |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 148 | 9.53 | 10.45 | 7.29 | 68.7% | 0.212 | 84.5% |
| Model only (before blending) | 148 | 9.62 | 10.87 | 7.40 | 68.0% | – | – |
| Betting line when predicted | 148 | 9.53 | 10.45 | 7.28 | 68.7% | – | – |

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

## Power ratings

Points per game better than an average team on a neutral field, from opponent-adjusted EPA with this season's games weighted against a preseason prior. Defense is positive when it holds opponents below average.

| # | Team | Net | Offense | Defense | Special teams | Elo |
|---|---|---|---|---|---|---|
| 1 | BUF | +6.2 | +5.3 | +0.1 | +0.8 | 1705 |
| 2 | JAX | +5.8 | +3.3 | +1.7 | +0.7 | 1654 |
| 3 | SF | +5.0 | +6.0 | +0.2 | -1.2 | 1647 |
| 4 | DET | +4.9 | +3.4 | -0.0 | +1.5 | 1625 |
| 5 | CHI | +4.8 | +2.7 | +0.6 | +1.5 | 1629 |
| 6 | SEA | +4.3 | -0.1 | +3.5 | +0.9 | 1647 |
| 7 | LA | +3.9 | +3.2 | +2.5 | -1.8 | 1622 |
| 8 | MIN | +2.4 | -3.7 | +4.1 | +2.0 | 1625 |
| 9 | KC | +2.2 | +3.3 | +0.9 | -2.0 | 1589 |
| 10 | CIN | +2.2 | +3.7 | -2.0 | +0.5 | 1590 |
| 11 | GB | +1.8 | +2.3 | +0.7 | -1.2 | 1546 |
| 12 | DEN | +1.6 | +0.2 | +1.4 | +0.0 | 1647 |
| 13 | NE | +1.5 | +1.5 | -0.2 | +0.2 | 1537 |
| 14 | HOU | +1.3 | -0.1 | +1.0 | +0.3 | 1525 |
| 15 | BAL | +0.4 | +1.4 | -0.2 | -0.9 | 1477 |
| 16 | TB | +0.2 | -2.2 | +2.0 | +0.4 | 1494 |
| 17 | DAL | -0.3 | +3.4 | -3.8 | +0.1 | 1455 |
| 18 | PIT | -0.5 | -0.5 | +0.1 | -0.2 | 1576 |
| 19 | NYG | -0.7 | -0.4 | +0.0 | -0.4 | 1467 |
| 20 | CAR | -1.2 | -0.0 | -0.8 | -0.3 | 1443 |
| 21 | IND | -1.5 | -1.8 | -0.8 | +1.0 | 1398 |
| 22 | WAS | -1.7 | -0.4 | -1.6 | +0.4 | 1447 |
| 23 | PHI | -2.3 | -3.0 | +0.6 | +0.1 | 1397 |
| 24 | CLE | -3.0 | -4.1 | +1.0 | +0.1 | 1460 |
| 25 | NO | -3.4 | -2.3 | -0.4 | -0.7 | 1404 |
| 26 | NYJ | -3.7 | -2.0 | -2.5 | +0.7 | 1328 |
| 27 | ATL | -3.9 | -2.6 | -0.2 | -1.1 | 1421 |
| 28 | MIA | -4.7 | -2.0 | -1.7 | -1.0 | 1359 |
| 29 | LAC | -4.8 | -5.5 | +1.0 | -0.3 | 1374 |
| 30 | ARI | -5.3 | -2.5 | -1.8 | -0.9 | 1374 |
| 31 | LV | -5.4 | -3.4 | -2.5 | +0.5 | 1399 |
| 32 | TEN | -6.1 | -3.4 | -2.8 | +0.1 | 1301 |

## Current model fit

- Fitted on 1841 games from seasons 2020–2026.
- Home field: 1.4 points (1.8 in divisional games).
- QB adjustment: 0.85 points per point of QB value gap.
- Special teams: 0.45 points per point of net special-teams EPA.
- Weight on the betting line: 90% for the margin, 96% for the total.
- Wind: -0.21 total points per mph above 10 mph at open-air stadiums.
