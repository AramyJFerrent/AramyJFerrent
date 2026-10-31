# NBA score predictions

Updated Sat Oct 31, 2026 02:36 AM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Saturday, October 31

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3:00 PM | POR @ UTA | POR 119, UTA 113 | POR 68% | POR -210 / UTA +210<br>posted POR -225 / UTA +185 | POR -6.2 / POR -6.5 (fav covers 50%) | 231.6 / 231.5 (over 49%) | 104–133 / 98–127 | 5% | POR: Ja Morant (out); Robert Williams III (day-to-day) (-0.7)<br>UTA: Lauri Markkanen (day-to-day); Jaren Jackson Jr. (out); Trey Alexander (out); Jusuf Nurkic (out) (-1.2) | no edge | no edge | no edge |
| 6:00 PM | PHI @ CHA | PHI 109, CHA 107 | PHI 56% | PHI -130 / CHA +130<br>posted PHI -120 / CHA +100 | PHI -1.9 / PHI -1.5 (fav covers 54%) | 216.8 / 216.5 (over 49%) | 95–124 / 94–122 | 5% | PHI: Jaylen Brown (day-to-day); Dominick Barlow (out) (+0.5)<br>CHA: Kon Knueppel (out); Coby White (out); Grant Williams (out) (-0.7) | no edge | no edge | no edge |
| 7:00 PM | ATL @ NOP | ATL 122, NOP 118 | ATL 62% | ATL -165 / NOP +165<br>posted ATL -170 / NOP +142 | ATL -4.1 / ATL -4.5 (fav covers 50%) | 239.6 / 239.5 (over 49%) | 107–137 / 103–133 | 5% | NOP: Yves Missi (out); Jordan Poole (out) (+0.3) | no edge | no edge | no edge |
| 8:00 PM | SAC @ MEM | SAC 112, MEM 122 | MEM 77% | SAC +335 / MEM -335<br>posted SAC +350 / MEM -455 | MEM -10 / MEM -10.5 (fav covers 47%) | 233.5 / 233.5 (over 49%) | 97–127 / 107–136 | 4% | SAC: Maxime Raynaud (out); Keegan Murray (out); Dylan Cardwell (out) (+0.2)<br>MEM: Ty Jerome (day-to-day); Scotty Pippen Jr. (day-to-day); Quinten Post (day-to-day) (-0.4) | no edge | no edge | no edge |
| 8:00 PM | CLE @ MIL | CLE 123, MIL 114 | CLE 75% | CLE -300 / MIL +300<br>posted CLE -360 / MIL +285 | CLE -9.1 / CLE -9.5 (fav covers 48%) | 237.4 / 237.5 (over 49%) | 109–138 / 99–129 | 4% | CLE: Jaylon Tyson (out); Meleek Thomas (day-to-day) (+0.4) | no edge | no edge | no edge |
| 8:00 PM | MIN @ SAS | MIN 107, SAS 119 | SAS 81% | MIN +440 / SAS -440<br>posted MIN +425 / SAS -575 | SAS -12.1 / SAS -12.5 (fav covers 47%) | 226.1 / 226.5 (over 48%) | 92–122 / 105–133 | 4% | MIN: Anthony Edwards (out); Donte DiVincenzo (out) (-1.4)<br>SAS: Tobias Harris (out) (+0.7) | no edge | no edge | no edge |
| 8:30 PM | OKC @ HOU | OKC 107, HOU 112 | HOU 64% | OKC +175 / HOU -175<br>posted OKC +142 / HOU -170 | HOU -4.6 / HOU -4.5 (fav covers 52%) | 218.6 / 218.5 (over 50%) | 93–121 / 98–126 | 5% | OKC: Chet Holmgren (out); Jalen Williams (out); Alex Caruso (out); Cason Wallace (out) (-2.4)<br>HOU: Alperen Sengun (day-to-day); Reed Sheppard (day-to-day); Steven Adams (out) (+0.0) | no edge | no edge | no edge |

