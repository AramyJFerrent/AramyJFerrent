# NFL score predictions

Updated Tue Oct 20, 2026 01:58 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the model alone, before it is blended with the line: the model's own expected points are run through the same score simulator, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV and the model's chance it wins. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers often sit several points from the line (the final prediction gives the line over 90% of the weight for that reason), so an edge shows up in about three games of four. In walk-forward backtests against closing lines and prices (2015–2025), betting every edge returned +0.7% on spreads, -4.4% on moneylines and -3.3% on totals, and every 95% range includes zero; against Wednesday lines at an assumed -110 (2015–2020), spread edges returned +2.1%. The live record is tracked below.

## 2026 Week 7

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 10/22 8:15 PM | NE @ CHI | NE 24, CHI 27 | CHI 59% | NE +140 / CHI -140 | 23.8 – 26.7 | 13–36 / 15–38 | CHI -1.6 / CHI -3.0 | 49.7 / 50.5 | no edge | no edge | Under 50.5 (-105): EV +4.6%, model 54% | Drake Maye / Caleb Williams |  |
| Sun 10/25 9:30 AM | PIT @ NO | PIT 23, NO 20 | PIT 61% | PIT -155 / NO +155 | 23.9 – 20.6 | 13–36 / 10–32 | PIT -1.2 / PIT -3.5 | 43.9 / 44.5 | NO +3.5 (-118): EV +10.7%, model 60% | NO (+150): EV +17.0%, model 47% | no edge | Aaron Rodgers / Tyler Shough |  |
| Sun 10/25 1:00 PM | CIN @ BAL | CIN 24, BAL 27 | BAL 58% | CIN +140 / BAL -140 | 24.4 – 27.1 | 13–37 / 16–40 | CIN -2.4 / BAL -3.0 | 50.4 / 51.5 | CIN +3.0 (-118): EV +21.7%, model 62% | CIN (+124): EV +27.6%, model 57% | no edge | Joe Burrow / Tyler Huntley |  |
| Sun 10/25 1:00 PM | CLE @ TEN | CLE 20, TEN 17 | CLE 55% | CLE -125 / TEN +125 | 20.1 – 18.4 | 9–31 / 7–30 | CLE -3.8 / CLE -1.5 | 38.6 / 38.5 | CLE -1.5 (-112): EV +12.7%, model 60% | CLE (-130): EV +10.1%, model 62% | no edge | Deshaun Watson / Cam Ward |  |
| Sun 10/25 1:00 PM | IND @ MIN | IND 17, MIN 23 | MIN 71% | IND +245 / MIN -245 | 17.5 – 24.0 | 7–29 / 13–36 | MIN -6.9 / MIN -6.5 | 42.8 / 41.5 | no edge | no edge | no edge | Daniel Jones / Kyler Murray |  |
| Sun 10/25 1:00 PM | MIA @ NYJ | MIA 17, NYJ 20 | NYJ 64% | MIA +180 / NYJ -180 | 17.0 – 21.5 | 7–28 / 10–34 | NYJ -4.0 / NYJ -4.5 | 43.5 / 38.5 | MIA +4.5 (-102): EV +8.3%, model 55% | MIA (+195): EV +11.8%, model 38% | Over 38.5 (-115): EV +19.3%, model 64% | Malik Willis / Geno Smith |  |
| Sun 10/25 1:00 PM | NYG @ HOU | NYG 17, HOU 24 | HOU 78% | NYG +355 / HOU -355 | 16.4 – 26.1 | 6–27 / 14–38 | HOU -4.6 / HOU -10.0 | 43.8 / 42.5 | NYG +10.0 (-112): EV +33.3%, model 69% | NYG (+390): EV +72.5%, model 35% | no edge | Jameis Winston / C.J. Stroud |  |
| Sun 10/25 1:00 PM | SF @ ATL | SF 27, ATL 24 | SF 59% | SF -145 / ATL +145 | 26.9 – 23.6 | 16–39 / 13–36 | SF -6.8 / SF -3.0 | 49.0 / 50.5 | SF -3.0 (-115): EV +14.1%, model 57% | SF (-175): EV +9.7%, model 70% | Under 50.5 (-110): EV +4.9%, model 55% | Brock Purdy / Michael Penix Jr. |  |
| Sun 10/25 1:00 PM | TB @ CAR | TB 20, CAR 23 | CAR 61% | TB +160 / CAR -160 | 20.4 – 24.1 | 10–32 / 13–36 | CAR -6.4 / CAR -3.5 | 42.6 / 44.5 | CAR -3.5 (-108): EV +7.3%, model 56% | CAR (-185): EV +7.2%, model 69% | Under 44.5 (-110): EV +8.9%, model 57% | Jalon Daniels / Bryce Young |  |
| Sun 10/25 4:05 PM | DEN @ ARI | DEN 23, ARI 20 | DEN 63% | DEN -170 / ARI +170 | 24.0 – 19.5 | 13–37 / 9–31 | DEN -3.2 / DEN -4.5 | 43.4 / 43.5 | ARI +4.5 (-110): EV +7.9%, model 57% | ARI (+195): EV +17.7%, model 40% | no edge | Bo Nix / Jacoby Brissett |  |
| Sun 10/25 4:25 PM | GB @ DET | GB 24, DET 27 | DET 59% | GB +145 / DET -145 | 25.2 – 28.3 | 13–37 / 16–41 | DET -4.5 / DET -3.0 | 52.7 / 53.5 | DET -3.0 (-105): EV +4.2%, model 49% | no edge | no edge | Jordan Love / Jared Goff |  |
| Sun 10/25 4:25 PM | LA @ LV | LA 27, LV 24 | LA 63% | LA -170 / LV +170 | 25.9 – 21.6 | 13–38 / 10–34 | LA -2.6 / LA -4.5 | 47.3 / 47.5 | LV +4.5 (-115): EV +10.3%, model 59% | LV (+185): EV +19.2%, model 42% | no edge | Matthew Stafford / Kirk Cousins |  |
| Sun 10/25 8:20 PM | KC @ SEA | KC 20, SEA 23 | SEA 57% | KC +135 / SEA -135 | 20.1 – 22.4 | 9–31 / 10–34 | SEA -0.5 / SEA -2.5 | 42.6 / 42.5 | KC +2.5 (-110): EV +3.5%, model 54% | KC (+120): EV +7.6%, model 49% | no edge | Patrick Mahomes / Drew Lock |  |
| Mon 10/26 8:15 PM | DAL @ PHI | DAL 23, PHI 20 | DAL 62% | DAL -160 / PHI +160 | 24.2 – 20.3 | 13–37 / 10–32 | PHI -3.5 / DAL -4.5 | 49.3 / 44.5 | PHI +4.5 (-108): EV +43.8%, model 75% | PHI (+180): EV +68.5%, model 60% | Over 44.5 (-110): EV +17.9%, model 62% | Dak Prescott / Jalen Hurts |  |

