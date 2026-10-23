# NBA score predictions

Updated Thu Oct 22, 2026 09:31 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the model's own chances before any blending with the line (its own simulated scores, pushes returning the stake). A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV and the model's chance of winning the bet. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment: the model alone is less accurate than the closing line, and its backtest found no edge against closing lines.

## Friday, October 23

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4:00 PM | CHI @ MIL | CHI 118, MIL 120 | MIL 55% | CHI +125 / MIL -125<br>posted CHI -105 / MIL -115 | MIL -1.9 / MIL -1.5 (fav covers 52%) | 237.6 / 237.5 (over 49%) | 103–133 / 105–134 | 5% | CHI: Josh Giddey (day-to-day); Jordan Hawkins (day-to-day); Nic Claxton (out); Zach Collins (day-to-day); Tobe Awaka (day-to-day) (+0.0) | MIL -1.5 (-105): EV +12.9%, model 58% | MIL ML (-115): EV +12.5%, model 60% | Under 237.5 (-110): EV +13.7%, model 60% |
| 7:00 PM | NYK @ BOS | NYK 111, BOS 114 | BOS 60% | NYK +150 / BOS -150<br>posted NYK +120 / BOS -142 | BOS -3 / BOS -2.5 (fav covers 53%) | 224.7 / 224.5 (over 50%) | 96–125 / 100–128 | 5% | BOS: Devin Carter (out) (+1.1) | BOS -2.5 (-110): EV +14.3%, model 60% | BOS ML (-142): EV +12.0%, model 66% | Under 224.5 (-115): EV +12.9%, model 60% |
| 7:00 PM | ATL @ CHA | ATL 114, CHA 112 | ATL 56% | ATL -130 / CHA +130<br>posted ATL -142 / CHA +120 | ATL -2.2 / ATL -2.5 (fav covers 51%) | 225.9 / 225.5 (over 50%) | 100–128 / 98–126 | 6% | CHA: Kon Knueppel (out); Coby White (out); Grant Williams (out) (-0.6) | CHA +2.5 (-108): EV +3.2%, model 54% | CHA ML (+120): EV +5.2%, model 48% | Over 225.5 (-110): EV +3.5%, model 54% |
| 7:00 PM | DAL @ IND | DAL 116, IND 121 | IND 64% | DAL +180 / IND -180<br>posted DAL +185 / IND -225 | IND -5.1 / IND -5.5 (fav covers 50%) | 236.5 / 236.5 (over 49%) | 101–131 / 106–136 | 4% | DAL: Santi Aldama (out); Dereck Lively II (out) (-0.3)<br>IND: Aaron Nesmith (day-to-day); Johnny Furphy (out); Ben Sheppard (day-to-day); T.J. McConnell (out) (+0.2) | no edge | DAL ML (+185): EV +7.1%, model 38% | Under 236.5 (-105): EV +27.4%, model 65% |
| 7:00 PM | MIN @ ORL | MIN 119, ORL 118 | MIN 51% | MIN -105 / ORL +105<br>posted MIN -125 / ORL +105 | MIN -0.3 / MIN -1.5 (fav covers 49%) | 236.4 / 236.5 (over 49%) | 104–133 / 103–133 | 5% | MIN: Donte DiVincenzo (out) (-0.3)<br>ORL: Anthony Black (out) (+1.6) | ORL +1.5 (-110): EV +22.9%, model 64% | ORL ML (+105): EV +27.0%, model 62% | Under 236.5 (-110): EV +22.1%, model 64% |
| 7:00 PM | TOR @ WAS | TOR 121, WAS 115 | TOR 66% | TOR -195 / WAS +195<br>posted TOR -218 / WAS +180 | TOR -5.6 / TOR -5.5 (fav covers 51%) | 236.5 / 236.5 (over 49%) | 107–135 / 101–130 | 5% | WAS: Jamir Watkins (out); Tristan Vukcevic (out) (+0.7) | TOR -5.5 (-105): EV +5.7%, model 54% | no edge | Under 236.5 (-112): EV +8.6%, model 57% |
| 8:00 PM | DET @ MIA | DET 120, MIA 118 | DET 54% | DET -120 / MIA +120<br>posted DET -110 / MIA -110 | DET -1.5 / DET -1.5 (fav covers 52%) | 237.8 / 237.5 (over 50%) | 105–134 / 103–133 | 5% | DET: Taurean Prince (day-to-day) (+0.2) | no edge | no edge | Under 237.5 (-112): EV +40.3%, model 74% |
| 9:30 PM | HOU @ SAS | HOU 111, SAS 116 | SAS 65% | HOU +185 / SAS -185<br>posted HOU +180 / SAS -218 | SAS -5.2 / SAS -5.5 (fav covers 50%) | 227.5 / 227.5 (over 49%) | 97–126 / 102–131 | 5% | HOU: Reed Sheppard (day-to-day); Steven Adams (day-to-day) (+0.3)<br>SAS: De'Aaron Fox (day-to-day); Tobias Harris (out); Keldon Johnson (day-to-day) (+0.9) | no edge | HOU ML (+180): EV +4.3%, model 37% | Under 227.5 (-115): EV +14.2%, model 61% |
| 9:30 PM | NOP @ UTA | NOP 118, UTA 121 | UTA 59% | NOP +145 / UTA -145<br>posted NOP +114 / UTA -135 | UTA -2.9 / UTA -2.5 (fav covers 53%) | 238.4 / 238.5 (over 50%) | 103–133 / 106–135 | 5% | UTA: Trey Alexander (out); Jusuf Nurkic (out) (+0.1) | UTA -2.5 (-112): EV +9.8%, model 58% | UTA ML (-135): EV +10.5%, model 63% | Under 238.5 (-105): EV +33.3%, model 68% |
| 10:00 PM | MEM @ GSW | MEM 116, GSW 120 | GSW 61% | MEM +155 / GSW -155<br>posted MEM +130 / GSW -155 | GSW -3.7 / GSW -3.5 (fav covers 52%) | 235.4 / 235.5 (over 49%) | 101–131 / 105–134 | 5% | MEM: Cedric Coward (day-to-day) (-0.1)<br>GSW: Brandin Podziemski (day-to-day); Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out) (-1.6) | no edge | no edge | Under 235.5 (-110): EV +20.6%, model 63% |
| 10:00 PM | LAC @ LAL | LAC 110, LAL 118 | LAL 73% | LAC +270 / LAL -270<br>posted LAC +310 / LAL -395 | LAL -8.3 / LAL -9.5 (fav covers 46%) | 228.4 / 228.5 (over 49%) | 95–125 / 104–133 | 4% | LAC: Max Strus (out); Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+1.1) | LAC +9.5 (-112): EV +25.9%, model 66% | LAC ML (+310): EV +58.0%, model 39% | Under 228.5 (-110): EV +20.6%, model 63% |
| 10:00 PM | POR @ SAC | POR 120, SAC 112 | POR 71% | POR -245 / SAC +245<br>posted POR -305 / SAC +245 | POR -7.8 / POR -7.5 (fav covers 51%) | 232.4 / 232.5 (over 49%) | 105–135 / 98–127 | 4% | POR: Branden Carlson (out) (+1.4)<br>SAC: Maxime Raynaud (out); Dylan Cardwell (out); Malik Monk (day-to-day) (+0.8) | no edge | no edge | Under 232.5 (-112): EV +41.5%, model 75% |