## Sunday, November 1

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3:30 PM | BOS @ ORL | BOS 114, ORL 110 | BOS 64% | BOS -175 / ORL +175 | BOS -4.6 | 223.6 | 100–128 / 95–124 | 5% | BOS: Devin Carter (out) (+1.1)<br>ORL: Paolo Banchero (out); Jalen Suggs (out) (+0.2) | no line yet | no line yet | no line yet |
| 5:00 PM | BKN @ IND | BKN 113, IND 119 | IND 65% | BKN +185 / IND -185 | IND -5.2 | 232.0 | 99–128 / 104–133 | 5% | BKN: Egor Demin (out) (+0.8)<br>IND: Tyrese Haliburton (out); Obi Toppin (day-to-day); Johnny Furphy (out); Ivica Zubac (out); Ben Sheppard (out); T.J. McConnell (out) (-0.5) | no line yet | no line yet | no line yet |
| 8:30 PM | LAC @ GSW | LAC 112, GSW 115 | GSW 59% | LAC +145 / GSW -145 | GSW -3.4 | 226.7 | 97–126 / 101–129 | 5% | LAC: Max Strus (out); Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+1.0)<br>GSW: Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out) (-1.3) | no line yet | no line yet | no line yet |
| 9:00 PM | TOR @ LAL | TOR 112, LAL 117 | LAL 64% | TOR +175 / LAL -175 | LAL -4.9 | 228.9 | 97–127 / 102–131 | 6% | TOR: Kawhi Leonard (out) (-1.8)<br>LAL: Ziaire Williams (day-to-day) (+0.4) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 71 | 11.23 | 14.69 | 9.64 | 0.580 | 0.199 | 69.0% | 80.3% |
| Model only (before blending) | 71 | 11.99 | 14.25 | 9.83 | 0.622 | 0.218 | 63.4% | – |
| Elo | 71 | 12.17 | – | – | 0.650 | 0.230 | 60.6% | – |
| Final prediction, games with a line | 71 | 11.23 | 14.69 | 9.64 | 0.580 | 0.199 | 69.0% | 80.3% |
| Model only, games with a line | 71 | 11.99 | 14.25 | 9.83 | 0.622 | 0.218 | 63.4% | – |
| Betting line | 71 | 11.12 | 14.68 | 9.60 | 0.565 | 0.193 | 69.0% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.8% of games, happened in 5.6%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 5 | 0-5-0 | 1.9 | -1.88 | -100.0% | +8.8% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 4 of 5 games (80%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Thursday, October 29

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| CLE @ ATL | 118–120 | 111–114 | 54% | ATL -1.4 / ATL -1.5 | yes |
| SAC @ NOP | 115–121 | 120–132 | 66% | NOP -5.7 / NOP -6.5 | yes |
| MEM @ POR | 112–120 | 124–103 | 28% | POR -7.7 / POR -7.5 | no |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | HOU | +7.1 | +7.2 | +3.5 | +3.5 | 101.9 | +0.0 | 1616 |
| 2 | SAS | +6.7 | +6.8 | +2.0 | +4.6 | 102.3 | +0.7 | 1687 |
| 3 | BOS | +5.6 | +5.6 | +3.1 | +2.6 | 99.8 | +1.1 | 1615 |
| 4 | DET | +5.4 | +5.3 | +1.7 | +3.7 | 98.5 | -0.2 | 1643 |
| 5 | NYK | +4.0 | +4.0 | +1.4 | +2.6 | 101.1 | -0.3 | 1695 |
| 6 | OKC | +3.3 | +3.4 | -0.5 | +3.8 | 102.0 | -2.4 | 1677 |
| 7 | MIN | +3.0 | +3.1 | +1.0 | +2.0 | 104.3 | -1.4 | 1593 |
| 8 | POR | +2.8 | +2.8 | +2.5 | +0.3 | 102.4 | -0.7 | 1527 |
| 9 | LAL | +2.5 | +2.5 | +2.9 | -0.3 | 101.4 | +0.4 | 1590 |
| 10 | PHI | +2.1 | +2.2 | -0.6 | +2.7 | 107.2 | +0.5 | 1553 |
| 11 | TOR | +1.9 | +2.0 | -0.3 | +2.2 | 106.2 | -1.9 | 1565 |
| 12 | CLE | +1.7 | +1.8 | +2.1 | -0.3 | 101.5 | +0.4 | 1574 |
| 13 | GSW | +1.1 | +1.2 | +1.3 | -0.1 | 103.5 | -1.3 | 1474 |
| 14 | ATL | +0.5 | +0.6 | +0.6 | -0.1 | 106.8 | +0.8 | 1556 |
| 15 | DEN | +0.5 | +0.5 | +1.9 | -1.3 | 98.6 | +1.9 | 1570 |
| 16 | MIA | +0.4 | +0.4 | +0.9 | -0.5 | 107.7 | +0.0 | 1494 |
| 17 | ORL | +0.0 | +0.0 | -2.0 | +2.1 | 105.7 | +0.2 | 1524 |
| 18 | PHX | -0.8 | -0.8 | +1.0 | -1.8 | 101.5 | +0.4 | 1507 |
| 19 | MEM | -1.2 | -1.2 | +0.4 | -1.6 | 102.5 | -0.4 | 1414 |
| 20 | DAL | -1.3 | -1.3 | -0.7 | -0.5 | 102.7 | +0.8 | 1447 |
| 21 | IND | -1.5 | -1.6 | -0.1 | -1.5 | 103.5 | -0.5 | 1379 |
| 22 | CHA | -2.2 | -2.2 | -2.6 | +0.3 | 97.5 | -0.6 | 1556 |
| 23 | LAC | -2.5 | -2.5 | -1.7 | -0.7 | 101.6 | +1.0 | 1509 |
| 24 | UTA | -3.6 | -3.7 | -2.1 | -1.5 | 102.4 | -1.3 | 1319 |
| 25 | NOP | -4.5 | -4.8 | -2.1 | -2.3 | 108.4 | +0.3 | 1412 |
| 26 | WAS | -5.1 | -5.2 | -1.9 | -3.1 | 102.8 | -0.1 | 1300 |
| 27 | BKN | -5.9 | -6.3 | -2.8 | -3.1 | 106.1 | +0.9 | 1293 |
| 28 | CHI | -6.2 | -7.1 | -3.3 | -3.0 | 113.1 | +0.1 | 1366 |
| 29 | MIL | -6.3 | -6.7 | -2.3 | -4.0 | 105.5 | +0.0 | 1357 |
| 30 | SAC | -7.4 | -7.9 | -3.1 | -4.4 | 105.9 | +0.2 | 1337 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +6.3 | +1.6 | +4.7 | 34 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.8 | +5.1 | +0.8 | 32 |
| 3 | Nikola Jokic | DEN | +5.0 | +5.3 | -0.3 | 37 |
| 4 | Kawhi Leonard | TOR | +4.5 | +3.6 | +0.8 | 30 |
| 5 | Luka Doncic | LAL | +3.5 | +4.9 | -1.4 | 36 |
| 6 | Giannis Antetokounmpo | MIA | +3.3 | +3.5 | -0.1 | 32 |
| 7 | Joel Embiid | PHI | +3.2 | +1.6 | +1.5 | 36 |
| 8 | Kyrie Irving | DAL | +3.1 | +3.1 | +0.1 | 28 |
| 9 | Fred VanVleet | HOU | +2.8 | +1.8 | +0.9 | 31 |
| 10 | Herbert Jones | NOP | +2.3 | +0.0 | +2.3 | 22 |
| 11 | Lauri Markkanen | UTA | +2.3 | +2.1 | +0.2 | 24 |
| 12 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 13 | Franz Wagner | ORL | +2.1 | +0.6 | +1.5 | 33 |
| 14 | Chet Holmgren | OKC | +2.1 | +0.1 | +2.0 | 30 |
| 15 | Ausar Thompson | DET | +2.0 | -0.2 | +2.2 | 27 |
| 16 | Dyson Daniels | ATL | +1.9 | +0.9 | +1.0 | 29 |
| 17 | Ty Jerome | MEM | +1.9 | +3.3 | -1.4 | 28 |
| 18 | Bam Adebayo | MIA | +1.9 | +1.0 | +0.9 | 31 |
| 19 | Pascal Siakam | IND | +1.8 | +1.7 | +0.1 | 33 |
| 20 | Kevin Durant | HOU | +1.6 | +3.1 | -1.5 | 33 |
| 21 | Cade Cunningham | DET | +1.6 | +1.6 | +0.0 | 37 |
| 22 | Jarrett Allen | CLE | +1.6 | +1.2 | +0.4 | 29 |
| 23 | LaMelo Ball | MIN | +1.6 | +3.9 | -2.3 | 27 |
| 24 | Rudy Gobert | MIN | +1.5 | -3.4 | +4.9 | 28 |
| 25 | Nickeil Alexander-Walker | ATL | +1.4 | +1.7 | -0.3 | 31 |
| 26 | Dean Wade | PHI | +1.3 | -0.1 | +1.4 | 22 |
| 27 | Paul Reed | DET | +1.2 | +0.0 | +1.3 | 28 |
| 28 | Jrue Holiday | POR | +1.2 | +0.3 | +1.0 | 28 |
| 29 | Derrick White | BOS | +1.2 | -0.2 | +1.4 | 31 |
| 30 | Devin Vassell | SAS | +1.0 | +0.8 | +0.3 | 33 |

## Current model fit

- Fitted on 5353 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.16 (offense) and 0.15 (defense); player lineup ratings 0.76 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.2% of recent games went to overtime.
