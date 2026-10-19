# NBA score predictions

Updated Mon Oct 19, 2026 04:27 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. The model pick is the side the model's own spread (before blending with the line) favors by 1 point or more; treat it as an experiment, since the backtest found no edge against closing lines.

## Tuesday, October 20

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Model pick vs line (edge) |
|---|---|---|---|---|---|---|---|---|---|---|
| 3:00 PM | BOS @ DET | BOS 111, DET 110 | BOS 55% | BOS -125 / DET +125 | BOS -1.8 | 221.1 | 97–126 / 96–124 | 5% | – | no line yet |
| 7:00 PM | PHI @ NYK | PHI 108, NYK 116 | NYK 72% | PHI +250 / NYK -250 | NYK -7.6 | 223.5 | 93–123 / 102–130 | 5% | – | no line yet |
| 9:30 PM | OKC @ SAS | OKC 108, SAS 112 | SAS 61% | OKC +155 / SAS -155 | SAS -3.6 | 220.5 | 94–123 / 98–126 | 5% | – | no line yet |

## Wednesday, October 21

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Model pick vs line (edge) |
|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | ATL @ ORL | ATL 109, ORL 115 | ORL 65% | ATL +185 / ORL -185 | ORL -5.1 | 224.0 | 95–124 / 100–129 | 5% | – | no line yet |
| 7:00 PM | MIL @ WAS | MIL 115, WAS 116 | WAS 50% | MIL +100 / WAS -100 | pick'em | 229.8 | 100–130 / 100–129 | 5% | – | no line yet |
| 7:30 PM | MIN @ MIA | MIN 112, MIA 116 | MIA 61% | MIN +160 / MIA -160 | MIA -4 | 228.7 | 98–127 / 102–131 | 5% | – | no line yet |
| 7:30 PM | CHA @ BKN | CHA 113, BKN 110 | CHA 60% | CHA -150 / BKN +150 | CHA -3.4 | 222.8 | 99–127 / 95–124 | 5% | – | no line yet |
| 7:30 PM | CHI @ TOR | CHI 109, TOR 118 | TOR 73% | CHI +275 / TOR -275 | TOR -8.4 | 227.2 | 95–124 / 103–132 | 5% | – | no line yet |
| 8:00 PM | UTA @ MEM | UTA 116, MEM 115 | UTA 53% | UTA -110 / MEM +110 | UTA -0.9 | 231.7 | 102–131 / 101–130 | 5% | – | no line yet |
| 8:00 PM | IND @ NOP | IND 117, NOP 114 | IND 56% | IND -130 / NOP +130 | IND -2.3 | 231.2 | 103–131 / 100–129 | 5% | – | no line yet |
| 8:30 PM | DAL @ HOU | DAL 108, HOU 116 | HOU 72% | DAL +255 / HOU -255 | HOU -7.8 | 223.8 | 94–123 / 102–130 | 5% | – | no line yet |
| 10:00 PM | GSW @ LAL | GSW 113, LAL 114 | GSW 50% | GSW -100 / LAL +100 | pick'em | 225.5 | 98–127 / 98–128 | 6% | – | no line yet |
| 10:00 PM | PHX @ POR | PHX 112, POR 115 | POR 57% | PHX +135 / POR -135 | POR -2.6 | 226.9 | 98–127 / 100–129 | 5% | – | no line yet |
| 10:30 PM | SAC @ LAC | SAC 110, LAC 116 | LAC 67% | SAC +205 / LAC -205 | LAC -5.7 | 225.6 | 95–125 / 101–130 | 5% | – | no line yet |

## How the 2026-27 predictions have done

