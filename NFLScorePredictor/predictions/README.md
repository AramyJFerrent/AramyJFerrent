# NFL score predictions

Updated Mon Oct 19, 2026 09:46 PM ET. Refreshed automatically every day of the season; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. Ties refund moneyline bets, so they are left out of these odds.

The model pick is the side the model's own spread favors against the current line, with the gap in points (under half a point is no edge). Treat it as an experiment: in walk-forward backtests these picks covered 53.7% against Wednesday lines (2015–2020) but only 51.7% against closing lines (2015–2025), and 52.4% is break-even at standard -110 odds. The live record is tracked below, graded against the first line each game had.

## 2026 Week 7

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Model pick (edge) | Total: model / line | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 10/22 8:15 PM | NE @ CHI | NE 24, CHI 27 | CHI 59% | NE +145 / CHI -145 | 23.8 – 26.7 | 13–36 / 15–38 | CHI -1.6 / CHI -3.0 | NE +3.0 (1.4) | 49.7 / 50.5 | Drake Maye / Caleb Williams |  |
| Sun 10/25 9:30 AM | PIT @ NO | PIT 23, NO 20 | PIT 60% | PIT -150 / NO +150 | 23.7 – 20.8 | 13–35 / 10–33 | PIT -1.2 / PIT -3.0 | NO +3.0 (1.8) | 43.9 / 44.5 | Aaron Rodgers / Tyler Shough |  |
| Sun 10/25 1:00 PM | CIN @ BAL | CIN 24, BAL 27 | BAL 57% | CIN +135 / BAL -135 | 24.7 – 26.8 | 13–37 / 16–39 | CIN -2.4 / BAL -2.5 | CIN +2.5 (4.9) | 50.4 / 51.5 | Joe Burrow / Tyler Huntley |  |
| Sun 10/25 1:00 PM | CLE @ TEN | CLE 20, TEN 17 | CLE 56% | CLE -125 / TEN +125 | 20.1 – 18.4 | 9–31 / 7–30 | CLE -3.8 / CLE -1.5 | CLE -1.5 (2.3) | 38.6 / 38.5 | Deshaun Watson / Cam Ward |  |
| Sun 10/25 1:00 PM | IND @ MIN | IND 17, MIN 24 | MIN 68% | IND +215 / MIN -215 | 17.7 – 23.8 | 7–29 / 13–36 | MIN -6.9 / MIN -6.0 | MIN -6.0 (0.9) | 42.8 / 41.5 | Daniel Jones / Kyler Murray |  |
| Sun 10/25 1:00 PM | MIA @ NYJ | MIA 17, NYJ 20 | NYJ 65% | MIA +185 / NYJ -185 | 17.0 – 21.5 | 7–28 / 10–34 | NYJ -4.0 / NYJ -4.5 | MIA +4.5 (0.5) | 43.5 / 38.5 | Malik Willis / Geno Smith |  |
| Sun 10/25 1:00 PM | NYG @ HOU | NYG 17, HOU 24 | HOU 77% | NYG +340 / HOU -340 | 16.7 – 25.8 | 6–27 / 13–38 | HOU -4.6 / HOU -9.5 | NYG +9.5 (4.9) | 43.8 / 42.5 | Jameis Winston / C.J. Stroud |  |
| Sun 10/25 1:00 PM | SF @ ATL | SF 27, ATL 20 | SF 68% | SF -215 / ATL +215 | 27.6 – 21.4 | 16–40 / 10–34 | SF -6.2 / – | – | 48.9 / – | Brock Purdy / Michael Penix Jr. | no line yet |
| Sun 10/25 1:00 PM | TB @ CAR | TB 20, CAR 23 | CAR 61% | TB +160 / CAR -160 | 20.4 – 24.1 | 10–32 / 13–36 | CAR -6.4 / CAR -3.5 | CAR -3.5 (2.9) | 42.6 / 44.5 | Jalon Daniels / Bryce Young |  |
| Sun 10/25 4:05 PM | DEN @ ARI | DEN 23, ARI 20 | DEN 63% | DEN -170 / ARI +170 | 24.0 – 19.5 | 13–37 / 9–31 | DEN -3.3 / DEN -4.5 | ARI +4.5 (1.2) | 43.5 / 43.5 | Bo Nix / Jacoby Brissett |  |
| Sun 10/25 4:25 PM | GB @ DET | GB 24, DET 27 | DET 60% | GB +150 / DET -150 | 24.7 – 27.8 | 13–37 / 16–40 | DET -4.5 / DET -3.0 | DET -3.0 (1.5) | 52.7 / 52.5 | Jordan Love / Jared Goff |  |
| Sun 10/25 4:25 PM | LA @ LV | LA 27, LV 24 | LA 62% | LA -160 / LV +160 | 25.9 – 21.6 | 13–38 / 10–34 | LA -2.6 / LA -4.5 | LV +4.5 (1.9) | 47.4 / 47.5 | Matthew Stafford / Kirk Cousins |  |
| Sun 10/25 8:20 PM | KC @ SEA | KC 20, SEA 23 | SEA 58% | KC +135 / SEA -135 | 20.1 – 22.4 | 10–31 / 10–34 | SEA -0.5 / SEA -2.5 | KC +2.5 (2.0) | 42.6 / 42.5 | Patrick Mahomes / Drew Lock |  |
| Mon 10/26 8:15 PM | DAL @ PHI | DAL 23, PHI 20 | DAL 62% | DAL -160 / PHI +160 | 24.2 – 20.3 | 13–36 / 10–32 | PHI -3.5 / DAL -4.5 | PHI +4.5 (8.0) | 49.3 / 44.5 | Dak Prescott / Jalen Hurts |  |

