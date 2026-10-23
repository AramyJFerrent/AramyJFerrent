# NBA score predictions

Updated Fri Oct 23, 2026 01:56 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the model's own chances before any blending with the line (its own simulated scores, pushes returning the stake). A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV and the model's chance of winning the bet. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment: the model alone is less accurate than the closing line, and its backtest found no edge against closing lines.

## Friday, October 23

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4:00 PM | CHI @ MIL | CHI 119, MIL 121 | MIL 55% | CHI +125 / MIL -125<br>posted CHI -102 / MIL -118 | MIL -1.9 / MIL -1.5 (fav covers 53%) | 240.6 / 240.5 (over 49%) | 104–134 / 107–136 | 5% | CHI: Nic Claxton (out) (+0.0) | MIL -1.5 (-105): EV +13.0%, model 58% | MIL ML (-118): EV +11.2%, model 60% | Under 240.5 (-112): EV +24.8%, model 66% |
| 7:00 PM | NYK @ BOS | NYK 109, BOS 112 | BOS 60% | NYK +150 / BOS -150<br>posted NYK +114 / BOS -135 | BOS -3.1 / BOS -2.5 (fav covers 54%) | 221.8 / 221.5 (over 50%) | 95–124 / 98–127 | 6% | BOS: Devin Carter (out) (+1.1) | BOS -2.5 (-110): EV +14.4%, model 60% | BOS ML (-135): EV +14.9%, model 66% | Under 221.5 (-112): EV +4.9%, model 55% |
| 7:00 PM | ATL @ CHA | ATL 115, CHA 112 | ATL 56% | ATL -130 / CHA +130<br>posted ATL -142 / CHA +120 | ATL -2.2 / ATL -2.5 (fav covers 50%) | 226.9 / 226.5 (over 50%) | 100–129 / 98–127 | 6% | CHA: Kon Knueppel (out); Coby White (out); Grant Williams (out) (-0.5) | CHA +2.5 (-105): EV +4.6%, model 54% | CHA ML (+120): EV +5.3%, model 48% | no edge |
| 7:00 PM | DAL @ IND | DAL 116, IND 123 | IND 69% | DAL +220 / IND -220<br>posted DAL +215 / IND -265 | IND -6.7 / IND -7.5 (fav covers 49%) | 239.6 / 239.5 (over 49%) | 102–132 / 108–138 | 5% | DAL: Santi Aldama (out); Dereck Lively II (out) (-0.2)<br>IND: Aaron Nesmith (day-to-day); Johnny Furphy (out); Ben Sheppard (day-to-day); T.J. McConnell (out) (+0.2) | DAL +7.5 (-110): EV +12.4%, model 59% | DAL ML (+215): EV +18.3%, model 38% | Under 239.5 (-105): EV +38.3%, model 71% |
| 7:00 PM | MIN @ ORL | MIN 116, ORL 118 | ORL 56% | MIN +125 / ORL -125<br>posted MIN -108 / ORL -112 | ORL -2.1 / ORL -1.5 (fav covers 53%) | 234.5 / 234.5 (over 49%) | 101–131 / 104–133 | 5% | MIN: Donte DiVincenzo (out) (-0.3)<br>ORL: Anthony Black (out) (+1.6) | ORL -1.5 (-105): EV +15.9%, model 59% | ORL ML (-112): EV +17.2%, model 62% | Under 234.5 (-112): EV +14.3%, model 60% |
| 7:00 PM | TOR @ WAS | TOR 123, WAS 115 | TOR 72% | TOR -260 / WAS +260<br>posted TOR -340 / WAS +270 | TOR -8.1 / TOR -8.5 (fav covers 48%) | 237.5 / 237.5 (over 49%) | 108–137 / 100–130 | 5% | WAS: Jamir Watkins (out); Tristan Vukcevic (out) (+0.7) | WAS +8.5 (-105): EV +9.5%, model 56% | WAS ML (+270): EV +16.8%, model 32% | Under 237.5 (-112): EV +14.2%, model 60% |
| 8:00 PM | DET @ MIA | DET 119, MIA 117 | DET 54% | DET -120 / MIA +120<br>posted DET -125 / MIA +105 | DET -1.5 / DET -1.5 (fav covers 52%) | 235.9 / 235.5 (over 50%) | 104–133 / 102–132 | 6% | – | no edge | no edge | Under 235.5 (-112): EV +33.3%, model 70% |
| 9:30 PM | HOU @ SAS | HOU 110, SAS 114 | SAS 63% | HOU +170 / SAS -170<br>posted HOU +160 / SAS -192 | SAS -4.4 / SAS -4.5 (fav covers 51%) | 224.4 / 224.5 (over 49%) | 96–124 / 100–129 | 5% | HOU: Reed Sheppard (day-to-day); Steven Adams (day-to-day) (+0.3)<br>SAS: De'Aaron Fox (day-to-day); Tobias Harris (out); Keldon Johnson (day-to-day) (+0.9) | no edge | no edge | no edge |
| 9:30 PM | NOP @ UTA | NOP 119, UTA 121 | UTA 57% | NOP +130 / UTA -130<br>posted NOP -108 / UTA -112 | UTA -2.1 / UTA -1.5 (fav covers 54%) | 239.5 / 239.5 (over 49%) | 104–134 / 106–136 | 5% | UTA: Trey Alexander (out); Jusuf Nurkic (out) (+0.0) | UTA -1.5 (-102): EV +21.5%, model 61% | UTA ML (-112): EV +20.4%, model 64% | Under 239.5 (-108): EV +35.5%, model 70% |
| 10:00 PM | MEM @ GSW | MEM 116, GSW 121 | GSW 63% | MEM +170 / GSW -170<br>posted MEM +145 / GSW -175 | GSW -4.5 / GSW -4.5 (fav covers 51%) | 237.5 / 237.5 (over 49%) | 102–131 / 106–135 | 5% | MEM: Cedric Coward (day-to-day) (-0.1)<br>GSW: Brandin Podziemski (day-to-day); Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out) (-1.6) | no edge | no edge | Under 237.5 (-110): EV +29.4%, model 68% |
| 10:00 PM | LAC @ LAL | LAC 109, LAL 116 | LAL 71% | LAC +245 / LAL -245<br>posted LAC +295 / LAL -375 | LAL -7.5 / LAL -8.5 (fav covers 47%) | 225.5 / 225.5 (over 50%) | 94–124 / 102–131 | 5% | LAC: Max Strus (out); Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+1.1) | LAC +8.5 (-108): EV +21.9%, model 63% | LAC ML (+295): EV +52.7%, model 39% | Under 225.5 (-105): EV +10.2%, model 56% |
| 10:00 PM | POR @ SAC | POR 122, SAC 112 | POR 77% | POR -330 / SAC +330<br>posted POR -470 / SAC +360 | POR -10.2 / POR -10.5 (fav covers 48%) | 233.4 / 233.5 (over 49%) | 107–136 / 97–127 | 4% | POR: Branden Carlson (out) (+1.5)<br>SAC: Maxime Raynaud (out); Dylan Cardwell (out); Malik Monk (day-to-day) (+0.8) | SAC +10.5 (-112): EV +7.2%, model 57% | SAC ML (+360): EV +19.9%, model 26% | Under 233.5 (-115): EV +42.9%, model 76% |

