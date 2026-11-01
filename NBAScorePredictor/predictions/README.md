# NBA score predictions

Updated Sun Nov 01, 2026 04:23 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Sunday, November 1

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5:00 PM | BKN @ IND | BKN 114, IND 117 | IND 60% | BKN +150 / IND -150<br>posted BKN +136 / IND -162 | IND -3.5 / IND -3.5 (fav covers 51%) | 230.7 / 230.5 (over 50%) | 99–128 / 103–131 | 5% | BKN: Mikel Brown Jr. (out); Egor Demin (out) (+1.7)<br>IND: Tyrese Haliburton (out); Obi Toppin (out); Johnny Furphy (out); Ben Sheppard (out); T.J. McConnell (out); Ivica Zubac (out) (-1.1) | no edge | no edge | no edge |
| 8:30 PM | LAC @ GSW | LAC 109, GSW 112 | GSW 58% | LAC +135 / GSW -135<br>posted LAC +110 / GSW -130 | GSW -2.5 / GSW -2.5 (fav covers 52%) | 220.7 / 220.5 (over 49%) | 95–124 / 98–126 | 5% | LAC: Max Strus (out); Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+0.7)<br>GSW: Draymond Green (out); Moses Moody (out); Stephen Curry (out); Jimmy Butler III (out); Kristaps Porzingis (out); Gui Santos (day-to-day) (-3.5) | no edge | no edge | no edge |
| 9:00 PM | TOR @ LAL | TOR 111, LAL 114 | LAL 57% | TOR +135 / LAL -135<br>posted TOR +124 / LAL -148 | LAL -2.8 / LAL -2.5 (fav covers 52%) | 224.7 / 224.5 (over 50%) | 97–126 / 100–128 | 5% | TOR: Kawhi Leonard (out) (-1.8)<br>LAL: Ziaire Williams (out) (+0.8) | no edge | no edge | no edge |