## 2026 Week 8

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 10/29 8:15 PM | CAR @ GB | CAR 24, GB 27 | GB 61% | CAR +160 / GB -160 | 23.1 – 26.9 | 12–35 / 15–39 | GB -3.8 / – | 50.3 / 45.5 | no line yet | no edge | Over 45.5 (-115): EV +17.8%, model 63% | B.Young / J.Love |  |
| Sun 11/01 1:00 PM | ARI @ DAL | ARI 24, DAL 30 | DAL 69% | ARI +225 / DAL -225 | 22.6 – 28.9 | 10–35 / 17–41 | DAL -3.4 / DAL -6.5 | 51.9 / 51.5 | ARI +6.5 (-110): EV +20.3%, model 63% | ARI (+250): EV +40.0%, model 40% | no edge | J.Brissett / D.Prescott |  |
| Sun 11/01 1:00 PM | ATL @ TB | ATL 20, TB 23 | TB 55% | ATL +125 / TB -125 | 21.5 – 23.0 | 10–34 / 12–35 | TB -1.2 / TB -1.5 | 38.0 / 44.5 | no edge | no edge | Under 44.5 (-115): EV +33.4%, model 71% | M.Penix / J.Daniels |  |
| Sun 11/01 1:00 PM | BAL @ BUF | BAL 24, BUF 27 | BUF 59% | BAL +140 / BUF -140 | 25.3 – 28.2 | 13–37 / 16–41 | BUF -9.0 / BUF -2.5 | 53.7 / 53.5 | BUF -2.5 (-114): EV +34.1%, model 71% | BUF (-142): EV +29.7%, model 76% | no edge | T.Huntley / J.Allen |  |
| Sun 11/01 1:00 PM | CLE @ PIT | CLE 17, PIT 20 | PIT 64% | CLE +175 / PIT -175 | 17.6 – 21.9 | 7–29 / 10–34 | PIT -2.3 / PIT -4.5 | 40.0 / 39.5 | CLE +4.5 (-105): EV +17.5%, model 60% | CLE (+194): EV +27.3%, model 43% | no edge | D.Watson / A.Rodgers |  |
| Sun 11/01 1:00 PM | IND @ JAX | IND 20, JAX 27 | JAX 72% | IND +260 / JAX -260 | 20.0 – 27.5 | 9–31 / 16–40 | JAX -8.1 / JAX -7.5 | 49.0 / 47.5 | no edge | IND (+310): EV +4.0%, model 25% | Over 47.5 (-105): EV +5.1%, model 54% | D.Jones / T.Lawrence |  |
| Sun 11/01 1:00 PM | LV @ NYJ | LV 20, NYJ 23 | NYJ 55% | LV +120 / NYJ -120 | 21.0 – 22.5 | 10–33 / 10–34 | NYJ -2.0 / NYJ -1.5 | 44.6 / 43.5 | NYJ -1.5 (-105): EV +4.8%, model 54% | NYJ (-118): EV +4.3%, model 56% | no edge | K.Cousins / G.Smith |  |
| Sun 11/01 1:00 PM | MIN @ DET | MIN 20, DET 23 | DET 56% | MIN +130 / DET -130 | 21.9 – 24.1 | 10–34 / 13–36 | DET -2.2 / – | 46.1 / 48.5 | no line yet | no edge | Under 48.5 (-115): EV +7.6%, model 58% | K.Murray / J.Goff |  |
| Sun 11/01 1:00 PM | TEN @ CIN | TEN 17, CIN 27 | CIN 79% | TEN +390 / CIN -390 | 17.5 – 28.0 | 7–29 / 16–41 | CIN -11.2 / CIN -10.5 | 47.4 / 45.5 | no edge | TEN (+460): EV +6.8%, model 19% | Over 45.5 (-110): EV +5.6%, model 55% | C.Ward / J.Burrow |  |
| Sun 11/01 4:05 PM | LAC @ LA | LAC 20, LA 27 | LA 72% | LAC +260 / LA -260 | 19.1 – 26.4 | 9–31 / 14–39 | LA -5.5 / LA -7.5 | 42.2 / 45.5 | LAC +7.5 (-112): EV +17.5%, model 62% | LAC (+315): EV +36.0%, model 33% | Under 45.5 (-105): EV +18.9%, model 61% | J.Herbert / M.Stafford |  |
| Sun 11/01 4:25 PM | KC @ DEN | KC 23, DEN 20 | KC 55% | KC -125 / DEN +125 | 22.0 – 20.5 | 10–34 / 10–32 | KC -1.2 / KC -1.5 | 46.5 / 42.5 | no edge | no edge | Over 42.5 (-115): EV +15.2%, model 62% | P.Mahomes / B.Nix |  |
| Sun 11/01 4:25 PM | NE @ MIA | NE 27, MIA 17 | NE 76% | NE -310 / MIA +310 | 26.0 – 17.5 | 14–38 / 7–29 | NE -7.7 / NE -8.5 | 46.1 / 43.5 | MIA +8.5 (-120): EV +4.3%, model 57% | MIA (+340): EV +18.1%, model 27% | Over 43.5 (-120): EV +3.5%, model 56% | D.Maye / M.Willis |  |
| Sun 11/01 8:20 PM | PHI @ WAS | PHI 20, WAS 23 | WAS 61% | PHI +160 / WAS -160 | 18.4 – 22.1 | 7–30 / 10–34 | WAS -6.0 / WAS -3.5 | 41.2 / 40.5 | no edge | no edge | no edge | T.McKee / J.Daniels |  |
| Mon 11/02 8:15 PM | CHI @ SEA | CHI 20, SEA 23 | SEA 53% | CHI +115 / SEA -115 | 21.1 – 22.2 | 10–33 / 10–34 | SEA -1.1 / – | 43.3 / 46.5 | no line yet | CHI (+138): EV +9.9%, model 46% | Under 46.5 (-110): EV +14.1%, model 60% | C.Williams / S.Darnold |  |

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