## Saturday, October 24

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6:00 PM | MIA @ CHA | MIA 113, CHA 114 | CHA 51% | MIA +105 / CHA -105 | pick'em | 225.2 | 98–127 / 98–127 | 6% | CHA: Kon Knueppel (out); Coby White (out); Grant Williams (out) (-0.5) | no line yet | no line yet | no line yet |
| 7:30 PM | BKN @ CLE | BKN 108, CLE 120 | CLE 81% | BKN +420 / CLE -420 | CLE -11.5 | 227.8 | 94–123 / 105–134 | 4% | – | no line yet | no line yet | no line yet |
| 7:30 PM | MIL @ PHI | MIL 109, PHI 121 | PHI 81% | MIL +425 / PHI -425 | PHI -11.8 | 230.3 | 95–124 / 107–135 | 4% | PHI: Joel Embiid (day-to-day); Dominick Barlow (out) (-0.7) | no line yet | no line yet | no line yet |
| 8:00 PM | WAS @ CHI | WAS 118, CHI 119 | CHI 52% | WAS +105 / CHI -105 | CHI -0.5 | 236.8 | 103–133 / 104–134 | 5% | WAS: Jamir Watkins (out); Tristan Vukcevic (out) (+0.7)<br>CHI: Nic Claxton (out) (+0.0) | no line yet | no line yet | no line yet |
| 8:00 PM | SAS @ DAL | SAS 118, DAL 109 | SAS 74% | SAS -290 / DAL +290 | SAS -8.9 | 226.8 | 103–132 / 94–124 | 4% | SAS: De'Aaron Fox (day-to-day); Tobias Harris (out); Keldon Johnson (day-to-day) (+0.9)<br>DAL: Santi Aldama (out); Dereck Lively II (out) (-0.2) | no line yet | no line yet | no line yet |
| 8:30 PM | HOU @ ATL | HOU 116, ATL 115 | HOU 55% | HOU -125 / ATL +125 | HOU -1.6 | 231.2 | 102–131 / 100–129 | 5% | HOU: Reed Sheppard (day-to-day); Steven Adams (day-to-day) (+0.3) | no line yet | no line yet | no line yet |
| 9:00 PM | NOP @ DEN | NOP 108, DEN 121 | DEN 82% | NOP +465 / DEN -465 | DEN -12.8 | 228.4 | 93–123 / 106–135 | 3% | DEN: Spencer Jones (day-to-day); Cameron Johnson (day-to-day) (+0.4) | no line yet | no line yet | no line yet |
| 10:00 PM | GSW @ PHX | GSW 110, PHX 116 | PHX 69% | GSW +225 / PHX -225 | PHX -6.5 | 225.9 | 95–124 / 102–130 | 5% | GSW: Brandin Podziemski (day-to-day); Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out) (-1.6)<br>PHX: Luke Kennard (day-to-day); Oso Ighodaro (day-to-day); Mark Williams (out) (+0.2) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 16 | 14.21 | 14.86 | 10.29 | 0.581 | 0.197 | 75.0% | 75.0% |
| Model only (before blending) | 16 | 15.78 | 13.52 | 10.82 | 0.674 | 0.240 | 62.5% | – |
| Elo | 16 | 14.87 | – | – | 0.628 | 0.218 | 62.5% | – |
| Final prediction, games with a line | 16 | 14.21 | 14.86 | 10.29 | 0.581 | 0.197 | 75.0% | 75.0% |
| Model only, games with a line | 16 | 15.78 | 13.52 | 10.82 | 0.674 | 0.240 | 62.5% | – |
| Betting line | 16 | 13.88 | 14.81 | 10.16 | 0.560 | 0.188 | 75.0% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.9% of games, happened in 0.0%.