## Saturday, October 24

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6:00 PM | MIA @ CHA | MIA 113, CHA 114 | CHA 51% | MIA +105 / CHA -105 | pick'em | 225.3 | 98–127 / 98–127 | 5% | CHA: Kon Knueppel (out); Coby White (out); Grant Williams (out) (-0.6) | no line yet | no line yet | no line yet |
| 7:30 PM | BKN @ CLE | BKN 107, CLE 118 | CLE 80% | BKN +390 / CLE -390 | CLE -10.9 | 225.6 | 93–122 / 104–132 | 4% | – | no line yet | no line yet | no line yet |
| 7:30 PM | MIL @ PHI | MIL 109, PHI 120 | PHI 78% | MIL +365 / PHI -365 | PHI -10.6 | 229.2 | 95–124 / 105–134 | 4% | PHI: Dean Wade (out); Dominick Barlow (out) (-0.7) | no line yet | no line yet | no line yet |
| 8:00 PM | WAS @ CHI | WAS 118, CHI 119 | CHI 52% | WAS +105 / CHI -105 | CHI -0.5 | 236.9 | 103–133 / 104–134 | 5% | WAS: Jamir Watkins (out); Tristan Vukcevic (out) (+0.7)<br>CHI: Josh Giddey (day-to-day); Jordan Hawkins (day-to-day); Nic Claxton (out); Zach Collins (day-to-day); Tobe Awaka (day-to-day) (+0.0) | no line yet | no line yet | no line yet |
| 8:00 PM | SAS @ DAL | SAS 117, DAL 108 | SAS 74% | SAS -285 / DAL +285 | SAS -8.8 | 225.8 | 103–132 / 94–123 | 4% | SAS: De'Aaron Fox (day-to-day); Tobias Harris (out); Keldon Johnson (day-to-day) (+0.9)<br>DAL: Santi Aldama (out); Dereck Lively II (out) (-0.3) | no line yet | no line yet | no line yet |
| 8:30 PM | HOU @ ATL | HOU 116, ATL 115 | HOU 55% | HOU -125 / ATL +125 | HOU -1.7 | 231.3 | 102–131 / 100–129 | 5% | HOU: Reed Sheppard (day-to-day); Steven Adams (day-to-day) (+0.3) | no line yet | no line yet | no line yet |
| 9:00 PM | NOP @ DEN | NOP 111, DEN 125 | DEN 85% | NOP +560 / DEN -560 | DEN -14.5 | 236.0 | 96–126 / 111–140 | 3% | DEN: Spencer Jones (out) (+1.1) | no line yet | no line yet | no line yet |
| 10:00 PM | GSW @ PHX | GSW 110, PHX 116 | PHX 69% | GSW +225 / PHX -225 | PHX -6.4 | 226.0 | 95–125 / 102–130 | 5% | GSW: Brandin Podziemski (day-to-day); Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out) (-1.6)<br>PHX: Luke Kennard (day-to-day); Oso Ighodaro (day-to-day); Mark Williams (out) (+0.2) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 14 | 15.52 | 11.68 | 9.10 | 0.600 | 0.206 | 71.4% | 78.6% |
| Model only (before blending) | 14 | 17.21 | 11.38 | 10.33 | 0.704 | 0.254 | 57.1% | – |
| Elo | 14 | 16.12 | – | – | 0.654 | 0.231 | 57.1% | – |
| Final prediction, games with a line | 14 | 15.52 | 11.68 | 9.10 | 0.600 | 0.206 | 71.4% | 78.6% |
| Model only, games with a line | 14 | 17.21 | 11.38 | 10.33 | 0.704 | 0.254 | 57.1% | – |
| Betting line | 14 | 15.14 | 11.64 | 8.96 | 0.578 | 0.196 | 71.4% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 5.0% of games, happened in 0.0%.

