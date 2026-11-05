# NBA score predictions

Updated Wed Nov 04, 2026 08:43 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Wednesday, November 4

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9:00 PM | TOR @ DEN | TOR 113, DEN 119 | DEN 66% | TOR +195 / DEN -195<br>posted TOR +169 / DEN -203 | DEN -5.5 / DEN -5.5 (fav covers 51%) | 231.6 / 231.5 (over 49%) | 99–128 / 104–133 | 5% | TOR: Kawhi Leonard (out) (-1.7)<br>DEN: Spencer Jones (out) (+1.1) | no edge | no edge | no edge |
| 9:00 PM | POR @ PHX | POR 115, PHX 112 | POR 59% | POR -140 / PHX +140<br>posted POR -143 / PHX +121 | POR -3.1 / POR -3.5 (fav covers 50%) | 227.8 / 227.5 (over 49%) | 101–130 / 98–127 | 5% | POR: Ja Morant (out) (-0.4)<br>PHX: Mark Williams (out); Jordan Goodwin (out) (+0.2) | no edge | no edge | no edge |
| 9:30 PM | DAL @ SAS | DAL 107, SAS 119 | SAS 81% | DAL +430 / SAS -430<br>posted DAL +458 / SAS -620 | SAS -11.9 / SAS -12.5 (fav covers 47%) | 226.3 / 226.5 (over 49%) | 93–122 / 105–133 | 4% | DAL: Santi Aldama (out); Max Christie (out); Dereck Lively II (out); Sergio de Larrea (out) (+1.3)<br>SAS: Tobias Harris (out) (+0.7) | no edge | DAL ML (+458): EV +3.2%, 18%, stake 0.2u | no edge |
| 10:00 PM | LAL @ SAC | LAL 122, SAC 111 | LAL 81% | LAL -415 / SAC +415<br>posted LAL -650 / SAC +470 | LAL -11.9 / LAL -12.5 (fav covers 47%) | 233.0 / 233.5 (over 48%) | 108–137 / 96–126 | 3% | SAC: Maxime Raynaud (out); Keegan Murray (out) (+0.2) | no edge | no edge | no edge |
| 10:30 PM | MIA @ LAC | MIA 119, LAC 114 | MIA 64% | MIA -175 / LAC +175<br>posted MIA -216 / LAC +180 | MIA -4.7 / MIA -5.5 (fav covers 49%) | 233.6 / 233.5 (over 49%) | 104–134 / 100–129 | 5% | MIA: Giannis Antetokounmpo (day-to-day) (-0.8)<br>LAC: Brandon Ingram (out); Jordan Miller (out); Isaiah Jackson (day-to-day); Bradley Beal (out); Yanic Konan Niederhauser (out) (+0.3) | no edge | no edge | no edge |

