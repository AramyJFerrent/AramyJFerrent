# College football score predictions

Updated Sun Oct 25, 2026 01:11 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 9

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 10/27 7:00 PM | Delaware @ Western Kentucky | Delaware 31, Western Kentucky 28 | Delaware 54% | Delaware -115 / Western Kentucky +115 | 29.1 – 27.8 | 14–44 / 14–42 | Western Kentucky -0.3 / Delaware -1.5 | 54.6 / 57.5 | no edge | no edge | no edge |  |
| Tue 10/27 8:00 PM | Sam Houston @ Missouri State | Sam Houston 24, Missouri State 27 | Missouri State 64% | Sam Houston +180 / Missouri State -180 | 22.7 – 28.3 | 10–37 / 14–43 | Missouri State -6.3 / Missouri State -5.5 | 49.2 / 51.5 | no edge | no edge | no edge |  |
| Wed 10/28 7:00 PM | Kennesaw State @ Middle Tennessee | Kennesaw State 24, Middle Tennessee 27 | Middle Tennessee 59% | Kennesaw State +145 / Middle Tennessee -145 | 23.3 – 26.4 | 10–37 / 13–41 | Middle Tennessee -3.2 / Middle Tennessee -3.0 | 50.5 / 49.5 | no edge | no edge | no edge |  |
| Wed 10/28 8:00 PM | Jacksonville State @ New Mexico State | Jacksonville State 27, New Mexico State 24 | Jacksonville State 59% | Jacksonville State -145 / New Mexico State +145 | 26.6 – 23.2 | 13–41 / 10–37 | Jacksonville State -6.7 / Jacksonville State -3.0 | 50.9 / 49.5 | no edge | no edge | no edge |  |
| Thu 10/29 7:30 PM | Florida Atlantic @ North Texas | Florida Atlantic 31, North Texas 41 | North Texas 74% | Florida Atlantic +290 / North Texas -290 | 30.9 – 41.3 | 17–45 / 27–57 | North Texas -9.8 / North Texas -10.5 | 71.2 / 72.5 | no edge | no edge | no edge |  |
| Thu 10/29 7:30 PM | Troy @ James Madison | Troy 17, James Madison 38 | James Madison 91% | Troy +1010 / James Madison -1010 | 16.5 – 35.9 | 6–28 / 21–52 | James Madison -18.2 / James Madison -19.5 | 51.6 / 52.5 | no edge | no edge | no edge |  |
| Fri 10/30 7:00 PM | Tulane @ Charlotte | Tulane 31, Charlotte 17 | Tulane 79% | Tulane -385 / Charlotte +385 | 29.3 – 17.5 | 14–44 / 7–30 | Tulane -15.5 / Tulane -11.5 | 47.8 / 46.5 | no edge | no edge | no edge |  |
| Fri 10/30 7:30 PM | Baylor @ UCF | Baylor 21, UCF 24 | UCF 53% | Baylor +115 / UCF -115 | 23.5 – 24.8 | 10–37 / 12–38 | Baylor -0.7 / UCF -1.5 | 51.2 / 47.5 | no edge | no edge | no edge |  |
| Fri 10/30 10:30 PM | Kent State @ Sacramento State | Kent State 27, Sacramento State 20 | Kent State 75% | Kent State -295 / Sacramento State +295 | 28.2 – 18.6 | 14–42 / 7–31 | Sacramento State -0.5 / Kent State -10.5 | 48.0 / 46.5 | no edge | Sacramento State (+340): EV +6.0%, 24%, stake 0.4u | no edge |  |
| Sat 10/31 TBA | Northwestern @ Oregon | Northwestern 24, Oregon 27 | Oregon 60% | Northwestern +150 / Oregon -150 | 23.4 – 27.1 | 10–37 / 14–42 | Oregon -5.6 / Oregon -3.5 | 50.5 / 50.5 | no edge | no edge | no edge |  |
| Sat 10/31 TBA | Purdue @ Penn State | Purdue 24, Penn State 31 | Penn State 72% | Purdue +260 / Penn State -260 | 21.6 – 30.5 | 10–35 / 17–45 | Penn State -12.1 / Penn State -8.5 | 50.6 / 52.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | Arizona @ Texas Tech | Arizona 24, Texas Tech 27 | Texas Tech 63% | Arizona +170 / Texas Tech -170 | 24.6 – 29.6 | 12–38 / 16–45 | Texas Tech -9.5 / Texas Tech -4.5 | 48.9 / 55.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | California @ NC State | California 24, NC State 31 | NC State 71% | California +240 / NC State -240 | 24.3 – 33.0 | 10–38 / 18–48 | NC State -10.9 / NC State -8.5 | 60.3 / 56.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | SMU @ Syracuse | SMU 34, Syracuse 24 | SMU 75% | SMU -300 / Syracuse +300 | 33.5 – 23.5 | 19–49 / 10–37 | SMU -9.8 / SMU -10.0 | 54.6 / 57.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | Boston College @ Duke | Boston College 21, Duke 28 | Duke 69% | Boston College +225 / Duke -225 | 20.3 – 27.8 | 7–34 / 14–42 | Duke -12.5 / Duke -7.0 | 50.3 / 47.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | Wisconsin @ Iowa | Wisconsin 17, Iowa 20 | Iowa 61% | Wisconsin +155 / Iowa -155 | 18.2 – 22.0 | 7–31 / 10–35 | Iowa -6.8 / Iowa -3.5 | 43.4 / 39.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | Illinois @ Maryland | Illinois 27, Maryland 24 | Illinois 57% | Illinois -135 / Maryland +135 | 27.8 – 25.1 | 14–42 / 13–38 | Maryland -0.3 / Illinois -3.0 | 54.3 / 52.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | Notre Dame vs Navy | Notre Dame 42, Navy 10 | Notre Dame 99% | Notre Dame -7065 / Navy +7065 | 41.2 – 10.9 | 27–58 / 0–21 | Notre Dame -28.5 / Notre Dame -30.5 | 50.8 / 52.5 | no edge | no edge | no edge | neutral site |
| Sat 10/31 12:00 PM | UAB @ South Florida | UAB 20, South Florida 27 | South Florida 75% | UAB +295 / South Florida -295 | 18.7 – 28.3 | 7–31 / 14–42 | South Florida -10.1 / South Florida -9.5 | 50.4 / 46.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | Bowling Green @ Western Michigan | Bowling Green 14, Western Michigan 31 | Western Michigan 87% | Bowling Green +640 / Western Michigan -640 | 14.1 – 29.6 | 3–26 / 15–45 | Western Michigan -15.0 / Western Michigan -15.5 | 44.4 / 43.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:30 PM | Michigan @ Rutgers | Michigan 31, Rutgers 17 | Michigan 84% | Michigan -510 / Rutgers +510 | 31.0 – 16.9 | 17–46 / 6–29 | Michigan -15.5 / Michigan -14.0 | 49.6 / 47.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:45 PM | Auburn @ Ole Miss | Auburn 24, Ole Miss 35 | Ole Miss 79% | Auburn +375 / Ole Miss -375 | 21.9 – 34.2 | 10–35 / 20–49 | Ole Miss -9.4 / Ole Miss -12.5 | 58.6 / 55.5 | no edge | no edge | no edge |  |
| Sat 10/31 1:00 PM | Marshall @ Old Dominion | Marshall 24, Old Dominion 21 | Marshall 58% | Marshall -140 / Old Dominion +140 | 24.8 – 21.7 | 13–38 / 9–35 | Marshall -4.2 / Marshall -3.0 | 47.0 / 46.5 | no edge | no edge | no edge |  |
| Sat 10/31 2:00 PM | Kansas State @ Colorado | Kansas State 27, Colorado 24 | Kansas State 58% | Kansas State -135 / Colorado +135 | 26.1 – 23.1 | 13–41 / 10–37 | Kansas State -7.8 / Kansas State -2.5 | 52.2 / 48.5 | no edge | no edge | no edge |  |
| Sat 10/31 2:00 PM | Coastal Carolina @ Georgia State | Coastal Carolina 24, Georgia State 31 | Georgia State 67% | Coastal Carolina +205 / Georgia State -205 | 25.4 – 32.0 | 12–39 / 17–48 | Georgia State -7.6 / Georgia State -6.5 | 56.7 / 57.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:00 PM | UConn @ Air Force | UConn 24, Air Force 27 | Air Force 57% | UConn +135 / Air Force -135 | 26.7 – 29.5 | 13–41 / 15–44 | Air Force -1.4 / Air Force -3.0 | 58.9 / 55.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:00 PM | Temple @ East Carolina | Temple 24, East Carolina 27 | East Carolina 64% | Temple +175 / East Carolina -175 | 22.6 – 27.5 | 10–35 / 14–42 | East Carolina -8.4 / East Carolina -4.5 | 52.3 / 49.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:00 PM | Louisiana Tech @ South Alabama | Louisiana Tech 31, South Alabama 28 | Louisiana Tech 61% | Louisiana Tech -155 / South Alabama +155 | 30.5 – 26.1 | 17–45 / 13–41 | Louisiana Tech -2.6 / Louisiana Tech -4.5 | 57.1 / 56.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:15 PM | Stanford @ Louisville | Stanford 20, Louisville 41 | Louisville 92% | Stanford +1195 / Louisville -1195 | 19.5 – 41.0 | 7–32 / 26–57 | Louisville -26.8 / Louisville -21.0 | 56.2 / 61.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Florida vs Georgia | Florida 24, Georgia 34 | Georgia 75% | Florida +305 / Georgia -305 | 22.7 – 33.1 | 10–37 / 17–48 | Georgia -9.3 / Georgia -10.5 | 53.2 / 56.5 | no edge | no edge | no edge | neutral site |
| Sat 10/31 3:30 PM | Arizona State @ BYU | Arizona State 17, BYU 31 | BYU 84% | Arizona State +535 / BYU -535 | 18.0 – 32.5 | 7–31 / 17–48 | BYU -14.6 / BYU -14.5 | 50.6 / 50.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Kansas @ TCU | Kansas 21, TCU 24 | TCU 61% | Kansas +155 / TCU -155 | 22.3 – 26.4 | 10–35 / 13–41 | Kansas -0.6 / TCU -4.5 | 49.4 / 48.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Minnesota @ Indiana | Minnesota 10, Indiana 31 | Indiana 93% | Minnesota +1245 / Indiana -1245 | 11.2 – 30.8 | 3–21 / 16–45 | Indiana -21.0 / Indiana -19.5 | 40.2 / 42.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Colorado State @ Utah State | Colorado State 31, Utah State 34 | Utah State 59% | Colorado State +140 / Utah State -140 | 29.6 – 33.1 | 15–45 / 18–48 | Utah State -3.3 / Utah State -3.5 | 55.5 / 64.5 | no edge | no edge | Under 64.5 (-110): EV +3.6%, 54%, stake 1.0u |  |
| Sat 10/31 3:30 PM | UTEP @ North Dakota State | UTEP 10, North Dakota State 38 | North Dakota State 98% | UTEP +4365 / North Dakota State -4365 | 10.2 – 37.8 | 0–20 / 23–54 | North Dakota State -27.7 / North Dakota State -27.5 | 41.9 / 49.5 | no edge | no edge | Under 49.5 (-110*): EV +3.2%, 54%, stake 0.9u | * price not posted; assumed -110 |
| Sat 10/31 3:30 PM | Florida International @ Liberty | Florida International 17, Liberty 27 | Liberty 79% | Florida International +385 / Liberty -385 | 16.5 – 28.4 | 6–29 / 14–42 | Liberty -15.1 / Liberty -11.5 | 46.6 / 44.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Southern Miss @ UL Monroe | Southern Miss 27, UL Monroe 24 | Southern Miss 58% | Southern Miss -140 / UL Monroe +140 | 28.0 – 25.0 | 14–42 / 13–38 | Southern Miss -2.8 / Southern Miss -3.0 | 55.3 / 52.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:45 PM | Utah @ Cincinnati | Utah 31, Cincinnati 24 | Utah 67% | Utah -205 / Cincinnati +205 | 31.8 – 24.8 | 17–47 / 12–38 | Utah -7.0 / Utah -7.0 | 60.8 / 55.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:45 PM | Virginia @ Wake Forest | Virginia 17, Wake Forest 31 | Wake Forest 83% | Virginia +480 / Wake Forest -480 | 17.8 – 31.5 | 7–31 / 17–47 | Wake Forest -15.3 / Wake Forest -13.5 | 48.4 / 49.5 | no edge | no edge | no edge |  |
| Sat 10/31 4:00 PM | New Mexico @ San José State | New Mexico 27, San José State 13 | New Mexico 85% | New Mexico -585 / San José State +585 | 28.7 – 14.4 | 14–44 / 3–26 | New Mexico -12.0 / New Mexico -14.5 | 49.5 / 41.5 | no edge | no edge | no edge |  |
| Sat 10/31 4:15 PM | South Carolina @ Oklahoma | South Carolina 21, Oklahoma 24 | Oklahoma 62% | South Carolina +160 / Oklahoma -160 | 20.2 – 24.4 | 7–34 / 10–38 | Oklahoma -11.7 / Oklahoma -3.5 | 44.6 / 44.5 | no edge | no edge | no edge |  |
| Sat 10/31 4:15 PM | Nevada @ UCLA | Nevada 10, UCLA 34 | UCLA 96% | Nevada +2185 / UCLA -2185 | 11.7 – 35.1 | 3–21 / 20–51 | UCLA -33.6 / UCLA -22.5 | 48.0 / 46.5 | no edge | no edge | no edge |  |
| Sat 10/31 6:30 PM | App State @ Georgia Southern | App State 24, Georgia Southern 27 | Georgia Southern 59% | App State +140 / Georgia Southern -140 | 26.0 – 29.1 | 13–40 / 14–44 | App State -0.9 / Georgia Southern -3.5 | 57.3 / 54.5 | no edge | no edge | no edge |  |
| Sat 10/31 7:00 PM | Oklahoma State @ Iowa State | Oklahoma State 31, Iowa State 24 | Oklahoma State 71% | Oklahoma State -245 / Iowa State +245 | 32.3 – 23.7 | 17–48 / 10–38 | Iowa State -6.0 / Oklahoma State -10.0 | 54.1 / 56.5 | Iowa State +10.0 (-110*): EV +3.1%, 52%, stake 0.9u | Iowa State (+300): EV +8.5%, 27%, stake 0.7u | no edge | * price not posted; assumed -110 |
| Sat 10/31 7:00 PM | Clemson @ Florida State | Clemson 24, Florida State 27 | Florida State 63% | Clemson +170 / Florida State -170 | 22.7 – 28.1 | 10–37 / 14–42 | Florida State -3.9 / Florida State -5.5 | 52.0 / 50.5 | no edge | no edge | no edge |  |
| Sat 10/31 7:00 PM | Washington State @ San Diego State | Washington State 21, San Diego State 24 | San Diego State 56% | Washington State +130 / San Diego State -130 | 21.2 – 23.5 | 9–34 / 10–37 | San Diego State -2.4 / – | 44.7 / – | no line yet | no line yet (fair: San Diego State -130) | no line yet |  |
| Sat 10/31 7:30 PM | Mississippi State @ Texas | Mississippi State 17, Texas 34 | Texas 92% | Mississippi State +1125 / Texas -1125 | 15.5 – 35.2 | 3–27 / 20–51 | Texas -10.9 / Texas -20.5 | 51.8 / 50.5 | no edge | Mississippi State (+800): EV +3.9%, 12%, stake 0.1u | no edge |  |
| Sat 10/31 7:30 PM | Georgia Tech @ Pittsburgh | Georgia Tech 24, Pittsburgh 31 | Pittsburgh 68% | Georgia Tech +215 / Pittsburgh -215 | 22.8 – 30.1 | 10–37 / 16–45 | Pittsburgh -9.9 / Pittsburgh -7.0 | 54.7 / 52.5 | no edge | no edge | no edge |  |
| Sat 10/31 7:30 PM | Miami @ North Carolina | Miami 34, North Carolina 17 | Miami 87% | Miami -695 / North Carolina +695 | 34.4 – 17.6 | 20–50 / 7–31 | Miami -20.1 / Miami -16.5 | 54.1 / 51.5 | no edge | no edge | no edge |  |
| Sat 10/31 7:30 PM | Ohio State @ USC | Ohio State 28, USC 21 | Ohio State 69% | Ohio State -225 / USC +225 | 29.5 – 22.2 | 14–45 / 10–35 | Ohio State -10.1 / Ohio State -7.0 | 56.8 / 50.5 | no edge | no edge | no edge |  |
| Sat 10/31 7:45 PM | Missouri @ Arkansas | Missouri 27, Arkansas 17 | Missouri 76% | Missouri -310 / Arkansas +310 | 29.0 – 18.8 | 14–44 / 7–31 | Missouri -12.8 / Missouri -10.0 | 49.2 / 47.5 | no edge | no edge | no edge |  |
| Sat 10/31 8:00 PM | Washington @ Nebraska | Washington 21, Nebraska 28 | Nebraska 74% | Washington +280 / Nebraska -280 | 19.9 – 29.4 | 7–33 / 14–44 | Nebraska -8.8 / Nebraska -9.5 | 48.7 / 49.5 | no edge | no edge | no edge |  |
| Sat 10/31 8:00 PM | Army @ Memphis | Army 24, Memphis 31 | Memphis 65% | Army +190 / Memphis -190 | 25.7 – 31.6 | 13–41 / 17–47 | Memphis -5.7 / Memphis -6.0 | 60.5 / 56.5 | no edge | no edge | no edge |  |
| Sat 10/31 10:00 PM | Texas State @ Boise State | Texas State 24, Boise State 38 | Boise State 78% | Texas State +355 / Boise State -355 | 26.6 – 38.8 | 13–41 / 24–55 | Boise State -8.7 / Boise State -12.5 | 65.0 / 65.5 | no edge | no edge | no edge |  |
| Sat 10/31 10:30 PM | Northern Illinois @ UNLV | Northern Illinois 14, UNLV 38 | UNLV 96% | Northern Illinois +2135 / UNLV -2135 | 14.4 – 38.3 | 3–26 / 24–55 | UNLV -17.4 / UNLV -24.5 | 53.7 / 52.5 | no edge | no edge | no edge |  |
| Sat 10/31 11:00 PM | Oregon State @ Fresno State | Oregon State 31, Fresno State 24 | Oregon State 67% | Oregon State -205 / Fresno State +205 | 32.0 – 25.3 | 17–47 / 13–40 | Oregon State -3.8 / Oregon State -7.0 | 56.5 / 57.5 | no edge | no edge | no edge |  |

