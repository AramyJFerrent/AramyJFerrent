# College football score predictions

Updated Sun Nov 08, 2026 02:58 AM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 11

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/10 7:00 PM | Western Michigan @ Akron | Western Michigan 31, Akron 17 | Western Michigan 82% | Western Michigan -470 / Akron +470 | 30.8 – 17.2 | 17–45 / 6–30 | Western Michigan -14.8 / Western Michigan -13.5 | 49.8 / 47.5 | no edge | no edge | no edge |  |
| Tue 11/10 7:00 PM | Kent State @ Bowling Green | Kent State 17, Bowling Green 24 | Bowling Green 66% | Kent State +190 / Bowling Green -190 | 19.2 – 24.7 | 7–31 / 10–38 | Bowling Green -5.4 / Bowling Green -5.5 | 41.6 / 44.5 | no edge | no edge | no edge |  |
| Tue 11/10 8:00 PM | Ohio @ Miami (OH) | Ohio 24, Miami (OH) 27 | Miami (OH) 54% | Ohio +115 / Miami (OH) -115 | 23.3 – 24.4 | 10–37 / 11–38 | Ohio -2.7 / Miami (OH) -1.5 | 48.4 / 47.5 | no edge | no edge | no edge |  |
| Wed 11/11 TBA | Massachusetts @ Toledo | Massachusetts 17, Toledo 31 | Toledo 84% | Massachusetts +515 / Toledo -515 | 19.1 – 33.5 | 7–31 / 19–49 | Toledo -18.8 / Toledo -14.0 | 48.8 / 53.5 | no edge | no edge | no edge |  |
| Wed 11/11 7:30 PM | Buffalo @ Ball State | Buffalo 27, Ball State 24 | Buffalo 56% | Buffalo -130 / Ball State +130 | 27.2 – 24.6 | 14–42 / 12–38 | Ball State -1.2 / Buffalo -3.0 | 52.9 / 51.5 | no edge | no edge | no edge |  |
| Wed 11/11 7:30 PM | Sacramento State @ Central Michigan | Sacramento State 17, Central Michigan 31 | Central Michigan 86% | Sacramento State +595 / Central Michigan -595 | 14.8 – 29.9 | 3–27 / 16–45 | Central Michigan -10.9 / Central Michigan -15.5 | 45.8 / 44.5 | no edge | no edge | no edge |  |
| Thu 11/12 8:00 PM | Memphis @ South Florida | Memphis 27, South Florida 24 | Memphis 67% | Memphis -200 / South Florida +200 | 28.3 – 22.3 | 14–43 / 10–35 | Memphis -0.8 / Memphis -6.5 | 55.0 / 49.5 | no edge | no edge | no edge |  |
| Thu 11/12 9:00 PM | Louisiana @ UL Monroe | Louisiana 31, UL Monroe 21 | Louisiana 78% | Louisiana -350 / UL Monroe +350 | 30.2 – 19.1 | 16–45 / 7–31 | Louisiana -5.9 / Louisiana -11.5 | 52.8 / 48.5 | no edge | UL Monroe (+350): EV +3.3%, 23%, stake 0.2u | no edge |  |
| Fri 11/13 7:00 PM | Florida State @ Pittsburgh | Florida State 24, Pittsburgh 27 | Pittsburgh 60% | Florida State +150 / Pittsburgh -150 | 25.2 – 28.7 | 12–39 / 14–43 | Pittsburgh -2.5 / Pittsburgh -3.5 | 55.6 / 53.5 | no edge | no edge | no edge |  |
| Fri 11/13 9:00 PM | Illinois @ UCLA | Illinois 21, UCLA 31 | UCLA 75% | Illinois +300 / UCLA -300 | 19.3 – 29.2 | 7–32 / 14–44 | UCLA -14.2 / UCLA -9.5 | 52.6 / 47.5 | no edge | no edge | no edge |  |
| Fri 11/13 10:15 PM | Houston @ Colorado | Houston 31, Colorado 21 | Houston 76% | Houston -325 / Colorado +325 | 29.9 – 19.8 | 16–45 / 7–31 | Houston -5.7 / Houston -10.5 | 54.3 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Arizona State @ UCF | Arizona State 24, UCF 27 | UCF 50% | Arizona State +100 / UCF -100 | 25.0 – 25.2 | 12–38 / 13–39 | UCF -0.2 / – | 50.3 / – | no line yet | no line yet (fair: UCF -100) | no line yet |  |
| Sat 11/14 TBA | Baylor @ BYU | Baylor 21, BYU 28 | BYU 67% | Baylor +205 / BYU -205 | 21.4 – 27.8 | 9–34 / 14–42 | BYU -6.0 / BYU -6.5 | 52.1 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Cincinnati @ Iowa State | Cincinnati 28, Iowa State 31 | Iowa State 60% | Cincinnati +150 / Iowa State -150 | 28.5 – 32.2 | 14–42 / 17–48 | Iowa State -3.6 / – | 60.7 / – | no line yet | no line yet (fair: Iowa State -150) | no line yet |  |
| Sat 11/14 TBA | Kansas @ West Virginia | Kansas 34, West Virginia 31 | Kansas 60% | Kansas -150 / West Virginia +150 | 32.6 – 28.8 | 17–48 / 14–44 | Kansas -3.8 / – | 61.6 / – | no line yet | no line yet (fair: Kansas -150) | no line yet |  |
| Sat 11/14 TBA | Kansas State @ TCU | Kansas State 21, TCU 24 | TCU 54% | Kansas State +115 / TCU -115 | 23.5 – 24.8 | 10–38 / 10–38 | TCU -1.3 / – | 48.3 / – | no line yet | no line yet (fair: TCU -115) | no line yet |  |
| Sat 11/14 TBA | Texas Tech @ Oklahoma State | Texas Tech 31, Oklahoma State 28 | Texas Tech 55% | Texas Tech -125 / Oklahoma State +125 | 32.0 – 30.0 | 17–48 / 16–45 | Texas Tech -6.7 / Texas Tech -1.5 | 55.8 / 63.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Utah @ Arizona | Utah 27, Arizona 24 | Utah 57% | Utah -135 / Arizona +135 | 28.0 – 25.2 | 14–42 / 13–39 | Utah -5.6 / Utah -2.5 | 56.2 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Missouri @ Georgia | Missouri 17, Georgia 31 | Georgia 83% | Missouri +475 / Georgia -475 | 16.9 – 30.3 | 6–29 / 16–45 | Georgia -12.1 / Georgia -13.5 | 46.4 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Florida @ Kentucky | Florida 24, Kentucky 27 | Kentucky 56% | Florida +130 / Kentucky -130 | 25.4 – 27.6 | 13–40 / 14–42 | Florida -1.2 / Kentucky -2.5 | 51.7 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Texas @ LSU | Texas 21, LSU 24 | LSU 63% | Texas +170 / LSU -170 | 20.4 – 25.2 | 7–34 / 12–39 | LSU -8.3 / LSU -4.5 | 46.1 / 45.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Ole Miss @ Oklahoma | Ole Miss 27, Oklahoma 24 | Ole Miss 56% | Ole Miss -130 / Oklahoma +130 | 26.5 – 24.1 | 13–41 / 10–38 | Ole Miss -1.5 / Ole Miss -2.5 | 50.6 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Tennessee @ Texas A&M | Tennessee 24, Texas A&M 21 | Tennessee 58% | Tennessee -140 / Texas A&M +140 | 23.4 – 20.5 | 10–38 / 7–34 | Tennessee -2.6 / Tennessee -3.0 | 45.7 / 43.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Louisville @ North Carolina | Louisville 31, North Carolina 28 | Louisville 58% | Louisville -135 / North Carolina +135 | 30.9 – 28.0 | 17–45 / 14–42 | Louisville -8.2 / Louisville -2.5 | 57.1 / 59.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Stanford @ Virginia Tech | Stanford 17, Virginia Tech 34 | Virginia Tech 86% | Stanford +635 / Virginia Tech -635 | 19.1 – 35.0 | 7–31 / 20–50 | Virginia Tech -15.8 / – | 56.4 / – | no line yet | no line yet (fair: Virginia Tech -635) | no line yet |  |
| Sat 11/14 TBA | Purdue @ Iowa | Purdue 17, Iowa 34 | Iowa 88% | Purdue +715 / Iowa -715 | 16.3 – 32.9 | 6–28 / 17–48 | Iowa -16.6 / – | 49.2 / – | no line yet | no line yet (fair: Iowa -715) | no line yet |  |
| Sat 11/14 12:00 PM | Auburn @ Mississippi State | Auburn 31, Mississippi State 28 | Auburn 51% | Auburn -105 / Mississippi State +105 | 28.5 – 28.2 | 14–44 / 14–42 | Auburn -0.2 / – | 56.7 / – | no line yet | no line yet (fair: Auburn -105) | no line yet |  |
| Sat 11/14 12:00 PM | Duke @ Miami | Duke 21, Miami 38 | Miami 86% | Duke +620 / Miami -620 | 20.3 – 35.9 | 7–34 / 21–52 | Miami -16.3 / Miami -15.5 | 56.5 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/14 12:00 PM | Syracuse @ NC State | Syracuse 24, NC State 27 | NC State 58% | Syracuse +135 / NC State -135 | 26.2 – 29.0 | 13–41 / 14–44 | NC State -2.8 / – | 57.4 / – | no line yet | no line yet (fair: NC State -135) | no line yet |  |
| Sat 11/14 12:00 PM | Wake Forest @ SMU | Wake Forest 31, SMU 28 | Wake Forest 57% | Wake Forest -130 / SMU +130 | 30.0 – 27.7 | 16–45 / 14–42 | SMU -0.3 / Wake Forest -2.5 | 54.4 / 58.5 | no edge | no edge | no edge |  |
| Sat 11/14 12:00 PM | Wisconsin @ Maryland | Wisconsin 24, Maryland 21 | Wisconsin 58% | Wisconsin -140 / Maryland +140 | 23.3 – 20.4 | 10–37 / 7–34 | Wisconsin -2.9 / – | 45.0 / – | no line yet | no line yet (fair: Wisconsin -140) | no line yet |  |
| Sat 11/14 12:00 PM | Northwestern @ Ohio State | Northwestern 17, Ohio State 31 | Ohio State 77% | Northwestern +340 / Ohio State -340 | 18.8 – 29.8 | 7–31 / 14–45 | Ohio State -16.7 / Ohio State -10.5 | 54.0 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/14 12:00 PM | James Madison @ UConn | James Madison 31, UConn 28 | James Madison 59% | James Madison -145 / UConn +145 | 29.7 – 26.5 | 16–44 / 13–41 | James Madison -3.2 / – | 56.2 / – | no line yet | no line yet (fair: James Madison -145) | no line yet |  |
| Sat 11/14 12:30 PM | Georgia Tech @ Clemson | Georgia Tech 17, Clemson 31 | Clemson 83% | Georgia Tech +495 / Clemson -495 | 17.5 – 30.9 | 6–30 / 17–45 | Clemson -13.4 / – | 49.5 / – | no line yet | no line yet (fair: Clemson -495) | no line yet |  |
| Sat 11/14 12:30 PM | Nebraska @ Rutgers | Nebraska 34, Rutgers 20 | Nebraska 80% | Nebraska -405 / Rutgers +405 | 33.2 – 20.7 | 18–48 / 7–34 | Nebraska -12.6 / – | 54.5 / – | no line yet | no line yet (fair: Nebraska -405) | no line yet |  |
| Sat 11/14 12:45 PM | Alabama @ Vanderbilt | Alabama 38, Vanderbilt 17 | Alabama 90% | Alabama -920 / Vanderbilt +920 | 36.4 – 17.5 | 21–52 / 7–30 | Alabama -12.8 / Alabama -19.5 | 51.6 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/14 1:00 PM | East Carolina @ Charlotte | East Carolina 31, Charlotte 17 | East Carolina 85% | East Carolina -565 / Charlotte +565 | 32.5 – 17.6 | 17–48 / 7–30 | East Carolina -14.9 / – | 50.0 / – | no line yet | no line yet (fair: East Carolina -565) | no line yet |  |
| Sat 11/14 1:00 PM | UAB @ Temple | UAB 24, Temple 27 | Temple 56% | UAB +125 / Temple -125 | 24.5 – 26.7 | 10–38 / 13–41 | Temple -2.2 / – | 51.5 / – | no line yet | no line yet (fair: Temple -125) | no line yet |  |
| Sat 11/14 1:00 PM | Arkansas State @ Coastal Carolina | Arkansas State 24, Coastal Carolina 27 | Coastal Carolina 54% | Arkansas State +115 / Coastal Carolina -115 | 24.3 – 25.9 | 10–38 / 13–41 | Coastal Carolina -1.5 / – | 51.5 / – | no line yet | no line yet (fair: Coastal Carolina -115) | no line yet |  |
| Sat 11/14 2:00 PM | Tulane @ Rice | Tulane 27, Rice 24 | Tulane 61% | Tulane -160 / Rice +160 | 27.3 – 23.1 | 14–42 / 10–37 | Tulane -4.2 / – | 50.5 / – | no line yet | no line yet (fair: Tulane -160) | no line yet |  |
| Sat 11/14 2:00 PM | Kennesaw State @ Sam Houston | Kennesaw State 24, Sam Houston 21 | Kennesaw State 62% | Kennesaw State -160 / Sam Houston +160 | 24.2 – 19.9 | 10–38 / 7–33 | Kennesaw State -4.3 / – | 44.1 / – | no line yet | no line yet (fair: Kennesaw State -160) | no line yet |  |
| Sat 11/14 3:00 PM | New Mexico State @ Missouri State | New Mexico State 24, Missouri State 27 | Missouri State 64% | New Mexico State +175 / Missouri State -175 | 23.3 – 28.7 | 10–38 / 14–44 | Missouri State -5.4 / – | 52.0 / – | no line yet | no line yet (fair: Missouri State -175) | no line yet |  |
| Sat 11/14 3:00 PM | Florida International @ Delaware | Florida International 17, Delaware 31 | Delaware 80% | Florida International +400 / Delaware -400 | 19.2 – 31.7 | 7–32 / 17–48 | Delaware -12.5 / – | 51.9 / – | no line yet | no line yet (fair: Delaware -400) | no line yet |  |
| Sat 11/14 3:30 PM | Boston College @ Notre Dame | Boston College 3, Notre Dame 38 | Notre Dame 100% | Boston College +9900 / Notre Dame -9900 | 6.2 – 40.0 | 0–13 / 24–56 | Notre Dame -33.8 / – | 47.6 / – | no line yet | no line yet (fair: Notre Dame -9900) | no line yet |  |
| Sat 11/14 3:30 PM | California @ Virginia | California 21, Virginia 31 | Virginia 75% | California +295 / Virginia -295 | 20.2 – 29.7 | 7–34 / 16–45 | Virginia -9.5 / – | 50.8 / – | no line yet | no line yet (fair: Virginia -295) | no line yet |  |
| Sat 11/14 3:30 PM | USC @ Indiana | USC 21, Indiana 28 | Indiana 68% | USC +210 / Indiana -210 | 21.3 – 28.5 | 9–34 / 14–43 | Indiana -10.0 / Indiana -7.0 | 50.9 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Michigan @ Oregon | Michigan 17, Oregon 24 | Oregon 75% | Michigan +295 / Oregon -295 | 16.4 – 25.6 | 6–28 / 13–41 | Oregon -4.9 / Oregon -9.5 | 44.1 / 41.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Florida Atlantic @ Tulsa | Florida Atlantic 31, Tulsa 34 | Tulsa 57% | Florida Atlantic +130 / Tulsa -130 | 31.4 – 34.4 | 17–47 / 20–49 | Tulsa -2.9 / – | 65.8 / – | no line yet | no line yet (fair: Tulsa -130) | no line yet |  |
| Sat 11/14 3:30 PM | Nevada @ Northern Illinois | Nevada 27, Northern Illinois 24 | Nevada 57% | Nevada -135 / Northern Illinois +135 | 25.8 – 23.3 | 13–40 / 10–38 | Nevada -2.4 / – | 49.1 / – | no line yet | no line yet (fair: Nevada -135) | no line yet |  |
| Sat 11/14 3:30 PM | Georgia Southern @ Georgia State | Georgia Southern 28, Georgia State 31 | Georgia State 54% | Georgia Southern +120 / Georgia State -120 | 27.7 – 29.7 | 14–42 / 16–44 | Georgia State -2.0 / – | 58.7 / – | no line yet | no line yet (fair: Georgia State -120) | no line yet |  |
| Sat 11/14 3:30 PM | Jacksonville State @ Western Kentucky | Jacksonville State 27, Western Kentucky 24 | Jacksonville State 64% | Jacksonville State -175 / Western Kentucky +175 | 29.2 – 24.1 | 14–44 / 10–38 | Jacksonville State -5.1 / – | 53.5 / – | no line yet | no line yet (fair: Jacksonville State -175) | no line yet |  |
| Sat 11/14 3:30 PM | Middle Tennessee @ Liberty | Middle Tennessee 13, Liberty 34 | Liberty 93% | Middle Tennessee +1290 / Liberty -1290 | 13.4 – 34.3 | 3–24 / 20–51 | Liberty -20.9 / – | 49.2 / – | no line yet | no line yet (fair: Liberty -1290) | no line yet |  |
| Sat 11/14 4:00 PM | Fresno State @ Texas State | Fresno State 28, Texas State 31 | Texas State 60% | Fresno State +150 / Texas State -150 | 28.4 – 32.5 | 14–42 / 17–48 | Texas State -4.1 / – | 60.8 / – | no line yet | no line yet (fair: Texas State -150) | no line yet |  |
| Sat 11/14 4:15 PM | Washington @ Michigan State | Washington 24, Michigan State 17 | Washington 75% | Washington -305 / Michigan State +305 | 27.5 – 17.9 | 14–42 / 7–30 | Washington -9.6 / – | 45.6 / – | no line yet | no line yet (fair: Washington -305) | no line yet |  |
| Sat 11/14 5:00 PM | Southern Miss @ Louisiana Tech | Southern Miss 17, Louisiana Tech 34 | Louisiana Tech 85% | Southern Miss +565 / Louisiana Tech -565 | 18.3 – 33.5 | 7–31 / 19–49 | Louisiana Tech -15.2 / – | 51.8 / – | no line yet | no line yet (fair: Louisiana Tech -565) | no line yet |  |
| Sat 11/14 6:00 PM | Oregon State @ Boise State | Oregon State 31, Boise State 34 | Boise State 63% | Oregon State +165 / Boise State -165 | 28.7 – 33.4 | 14–42 / 20–48 | Boise State -6.7 / Boise State -4.5 | 60.6 / 62.5 | no edge | no edge | no edge |  |
| Sat 11/14 6:00 PM | App State @ Marshall | App State 24, Marshall 31 | Marshall 63% | App State +175 / Marshall -175 | 25.3 – 30.6 | 13–39 / 17–45 | Marshall -5.3 / – | 55.9 / – | no line yet | no line yet (fair: Marshall -175) | no line yet |  |
| Sat 11/14 7:00 PM | Minnesota @ Penn State | Minnesota 17, Penn State 24 | Penn State 70% | Minnesota +235 / Penn State -235 | 17.8 – 25.1 | 7–31 / 13–39 | Penn State -10.2 / Penn State -7.0 | 41.1 / 43.5 | no edge | no edge | no edge |  |
| Sat 11/14 7:00 PM | San José State @ Air Force | San José State 20, Air Force 34 | Air Force 82% | San José State +455 / Air Force -455 | 20.4 – 33.6 | 7–34 / 19–49 | Air Force -13.2 / – | 53.9 / – | no line yet | no line yet (fair: Air Force -455) | no line yet |  |
| Sat 11/14 7:00 PM | Troy @ South Alabama | Troy 24, South Alabama 27 | South Alabama 58% | Troy +140 / South Alabama -140 | 25.9 – 28.9 | 13–41 / 14–44 | South Alabama -3.1 / – | 54.8 / – | no line yet | no line yet (fair: South Alabama -140) | no line yet |  |
| Sat 11/14 7:30 PM | UNLV @ New Mexico | UNLV 20, New Mexico 27 | New Mexico 69% | UNLV +220 / New Mexico -220 | 19.6 – 27.0 | 7–33 / 14–41 | New Mexico -7.4 / – | 46.6 / – | no line yet | no line yet (fair: New Mexico -220) | no line yet |  |
| Sat 11/14 7:45 PM | South Carolina @ Arkansas | South Carolina 31, Arkansas 24 | South Carolina 72% | South Carolina -260 / Arkansas +260 | 30.4 – 21.7 | 17–45 / 10–35 | South Carolina -10.3 / South Carolina -8.5 | 54.8 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/14 9:00 PM | North Texas @ UTSA | North Texas 35, UTSA 38 | UTSA 53% | North Texas +110 / UTSA -110 | 34.1 – 35.0 | 20–49 / 20–51 | UTSA -0.9 / – | 69.1 / – | no line yet | no line yet (fair: UTSA -110) | no line yet |  |
| Sat 11/14 9:30 PM | Utah State @ San Diego State | Utah State 24, San Diego State 27 | San Diego State 56% | Utah State +130 / San Diego State -130 | 22.9 – 25.6 | 10–37 / 13–40 | San Diego State -2.7 / – | 48.5 / – | no line yet | no line yet (fair: San Diego State -130) | no line yet |  |
| Sat 11/14 10:00 PM | Wyoming @ UTEP | Wyoming 27, UTEP 17 | Wyoming 79% | Wyoming -380 / UTEP +380 | 28.5 – 16.9 | 14–43 / 6–30 | Wyoming -11.6 / – | 45.4 / – | no line yet | no line yet (fair: Wyoming -380) | no line yet |  |
| Sat 11/14 10:30 PM | Colorado State @ Washington State | Colorado State 24, Washington State 31 | Washington State 65% | Colorado State +190 / Washington State -190 | 25.6 – 31.7 | 13–40 / 17–48 | Washington State -6.1 / – | 57.3 / – | no line yet | no line yet (fair: Washington State -190) | no line yet |  |
| Sat 11/14 11:00 PM | North Dakota State @ Hawai'i | North Dakota State 27, Hawai'i 20 | North Dakota State 69% | North Dakota State -225 / Hawai'i +225 | 26.7 – 19.6 | 13–41 / 7–32 | North Dakota State -7.1 / – | 47.5 / – | no line yet | no line yet (fair: North Dakota State -225) | no line yet |  |