## Thursday, November 5

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9:00 PM | ORL @ PHX | ORL 114, PHX 113 | ORL 51% | ORL -105 / PHX +105 | ORL -0.3 | 226.3 | 98–128 / 99–127 | 5% | ORL: Paolo Banchero (out); Jalen Suggs (out) (+0.5)<br>PHX: Mark Williams (out); Jordan Goodwin (out) (+0.2) | no line yet | no line yet | no line yet |
| 10:00 PM | MIA @ GSW | MIA 116, GSW 121 | GSW 66% | MIA +195 / GSW -195 | GSW -5.4 | 236.8 | 101–131 / 106–136 | 4% | MIA: Giannis Antetokounmpo (day-to-day) (-0.8)<br>GSW: Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out); Gui Santos (out) (-1.3) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 107 | 11.11 | 15.43 | 9.76 | 0.579 | 0.199 | 68.2% | 79.4% |
| Model only (before blending) | 107 | 11.62 | 15.11 | 9.89 | 0.608 | 0.212 | 65.4% | – |
| Elo | 107 | 12.02 | – | – | 0.646 | 0.229 | 59.8% | – |
| Final prediction, games with a line | 107 | 11.11 | 15.43 | 9.76 | 0.579 | 0.199 | 68.2% | 79.4% |
| Model only, games with a line | 107 | 11.62 | 15.11 | 9.89 | 0.608 | 0.212 | 65.4% | – |
| Betting line | 107 | 11.02 | 15.42 | 9.73 | 0.567 | 0.194 | 68.2% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.7% of games, happened in 4.7%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 5 | 0-5-0 | 1.9 | -1.88 | -100.0% | +8.8% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 4 of 5 games (80%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Monday, November 2

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| OKC @ CLE | 112–117 | 117–112 | 36% | CLE -4.6 / CLE -4.5 | yes |
| DET @ CHA | 108–102 | 124–91 | 67% | DET -5.6 / DET -5.5 | no |
| ATL @ IND | 118–109 | 108–104 | 74% | ATL -8.9 / ATL -9.5 | yes |
| BKN @ NYK | 102–116 | 90–103 | 86% | NYK -14.4 / NYK -14.5 | yes |
| WAS @ ORL | 111–114 | 103–94 | 41% | ORL -3 / ORL -2.5 | no |
| CHI @ PHI | 114–125 | 107–126 | 78% | PHI -10.4 / PHI -10.5 | yes |
| SAC @ DAL | 112–120 | 115–100 | 29% | DAL -7.5 / DAL -7.5 | no |
| NOP @ MEM | 113–118 | 135–134 (OT) | 34% | MEM -5.4 / MEM -5.5 | no |
| MIL @ MIN | 110–121 | 100–112 | 79% | MIN -10.9 / MIN -10.5 | yes |
| BOS @ HOU | 106–110 | 93–109 | 64% | HOU -4.4 / HOU -4.5 | yes |
| UTA @ SAS | 106–122 | 97–119 | 89% | SAS -16.6 / SAS -16.5 | yes |
| POR @ DEN | 114–118 | 118–110 | 38% | DEN -4.2 / DEN -4.5 | yes |
| PHX @ GSW | 113–115 | 113–116 | 57% | GSW -2.3 / GSW -2.5 | yes |
| TOR @ LAC | 112–108 | 125–118 | 62% | TOR -3.9 / TOR -4.5 | yes |
| MIA @ LAL | 117–119 | 117–138 | 57% | LAL -2.2 / LAL -2.5 | no |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | HOU | +7.6 | +7.5 | +4.0 | +3.6 | 98.9 | -0.5 | 1634 |
| 2 | DET | +6.3 | +6.3 | +2.0 | +4.3 | 101.0 | -0.1 | 1666 |
| 3 | SAS | +6.2 | +6.4 | +1.8 | +4.4 | 102.5 | +0.7 | 1694 |
| 4 | BOS | +5.9 | +5.8 | +3.2 | +2.7 | 97.5 | +0.3 | 1618 |
| 5 | MIN | +4.1 | +4.2 | +1.5 | +2.6 | 103.3 | -0.1 | 1600 |
| 6 | NYK | +4.0 | +3.9 | +1.1 | +2.9 | 97.1 | -0.6 | 1687 |
| 7 | LAL | +3.6 | +3.7 | +3.7 | -0.1 | 102.3 | +0.3 | 1587 |
| 8 | POR | +3.5 | +3.6 | +2.2 | +1.3 | 101.1 | -0.4 | 1550 |
| 9 | OKC | +3.2 | +3.2 | -0.4 | +3.6 | 100.1 | -0.2 | 1667 |
| 10 | PHI | +2.7 | +2.7 | +0.0 | +2.7 | 101.2 | +0.2 | 1575 |
| 11 | DEN | +1.9 | +1.9 | +3.3 | -1.3 | 98.2 | +1.1 | 1566 |
| 12 | GSW | +1.9 | +1.9 | +1.5 | +0.4 | 101.3 | -1.2 | 1505 |
| 13 | TOR | +1.9 | +2.0 | +0.5 | +1.4 | 106.2 | -1.8 | 1556 |
| 14 | CLE | +1.9 | +1.9 | +2.3 | -0.5 | 102.1 | -0.5 | 1578 |
| 15 | MIA | +0.3 | +0.3 | +1.9 | -1.6 | 106.5 | -0.9 | 1492 |
| 16 | MEM | -0.5 | -0.5 | +1.1 | -1.6 | 101.8 | +0.1 | 1421 |
| 17 | PHX | -0.9 | -0.9 | +1.2 | -2.1 | 101.7 | +0.2 | 1494 |
| 18 | ORL | -0.9 | -0.9 | -2.0 | +1.1 | 99.0 | +0.5 | 1505 |
| 19 | DAL | -1.3 | -1.3 | -0.9 | -0.4 | 101.7 | +1.2 | 1432 |
| 20 | ATL | -1.7 | -1.9 | -1.2 | -0.6 | 107.5 | +0.9 | 1538 |
| 21 | NOP | -3.1 | -3.2 | -1.1 | -2.0 | 105.8 | -0.1 | 1439 |
| 22 | IND | -3.2 | -3.3 | -1.3 | -1.9 | 102.0 | -0.4 | 1353 |
| 23 | LAC | -3.6 | -3.6 | -1.6 | -2.0 | 100.5 | +0.3 | 1480 |
| 24 | CHA | -4.2 | -4.0 | -3.8 | -0.4 | 96.0 | -1.0 | 1504 |
| 25 | WAS | -4.2 | -4.2 | -2.8 | -1.4 | 100.6 | +0.3 | 1345 |
| 26 | UTA | -4.5 | -4.7 | -3.6 | -0.9 | 102.9 | -0.8 | 1308 |
| 27 | CHI | -5.9 | -6.7 | -2.9 | -3.0 | 112.5 | -0.4 | 1359 |
| 28 | BKN | -6.3 | -6.4 | -3.7 | -2.6 | 101.1 | +0.8 | 1303 |
| 29 | SAC | -7.1 | -7.5 | -3.3 | -3.9 | 105.2 | +0.2 | 1350 |
| 30 | MIL | -7.4 | -7.8 | -2.9 | -4.5 | 105.6 | +0.6 | 1344 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +6.2 | +1.6 | +4.6 | 30 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.8 | +5.0 | +0.7 | 34 |
| 3 | Nikola Jokic | DEN | +4.9 | +5.2 | -0.3 | 37 |
| 4 | Kawhi Leonard | TOR | +4.5 | +3.6 | +0.9 | 30 |
| 5 | Luka Doncic | LAL | +4.4 | +5.5 | -1.1 | 36 |
| 6 | Giannis Antetokounmpo | MIA | +3.8 | +4.0 | -0.2 | 32 |
| 7 | Kyrie Irving | DAL | +3.6 | +3.4 | +0.2 | 31 |
| 8 | Joel Embiid | PHI | +3.4 | +1.7 | +1.7 | 31 |
| 9 | Herbert Jones | NOP | +3.0 | +0.0 | +3.0 | 25 |
| 10 | Fred VanVleet | HOU | +2.6 | +1.9 | +0.7 | 30 |
| 11 | Marcus Smart | HOU | +2.6 | +1.2 | +1.3 | 23 |
| 12 | Jarrett Allen | CLE | +2.3 | +1.8 | +0.6 | 28 |
| 13 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 14 | Ausar Thompson | DET | +2.1 | +0.0 | +2.1 | 26 |
| 15 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.0 | 30 |
| 16 | Franz Wagner | ORL | +2.0 | +0.8 | +1.2 | 37 |
| 17 | Cade Cunningham | DET | +2.0 | +1.8 | +0.2 | 31 |
| 18 | Stephen Curry | GSW | +1.9 | +4.4 | -2.4 | 31 |
| 19 | Neemias Queta | BOS | +1.9 | +0.9 | +1.0 | 24 |
| 20 | Lauri Markkanen | UTA | +1.8 | +1.7 | +0.1 | 28 |
| 21 | Ty Jerome | MEM | +1.8 | +3.3 | -1.5 | 31 |
| 22 | Dean Wade | PHI | +1.8 | +0.4 | +1.4 | 25 |
| 23 | LaMelo Ball | MIN | +1.8 | +3.8 | -2.0 | 28 |
| 24 | Donovan Mitchell | CLE | +1.7 | +2.3 | -0.6 | 32 |
| 25 | Derrick White | BOS | +1.7 | +0.1 | +1.6 | 30 |
| 26 | Bam Adebayo | MIA | +1.6 | +1.4 | +0.2 | 32 |
| 27 | Jrue Holiday | POR | +1.6 | +0.7 | +0.9 | 28 |
| 28 | Rudy Gobert | MIN | +1.5 | -3.5 | +5.0 | 29 |
| 29 | Kevin Durant | HOU | +1.5 | +3.2 | -1.7 | 32 |
| 30 | Paul Reed | DET | +1.4 | +0.1 | +1.3 | 29 |

## Current model fit

- Fitted on 5389 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.16 (offense) and 0.15 (defense); player lineup ratings 0.76 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.1% of recent games went to overtime.
