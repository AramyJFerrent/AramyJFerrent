# NBA score predictions

Updated Fri Nov 20, 2026 03:02 AM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Friday, November 20

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | CHA @ ATL | CHA 107, ATL 113 | ATL 69% | CHA +225 / ATL -225<br>posted CHA +191 / ATL -230 | ATL -6.6 / ATL -6.5 (fav covers 52%) | 219.7 / 219.5 (over 50%) | 92–121 / 99–127 | 5% | CHA: Grayson Allen (out); Dennis Schroder (out); Grant Williams (out); Kon Knueppel (out) (-1.1)<br>ATL: CJ McCollum (out); Kingston Flemings (day-to-day); Jock Landale (out) (+1.3) | no edge | no edge | no edge |
| 7:30 PM | ORL @ BKN | ORL 115, BKN 109 | ORL 67% | ORL -200 / BKN +200<br>posted ORL -218 / BKN +181 | ORL -5.7 / ORL -5.5 (fav covers 52%) | 223.6 / 223.5 (over 49%) | 100–129 / 95–124 | 5% | ORL: Paolo Banchero (out) (+1.6) | no edge | no edge | no edge |
| 7:30 PM | IND @ CLE | IND 114, CLE 120 | CLE 67% | IND +200 / CLE -200<br>posted IND +220 / CLE -268 | CLE -5.8 / CLE -6.5 (fav covers 49%) | 234.7 / 234.5 (over 50%) | 100–129 / 106–135 | 5% | IND: Andrew Nembhard (day-to-day); Tyrese Haliburton (out); Johnny Furphy (out); Ben Sheppard (out); T.J. McConnell (day-to-day) (+0.3)<br>CLE: Evan Mobley (out); Jaylon Tyson (out); Peyton Watson (day-to-day) (-0.1) | no edge | no edge | no edge |
| 7:30 PM | TOR @ DET | TOR 105, DET 113 | DET 73% | TOR +275 / DET -275<br>posted TOR +237 / DET -291 | DET -8.1 / DET -7.5 (fav covers 52%) | 217.4 / 217.5 (over 49%) | 90–119 / 99–127 | 4% | TOR: RJ Barrett (out); Kawhi Leonard (out); Collin Murray-Boyles (out) (-2.5)<br>DET: Cade Cunningham (day-to-day); Duncan Robinson (out); Jalen Duren (out); Ronald Holland II (out) (+0.9) | no edge | no edge | no edge |
| 8:00 PM | WAS @ CHI | WAS 118, CHI 122 | CHI 61% | WAS +155 / CHI -155<br>posted WAS +120 / CHI -142 | CHI -3.8 / CHI -3.5 (fav covers 53%) | 240.4 / 240.5 (over 49%) | 104–133 / 107–137 | 5% | WAS: Jamir Watkins (out); Justin Champagnie (out); Tristan Vukcevic (out) (+0.1)<br>CHI: Caleb Wilson (out); Noa Essengue (day-to-day) (+1.9) | no edge | no edge | no edge |
| 8:00 PM | NOP @ OKC | NOP 109, OKC 120 | OKC 79% | NOP +380 / OKC -380<br>posted NOP +411 / OKC -546 | OKC -10.9 / OKC -11.5 (fav covers 47%) | 229.3 / 229.5 (over 49%) | 94–124 / 106–134 | 4% | NOP: Trey Murphy III (out); Dejounte Murray (out); Trendon Watford (out); Bennedict Mathurin (out); Bryce McGowens (out) (+0.1)<br>OKC: Chet Holmgren (out); Jalen Williams (out); Cason Wallace (out); Alex Caruso (day-to-day) (-1.1) | no edge | no edge | no edge |
| 9:30 PM | PHX @ UTA | PHX 116, UTA 112 | PHX 62% | PHX -160 / UTA +160<br>posted PHX -180 / UTA +151 | PHX -4.1 / PHX -4.5 (fav covers 50%) | 227.7 / 227.5 (over 49%) | 102–130 / 97–126 | 6% | PHX: Mark Williams (out) (+0.5)<br>UTA: Lauri Markkanen (out); Jaren Jackson Jr. (out); Jusuf Nurkic (out) (-2.3) | no edge | no edge | no edge |
| 10:00 PM | HOU @ DEN | HOU 112, DEN 113 | DEN 53% | HOU +115 / DEN -115<br>posted HOU +105 / DEN -125 | DEN -1.2 / DEN -1.5 (fav covers 51%) | 225.6 / 225.5 (over 49%) | 98–127 / 99–128 | 5% | HOU: Alperen Sengun (day-to-day); Clint Capela (out); Steven Adams (day-to-day) (-0.3) | no edge | no edge | no edge |
| 10:00 PM | SAC @ LAL | SAC 108, LAL 123 | LAL 85% | SAC +570 / LAL -570<br>posted SAC +600 / LAL -890 | LAL -14.3 / LAL -14.5 (fav covers 48%) | 231.2 / 231.5 (over 48%) | 94–123 / 108–137 | 3% | SAC: De'Andre Hunter (day-to-day); Maxime Raynaud (out); Precious Achiuwa (day-to-day) (+0.5)<br>LAL: Austin Reaves (out) (-1.2) | no edge | no edge | no edge |

