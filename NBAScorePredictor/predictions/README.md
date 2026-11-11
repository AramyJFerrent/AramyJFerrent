# NBA score predictions

Updated Wed Nov 11, 2026 02:28 AM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Wednesday, November 11

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | WAS @ IND | WAS 111, IND 115 | IND 61% | WAS +160 / IND -160<br>posted WAS +139 / IND -166 | IND -3.8 / IND -3.5 (fav covers 52%) | 225.8 / 225.5 (over 50%) | 96–126 / 101–129 | 5% | WAS: Jamir Watkins (out); Justin Champagnie (out); Tristan Vukcevic (out) (+0.0)<br>IND: Tyrese Haliburton (out); Johnny Furphy (out); Ben Sheppard (out) (-0.2) | no edge | no edge | no edge |
| 7:00 PM | CLE @ NYK | CLE 109, NYK 113 | NYK 62% | CLE +165 / NYK -165<br>posted CLE +140 / NYK -166 | NYK -4.2 / NYK -4.5 (fav covers 50%) | 221.6 / 221.5 (over 50%) | 94–123 / 99–127 | 5% | CLE: Sam Merrill (out); Jaylon Tyson (out) (-0.5)<br>NYK: Josh Hart (out) (-0.2) | no edge | no edge | no edge |
| 7:00 PM | BOS @ TOR | BOS 111, TOR 104 | BOS 71% | BOS -240 / TOR +240<br>posted BOS -279 / TOR +228 | BOS -7.1 / BOS -7.5 (fav covers 49%) | 215.6 / 215.5 (over 49%) | 98–125 / 90–119 | 5% | TOR: Scottie Barnes (out); Immanuel Quickley (day-to-day); Kawhi Leonard (out); Collin Murray-Boyles (day-to-day) (-3.1) | no edge | no edge | no edge |
| 8:00 PM | SAS @ CHI | SAS 128, CHI 112 | SAS 86% | SAS -635 / CHI +635<br>posted SAS -1200 / CHI +750 | SAS -15.6 / SAS -15.5 (fav covers 49%) | 240.0 / 240.5 (over 48%) | 113–142 / 97–128 | 3% | SAS: Tobias Harris (out); Devin Vassell (day-to-day) (+0.6)<br>CHI: Norman Powell (day-to-day) (-0.2) | no edge | no edge | no edge |
| 8:00 PM | DEN @ MEM | DEN 116, MEM 113 | DEN 60% | DEN -150 / MEM +150<br>posted DEN -174 / MEM +146 | DEN -3.3 / DEN -3.5 (fav covers 51%) | 228.7 / 228.5 (over 49%) | 101–131 / 98–127 | 6% | MEM: Isaiah Stewart (day-to-day); Scotty Pippen Jr. (out) (+0.8) | no edge | no edge | no edge |
| 8:00 PM | LAL @ MIL | LAL 122, MIL 110 | LAL 81% | LAL -425 / MIL +425<br>posted LAL -578 / MIL +431 | LAL -12.1 / LAL -11.5 (fav covers 51%) | 232.3 / 232.5 (over 49%) | 108–136 / 95–125 | 4% | LAL: Quentin Grimes (day-to-day) (+0.2)<br>MIL: Tyler Herro (out) (-1.0) | no edge | no edge | no edge |
| 8:00 PM | BKN @ NOP | BKN 113, NOP 117 | NOP 62% | BKN +165 / NOP -165<br>posted BKN +156 / NOP -186 | NOP -4.2 / NOP -4.5 (fav covers 51%) | 229.7 / 229.5 (over 49%) | 98–127 / 103–131 | 5% | BKN: Nolan Traore (day-to-day); Egor Demin (out) (+0.5)<br>NOP: Trey Murphy III (day-to-day); Yves Missi (out); Trendon Watford (out) (+0.3) | no edge | no edge | no edge |
| 9:00 PM | ORL @ UTA | ORL 111, UTA 107 | ORL 63% | ORL -170 / UTA +170<br>posted ORL -166 / UTA +140 | ORL -4.3 / ORL -4.5 (fav covers 51%) | 217.4 / 217.5 (over 49%) | 97–125 / 92–121 | 4% | ORL: Paolo Banchero (out); Jalen Suggs (out); Tristan da Silva (out) (+1.3)<br>UTA: Lauri Markkanen (out); Keyonte George (out); Jaren Jackson Jr. (out); Jusuf Nurkic (out) (-2.3) | no edge | no edge | no edge |
| 9:30 PM | GSW @ HOU | GSW 108, HOU 114 | HOU 68% | GSW +215 / HOU -215<br>posted GSW +196 / HOU -237 | HOU -6.1 / HOU -6.5 (fav covers 50%) | 221.6 / 221.5 (over 49%) | 93–122 / 100–128 | 5% | GSW: Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out); Will Richard (out); Gary Payton II (out); Brandon Williams (out) (+0.2)<br>HOU: Steven Adams (out); Clint Capela (out) (-0.6) | no edge | no edge | no edge |
| 10:00 PM | OKC @ POR | OKC 114, POR 113 | OKC 54% | OKC -115 / POR +115<br>posted OKC -116 / POR -102 | OKC -1.3 / OKC -1.5 (fav covers 51%) | 226.7 / 226.5 (over 50%) | 100–128 / 98–127 | 5% | OKC: Chet Holmgren (out); Jalen Williams (out); Jaylin Williams (out); Cason Wallace (out) (-0.2)<br>POR: Ja Morant (out) (-0.4) | no edge | no edge | no edge |

