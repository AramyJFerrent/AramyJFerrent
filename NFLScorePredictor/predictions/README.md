# NFL score predictions

Updated Tue Oct 20, 2026 09:43 AM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the model alone, before it is blended with the line: the model's own expected points are run through the same score simulator, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV and the model's chance it wins. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers often sit several points from the line (the final prediction gives the line over 90% of the weight for that reason), so an edge shows up in about three games of four. In walk-forward backtests against closing lines and prices (2015–2025), betting every edge returned +0.7% on spreads, -4.4% on moneylines and -3.3% on totals, and every 95% range includes zero; against Wednesday lines at an assumed -110 (2015–2020), spread edges returned +2.1%. The live record is tracked below.

## 2026 Week 7

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 10/22 8:15 PM | NE @ CHI | NE 24, CHI 27 | CHI 59% | NE +145 / CHI -145 | 23.8 – 26.7 | 13–35 / 15–38 | CHI -1.6 / CHI -3.0 | 49.7 / 50.5 | no edge | no edge | no edge | Drake Maye / Caleb Williams |  |
| Sun 10/25 9:30 AM | PIT @ NO | PIT 23, NO 20 | PIT 61% | PIT -160 / NO +160 | 23.9 – 20.6 | 13–36 / 10–32 | PIT -1.2 / PIT -3.5 | 43.9 / 44.5 | NO +3.5 (-118): EV +10.4%, model 60% | NO (+150): EV +14.8%, model 46% | no edge | Aaron Rodgers / Tyler Shough |  |
| Sun 10/25 1:00 PM | CIN @ BAL | CIN 24, BAL 27 | BAL 58% | CIN +140 / BAL -140 | 24.4 – 27.1 | 13–37 / 16–40 | CIN -2.4 / BAL -3.0 | 50.4 / 51.5 | CIN +3.0 (-118): EV +21.4%, model 62% | CIN (+124): EV +27.6%, model 57% | no edge | Joe Burrow / Tyler Huntley |  |
| Sun 10/25 1:00 PM | CLE @ TEN | CLE 20, TEN 17 | CLE 55% | CLE -125 / TEN +125 | 20.1 – 18.4 | 9–31 / 7–30 | CLE -3.8 / CLE -1.5 | 38.6 / 38.5 | CLE -1.5 (-115): EV +11.5%, model 60% | CLE (-130): EV +10.2%, model 62% | no edge | Deshaun Watson / Cam Ward |  |
| Sun 10/25 1:00 PM | IND @ MIN | IND 17, MIN 23 | MIN 70% | IND +230 / MIN -230 | 17.5 – 24.0 | 7–29 / 13–36 | MIN -6.9 / MIN -6.5 | 42.8 / 41.5 | no edge | no edge | no edge | Daniel Jones / Kyler Murray |  |
| Sun 10/25 1:00 PM | MIA @ NYJ | MIA 17, NYJ 20 | NYJ 65% | MIA +190 / NYJ -190 | 17.0 – 21.5 | 7–27 / 10–34 | NYJ -4.0 / NYJ -4.5 | 43.5 / 38.5 | MIA +4.5 (-102): EV +7.6%, model 54% | MIA (+190): EV +9.8%, model 38% | Over 38.5 (-115): EV +18.1%, model 63% | Malik Willis / Geno Smith |  |
| Sun 10/25 1:00 PM | NYG @ HOU | NYG 17, HOU 27 | HOU 78% | NYG +355 / HOU -355 | 16.4 – 26.1 | 6–27 / 13–38 | HOU -4.6 / HOU -10.0 | 43.8 / 42.5 | NYG +10.0 (-112): EV +32.2%, model 68% | NYG (+390): EV +74.1%, model 36% | no edge | Jameis Winston / C.J. Stroud |  |
| Sun 10/25 1:00 PM | SF @ ATL | SF 27, ATL 24 | SF 61% | SF -160 / ATL +160 | 27.1 – 23.4 | 16–39 / 12–36 | SF -6.8 / SF -3.5 | 49.0 / 50.5 | SF -3.5 (-115): EV +5.4%, model 56% | SF (-205): EV +3.6%, model 70% | Under 50.5 (-110): EV +5.3%, model 55% | Brock Purdy / Michael Penix Jr. |  |
| Sun 10/25 1:00 PM | TB @ CAR | TB 20, CAR 23 | CAR 61% | TB +160 / CAR -160 | 20.4 – 24.1 | 10–32 / 13–37 | CAR -6.4 / CAR -3.5 | 42.6 / 44.5 | CAR -3.5 (-108): EV +8.0%, model 56% | CAR (-192): EV +6.3%, model 70% | Under 44.5 (-110): EV +9.2%, model 57% | Jalon Daniels / Bryce Young |  |
| Sun 10/25 4:05 PM | DEN @ ARI | DEN 23, ARI 20 | DEN 63% | DEN -170 / ARI +170 | 24.0 – 19.5 | 13–37 / 9–31 | DEN -3.2 / DEN -4.5 | 43.4 / 43.5 | ARI +4.5 (-110): EV +9.8%, model 58% | ARI (+195): EV +16.6%, model 39% | no edge | Bo Nix / Jacoby Brissett |  |
| Sun 10/25 4:25 PM | GB @ DET | GB 24, DET 27 | DET 61% | GB +155 / DET -155 | 25.2 – 28.3 | 13–37 / 16–41 | DET -4.5 / DET -3.0 | 52.7 / 53.5 | DET -3.0 (-105): EV +5.3%, model 50% | no edge | no edge | Jordan Love / Jared Goff |  |
| Sun 10/25 4:25 PM | LA @ LV | LA 27, LV 24 | LA 62% | LA -165 / LV +165 | 25.9 – 21.6 | 13–38 / 10–34 | LA -2.6 / LA -4.5 | 47.3 / 47.5 | LV +4.5 (-115): EV +8.5%, model 58% | LV (+185): EV +18.4%, model 41% | no edge | Matthew Stafford / Kirk Cousins |  |
| Sun 10/25 8:20 PM | KC @ SEA | KC 20, SEA 23 | SEA 57% | KC +135 / SEA -135 | 20.1 – 22.4 | 9–31 / 10–34 | SEA -0.5 / SEA -2.5 | 42.6 / 42.5 | KC +2.5 (-110): EV +3.1%, model 54% | KC (+114): EV +3.9%, model 48% | no edge | Patrick Mahomes / Drew Lock |  |
| Mon 10/26 8:15 PM | DAL @ PHI | DAL 23, PHI 20 | DAL 62% | DAL -165 / PHI +165 | 24.2 – 20.3 | 13–36 / 10–32 | PHI -3.5 / DAL -4.5 | 49.3 / 44.5 | PHI +4.5 (-108): EV +43.4%, model 74% | PHI (+180): EV +68.4%, model 60% | Over 44.5 (-110): EV +17.9%, model 62% | Dak Prescott / Jalen Hurts |  |