## Saturday, November 21

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1:00 PM | MIL @ PHI | MIL 109, PHI 122 | PHI 84% | MIL +515 / PHI -515 | PHI -13.3 | 230.5 | 94–124 / 108–136 | 3% | MIL: Kyle Kuzma (day-to-day); Myles Turner (day-to-day) (+0.1)<br>PHI: Tyrese Maxey (day-to-day); Jaylen Brown (out); Dean Wade (day-to-day); Adem Bona (out); Dominick Barlow (out) (+0.7) | no line yet | no line yet | no line yet |
| 7:30 PM | POR @ NYK | POR 107, NYK 111 | NYK 62% | POR +160 / NYK -160 | NYK -3.7 | 217.3 | 93–121 / 96–124 | 5% | POR: Deni Avdija (day-to-day); Ja Morant (out); Robert Williams III (day-to-day); Chris Youngblood (out) (+0.0) | no line yet | no line yet | no line yet |
| 8:00 PM | LAC @ DAL | LAC 112, DAL 117 | DAL 63% | LAC +170 / DAL -170 | DAL -4.3 | 228.8 | 98–127 / 102–131 | 5% | LAC: Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out) (+0.2)<br>DAL: Dereck Lively II (out); Sergio de Larrea (out) (+0.8) | no line yet | no line yet | no line yet |
| 8:00 PM | MEM @ MIN | MEM 112, MIN 120 | MIN 72% | MEM +255 / MIN -255 | MIN -7.7 | 231.3 | 97–126 / 105–134 | 4% | MEM: Ty Jerome (out); Jerami Grant (day-to-day); Zach Edey (day-to-day); Scotty Pippen Jr. (out) (-1.2)<br>MIN: Anthony Edwards (out); Donte DiVincenzo (out); Jaylen Clark (out) (-0.8) | no line yet | no line yet | no line yet |
| 8:00 PM | NOP @ SAS | NOP 104, SAS 122 | SAS 90% | NOP +900 / SAS -900 | SAS -17.6 | 226.0 | 90–119 / 108–136 | 2% | NOP: Trey Murphy III (out); Dejounte Murray (out); Trendon Watford (out); Bennedict Mathurin (out); Bryce McGowens (out) (+0.1)<br>SAS: Dylan Harper (out); Tobias Harris (out) (+0.1) | no line yet | no line yet | no line yet |
| 10:00 PM | BOS @ SAC | BOS 119, SAC 103 | BOS 88% | BOS -745 / SAC +745 | BOS -15.7 | 221.8 | 105–133 / 89–117 | 3% | SAC: De'Andre Hunter (day-to-day); Maxime Raynaud (out); Precious Achiuwa (day-to-day) (+0.4) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 222 | 11.35 | 14.05 | 9.28 | 0.575 | 0.196 | 69.8% | 81.1% |
| Model only (before blending) | 222 | 11.58 | 13.89 | 9.31 | 0.588 | 0.202 | 69.4% | – |
| Elo | 222 | 11.95 | – | – | 0.618 | 0.215 | 64.0% | – |
| Final prediction, games with a line | 222 | 11.35 | 14.05 | 9.28 | 0.575 | 0.196 | 69.8% | 81.1% |
| Model only, games with a line | 222 | 11.58 | 13.89 | 9.31 | 0.588 | 0.202 | 69.4% | – |
| Betting line | 222 | 11.33 | 14.06 | 9.28 | 0.572 | 0.195 | 69.8% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.7% of games, happened in 5.4%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 15 | 2-13-0 | 5.6 | -2.59 | -46.2% | +6.5% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 5 of 6 games (83%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Wednesday, November 18

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| MEM @ CLE | 118–122 | 124–121 | 38% | CLE -4.4 / CLE -4.5 | yes |
| HOU @ IND | 117–109 | 119–104 | 72% | HOU -7.7 / HOU -8.5 | yes |
| MIL @ MIA | 112–123 | 130–137 | 80% | MIA -11.6 / MIA -11.5 | no |
| PHI @ ORL | 109–112 | 121–116 | 42% | ORL -2.5 / ORL -2.5 | yes |
| CHI @ BKN | 119–120 | 137–107 | 48% | BKN -1 / BKN -1.5 | no |
| WAS @ TOR | 110–113 | 103–99 | 41% | TOR -3.2 / TOR -3.5 | yes |
| DET @ NOP | 116–111 | 122–109 | 64% | DET -4.9 / DET -4.5 | yes |
| ATL @ OKC | 111–117 | 117–112 | 32% | OKC -6.2 / OKC -6.5 | yes |
| GSW @ DAL | 110–115 | 94–116 | 63% | DAL -4.4 / DAL -4.5 | no |
| BOS @ DEN | 111–109 | 101–105 | 42% | BOS -2.4 / BOS -2.5 | yes |
| UTA @ LAL | 109–120 | 109–97 | 20% | LAL -11.4 / LAL -11.5 | no |
| PHX @ SAC | 117–110 | 128–107 | 71% | PHX -7.2 / PHX -7.5 | yes |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | SAS | +8.3 | +8.2 | +3.2 | +5.2 | 98.4 | +0.1 | 1714 |
| 2 | BOS | +7.6 | +7.3 | +3.3 | +4.2 | 96.3 | +0.0 | 1648 |
| 3 | HOU | +6.0 | +5.8 | +3.5 | +2.5 | 97.4 | -0.3 | 1622 |
| 4 | DET | +5.7 | +5.7 | +2.4 | +3.3 | 99.2 | +0.9 | 1651 |
| 5 | MIN | +4.4 | +4.6 | +0.9 | +3.5 | 104.3 | -0.8 | 1613 |
| 6 | NYK | +4.4 | +4.1 | +1.2 | +3.2 | 93.3 | +0.0 | 1687 |
| 7 | LAL | +4.1 | +4.2 | +3.5 | +0.6 | 102.4 | -1.2 | 1603 |
| 8 | DEN | +4.1 | +4.0 | +3.5 | +0.6 | 99.0 | +0.2 | 1573 |
| 9 | OKC | +2.9 | +3.0 | -0.7 | +3.6 | 102.0 | -1.1 | 1640 |
| 10 | POR | +2.5 | +2.6 | +1.4 | +1.2 | 102.6 | +0.0 | 1573 |
| 11 | PHI | +2.1 | +2.1 | +1.3 | +0.8 | 100.6 | +0.7 | 1582 |
| 12 | PHX | +0.6 | +0.6 | +1.1 | -0.5 | 101.4 | +0.5 | 1527 |
| 13 | MIA | +0.5 | +0.5 | +1.9 | -1.4 | 105.2 | +0.1 | 1548 |
| 14 | ORL | +0.4 | +0.4 | -1.2 | +1.6 | 99.1 | +1.6 | 1519 |
| 15 | CLE | +0.4 | +0.4 | +1.8 | -1.4 | 100.7 | -0.1 | 1567 |
| 16 | TOR | -0.1 | -0.1 | -0.4 | +0.3 | 98.5 | -2.5 | 1489 |
| 17 | GSW | -0.5 | -0.5 | -0.7 | +0.2 | 100.6 | -3.6 | 1484 |
| 18 | MEM | -0.7 | -0.7 | +1.6 | -2.3 | 101.9 | -1.2 | 1475 |
| 19 | UTA | -1.0 | -1.1 | -1.9 | +0.8 | 101.2 | -2.3 | 1353 |
| 20 | IND | -1.3 | -1.4 | -0.4 | -0.9 | 103.2 | +0.3 | 1364 |
| 21 | DAL | -1.6 | -1.6 | -1.0 | -0.6 | 102.3 | +0.8 | 1448 |
| 22 | ATL | -2.0 | -2.2 | -2.0 | +0.0 | 107.7 | +1.4 | 1542 |
| 23 | LAC | -3.5 | -3.5 | -1.4 | -2.1 | 100.8 | +0.2 | 1443 |
| 24 | CHI | -3.7 | -4.0 | -1.6 | -2.1 | 108.4 | +1.9 | 1409 |
| 25 | NOP | -4.9 | -5.0 | -1.5 | -3.4 | 102.8 | +0.1 | 1363 |
| 26 | CHA | -5.0 | -4.8 | -4.6 | -0.4 | 96.0 | -1.1 | 1467 |
| 27 | WAS | -5.5 | -5.5 | -2.4 | -3.1 | 100.6 | +0.1 | 1315 |
| 28 | BKN | -7.2 | -7.2 | -2.9 | -4.3 | 100.7 | +0.1 | 1310 |
| 29 | MIL | -8.3 | -8.4 | -3.7 | -4.6 | 102.1 | +0.2 | 1313 |
| 30 | SAC | -8.7 | -8.9 | -4.2 | -4.6 | 101.8 | +0.5 | 1307 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +8.4 | +2.7 | +5.8 | 31 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.9 | +5.1 | +0.7 | 34 |
| 3 | Nikola Jokic | DEN | +5.1 | +4.5 | +0.5 | 38 |
| 4 | Kawhi Leonard | TOR | +4.6 | +3.6 | +0.9 | 30 |
| 5 | Giannis Antetokounmpo | MIA | +4.4 | +4.3 | +0.1 | 31 |
| 6 | Luka Doncic | LAL | +4.0 | +5.0 | -1.0 | 38 |
| 7 | Kyrie Irving | DAL | +3.7 | +3.6 | +0.1 | 32 |
| 8 | Joel Embiid | PHI | +2.9 | +1.7 | +1.2 | 32 |
| 9 | Neemias Queta | BOS | +2.8 | +1.1 | +1.8 | 24 |
| 10 | Franz Wagner | ORL | +2.5 | +1.5 | +1.0 | 37 |
| 11 | Derrick White | BOS | +2.5 | +0.5 | +2.0 | 31 |
| 12 | Donovan Mitchell | CLE | +2.4 | +3.3 | -0.9 | 34 |
| 13 | Javonte Green | DET | +2.3 | +0.2 | +2.1 | 24 |
| 14 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 15 | Ausar Thompson | DET | +2.2 | +0.1 | +2.1 | 30 |
| 16 | Paul Reed | DET | +2.1 | +0.7 | +1.4 | 24 |
| 17 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.1 | 30 |
| 18 | Bam Adebayo | MIA | +2.1 | +1.4 | +0.6 | 29 |
| 19 | LaMelo Ball | MIN | +2.0 | +3.5 | -1.5 | 29 |
| 20 | Dyson Daniels | ATL | +2.0 | +0.2 | +1.9 | 33 |
| 21 | Jarrett Allen | CLE | +2.0 | +1.9 | +0.1 | 29 |
| 22 | Fred VanVleet | HOU | +2.0 | +1.4 | +0.5 | 29 |
| 23 | Herbert Jones | NOP | +2.0 | -1.0 | +3.0 | 28 |
| 24 | Pascal Siakam | IND | +1.9 | +1.5 | +0.4 | 33 |
| 25 | Dean Wade | PHI | +1.7 | +0.9 | +0.7 | 30 |
| 26 | Ty Jerome | MEM | +1.6 | +2.6 | -1.0 | 30 |
| 27 | Cade Cunningham | DET | +1.6 | +1.8 | -0.2 | 38 |
| 28 | Damian Lillard | POR | +1.5 | +1.7 | -0.2 | 29 |
| 29 | Rudy Gobert | MIN | +1.5 | -3.7 | +5.3 | 26 |
| 30 | De'Aaron Fox | SAS | +1.4 | +1.3 | +0.1 | 28 |

## Current model fit

- Fitted on 5504 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.14 (offense) and 0.15 (defense); player lineup ratings 0.77 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.2% of recent games went to overtime.