### Betting edges

| Market | Edges | Record (W-L-P) | Units | ROI |
|---|---|---|---|---|
| Spread | 10 | 2-8-0 | -6.20 | -62.0% |
| Moneyline | 12 | 1-11-0 | -10.17 | -84.7% |
| Total | 12 | 8-4-0 | +3.44 | +28.7% |

Spread moved toward the model's first spread edge before tip-off: 1 of 1 games (100%).

Live predictions only, 1 unit on each edge at the price logged with the last prediction before tip-off; a push returns the stake. ROI is units won per unit bet. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Wednesday, October 21

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| ATL @ ORL | 115–118 | 132–125 | 40% | ORL -3.4 / ORL -2.5 | no |
| MIL @ WAS | 117–121 | 116–128 | 61% | WAS -3.8 / WAS -4.5 | yes |
| MIN @ MIA | 119–121 | 131–106 | 44% | MIA -2 / MIA -1.5 | no |
| CHA @ BKN | 111–109 | 110–103 | 55% | CHA -1.6 / CHA -1.5 | yes |
| CHI @ TOR | 114–124 | 92–135 | 76% | TOR -9.8 / TOR -10.5 | no |
| UTA @ MEM | 120–121 | 103–123 | 53% | MEM -1.2 / MEM -1.5 | no |
| IND @ NOP | 121–118 | 123–120 | 58% | IND -3.1 / IND -3.5 | yes |
| DAL @ HOU | 111–120 | 110–128 | 76% | HOU -9.3 / HOU -9.5 | yes |
| GSW @ LAL | 114–120 | 105–127 | 66% | LAL -5.7 / LAL -6.5 | yes |
| PHX @ POR | 115–118 | 83–124 | 60% | POR -3.4 / POR -3.5 | no |
| SAC @ LAC | 111–116 | 96–121 | 66% | LAC -5.5 / LAC -5.5 | yes |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | SAS | +6.9 | +7.3 | +1.9 | +5.0 | 106.2 | +0.9 | 1687 |
| 2 | BOS | +6.4 | +6.4 | +3.4 | +3.0 | 101.1 | +1.1 | 1602 |
| 3 | OKC | +6.0 | +6.4 | +1.1 | +4.9 | 105.2 | +2.0 | 1702 |
| 4 | HOU | +5.1 | +5.2 | +2.7 | +2.4 | 102.0 | +0.3 | 1576 |
| 5 | NYK | +4.3 | +4.5 | +1.1 | +3.3 | 104.0 | +0.0 | 1711 |
| 6 | POR | +3.3 | +3.3 | +1.5 | +1.7 | 101.6 | +1.5 | 1543 |
| 7 | DEN | +3.1 | +3.2 | +4.3 | -1.2 | 104.0 | +1.1 | 1596 |
| 8 | DET | +2.9 | +3.0 | +1.4 | +1.5 | 102.2 | +0.2 | 1623 |
| 9 | CLE | +2.9 | +3.0 | +2.6 | +0.3 | 103.3 | +0.0 | 1579 |
| 10 | TOR | +2.5 | +2.7 | +0.6 | +1.8 | 107.7 | +0.7 | 1556 |
| 11 | MIN | +1.7 | +1.8 | +0.9 | +0.7 | 106.7 | -0.3 | 1580 |
| 12 | ORL | +1.7 | +1.8 | -0.6 | +2.3 | 107.4 | +1.7 | 1540 |
| 13 | PHI | +1.7 | +1.8 | +0.1 | +1.6 | 105.6 | -0.7 | 1550 |
| 14 | ATL | +0.8 | +0.9 | +0.9 | +0.0 | 108.3 | +0.8 | 1543 |
| 15 | LAL | +0.8 | +0.9 | +0.8 | +0.0 | 102.5 | +1.0 | 1577 |
| 16 | MIA | +0.5 | +0.5 | +0.7 | -0.2 | 105.3 | +0.0 | 1501 |
| 17 | PHX | +0.1 | +0.1 | +0.9 | -0.8 | 100.9 | +0.2 | 1505 |
| 18 | GSW | -0.5 | -0.5 | +0.0 | -0.5 | 103.6 | -1.6 | 1444 |
| 19 | CHA | -0.8 | -0.8 | -1.6 | +0.8 | 103.4 | -0.6 | 1601 |
| 20 | IND | -1.0 | -1.1 | +0.5 | -1.6 | 105.6 | +0.2 | 1388 |
| 21 | LAC | -1.4 | -1.5 | -0.7 | -0.7 | 102.8 | +1.1 | 1532 |
| 22 | DAL | -2.8 | -2.9 | -1.4 | -1.4 | 103.7 | -0.3 | 1388 |
| 23 | UTA | -3.5 | -3.7 | -2.3 | -1.2 | 105.4 | +0.1 | 1329 |
| 24 | MEM | -3.8 | -4.0 | -1.1 | -2.7 | 105.1 | -0.1 | 1349 |
| 25 | MIL | -5.3 | -5.5 | -1.6 | -3.7 | 104.0 | +0.0 | 1374 |
| 26 | WAS | -5.9 | -6.2 | -2.3 | -3.6 | 106.1 | +0.7 | 1298 |
| 27 | NOP | -6.0 | -6.3 | -2.4 | -3.6 | 105.7 | +0.0 | 1421 |
| 28 | BKN | -6.2 | -6.4 | -3.6 | -2.6 | 103.6 | +0.1 | 1317 |
| 29 | SAC | -6.8 | -7.0 | -3.5 | -3.2 | 103.4 | +0.8 | 1367 |
| 30 | CHI | -6.8 | -7.5 | -4.4 | -2.4 | 109.5 | +0.0 | 1374 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Shai Gilgeous-Alexander | OKC | +5.7 | +5.1 | +0.6 | 37 |
| 2 | Nikola Jokic | DEN | +5.5 | +5.8 | -0.3 | 40 |
| 3 | Victor Wembanyama | SAS | +5.4 | +0.9 | +4.5 | 38 |
| 4 | Kawhi Leonard | TOR | +4.9 | +4.2 | +0.8 | 31 |
| 5 | Giannis Antetokounmpo | MIA | +4.7 | +4.1 | +0.6 | 28 |
| 6 | Alex Caruso | OKC | +3.9 | +0.0 | +3.9 | 27 |
| 7 | Luka Doncic | LAL | +3.0 | +3.9 | -0.9 | 32 |
| 8 | Joel Embiid | PHI | +3.0 | +1.7 | +1.3 | 32 |
| 9 | Franz Wagner | ORL | +2.6 | +1.2 | +1.4 | 29 |
| 10 | Kyrie Irving | DAL | +2.4 | +2.5 | -0.1 | 26 |
| 11 | Dyson Daniels | ATL | +2.4 | +1.4 | +0.9 | 28 |
| 12 | Chet Holmgren | OKC | +2.3 | +0.4 | +1.9 | 30 |
| 13 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 14 | Lauri Markkanen | UTA | +2.2 | +1.5 | +0.8 | 31 |
| 15 | Marcus Smart | HOU | +2.1 | +0.7 | +1.4 | 31 |
| 16 | Derrick White | BOS | +2.1 | +0.3 | +1.8 | 37 |
| 17 | Jarrett Allen | CLE | +2.0 | +1.6 | +0.4 | 30 |
| 18 | Pascal Siakam | IND | +1.9 | +1.7 | +0.2 | 32 |
| 19 | Fred VanVleet | HOU | +1.8 | +1.1 | +0.7 | 36 |
| 20 | Ausar Thompson | DET | +1.7 | -0.2 | +2.0 | 30 |
| 21 | Bam Adebayo | MIA | +1.7 | +0.8 | +0.9 | 27 |
| 22 | Rudy Gobert | MIN | +1.6 | -2.8 | +4.4 | 28 |
| 23 | Jrue Holiday | POR | +1.5 | +0.1 | +1.4 | 32 |
| 24 | OG Anunoby | NYK | +1.5 | -0.3 | +1.8 | 34 |
| 25 | Donovan Mitchell | CLE | +1.4 | +2.0 | -0.6 | 36 |
| 26 | Cade Cunningham | DET | +1.3 | +1.4 | -0.1 | 38 |
| 27 | Jayson Tatum | BOS | +1.2 | +1.2 | -0.1 | 36 |
| 28 | Damian Lillard | POR | +1.1 | +1.9 | -0.8 | 24 |
| 29 | Devin Vassell | SAS | +1.1 | +0.5 | +0.5 | 36 |
| 30 | Ty Jerome | MEM | +1.1 | +2.7 | -1.7 | 27 |

## Current model fit

- Fitted on 5296 games from 2022-23 to 2026-27.
- Home court: +2.1 points per 100 possessions for the home team over the visitor (about 2.1 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.16 (offense) and 0.17 (defense); player lineup ratings 0.76 and 0.75.
- Blend: 81% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.1% of recent games went to overtime.
