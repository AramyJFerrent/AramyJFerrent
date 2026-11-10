# NBA score predictions

Updated Mon Nov 09, 2026 07:52 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Monday, November 9

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8:00 PM | IND @ DAL | IND 111, DAL 116 | DAL 63% | IND +170 / DAL -170<br>posted IND +160 / DAL -191 | DAL -4.6 / DAL -4.5 (fav covers 52%) | 227.5 / 227.5 (over 49%) | 97–126 / 102–130 | 5% | IND: Tyrese Haliburton (out); Johnny Furphy (out); Ben Sheppard (out) (-0.3)<br>DAL: Morez Johnson Jr. (out); Dereck Lively II (out); Sergio de Larrea (out) (+1.8) | no edge | no edge | no edge |
| 8:30 PM | DEN @ HOU | DEN 110, HOU 114 | HOU 63% | DEN +170 / HOU -170<br>posted DEN +154 / HOU -183 | HOU -4.6 / HOU -4.5 (fav covers 52%) | 223.7 / 223.5 (over 50%) | 95–124 / 100–128 | 5% | HOU: Steven Adams (out); Clint Capela (out) (-0.4) | no edge | no edge | no edge |
| 9:00 PM | SAS @ PHX | SAS 117, PHX 108 | SAS 73% | SAS -275 / PHX +275<br>posted SAS -396 / PHX +312 | SAS -8.5 / SAS -9.5 (fav covers 47%) | 225.5 / 225.5 (over 50%) | 103–131 / 94–123 | 4% | SAS: Tobias Harris (out); Devin Vassell (out) (-0.5)<br>PHX: Mark Williams (out); Jordan Goodwin (out) (+0.3) | no edge | PHX ML (+312): EV +7.0%, 26%, stake 0.6u | no edge |
| 10:00 PM | NOP @ GSW | NOP 109, GSW 120 | GSW 81% | NOP +425 / GSW -425<br>posted NOP +426 / GSW -569 | GSW -11.9 / GSW -11.5 (fav covers 50%) | 229.1 / 229.5 (over 48%) | 94–123 / 106–135 | 3% | NOP: Zion Williamson (out); Trey Murphy III (out); Yves Missi (out); Trendon Watford (out) (-2.3)<br>GSW: Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out); Will Richard (out); Gui Santos (day-to-day); Gary Payton II (day-to-day) (+0.1) | no edge | no edge | no edge |

