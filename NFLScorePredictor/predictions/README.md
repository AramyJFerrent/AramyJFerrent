# NFL score predictions

Updated Wed Oct 21, 2026 02:02 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The edge columns price every side of the spread, moneyline and total with the model alone, before it is blended with the line: the model's own expected points are run through the same score simulator, and each side's expected value (EV) is what $1 staked returns on average at the posted price (pushes on whole-number lines and moneyline ties refund the stake). A side is an edge when its EV is at least +3%; the cell shows the best side, its price, its EV and the model's chance it wins. Prices come from the nflverse schedule; a spread or total price marked * was not posted and is assumed to be -110. Moneylines are never assumed. Treat the edges as an experiment, not betting advice. The model's own numbers often sit several points from the line (the final prediction gives the line over 90% of the weight for that reason), so an edge shows up in about three games of four. In walk-forward backtests against closing lines and prices (2015–2025), betting every edge returned +0.7% on spreads, -4.4% on moneylines and -3.3% on totals, and every 95% range includes zero; against Wednesday lines at an assumed -110 (2015–2020), spread edges returned +2.1%. The live record is tracked below.

## 2026 Week 7

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 10/22 8:15 PM | NE @ CHI | NE 24, CHI 27 | CHI 59% | NE +145 / CHI -145 | 23.8 – 26.7 | 13–36 / 15–39 | CHI -1.6 / CHI -3.0 | 49.7 / 50.5 | NE +3.0 (-118): EV +3.2%, model 51% | NE (+130): EV +6.9%, model 46% | Under 50.5 (-105): EV +3.6%, model 53% | Drake Maye / Caleb Williams |  |
| Sun 10/25 9:30 AM | PIT @ NO | PIT 23, NO 20 | PIT 61% | PIT -160 / NO +160 | 23.9 – 20.6 | 13–36 / 10–32 | PIT -1.2 / PIT -3.5 | 43.9 / 44.5 | NO +3.5 (-118): EV +10.2%, model 60% | NO (+154): EV +16.6%, model 46% | no edge | Aaron Rodgers / Tyler Shough |  |
| Sun 10/25 1:00 PM | CIN @ BAL | CIN 24, BAL 27 | BAL 55% | CIN +120 / BAL -120 | 24.1 – 25.4 | 13–36 / 14–38 | CIN -2.4 / BAL -1.5 | 50.4 / 49.5 | CIN +1.5 (-110): EV +14.4%, model 60% | CIN (+105): EV +17.3%, model 57% | no edge | Joe Burrow / Tyler Huntley |  |
| Sun 10/25 1:00 PM | CLE @ TEN | CLE 20, TEN 17 | CLE 56% | CLE -125 / TEN +125 | 19.6 – 17.9 | 9–31 / 7–29 | CLE -3.8 / CLE -1.5 | 38.6 / 37.5 | CLE -1.5 (-110): EV +14.3%, model 60% | CLE (-125): EV +12.5%, model 62% | no edge | Deshaun Watson / Cam Ward |  |
| Sun 10/25 1:00 PM | IND @ MIN | IND 17, MIN 23 | MIN 70% | IND +230 / MIN -230 | 17.5 – 24.0 | 7–28 / 13–36 | MIN -6.9 / MIN -6.5 | 42.8 / 41.5 | no edge | no edge | no edge | Daniel Jones / Kyler Murray |  |
| Sun 10/25 1:00 PM | MIA @ NYJ | MIA 17, NYJ 20 | NYJ 64% | MIA +180 / NYJ -180 | 17.5 – 22.0 | 7–28 / 10–34 | NYJ -4.0 / NYJ -4.5 | 43.5 / 39.5 | MIA +4.5 (-105): EV +6.8%, model 55% | MIA (+185): EV +7.2%, model 38% | Over 39.5 (-108): EV +18.3%, model 61% | Malik Willis / Geno Smith |  |
| Sun 10/25 1:00 PM | NYG @ HOU | NYG 17, HOU 27 | HOU 78% | NYG +355 / HOU -355 | 16.4 – 26.1 | 6–27 / 14–38 | HOU -6.9 / HOU -10.0 | 41.5 / 42.5 | NYG +10.0 (-108): EV +22.7%, model 62% | NYG (+390): EV +40.4%, model 29% | Under 42.5 (-102): EV +6.0%, model 54% | J.J. McCarthy / C.J. Stroud |  |
| Sun 10/25 1:00 PM | SF @ ATL | SF 27, ATL 24 | SF 60% | SF -150 / ATL +150 | 26.9 – 23.6 | 15–39 / 13–36 | SF -6.8 / SF -3.0 | 49.0 / 50.5 | SF -3.0 (-115): EV +14.2%, model 57% | SF (-175): EV +9.6%, model 70% | Under 50.5 (-115): EV +3.3%, model 55% | Brock Purdy / Michael Penix Jr. |  |
| Sun 10/25 1:00 PM | TB @ CAR | TB 20, CAR 23 | CAR 61% | TB +155 / CAR -155 | 20.4 – 24.1 | 10–32 / 13–36 | CAR -6.4 / CAR -3.5 | 42.6 / 44.5 | CAR -3.5 (-105): EV +7.3%, model 55% | CAR (-175): EV +8.8%, model 69% | Under 44.5 (-110): EV +10.0%, model 58% | Jalon Daniels / Bryce Young |  |
| Sun 10/25 4:05 PM | DEN @ ARI | DEN 23, ARI 20 | DEN 63% | DEN -175 / ARI +175 | 24.0 – 19.5 | 13–37 / 9–31 | DEN -3.2 / DEN -4.5 | 43.4 / 43.5 | ARI +4.5 (-110): EV +8.5%, model 57% | ARI (+195): EV +16.1%, model 39% | no edge | Bo Nix / Jacoby Brissett |  |
| Sun 10/25 4:25 PM | GB @ DET | GB 24, DET 27 | DET 59% | GB +145 / DET -145 | 25.2 – 28.3 | 13–37 / 16–41 | DET -4.5 / DET -3.0 | 52.7 / 53.5 | no edge | no edge | no edge | Jordan Love / Jared Goff |  |
| Sun 10/25 4:25 PM | LA @ LV | LA 27, LV 24 | LA 63% | LA -170 / LV +170 | 26.4 – 22.1 | 14–38 / 10–34 | LA -2.6 / LA -4.5 | 47.3 / 48.5 | LV +4.5 (-115): EV +9.0%, model 58% | LV (+180): EV +18.0%, model 42% | Under 48.5 (-112): EV +3.2%, model 55% | Matthew Stafford / Kirk Cousins |  |
| Sun 10/25 8:20 PM | KC @ SEA | KC 20, SEA 23 | SEA 57% | KC +135 / SEA -135 | 20.1 – 22.4 | 10–31 / 10–34 | SEA -0.5 / SEA -2.5 | 42.6 / 42.5 | KC +2.5 (-102): EV +7.0%, model 54% | KC (+124): EV +8.7%, model 48% | no edge | Patrick Mahomes / Drew Lock |  |
| Mon 10/26 8:15 PM | DAL @ PHI | DAL 23, PHI 20 | DAL 62% | DAL -160 / PHI +160 | 24.2 – 20.3 | 13–36 / 9–31 | PHI -3.5 / DAL -4.5 | 49.3 / 44.5 | PHI +4.5 (-108): EV +43.8%, model 75% | PHI (+185): EV +72.6%, model 60% | Over 44.5 (-110): EV +19.0%, model 62% | Dak Prescott / Jalen Hurts |  |

