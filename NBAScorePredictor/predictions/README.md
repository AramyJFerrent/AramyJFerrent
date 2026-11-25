# NBA score predictions

Updated Wed Nov 25, 2026 12:26 AM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Wednesday, November 25

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5:00 PM | MIA @ PHI | MIA 118, PHI 120 | PHI 55% | MIA +120 / PHI -120<br>posted MIA -102 / PHI -116 | PHI -1.8 / PHI -1.5 (fav covers 52%) | 237.6 / 237.5 (over 49%) | 103–133 / 105–134 | 5% | MIA: Giannis Antetokounmpo (day-to-day) (-0.9)<br>PHI: Joel Embiid (day-to-day) (-0.5) | no edge | no edge | no edge |
| 7:00 PM | CHI @ CHA | CHI 109, CHA 112 | CHA 60% | CHI +150 / CHA -150<br>posted CHI +130 / CHA -155 | CHA -2.9 / CHA -3.5 (fav covers 50%) | 221.8 / 221.5 (over 50%) | 95–124 / 98–127 | 6% | CHI: Norman Powell (out); Jalen Smith (day-to-day); Caleb Wilson (out) (+0.3)<br>CHA: Sion James (day-to-day); Grayson Allen (out); Dennis Schroder (out); Kon Knueppel (out); Ryan Kalkbrenner (day-to-day) (-0.2) | no edge | no edge | no edge |
| 7:30 PM | CLE @ NYK | CLE 108, NYK 112 | NYK 60% | CLE +150 / NYK -150<br>posted CLE +137 / NYK -163 | NYK -3.3 / NYK -3.5 (fav covers 51%) | 219.9 / 219.5 (over 49%) | 94–123 / 98–126 | 6% | CLE: Evan Mobley (out) (-0.3)<br>NYK: OG Anunoby (out); Josh Hart (day-to-day); Karl-Anthony Towns (day-to-day) (-2.1) | no edge | no edge | no edge |
| 7:30 PM | MIN @ OKC | MIN 111, OKC 113 | OKC 54% | MIN +120 / OKC -120<br>posted MIN +101 / OKC -119 | OKC -1.2 / OKC -1.5 (fav covers 51%) | 223.8 / 223.5 (over 50%) | 97–126 / 98–127 | 6% | MIN: Anthony Edwards (out); Donte DiVincenzo (out); Jaylen Clark (out) (-0.5)<br>OKC: Chet Holmgren (out); Jalen Williams (out); Aday Mara (out); Cason Wallace (out); Jaylin Williams (out) (+1.5) | no edge | no edge | no edge |
| 8:00 PM | LAC @ MEM | LAC 111, MEM 118 | MEM 69% | LAC +225 / MEM -225<br>posted LAC +217 / MEM -264 | MEM -6.7 / MEM -6.5 (fav covers 51%) | 229.4 / 229.5 (over 48%) | 97–126 / 104–132 | 5% | LAC: Jordan Miller (out); Bradley Beal (out) (+0.5)<br>MEM: Cameron Boozer (out); Jerami Grant (out); Scotty Pippen Jr. (out) (+2.3) | no edge | no edge | no edge |
| 8:00 PM | BKN @ MIL | BKN 115, MIL 117 | MIL 55% | BKN +120 / MIL -120<br>posted BKN -106 / MIL -111 | MIL -1.5 / MIL -1.5 (fav covers 52%) | 231.6 / 231.5 (over 49%) | 100–130 / 102–131 | 5% | BKN: Nolan Traore (out) (+0.8) | no edge | no edge | no edge |
| 8:30 PM | PHX @ HOU | PHX 108, HOU 117 | HOU 75% | PHX +295 / HOU -295<br>posted PHX +319 / HOU -406 | HOU -8.8 / HOU -9.5 (fav covers 47%) | 224.5 / 224.5 (over 49%) | 93–122 / 102–131 | 4% | PHX: Mark Williams (out) (+0.5) | no edge | no edge | no edge |
| 10:00 PM | SAC @ GSW | SAC 107, GSW 112 | GSW 66% | SAC +195 / GSW -195<br>posted SAC +199 / GSW -241 | GSW -5.4 / GSW -5.5 (fav covers 51%) | 218.5 / 218.5 (over 49%) | 92–121 / 98–126 | 5% | SAC: Maxime Raynaud (out) (+0.7)<br>GSW: Yaxel Lendeborg (day-to-day); Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out); Stephen Curry (out); Brandon Williams (out) (-2.6) | no edge | no edge | no edge |
| 10:00 PM | SAS @ POR | SAS 115, POR 112 | SAS 58% | SAS -140 / POR +140<br>posted SAS -155 / POR +130 | SAS -2.8 / SAS -3.5 (fav covers 49%) | 226.6 / 226.5 (over 49%) | 100–129 / 97–127 | 5% | SAS: Dylan Harper (out); Victor Wembanyama (day-to-day); Tobias Harris (out); De'Aaron Fox (day-to-day) (-1.3)<br>POR: Ja Morant (out); Chris Youngblood (out) (+0.8) | no edge | no edge | no edge |

