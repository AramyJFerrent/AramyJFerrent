# College football score predictions

Updated Sat Nov 21, 2026 09:10 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 12

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sat 11/21 9:30 PM | San Diego State @ Boise State | San Diego State 20, Boise State 41 | Boise State 91% | San Diego State +955 / Boise State -955 | 20.1 – 39.9 | 7–34 / 24–56 | Boise State -13.7 / Boise State -20.5 | 56.7 / 60.8 | no edge | no edge | no edge |  |
| Sat 11/21 10:15 PM | Oklahoma State @ Arizona State | Oklahoma State 31, Arizona State 28 | Oklahoma State 55% | Oklahoma State -125 / Arizona State +125 | 30.7 – 28.5 | 17–45 / 14–43 | Arizona State -1.1 / Oklahoma State -2.5 | 57.7 / 59.5 | no edge | no edge | no edge |  |
| Sat 11/21 10:30 PM | Utah State @ Oregon State | Utah State 24, Oregon State 31 | Oregon State 69% | Utah State +220 / Oregon State -220 | 22.2 – 29.6 | 10–35 / 16–44 | Oregon State -12.1 / Oregon State -7.0 | 53.2 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/21 10:30 PM | Hawai'i @ Nevada | Hawai'i 17, Nevada 24 | Nevada 67% | Hawai'i +205 / Nevada -205 | 17.7 – 23.9 | 7–30 / 10–38 | Hawai'i -1.1 / Nevada -7.0 | 46.7 / 40.5 | no edge | no edge | no edge |  |