## 2026 Week 12

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/17 7:00 PM | Ball State @ Ohio | Ball State 17, Ohio 34 | Ohio 87% | Ball State +685 / Ohio -685 | 17.3 – 33.9 | 6–30 / 20–49 | Ohio -16.7 / – | 51.2 / – | no line yet | no line yet (fair: Ohio -685) | no line yet |  |
| Tue 11/17 7:00 PM | Eastern Michigan @ Western Michigan | Eastern Michigan 17, Western Michigan 34 | Western Michigan 87% | Eastern Michigan +660 / Western Michigan -660 | 17.4 – 33.5 | 6–30 / 19–49 | Western Michigan -16.0 / – | 50.9 / – | no line yet | no line yet (fair: Western Michigan -660) | no line yet |  |
| Tue 11/17 7:00 PM | Miami (OH) @ Kent State | Miami (OH) 27, Kent State 17 | Miami (OH) 76% | Miami (OH) -310 / Kent State +310 | 28.5 – 18.1 | 14–43 / 7–31 | Miami (OH) -10.4 / – | 46.6 / – | no line yet | no line yet (fair: Miami (OH) -310) | no line yet |  |
| Wed 11/18 TBA | Akron @ Massachusetts | Akron 20, Massachusetts 27 | Massachusetts 73% | Akron +275 / Massachusetts -275 | 19.6 – 28.1 | 7–33 / 14–42 | Massachusetts -8.5 / – | 47.7 / – | no line yet | no line yet (fair: Massachusetts -275) | no line yet |  |
| Wed 11/18 TBA | Central Michigan @ Buffalo | Central Michigan 27, Buffalo 24 | Central Michigan 56% | Central Michigan -130 / Buffalo +130 | 26.2 – 23.9 | 13–41 / 10–38 | Central Michigan -2.3 / – | 50.1 / – | no line yet | no line yet (fair: Central Michigan -130) | no line yet |  |
| Thu 11/19 7:30 PM | Rice @ Temple | Rice 24, Temple 31 | Temple 64% | Rice +175 / Temple -175 | 24.0 – 29.6 | 10–38 / 16–44 | Temple -5.6 / – | 53.5 / – | no line yet | no line yet (fair: Temple -175) | no line yet |  |
| Fri 11/20 6:00 PM | Iowa State @ UCF | Iowa State 27, UCF 24 | Iowa State 56% | Iowa State -130 / UCF +130 | 26.9 – 24.7 | 13–41 / 11–38 | Iowa State -2.2 / – | 51.6 / – | no line yet | no line yet (fair: Iowa State -130) | no line yet |  |
| Fri 11/20 7:30 PM | Clemson @ Duke | Clemson 21, Duke 24 | Duke 66% | Clemson +190 / Duke -190 | 20.3 – 25.9 | 7–34 / 13–41 | Duke -5.7 / – | 46.2 / – | no line yet | no line yet (fair: Duke -190) | no line yet |  |
| Fri 11/20 7:30 PM | Bowling Green @ Toledo | Bowling Green 10, Toledo 31 | Toledo 93% | Bowling Green +1260 / Toledo -1260 | 12.4 – 32.5 | 3–23 / 17–48 | Toledo -20.1 / – | 44.9 / – | no line yet | no line yet (fair: Toledo -1260) | no line yet |  |
| Fri 11/20 8:00 PM | Oregon @ Michigan State | Oregon 31, Michigan State 14 | Oregon 91% | Oregon -1000 / Michigan State +1000 | 32.1 – 14.0 | 17–48 / 3–25 | Oregon -18.0 / – | 46.1 / – | no line yet | no line yet (fair: Oregon -1000) | no line yet |  |
| Fri 11/20 8:00 PM | UTEP @ Air Force | UTEP 17, Air Force 38 | Air Force 94% | UTEP +1635 / Air Force -1635 | 14.8 – 37.3 | 3–27 / 23–53 | Air Force -22.5 / – | 52.1 / – | no line yet | no line yet (fair: Air Force -1635) | no line yet |  |
| Fri 11/20 9:00 PM | New Mexico @ Wyoming | New Mexico 24, Wyoming 17 | New Mexico 73% | New Mexico -265 / Wyoming +265 | 25.9 – 17.1 | 13–40 / 7–30 | New Mexico -8.8 / – | 43.0 / – | no line yet | no line yet (fair: New Mexico -265) | no line yet |  |
| Sat 11/21 TBA | Vanderbilt @ Florida | Vanderbilt 21, Florida 31 | Florida 78% | Vanderbilt +350 / Florida -350 | 21.3 – 32.6 | 9–35 / 17–48 | Florida -11.3 / – | 53.9 / – | no line yet | no line yet (fair: Florida -350) | no line yet |  |
| Sat 11/21 TBA | Kentucky @ Missouri | Kentucky 21, Missouri 28 | Missouri 70% | Kentucky +235 / Missouri -235 | 20.7 – 28.3 | 7–34 / 14–43 | Missouri -7.6 / – | 49.1 / – | no line yet | no line yet (fair: Missouri -235) | no line yet |  |
| Sat 11/21 TBA | Texas A&M @ Oklahoma | Texas A&M 24, Oklahoma 27 | Oklahoma 57% | Texas A&M +135 / Oklahoma -135 | 23.3 – 26.1 | 10–37 / 13–41 | Oklahoma -5.9 / Oklahoma -2.5 | 40.4 / 51.5 | no edge | no edge | Under 51.5 (-110*): EV +3.7%, 54%, stake 1.0u | * price not posted; assumed -110 |
| Sat 11/21 TBA | Georgia @ South Carolina | Georgia 31, South Carolina 24 | Georgia 73% | Georgia -275 / South Carolina +275 | 29.9 – 20.7 | 16–45 / 7–34 | Georgia -9.2 / – | 50.5 / – | no line yet | no line yet (fair: Georgia -275) | no line yet |  |
| Sat 11/21 TBA | LSU @ Tennessee | LSU 31, Tennessee 28 | LSU 56% | LSU -125 / Tennessee +125 | 29.0 – 27.0 | 14–44 / 13–41 | LSU -7.2 / LSU -1.5 | 49.7 / 57.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | Arkansas @ Texas | Arkansas 10, Texas 34 | Texas 95% | Arkansas +1990 / Texas -1990 | 11.7 – 34.6 | 3–21 / 20–51 | Texas -23.0 / – | 46.3 / – | no line yet | no line yet (fair: Texas -1990) | no line yet |  |
| Sat 11/21 TBA | Arizona @ Kansas State | Arizona 27, Kansas State 24 | Arizona 58% | Arizona -135 / Kansas State +135 | 29.0 – 26.0 | 14–44 / 13–41 | Arizona -3.0 / – | 55.0 / – | no line yet | no line yet (fair: Arizona -135) | no line yet |  |
| Sat 11/21 TBA | BYU @ Kansas | BYU 27, Kansas 24 | BYU 62% | BYU -165 / Kansas +165 | 28.4 – 23.8 | 14–42 / 10–38 | BYU -4.6 / – | 52.2 / – | no line yet | no line yet (fair: BYU -165) | no line yet |  |
| Sat 11/21 TBA | Colorado @ Cincinnati | Colorado 24, Cincinnati 31 | Cincinnati 67% | Colorado +205 / Cincinnati -205 | 25.8 – 32.6 | 13–40 / 17–48 | Cincinnati -6.8 / – | 58.4 / – | no line yet | no line yet (fair: Cincinnati -205) | no line yet |  |
| Sat 11/21 TBA | Houston @ West Virginia | Houston 35, West Virginia 28 | Houston 69% | Houston -220 / West Virginia +220 | 35.5 – 28.2 | 20–51 / 14–42 | Houston -7.3 / – | 63.7 / – | no line yet | no line yet (fair: Houston -220) | no line yet |  |
| Sat 11/21 TBA | Oklahoma State @ Arizona State | Oklahoma State 31, Arizona State 28 | Oklahoma State 56% | Oklahoma State -130 / Arizona State +130 | 30.5 – 28.1 | 16–45 / 14–42 | Oklahoma State -2.4 / – | 58.6 / – | no line yet | no line yet (fair: Oklahoma State -130) | no line yet |  |
| Sat 11/21 TBA | Texas Tech @ Baylor | Texas Tech 28, Baylor 21 | Texas Tech 67% | Texas Tech -205 / Baylor +205 | 28.3 – 21.9 | 14–42 / 10–35 | Texas Tech -6.5 / – | 50.2 / – | no line yet | no line yet (fair: Texas Tech -205) | no line yet |  |
| Sat 11/21 TBA | Utah @ TCU | Utah 31, TCU 17 | Utah 80% | Utah -400 / TCU +400 | 30.9 – 18.7 | 17–46 / 7–31 | Utah -12.2 / – | 49.6 / – | no line yet | no line yet (fair: Utah -400) | no line yet |  |
| Sat 11/21 TBA | Virginia Tech @ Miami | Virginia Tech 21, Miami 38 | Miami 86% | Virginia Tech +640 / Miami -640 | 20.0 – 36.9 | 7–33 / 21–52 | Miami -21.2 / Miami -16.5 | 58.4 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | NC State @ Florida State | NC State 27, Florida State 34 | Florida State 65% | NC State +185 / Florida State -185 | 27.4 – 33.4 | 14–42 / 19–49 | Florida State -6.0 / – | 60.8 / – | no line yet | no line yet (fair: Florida State -185) | no line yet |  |
| Sat 11/21 TBA | North Carolina @ Virginia | North Carolina 27, Virginia 24 | North Carolina 53% | North Carolina -115 / Virginia +115 | 26.4 – 25.1 | 13–41 / 13–38 | North Carolina -1.3 / – | 51.5 / – | no line yet | no line yet (fair: North Carolina -115) | no line yet |  |
| Sat 11/21 TBA | Pittsburgh @ Louisville | Pittsburgh 21, Louisville 31 | Louisville 81% | Pittsburgh +440 / Louisville -440 | 20.6 – 33.5 | 7–34 / 19–49 | Louisville -12.9 / – | 54.0 / – | no line yet | no line yet (fair: Louisville -440) | no line yet |  |
| Sat 11/21 TBA | Stanford @ California | Stanford 24, California 31 | California 62% | Stanford +165 / California -165 | 25.4 – 30.2 | 13–40 / 16–45 | California -4.8 / – | 55.6 / – | no line yet | no line yet (fair: California -165) | no line yet |  |
| Sat 11/21 TBA | Syracuse @ Boston College | Syracuse 27, Boston College 24 | Syracuse 61% | Syracuse -155 / Boston College +155 | 27.5 – 23.4 | 14–42 / 10–37 | Syracuse -4.2 / – | 50.9 / – | no line yet | no line yet (fair: Syracuse -155) | no line yet |  |
| Sat 11/21 TBA | Wake Forest @ Georgia Tech | Wake Forest 35, Georgia Tech 17 | Wake Forest 89% | Wake Forest -840 / Georgia Tech +840 | 36.8 – 18.3 | 21–52 / 7–31 | Wake Forest -18.4 / – | 55.1 / – | no line yet | no line yet (fair: Wake Forest -840) | no line yet |  |
| Sat 11/21 TBA | Iowa @ Illinois | Iowa 27, Illinois 24 | Iowa 63% | Iowa -170 / Illinois +170 | 27.8 – 22.9 | 14–42 / 10–37 | Iowa -4.8 / – | 50.7 / – | no line yet | no line yet (fair: Iowa -170) | no line yet |  |
| Sat 11/21 TBA | UCLA @ Michigan | UCLA 24, Michigan 21 | UCLA 53% | UCLA -115 / Michigan +115 | 22.1 – 21.1 | 10–35 / 9–34 | UCLA -1.0 / – | 43.2 / – | no line yet | no line yet (fair: UCLA -115) | no line yet |  |
| Sat 11/21 TBA | Northwestern @ Minnesota | Northwestern 24, Minnesota 21 | Northwestern 64% | Northwestern -180 / Minnesota +180 | 26.3 – 21.0 | 13–41 / 9–34 | Northwestern -5.4 / – | 47.3 / – | no line yet | no line yet (fair: Northwestern -180) | no line yet |  |
| Sat 11/21 TBA | Ohio State @ Nebraska | Ohio State 31, Nebraska 21 | Ohio State 80% | Ohio State -390 / Nebraska +390 | 30.9 – 19.0 | 17–45 / 7–31 | Ohio State -11.9 / – | 49.9 / – | no line yet | no line yet (fair: Ohio State -390) | no line yet |  |
| Sat 11/21 TBA | Rutgers @ Penn State | Rutgers 17, Penn State 34 | Penn State 88% | Rutgers +755 / Penn State -755 | 17.4 – 35.0 | 6–30 / 20–51 | Penn State -17.5 / – | 52.4 / – | no line yet | no line yet (fair: Penn State -755) | no line yet |  |
| Sat 11/21 TBA | Wisconsin @ Purdue | Wisconsin 27, Purdue 20 | Wisconsin 67% | Wisconsin -200 / Purdue +200 | 27.5 – 21.1 | 14–42 / 7–34 | Wisconsin -6.3 / – | 48.6 / – | no line yet | no line yet (fair: Wisconsin -200) | no line yet |  |
| Sat 11/21 TBA | Maryland @ USC | Maryland 21, USC 35 | USC 82% | Maryland +450 / USC -450 | 20.9 – 34.4 | 7–34 / 20–49 | USC -13.5 / – | 55.3 / – | no line yet | no line yet (fair: USC -450) | no line yet |  |
| Sat 11/21 TBA | Indiana @ Washington | Indiana 27, Washington 17 | Indiana 77% | Indiana -335 / Washington +335 | 27.1 – 16.6 | 13–42 / 6–28 | Indiana -10.4 / – | 43.7 / – | no line yet | no line yet (fair: Indiana -335) | no line yet |  |
| Sat 11/21 TBA | Charlotte @ Tulsa | Charlotte 17, Tulsa 38 | Tulsa 93% | Charlotte +1290 / Tulsa -1290 | 16.7 – 38.5 | 6–28 / 24–55 | Tulsa -21.7 / – | 55.2 / – | no line yet | no line yet (fair: Tulsa -1290) | no line yet |  |
| Sat 11/21 TBA | South Florida @ Florida Atlantic | South Florida 28, Florida Atlantic 31 | Florida Atlantic 56% | South Florida +130 / Florida Atlantic -130 | 29.7 – 31.8 | 16–44 / 17–47 | Florida Atlantic -2.1 / – | 61.5 / – | no line yet | no line yet (fair: Florida Atlantic -130) | no line yet |  |
| Sat 11/21 TBA | North Texas @ Tulane | North Texas 34, Tulane 27 | North Texas 67% | North Texas -205 / Tulane +205 | 34.8 – 27.8 | 20–50 / 14–42 | North Texas -7.0 / – | 62.5 / – | no line yet | no line yet (fair: North Texas -205) | no line yet |  |
| Sat 11/21 TBA | UTSA @ UAB | UTSA 31, UAB 24 | UTSA 73% | UTSA -265 / UAB +265 | 31.9 – 23.1 | 17–47 / 10–37 | UTSA -8.7 / – | 55.0 / – | no line yet | no line yet (fair: UTSA -265) | no line yet |  |
| Sat 11/21 TBA | Hawai'i @ Nevada | Hawai'i 27, Nevada 24 | Hawai'i 56% | Hawai'i -125 / Nevada +125 | 25.2 – 23.2 | 13–39 / 10–37 | Hawai'i -2.0 / – | 48.5 / – | no line yet | no line yet (fair: Hawai'i -125) | no line yet |  |
| Sat 11/21 TBA | UL Monroe @ App State | UL Monroe 21, App State 31 | App State 75% | UL Monroe +305 / App State -305 | 21.9 – 32.1 | 9–35 / 17–48 | App State -10.2 / – | 54.0 / – | no line yet | no line yet (fair: App State -305) | no line yet |  |
| Sat 11/21 TBA | Arkansas State @ Louisiana Tech | Arkansas State 21, Louisiana Tech 31 | Louisiana Tech 76% | Arkansas State +315 / Louisiana Tech -315 | 20.2 – 30.6 | 7–34 / 16–45 | Louisiana Tech -10.4 / – | 50.8 / – | no line yet | no line yet (fair: Louisiana Tech -315) | no line yet |  |
| Sat 11/21 TBA | Coastal Carolina @ Louisiana | Coastal Carolina 24, Louisiana 27 | Louisiana 64% | Coastal Carolina +180 / Louisiana -180 | 22.7 – 28.0 | 10–36 / 14–42 | Louisiana -5.3 / – | 50.7 / – | no line yet | no line yet (fair: Louisiana -180) | no line yet |  |
| Sat 11/21 TBA | Georgia Southern @ Troy | Georgia Southern 27, Troy 24 | Georgia Southern 54% | Georgia Southern -115 / Troy +115 | 26.1 – 24.8 | 13–41 / 10–38 | Georgia Southern -1.3 / – | 50.9 / – | no line yet | no line yet (fair: Georgia Southern -115) | no line yet |  |
| Sat 11/21 TBA | Georgia State @ Marshall | Georgia State 28, Marshall 31 | Marshall 60% | Georgia State +150 / Marshall -150 | 27.5 – 31.3 | 14–42 / 17–46 | Marshall -3.8 / – | 58.8 / – | no line yet | no line yet (fair: Marshall -150) | no line yet |  |
| Sat 11/21 TBA | South Alabama @ Southern Miss | South Alabama 31, Southern Miss 28 | South Alabama 56% | South Alabama -125 / Southern Miss +125 | 31.3 – 29.0 | 17–46 / 14–44 | South Alabama -2.3 / – | 60.3 / – | no line yet | no line yet (fair: South Alabama -125) | no line yet |  |
| Sat 11/21 12:00 PM | Wofford @ Ole Miss | Wofford 3, Ole Miss 59 | Ole Miss 100% | Wofford +9900 / Ole Miss -9900 | 3.0 – 59.5 | 0–7 / 45–74 | Ole Miss -56.5 / – | 62.5 / – | no line yet | no line yet (fair: Ole Miss -9900) | no line yet | FCS opponent |
| Sat 11/21 12:00 PM | East Carolina @ Army | East Carolina 24, Army 27 | Army 57% | East Carolina +135 / Army -135 | 25.9 – 28.9 | 13–41 / 14–43 | Army -3.0 / – | 54.7 / – | no line yet | no line yet (fair: Army -135) | no line yet |  |
| Sat 11/21 12:00 PM | Memphis @ Navy | Memphis 31, Navy 28 | Memphis 51% | Memphis -105 / Navy +105 | 29.6 – 29.0 | 15–44 / 14–44 | Memphis -0.5 / – | 58.6 / – | no line yet | no line yet (fair: Memphis -105) | no line yet |  |
| Sat 11/21 1:00 PM | Tennessee Tech @ Mississippi State | Tennessee Tech 10, Mississippi State 42 | Mississippi State 99% | Tennessee Tech +9900 / Mississippi State -9900 | 10.1 – 42.6 | 0–20 / 28–59 | Mississippi State -32.5 / – | 52.7 / – | no line yet | no line yet (fair: Mississippi State -9900) | no line yet | FCS opponent |
| Sat 11/21 1:00 PM | Western Kentucky @ Liberty | Western Kentucky 17, Liberty 34 | Liberty 87% | Western Kentucky +660 / Liberty -660 | 17.4 – 33.6 | 6–30 / 19–49 | Liberty -16.2 / – | 50.9 / – | no line yet | no line yet (fair: Liberty -660) | no line yet |  |
| Sat 11/21 2:00 PM | Chattanooga @ Alabama | Chattanooga 0, Alabama 52 | Alabama 100% | Chattanooga +9900 / Alabama -9900 | 3.0 – 53.5 | 0–7 / 38–69 | Alabama -50.5 / – | 56.5 / – | no line yet | no line yet (fair: Alabama -9900) | no line yet | FCS opponent |
| Sat 11/21 2:00 PM | Missouri State @ Jacksonville State | Missouri State 24, Jacksonville State 34 | Jacksonville State 79% | Missouri State +375 / Jacksonville State -375 | 22.0 – 34.0 | 10–35 / 20–49 | Jacksonville State -12.0 / – | 56.1 / – | no line yet | no line yet (fair: Jacksonville State -375) | no line yet |  |
| Sat 11/21 2:00 PM | Middle Tennessee @ Sam Houston | Middle Tennessee 24, Sam Houston 21 | Middle Tennessee 50% | Middle Tennessee -100 / Sam Houston +100 | 21.8 – 21.4 | 10–35 / 10–35 | Middle Tennessee -0.4 / – | 43.3 / – | no line yet | no line yet (fair: Middle Tennessee -100) | no line yet |  |
| Sat 11/21 3:00 PM | Delaware @ New Mexico State | Delaware 31, New Mexico State 24 | Delaware 72% | Delaware -255 / New Mexico State +255 | 31.0 – 22.3 | 17–45 / 10–35 | Delaware -8.7 / – | 53.3 / – | no line yet | no line yet (fair: Delaware -255) | no line yet |  |
| Sat 11/21 3:00 PM | Florida International @ Kennesaw State | Florida International 21, Kennesaw State 24 | Kennesaw State 65% | Florida International +180 / Kennesaw State -180 | 20.8 – 26.2 | 8–34 / 13–41 | Kennesaw State -5.4 / – | 47.1 / – | no line yet | no line yet (fair: Kennesaw State -180) | no line yet |  |
| Sat 11/21 3:30 PM | Samford @ Auburn | Samford 0, Auburn 45 | Auburn 100% | Samford +9900 / Auburn -9900 | 3.0 – 47.4 | 0–7 / 33–63 | Auburn -44.4 / – | 50.4 / – | no line yet | no line yet (fair: Auburn -9900) | no line yet | FCS opponent |
| Sat 11/21 3:30 PM | Old Dominion @ UConn | Old Dominion 17, UConn 31 | UConn 83% | Old Dominion +490 / UConn -490 | 16.6 – 30.5 | 6–28 / 16–45 | UConn -13.9 / – | 47.1 / – | no line yet | no line yet (fair: UConn -490) | no line yet |  |
| Sat 11/21 4:00 PM | Northern Illinois @ North Dakota State | Northern Illinois 13, North Dakota State 34 | North Dakota State 94% | Northern Illinois +1480 / North Dakota State -1480 | 13.4 – 34.7 | 3–24 / 20–50 | North Dakota State -21.3 / – | 48.1 / – | no line yet | no line yet (fair: North Dakota State -1480) | no line yet |  |
| Sat 11/21 6:00 PM | Washington State @ Texas State | Washington State 24, Texas State 34 | Texas State 74% | Washington State +280 / Texas State -280 | 24.6 – 34.3 | 12–38 / 20–49 | Texas State -9.7 / – | 58.9 / – | no line yet | no line yet (fair: Texas State -280) | no line yet |  |
| Sat 11/21 7:00 PM | UNLV @ San José State | UNLV 28, San José State 21 | UNLV 72% | UNLV -265 / San José State +265 | 29.8 – 21.2 | 16–45 / 9–34 | UNLV -8.6 / – | 50.9 / – | no line yet | no line yet (fair: UNLV -265) | no line yet |  |
| Sat 11/21 7:30 PM | SMU @ Notre Dame | SMU 17, Notre Dame 34 | Notre Dame 88% | SMU +705 / Notre Dame -705 | 19.3 – 36.5 | 7–32 / 21–52 | Notre Dame -13.8 / Notre Dame -17.5 | 52.7 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | Colorado State @ Fresno State | Colorado State 24, Fresno State 34 | Fresno State 78% | Colorado State +360 / Fresno State -360 | 23.8 – 35.5 | 10–38 / 21–51 | Fresno State -11.7 / – | 59.3 / – | no line yet | no line yet (fair: Fresno State -360) | no line yet |  |
| Sat 11/21 9:30 PM | San Diego State @ Boise State | San Diego State 17, Boise State 34 | Boise State 87% | San Diego State +665 / Boise State -665 | 19.3 – 35.7 | 7–31 / 21–51 | Boise State -16.5 / – | 55.0 / – | no line yet | no line yet (fair: Boise State -665) | no line yet |  |
| Sat 11/21 10:30 PM | Utah State @ Oregon State | Utah State 21, Oregon State 35 | Oregon State 80% | Utah State +405 / Oregon State -405 | 20.8 – 33.3 | 7–34 / 19–49 | Oregon State -12.5 / – | 54.0 / – | no line yet | no line yet (fair: Oregon State -405) | no line yet |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 655 | 11.75 | 12.21 | 8.46 | 79.7% | 0.142 | 81.9% |
| Model only (before blending) | 655 | 12.50 | 12.53 | 8.74 | 76.9% | – | – |
| Betting line when predicted | 653 | 11.73 | 12.17 | 8.45 | 79.8% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin of an FBS game by about 12.5 points.