## 2026 Week 8

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Model pick (edge) | Total: model / line | QBs | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 10/29 8:15 PM | CAR @ GB | CAR 24, GB 27 | GB 61% | CAR +155 / GB -155 | 23.3 – 27.1 | 12–35 / 15–40 | GB -3.8 / – | – | 50.4 / – | B.Young / J.Love | no line yet |
| Sun 11/01 1:00 PM | ARI @ DAL | ARI 24, DAL 27 | DAL 61% | ARI +155 / DAL -155 | 24.3 – 27.7 | 13–37 / 16–40 | DAL -3.4 / – | – | 51.9 / – | J.Brissett / D.Prescott | no line yet |
| Sun 11/01 1:00 PM | ATL @ TB | ATL 17, TB 20 | TB 54% | ATL +120 / TB -120 | 18.4 – 19.6 | 7–30 / 9–31 | TB -1.2 / – | – | 38.0 / – | M.Penix / J.Daniels | no line yet |
| Sun 11/01 1:00 PM | BAL @ BUF | BAL 24, BUF 31 | BUF 75% | BAL +295 / BUF -295 | 22.4 – 31.4 | 10–34 / 20–44 | BUF -9.0 / – | – | 53.8 / – | T.Huntley / J.Allen | no line yet |
| Sun 11/01 1:00 PM | CLE @ PIT | CLE 20, PIT 23 | PIT 58% | CLE +140 / PIT -140 | 18.9 – 21.2 | 8–30 / 10–33 | PIT -2.3 / – | – | 40.0 / – | D.Watson / A.Rodgers | no line yet |
| Sun 11/01 1:00 PM | IND @ JAX | IND 20, JAX 27 | JAX 74% | IND +295 / JAX -295 | 20.5 – 28.5 | 9–32 / 17–41 | JAX -8.1 / – | – | 49.0 / – | D.Jones / T.Lawrence | no line yet |
| Sun 11/01 1:00 PM | LV @ NYJ | LV 20, NYJ 23 | NYJ 56% | LV +130 / NYJ -130 | 21.3 – 23.3 | 10–34 / 12–35 | NYJ -2.0 / – | – | 44.6 / – | K.Cousins / G.Smith | no line yet |
| Sun 11/01 1:00 PM | MIN @ DET | MIN 20, DET 23 | DET 57% | MIN +135 / DET -135 | 21.9 – 24.1 | 10–34 / 13–36 | DET -2.2 / – | – | 46.1 / – | K.Murray / J.Goff | no line yet |
| Sun 11/01 1:00 PM | TEN @ CIN | TEN 17, CIN 31 | CIN 81% | TEN +430 / CIN -430 | 18.1 – 29.3 | 7–30 / 17–42 | CIN -11.2 / – | – | 47.4 / – | C.Ward / J.Burrow | no line yet |
| Sun 11/01 4:05 PM | LAC @ LA | LAC 20, LA 23 | LA 67% | LAC +200 / LA -200 | 18.4 – 23.8 | 7–30 / 13–37 | LA -5.5 / – | – | 42.2 / – | J.Herbert / M.Stafford | no line yet |
| Sun 11/01 4:25 PM | KC @ DEN | KC 23, DEN 20 | KC 55% | KC -120 / DEN +120 | 23.8 – 22.7 | 13–36 / 10–34 | KC -1.2 / – | – | 46.5 / – | P.Mahomes / B.Nix | no line yet |
| Sun 11/01 4:25 PM | NE @ MIA | NE 27, MIA 20 | NE 74% | NE -280 / MIA +280 | 26.9 – 19.2 | 16–39 / 8–31 | NE -7.7 / – | – | 46.1 / – | D.Maye / M.Willis | no line yet |
| Sun 11/01 8:20 PM | PHI @ WAS | PHI 17, WAS 23 | WAS 70% | PHI +235 / WAS -235 | 17.4 – 24.0 | 7–28 / 13–36 | WAS -6.7 / – | – | 41.4 / – | T.McKee / J.Daniels | no line yet |
| Mon 11/02 8:15 PM | CHI @ SEA | CHI 20, SEA 23 | SEA 54% | CHI +115 / SEA -115 | 21.1 – 22.2 | 10–33 / 10–34 | SEA -1.1 / – | – | 43.3 / – | C.Williams / S.Darnold | no line yet |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 92 | 9.36 | 10.61 | 7.13 | 63.7% | 0.230 | 84.2% |
| Model only (before blending) | 92 | 9.22 | 11.37 | 7.38 | 65.9% | – | – |
| Betting line when predicted | 92 | 9.37 | 10.59 | 7.12 | 63.7% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin by about 10 points per game.