## 2026 Week 13

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/24 7:00 PM | Kent State @ Eastern Michigan | Kent State 20, Eastern Michigan 27 | Eastern Michigan 67% | Kent State +205 / Eastern Michigan -205 | 20.3 – 26.8 | 7–34 / 13–41 | Eastern Michigan -6.6 / Eastern Michigan -6.5 | 49.6 / 46.5 | no edge | no edge | no edge |  |
| Tue 11/24 7:00 PM | Miami (OH) @ Western Michigan | Miami (OH) 20, Western Michigan 27 | Western Michigan 69% | Miami (OH) +220 / Western Michigan -220 | 19.9 – 26.9 | 7–34 / 13–42 | Western Michigan -1.9 / Western Michigan -7.5 | 47.9 / 46.5 | no edge | no edge | no edge |  |
| Thu 11/26 8:00 PM | TCU @ Texas Tech | TCU 17, Texas Tech 28 | Texas Tech 78% | TCU +345 / Texas Tech -345 | 17.8 – 29.0 | 7–30 / 14–44 | Texas Tech -17.7 / Texas Tech -10.5 | 44.0 / 47.5 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Mississippi State @ Ole Miss | Mississippi State 17, Ole Miss 38 | Ole Miss 90% | Mississippi State +855 / Ole Miss -855 | 19.3 – 38.4 | 7–31 / 23–54 | Ole Miss -14.8 / Ole Miss -19.5 | 58.8 / 57.5 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Nebraska @ Iowa | Nebraska 17, Iowa 24 | Iowa 67% | Nebraska +200 / Iowa -200 | 16.8 – 22.8 | 6–28 / 10–36 | Iowa -5.5 / Iowa -6.0 | 44.8 / 38.5 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Tulsa @ UTSA | Tulsa 28, UTSA 31 | UTSA 60% | Tulsa +150 / UTSA -150 | 26.5 – 30.3 | 13–41 / 16–45 | UTSA -3.8 / – | 56.8 / – | no line yet | no line yet (fair: UTSA -150) | no line yet |  |
| Fri 11/27 12:00 PM | Buffalo @ Akron | Buffalo 27, Akron 20 | Buffalo 74% | Buffalo -290 / Akron +290 | 29.8 – 20.0 | 16–45 / 7–34 | Buffalo -8.1 / Buffalo -10.0 | 51.9 / 49.5 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Toledo @ Ohio | Toledo 24, Ohio 21 | Toledo 62% | Toledo -160 / Ohio +160 | 25.8 – 21.8 | 13–40 / 10–35 | Toledo -4.0 / – | 48.2 / – | no line yet | no line yet (fair: Toledo -160) | no line yet |  |
| Fri 11/27 3:00 PM | App State @ South Alabama | App State 28, South Alabama 31 | South Alabama 56% | App State +130 / South Alabama -130 | 28.2 – 31.0 | 14–42 / 17–45 | South Alabama -2.8 / – | 59.2 / – | no line yet | no line yet (fair: South Alabama -130) | no line yet |  |
| Fri 11/27 3:30 PM | Florida @ Florida State | Florida 27, Florida State 24 | Florida 61% | Florida -160 / Florida State +160 | 28.8 – 24.2 | 14–44 / 10–38 | Florida -5.8 / Florida -4.5 | 55.5 / 52.5 | no edge | no edge | no edge |  |
| Fri 11/27 3:30 PM | Temple @ Memphis | Temple 21, Memphis 38 | Memphis 88% | Temple +725 / Memphis -725 | 21.6 – 39.4 | 9–35 / 24–55 | Memphis -17.8 / – | 61.0 / – | no line yet | no line yet (fair: Memphis -725) | no line yet |  |
| Fri 11/27 3:30 PM | North Dakota State @ San José State | North Dakota State 28, San José State 14 | North Dakota State 81% | North Dakota State -430 / San José State +430 | 27.8 – 15.2 | 14–42 / 3–27 | North Dakota State -12.6 / – | 43.0 / – | no line yet | no line yet (fair: North Dakota State -430) | no line yet |  |
| Fri 11/27 4:30 PM | Air Force @ New Mexico | Air Force 24, New Mexico 27 | New Mexico 63% | Air Force +165 / New Mexico -165 | 21.9 – 26.5 | 10–35 / 13–41 | New Mexico -4.7 / – | 48.4 / – | no line yet | no line yet (fair: New Mexico -165) | no line yet |  |
| Fri 11/27 7:30 PM | Texas @ Texas A&M | Texas 24, Texas A&M 17 | Texas 72% | Texas -255 / Texas A&M +255 | 24.6 – 16.7 | 10–38 / 6–28 | Texas -12.3 / Texas -7.5 | 40.6 / 41.5 | no edge | no edge | no edge |  |
| Fri 11/27 7:30 PM | Minnesota @ Wisconsin | Minnesota 17, Wisconsin 24 | Wisconsin 73% | Minnesota +275 / Wisconsin -275 | 15.2 – 23.7 | 3–27 / 10–38 | Wisconsin -8.5 / – | 38.9 / – | no line yet | no line yet (fair: Wisconsin -275) | no line yet |  |
| Fri 11/27 9:00 PM | West Virginia @ Utah | West Virginia 20, Utah 45 | Utah 94% | West Virginia +1680 / Utah -1680 | 19.7 – 44.3 | 7–32 / 29–61 | Utah -24.5 / – | 64.0 / – | no line yet | no line yet (fair: Utah -1680) | no line yet |  |
| Sat 11/28 TBA | Auburn @ Alabama | Auburn 17, Alabama 31 | Alabama 82% | Auburn +465 / Alabama -465 | 18.5 – 32.1 | 7–31 / 17–48 | Alabama -10.0 / Alabama -14.0 | 51.2 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | LSU @ Arkansas | LSU 35, Arkansas 17 | LSU 91% | LSU -975 / Arkansas +975 | 35.6 – 16.4 | 21–51 / 6–28 | LSU -19.3 / – | 52.0 / – | no line yet | no line yet (fair: LSU -975) | no line yet |  |
| Sat 11/28 TBA | Georgia Tech @ Georgia | Georgia Tech 3, Georgia 41 | Georgia 100% | Georgia Tech +9900 / Georgia -9900 | 6.3 – 43.7 | 0–13 / 30–59 | Georgia -37.4 / – | 50.2 / – | no line yet | no line yet (fair: Georgia -9900) | no line yet |  |
| Sat 11/28 TBA | Louisville @ Kentucky | Louisville 24, Kentucky 27 | Kentucky 53% | Louisville +115 / Kentucky -115 | 26.6 – 27.5 | 13–41 / 14–42 | Louisville -5.5 / Kentucky -1.5 | 52.5 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | South Carolina @ Clemson | South Carolina 24, Clemson 27 | Clemson 57% | South Carolina +130 / Clemson -130 | 24.8 – 27.5 | 12–38 / 14–42 | South Carolina -0.5 / Clemson -3.0 | 46.9 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Tennessee @ Vanderbilt | Tennessee 27, Vanderbilt 24 | Tennessee 59% | Tennessee -145 / Vanderbilt +145 | 29.8 – 25.8 | 16–45 / 13–41 | Tennessee -13.3 / Tennessee -3.0 | 47.2 / 57.5 | no edge | no edge | Under 57.5 (-110*): EV +5.2%, 55%, stake 1.4u | * price not posted; assumed -110 |
| Sat 11/28 TBA | Duke @ Wake Forest | Duke 20, Wake Forest 34 | Wake Forest 82% | Duke +455 / Wake Forest -455 | 20.5 – 34.4 | 7–34 / 20–50 | Wake Forest -17.4 / Wake Forest -13.5 | 52.5 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | SMU @ Stanford | SMU 34, Stanford 21 | SMU 82% | SMU -470 / Stanford +470 | 35.1 – 21.4 | 20–51 / 9–35 | SMU -13.7 / – | 56.5 / – | no line yet | no line yet (fair: SMU -470) | no line yet |  |
| Sat 11/28 TBA | Purdue @ Indiana | Purdue 10, Indiana 38 | Indiana 96% | Purdue +2545 / Indiana -2545 | 12.3 – 37.5 | 3–24 / 23–54 | Indiana -25.1 / – | 49.8 / – | no line yet | no line yet (fair: Indiana -2545) | no line yet |  |
| Sat 11/28 TBA | Washington @ Oregon | Washington 17, Oregon 31 | Oregon 80% | Washington +405 / Oregon -405 | 18.0 – 30.6 | 7–31 / 17–45 | Oregon -13.5 / Oregon -12.5 | 49.0 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Boston College @ Miami | Boston College 10, Miami 45 | Miami 99% | Boston College +8060 / Miami -8060 | 11.5 – 44.1 | 3–21 / 29–61 | Miami -32.7 / – | 55.6 / – | no line yet | no line yet (fair: Miami -8060) | no line yet |  |
| Sat 11/28 12:00 PM | NC State @ North Carolina | NC State 27, North Carolina 24 | NC State 52% | NC State -110 / North Carolina +110 | 28.6 – 27.4 | 14–43 / 14–42 | North Carolina -1.7 / NC State -1.5 | 58.2 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Notre Dame @ Syracuse | Notre Dame 38, Syracuse 17 | Notre Dame 92% | Notre Dame -1110 / Syracuse +1110 | 37.3 – 16.7 | 23–52 / 6–29 | Notre Dame -20.9 / Notre Dame -20.5 | 51.5 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Michigan @ Ohio State | Michigan 14, Ohio State 28 | Ohio State 81% | Michigan +435 / Ohio State -435 | 14.8 – 27.5 | 3–27 / 13–42 | Ohio State -14.2 / Ohio State -12.5 | 45.6 / 41.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | UConn @ Wyoming | UConn 31, Wyoming 28 | UConn 60% | UConn -150 / Wyoming +150 | 30.0 – 25.7 | 16–45 / 13–40 | UConn -4.3 / – | 55.7 / – | no line yet | no line yet (fair: UConn -150) | no line yet |  |
| Sat 11/28 12:00 PM | Navy @ Charlotte | Navy 34, Charlotte 17 | Navy 89% | Navy -800 / Charlotte +800 | 35.1 – 17.1 | 20–51 / 6–30 | Navy -18.0 / – | 52.2 / – | no line yet | no line yet (fair: Navy -800) | no line yet |  |
| Sat 11/28 12:00 PM | Central Michigan @ Ball State | Central Michigan 27, Ball State 24 | Central Michigan 62% | Central Michigan -160 / Ball State +160 | 27.2 – 23.0 | 13–41 / 10–37 | Central Michigan -4.2 / – | 51.0 / – | no line yet | no line yet (fair: Central Michigan -160) | no line yet |  |
| Sat 11/28 12:00 PM | Louisiana Tech @ Georgia Southern | Louisiana Tech 24, Georgia Southern 21 | Louisiana Tech 50% | Louisiana Tech -100 / Georgia Southern +100 | 24.2 – 23.9 | 10–38 / 10–38 | Louisiana Tech -0.3 / – | 50.0 / – | no line yet | no line yet (fair: Louisiana Tech -100) | no line yet |  |
| Sat 11/28 12:30 PM | Illinois @ Northwestern | Illinois 24, Northwestern 27 | Northwestern 62% | Illinois +165 / Northwestern -165 | 22.2 – 26.9 | 10–35 / 13–41 | Northwestern -7.1 / Northwestern -4.5 | 56.5 / 47.5 | no edge | no edge | Over 47.5 (-110*): EV +4.6%, 55%, stake 1.3u | * price not posted; assumed -110 |
| Sat 11/28 1:00 PM | Florida Atlantic @ East Carolina | Florida Atlantic 28, East Carolina 31 | East Carolina 60% | Florida Atlantic +150 / East Carolina -150 | 26.6 – 30.1 | 13–41 / 16–45 | East Carolina -3.5 / – | 57.8 / – | no line yet | no line yet (fair: East Carolina -150) | no line yet |  |
| Sat 11/28 1:00 PM | Kennesaw State @ Western Kentucky | Kennesaw State 24, Western Kentucky 27 | Western Kentucky 51% | Kennesaw State +105 / Western Kentucky -105 | 26.3 – 26.9 | 13–41 / 13–41 | Western Kentucky -0.6 / – | 54.1 / – | no line yet | no line yet (fair: Western Kentucky -105) | no line yet |  |
| Sat 11/28 1:00 PM | Marshall @ UL Monroe | Marshall 31, UL Monroe 24 | Marshall 65% | Marshall -185 / UL Monroe +185 | 29.6 – 23.6 | 16–44 / 10–37 | Marshall -6.0 / – | 53.9 / – | no line yet | no line yet (fair: Marshall -185) | no line yet |  |
| Sat 11/28 1:00 PM | Southern Miss @ Old Dominion | Southern Miss 17, Old Dominion 27 | Old Dominion 72% | Southern Miss +265 / Old Dominion -265 | 18.9 – 28.1 | 7–31 / 14–43 | Old Dominion -9.1 / – | 47.0 / – | no line yet | no line yet (fair: Old Dominion -265) | no line yet |  |
| Sat 11/28 2:00 PM | UCF @ Colorado | UCF 24, Colorado 27 | Colorado 54% | UCF +115 / Colorado -115 | 25.0 – 26.6 | 13–38 / 13–41 | Colorado -1.6 / – | 51.6 / – | no line yet | no line yet (fair: Colorado -115) | no line yet |  |
| Sat 11/28 2:00 PM | Kansas State @ Iowa State | Kansas State 24, Iowa State 27 | Iowa State 55% | Kansas State +125 / Iowa State -125 | 25.5 – 27.6 | 13–40 / 14–41 | Iowa State -2.1 / – | 53.9 / – | no line yet | no line yet (fair: Iowa State -125) | no line yet |  |
| Sat 11/28 2:00 PM | Army @ Rice | Army 31, Rice 24 | Army 66% | Army -190 / Rice +190 | 31.4 – 25.5 | 17–45 / 13–40 | Army -5.9 / – | 56.9 / – | no line yet | no line yet (fair: Army -190) | no line yet |  |
| Sat 11/28 2:00 PM | Coastal Carolina @ James Madison | Coastal Carolina 17, James Madison 34 | James Madison 86% | Coastal Carolina +620 / James Madison -620 | 17.7 – 33.7 | 7–30 / 19–49 | James Madison -16.0 / – | 51.4 / – | no line yet | no line yet (fair: James Madison -620) | no line yet |  |
| Sat 11/28 2:00 PM | Louisiana @ Georgia State | Louisiana 27, Georgia State 24 | Louisiana 53% | Louisiana -115 / Georgia State +115 | 28.2 – 26.9 | 14–42 / 13–41 | Louisiana -1.3 / – | 55.6 / – | no line yet | no line yet (fair: Louisiana -115) | no line yet |  |
| Sat 11/28 2:00 PM | Liberty @ Missouri State | Liberty 34, Missouri State 17 | Liberty 87% | Liberty -695 / Missouri State +695 | 33.8 – 17.0 | 19–49 / 6–30 | Liberty -16.9 / – | 52.6 / – | no line yet | no line yet (fair: Liberty -695) | no line yet |  |
| Sat 11/28 2:00 PM | Sam Houston @ Florida International | Sam Houston 17, Florida International 24 | Florida International 72% | Sam Houston +265 / Florida International -265 | 16.2 – 24.5 | 6–28 / 10–38 | Florida International -8.4 / – | 40.7 / – | no line yet | no line yet (fair: Florida International -265) | no line yet |  |
| Sat 11/28 2:00 PM | New Mexico State @ Middle Tennessee | New Mexico State 24, Middle Tennessee 31 | Middle Tennessee 64% | New Mexico State +175 / Middle Tennessee -175 | 22.7 – 28.2 | 10–36 / 14–42 | Middle Tennessee -5.6 / – | 51.1 / – | no line yet | no line yet (fair: Middle Tennessee -175) | no line yet |  |
| Sat 11/28 3:00 PM | Virginia @ Virginia Tech | Virginia 24, Virginia Tech 27 | Virginia Tech 54% | Virginia +120 / Virginia Tech -120 | 25.9 – 27.2 | 13–40 / 14–41 | Virginia -0.4 / Virginia Tech -1.5 | 51.7 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/28 3:00 PM | Troy @ Arkansas State | Troy 21, Arkansas State 24 | Arkansas State 63% | Troy +170 / Arkansas State -170 | 21.0 – 26.0 | 8–34 / 13–41 | Arkansas State -5.0 / – | 47.3 / – | no line yet | no line yet (fair: Arkansas State -170) | no line yet |  |
| Sat 11/28 3:30 PM | Cincinnati @ BYU | Cincinnati 24, BYU 34 | BYU 77% | Cincinnati +330 / BYU -330 | 23.2 – 34.4 | 10–37 / 20–50 | BYU -11.2 / – | 57.7 / – | no line yet | no line yet (fair: BYU -330) | no line yet |  |
| Sat 11/28 3:30 PM | Penn State @ Maryland | Penn State 24, Maryland 21 | Penn State 66% | Penn State -195 / Maryland +195 | 26.0 – 20.1 | 13–41 / 7–34 | Penn State -5.9 / – | 46.2 / – | no line yet | no line yet (fair: Penn State -195) | no line yet |  |
| Sat 11/28 3:30 PM | USC @ UCLA | USC 24, UCLA 27 | UCLA 58% | USC +135 / UCLA -135 | 24.7 – 27.7 | 12–38 / 14–42 | UCLA -7.2 / UCLA -2.5 | 52.0 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/28 3:30 PM | Tulane @ South Florida | Tulane 21, South Florida 28 | South Florida 66% | Tulane +195 / South Florida -195 | 22.3 – 28.5 | 10–35 / 14–42 | South Florida -6.2 / – | 51.2 / – | no line yet | no line yet (fair: South Florida -195) | no line yet |  |
| Sat 11/28 3:30 PM | UTEP @ Northern Illinois | UTEP 21, Northern Illinois 31 | Northern Illinois 75% | UTEP +300 / Northern Illinois -300 | 20.5 – 30.3 | 7–34 / 16–45 | Northern Illinois -9.8 / – | 50.7 / – | no line yet | no line yet (fair: Northern Illinois -300) | no line yet |  |
| Sat 11/28 3:30 PM | Massachusetts @ Bowling Green | Massachusetts 17, Bowling Green 20 | Bowling Green 61% | Massachusetts +155 / Bowling Green -155 | 17.9 – 21.8 | 7–31 / 10–35 | Bowling Green -3.9 / – | 39.7 / – | no line yet | no line yet (fair: Bowling Green -155) | no line yet |  |
| Sat 11/28 3:30 PM | Jacksonville State @ Delaware | Jacksonville State 28, Delaware 31 | Delaware 55% | Jacksonville State +120 / Delaware -120 | 27.7 – 29.7 | 14–42 / 15–45 | Delaware -2.0 / – | 57.7 / – | no line yet | no line yet (fair: Delaware -120) | no line yet |  |
| Sat 11/28 4:00 PM | UAB @ North Texas | UAB 24, North Texas 31 | North Texas 74% | UAB +285 / North Texas -285 | 24.0 – 34.1 | 10–38 / 20–49 | North Texas -10.0 / – | 58.1 / – | no line yet | no line yet (fair: North Texas -285) | no line yet |  |
| Sat 11/28 4:15 PM | Oklahoma @ Missouri | Oklahoma 21, Missouri 24 | Missouri 53% | Oklahoma +115 / Missouri -115 | 20.7 – 21.7 | 7–34 / 10–35 | Oklahoma -3.7 / Missouri -1.5 | 42.2 / 42.5 | no edge | no edge | no edge |  |
| Sat 11/28 4:15 PM | Michigan State @ Rutgers | Michigan State 24, Rutgers 27 | Rutgers 51% | Michigan State +105 / Rutgers -105 | 25.4 – 25.6 | 13–39 / 13–39 | Rutgers -0.2 / – | 51.1 / – | no line yet | no line yet (fair: Rutgers -105) | no line yet |  |
| Sat 11/28 6:15 PM | Kansas @ Oklahoma State | Kansas 28, Oklahoma State 31 | Oklahoma State 55% | Kansas +125 / Oklahoma State -125 | 28.5 – 30.8 | 14–43 / 17–45 | Oklahoma State -2.3 / – | 59.3 / – | no line yet | no line yet (fair: Oklahoma State -125) | no line yet |  |
| Sat 11/28 7:30 PM | Pittsburgh @ California | Pittsburgh 28, California 21 | Pittsburgh 72% | Pittsburgh -255 / California +255 | 29.4 – 20.7 | 15–44 / 7–34 | Pittsburgh -8.7 / – | 50.0 / – | no line yet | no line yet (fair: Pittsburgh -255) | no line yet |  |
| Sat 11/28 9:00 PM | Arizona State @ Arizona | Arizona State 24, Arizona 27 | Arizona 62% | Arizona State +165 / Arizona -165 | 24.0 – 28.7 | 10–38 / 14–43 | Arizona -6.1 / Arizona -4.5 | 53.8 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/28 9:00 PM | Nevada @ UNLV | Nevada 17, UNLV 27 | UNLV 78% | Nevada +360 / UNLV -360 | 17.8 – 29.0 | 7–31 / 14–44 | UNLV -11.3 / – | 46.8 / – | no line yet | no line yet (fair: UNLV -360) | no line yet |  |
| Sat 11/28 9:30 PM | Baylor @ Houston | Baylor 28, Houston 31 | Houston 54% | Baylor +115 / Houston -115 | 27.8 – 29.4 | 14–42 / 16–44 | Houston -1.6 / – | 57.2 / – | no line yet | no line yet (fair: Houston -115) | no line yet |  |
| Sat 11/28 11:00 PM | Sacramento State @ Hawai'i | Sacramento State 17, Hawai'i 31 | Hawai'i 84% | Sacramento State +515 / Hawai'i -515 | 17.2 – 31.4 | 6–30 / 17–46 | Hawai'i -14.3 / – | 48.6 / – | no line yet | no line yet (fair: Hawai'i -515) | no line yet |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 803 | 11.83 | 12.21 | 8.51 | 77.7% | 0.151 | 81.7% |
| Model only (before blending) | 803 | 12.47 | 12.57 | 8.76 | 75.7% | – | – |
| Betting line when predicted | 801 | 11.82 | 12.16 | 8.50 | 77.8% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin of an FBS game by about 12.5 points.