## 2026 Week 8

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 10/29 8:15 PM | CAR @ GB | CAR 24, GB 27 | GB 61% | CAR +155 / GB -155 | 23.3 – 27.0 | 12–35 / 15–40 | GB -3.8 / – | 50.3 / – | no line yet | no line yet | no line yet | B.Young / J.Love |  |
| Sun 11/01 1:00 PM | ARI @ DAL | ARI 24, DAL 27 | DAL 60% | ARI +155 / DAL -155 | 24.3 – 27.6 | 13–36 / 16–40 | DAL -3.4 / – | 51.9 / – | no line yet | no line yet | no line yet | J.Brissett / D.Prescott |  |
| Sun 11/01 1:00 PM | ATL @ TB | ATL 17, TB 20 | TB 55% | ATL +120 / TB -120 | 18.4 – 19.6 | 7–30 / 9–31 | TB -1.2 / – | 38.0 / – | no line yet | no line yet | no line yet | M.Penix / J.Daniels |  |
| Sun 11/01 1:00 PM | BAL @ BUF | BAL 24, BUF 31 | BUF 76% | BAL +310 / BUF -310 | 22.4 – 31.4 | 10–34 / 19–44 | BUF -9.0 / – | 53.7 / – | no line yet | no line yet | no line yet | T.Huntley / J.Allen |  |
| Sun 11/01 1:00 PM | CLE @ PIT | CLE 20, PIT 23 | PIT 57% | CLE +135 / PIT -135 | 18.9 – 21.2 | 9–30 / 10–33 | PIT -2.3 / – | 40.0 / – | no line yet | no line yet | no line yet | D.Watson / A.Rodgers |  |
| Sun 11/01 1:00 PM | IND @ JAX | IND 20, JAX 27 | JAX 73% | IND +275 / JAX -275 | 20.4 – 28.5 | 10–32 / 17–41 | JAX -8.1 / – | 49.0 / – | no line yet | no line yet | no line yet | D.Jones / T.Lawrence |  |
| Sun 11/01 1:00 PM | LV @ NYJ | LV 20, NYJ 23 | NYJ 55% | LV +125 / NYJ -125 | 21.3 – 23.3 | 10–33 / 12–35 | NYJ -2.0 / – | 44.6 / – | no line yet | no line yet | no line yet | K.Cousins / G.Smith |  |
| Sun 11/01 1:00 PM | MIN @ DET | MIN 20, DET 23 | DET 57% | MIN +130 / DET -130 | 21.9 – 24.1 | 10–34 / 13–37 | DET -2.2 / – | 46.1 / – | no line yet | no line yet | no line yet | K.Murray / J.Goff |  |
| Sun 11/01 1:00 PM | TEN @ CIN | TEN 17, CIN 27 | CIN 81% | TEN +420 / CIN -420 | 18.1 – 29.3 | 7–30 / 17–42 | CIN -11.2 / – | 47.4 / – | no line yet | no line yet | no line yet | C.Ward / J.Burrow |  |
| Sun 11/01 4:05 PM | LAC @ LA | LAC 20, LA 23 | LA 67% | LAC +200 / LA -200 | 18.4 – 23.8 | 7–30 / 13–36 | LA -5.5 / – | 42.2 / – | no line yet | no line yet | no line yet | J.Herbert / M.Stafford |  |
| Sun 11/01 4:25 PM | KC @ DEN | KC 23, DEN 20 | KC 55% | KC -120 / DEN +120 | 23.8 – 22.6 | 13–36 / 10–34 | KC -1.2 / – | 46.5 / – | no line yet | no line yet | no line yet | P.Mahomes / B.Nix |  |
| Sun 11/01 4:25 PM | NE @ MIA | NE 27, MIA 20 | NE 73% | NE -275 / MIA +275 | 26.9 – 19.2 | 15–40 / 9–31 | NE -7.7 / – | 46.1 / – | no line yet | no line yet | no line yet | D.Maye / M.Willis |  |
| Sun 11/01 8:20 PM | PHI @ WAS | PHI 17, WAS 23 | WAS 68% | PHI +215 / WAS -215 | 17.6 – 23.6 | 7–29 / 13–36 | WAS -6.0 / – | 41.2 / – | no line yet | no line yet | no line yet | T.McKee / J.Daniels |  |
| Mon 11/02 8:15 PM | CHI @ SEA | CHI 20, SEA 23 | SEA 53% | CHI +115 / SEA -115 | 21.1 – 22.2 | 10–33 / 10–34 | SEA -1.1 / – | 43.3 / – | no line yet | no line yet | no line yet | C.Williams / S.Darnold |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 93 | 9.27 | 10.62 | 7.12 | 64.1% | 0.229 | 84.4% |
| Model only (before blending) | 93 | 9.13 | 11.40 | 7.37 | 66.3% | – | – |
| Betting line when predicted | 93 | 9.28 | 10.60 | 7.11 | 64.1% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin by about 10 points per game.