80 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines and actual starters, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Model picks against the spread

| Picks against | Record (W-L-P) | Cover rate |
|---|---|---|
| Early-week line (first prediction with a line) | 5-4-0 | 55.6% |
| Line at kickoff (last prediction; includes 80 backfilled games) | 43-31-5 | 58.1% |

Line moved toward the model's early pick before kickoff: 6 of 9 games (67%).

Break-even at standard -110 odds is 52.4%. Lines moving toward the model's pick (closing line value) is the quickest sign that it knows something the market doesn't yet.

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

## Power ratings

Points per game better than an average team on a neutral field, from opponent-adjusted EPA with this season's games weighted against a preseason prior. Defense is positive when it holds opponents below average.

| # | Team | Net | Offense | Defense | Special teams | Elo |
|---|---|---|---|---|---|---|
| 1 | BUF | +5.4 | +6.0 | -1.5 | +0.8 | 1653 |
| 2 | JAX | +4.1 | +2.7 | +0.8 | +0.6 | 1608 |
| 3 | SF | +3.7 | +4.3 | -0.1 | -0.5 | 1654 |
| 4 | SEA | +3.7 | -1.4 | +3.4 | +1.6 | 1652 |
| 5 | NE | +3.5 | +2.4 | +0.9 | +0.2 | 1618 |
| 6 | DET | +3.4 | +3.4 | -1.1 | +1.1 | 1554 |
| 7 | CHI | +3.2 | +1.9 | +0.1 | +1.2 | 1560 |
| 8 | KC | +3.0 | +2.9 | +0.7 | -0.6 | 1583 |
| 9 | BAL | +2.9 | +3.4 | +0.1 | -0.6 | 1557 |
| 10 | GB | +2.2 | +2.2 | +0.2 | -0.3 | 1537 |
| 11 | LA | +1.9 | +2.7 | +0.9 | -1.7 | 1559 |
| 12 | MIN | +1.6 | -2.8 | +3.0 | +1.4 | 1630 |
| 13 | CIN | +1.2 | +1.9 | -1.0 | +0.2 | 1526 |
| 14 | HOU | +0.9 | -0.4 | +1.6 | -0.3 | 1547 |
| 15 | DEN | +0.6 | -0.9 | +1.8 | -0.3 | 1613 |
| 16 | CAR | +0.4 | +1.2 | -0.9 | +0.2 | 1499 |
| 17 | IND | -0.4 | +0.1 | -1.0 | +0.5 | 1425 |
| 18 | PHI | -0.5 | -2.1 | +1.0 | +0.7 | 1486 |
| 19 | TB | -1.3 | -1.9 | +0.8 | -0.2 | 1427 |
| 20 | PIT | -1.5 | -1.4 | +0.1 | -0.2 | 1545 |
| 21 | DAL | -1.5 | +2.1 | -3.7 | +0.0 | 1433 |
| 22 | WAS | -1.7 | +0.0 | -1.5 | -0.3 | 1421 |
| 23 | NYG | -1.9 | -1.7 | -0.7 | +0.4 | 1434 |
| 24 | ATL | -2.5 | -1.6 | +0.3 | -1.2 | 1454 |
| 25 | NO | -2.8 | -1.8 | -0.7 | -0.4 | 1425 |
| 26 | NYJ | -2.9 | -2.7 | -0.7 | +0.5 | 1381 |
| 27 | CLE | -3.0 | -4.4 | +1.5 | -0.1 | 1459 |
| 28 | ARI | -3.4 | -1.1 | -1.3 | -1.0 | 1393 |
| 29 | MIA | -3.7 | -1.4 | -1.7 | -0.7 | 1373 |
| 30 | LV | -3.8 | -2.7 | -0.8 | -0.3 | 1421 |
| 31 | LAC | -3.8 | -4.6 | +1.2 | -0.4 | 1409 |
| 32 | TEN | -7.0 | -4.7 | -2.0 | -0.4 | 1325 |

## Current model fit

- Fitted on 1785 games from seasons 2020–2026.
- Home field: 1.6 points (2.0 in divisional games).
- QB adjustment: 0.83 points per point of QB value gap.
- Special teams: 0.45 points per point of net special-teams EPA.
- Weight on the betting line: 93% for the margin, 100% for the total.
- Wind: -0.19 total points per mph above 10 mph at open-air stadiums.