501 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 8 | 1-7-0 | 2.7 | -0.68 | -25.4% | +4.6% |
| Total | 3 | 1-2-0 | 3.2 | -1.47 | -45.9% | +4.1% |

3 of these edges were priced at an assumed -110 (price not posted).

Every edge logged before kickoff at the stake and price logged with it (backfilled games, and edges logged before edges were priced from the final prediction, are not included). Units are 1% of the bankroll; ROI is units won per unit staked, pushes returning the stake, and expected ROI is what the edges' EVs promised.

### Week 10 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| Ohio @ Akron | 31–17 | 28–20 | 84% | yes |
| Buffalo @ Miami (OH) | 17–24 | 34–31 | 32% | no |
| Ball State @ Massachusetts | 24–27 | 30–31 | 57% | yes |
| Toledo @ Sacramento State | 38–14 | 20–17 | 96% | no |
| Central Michigan vs Eastern Michigan | 21–24 | 35–7 | 47% | no |
| UTSA @ Florida Atlantic | 38–31 | 29–60 | 35% | no |
| James Madison @ Southern Miss | 34–21 | 54–23 | 82% | no |
| Virginia Tech @ SMU | 24–31 | 28–51 | 67% | no |
| South Florida @ East Carolina | 17–20 | 17–20 | 55% | yes |
| Nebraska @ Illinois | 27–24 | 13–24 | 39% | no |
| New Mexico @ Nevada | 24–17 | 31–3 | 78% | yes |
| TCU @ Arizona | 21–28 | 28–29 | 70% | yes |
| Texas @ Missouri | 20–17 | 34–20 | 56% | yes |
| BYU @ Utah | 24–27 | 20–28 | 63% | yes |
| Iowa State @ Baylor | 21–28 | 31–42 | 75% | yes |
| Clemson @ Syracuse | 27–24 | 18–13 | 56% | yes |
| Florida State @ Boston College | 31–24 | 31–24 | 67% | yes |
| North Carolina @ UConn | 31–24 | 38–21 | 67% | yes |
| UCLA @ Minnesota | 24–17 | 34–20 | 64% | yes |
| Tulsa @ Tulane | 27–24 | 60–10 | 55% | no |
| Duke @ NC State | 27–24 | 41–3 | 61% | no |
| Maryland @ Purdue | 24–31 | 34–29 | 37% | yes |
| Arkansas @ Auburn | 21–31 | 23–26 | 77% | yes |
| Oklahoma State @ Kansas State | 34–31 | 66–28 | 64% | no |
| Old Dominion @ Coastal Carolina | 17–24 | 21–8 | 33% | no |
| Georgia State @ App State | 24–31 | 39–23 | 34% | no |
| Texas A&M @ South Carolina | 24–31 | 9–17 | 67% | no |
| UL Monroe @ Arkansas State | 20–34 | 19–17 | 17% | no |
| Delaware @ Kennesaw State | 27–24 | 40–42 | 49% | yes |
| Penn State @ Washington | 21–24 | 28–25 | 44% | yes |
| Charlotte @ UAB | 20–27 | 12–23 | 74% | yes |
| Temple @ Navy | 24–31 | 35–42 | 69% | yes |
| Marshall @ Georgia Southern | 24–31 | 13–49 | 68% | no |