## Tuesday, November 10

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:30 PM | MIL @ NYK | MIL 102, NYK 117 | NYK 87% | MIL +695 / NYK -695<br>posted MIL +710 / NYK -1120 | NYK -15.2 / NYK -15.5 (fav covers 48%) | 219.0 / 219.5 (over 48%) | 88–117 / 103–131 | 3% | MIL: Tyler Herro (day-to-day) (-0.3)<br>NYK: Josh Hart (day-to-day) (-0.1) | no edge | no edge | no edge |
| 8:00 PM | BOS @ PHI | BOS 108, PHI 109 | PHI 52% | BOS +110 / PHI -110<br>posted BOS -109 / PHI -109 | PHI -0.8 / PHI -1.5 (fav covers 50%) | 215.9 / 215.5 (over 50%) | 93–122 / 94–122 | 6% | PHI: Adem Bona (out); Dominick Barlow (out) (+0.5) | no edge | no edge | no edge |
| 9:00 PM | LAC @ PHX | LAC 113, PHX 115 | PHX 57% | LAC +130 / PHX -130 | PHX -2.5 | 228.3 | 98–128 / 101–130 | 5% | LAC: Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+0.7)<br>PHX: Mark Williams (out); Jordan Goodwin (out) (+0.3) | no line yet | no line yet | no line yet |
| 9:00 PM | MIA @ UTA | MIA 115, UTA 113 | MIA 55% | MIA -120 / UTA +120 | MIA -1.5 | 228.0 | 100–129 / 99–128 | 5% | MIA: Giannis Antetokounmpo (day-to-day) (-0.9)<br>UTA: Lauri Markkanen (day-to-day); Keyonte George (out); Jaren Jackson Jr. (out); Jusuf Nurkic (out) (-0.8) | no line yet | no line yet | no line yet |
| 10:00 PM | ORL @ SAC | ORL 114, SAC 110 | ORL 62% | ORL -165 / SAC +165 | ORL -3.8 | 223.4 | 99–128 / 95–124 | 5% | ORL: Paolo Banchero (out); Jalen Suggs (out) (+0.2)<br>SAC: Maxime Raynaud (out); Domantas Sabonis (day-to-day); Keegan Murray (day-to-day) (+0.2) | no line yet | no line yet | no line yet |
| 11:00 PM | OKC @ POR | OKC 114, POR 113 | OKC 54% | OKC -115 / POR +115<br>posted OKC -122 / POR +103 | OKC -1.3 / OKC -1.5 (fav covers 51%) | 226.7 / 226.5 (over 49%) | 100–128 / 98–127 | 5% | OKC: Chet Holmgren (out); Jalen Williams (out); Jaylin Williams (out); Cason Wallace (out) (-0.2)<br>POR: Ja Morant (out); Robert Williams III (day-to-day) (-0.6) | no edge | no edge | no edge |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 146 | 10.94 | 14.46 | 9.36 | 0.558 | 0.189 | 71.2% | 81.2% |
| Model only (before blending) | 146 | 11.32 | 14.26 | 9.45 | 0.584 | 0.200 | 69.9% | – |
| Elo | 146 | 11.66 | – | – | 0.602 | 0.210 | 65.1% | – |
| Final prediction, games with a line | 146 | 10.94 | 14.46 | 9.36 | 0.558 | 0.189 | 71.2% | 81.2% |
| Model only, games with a line | 146 | 11.32 | 14.26 | 9.45 | 0.584 | 0.200 | 69.9% | – |
| Betting line | 146 | 10.88 | 14.46 | 9.35 | 0.548 | 0.185 | 71.2% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.7% of games, happened in 5.5%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 8 | 0-8-0 | 2.9 | -2.91 | -100.0% | +8.6% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 4 of 5 games (80%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Sunday, November 8

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| PHI @ CHI | 124–115 | 127–121 | 75% | PHI -9.5 / PHI -9.5 | yes |
| LAL @ DET | 105–112 | 121–116 | 29% | DET -7.4 / DET -7.5 | no |
| UTA @ MIN | 105–117 | 100–115 | 82% | MIN -12.4 / MIN -12.5 | yes |
| BKN @ DAL | 108–115 | 93–130 | 71% | DAL -7.6 / DAL -7.5 | no |
| BOS @ MIL | 117–104 | 117–97 | 82% | BOS -12.5 / BOS -12.5 | yes |
| NOP @ LAC | 114–113 | 123–139 | 47% | NOP -0.9 / NOP -1.5 | no |
| MIA @ SAC | 123–113 | 114–108 | 77% | MIA -10.3 / MIA -11.5 | yes |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | HOU | +7.1 | +7.0 | +3.2 | +3.9 | 99.0 | -0.4 | 1613 |
| 2 | SAS | +7.0 | +7.2 | +2.8 | +4.2 | 102.4 | -0.5 | 1712 |
| 3 | BOS | +6.9 | +6.6 | +3.7 | +3.2 | 95.2 | +0.0 | 1646 |
| 4 | DET | +6.1 | +6.2 | +2.3 | +3.8 | 100.8 | -0.1 | 1643 |
| 5 | MIN | +5.6 | +5.7 | +2.5 | +3.1 | 102.4 | -0.8 | 1622 |
| 6 | LAL | +5.2 | +5.3 | +4.8 | +0.4 | 102.0 | -2.0 | 1609 |
| 7 | NYK | +4.0 | +3.8 | +1.2 | +2.7 | 95.6 | -0.1 | 1701 |
| 8 | OKC | +3.9 | +4.0 | -0.2 | +4.2 | 102.1 | -0.2 | 1685 |
| 9 | DEN | +3.2 | +3.1 | +3.9 | -0.8 | 97.6 | +0.2 | 1582 |
| 10 | GSW | +3.1 | +3.1 | +1.9 | +1.2 | 102.0 | +0.1 | 1523 |
| 11 | PHI | +2.4 | +2.5 | +0.0 | +2.4 | 101.1 | +0.6 | 1577 |
| 12 | POR | +2.0 | +2.0 | +1.8 | +0.2 | 102.6 | -0.6 | 1544 |
| 13 | CLE | +1.7 | +1.7 | +1.9 | -0.2 | 101.8 | -0.3 | 1578 |
| 14 | TOR | +0.7 | +0.7 | +0.2 | +0.5 | 105.2 | -4.2 | 1552 |
| 15 | PHX | +0.2 | +0.2 | +1.2 | -1.0 | 101.3 | +0.3 | 1498 |
| 16 | DAL | +0.0 | +0.0 | -0.1 | +0.1 | 100.8 | +1.8 | 1447 |
| 17 | MIA | -0.5 | -0.5 | +0.8 | -1.2 | 105.1 | -0.9 | 1491 |
| 18 | ORL | -1.6 | -1.6 | -2.5 | +0.9 | 100.2 | +0.2 | 1489 |
| 19 | ATL | -2.2 | -2.3 | -0.9 | -1.3 | 108.4 | +1.9 | 1549 |
| 20 | IND | -2.5 | -2.6 | -1.2 | -1.3 | 102.4 | -0.3 | 1358 |
| 21 | LAC | -2.6 | -2.6 | -0.8 | -1.8 | 100.0 | +0.7 | 1485 |
| 22 | MEM | -2.7 | -2.8 | -0.8 | -1.9 | 103.8 | +0.3 | 1402 |
| 23 | NOP | -3.3 | -3.4 | -0.6 | -2.6 | 104.3 | -2.3 | 1429 |
| 24 | UTA | -3.8 | -3.9 | -3.8 | -0.1 | 101.5 | -0.8 | 1297 |
| 25 | WAS | -5.4 | -5.4 | -3.3 | -2.1 | 101.0 | +0.7 | 1331 |
| 26 | CHA | -6.1 | -5.9 | -4.9 | -1.2 | 96.4 | -2.1 | 1467 |
| 27 | BKN | -6.4 | -6.5 | -3.7 | -2.7 | 102.4 | +0.6 | 1306 |
| 28 | CHI | -7.1 | -7.8 | -3.2 | -3.9 | 110.7 | -0.3 | 1351 |
| 29 | SAC | -7.5 | -7.7 | -3.3 | -4.2 | 101.9 | +0.2 | 1334 |
| 30 | MIL | -7.6 | -7.7 | -3.0 | -4.6 | 102.1 | -0.3 | 1330 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +7.4 | +2.2 | +5.3 | 27 |
| 2 | Shai Gilgeous-Alexander | OKC | +6.0 | +5.2 | +0.9 | 31 |
| 3 | Nikola Jokic | DEN | +5.2 | +5.1 | +0.1 | 35 |
| 4 | Kawhi Leonard | TOR | +4.5 | +3.6 | +0.9 | 30 |
| 5 | Luka Doncic | LAL | +4.4 | +5.3 | -0.8 | 36 |
| 6 | Giannis Antetokounmpo | MIA | +3.8 | +3.7 | +0.2 | 34 |
| 7 | Kyrie Irving | DAL | +3.5 | +3.5 | +0.0 | 30 |
| 8 | Joel Embiid | PHI | +3.0 | +1.4 | +1.5 | 29 |
| 9 | Donovan Mitchell | CLE | +2.7 | +3.0 | -0.4 | 34 |
| 10 | Herbert Jones | NOP | +2.6 | -0.4 | +3.0 | 22 |
| 11 | Stephen Curry | GSW | +2.4 | +4.6 | -2.1 | 32 |
| 12 | Fred VanVleet | HOU | +2.4 | +1.7 | +0.7 | 30 |
| 13 | LaMelo Ball | MIN | +2.3 | +4.2 | -1.9 | 31 |
| 14 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 15 | Marcus Smart | HOU | +2.1 | +1.0 | +1.0 | 21 |
| 16 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.1 | 30 |
| 17 | Franz Wagner | ORL | +2.0 | +1.0 | +1.0 | 39 |
| 18 | Dyson Daniels | ATL | +1.9 | +0.4 | +1.5 | 32 |
| 19 | Ausar Thompson | DET | +1.9 | -0.2 | +2.0 | 27 |
| 20 | Rudy Gobert | MIN | +1.9 | -3.1 | +5.0 | 29 |
| 21 | Pascal Siakam | IND | +1.7 | +1.5 | +0.2 | 32 |
| 22 | Derrick White | BOS | +1.7 | +0.3 | +1.4 | 29 |
| 23 | Ty Jerome | MEM | +1.7 | +2.9 | -1.3 | 30 |
| 24 | Neemias Queta | BOS | +1.7 | +0.8 | +0.8 | 22 |
| 25 | Dean Wade | PHI | +1.6 | +0.4 | +1.2 | 21 |
| 26 | De'Aaron Fox | SAS | +1.5 | +1.5 | +0.0 | 26 |
| 27 | Bam Adebayo | MIA | +1.4 | +1.0 | +0.4 | 34 |
| 28 | Cade Cunningham | DET | +1.4 | +1.5 | -0.1 | 36 |
| 29 | Lauri Markkanen | UTA | +1.3 | +1.1 | +0.2 | 33 |
| 30 | Anthony Davis | WAS | +1.3 | -0.1 | +1.4 | 32 |

## Current model fit

- Fitted on 5428 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.8 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.17 (offense) and 0.15 (defense); player lineup ratings 0.76 and 0.75.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.2% of recent games went to overtime.