Nothing graded yet; results appear here after the first predicted games finish.

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | SAS | +6.6 | +6.7 | +2.1 | +4.5 | 101.0 | +0.0 | 1703 |
| 2 | BOS | +6.2 | +6.0 | +3.0 | +3.2 | 97.9 | +0.0 | 1608 |
| 3 | NYK | +5.8 | +5.7 | +3.0 | +2.8 | 98.2 | +0.0 | 1727 |
| 4 | OKC | +5.1 | +5.1 | +0.8 | +4.3 | 100.0 | +0.0 | 1687 |
| 5 | HOU | +4.4 | +4.4 | +1.9 | +2.5 | 99.3 | +0.0 | 1571 |
| 6 | DEN | +3.5 | +3.5 | +4.6 | -1.0 | 100.2 | +0.0 | 1596 |
| 7 | ORL | +3.1 | +3.1 | -0.5 | +3.5 | 100.7 | +0.0 | 1551 |
| 8 | POR | +2.5 | +2.5 | +0.8 | +1.6 | 100.5 | +0.0 | 1522 |
| 9 | DET | +2.2 | +2.2 | +0.8 | +1.4 | 99.0 | +0.0 | 1616 |
| 10 | PHX | +1.8 | +1.8 | +1.7 | +0.1 | 99.9 | +0.0 | 1526 |
| 11 | TOR | +1.8 | +1.8 | +0.7 | +1.1 | 100.9 | +0.0 | 1546 |
| 12 | MIA | +1.7 | +1.7 | +1.3 | +0.4 | 100.2 | +0.0 | 1522 |
| 13 | CLE | +1.7 | +1.7 | +1.8 | -0.1 | 99.4 | +0.0 | 1579 |
| 14 | GSW | +1.7 | +1.7 | +1.2 | +0.5 | 99.9 | +0.0 | 1452 |
| 15 | PHI | +0.1 | +0.1 | +0.1 | +0.0 | 99.9 | +0.0 | 1534 |
| 16 | ATL | -0.1 | -0.1 | -0.1 | +0.0 | 101.6 | +0.0 | 1531 |
| 17 | MIN | -0.3 | -0.3 | +0.0 | -0.3 | 101.7 | +0.0 | 1558 |
| 18 | LAL | -0.4 | -0.4 | +0.3 | -0.7 | 98.8 | +0.0 | 1569 |
| 19 | CHA | -1.2 | -1.2 | -1.6 | +0.3 | 100.0 | +0.0 | 1597 |
| 20 | DAL | -1.2 | -1.3 | -1.0 | -0.2 | 101.0 | +0.0 | 1393 |
| 21 | LAC | -1.6 | -1.6 | -0.7 | -0.9 | 99.7 | +0.0 | 1525 |
| 22 | IND | -1.8 | -1.8 | -0.2 | -1.6 | 101.5 | +0.0 | 1379 |
| 23 | UTA | -2.4 | -2.5 | -1.5 | -0.9 | 102.5 | +0.0 | 1342 |
| 24 | CHI | -4.5 | -4.6 | -3.1 | -1.4 | 102.6 | +0.0 | 1384 |
| 25 | MIL | -4.6 | -4.6 | -1.7 | -2.8 | 100.1 | +0.0 | 1388 |
| 26 | MEM | -5.3 | -5.4 | -2.0 | -3.3 | 102.2 | +0.0 | 1336 |
| 27 | SAC | -5.5 | -5.5 | -2.6 | -2.9 | 100.3 | +0.0 | 1374 |
| 28 | NOP | -6.0 | -6.1 | -2.5 | -3.4 | 101.5 | +0.0 | 1429 |
| 29 | WAS | -6.6 | -6.7 | -2.9 | -3.6 | 102.1 | +0.0 | 1285 |
| 30 | BKN | -6.7 | -6.7 | -3.8 | -2.9 | 100.2 | +0.0 | 1320 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Shai Gilgeous-Alexander | OKC | +5.6 | +4.9 | +0.7 | 37 |
| 2 | Nikola Jokic | DEN | +5.5 | +5.8 | -0.3 | 40 |
| 3 | Victor Wembanyama | SAS | +5.4 | +1.1 | +4.3 | 40 |
| 4 | Giannis Antetokounmpo | MIL | +4.9 | +4.4 | +0.6 | 27 |
| 5 | Kawhi Leonard | LAC | +4.9 | +4.3 | +0.6 | 35 |
| 6 | Alex Caruso | OKC | +3.4 | -0.2 | +3.6 | 29 |
| 7 | Joel Embiid | PHI | +2.7 | +2.0 | +0.7 | 31 |
| 8 | Franz Wagner | ORL | +2.7 | +1.1 | +1.6 | 28 |
| 9 | Kyrie Irving | DAL | +2.7 | +2.7 | +0.0 | 27 |
| 10 | Bam Adebayo | MIA | +2.5 | +0.9 | +1.5 | 25 |
| 11 | Chet Holmgren | OKC | +2.4 | +0.6 | +1.8 | 29 |
| 12 | OG Anunoby | NYK | +2.2 | +0.6 | +1.6 | 36 |
| 13 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 14 | Luka Doncic | LAL | +2.1 | +3.3 | -1.2 | 33 |
| 15 | Lauri Markkanen | UTA | +2.1 | +1.4 | +0.7 | 27 |
| 16 | Derrick White | BOS | +2.0 | +0.1 | +1.9 | 38 |
| 17 | Jarrett Allen | CLE | +2.0 | +1.6 | +0.4 | 30 |
| 18 | Dyson Daniels | ATL | +2.0 | +1.0 | +1.0 | 24 |
| 19 | Marcus Smart | LAL | +1.9 | +0.4 | +1.5 | 34 |
| 20 | Pascal Siakam | IND | +1.8 | +1.4 | +0.4 | 30 |
| 21 | Ausar Thompson | DET | +1.6 | -0.2 | +1.8 | 29 |
| 22 | Fred VanVleet | HOU | +1.5 | +0.9 | +0.6 | 40 |
| 23 | Cade Cunningham | DET | +1.5 | +1.5 | +0.0 | 40 |
| 24 | Donovan Mitchell | CLE | +1.4 | +2.0 | -0.6 | 36 |
| 25 | Jayson Tatum | BOS | +1.2 | +1.2 | +0.1 | 35 |
| 26 | Devin Booker | PHX | +1.2 | +2.4 | -1.1 | 39 |
| 27 | Julian Champagnie | SAS | +1.2 | +1.3 | -0.1 | 31 |
| 28 | Amen Thompson | HOU | +1.0 | +0.3 | +0.6 | 44 |
| 29 | Devin Vassell | SAS | +0.9 | +0.6 | +0.3 | 38 |
| 30 | Anthony Davis | DAL | +0.9 | -0.2 | +1.1 | 35 |

## Current model fit

- Fitted on 5282 games from 2022-23 to 2025-26.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.16 (offense) and 0.17 (defense); player lineup ratings 0.76 and 0.74.
- Blend: 81% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.2% of recent games went to overtime.