## Monday, November 2

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | OKC @ CLE | OKC 111, CLE 115 | CLE 62% | OKC +160 / CLE -160 | CLE -3.9 | 225.3 | 96–125 / 100–129 | 5% | OKC: Chet Holmgren (out); Jalen Williams (out); Alex Caruso (out); Cason Wallace (out) (-2.5)<br>CLE: Jaylon Tyson (day-to-day) (+0.1) | no line yet | no line yet | no line yet |
| 7:30 PM | DET @ CHA | DET 107, CHA 99 | DET 72% | DET -265 / CHA +265 | DET -7.4 | 205.6 | 93–120 / 85–113 | 5% | DET: Jalen Duren (out) (-0.2)<br>CHA: Kon Knueppel (out); Coby White (out); Grant Williams (out) (-0.8) | no line yet | no line yet | no line yet |
| 7:30 PM | ATL @ IND | ATL 119, IND 116 | ATL 60% | ATL -150 / IND +150 | ATL -3.4 | 235.4 | 105–134 / 101–131 | 5% | ATL: Jalen Johnson (day-to-day) (+0.7)<br>IND: Tyrese Haliburton (out); Obi Toppin (out); Johnny Furphy (out); Ben Sheppard (out); T.J. McConnell (out); Ivica Zubac (out) (-1.1) | no line yet | no line yet | no line yet |
| 7:30 PM | BKN @ NYK | BKN 106, NYK 119 | NYK 84% | BKN +520 / NYK -520 | NYK -13.2 | 225.5 | 92–121 / 105–133 | 3% | BKN: Mikel Brown Jr. (out); Egor Demin (out) (+1.7)<br>NYK: Jose Alvarado (out) (-0.3) | no line yet | no line yet | no line yet |
| 7:30 PM | WAS @ ORL | WAS 110, ORL 116 | ORL 67% | WAS +205 / ORL -205 | ORL -5.9 | 226.5 | 96–125 / 102–130 | 5% | WAS: Jamir Watkins (out); Justin Champagnie (out); Tristan Vukcevic (out) (+0.0)<br>ORL: Paolo Banchero (out); Jalen Suggs (out) (+0.7) | no line yet | no line yet | no line yet |
| 7:30 PM | CHI @ PHI | CHI 113, PHI 124 | PHI 77% | CHI +345 / PHI -345 | PHI -10.4 | 236.8 | 98–128 / 109–138 | 4% | CHI: Nic Claxton (out) (+0.2)<br>PHI: Joel Embiid (day-to-day); LeBron James (day-to-day); Dominick Barlow (out) (-0.4) | no line yet | no line yet | no line yet |
| 8:00 PM | SAC @ DAL | SAC 111, DAL 123 | DAL 80% | SAC +390 / DAL -390 | DAL -11.2 | 233.8 | 96–127 / 108–137 | 4% | SAC: Maxime Raynaud (out); Keegan Murray (out); Dylan Cardwell (out) (+0.0)<br>DAL: Santi Aldama (out); Dereck Lively II (out); Sergio de Larrea (out) (+1.1) | no line yet | no line yet | no line yet |
| 8:00 PM | NOP @ MEM | NOP 115, MEM 120 | MEM 63% | NOP +170 / MEM -170 | MEM -4.3 | 235.1 | 100–131 / 105–134 | 6% | NOP: Trey Murphy III (day-to-day); Yves Missi (out); Jordan Poole (out) (+0.3)<br>MEM: Ty Jerome (day-to-day); Scotty Pippen Jr. (day-to-day); Quinten Post (day-to-day) (-0.4) | no line yet | no line yet | no line yet |
| 8:00 PM | MIL @ MIN | MIL 110, MIN 123 | MIN 82% | MIL +440 / MIN -440 | MIN -12.4 | 233.3 | 96–126 / 108–137 | 3% | MIN: Anthony Edwards (out); Rudy Gobert (day-to-day); Donte DiVincenzo (out) (-1.6) | no line yet | no line yet | no line yet |
| 8:30 PM | BOS @ HOU | BOS 109, HOU 114 | HOU 63% | BOS +170 / HOU -170 | HOU -4.3 | 222.8 | 95–124 / 99–128 | 5% | BOS: Jayson Tatum (day-to-day); Devin Carter (out); Mitchell Robinson (out) (+0.9)<br>HOU: Reed Sheppard (day-to-day); Steven Adams (out); Clint Capela (day-to-day) (+0.0) | no line yet | no line yet | no line yet |
| 8:30 PM | UTA @ SAS | UTA 104, SAS 120 | SAS 88% | UTA +740 / SAS -740 | SAS -15.8 | 223.6 | 89–118 / 106–134 | 2% | UTA: Jaren Jackson Jr. (out); Trey Alexander (out); Jusuf Nurkic (out) (-0.9)<br>SAS: Tobias Harris (out) (+0.8) | no line yet | no line yet | no line yet |
| 9:00 PM | POR @ DEN | POR 113, DEN 116 | DEN 60% | POR +150 / DEN -150 | DEN -3.4 | 229.0 | 98–127 / 102–130 | 5% | POR: Ja Morant (out) (-0.5)<br>DEN: Spencer Jones (out); Alpha Diallo (out) (+2.2) | no line yet | no line yet | no line yet |
| 10:00 PM | PHX @ GSW | PHX 116, GSW 115 | PHX 54% | PHX -120 / GSW +120 | PHX -1.3 | 231.1 | 102–131 / 100–130 | 5% | PHX: Mark Williams (out) (+0.4)<br>GSW: Draymond Green (out); Moses Moody (out); Stephen Curry (out); Jimmy Butler III (out); Kristaps Porzingis (out); Gui Santos (day-to-day) (-3.5) | no line yet | no line yet | no line yet |
| 10:00 PM | TOR @ LAC | TOR 112, LAC 111 | TOR 52% | TOR -110 / LAC +110 | TOR -0.7 | 222.9 | 98–126 / 97–126 | 5% | TOR: Kawhi Leonard (out) (-1.8)<br>LAC: Max Strus (out); Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+0.7) | no line yet | no line yet | no line yet |
| 10:00 PM | MIA @ LAL | MIA 117, LAL 119 | LAL 55% | MIA +125 / LAL -125 | LAL -2 | 236.9 | 103–132 / 105–134 | 5% | LAL: Ziaire Williams (out) (+0.8) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 88 | 11.52 | 14.97 | 9.71 | 0.579 | 0.199 | 68.2% | 80.1% |
| Model only (before blending) | 88 | 12.10 | 14.60 | 9.87 | 0.609 | 0.212 | 64.8% | – |
| Elo | 88 | 12.52 | – | – | 0.647 | 0.229 | 58.0% | – |
| Final prediction, games with a line | 88 | 11.52 | 14.97 | 9.71 | 0.579 | 0.199 | 68.2% | 80.1% |
| Model only, games with a line | 88 | 12.10 | 14.60 | 9.87 | 0.609 | 0.212 | 64.8% | – |
| Betting line | 88 | 11.43 | 14.93 | 9.66 | 0.565 | 0.193 | 68.2% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.7% of games, happened in 4.5%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 5 | 0-5-0 | 1.9 | -1.88 | -100.0% | +8.8% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 4 of 5 games (80%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Saturday, October 31

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| POR @ UTA | 119–112 | 112–90 | 70% | POR -7 / POR -7.5 | no |
| PHI @ CHA | 106–105 | 109–104 | 54% | PHI -1.3 / PHI -1.5 | yes |
| ATL @ NOP | 123–119 | 99–121 | 38% | ATL -4.3 / ATL -4.5 | no |
| SAC @ MEM | 111–119 | 105–136 | 73% | MEM -8.3 / MEM -8.5 | no |
| CLE @ MIL | 122–113 | 136–111 | 74% | CLE -8.9 / CLE -9.5 | yes |
| MIN @ SAS | 108–120 | 111–121 | 82% | SAS -11.9 / SAS -12.5 | yes |
| OKC @ HOU | 108–111 | 98–119 | 60% | HOU -3.1 / HOU -2.5 | yes |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | HOU | +7.0 | +7.0 | +3.7 | +3.4 | 100.1 | +0.0 | 1623 |
| 2 | SAS | +6.9 | +7.0 | +2.2 | +4.6 | 102.2 | +0.8 | 1692 |
| 3 | DET | +5.9 | +5.9 | +1.5 | +4.4 | 99.9 | -0.2 | 1647 |
| 4 | BOS | +5.7 | +5.7 | +3.1 | +2.5 | 99.7 | +0.9 | 1618 |
| 5 | NYK | +4.0 | +4.0 | +1.3 | +2.8 | 98.7 | -0.3 | 1686 |
| 6 | MIN | +3.7 | +3.8 | +1.5 | +2.1 | 104.3 | -1.6 | 1598 |
| 7 | POR | +2.9 | +3.0 | +1.8 | +1.1 | 102.5 | -0.6 | 1537 |
| 8 | OKC | +2.7 | +2.7 | -0.7 | +3.5 | 100.5 | -2.5 | 1660 |
| 9 | PHI | +2.4 | +2.4 | -0.2 | +2.6 | 101.9 | -0.4 | 1570 |
| 10 | TOR | +2.1 | +2.2 | +0.5 | +1.6 | 102.8 | -1.8 | 1552 |
| 11 | CLE | +2.0 | +2.1 | +2.3 | -0.2 | 102.1 | +0.1 | 1585 |
| 12 | LAL | +1.9 | +2.0 | +2.2 | -0.3 | 100.6 | +0.8 | 1573 |
| 13 | GSW | +1.8 | +1.8 | +1.2 | +0.6 | 102.5 | -3.6 | 1492 |
| 14 | DEN | +1.6 | +1.6 | +2.9 | -1.3 | 98.9 | +2.2 | 1579 |
| 15 | MIA | +0.9 | +1.0 | +1.9 | -1.0 | 106.8 | +0.0 | 1501 |
| 16 | ORL | +0.7 | +0.7 | -1.0 | +1.6 | 102.7 | +0.7 | 1536 |
| 17 | DAL | -0.3 | -0.3 | -0.2 | -0.1 | 102.9 | +1.1 | 1456 |
| 18 | PHX | -0.6 | -0.7 | +1.5 | -2.1 | 101.5 | +0.4 | 1498 |
| 19 | MEM | -0.7 | -0.7 | +0.5 | -1.2 | 103.1 | -0.4 | 1426 |
| 20 | ATL | -0.9 | -1.0 | -0.5 | -0.5 | 107.1 | +0.8 | 1533 |
| 21 | IND | -2.3 | -2.4 | +0.1 | -2.5 | 103.3 | -1.1 | 1371 |
| 22 | CHA | -3.1 | -2.9 | -3.4 | +0.3 | 94.9 | -0.8 | 1523 |
| 23 | LAC | -3.2 | -3.2 | -1.8 | -1.4 | 101.1 | +0.7 | 1498 |
| 24 | NOP | -3.5 | -3.8 | -1.8 | -1.8 | 107.4 | +0.3 | 1434 |
| 25 | WAS | -4.4 | -4.6 | -2.5 | -2.0 | 102.8 | +0.0 | 1325 |
| 26 | UTA | -4.9 | -5.0 | -3.4 | -1.5 | 102.6 | -0.9 | 1309 |
| 27 | CHI | -6.0 | -6.8 | -3.0 | -3.0 | 113.3 | +0.2 | 1363 |
| 28 | BKN | -6.7 | -7.1 | -3.6 | -3.2 | 106.2 | +1.8 | 1290 |
| 29 | MIL | -7.4 | -7.9 | -2.8 | -4.6 | 106.4 | +0.0 | 1347 |
| 30 | SAC | -8.0 | -8.5 | -3.5 | -4.5 | 106.5 | +0.0 | 1325 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +6.4 | +1.7 | +4.7 | 34 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.8 | +5.0 | +0.8 | 31 |
| 3 | Nikola Jokic | DEN | +5.1 | +5.4 | -0.3 | 37 |
| 4 | Kawhi Leonard | TOR | +4.5 | +3.6 | +0.9 | 30 |
| 5 | Giannis Antetokounmpo | MIA | +3.8 | +3.9 | -0.1 | 31 |
| 6 | Luka Doncic | LAL | +3.7 | +4.9 | -1.2 | 36 |
| 7 | Kyrie Irving | DAL | +3.5 | +3.4 | +0.1 | 31 |
| 8 | Joel Embiid | PHI | +3.1 | +1.5 | +1.6 | 35 |
| 9 | Herbert Jones | NOP | +2.6 | -0.3 | +2.9 | 23 |
| 10 | Franz Wagner | ORL | +2.5 | +1.2 | +1.3 | 35 |
| 11 | Fred VanVleet | HOU | +2.5 | +1.8 | +0.7 | 32 |
| 12 | Marcus Smart | HOU | +2.5 | +1.3 | +1.2 | 24 |
| 13 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 14 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.0 | 30 |
| 15 | Lauri Markkanen | UTA | +2.0 | +1.7 | +0.2 | 26 |
| 16 | Jarrett Allen | CLE | +2.0 | +1.2 | +0.7 | 27 |
| 17 | Ausar Thompson | DET | +1.9 | -0.3 | +2.2 | 27 |
| 18 | Ty Jerome | MEM | +1.9 | +3.3 | -1.4 | 28 |
| 19 | Bam Adebayo | MIA | +1.8 | +1.4 | +0.4 | 32 |
| 20 | Rudy Gobert | MIN | +1.8 | -3.3 | +5.1 | 28 |
| 21 | Cade Cunningham | DET | +1.7 | +1.6 | +0.1 | 33 |
| 22 | Dyson Daniels | ATL | +1.7 | +0.7 | +1.0 | 28 |
| 23 | LaMelo Ball | MIN | +1.7 | +3.8 | -2.2 | 25 |
| 24 | Kevin Durant | HOU | +1.5 | +3.2 | -1.7 | 32 |
| 25 | Donovan Mitchell | CLE | +1.5 | +2.3 | -0.8 | 30 |
| 26 | Stephen Curry | GSW | +1.4 | +4.2 | -2.7 | 30 |
| 27 | Derrick White | BOS | +1.4 | -0.1 | +1.6 | 29 |
| 28 | Pascal Siakam | IND | +1.4 | +1.7 | -0.4 | 31 |
| 29 | Dean Wade | PHI | +1.3 | -0.2 | +1.5 | 26 |
| 30 | Jrue Holiday | POR | +1.2 | +0.3 | +1.0 | 26 |

## Current model fit

- Fitted on 5370 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.15 (offense) and 0.15 (defense); player lineup ratings 0.76 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.1% of recent games went to overtime.