80 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines and actual starters, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

Every edge logged with the last prediction before kickoff, graded at the price logged with it, one unit per bet (live predictions only; backfilled games are left out). ROI is units won per unit staked.

| Market | Edges | Record (W-L-P) | Units | ROI |
|---|---|---|---|---|
| Spread | 0 | 0-0-0 | +0.00 | – |
| Moneyline | 0 | 0-0-0 | +0.00 | – |
| Total | 0 | 0-0-0 | +0.00 | – |

Spread line moved toward the model's early spread edge before kickoff: 0 of 0 games. Lines moving toward the edge (closing line value) is the quickest sign that the model knows something the market doesn't yet.

### Week 6 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| SEA @ DEN | 20–17 | 14–17 | 42% | yes |
| HOU @ JAX | 20–23 | 34–31 | 41% | no |
| BAL @ CLE | 20–17 | 10–13 | 40% | yes |
| CAR @ PHI | 20–17 | 25–14 | 60% | yes |
| CHI @ ATL | 27–24 | 31–23 | 55% | yes |
| NO @ NYG | 23–20 | 34–27 | 54% | yes |
| NYJ @ NE | 17–24 | 19–26 | 72% | yes |
| PIT @ TB | 20–17 | 26–19 | 54% | yes |
| TEN @ IND | 17–24 | 26–20 | 29% | yes |
| ARI @ LA | 20–30 | 18–16 | 16% | no |
| BUF @ LV | 27–24 | 33–30 | 67% | yes |
| LAC @ KC | 17–24 | 6–22 | 74% | yes |
| DAL @ GB | 24–27 | 13–23 | 55% | no |
| WAS @ SF | 23–30 | 17–23 | 72% | yes |