## 2026 Week 8

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 10/29 8:15 PM | CAR @ GB | CAR 20, GB 23 | GB 59% | CAR +145 / GB -145 | 22.2 – 25.3 | 10–34 / 13–37 | GB -3.8 / GB -3.0 | 50.3 / 47.5 | GB -3.0 (-105): EV +3.4%, model 49% | no edge | Over 47.5 (-105): EV +13.2%, model 58% | Bryce Young / Jordan Love |  |
| Sun 11/01 1:00 PM | ARI @ DAL | ARI 23, DAL 30 | DAL 69% | ARI +220 / DAL -220 | 22.6 – 28.9 | 10–34 / 17–41 | DAL -3.4 / DAL -6.5 | 51.9 / 51.5 | ARI +6.5 (-110): EV +20.7%, model 63% | ARI (+245): EV +39.4%, model 40% | no edge | Jacoby Brissett / Dak Prescott |  |
| Sun 11/01 1:00 PM | ATL @ TB | ATL 20, TB 23 | TB 55% | ATL +125 / TB -125 | 21.5 – 23.0 | 10–33 / 12–35 | TB -1.2 / TB -1.5 | 38.0 / 44.5 | no edge | no edge | Under 44.5 (-110): EV +36.6%, model 72% | Michael Penix Jr. / Jalon Daniels |  |
| Sun 11/01 1:00 PM | BAL @ BUF | BAL 24, BUF 27 | BUF 59% | BAL +145 / BUF -145 | 24.8 – 27.7 | 13–37 / 16–40 | BUF -9.0 / BUF -2.5 | 53.7 / 52.5 | BUF -2.5 (-120): EV +31.1%, model 72% | BUF (-155): EV +24.5%, model 76% | no edge | Tyler Huntley / Josh Allen |  |
| Sun 11/01 1:00 PM | CLE @ PIT | CLE 17, PIT 20 | PIT 64% | CLE +180 / PIT -180 | 17.1 – 21.4 | 6–28 / 10–34 | PIT -2.3 / PIT -4.5 | 40.0 / 38.5 | CLE +4.5 (-110): EV +14.6%, model 60% | CLE (+170): EV +15.6%, model 43% | no edge | Deshaun Watson / Aaron Rodgers |  |
| Sun 11/01 1:00 PM | IND @ JAX | IND 20, JAX 27 | JAX 73% | IND +270 / JAX -270 | 20.0 – 27.5 | 9–31 / 16–40 | JAX -8.1 / JAX -7.5 | 49.0 / 47.5 | no edge | no edge | no edge | Daniel Jones / Trevor Lawrence |  |
| Sun 11/01 1:00 PM | LV @ NYJ | LV 20, NYJ 23 | NYJ 54% | LV +120 / NYJ -120 | 20.5 – 22.0 | 10–32 / 10–34 | NYJ -2.0 / NYJ -1.5 | 44.6 / 42.5 | NYJ -1.5 (+100): EV +7.9%, model 54% | NYJ (-112): EV +7.2%, model 57% | Over 42.5 (-110): EV +6.9%, model 56% | Kirk Cousins / Geno Smith |  |
| Sun 11/01 1:00 PM | MIN @ DET | MIN 24, DET 27 | DET 58% | MIN +135 / DET -135 | 22.5 – 25.0 | 10–34 / 13–37 | DET -2.2 / DET -2.5 | 46.1 / 47.5 | no edge | no edge | Under 47.5 (-115): EV +4.3%, model 56% | Kyler Murray / Jared Goff |  |
| Sun 11/01 1:00 PM | TEN @ CIN | TEN 17, CIN 27 | CIN 78% | TEN +365 / CIN -365 | 18.2 – 28.3 | 7–30 / 16–41 | CIN -11.2 / CIN -10.0 | 47.4 / 46.5 | no edge | no edge | no edge | Cam Ward / Joe Burrow |  |
| Sun 11/01 4:05 PM | LAC @ LA | LAC 20, LA 27 | LA 72% | LAC +255 / LA -255 | 19.6 – 26.9 | 9–31 / 15–40 | LA -5.5 / LA -7.5 | 42.2 / 46.5 | LAC +7.5 (-115): EV +15.8%, model 62% | LAC (+280): EV +24.7%, model 33% | Under 46.5 (-110): EV +21.4%, model 64% | Justin Herbert / Matthew Stafford |  |
| Sun 11/01 4:25 PM | KC @ DEN | KC 23, DEN 20 | KC 56% | KC -125 / DEN +125 | 22.0 – 20.5 | 10–34 / 10–32 | KC -1.2 / KC -1.5 | 46.5 / 42.5 | no edge | no edge | Over 42.5 (-110): EV +19.2%, model 62% | Patrick Mahomes / Bo Nix |  |
| Sun 11/01 4:25 PM | NE @ MIA | NE 27, MIA 20 | NE 73% | NE -275 / MIA +275 | 26.0 – 18.5 | 14–38 / 7–30 | NE -7.7 / NE -7.5 | 46.1 / 44.5 | MIA +7.5 (-105): EV +7.0%, model 55% | MIA (+330): EV +15.5%, model 27% | no edge | Drake Maye / Malik Willis |  |
| Sun 11/01 8:20 PM | PHI @ WAS | PHI 20, WAS 23 | WAS 61% | PHI +155 / WAS -155 | 19.1 – 22.4 | 9–31 / 10–34 | WAS -1.9 / WAS -3.5 | 45.4 / 41.5 | PHI +3.5 (-110): EV +10.1%, model 58% | PHI (+154): EV +11.9%, model 44% | Over 41.5 (-110): EV +15.9%, model 61% | Jalen Hurts / Jayden Daniels |  |
| Mon 11/02 8:15 PM | CHI @ SEA | CHI 20, SEA 23 | SEA 59% | CHI +145 / SEA -145 | 21.9 – 24.6 | 10–34 / 13–37 | CHI -0.6 / SEA -3.0 | 41.6 / 46.5 | CHI +3.0 (-110): EV +16.8%, model 57% | CHI (+136): EV +21.3%, model 51% | Under 46.5 (-110): EV +24.8%, model 65% | Caleb Williams / Drew Lock |  |

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

Spread line moved toward the model's early spread edge before kickoff: 1 of 1 games (100%). Lines moving toward the edge (closing line value) is the quickest sign that the model knows something the market doesn't yet.

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