501 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 11 | 2-9-0 | 3.5 | +0.18 | +5.2% | +4.7% |
| Total | 10 | 5-5-0 | 13.6 | -1.01 | -7.4% | +6.9% |

10 of these edges were priced at an assumed -110 (price not posted).

Every edge logged before kickoff at the stake and price logged with it (backfilled games, and edges logged before edges were priced from the final prediction, are not included). Units are 1% of the bankroll; ROI is units won per unit staked, pushes returning the stake, and expected ROI is what the edges' EVs promised.

### Week 12 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| Eastern Michigan @ Western Michigan | 14–31 | 27–34 | 87% | yes |
| Ball State @ Ohio | 21–31 | 28–35 | 76% | yes |
| Miami (OH) @ Kent State | 24–17 | 20–3 | 75% | no |
| Akron @ Massachusetts | 21–24 | 34–33 | 40% | yes |
| Central Michigan @ Buffalo | 21–24 | 21–40 | 56% | no |
| Rice @ Temple | 24–27 | 31–27 | 43% | yes |
| Iowa State @ UCF | 27–24 | 17–48 | 46% | no |
| Clemson @ Duke | 17–24 | 20–10 | 21% | no |
| Bowling Green @ Toledo | 14–31 | 0–19 | 88% | no |
| Oregon @ Michigan State | 31–14 | 45–7 | 90% | yes |
| UTEP @ Air Force | 13–34 | 3–52 | 95% | yes |
| New Mexico @ Wyoming | 24–17 | 24–17 | 75% | yes |
| Vanderbilt @ Florida | 17–31 | 27–34 | 82% | yes |
| Wofford @ Ole Miss | 3–55 | 17–59 | 100% | no |
| BYU @ Kansas | 24–21 | 31–29 | 62% | yes |
| Colorado @ Cincinnati | 28–31 | 28–35 | 58% | yes |
| Syracuse @ Boston College | 27–24 | 15–27 | 41% | yes |
| Wake Forest @ Georgia Tech | 38–17 | 50–29 | 92% | yes |
| Northwestern @ Minnesota | 24–21 | 17–20 | 43% | yes |
| Ohio State @ Nebraska | 24–21 | 28–31 | 39% | yes |
| Wisconsin @ Purdue | 24–21 | 42–10 | 66% | no |
| East Carolina @ Army | 21–24 | 10–6 | 35% | no |
| Memphis @ Navy | 34–31 | 34–38 | 43% | yes |
| North Texas @ Tulane | 31–24 | 24–28 | 34% | yes |
| North Carolina @ Virginia | 21–24 | 24–41 | 55% | no |
| Tennessee Tech @ Mississippi State | 10–45 | 16–34 | 99% | yes |
| Houston @ West Virginia | 38–31 | 34–31 | 68% | yes |
| Western Kentucky @ Liberty | 17–34 | 14–45 | 88% | yes |
| Chattanooga @ Alabama | 3–52 | 0–47 | 100% | yes |
| Charlotte @ Tulsa | 14–38 | 14–42 | 95% | yes |
| Missouri State @ Jacksonville State | 21–31 | 20–25 | 77% | yes |
| Middle Tennessee @ Sam Houston | 27–24 | 31–28 | 66% | yes |
| Iowa @ Illinois | 24–17 | 34–17 | 74% | yes |
| UL Monroe @ App State | 17–31 | 16–17 | 82% | yes |
| Coastal Carolina @ Louisiana | 21–31 | 24–38 | 75% | yes |
| Delaware @ New Mexico State | 27–24 | 42–30 | 59% | yes |
| Florida International @ Kennesaw State | 21–24 | 24–35 | 58% | yes |
| Samford @ Auburn | 3–52 | 17–59 | 100% | no |
| LSU @ Tennessee | 24–21 | 13–27 | 47% | yes |
| Arkansas @ Texas | 14–31 | 3–45 | 91% | yes |
| Texas Tech @ Baylor | 31–24 | 20–10 | 64% | no |
| NC State @ Florida State | 24–34 | 28–10 | 26% | no |
| UCLA @ Michigan | 20–17 | 16–18 | 40% | yes |
| Rutgers @ Penn State | 10–38 | 25–24 | 4% | no |
| Indiana @ Washington | 24–17 | 24–27 | 26% | yes |
| Old Dominion @ UConn | 17–31 | 21–29 | 84% | yes |
| Texas A&M @ Oklahoma | 17–24 | 7–28 | 70% | yes |
| Northern Illinois @ North Dakota State | 10–38 | 25–31 | 97% | no |
| Georgia Southern @ Troy | 28–21 | 45–7 | 73% | no |
| Georgia State @ Marshall | 28–31 | 27–28 | 58% | yes |
| South Alabama @ Southern Miss | 34–31 | 40–35 | 62% | yes |