## 2026 Week 10

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/03 7:00 PM | Ohio @ Akron | Ohio 34, Akron 17 | Ohio 90% | Ohio -950 / Akron +950 | 34.9 – 15.8 | 20–51 / 6–28 | Ohio -19.0 / – | 51.2 / – | no line yet | no line yet (fair: Ohio -950) | no line yet |  |
| Tue 11/03 7:00 PM | Buffalo @ Miami (OH) | Buffalo 17, Miami (OH) 31 | Miami (OH) 81% | Buffalo +415 / Miami (OH) -415 | 17.8 – 30.0 | 6–31 / 16–45 | Miami (OH) -12.2 / – | 48.4 / – | no line yet | no line yet (fair: Miami (OH) -415) | no line yet |  |
| Wed 11/04 TBA | Ball State @ Massachusetts | Ball State 24, Massachusetts 27 | Massachusetts 58% | Ball State +140 / Massachusetts -140 | 23.1 – 25.8 | 10–37 / 13–40 | Massachusetts -2.7 / – | 48.9 / – | no line yet | no line yet (fair: Massachusetts -140) | no line yet |  |
| Wed 11/04 TBA | Central Michigan vs Eastern Michigan | Central Michigan 27, Eastern Michigan 24 | Central Michigan 60% | Central Michigan -150 / Eastern Michigan +150 | 27.1 – 23.4 | 14–41 / 10–37 | Central Michigan -3.7 / – | 50.4 / – | no line yet | no line yet (fair: Central Michigan -150) | no line yet | neutral site |
| Wed 11/04 TBA | Toledo @ Sacramento State | Toledo 38, Sacramento State 17 | Toledo 92% | Toledo -1135 / Sacramento State +1135 | 35.7 – 15.6 | 21–52 / 3–28 | Toledo -20.0 / – | 51.3 / – | no line yet | no line yet (fair: Toledo -1135) | no line yet |  |
| Thu 11/05 8:00 PM | UTSA @ Florida Atlantic | UTSA 34, Florida Atlantic 31 | UTSA 56% | UTSA -130 / Florida Atlantic +130 | 33.7 – 31.4 | 20–49 / 17–46 | UTSA -2.3 / – | 65.2 / – | no line yet | no line yet (fair: UTSA -130) | no line yet |  |
| Thu 11/05 8:00 PM | James Madison @ Southern Miss | James Madison 38, Southern Miss 17 | James Madison 90% | James Madison -890 / Southern Miss +890 | 36.7 – 18.0 | 21–52 / 7–31 | James Madison -18.7 / – | 54.7 / – | no line yet | no line yet (fair: James Madison -890) | no line yet |  |
| Fri 11/06 7:00 PM | Virginia Tech @ SMU | Virginia Tech 21, SMU 31 | SMU 77% | Virginia Tech +330 / SMU -330 | 22.2 – 33.0 | 10–35 / 17–48 | SMU -10.9 / – | 55.2 / – | no line yet | no line yet (fair: SMU -330) | no line yet |  |
| Fri 11/06 7:30 PM | South Florida @ East Carolina | South Florida 24, East Carolina 21 | South Florida 50% | South Florida -100 / East Carolina +100 | 24.7 – 24.7 | 12–38 / 12–38 | PK / – | 49.4 / – | no line yet | no line yet (fair: South Florida -100) | no line yet |  |
| Fri 11/06 8:00 PM | Nebraska @ Illinois | Nebraska 31, Illinois 24 | Nebraska 71% | Nebraska -245 / Illinois +245 | 31.2 – 23.0 | 17–45 / 10–37 | Nebraska -8.2 / – | 54.2 / – | no line yet | no line yet (fair: Nebraska -245) | no line yet |  |
| Fri 11/06 9:00 PM | New Mexico @ Nevada | New Mexico 27, Nevada 17 | New Mexico 78% | New Mexico -355 / Nevada +355 | 28.7 – 17.8 | 14–43 / 7–31 | New Mexico -10.9 / – | 46.6 / – | no line yet | no line yet (fair: New Mexico -355) | no line yet |  |
| Fri 11/06 10:15 PM | TCU @ Arizona | TCU 20, Arizona 27 | Arizona 72% | TCU +255 / Arizona -255 | 20.2 – 28.8 | 7–34 / 14–43 | Arizona -8.6 / – | 49.0 / – | no line yet | no line yet (fair: Arizona -255) | no line yet |  |
| Sat 11/07 TBA | Arkansas @ Auburn | Arkansas 17, Auburn 34 | Auburn 84% | Arkansas +535 / Auburn -535 | 19.0 – 33.7 | 7–31 / 19–49 | Auburn -14.7 / – | 52.7 / – | no line yet | no line yet (fair: Auburn -535) | no line yet |  |
| Sat 11/07 TBA | Oklahoma @ Florida | Oklahoma 24, Florida 21 | Oklahoma 52% | Oklahoma -110 / Florida +110 | 23.6 – 22.9 | 10–38 / 10–37 | Oklahoma -0.7 / – | 46.5 / – | no line yet | no line yet (fair: Oklahoma -110) | no line yet |  |
| Sat 11/07 TBA | Alabama @ LSU | Alabama 24, LSU 27 | LSU 61% | Alabama +155 / LSU -155 | 24.8 – 28.8 | 11–38 / 14–44 | LSU -9.7 / LSU -3.5 | 50.0 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | Georgia @ Ole Miss | Georgia 27, Ole Miss 24 | Georgia 62% | Georgia -160 / Ole Miss +160 | 29.9 – 25.6 | 16–45 / 13–40 | Georgia -1.8 / Georgia -4.5 | 55.7 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | Vanderbilt @ Mississippi State | Vanderbilt 24, Mississippi State 31 | Mississippi State 67% | Vanderbilt +200 / Mississippi State -200 | 25.0 – 31.7 | 10–38 / 17–47 | Mississippi State -6.7 / – | 56.7 / – | no line yet | no line yet (fair: Mississippi State -200) | no line yet |  |
| Sat 11/07 TBA | Texas @ Missouri | Texas 21, Missouri 24 | Texas 51% | Texas -105 / Missouri +105 | 22.7 – 22.4 | 10–36 / 10–36 | Texas -0.3 / – | 45.0 / – | no line yet | no line yet (fair: Texas -105) | no line yet |  |
| Sat 11/07 TBA | Texas A&M @ South Carolina | Texas A&M 27, South Carolina 24 | Texas A&M 55% | Texas A&M -120 / South Carolina +120 | 25.2 – 23.5 | 13–38 / 10–38 | Texas A&M -1.7 / – | 48.7 / – | no line yet | no line yet (fair: Texas A&M -120) | no line yet |  |
| Sat 11/07 TBA | Kentucky @ Tennessee | Kentucky 17, Tennessee 27 | Tennessee 77% | Kentucky +335 / Tennessee -335 | 18.6 – 29.3 | 7–31 / 14–45 | Tennessee -10.7 / – | 47.8 / – | no line yet | no line yet (fair: Tennessee -335) | no line yet |  |
| Sat 11/07 TBA | BYU @ Utah | BYU 24, Utah 27 | Utah 59% | BYU +145 / Utah -145 | 24.3 – 27.4 | 10–38 / 14–42 | Utah -4.5 / Utah -3.0 | 52.6 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | UCF @ Kansas | UCF 24, Kansas 31 | Kansas 67% | UCF +205 / Kansas -205 | 22.6 – 29.2 | 10–36 / 15–45 | Kansas -6.6 / – | 51.7 / – | no line yet | no line yet (fair: Kansas -205) | no line yet |  |
| Sat 11/07 TBA | Cincinnati @ Houston | Cincinnati 31, Houston 34 | Houston 62% | Cincinnati +165 / Houston -165 | 28.9 – 33.8 | 14–44 / 20–49 | Houston -4.9 / – | 62.8 / – | no line yet | no line yet (fair: Houston -165) | no line yet |  |
| Sat 11/07 TBA | Colorado @ Arizona State | Colorado 24, Arizona State 27 | Arizona State 60% | Colorado +150 / Arizona State -150 | 23.2 – 27.0 | 10–37 / 14–41 | Arizona State -3.7 / – | 50.2 / – | no line yet | no line yet (fair: Arizona State -150) | no line yet |  |
| Sat 11/07 TBA | Iowa State @ Baylor | Iowa State 24, Baylor 27 | Baylor 52% | Iowa State +110 / Baylor -110 | 25.1 – 25.9 | 13–38 / 13–41 | Baylor -0.8 / – | 51.0 / – | no line yet | no line yet (fair: Baylor -110) | no line yet |  |
| Sat 11/07 TBA | Oklahoma State @ Kansas State | Oklahoma State 24, Kansas State 34 | Kansas State 74% | Oklahoma State +290 / Kansas State -290 | 24.2 – 34.1 | 10–38 / 20–49 | Kansas State -9.8 / – | 58.3 / – | no line yet | no line yet (fair: Kansas State -290) | no line yet |  |
| Sat 11/07 TBA | West Virginia @ Texas Tech | West Virginia 17, Texas Tech 38 | Texas Tech 91% | West Virginia +1070 / Texas Tech -1070 | 17.9 – 38.2 | 7–31 / 23–54 | Texas Tech -20.3 / – | 56.0 / – | no line yet | no line yet (fair: Texas Tech -1070) | no line yet |  |
| Sat 11/07 TBA | Clemson @ Syracuse | Clemson 24, Syracuse 21 | Clemson 53% | Clemson -115 / Syracuse +115 | 24.9 – 23.6 | 13–38 / 10–38 | Clemson -1.3 / – | 48.5 / – | no line yet | no line yet (fair: Clemson -115) | no line yet |  |
| Sat 11/07 TBA | Duke @ NC State | Duke 31, NC State 28 | Duke 54% | Duke -115 / NC State +115 | 29.6 – 28.6 | 16–45 / 14–43 | Duke -1.0 / – | 58.2 / – | no line yet | no line yet (fair: Duke -115) | no line yet |  |
| Sat 11/07 TBA | Louisville @ Georgia Tech | Louisville 38, Georgia Tech 21 | Louisville 87% | Louisville -660 / Georgia Tech +660 | 37.4 – 20.7 | 22–53 / 7–34 | Louisville -16.7 / – | 58.1 / – | no line yet | no line yet (fair: Louisville -660) | no line yet |  |
| Sat 11/07 TBA | Florida State @ Boston College | Florida State 31, Boston College 24 | Florida State 71% | Florida State -240 / Boston College +240 | 31.2 – 23.3 | 17–46 / 10–37 | Florida State -7.9 / – | 54.5 / – | no line yet | no line yet (fair: Florida State -240) | no line yet |  |
| Sat 11/07 TBA | Merrimack @ Wake Forest | Merrimack 3, Wake Forest 59 | Wake Forest 100% | Merrimack +9900 / Wake Forest -9900 | 3.0 – 58.5 | 0–7 / 44–73 | Wake Forest -55.5 / – | 61.5 / – | no line yet | no line yet (fair: Wake Forest -9900) | no line yet | FCS opponent |
| Sat 11/07 TBA | Michigan State @ Michigan | Michigan State 14, Michigan 31 | Michigan 88% | Michigan State +765 / Michigan -765 | 16.1 – 32.9 | 6–28 / 17–48 | Michigan -19.6 / Michigan -16.5 | 43.0 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | UCLA @ Minnesota | UCLA 27, Minnesota 17 | UCLA 75% | UCLA -305 / Minnesota +305 | 27.0 – 17.1 | 13–41 / 6–30 | UCLA -9.9 / – | 44.1 / – | no line yet | no line yet (fair: UCLA -305) | no line yet |  |
| Sat 11/07 TBA | Iowa @ Northwestern | Iowa 24, Northwestern 27 | Northwestern 56% | Iowa +130 / Northwestern -130 | 23.8 – 26.2 | 10–38 / 13–40 | Northwestern -2.4 / – | 49.9 / – | no line yet | no line yet (fair: Northwestern -130) | no line yet |  |
| Sat 11/07 TBA | Oregon @ Ohio State | Oregon 24, Ohio State 31 | Ohio State 67% | Oregon +205 / Ohio State -205 | 22.5 – 29.2 | 10–37 / 14–44 | Ohio State -13.7 / Ohio State -6.0 | 48.2 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | Maryland @ Purdue | Maryland 24, Purdue 27 | Purdue 56% | Maryland +125 / Purdue -125 | 25.3 – 27.5 | 13–39 / 14–42 | Purdue -2.2 / – | 52.9 / – | no line yet | no line yet (fair: Purdue -125) | no line yet |  |
| Sat 11/07 TBA | Penn State @ Washington | Penn State 24, Washington 21 | Penn State 52% | Penn State -110 / Washington +110 | 23.6 – 23.0 | 10–37 / 10–37 | Penn State -0.6 / – | 46.5 / – | no line yet | no line yet (fair: Penn State -110) | no line yet |  |
| Sat 11/07 TBA | Rutgers @ Wisconsin | Rutgers 17, Wisconsin 31 | Wisconsin 84% | Rutgers +515 / Wisconsin -515 | 18.2 – 32.6 | 7–31 / 17–48 | Wisconsin -14.3 / – | 50.8 / – | no line yet | no line yet (fair: Wisconsin -515) | no line yet |  |
| Sat 11/07 TBA | Charlotte @ UAB | Charlotte 17, UAB 31 | UAB 84% | Charlotte +515 / UAB -515 | 17.8 – 32.1 | 7–31 / 17–48 | UAB -14.3 / – | 49.9 / – | no line yet | no line yet (fair: UAB -515) | no line yet |  |
| Sat 11/07 TBA | Rice @ North Texas | Rice 20, North Texas 41 | North Texas 91% | Rice +1005 / North Texas -1005 | 21.0 – 40.8 | 7–34 / 26–57 | North Texas -19.8 / – | 61.8 / – | no line yet | no line yet (fair: North Texas -1005) | no line yet |  |
| Sat 11/07 TBA | Tulsa @ Tulane | Tulsa 24, Tulane 27 | Tulane 59% | Tulsa +145 / Tulane -145 | 23.9 – 27.1 | 10–38 / 13–41 | Tulane -3.2 / – | 51.0 / – | no line yet | no line yet (fair: Tulane -145) | no line yet |  |
| Sat 11/07 TBA | Hawai'i @ UTEP | Hawai'i 31, UTEP 17 | Hawai'i 81% | Hawai'i -420 / UTEP +420 | 30.9 – 18.6 | 17–45 / 7–31 | Hawai'i -12.4 / – | 49.5 / – | no line yet | no line yet (fair: Hawai'i -420) | no line yet |  |
| Sat 11/07 TBA | Northern Illinois @ San José State | Northern Illinois 24, San José State 31 | San José State 69% | Northern Illinois +225 / San José State -225 | 23.2 – 30.9 | 10–37 / 17–45 | San José State -7.7 / – | 54.1 / – | no line yet | no line yet (fair: San José State -225) | no line yet |  |
| Sat 11/07 TBA | Georgia State @ App State | Georgia State 28, App State 31 | App State 57% | Georgia State +130 / App State -130 | 28.0 – 30.9 | 14–42 / 17–45 | App State -3.0 / – | 58.9 / – | no line yet | no line yet (fair: App State -130) | no line yet |  |
| Sat 11/07 TBA | Old Dominion @ Coastal Carolina | Old Dominion 21, Coastal Carolina 24 | Coastal Carolina 58% | Old Dominion +140 / Coastal Carolina -140 | 20.7 – 23.7 | 7–34 / 10–37 | Coastal Carolina -3.0 / – | 44.4 / – | no line yet | no line yet (fair: Coastal Carolina -140) | no line yet |  |
| Sat 11/07 TBA | Marshall @ Georgia Southern | Marshall 31, Georgia Southern 28 | Marshall 54% | Marshall -115 / Georgia Southern +115 | 29.6 – 28.2 | 14–44 / 14–42 | Marshall -1.4 / – | 57.7 / – | no line yet | no line yet (fair: Marshall -115) | no line yet |  |
| Sat 11/07 TBA | South Alabama @ Louisiana | South Alabama 28, Louisiana 31 | Louisiana 63% | South Alabama +170 / Louisiana -170 | 26.6 – 31.8 | 13–41 / 17–47 | Louisiana -5.2 / – | 58.3 / – | no line yet | no line yet (fair: Louisiana -170) | no line yet |  |
| Sat 11/07 TBA | Louisiana Tech @ Troy | Louisiana Tech 27, Troy 24 | Louisiana Tech 58% | Louisiana Tech -140 / Troy +140 | 25.9 – 23.0 | 13–40 / 10–37 | Louisiana Tech -3.0 / – | 48.9 / – | no line yet | no line yet (fair: Louisiana Tech -140) | no line yet |  |
| Sat 11/07 12:00 PM | North Carolina @ UConn | North Carolina 27, UConn 24 | North Carolina 52% | North Carolina -110 / UConn +110 | 28.2 – 27.4 | 14–42 / 14–42 | North Carolina -0.8 / – | 55.7 / – | no line yet | no line yet (fair: North Carolina -110) | no line yet |  |
| Sat 11/07 3:00 PM | UL Monroe @ Arkansas State | UL Monroe 20, Arkansas State 34 | Arkansas State 81% | UL Monroe +435 / Arkansas State -435 | 20.4 – 33.7 | 7–34 / 20–49 | Arkansas State -13.3 / – | 54.1 / – | no line yet | no line yet (fair: Arkansas State -435) | no line yet |  |
| Sat 11/07 3:00 PM | Delaware @ Kennesaw State | Delaware 31, Kennesaw State 24 | Delaware 63% | Delaware -175 / Kennesaw State +175 | 29.9 – 25.1 | 16–45 / 13–38 | Delaware -4.8 / – | 55.0 / – | no line yet | no line yet (fair: Delaware -175) | no line yet |  |
| Sat 11/07 3:30 PM | Temple @ Navy | Temple 24, Navy 31 | Navy 73% | Temple +265 / Navy -265 | 23.3 – 32.6 | 10–37 / 17–48 | Navy -9.3 / – | 55.8 / – | no line yet | no line yet (fair: Navy -265) | no line yet |  |
| Sat 11/07 3:30 PM | Western Kentucky @ Middle Tennessee | Western Kentucky 27, Middle Tennessee 24 | Western Kentucky 55% | Western Kentucky -120 / Middle Tennessee +120 | 26.0 – 24.0 | 13–41 / 10–38 | Western Kentucky -2.0 / – | 50.1 / – | no line yet | no line yet (fair: Western Kentucky -120) | no line yet |  |
| Sat 11/07 4:00 PM | Missouri State @ Florida International | Missouri State 24, Florida International 27 | Florida International 61% | Missouri State +155 / Florida International -155 | 23.8 – 27.8 | 10–38 / 14–42 | Florida International -4.0 / – | 51.7 / – | no line yet | no line yet (fair: Florida International -155) | no line yet |  |
| Sat 11/07 5:00 PM | Liberty @ New Mexico State | Liberty 31, New Mexico State 17 | Liberty 80% | Liberty -410 / New Mexico State +410 | 30.1 – 18.1 | 16–45 / 7–31 | Liberty -12.1 / – | 48.2 / – | no line yet | no line yet (fair: Liberty -410) | no line yet |  |
| Sat 11/07 6:00 PM | Boise State @ Colorado State | Boise State 38, Colorado State 24 | Boise State 85% | Boise State -545 / Colorado State +545 | 38.0 – 22.5 | 23–54 / 10–36 | Boise State -15.5 / – | 60.5 / – | no line yet | no line yet (fair: Boise State -545) | no line yet |  |
| Sat 11/07 7:00 PM | Sam Houston @ Jacksonville State | Sam Houston 14, Jacksonville State 31 | Jacksonville State 86% | Sam Houston +610 / Jacksonville State -610 | 15.9 – 31.0 | 6–28 / 17–46 | Jacksonville State -15.1 / – | 46.9 / – | no line yet | no line yet (fair: Jacksonville State -610) | no line yet |  |
| Sat 11/07 7:30 PM | Miami @ Notre Dame | Miami 24, Notre Dame 31 | Notre Dame 67% | Miami +205 / Notre Dame -205 | 23.8 – 30.1 | 10–38 / 16–45 | Notre Dame -4.5 / Notre Dame -6.5 | 51.6 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Air Force @ Army | Air Force 27, Army 34 | Army 66% | Air Force +195 / Army -195 | 26.7 – 33.0 | 13–41 / 18–48 | Army -6.3 / – | 59.7 / – | no line yet | no line yet (fair: Army -195) | no line yet |  |
| Sat 11/07 9:30 PM | Fresno State @ Utah State | Fresno State 27, Utah State 20 | Fresno State 66% | Fresno State -190 / Utah State +190 | 26.7 – 20.9 | 13–41 / 9–34 | Fresno State -5.8 / – | 47.6 / – | no line yet | no line yet (fair: Fresno State -190) | no line yet |  |
| Sat 11/07 10:30 PM | Texas State @ Oregon State | Texas State 31, Oregon State 38 | Oregon State 66% | Texas State +190 / Oregon State -190 | 31.5 – 37.5 | 17–45 / 23–52 | Oregon State -6.0 / – | 69.0 / – | no line yet | no line yet (fair: Oregon State -190) | no line yet |  |
| Sat 11/07 10:30 PM | Wyoming @ UNLV | Wyoming 21, UNLV 28 | UNLV 73% | Wyoming +270 / UNLV -270 | 20.2 – 29.0 | 7–34 / 14–44 | UNLV -8.8 / – | 49.2 / – | no line yet | no line yet (fair: UNLV -270) | no line yet |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 542 | 11.61 | 12.21 | 8.42 | 81.0% | 0.133 | 82.5% |
| Model only (before blending) | 542 | 12.36 | 12.51 | 8.69 | 78.8% | – | – |
| Betting line when predicted | 540 | 11.60 | 12.17 | 8.41 | 80.9% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin of an FBS game by about 12.5 points.