## Thursday, November 12

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | TOR @ PHI | TOR 107, PHI 117 | PHI 77% | TOR +345 / PHI -345 | PHI -10.2 | 224.6 | 93–122 / 103–132 | 4% | TOR: Scottie Barnes (out); Immanuel Quickley (day-to-day); Kawhi Leonard (out); Collin Murray-Boyles (day-to-day) (-3.2)<br>PHI: Adem Bona (out); Dominick Barlow (out) (+0.6) | no line yet | no line yet | no line yet |
| 7:00 PM | DET @ WAS | DET 118, WAS 106 | DET 80% | DET -390 / WAS +390 | DET -11.3 | 223.8 | 104–131 / 92–121 | 4% | DET: Jalen Duren (out) (-0.1)<br>WAS: Jamir Watkins (out); Justin Champagnie (out); Tristan Vukcevic (out) (+0.0) | no line yet | no line yet | no line yet |
| 8:00 PM | DAL @ MIN | DAL 111, MIN 116 | MIN 64% | DAL +180 / MIN -180 | MIN -5.1 | 226.1 | 96–125 / 101–130 | 4% | DAL: Morez Johnson Jr. (day-to-day); Dereck Lively II (out); Sergio de Larrea (out) (+1.3)<br>MIN: Anthony Edwards (out); Donte DiVincenzo (out) (-0.7) | no line yet | no line yet | no line yet |
| 9:00 PM | CHA @ PHX | CHA 105, PHX 113 | PHX 73% | CHA +275 / PHX -275 | PHX -8 | 218.2 | 91–120 / 99–127 | 5% | CHA: Moussa Diabate (day-to-day); Dennis Schroder (out); Brandon Miller (day-to-day); Kon Knueppel (out); Grant Williams (out) (-1.2)<br>PHX: Mark Williams (out) (+0.4) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 154 | 11.10 | 14.30 | 9.37 | 0.559 | 0.189 | 71.4% | 81.2% |
| Model only (before blending) | 154 | 11.47 | 14.15 | 9.45 | 0.582 | 0.200 | 69.5% | – |
| Elo | 154 | 11.87 | – | – | 0.601 | 0.209 | 64.9% | – |
| Final prediction, games with a line | 154 | 11.10 | 14.30 | 9.37 | 0.559 | 0.189 | 71.4% | 81.2% |
| Model only, games with a line | 154 | 11.47 | 14.15 | 9.45 | 0.582 | 0.200 | 69.5% | – |
| Betting line | 154 | 11.05 | 14.30 | 9.35 | 0.549 | 0.185 | 71.4% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.7% of games, happened in 5.2%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 9 | 0-9-0 | 3.5 | -3.47 | -100.0% | +8.3% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 5 of 6 games (83%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Monday, November 9

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| LAL @ ATL | 116–118 | 124–114 | 43% | ATL -2.2 / ATL -2.5 | yes |
| CLE @ CHA | 112–103 | 112–124 | 25% | CLE -9.1 / CLE -9.5 | no |
| WAS @ DET | 104–114 | 111–122 | 77% | DET -9.7 / DET -9.5 | yes |
| MEM @ TOR | 114–113 | 118–102 | 54% | MEM -1.2 / MEM -1.5 | yes |
| IND @ DAL | 111–116 | 122–125 | 63% | DAL -4.6 / DAL -4.5 | yes |
| DEN @ HOU | 110–114 | 100–110 | 63% | HOU -4.6 / HOU -4.5 | yes |
| SAS @ PHX | 117–108 | 122–96 | 73% | SAS -8.5 / SAS -9.5 | yes |
| NOP @ GSW | 109–120 | 87–138 | 81% | GSW -11.9 / GSW -11.5 | no |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | SAS | +7.4 | +7.5 | +3.1 | +4.3 | 101.1 | +0.6 | 1723 |
| 2 | HOU | +7.3 | +7.2 | +3.1 | +4.2 | 98.4 | -0.6 | 1620 |
| 3 | BOS | +6.9 | +6.6 | +3.7 | +3.2 | 95.2 | +0.0 | 1646 |
| 4 | DET | +6.1 | +6.2 | +2.3 | +3.7 | 101.6 | -0.1 | 1645 |
| 5 | MIN | +5.6 | +5.8 | +2.4 | +3.2 | 102.7 | -0.7 | 1622 |
| 6 | LAL | +5.2 | +5.3 | +4.8 | +0.5 | 102.0 | +0.2 | 1620 |
| 7 | NYK | +3.9 | +3.8 | +1.2 | +2.8 | 95.6 | -0.2 | 1701 |
| 8 | OKC | +3.9 | +4.0 | -0.3 | +4.2 | 102.2 | -0.2 | 1685 |
| 9 | DEN | +3.6 | +3.5 | +4.1 | -0.5 | 97.4 | +0.2 | 1575 |
| 10 | GSW | +3.4 | +3.5 | +2.1 | +1.3 | 101.2 | +0.2 | 1539 |
| 11 | PHI | +2.4 | +2.4 | -0.1 | +2.5 | 100.9 | +0.5 | 1577 |
| 12 | POR | +2.0 | +2.1 | +1.8 | +0.3 | 103.0 | -0.4 | 1544 |
| 13 | DAL | +0.5 | +0.5 | +0.4 | +0.1 | 101.6 | +1.3 | 1450 |
| 14 | CLE | +0.2 | +0.2 | +1.3 | -1.0 | 101.7 | -0.5 | 1565 |
| 15 | TOR | +0.2 | +0.2 | -0.1 | +0.3 | 102.9 | -3.2 | 1525 |
| 16 | MIA | -0.3 | -0.4 | +0.7 | -1.1 | 104.8 | +0.0 | 1491 |
| 17 | PHX | -0.8 | -0.8 | +0.6 | -1.3 | 100.2 | +0.4 | 1488 |
| 18 | ORL | -1.6 | -1.7 | -2.6 | +1.0 | 100.6 | +1.3 | 1489 |
| 19 | MEM | -1.7 | -1.7 | +0.0 | -1.7 | 101.6 | +0.9 | 1428 |
| 20 | IND | -2.0 | -2.1 | -0.6 | -1.4 | 103.3 | -0.2 | 1355 |
| 21 | ATL | -2.2 | -2.4 | -0.9 | -1.3 | 108.2 | +2.0 | 1539 |
| 22 | LAC | -2.6 | -2.6 | -0.8 | -1.7 | 100.3 | +0.7 | 1485 |
| 23 | UTA | -3.8 | -3.8 | -3.8 | +0.0 | 102.0 | -2.3 | 1297 |
| 24 | NOP | -4.5 | -4.7 | -1.4 | -3.1 | 103.4 | +0.3 | 1412 |
| 25 | WAS | -5.3 | -5.4 | -3.2 | -2.1 | 101.8 | +0.0 | 1330 |
| 26 | CHA | -5.5 | -5.3 | -4.4 | -1.1 | 96.5 | -1.2 | 1481 |
| 27 | BKN | -6.3 | -6.5 | -3.7 | -2.6 | 102.1 | +0.5 | 1306 |
| 28 | CHI | -7.1 | -7.8 | -3.2 | -3.9 | 110.6 | -0.2 | 1351 |
| 29 | SAC | -7.4 | -7.6 | -3.3 | -4.1 | 102.4 | +0.3 | 1334 |
| 30 | MIL | -7.6 | -7.8 | -3.1 | -4.6 | 102.2 | -1.0 | 1330 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +7.9 | +2.3 | +5.5 | 27 |
| 2 | Shai Gilgeous-Alexander | OKC | +6.0 | +5.1 | +0.9 | 31 |
| 3 | Nikola Jokic | DEN | +5.2 | +4.9 | +0.3 | 36 |
| 4 | Luka Doncic | LAL | +4.6 | +5.3 | -0.7 | 37 |
| 5 | Kawhi Leonard | TOR | +4.5 | +3.6 | +0.9 | 30 |
| 6 | Kyrie Irving | DAL | +4.1 | +3.9 | +0.2 | 33 |
| 7 | Giannis Antetokounmpo | MIA | +3.9 | +3.7 | +0.2 | 34 |
| 8 | Joel Embiid | PHI | +2.9 | +1.4 | +1.5 | 29 |
| 9 | Stephen Curry | GSW | +2.8 | +4.7 | -1.9 | 28 |
| 10 | Donovan Mitchell | CLE | +2.6 | +3.1 | -0.5 | 30 |
| 11 | Herbert Jones | NOP | +2.4 | -0.5 | +2.8 | 23 |
| 12 | Fred VanVleet | HOU | +2.3 | +1.4 | +0.9 | 30 |
| 13 | LaMelo Ball | MIN | +2.3 | +4.2 | -1.9 | 31 |
| 14 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 15 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.1 | 30 |
| 16 | Dyson Daniels | ATL | +2.1 | +0.6 | +1.5 | 32 |
| 17 | Ty Jerome | MEM | +2.0 | +3.1 | -1.1 | 30 |
| 18 | Franz Wagner | ORL | +2.0 | +0.9 | +1.1 | 39 |
| 19 | Rudy Gobert | MIN | +1.8 | -3.2 | +5.0 | 29 |
| 20 | Ausar Thompson | DET | +1.8 | -0.3 | +2.2 | 28 |
| 21 | Derrick White | BOS | +1.7 | +0.3 | +1.4 | 29 |
| 22 | De'Aaron Fox | SAS | +1.7 | +1.6 | +0.1 | 27 |
| 23 | Neemias Queta | BOS | +1.7 | +0.8 | +0.8 | 22 |
| 24 | Pascal Siakam | IND | +1.7 | +1.6 | +0.1 | 33 |
| 25 | Dean Wade | PHI | +1.6 | +0.4 | +1.2 | 21 |
| 26 | Bam Adebayo | MIA | +1.4 | +1.0 | +0.4 | 34 |
| 27 | Cade Cunningham | DET | +1.3 | +1.5 | -0.1 | 32 |
| 28 | Lauri Markkanen | UTA | +1.3 | +1.1 | +0.2 | 33 |
| 29 | Anthony Davis | WAS | +1.3 | -0.1 | +1.3 | 33 |
| 30 | Jaden McDaniels | MIN | +1.3 | +0.4 | +0.9 | 35 |

## Current model fit

- Fitted on 5436 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.8 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.16 (offense) and 0.16 (defense); player lineup ratings 0.76 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.2% of recent games went to overtime.