## FBS power ratings

Points per game better than an average FBS team on a neutral field, from opponent-adjusted EPA (garbage time removed) with this season's games weighted against a preseason prior, plus the weight the margin model puts on Elo (a rating built from game results alone). Defense is positive when it holds opponents below average.

| # | Team | Conference | Net | Offense | Defense | Special teams | Results (Elo) | Elo rating |
|---|---|---|---|---|---|---|---|---|
| 1 | Georgia | SEC | +27.8 | +9.2 | +12.4 | +0.9 | +5.4 | 1944 |
| 2 | Notre Dame | FBS Independents | +24.5 | +8.9 | +9.9 | +1.0 | +4.7 | 1892 |
| 3 | LSU | SEC | +23.4 | +9.6 | +12.0 | -0.2 | +2.0 | 1672 |
| 4 | Miami | ACC | +23.0 | +14.6 | +3.4 | +0.3 | +4.6 | 1881 |
| 5 | Ohio State | Big Ten | +22.9 | +11.1 | +8.1 | +0.3 | +3.4 | 1784 |
| 6 | Alabama | SEC | +22.0 | +8.1 | +9.2 | +0.6 | +4.1 | 1842 |
| 7 | Wake Forest | ACC | +21.8 | +8.8 | +9.1 | +0.5 | +3.5 | 1790 |
| 8 | Texas | SEC | +21.8 | +3.3 | +13.0 | +1.1 | +4.4 | 1866 |
| 9 | Utah | Big 12 | +21.4 | +11.1 | +5.8 | +0.1 | +4.5 | 1869 |
| 10 | Oregon | Big Ten | +21.2 | +6.6 | +9.8 | +0.8 | +4.0 | 1835 |
| 11 | Indiana | Big Ten | +20.8 | +5.3 | +10.0 | +0.4 | +5.0 | 1916 |
| 12 | Texas Tech | Big 12 | +19.5 | +2.4 | +11.8 | +1.6 | +3.8 | 1814 |
| 13 | Tennessee | SEC | +19.2 | +4.0 | +10.2 | +1.4 | +3.7 | 1807 |
| 14 | Oklahoma | SEC | +18.6 | +2.0 | +13.4 | +0.7 | +2.6 | 1718 |
| 15 | UCLA | Big Ten | +17.8 | +4.3 | +10.3 | +0.7 | +2.5 | 1708 |
| 16 | Ole Miss | SEC | +17.6 | +10.9 | +3.4 | +0.6 | +2.7 | 1729 |
| 17 | Louisville | ACC | +16.5 | +9.0 | +4.4 | +0.6 | +2.5 | 1711 |
| 18 | Iowa | Big Ten | +16.4 | +2.0 | +9.7 | +0.9 | +3.8 | 1816 |
| 19 | Auburn | SEC | +14.5 | +6.3 | +6.6 | +0.5 | +1.2 | 1605 |
| 20 | Nebraska | Big Ten | +13.9 | +5.1 | +7.0 | +0.4 | +1.4 | 1622 |
| 21 | USC | Big Ten | +13.6 | +10.3 | +0.5 | +0.1 | +2.7 | 1724 |
| 22 | Missouri | SEC | +12.9 | +3.6 | +7.0 | +0.3 | +2.0 | 1667 |
| 23 | BYU | Big 12 | +12.7 | +4.0 | +4.7 | +0.8 | +3.2 | 1771 |
| 24 | Florida | SEC | +12.2 | +6.4 | +4.2 | +0.4 | +1.2 | 1603 |
| 25 | Penn State | Big Ten | +11.9 | +3.4 | +6.7 | +0.1 | +1.7 | 1644 |
| 26 | Michigan | Big Ten | +11.4 | +1.1 | +9.1 | -0.0 | +1.2 | 1608 |
| 27 | Arizona | Big 12 | +11.0 | +6.2 | +2.5 | -0.1 | +2.4 | 1706 |
| 28 | Washington | Big Ten | +10.8 | +3.4 | +5.0 | +0.1 | +2.3 | 1698 |
| 29 | SMU | ACC | +10.4 | +6.5 | +2.0 | +0.2 | +1.6 | 1637 |
| 30 | South Carolina | SEC | +10.0 | +4.4 | +4.1 | +0.4 | +1.2 | 1602 |
| 31 | Baylor | Big 12 | +9.6 | +0.6 | +7.4 | +0.8 | +0.9 | 1583 |
| 32 | Houston | Big 12 | +9.4 | +8.6 | -0.9 | +0.3 | +1.5 | 1633 |
| 33 | Northwestern | Big Ten | +9.2 | +6.1 | +1.7 | +0.6 | +0.7 | 1567 |
| 34 | Wisconsin | Big Ten | +8.8 | -0.1 | +7.1 | +0.6 | +1.2 | 1605 |
| 35 | Kansas | Big 12 | +8.6 | +4.8 | +4.0 | +0.0 | -0.3 | 1488 |
| 36 | Oklahoma State | Big 12 | +8.3 | +8.0 | -0.1 | +0.2 | +0.3 | 1530 |
| 37 | Texas A&M | SEC | +7.9 | -0.1 | +7.4 | +0.3 | +0.3 | 1533 |
| 38 | Kentucky | SEC | +7.5 | +2.4 | +3.8 | +0.3 | +1.1 | 1594 |
| 39 | Arizona State | Big 12 | +7.1 | +1.7 | +4.1 | +0.2 | +1.1 | 1599 |
| 40 | Duke | ACC | +6.8 | +3.4 | +1.1 | +0.6 | +1.6 | 1639 |
| 41 | Boise State | Pac-12 | +6.4 | +7.2 | -3.5 | -0.1 | +2.8 | 1735 |
| 42 | Kansas State | Big 12 | +6.4 | +4.6 | +2.5 | +0.3 | -0.9 | 1436 |
| 43 | TCU | Big 12 | +5.8 | -1.8 | +6.4 | +0.0 | +1.1 | 1599 |
| 44 | Mississippi State | SEC | +5.7 | +2.7 | +3.7 | +0.1 | -0.7 | 1449 |
| 45 | Iowa State | Big 12 | +5.5 | +4.4 | +0.1 | +0.9 | +0.0 | 1512 |
| 46 | Clemson | ACC | +4.9 | -6.2 | +8.8 | +1.1 | +1.2 | 1608 |
| 47 | UCF | Big 12 | +4.8 | +2.8 | +2.1 | -0.1 | -0.0 | 1505 |
| 48 | Illinois | Big Ten | +4.7 | +5.1 | -1.7 | +0.3 | +1.0 | 1590 |
| 49 | Cincinnati | Big 12 | +4.5 | +8.9 | -4.8 | +0.2 | +0.2 | 1526 |
| 50 | Colorado | Big 12 | +4.5 | +2.2 | +4.0 | -0.5 | -1.2 | 1413 |
| 51 | Vanderbilt | SEC | +4.2 | +2.2 | +1.2 | +0.8 | +0.0 | 1510 |
| 52 | Virginia | ACC | +4.0 | -0.3 | +3.5 | +0.1 | +0.6 | 1559 |
| 53 | NC State | ACC | +3.9 | +5.9 | -1.6 | -0.7 | +0.3 | 1529 |
| 54 | Maryland | Big Ten | +3.3 | -0.1 | +4.2 | +0.5 | -1.2 | 1408 |
| 55 | Florida State | ACC | +3.2 | +4.6 | -0.8 | -0.3 | -0.4 | 1477 |
| 56 | Pittsburgh | ACC | +2.8 | -2.7 | +4.8 | +0.5 | +0.2 | 1525 |
| 57 | Minnesota | Big Ten | +2.5 | -3.0 | +4.5 | +0.8 | +0.2 | 1526 |
| 58 | Memphis | American Athletic | +2.4 | +4.7 | -2.9 | -0.7 | +1.4 | 1618 |
| 59 | North Carolina | ACC | +2.4 | +3.5 | -1.1 | +0.1 | -0.1 | 1503 |
| 60 | Arkansas | SEC | +2.0 | +1.2 | +1.1 | -0.4 | +0.2 | 1525 |
| 61 | UTSA | American Athletic | +2.0 | +2.3 | -1.9 | -0.1 | +1.6 | 1642 |
| 62 | Texas State | Pac-12 | +1.9 | +7.1 | -5.3 | -1.2 | +1.3 | 1613 |
| 63 | Syracuse | ACC | +1.6 | +1.5 | +2.4 | -0.8 | -1.4 | 1392 |
| 64 | Virginia Tech | ACC | +1.5 | +2.6 | -0.6 | -0.2 | -0.4 | 1475 |
| 65 | Liberty | Conference USA | +1.3 | +1.3 | -1.2 | +0.2 | +1.0 | 1591 |
| 66 | Tulsa | American Athletic | +1.2 | -0.2 | +2.0 | -0.7 | +0.1 | 1517 |
| 67 | James Madison | Sun Belt | +1.0 | -0.8 | +0.1 | +0.2 | +1.4 | 1625 |
| 68 | North Texas | American Athletic | +0.5 | +7.5 | -7.0 | -0.8 | +0.8 | 1573 |
| 69 | Toledo | Mid-American | +0.1 | -3.7 | +3.2 | -0.3 | +0.9 | 1577 |
| 70 | Oregon State | Pac-12 | -0.2 | +4.7 | -3.8 | -0.1 | -1.1 | 1423 |
| 71 | Louisiana Tech | Sun Belt | -0.4 | -2.5 | +1.9 | -0.8 | +1.0 | 1588 |
| 72 | Navy | American Athletic | -0.6 | +3.5 | -3.8 | -0.4 | +0.1 | 1518 |
| 73 | New Mexico | Mountain West | -0.7 | -4.1 | +2.3 | -0.2 | +1.4 | 1620 |
| 74 | West Virginia | Big 12 | -0.9 | +4.9 | -5.0 | +0.3 | -1.1 | 1417 |
| 75 | UConn | FBS Independents | -1.8 | +3.0 | -5.0 | -0.0 | +0.3 | 1530 |
| 76 | East Carolina | American Athletic | -2.1 | -6.6 | +4.7 | -0.8 | +0.5 | 1552 |
| 77 | North Dakota State | Mountain West | -2.4 | -5.6 | +2.8 | +1.0 | -0.6 | 1457 |
| 78 | South Florida | American Athletic | -2.4 | -1.3 | -1.6 | +0.1 | +0.3 | 1531 |
| 79 | Purdue | Big Ten | -2.5 | +2.8 | -4.3 | +0.9 | -1.9 | 1351 |
| 80 | Michigan State | Big Ten | -2.9 | -3.0 | +1.2 | -0.0 | -1.0 | 1428 |
| 81 | Air Force | Mountain West | -3.3 | +2.2 | -5.9 | +0.0 | +0.4 | 1538 |
| 82 | Georgia Southern | Sun Belt | -3.3 | -1.0 | -3.1 | -0.5 | +1.3 | 1610 |
| 83 | Fresno State | Pac-12 | -3.6 | -2.0 | -1.6 | -0.2 | +0.1 | 1520 |
| 84 | Georgia Tech | ACC | -4.5 | +0.7 | -4.1 | -0.3 | -0.8 | 1440 |
| 85 | UNLV | Mountain West | -4.7 | -2.2 | -3.0 | +0.2 | +0.3 | 1536 |
| 86 | Florida Atlantic | American Athletic | -4.7 | +2.6 | -7.4 | +0.7 | -0.6 | 1464 |
| 87 | Army | American Athletic | -5.2 | +3.4 | -8.4 | -0.0 | -0.1 | 1497 |
| 88 | San Diego State | Pac-12 | -5.3 | -3.9 | -0.9 | +0.3 | -0.7 | 1449 |
| 89 | Jacksonville State | Conference USA | -5.6 | -1.2 | -3.8 | +0.0 | -0.6 | 1462 |
| 90 | Stanford | ACC | -5.6 | -2.1 | -3.8 | +0.2 | +0.1 | 1513 |
| 91 | Rutgers | Big Ten | -5.7 | +1.5 | -6.1 | +0.6 | -1.8 | 1364 |
| 92 | Miami (OH) | Mid-American | -5.8 | -4.2 | -2.2 | +0.7 | -0.1 | 1500 |
| 93 | Delaware | Conference USA | -6.0 | +1.7 | -6.8 | +0.1 | -0.9 | 1438 |
| 94 | Western Michigan | Mid-American | -6.1 | -3.8 | -3.8 | +0.5 | +0.9 | 1580 |
| 95 | Washington State | Pac-12 | -6.3 | -4.6 | +0.1 | -0.3 | -1.5 | 1389 |
| 96 | Tulane | American Athletic | -6.4 | -4.2 | -2.3 | +0.2 | -0.2 | 1496 |
| 97 | Boston College | ACC | -6.4 | -3.9 | -1.4 | -0.6 | -0.6 | 1459 |
| 98 | Ohio | Mid-American | -6.5 | -3.6 | -3.2 | -0.1 | +0.3 | 1532 |
| 99 | California | ACC | -7.1 | -2.6 | -1.8 | -0.7 | -2.0 | 1344 |
| 100 | UAB | American Athletic | -7.9 | -6.5 | -0.6 | -0.1 | -0.7 | 1455 |
| 101 | Louisiana | Sun Belt | -8.0 | -3.2 | -4.9 | +0.0 | +0.2 | 1524 |
| 102 | Utah State | Pac-12 | -8.9 | -8.7 | +2.2 | -1.2 | -1.2 | 1412 |
| 103 | App State | Sun Belt | -9.7 | -4.5 | -2.8 | -1.1 | -1.3 | 1400 |
| 104 | Wyoming | Mountain West | -9.8 | -5.2 | -3.6 | -0.2 | -0.8 | 1447 |
| 105 | Kennesaw State | Conference USA | -10.2 | -4.5 | -3.7 | -0.8 | -1.2 | 1412 |
| 106 | Marshall | Sun Belt | -10.4 | -5.2 | -4.3 | +0.0 | -1.0 | 1428 |
| 107 | South Alabama | Sun Belt | -10.7 | +1.1 | -11.2 | +0.3 | -0.8 | 1440 |
| 108 | Hawai'i | Mountain West | -11.1 | -5.0 | -5.2 | +1.2 | -2.1 | 1341 |
| 109 | Old Dominion | Sun Belt | -11.1 | -11.5 | +3.6 | -1.7 | -1.5 | 1389 |
| 110 | Georgia State | Sun Belt | -11.3 | -1.3 | -8.0 | -0.3 | -1.7 | 1370 |
| 111 | Arkansas State | Sun Belt | -12.1 | -3.8 | -6.7 | +0.1 | -1.7 | 1374 |
| 112 | Western Kentucky | Conference USA | -12.2 | -5.9 | -3.8 | -0.5 | -2.0 | 1343 |
| 113 | Rice | American Athletic | -12.6 | -2.3 | -6.3 | -0.9 | -3.1 | 1258 |
| 114 | Coastal Carolina | Sun Belt | -12.7 | -7.1 | -3.9 | +0.2 | -2.0 | 1349 |
| 115 | Temple | American Athletic | -13.2 | -0.5 | -8.6 | -0.5 | -3.6 | 1214 |
| 116 | Central Michigan | Mid-American | -13.2 | -5.9 | -6.0 | +0.1 | -1.3 | 1400 |
| 117 | Buffalo | Mid-American | -13.3 | -9.2 | -4.5 | +0.3 | +0.2 | 1521 |
| 118 | Troy | Sun Belt | -13.3 | -9.0 | -0.5 | -1.3 | -2.4 | 1311 |
| 119 | Colorado State | Pac-12 | -13.4 | +4.4 | -14.3 | -0.2 | -3.3 | 1238 |
| 120 | Nevada | Mountain West | -13.8 | -10.9 | -1.4 | +0.5 | -2.1 | 1337 |
| 121 | Florida International | Conference USA | -14.7 | -8.4 | -2.7 | -1.3 | -2.4 | 1315 |
| 122 | Middle Tennessee | Conference USA | -15.4 | -4.8 | -8.3 | +0.2 | -2.5 | 1303 |
| 123 | San José State | Mountain West | -16.0 | -9.9 | -3.2 | -0.3 | -2.5 | 1302 |
| 124 | Missouri State | Conference USA | -16.7 | -5.4 | -7.5 | -1.0 | -2.8 | 1280 |
| 125 | New Mexico State | Conference USA | -16.7 | -7.3 | -3.9 | -1.8 | -3.7 | 1211 |
| 126 | UL Monroe | Sun Belt | -17.5 | -5.9 | -6.4 | -1.2 | -4.0 | 1181 |
| 127 | Bowling Green | Mid-American | -17.9 | -12.1 | -2.9 | -0.1 | -2.8 | 1280 |
| 128 | Northern Illinois | Mountain West | -17.9 | -2.6 | -8.8 | -1.4 | -5.1 | 1097 |
| 129 | Southern Miss | Sun Belt | -18.2 | -8.6 | -5.5 | -1.3 | -2.8 | 1283 |
| 130 | Eastern Michigan | Mid-American | -18.7 | -7.3 | -8.0 | -0.6 | -2.8 | 1280 |
| 131 | Massachusetts | Mid-American | -19.1 | -9.9 | -5.1 | -0.4 | -3.7 | 1207 |
| 132 | Ball State | Mid-American | -19.2 | -6.4 | -8.6 | -0.6 | -3.7 | 1212 |
| 133 | Sacramento State | Mid-American | -20.4 | -11.2 | -4.7 | +0.2 | -4.6 | 1136 |
| 134 | Sam Houston | Conference USA | -20.8 | -13.1 | -1.5 | -1.2 | -5.0 | 1102 |
| 135 | Charlotte | American Athletic | -21.0 | -9.4 | -7.0 | -0.5 | -4.1 | 1178 |
| 136 | Kent State | Mid-American | -22.7 | -10.9 | -7.3 | -0.7 | -3.8 | 1203 |
| 137 | Akron | Mid-American | -23.1 | -9.6 | -9.2 | -0.5 | -3.8 | 1199 |
| 138 | UTEP | Mountain West | -25.7 | -11.7 | -7.7 | -1.1 | -5.2 | 1088 |

## Current model fit

- Fitted on 4420 games from seasons 2022–2026.
- Home field on top of the ratings: 3.2 points (1.8 in conference games).
- Extra FBS edge over FCS opponents beyond their ratings: 14.0 points.
- Elo weight: 0.20 points of margin per point of Elo spread.
- Weight on the betting line: 91% for the margin, 82% for the total.