## Friday, November 27

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | MIA @ NYK | MIA 110, NYK 113 | NYK 61% | MIA +155 / NYK -155 | NYK -3.6 | 222.9 | 95–124 / 99–127 | 5% | MIA: Giannis Antetokounmpo (day-to-day) (-0.8)<br>NYK: OG Anunoby (out); Josh Hart (day-to-day); Karl-Anthony Towns (day-to-day) (-2.2) | no line yet | no line yet | no line yet |
| 7:30 PM | MIL @ DET | MIL 105, DET 118 | DET 84% | MIL +510 / DET -510 | DET -13 | 223.5 | 91–120 / 104–132 | 3% | DET: Cade Cunningham (out); Duncan Robinson (out); Jalen Duren (out) (-1.3) | no line yet | no line yet | no line yet |
| 7:30 PM | PHI @ IND | PHI 117, IND 116 | PHI 53% | PHI -110 / IND +110 | PHI -1 | 233.2 | 102–132 / 101–131 | 5% | PHI: Joel Embiid (day-to-day) (-0.5)<br>IND: Tyrese Haliburton (out); Aaron Nesmith (day-to-day); Ben Sheppard (out); T.J. McConnell (day-to-day) (-0.6) | no line yet | no line yet | no line yet |
| 7:30 PM | BKN @ TOR | BKN 109, TOR 115 | TOR 67% | BKN +205 / TOR -205 | TOR -6 | 223.8 | 95–124 / 100–129 | 5% | BKN: Nolan Traore (out) (+0.8)<br>TOR: RJ Barrett (out); Kawhi Leonard (out) (-2.5) | no line yet | no line yet | no line yet |
| 8:00 PM | ATL @ BOS | ATL 105, BOS 116 | BOS 79% | ATL +380 / BOS -380 | BOS -10.6 | 221.6 | 91–120 / 102–130 | 4% | ATL: CJ McCollum (out); Jock Landale (out) (+1.0)<br>BOS: Mitchell Robinson (out) (+0.4) | no line yet | no line yet | no line yet |
| 8:30 PM | MEM @ MIN | MEM 112, MIN 117 | MIN 64% | MEM +180 / MIN -180 | MIN -4.9 | 229.0 | 98–127 / 102–131 | 5% | MEM: Cameron Boozer (out); Jerami Grant (out); Scotty Pippen Jr. (out) (+2.4)<br>MIN: Anthony Edwards (out); Donte DiVincenzo (out); Jaylen Clark (out) (-0.5) | no line yet | no line yet | no line yet |
| 9:00 PM | DAL @ PHX | DAL 112, PHX 117 | PHX 62% | DAL +165 / PHX -165 | PHX -4.1 | 229.1 | 98–127 / 102–131 | 5% | DAL: Dereck Lively II (out); Sergio de Larrea (out) (+1.0)<br>PHX: Mark Williams (out) (+0.5) | no line yet | no line yet | no line yet |
| 9:30 PM | LAL @ SAS | LAL 110, SAS 116 | SAS 64% | LAL +180 / SAS -180 | SAS -5.2 | 225.9 | 96–125 / 101–130 | 5% | LAL: Austin Reaves (out) (-1.3)<br>SAS: Dylan Harper (out); Victor Wembanyama (day-to-day); Tobias Harris (out); De'Aaron Fox (day-to-day) (-1.3) | no line yet | no line yet | no line yet |
| 9:30 PM | DEN @ UTA | DEN 119, UTA 111 | DEN 71% | DEN -240 / UTA +240 | DEN -7.3 | 229.9 | 104–133 / 97–126 | 5% | UTA: Lauri Markkanen (out); Jaren Jackson Jr. (out); Jaxson Hayes (day-to-day); Jusuf Nurkic (out) (-2.5) | no line yet | no line yet | no line yet |
| 9:30 PM | NOP @ LAC | NOP 115, LAC 118 | LAC 60% | NOP +150 / LAC -150 | LAC -3.6 | 233.1 | 100–130 / 104–133 | 6% | NOP: Dejounte Murray (out); Trendon Watford (out); Bennedict Mathurin (out) (+0.8)<br>LAC: Jordan Miller (out); Bradley Beal (out) (+0.5) | no line yet | no line yet | no line yet |
| 9:30 PM | GSW @ POR | GSW 106, POR 115 | POR 77% | GSW +330 / POR -330 | POR -9.3 | 221.5 | 92–121 / 102–129 | 4% | GSW: Yaxel Lendeborg (day-to-day); Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out); Stephen Curry (out); Brandon Williams (out) (-2.6)<br>POR: Ja Morant (out); Chris Youngblood (out) (+0.8) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 258 | 10.84 | 14.49 | 9.33 | 0.576 | 0.197 | 69.8% | 80.8% |
| Model only (before blending) | 258 | 11.04 | 14.42 | 9.39 | 0.589 | 0.203 | 69.4% | – |
| Elo | 258 | 11.43 | – | – | 0.615 | 0.214 | 64.3% | – |
| Final prediction, games with a line | 258 | 10.84 | 14.49 | 9.33 | 0.576 | 0.197 | 69.8% | 80.8% |
| Model only, games with a line | 258 | 11.04 | 14.42 | 9.39 | 0.589 | 0.203 | 69.4% | – |
| Betting line | 258 | 10.83 | 14.50 | 9.34 | 0.574 | 0.196 | 69.8% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.6% of games, happened in 5.4%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 18 | 4-14-0 | 6.7 | -0.94 | -14.1% | +6.1% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 5 of 6 games (83%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Monday, November 23

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| MEM @ CHA | 110–106 | 117–111 | 62% | MEM -3.7 / MEM -3.5 | yes |
| POR @ PHI | 113–117 | 128–111 | 39% | PHI -3.7 / PHI -4.5 | yes |
| OKC @ IND | 113–110 | 120–125 | 40% | OKC -3.3 / OKC -4.5 | no |
| MIL @ TOR | 107–117 | 116–111 | 24% | TOR -9.9 / TOR -10.5 | yes |
| BKN @ MIN | 106–117 | 116–142 | 81% | MIN -11.6 / MIN -11.5 | no |
| CLE @ CHI | 124–116 | 108–122 | 29% | CLE -7.7 / CLE -8.5 | no |
| PHX @ NOP | 119–115 | 123–119 (OT) | 59% | PHX -3.6 / PHX -3.5 | yes |
| LAC @ HOU | 105–118 | 104–116 | 84% | HOU -13.1 / HOU -13.5 | yes |
| UTA @ LAL | 106–119 | 94–109 | 83% | LAL -13 / LAL -13.5 | yes |
| SAS @ SAC | 119–107 | 123–107 | 81% | SAS -12.1 / SAS -12.5 | yes |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | BOS | +7.3 | +6.9 | +2.3 | +5.0 | 95.4 | +0.3 | 1634 |
| 2 | SAS | +7.0 | +7.0 | +2.7 | +4.3 | 99.4 | -1.3 | 1721 |
| 3 | HOU | +6.4 | +6.2 | +4.0 | +2.3 | 98.2 | +0.0 | 1616 |
| 4 | DET | +5.2 | +5.1 | +2.1 | +3.1 | 97.4 | -1.3 | 1629 |
| 5 | MIN | +5.1 | +5.3 | +1.2 | +3.9 | 103.6 | -0.5 | 1615 |
| 6 | DEN | +5.1 | +5.1 | +5.1 | +0.0 | 100.3 | +0.0 | 1586 |
| 7 | LAL | +3.8 | +3.9 | +2.9 | +0.9 | 101.4 | -1.3 | 1607 |
| 8 | NYK | +3.7 | +3.5 | -0.3 | +4.0 | 93.9 | -2.1 | 1696 |
| 9 | POR | +3.3 | +3.4 | +1.8 | +1.6 | 102.0 | +0.8 | 1595 |
| 10 | OKC | +1.9 | +1.9 | -0.6 | +2.5 | 101.6 | +1.5 | 1617 |
| 11 | PHI | +1.6 | +1.6 | +1.6 | +0.0 | 100.4 | -0.5 | 1564 |
| 12 | MIA | +0.8 | +0.8 | +2.1 | -1.3 | 104.7 | -0.9 | 1559 |
| 13 | PHX | +0.7 | +0.7 | +0.8 | -0.1 | 100.8 | +0.5 | 1538 |
| 14 | TOR | +0.3 | +0.3 | +0.1 | +0.3 | 97.5 | -2.5 | 1485 |
| 15 | CLE | +0.3 | +0.3 | +1.7 | -1.4 | 100.9 | -0.3 | 1552 |
| 16 | MEM | -0.4 | -0.4 | +1.4 | -1.7 | 100.5 | +2.3 | 1496 |
| 17 | GSW | -0.4 | -0.4 | -1.0 | +0.7 | 98.4 | -2.6 | 1474 |
| 18 | ORL | -0.6 | -0.6 | -1.6 | +0.9 | 98.4 | +1.5 | 1497 |
| 19 | IND | -1.4 | -1.4 | -0.2 | -1.2 | 105.0 | -0.6 | 1373 |
| 20 | DAL | -1.8 | -1.9 | -1.2 | -0.7 | 101.1 | +1.0 | 1460 |
| 21 | UTA | -1.9 | -1.9 | -2.4 | +0.5 | 100.2 | -2.5 | 1339 |
| 22 | ATL | -2.0 | -2.1 | -2.2 | +0.2 | 106.2 | +1.0 | 1561 |
| 23 | LAC | -3.5 | -3.5 | -1.4 | -2.1 | 100.8 | +0.5 | 1430 |
| 24 | CHI | -3.8 | -4.1 | -1.7 | -2.1 | 106.7 | +0.3 | 1412 |
| 25 | WAS | -4.6 | -4.6 | -2.3 | -2.4 | 99.5 | +0.3 | 1350 |
| 26 | CHA | -5.2 | -4.9 | -4.6 | -0.6 | 95.7 | -0.1 | 1451 |
| 27 | NOP | -5.3 | -5.5 | -1.8 | -3.5 | 103.2 | +0.8 | 1355 |
| 28 | MIL | -7.1 | -7.3 | -2.5 | -4.5 | 103.2 | +0.0 | 1322 |
| 29 | BKN | -7.1 | -7.2 | -2.3 | -4.8 | 101.0 | +0.8 | 1304 |
| 30 | SAC | -7.5 | -7.6 | -3.9 | -3.6 | 100.6 | +0.7 | 1312 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +8.4 | +2.5 | +6.0 | 32 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.9 | +5.4 | +0.5 | 36 |
| 3 | Nikola Jokic | DEN | +5.2 | +4.9 | +0.3 | 39 |
| 4 | Kawhi Leonard | TOR | +4.6 | +3.6 | +1.0 | 30 |
| 5 | Giannis Antetokounmpo | MIA | +4.3 | +4.2 | +0.1 | 31 |
| 6 | Kyrie Irving | DAL | +3.9 | +3.6 | +0.2 | 31 |
| 7 | Luka Doncic | LAL | +3.7 | +4.8 | -1.1 | 36 |
| 8 | Joel Embiid | PHI | +2.9 | +1.9 | +1.0 | 33 |
| 9 | Dyson Daniels | ATL | +2.6 | +0.4 | +2.2 | 36 |
| 10 | Neemias Queta | BOS | +2.6 | +0.6 | +1.9 | 27 |
| 11 | Derrick White | BOS | +2.4 | +0.3 | +2.2 | 32 |
| 12 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 13 | Franz Wagner | ORL | +2.2 | +1.3 | +0.9 | 35 |
| 14 | Bam Adebayo | MIA | +2.2 | +1.7 | +0.5 | 32 |
| 15 | LaMelo Ball | MIN | +2.2 | +3.5 | -1.3 | 31 |
| 16 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.1 | 30 |
| 17 | Marcus Smart | HOU | +2.1 | +0.5 | +1.6 | 22 |
| 18 | Herbert Jones | NOP | +2.1 | -1.1 | +3.2 | 25 |
| 19 | Fred VanVleet | HOU | +2.0 | +1.6 | +0.4 | 31 |
| 20 | Paul Reed | DET | +2.0 | +0.7 | +1.4 | 26 |
| 21 | Ty Jerome | MEM | +2.0 | +2.7 | -0.6 | 29 |
| 22 | Pascal Siakam | IND | +2.0 | +1.4 | +0.6 | 33 |
| 23 | Ausar Thompson | DET | +2.0 | +0.1 | +1.9 | 34 |
| 24 | Jrue Holiday | POR | +1.9 | +1.1 | +0.8 | 29 |
| 25 | Javonte Green | DET | +1.9 | +0.1 | +1.8 | 21 |
| 26 | Damian Lillard | POR | +1.8 | +1.7 | +0.1 | 31 |
| 27 | Donovan Mitchell | CLE | +1.7 | +3.0 | -1.3 | 34 |
| 28 | De'Aaron Fox | SAS | +1.7 | +1.3 | +0.4 | 28 |
| 29 | Paul George | BOS | +1.5 | +0.4 | +1.1 | 31 |
| 30 | Austin Reaves | LAL | +1.5 | +2.6 | -1.1 | 33 |

## Current model fit

- Fitted on 5540 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.8 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.14 (offense) and 0.15 (defense); player lineup ratings 0.77 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 11.0 with correlation 0.23; 5.2% of recent games went to overtime.