## Power ratings

Points per game better than an average team on a neutral field, from opponent-adjusted EPA with this season's games weighted against a preseason prior. Defense is positive when it holds opponents below average.

| # | Team | Net | Offense | Defense | Special teams | Elo |
|---|---|---|---|---|---|---|
| 1 | BUF | +5.4 | +6.0 | -1.4 | +0.8 | 1653 |
| 2 | SF | +4.3 | +4.8 | +0.2 | -0.7 | 1659 |
| 3 | JAX | +4.0 | +2.7 | +0.8 | +0.6 | 1608 |
| 4 | SEA | +3.7 | -1.4 | +3.4 | +1.6 | 1652 |
| 5 | NE | +3.5 | +2.4 | +0.9 | +0.2 | 1618 |
| 6 | DET | +3.4 | +3.4 | -1.1 | +1.1 | 1554 |
| 7 | CHI | +3.2 | +1.8 | +0.1 | +1.2 | 1560 |
| 8 | KC | +3.0 | +2.9 | +0.7 | -0.6 | 1583 |
| 9 | BAL | +2.9 | +3.4 | +0.1 | -0.6 | 1557 |
| 10 | GB | +2.2 | +2.2 | +0.3 | -0.3 | 1537 |
| 11 | LA | +1.9 | +2.7 | +0.9 | -1.7 | 1559 |
| 12 | MIN | +1.6 | -2.8 | +3.0 | +1.4 | 1630 |
| 13 | CIN | +1.2 | +1.9 | -1.0 | +0.2 | 1526 |
| 14 | HOU | +0.9 | -0.4 | +1.6 | -0.3 | 1547 |
| 15 | DEN | +0.6 | -0.8 | +1.8 | -0.3 | 1613 |
| 16 | CAR | +0.4 | +1.2 | -0.9 | +0.2 | 1499 |
| 17 | IND | -0.4 | +0.1 | -1.0 | +0.5 | 1425 |
| 18 | PHI | -0.5 | -2.2 | +1.0 | +0.7 | 1486 |
| 19 | TB | -1.3 | -1.9 | +0.8 | -0.2 | 1427 |
| 20 | PIT | -1.5 | -1.4 | +0.1 | -0.2 | 1545 |
| 21 | DAL | -1.5 | +2.1 | -3.7 | +0.0 | 1433 |
| 22 | NYG | -2.0 | -1.7 | -0.7 | +0.4 | 1434 |
| 23 | WAS | -2.3 | -0.4 | -1.8 | -0.1 | 1415 |
| 24 | ATL | -2.5 | -1.6 | +0.3 | -1.2 | 1454 |
| 25 | NO | -2.8 | -1.8 | -0.7 | -0.4 | 1425 |
| 26 | NYJ | -2.9 | -2.7 | -0.7 | +0.5 | 1381 |
| 27 | CLE | -3.0 | -4.4 | +1.5 | -0.1 | 1459 |
| 28 | ARI | -3.3 | -1.1 | -1.2 | -1.0 | 1393 |
| 29 | MIA | -3.7 | -1.4 | -1.6 | -0.7 | 1373 |
| 30 | LV | -3.8 | -2.7 | -0.8 | -0.3 | 1421 |
| 31 | LAC | -3.8 | -4.6 | +1.2 | -0.4 | 1409 |
| 32 | TEN | -7.0 | -4.7 | -2.0 | -0.4 | 1325 |

## Current model fit

- Fitted on 1786 games from seasons 2020–2026.
- Home field: 1.6 points (2.0 in divisional games).
- QB adjustment: 0.82 points per point of QB value gap.
- Special teams: 0.45 points per point of net special-teams EPA.
- Weight on the betting line: 93% for the margin, 100% for the total.
- Wind: -0.19 total points per mph above 10 mph at open-air stadiums.