### Betting edges

| Market | Edges | Record (W-L-P) | Units | ROI |
|---|---|---|---|---|
| Spread | 11 | 2-9-0 | -7.20 | -65.4% |
| Moneyline | 13 | 1-12-0 | -11.17 | -85.9% |
| Total | 14 | 10-4-0 | +5.24 | +37.4% |

Spread moved toward the model's first spread edge before tip-off: 4 of 5 games (80%).

Live predictions only, 1 unit on each edge at the price logged with the last prediction before tip-off; a push returns the stake. ROI is units won per unit bet. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Thursday, October 22

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| CLE @ PHI | 118–120 | 106–114 | 58% | PHI -2.4 / PHI -2.5 | yes |
| DEN @ OKC | 115–122 | 84–96 | 71% | OKC -7.4 / OKC -7.5 | no |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | SAS | +6.9 | +7.3 | +2.0 | +4.8 | 106.9 | +0.9 | 1687 |
| 2 | OKC | +6.4 | +6.5 | +0.7 | +5.7 | 102.0 | +2.0 | 1708 |
| 3 | BOS | +6.3 | +6.4 | +3.5 | +2.9 | 101.0 | +1.1 | 1602 |
| 4 | HOU | +5.1 | +5.2 | +2.8 | +2.3 | 101.9 | +0.3 | 1576 |
| 5 | NYK | +4.3 | +4.4 | +1.2 | +3.1 | 103.2 | +0.0 | 1711 |
| 6 | POR | +3.2 | +3.3 | +1.6 | +1.7 | 101.6 | +1.5 | 1543 |
| 7 | CLE | +3.2 | +3.4 | +2.2 | +1.0 | 106.3 | +0.0 | 1572 |
| 8 | DET | +2.9 | +2.9 | +1.5 | +1.4 | 102.2 | +0.0 | 1623 |
| 9 | PHI | +2.5 | +2.7 | +0.1 | +2.4 | 108.0 | -0.7 | 1557 |
| 10 | TOR | +2.4 | +2.6 | +0.7 | +1.7 | 107.6 | +0.7 | 1556 |
| 11 | DEN | +2.4 | +2.4 | +3.1 | -0.7 | 100.0 | +0.4 | 1591 |
| 12 | ORL | +1.7 | +1.8 | -0.5 | +2.2 | 107.3 | +1.7 | 1540 |
| 13 | MIN | +1.6 | +1.8 | +1.0 | +0.6 | 106.6 | -0.3 | 1580 |
| 14 | ATL | +0.8 | +0.9 | +1.0 | -0.1 | 108.2 | +0.8 | 1543 |
| 15 | LAL | +0.8 | +0.8 | +0.9 | -0.1 | 102.5 | +1.0 | 1577 |
| 16 | MIA | +0.5 | +0.5 | +0.8 | -0.3 | 105.2 | +0.0 | 1501 |
| 17 | PHX | +0.1 | +0.1 | +1.0 | -0.9 | 100.9 | +0.2 | 1505 |
| 18 | GSW | -0.5 | -0.5 | +0.0 | -0.5 | 103.6 | -1.6 | 1444 |
| 19 | CHA | -0.8 | -0.8 | -1.5 | +0.7 | 103.3 | -0.5 | 1601 |
| 20 | IND | -1.0 | -1.1 | +0.6 | -1.7 | 105.6 | +0.2 | 1388 |
| 21 | LAC | -1.4 | -1.5 | -0.7 | -0.8 | 102.7 | +1.1 | 1532 |
| 22 | DAL | -2.8 | -2.9 | -1.3 | -1.5 | 103.6 | -0.3 | 1388 |
| 23 | UTA | -3.6 | -3.7 | -2.3 | -1.3 | 105.4 | +0.1 | 1329 |
| 24 | MEM | -3.8 | -4.0 | -1.0 | -2.8 | 105.1 | -0.1 | 1349 |
| 25 | MIL | -5.3 | -5.6 | -1.5 | -3.8 | 104.0 | +0.0 | 1374 |
| 26 | WAS | -5.9 | -6.3 | -2.2 | -3.7 | 106.0 | +0.7 | 1298 |
| 27 | NOP | -6.0 | -6.3 | -2.3 | -3.7 | 105.6 | +0.0 | 1421 |
| 28 | BKN | -6.2 | -6.4 | -3.5 | -2.7 | 103.5 | +0.1 | 1317 |
| 29 | SAC | -6.8 | -7.0 | -3.4 | -3.4 | 103.3 | +0.8 | 1367 |
| 30 | CHI | -6.9 | -7.5 | -4.3 | -2.5 | 109.3 | +0.0 | 1374 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Shai Gilgeous-Alexander | OKC | +6.0 | +5.1 | +0.9 | 36 |
| 2 | Victor Wembanyama | SAS | +5.4 | +0.9 | +4.5 | 38 |
| 3 | Nikola Jokic | DEN | +5.2 | +5.4 | -0.2 | 38 |
| 4 | Kawhi Leonard | TOR | +4.9 | +4.2 | +0.7 | 31 |
| 5 | Giannis Antetokounmpo | MIA | +4.7 | +4.1 | +0.6 | 28 |
| 6 | Alex Caruso | OKC | +4.0 | -0.2 | +4.2 | 25 |
| 7 | Joel Embiid | PHI | +3.2 | +1.7 | +1.5 | 33 |
| 8 | Luka Doncic | LAL | +3.0 | +3.9 | -0.9 | 32 |
| 9 | Franz Wagner | ORL | +2.6 | +1.2 | +1.4 | 29 |
| 10 | Kyrie Irving | DAL | +2.4 | +2.6 | -0.1 | 26 |
| 11 | Chet Holmgren | OKC | +2.4 | +0.4 | +2.0 | 29 |
| 12 | Dyson Daniels | ATL | +2.4 | +1.5 | +0.9 | 28 |
| 13 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 14 | Lauri Markkanen | UTA | +2.2 | +1.5 | +0.7 | 31 |
| 15 | Marcus Smart | HOU | +2.2 | +0.8 | +1.4 | 31 |
| 16 | Derrick White | BOS | +2.1 | +0.3 | +1.8 | 37 |
| 17 | Pascal Siakam | IND | +2.0 | +1.8 | +0.2 | 32 |
| 18 | Jarrett Allen | CLE | +1.9 | +1.3 | +0.7 | 29 |
| 19 | Fred VanVleet | HOU | +1.8 | +1.2 | +0.6 | 36 |
| 20 | Ausar Thompson | DET | +1.8 | -0.2 | +1.9 | 30 |
| 21 | Bam Adebayo | MIA | +1.7 | +0.8 | +0.9 | 27 |
| 22 | Rudy Gobert | MIN | +1.6 | -2.8 | +4.4 | 28 |
| 23 | Jrue Holiday | POR | +1.5 | +0.1 | +1.4 | 32 |
| 24 | OG Anunoby | NYK | +1.5 | -0.2 | +1.7 | 34 |
| 25 | Cade Cunningham | DET | +1.3 | +1.4 | -0.1 | 38 |
| 26 | Donovan Mitchell | CLE | +1.3 | +1.8 | -0.6 | 36 |
| 27 | Jayson Tatum | BOS | +1.2 | +1.3 | -0.1 | 36 |
| 28 | Damian Lillard | POR | +1.1 | +1.9 | -0.8 | 24 |
| 29 | Devin Vassell | SAS | +1.1 | +0.6 | +0.5 | 36 |
| 30 | Ty Jerome | MEM | +1.1 | +2.8 | -1.7 | 27 |

## Current model fit

- Fitted on 5298 games from 2022-23 to 2026-27.
- Home court: +2.1 points per 100 possessions for the home team over the visitor (about 2.1 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.17 (offense) and 0.16 (defense); player lineup ratings 0.76 and 0.75.
- Blend: 81% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.1% of recent games went to overtime.