## FBS power ratings

Points per game better than an average FBS team on a neutral field, from opponent-adjusted EPA (garbage time removed) with this season's games weighted against a preseason prior, plus the weight the margin model puts on Elo (a rating built from game results alone). Defense is positive when it holds opponents below average.

| # | Team | Conference | Net | Offense | Defense | Special teams | Results (Elo) | Elo rating |
|---|---|---|---|---|---|---|---|---|
| 1 | LSU | SEC | +26.3 | +10.8 | +12.5 | +0.2 | +2.9 | 1751 |
| 2 | Ohio State | Big Ten | +25.8 | +10.9 | +10.4 | +0.3 | +4.3 | 1868 |
| 3 | Georgia | SEC | +23.8 | +7.9 | +10.7 | +0.8 | +4.4 | 1880 |
| 4 | Notre Dame | FBS Independents | +23.0 | +8.8 | +9.1 | +1.0 | +4.1 | 1858 |
| 5 | Miami | ACC | +23.0 | +14.2 | +3.9 | +0.3 | +4.6 | 1894 |
| 6 | Indiana | Big Ten | +21.5 | +5.6 | +10.6 | +0.2 | +5.1 | 1939 |
| 7 | Utah | Big 12 | +20.3 | +10.3 | +6.0 | -0.1 | +4.2 | 1862 |
| 8 | Texas | SEC | +19.9 | +2.4 | +12.7 | +0.8 | +4.0 | 1848 |
| 9 | Alabama | SEC | +19.6 | +9.0 | +7.2 | +0.2 | +3.2 | 1777 |
| 10 | Ole Miss | SEC | +18.4 | +10.4 | +3.8 | +0.7 | +3.6 | 1815 |
| 11 | Texas Tech | Big 12 | +18.2 | +2.1 | +11.9 | +1.2 | +3.0 | 1761 |
| 12 | UCLA | Big Ten | +17.5 | +5.4 | +8.9 | +0.8 | +2.4 | 1709 |
| 13 | Oregon | Big Ten | +16.8 | +4.5 | +9.1 | +0.4 | +2.8 | 1743 |
| 14 | Wake Forest | ACC | +15.8 | +5.9 | +7.2 | +0.4 | +2.4 | 1710 |
| 15 | Tennessee | SEC | +15.8 | +3.7 | +8.5 | +1.0 | +2.5 | 1723 |
| 16 | Louisville | ACC | +14.9 | +9.3 | +3.5 | +0.1 | +2.0 | 1681 |
| 17 | Michigan | Big Ten | +14.8 | +3.5 | +9.3 | +0.0 | +2.0 | 1674 |
| 18 | Missouri | SEC | +14.6 | +4.3 | +7.9 | +0.4 | +2.0 | 1680 |
| 19 | Oklahoma | SEC | +14.6 | +0.3 | +12.4 | +0.6 | +1.3 | 1615 |
| 20 | USC | Big Ten | +13.9 | +10.6 | +0.3 | +0.3 | +2.7 | 1738 |
| 21 | SMU | ACC | +13.8 | +8.0 | +3.2 | +0.3 | +2.3 | 1700 |
| 22 | BYU | Big 12 | +13.3 | +5.3 | +4.5 | +0.7 | +2.7 | 1739 |
| 23 | Iowa | Big Ten | +13.0 | +1.5 | +7.8 | +0.8 | +2.9 | 1751 |
| 24 | Florida | SEC | +12.6 | +6.5 | +4.4 | +0.9 | +0.8 | 1579 |
| 25 | South Carolina | SEC | +12.3 | +5.7 | +4.0 | +0.6 | +2.1 | 1683 |
| 26 | Arizona | Big 12 | +12.0 | +6.1 | +3.4 | +0.1 | +2.4 | 1713 |
| 27 | Penn State | Big Ten | +11.7 | +3.0 | +7.1 | +0.1 | +1.6 | 1640 |
| 28 | Auburn | SEC | +11.7 | +5.0 | +5.6 | +0.6 | +0.5 | 1550 |
| 29 | Nebraska | Big Ten | +11.5 | +3.4 | +7.2 | +0.3 | +0.6 | 1558 |
| 30 | Texas A&M | SEC | +11.3 | +2.4 | +7.7 | +0.4 | +0.8 | 1579 |
| 31 | Northwestern | Big Ten | +11.1 | +7.0 | +1.8 | +0.8 | +1.5 | 1634 |
| 32 | Houston | Big 12 | +10.2 | +7.9 | +0.2 | +0.2 | +1.9 | 1673 |
| 33 | Oklahoma State | Big 12 | +9.8 | +9.3 | -0.5 | +0.5 | +0.6 | 1556 |
| 34 | Kentucky | SEC | +9.6 | +2.8 | +4.5 | +0.3 | +2.0 | 1677 |
| 35 | Baylor | Big 12 | +9.5 | +0.8 | +6.3 | +0.9 | +1.4 | 1628 |
| 36 | Mississippi State | SEC | +9.4 | +5.7 | +3.4 | +0.2 | +0.0 | 1512 |
| 37 | Duke | ACC | +8.8 | +3.7 | +1.9 | +0.7 | +2.5 | 1716 |
| 38 | Washington | Big Ten | +8.8 | +1.8 | +5.3 | +0.0 | +1.6 | 1642 |
| 39 | Wisconsin | Big Ten | +8.2 | -0.2 | +7.0 | +0.3 | +1.0 | 1593 |
| 40 | Kansas | Big 12 | +7.0 | +4.5 | +3.3 | -0.1 | -0.8 | 1439 |
| 41 | Iowa State | Big 12 | +6.8 | +4.7 | +0.7 | +1.0 | +0.3 | 1536 |
| 42 | Kansas State | Big 12 | +6.5 | +4.6 | +2.2 | +0.2 | -0.6 | 1454 |
| 43 | Illinois | Big Ten | +6.3 | +6.8 | -2.2 | +0.2 | +1.5 | 1638 |
| 44 | Boise State | Pac-12 | +6.3 | +4.8 | -0.9 | -0.1 | +2.5 | 1721 |
| 45 | Cincinnati | Big 12 | +6.2 | +9.0 | -3.8 | +0.3 | +0.7 | 1568 |
| 46 | Clemson | ACC | +5.6 | -4.8 | +8.3 | +0.7 | +1.4 | 1627 |
| 47 | TCU | Big 12 | +5.4 | -2.0 | +6.4 | +0.1 | +0.9 | 1582 |
| 48 | Arizona State | Big 12 | +5.3 | +1.0 | +3.8 | +0.0 | +0.5 | 1550 |
| 49 | Florida State | ACC | +5.2 | +7.4 | -1.4 | -0.7 | -0.1 | 1499 |
| 50 | Virginia Tech | ACC | +4.5 | +4.0 | -0.0 | +0.1 | +0.4 | 1541 |
| 51 | Vanderbilt | SEC | +4.4 | +4.6 | -0.6 | +0.2 | +0.2 | 1529 |
| 52 | Pittsburgh | ACC | +4.0 | -1.2 | +4.0 | +0.6 | +0.7 | 1566 |
| 53 | North Carolina | ACC | +3.7 | +3.5 | -1.0 | +0.7 | +0.5 | 1554 |
| 54 | North Texas | American Athletic | +3.5 | +10.1 | -7.4 | -0.9 | +1.6 | 1645 |
| 55 | James Madison | Sun Belt | +3.2 | -1.1 | +1.5 | +0.4 | +2.4 | 1711 |
| 56 | Minnesota | Big Ten | +3.2 | -3.6 | +5.6 | +0.9 | +0.2 | 1529 |
| 57 | UCF | Big 12 | +3.1 | +0.8 | +2.9 | +0.0 | -0.6 | 1459 |
| 58 | Colorado | Big 12 | +3.0 | +0.6 | +4.6 | -0.7 | -1.5 | 1378 |
| 59 | Maryland | Big Ten | +2.3 | -0.1 | +3.2 | +0.8 | -1.6 | 1374 |
| 60 | Memphis | American Athletic | +1.9 | +3.5 | -2.4 | -0.4 | +1.2 | 1614 |
| 61 | Oregon State | Pac-12 | +1.8 | +4.5 | -2.3 | +0.1 | -0.5 | 1468 |
| 62 | Syracuse | ACC | +1.5 | +1.1 | +2.6 | -0.8 | -1.4 | 1392 |
| 63 | NC State | ACC | +1.5 | +4.9 | -2.9 | -0.4 | -0.1 | 1498 |
| 64 | Virginia | ACC | +1.2 | -1.3 | +3.1 | -0.5 | -0.2 | 1494 |
| 65 | UTSA | American Athletic | +1.1 | +3.8 | -3.6 | -0.0 | +1.0 | 1596 |
| 66 | Arkansas | SEC | +0.8 | +1.4 | +0.8 | -0.7 | -0.6 | 1455 |
| 67 | Liberty | Conference USA | +0.8 | +0.6 | -0.7 | +0.3 | +0.5 | 1551 |
| 68 | New Mexico | Mountain West | +0.2 | -4.1 | +3.0 | -0.2 | +1.5 | 1636 |
| 69 | West Virginia | Big 12 | +0.1 | +4.0 | -4.5 | +0.6 | -0.1 | 1502 |
| 70 | Texas State | Pac-12 | -0.2 | +5.7 | -5.3 | -1.2 | +0.6 | 1563 |
| 71 | Toledo | Mid-American | -0.7 | -2.4 | +1.4 | -0.3 | +0.6 | 1559 |
| 72 | Navy | American Athletic | -1.0 | +3.6 | -3.8 | -0.5 | -0.3 | 1484 |
| 73 | Tulsa | American Athletic | -1.0 | +0.1 | -0.0 | -0.6 | -0.5 | 1466 |
| 74 | Purdue | Big Ten | -1.1 | +2.8 | -3.1 | +0.7 | -1.4 | 1386 |
| 75 | North Dakota State | Mountain West | -1.5 | -4.9 | +3.4 | +1.1 | -1.1 | 1419 |
| 76 | South Florida | American Athletic | -1.8 | -2.4 | -0.2 | +0.1 | +0.7 | 1569 |
| 77 | Florida Atlantic | American Athletic | -2.8 | +4.7 | -8.1 | +0.7 | -0.0 | 1506 |
| 78 | Fresno State | Pac-12 | -2.8 | -2.3 | -1.0 | -0.2 | +0.8 | 1574 |
| 79 | Louisiana Tech | Sun Belt | -2.9 | -3.1 | +0.6 | -0.8 | +0.4 | 1540 |
| 80 | Army | American Athletic | -3.0 | +5.2 | -8.6 | -0.1 | +0.5 | 1554 |
| 81 | East Carolina | American Athletic | -3.0 | -5.3 | +2.7 | -0.5 | +0.1 | 1520 |
| 82 | UConn | FBS Independents | -3.3 | +1.3 | -3.6 | -0.1 | -1.0 | 1427 |
| 83 | Michigan State | Big Ten | -3.5 | -3.5 | +1.1 | +0.3 | -1.4 | 1388 |
| 84 | Ohio | Mid-American | -3.7 | -1.9 | -2.9 | +0.2 | +0.9 | 1586 |
| 85 | Rutgers | Big Ten | -4.0 | +2.8 | -6.2 | +0.8 | -1.4 | 1388 |
| 86 | Georgia Tech | ACC | -4.5 | +1.2 | -4.2 | -0.1 | -1.4 | 1393 |
| 87 | Jacksonville State | Conference USA | -4.9 | -0.2 | -4.4 | -0.1 | -0.1 | 1497 |
| 88 | Air Force | Mountain West | -5.0 | +2.4 | -6.9 | -0.2 | -0.2 | 1488 |
| 89 | UNLV | Mountain West | -5.1 | -2.6 | -3.0 | +0.2 | +0.4 | 1543 |
| 90 | Boston College | ACC | -5.4 | -3.5 | -0.4 | -0.6 | -0.9 | 1431 |
| 91 | California | ACC | -6.0 | -2.2 | -1.8 | -0.4 | -1.7 | 1369 |
| 92 | Delaware | Conference USA | -6.6 | -0.2 | -5.3 | +0.3 | -1.4 | 1389 |
| 93 | Utah State | Pac-12 | -6.9 | -6.6 | +2.0 | -1.2 | -1.1 | 1412 |
| 94 | Western Michigan | Mid-American | -7.0 | -4.8 | -3.6 | +0.8 | +0.6 | 1561 |
| 95 | Tulane | American Athletic | -7.1 | -4.2 | -2.5 | +0.2 | -0.6 | 1454 |
| 96 | Georgia Southern | Sun Belt | -7.6 | -2.0 | -5.3 | -0.9 | +0.6 | 1556 |
| 97 | Marshall | Sun Belt | -7.7 | -3.4 | -3.8 | +0.1 | -0.6 | 1456 |
| 98 | San Diego State | Pac-12 | -8.1 | -4.6 | -2.6 | +0.3 | -1.2 | 1406 |
| 99 | Washington State | Pac-12 | -8.2 | -6.0 | -0.0 | -0.3 | -1.9 | 1349 |
| 100 | Stanford | ACC | -8.7 | -2.7 | -5.2 | -0.1 | -0.7 | 1448 |
| 101 | Georgia State | Sun Belt | -8.9 | -0.5 | -7.2 | -0.0 | -1.2 | 1407 |
| 102 | Miami (OH) | Mid-American | -9.3 | -4.8 | -4.1 | +0.7 | -1.0 | 1421 |
| 103 | Louisiana | Sun Belt | -9.6 | -5.0 | -4.1 | -0.1 | -0.4 | 1478 |
| 104 | UAB | American Athletic | -9.7 | -5.7 | -2.5 | -0.4 | -1.1 | 1419 |
| 105 | Temple | American Athletic | -9.8 | +0.6 | -7.2 | -0.5 | -2.7 | 1279 |
| 106 | App State | Sun Belt | -9.9 | -3.9 | -3.8 | -0.5 | -1.7 | 1361 |
| 107 | Hawai'i | Mountain West | -10.9 | -4.0 | -6.2 | +1.0 | -1.7 | 1365 |
| 108 | Troy | Sun Belt | -11.0 | -8.0 | -0.4 | -1.3 | -1.3 | 1401 |
| 109 | Wyoming | Mountain West | -11.0 | -6.4 | -3.2 | -0.2 | -1.1 | 1413 |
| 110 | Central Michigan | Mid-American | -11.6 | -6.2 | -4.3 | -0.1 | -1.1 | 1418 |
| 111 | Arkansas State | Sun Belt | -11.7 | -3.1 | -7.4 | +0.0 | -1.2 | 1408 |
| 112 | Old Dominion | Sun Belt | -11.9 | -13.9 | +4.8 | -1.6 | -1.2 | 1407 |
| 113 | South Alabama | Sun Belt | -11.9 | -0.3 | -10.5 | +0.3 | -1.3 | 1398 |
| 114 | Colorado State | Pac-12 | -11.9 | +3.0 | -12.0 | -0.3 | -2.6 | 1286 |
| 115 | Western Kentucky | Conference USA | -12.3 | -6.8 | -3.3 | -0.3 | -1.9 | 1345 |
| 116 | Kennesaw State | Conference USA | -12.7 | -6.6 | -3.6 | -0.8 | -1.7 | 1363 |
| 117 | Rice | American Athletic | -12.7 | -3.7 | -5.1 | -0.8 | -3.1 | 1246 |
| 118 | Coastal Carolina | Sun Belt | -13.0 | -7.5 | -3.9 | +0.4 | -2.1 | 1334 |
| 119 | Missouri State | Conference USA | -13.1 | -1.6 | -7.4 | -1.4 | -2.7 | 1281 |
| 120 | Nevada | Mountain West | -14.7 | -10.9 | -1.8 | +0.3 | -2.4 | 1309 |
| 121 | Florida International | Conference USA | -15.1 | -10.1 | -1.8 | -1.3 | -1.8 | 1353 |
| 122 | Southern Miss | Sun Belt | -15.2 | -8.0 | -3.8 | -1.2 | -2.3 | 1318 |
| 123 | New Mexico State | Conference USA | -15.7 | -8.5 | -2.7 | -1.8 | -2.8 | 1275 |
| 124 | San José State | Mountain West | -15.9 | -9.8 | -3.5 | -0.1 | -2.4 | 1303 |
| 125 | UL Monroe | Sun Belt | -16.8 | -5.8 | -6.0 | -1.3 | -3.6 | 1201 |
| 126 | Buffalo | Mid-American | -16.8 | -11.5 | -5.3 | +0.4 | -0.5 | 1469 |
| 127 | Massachusetts | Mid-American | -17.1 | -9.1 | -4.4 | -0.3 | -3.3 | 1229 |
| 128 | Ball State | Mid-American | -17.2 | -5.8 | -7.7 | -0.6 | -3.2 | 1241 |
| 129 | Middle Tennessee | Conference USA | -17.4 | -7.1 | -7.4 | +0.1 | -3.0 | 1257 |
| 130 | Northern Illinois | Mountain West | -18.3 | -3.7 | -9.2 | -1.0 | -4.3 | 1145 |
| 131 | Bowling Green | Mid-American | -18.6 | -11.7 | -4.1 | -0.0 | -2.8 | 1270 |
| 132 | Sam Houston | Conference USA | -18.9 | -12.5 | -0.8 | -1.3 | -4.3 | 1145 |
| 133 | Eastern Michigan | Mid-American | -19.1 | -7.9 | -7.9 | -0.7 | -2.6 | 1287 |
| 134 | Sacramento State | Mid-American | -20.4 | -11.9 | -4.4 | +0.3 | -4.3 | 1147 |
| 135 | Charlotte | American Athletic | -20.4 | -7.0 | -9.2 | -0.5 | -3.8 | 1190 |
| 136 | Kent State | Mid-American | -20.8 | -10.7 | -6.1 | -0.8 | -3.2 | 1241 |
| 137 | Akron | Mid-American | -22.7 | -10.3 | -8.0 | -0.7 | -3.7 | 1198 |
| 138 | UTEP | Mountain West | -24.0 | -11.6 | -6.5 | -1.2 | -4.7 | 1112 |

## Current model fit

- Fitted on 4272 games from seasons 2022–2026.
- Home field on top of the ratings: 3.2 points (1.9 in conference games).
- Extra FBS edge over FCS opponents beyond their ratings: 14.1 points.
- Elo weight: 0.19 points of margin per point of Elo spread.
- Weight on the betting line: 91% for the margin, 81% for the total.