501 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 1 | 0-1-0 | 0.4 | -0.45 | -100.0% | +6.9% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Every edge logged before kickoff at the stake and price logged with it (backfilled games, and edges logged before edges were priced from the final prediction, are not included). Units are 1% of the bankroll; ROI is units won per unit staked, pushes returning the stake, and expected ROI is what the edges' EVs promised.

### Week 8 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| Middle Tennessee @ Florida International | 17–24 | 26–23 | 25% | yes |
| Missouri State @ Delaware | 24–27 | 38–61 | 58% | no |
| South Alabama @ Marshall | 34–31 | 13–20 | 45% | no |
| New Mexico State @ Sam Houston | 24–21 | 30–24 | 58% | yes |
| James Madison @ App State | 34–24 | 31–34 | 21% | yes |
| Liberty @ Kennesaw State | 31–24 | 34–6 | 73% | no |
| East Carolina @ Memphis | 24–31 | 34–41 | 75% | yes |
| Duke @ Virginia | 21–24 | 19–16 | 45% | yes |
| Massachusetts @ UConn | 17–34 | 16–35 | 82% | yes |
| Army @ Tulsa | 24–27 | 38–35 | 45% | yes |
| Air Force @ Wyoming | 27–20 | 14–28 | 33% | yes |
| NC State @ Stanford | 31–24 | 28–31 | 30% | yes |
| LSU @ Auburn | 31–24 | 38–17 | 69% | yes |
| Texas Tech @ Cincinnati | 34–24 | 24–37 | 22% | no |
| West Virginia @ TCU | 24–34 | 24–20 | 25% | yes |
| California @ SMU | 17–38 | 20–59 | 90% | no |
| Pittsburgh @ Miami | 14–35 | 23–52 | 92% | no |
| Indiana @ Michigan | 24–17 | 13–6 | 70% | no |
| Rutgers @ Northwestern | 21–38 | 14–42 | 85% | yes |
| Rice @ Florida Atlantic | 24–31 | 49–51 | 73% | no |
| Western Michigan @ Toledo | 24–27 | 38–45 | 59% | no |
| Baylor @ Kansas | 24–27 | 24–25 | 54% | yes |
| Akron @ Kent State | 21–24 | 20–35 | 58% | yes |
| Miami (OH) @ Central Michigan | 20–17 | 28–27 | 60% | yes |
| Oregon @ Illinois | 31–21 | 10–21 | 24% | no |
| Oklahoma @ Mississippi State | 24–21 | 23–15 | 55% | yes |
| Boston College @ Georgia Tech | 24–31 | 49–27 | 32% | no |
| Iowa @ Minnesota | 24–17 | 10–13 | 29% | yes |
| North Texas @ Navy | 31–28 | 49–39 | 58% | no |
| Hawai'i @ Northern Illinois | 27–24 | 56–21 | 58% | no |
| Sacramento State @ Ball State | 17–31 | 17–34 | 82% | yes |
| Bowling Green @ Buffalo | 21–24 | 24–31 | 59% | yes |

## FBS power ratings

Points per game better than an average FBS team on a neutral field, from opponent-adjusted EPA (garbage time removed) with this season's games weighted against a preseason prior, plus the weight the margin model puts on Elo (a rating built from game results alone). Defense is positive when it holds opponents below average.

| # | Team | Conference | Net | Offense | Defense | Special teams | Results (Elo) | Elo rating |
|---|---|---|---|---|---|---|---|---|
| 1 | Ohio State | Big Ten | +26.9 | +10.8 | +10.5 | +0.4 | +5.2 | 1934 |
| 2 | LSU | SEC | +26.3 | +10.4 | +12.8 | +0.2 | +3.0 | 1751 |
| 3 | Miami | ACC | +24.4 | +12.9 | +6.6 | +0.2 | +4.6 | 1890 |
| 4 | Notre Dame | FBS Independents | +24.1 | +8.5 | +10.2 | +1.2 | +4.2 | 1849 |
| 5 | Georgia | SEC | +23.3 | +9.4 | +8.6 | +0.9 | +4.4 | 1866 |
| 6 | Indiana | Big Ten | +22.2 | +6.1 | +10.5 | +0.5 | +5.2 | 1935 |
| 7 | Ole Miss | SEC | +19.2 | +11.0 | +3.5 | +0.7 | +4.0 | 1834 |
| 8 | Alabama | SEC | +18.9 | +8.2 | +7.3 | +0.3 | +3.1 | 1760 |
| 9 | Texas | SEC | +18.0 | +3.5 | +10.9 | +0.5 | +3.2 | 1770 |
| 10 | Utah | Big 12 | +17.8 | +8.6 | +5.4 | +0.2 | +3.6 | 1801 |
| 11 | Texas Tech | Big 12 | +17.5 | +1.2 | +12.5 | +1.0 | +2.7 | 1733 |
| 12 | Oklahoma | SEC | +17.3 | +1.1 | +13.6 | +0.6 | +2.1 | 1677 |
| 13 | Tennessee | SEC | +16.0 | +3.2 | +9.1 | +0.7 | +3.0 | 1753 |
| 14 | UCLA | Big Ten | +15.9 | +6.3 | +7.2 | +0.6 | +1.8 | 1657 |
| 15 | Oregon | Big Ten | +15.7 | +2.9 | +9.9 | +0.4 | +2.6 | 1722 |
| 16 | BYU | Big 12 | +15.5 | +6.0 | +5.4 | +0.4 | +3.7 | 1814 |
| 17 | Missouri | SEC | +15.3 | +3.9 | +8.8 | +0.5 | +2.2 | 1686 |
| 18 | Louisville | ACC | +15.0 | +8.6 | +4.2 | +0.3 | +1.9 | 1663 |
| 19 | Wake Forest | ACC | +14.9 | +5.5 | +7.0 | +0.1 | +2.2 | 1688 |
| 20 | USC | Big Ten | +14.6 | +12.1 | -0.6 | +0.3 | +2.7 | 1734 |
| 21 | Michigan | Big Ten | +14.4 | +2.4 | +9.9 | +0.2 | +1.9 | 1661 |
| 22 | Nebraska | Big Ten | +14.0 | +4.7 | +7.4 | +0.6 | +1.4 | 1622 |
| 23 | Florida | SEC | +13.8 | +8.7 | +3.2 | +1.0 | +1.0 | 1592 |
| 24 | SMU | ACC | +13.1 | +6.7 | +3.9 | -0.0 | +2.5 | 1716 |
| 25 | Kansas State | Big 12 | +12.4 | +7.9 | +3.2 | +0.3 | +1.1 | 1599 |
| 26 | Texas A&M | SEC | +12.3 | +2.2 | +8.2 | +0.5 | +1.3 | 1618 |
| 27 | Auburn | SEC | +12.2 | +4.7 | +6.3 | +0.7 | +0.5 | 1550 |
| 28 | Iowa | Big Ten | +12.0 | +2.2 | +6.2 | +1.0 | +2.6 | 1723 |
| 29 | Northwestern | Big Ten | +11.9 | +6.1 | +3.0 | +1.0 | +1.8 | 1655 |
| 30 | Arizona | Big 12 | +11.5 | +5.4 | +3.7 | -0.0 | +2.5 | 1710 |
| 31 | Houston | Big 12 | +11.0 | +8.6 | +0.2 | +0.0 | +2.2 | 1690 |
| 32 | Penn State | Big Ten | +10.8 | +2.6 | +6.7 | +0.4 | +1.0 | 1593 |
| 33 | Mississippi State | SEC | +9.6 | +6.6 | +2.5 | +0.4 | +0.2 | 1523 |
| 34 | Wisconsin | Big Ten | +8.4 | +0.8 | +6.8 | +0.2 | +0.6 | 1559 |
| 35 | Kansas | Big 12 | +8.3 | +5.4 | +3.5 | +0.0 | -0.7 | 1454 |
| 36 | Kentucky | SEC | +8.3 | +1.8 | +4.6 | +0.2 | +1.8 | 1653 |
| 37 | Washington | Big Ten | +8.2 | +2.3 | +4.4 | -0.0 | +1.5 | 1635 |
| 38 | Cincinnati | Big 12 | +8.1 | +8.8 | -2.1 | +0.5 | +1.0 | 1592 |
| 39 | Iowa State | Big 12 | +7.9 | +2.9 | +3.2 | +0.9 | +0.8 | 1578 |
| 40 | South Carolina | SEC | +7.9 | +3.7 | +2.6 | +0.8 | +0.7 | 1569 |
| 41 | Florida State | ACC | +6.2 | +7.9 | -1.4 | -0.1 | -0.1 | 1497 |
| 42 | Baylor | Big 12 | +6.1 | -1.6 | +6.0 | +1.2 | +0.5 | 1546 |
| 43 | Boise State | Pac-12 | +5.4 | +4.0 | -1.1 | +0.2 | +2.4 | 1702 |
| 44 | Vanderbilt | SEC | +5.3 | +4.0 | +0.4 | +0.4 | +0.5 | 1553 |
| 45 | Duke | ACC | +5.1 | +2.0 | +0.6 | +0.7 | +1.8 | 1653 |
| 46 | Oklahoma State | Big 12 | +4.9 | +5.1 | -0.2 | +0.4 | -0.5 | 1464 |
| 47 | TCU | Big 12 | +4.9 | -1.7 | +5.4 | +0.4 | +0.8 | 1572 |
| 48 | Virginia Tech | ACC | +4.4 | +3.4 | +0.4 | +0.3 | +0.3 | 1531 |
| 49 | Clemson | ACC | +4.2 | -4.2 | +6.7 | +0.4 | +1.3 | 1613 |
| 50 | North Texas | American Athletic | +4.2 | +9.9 | -6.6 | -0.7 | +1.5 | 1634 |
| 51 | UCF | Big 12 | +4.1 | +0.8 | +4.1 | +0.0 | -0.7 | 1448 |
| 52 | James Madison | Sun Belt | +3.8 | -0.2 | +0.7 | +0.4 | +2.9 | 1747 |
| 53 | Minnesota | Big Ten | +3.6 | -2.4 | +4.9 | +0.5 | +0.7 | 1565 |
| 54 | Illinois | Big Ten | +3.6 | +5.4 | -3.2 | +0.3 | +1.1 | 1601 |
| 55 | Arizona State | Big 12 | +3.5 | +1.1 | +1.9 | +0.3 | +0.2 | 1521 |
| 56 | Colorado | Big 12 | +3.2 | -0.4 | +5.9 | -0.7 | -1.6 | 1377 |
| 57 | Pittsburgh | ACC | +3.1 | -0.5 | +2.6 | +0.6 | +0.4 | 1542 |
| 58 | NC State | ACC | +3.0 | +7.2 | -3.7 | -0.6 | +0.1 | 1515 |
| 59 | Oregon State | Pac-12 | +2.9 | +5.3 | -2.3 | +0.0 | -0.1 | 1498 |
| 60 | Virginia | ACC | +2.3 | -1.2 | +3.5 | -0.2 | +0.1 | 1517 |
| 61 | North Carolina | ACC | +1.5 | +0.8 | -0.3 | +0.6 | +0.3 | 1532 |
| 62 | Maryland | Big Ten | +1.2 | -0.7 | +3.4 | +0.6 | -2.0 | 1343 |
| 63 | Syracuse | ACC | +1.2 | +0.9 | +2.6 | -0.3 | -2.0 | 1347 |
| 64 | Memphis | American Athletic | +1.2 | +3.0 | -2.0 | -0.5 | +0.7 | 1566 |
| 65 | Purdue | Big Ten | +1.1 | +3.1 | -1.8 | +0.5 | -0.8 | 1444 |
| 66 | UTSA | American Athletic | +1.1 | +2.6 | -3.0 | -0.2 | +1.6 | 1636 |
| 67 | Arkansas | SEC | +0.9 | +1.0 | +0.4 | -0.4 | -0.2 | 1496 |
| 68 | Texas State | Pac-12 | +0.8 | +7.3 | -5.6 | -1.5 | +0.6 | 1559 |
| 69 | Toledo | Mid-American | +0.3 | -1.3 | +0.8 | +0.3 | +0.6 | 1555 |
| 70 | West Virginia | Big 12 | +0.0 | +4.0 | -4.6 | +0.6 | -0.1 | 1502 |
| 71 | New Mexico | Mountain West | -0.2 | -2.1 | +0.7 | +0.1 | +1.1 | 1598 |
| 72 | Liberty | Conference USA | -1.0 | -0.5 | -0.7 | -0.1 | +0.2 | 1527 |
| 73 | North Dakota State | Mountain West | -1.3 | -4.8 | +3.4 | +1.1 | -1.1 | 1419 |
| 74 | South Florida | American Athletic | -1.6 | -1.4 | -0.9 | -0.1 | +0.8 | 1572 |
| 75 | UConn | FBS Independents | -2.3 | +1.3 | -3.3 | -0.3 | -0.0 | 1507 |
| 76 | Army | American Athletic | -2.4 | +4.7 | -8.0 | -0.2 | +1.1 | 1602 |
| 77 | Navy | American Athletic | -2.5 | +2.1 | -3.5 | -0.7 | -0.3 | 1481 |
| 78 | Michigan State | Big Ten | -2.8 | -2.2 | +0.5 | +0.2 | -1.3 | 1399 |
| 79 | Ohio | Mid-American | -3.1 | -0.7 | -3.7 | +0.6 | +0.8 | 1571 |
| 80 | Fresno State | Pac-12 | -3.2 | -2.5 | -1.1 | -0.0 | +0.4 | 1544 |
| 81 | Tulane | American Athletic | -3.4 | -4.6 | -0.0 | +0.0 | +1.2 | 1604 |
| 82 | Boston College | ACC | -3.4 | -3.0 | +0.5 | -0.8 | -0.2 | 1493 |
| 83 | East Carolina | American Athletic | -3.5 | -5.1 | +2.5 | -0.6 | -0.3 | 1484 |
| 84 | Tulsa | American Athletic | -3.7 | -1.0 | -0.4 | -0.4 | -1.8 | 1358 |
| 85 | Georgia Tech | ACC | -3.8 | +2.5 | -5.2 | -0.0 | -1.1 | 1416 |
| 86 | Rutgers | Big Ten | -4.0 | +2.2 | -5.5 | +0.7 | -1.3 | 1402 |
| 87 | Florida Atlantic | American Athletic | -4.4 | +3.3 | -7.2 | +0.5 | -1.0 | 1426 |
| 88 | Air Force | Mountain West | -4.8 | +2.4 | -6.2 | -0.3 | -0.7 | 1453 |
| 89 | UNLV | Mountain West | -4.8 | -3.1 | -2.0 | +0.0 | +0.4 | 1540 |
| 90 | Louisiana Tech | Sun Belt | -5.3 | -3.7 | -0.3 | -0.8 | -0.5 | 1464 |
| 91 | California | ACC | -5.6 | -0.7 | -3.0 | -0.5 | -1.4 | 1392 |
| 92 | Jacksonville State | Conference USA | -6.1 | -0.7 | -4.6 | -0.4 | -0.5 | 1465 |
| 93 | Marshall | Sun Belt | -6.6 | -2.3 | -3.6 | -0.2 | -0.6 | 1462 |
| 94 | Washington State | Pac-12 | -6.8 | -6.3 | +1.4 | -0.4 | -1.5 | 1388 |
| 95 | Western Michigan | Mid-American | -7.1 | -4.2 | -3.9 | +0.5 | +0.5 | 1552 |
| 96 | App State | Sun Belt | -7.1 | -3.0 | -3.3 | -0.2 | -0.7 | 1454 |
| 97 | San Diego State | Pac-12 | -7.7 | -7.5 | +0.2 | +0.5 | -1.0 | 1425 |
| 98 | Georgia State | Sun Belt | -7.7 | +0.2 | -6.8 | -0.1 | -1.0 | 1424 |
| 99 | Miami (OH) | Mid-American | -8.1 | -4.6 | -3.3 | +0.5 | -0.8 | 1446 |
| 100 | Louisiana | Sun Belt | -8.4 | -4.5 | -4.1 | +0.0 | +0.1 | 1520 |
| 101 | Delaware | Conference USA | -8.6 | -1.7 | -5.2 | +0.2 | -1.9 | 1352 |
| 102 | Stanford | ACC | -8.9 | -3.6 | -4.6 | -0.2 | -0.5 | 1465 |
| 103 | UAB | American Athletic | -9.4 | -5.0 | -3.3 | -0.0 | -1.0 | 1427 |
| 104 | Temple | American Athletic | -9.5 | +1.0 | -7.5 | -0.5 | -2.5 | 1303 |
| 105 | Georgia Southern | Sun Belt | -9.6 | -2.3 | -6.0 | -1.0 | -0.3 | 1481 |
| 106 | Utah State | Pac-12 | -10.2 | -8.2 | +0.7 | -1.3 | -1.4 | 1393 |
| 107 | Western Kentucky | Conference USA | -10.4 | -7.0 | -1.8 | -0.2 | -1.3 | 1399 |
| 108 | Troy | Sun Belt | -10.4 | -5.9 | -2.2 | -1.2 | -1.1 | 1416 |
| 109 | Wyoming | Mountain West | -11.0 | -6.4 | -3.2 | -0.2 | -1.2 | 1413 |
| 110 | Arkansas State | Sun Belt | -11.2 | -3.6 | -6.5 | -0.0 | -1.1 | 1416 |
| 111 | South Alabama | Sun Belt | -11.3 | +0.1 | -10.8 | +0.1 | -0.9 | 1438 |
| 112 | Hawai'i | Mountain West | -11.4 | -4.4 | -5.9 | +0.7 | -1.7 | 1365 |
| 113 | Colorado State | Pac-12 | -11.7 | +1.1 | -9.4 | -0.6 | -2.9 | 1271 |
| 114 | Old Dominion | Sun Belt | -12.3 | -12.8 | +2.7 | -1.2 | -0.9 | 1431 |
| 115 | Rice | American Athletic | -13.0 | -3.8 | -5.0 | -0.9 | -3.2 | 1246 |
| 116 | Florida International | Conference USA | -13.0 | -9.7 | -1.0 | -0.7 | -1.6 | 1377 |
| 117 | Coastal Carolina | Sun Belt | -13.4 | -5.9 | -5.8 | +0.4 | -2.2 | 1332 |
| 118 | Nevada | Mountain West | -13.7 | -8.4 | -3.1 | +0.4 | -2.6 | 1292 |
| 119 | Missouri State | Conference USA | -14.0 | -1.6 | -7.8 | -1.4 | -3.1 | 1253 |
| 120 | Central Michigan | Mid-American | -14.0 | -7.6 | -4.6 | -0.2 | -1.6 | 1375 |
| 121 | New Mexico State | Conference USA | -14.2 | -7.8 | -2.5 | -1.4 | -2.5 | 1307 |
| 122 | San José State | Mountain West | -14.2 | -7.8 | -4.3 | -0.3 | -1.9 | 1356 |
| 123 | Kennesaw State | Conference USA | -14.9 | -6.8 | -4.7 | -0.8 | -2.6 | 1295 |
| 124 | Middle Tennessee | Conference USA | -15.1 | -5.7 | -7.0 | +0.1 | -2.4 | 1309 |
| 125 | Southern Miss | Sun Belt | -15.4 | -6.6 | -4.1 | -1.5 | -3.1 | 1254 |
| 126 | Ball State | Mid-American | -16.8 | -5.8 | -7.0 | -1.0 | -3.1 | 1251 |
| 127 | Eastern Michigan | Mid-American | -17.1 | -6.8 | -7.5 | -0.8 | -2.1 | 1337 |
| 128 | Massachusetts | Mid-American | -17.4 | -9.5 | -4.2 | -0.2 | -3.5 | 1219 |
| 129 | Sam Houston | Conference USA | -17.9 | -11.6 | -0.9 | -1.3 | -4.1 | 1173 |
| 130 | Buffalo | Mid-American | -18.0 | -12.7 | -5.1 | +0.6 | -0.8 | 1444 |
| 131 | Northern Illinois | Mountain West | -18.8 | -4.6 | -8.9 | -0.9 | -4.4 | 1149 |
| 132 | Kent State | Mid-American | -19.0 | -9.2 | -6.5 | -1.0 | -2.3 | 1318 |
| 133 | Bowling Green | Mid-American | -19.0 | -11.6 | -4.5 | -0.1 | -2.8 | 1279 |
| 134 | UL Monroe | Sun Belt | -20.6 | -6.5 | -8.1 | -1.5 | -4.5 | 1139 |
| 135 | Charlotte | American Athletic | -20.9 | -8.7 | -8.2 | -0.4 | -3.6 | 1211 |
| 136 | Sacramento State | Mid-American | -22.2 | -10.3 | -6.8 | +0.2 | -5.3 | 1074 |
| 137 | Akron | Mid-American | -22.8 | -10.1 | -7.8 | -1.2 | -3.7 | 1205 |
| 138 | UTEP | Mountain West | -24.1 | -11.9 | -6.1 | -1.4 | -4.7 | 1123 |

## Current model fit

- Fitted on 4159 games from seasons 2022–2026.
- Home field on top of the ratings: 3.2 points (1.8 in conference games).
- Extra FBS edge over FCS opponents beyond their ratings: 14.0 points.
- Elo weight: 0.20 points of margin per point of Elo spread.
- Weight on the betting line: 91% for the margin, 80% for the total.
