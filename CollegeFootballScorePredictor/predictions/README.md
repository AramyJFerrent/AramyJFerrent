# College football score predictions

Updated Sat Nov 07, 2026 08:24 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 10

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sat 11/07 9:30 PM | West Virginia @ Texas Tech | West Virginia 24, Texas Tech 41 | Texas Tech 86% | West Virginia +635 / Texas Tech -635 | 23.9 – 40.8 | 10–38 / 25–57 | Texas Tech -21.2 / Texas Tech -16.5 | 56.9 / 66.5 | no edge | no edge | no edge |  |
| Sat 11/07 9:30 PM | Fresno State @ Utah State | Fresno State 24, Utah State 21 | Utah State 51% | Fresno State +100 / Utah State -100 | 22.0 – 22.0 | 10–35 / 10–35 | Fresno State -2.7 / Utah State -0.2 | 46.8 / 43.2 | no edge | no edge | no edge |  |
| Sat 11/07 9:30 PM | Hawai'i @ UTEP | Hawai'i 28, UTEP 21 | Hawai'i 71% | Hawai'i -245 / UTEP +245 | 28.5 – 20.5 | 14–43 / 7–34 | Hawai'i -12.9 / Hawai'i -7.5 | 50.2 / 48.8 | no edge | no edge | no edge |  |
| Sat 11/07 10:30 PM | Texas State @ Oregon State | Texas State 31, Oregon State 38 | Oregon State 64% | Texas State +175 / Oregon State -175 | 32.7 – 38.2 | 17–48 / 23–53 | Oregon State -5.7 / Oregon State -5.5 | 68.1 / 71.5 | no edge | no edge | no edge |  |
| Sat 11/07 10:30 PM | Wyoming @ UNLV | Wyoming 24, UNLV 27 | UNLV 61% | Wyoming +155 / UNLV -155 | 22.5 – 26.7 | 10–36 / 13–41 | UNLV -8.7 / UNLV -3.8 | 49.9 / 49.0 | no edge | no edge | no edge |  |

## 2026 Week 11

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/10 7:00 PM | Western Michigan @ Akron | Western Michigan 31, Akron 17 | Western Michigan 83% | Western Michigan -485 / Akron +485 | 30.8 – 17.2 | 17–45 / 6–30 | Western Michigan -14.8 / Western Michigan -13.5 | 49.8 / 47.5 | no edge | no edge | no edge |  |
| Tue 11/10 7:00 PM | Kent State @ Bowling Green | Kent State 17, Bowling Green 24 | Bowling Green 66% | Kent State +190 / Bowling Green -190 | 19.2 – 24.7 | 7–31 / 10–38 | Bowling Green -5.4 / Bowling Green -5.5 | 41.6 / 44.5 | no edge | no edge | no edge |  |
| Tue 11/10 8:00 PM | Ohio @ Miami (OH) | Ohio 21, Miami (OH) 24 | Miami (OH) 53% | Ohio +110 / Miami (OH) -110 | 23.3 – 24.4 | 10–37 / 10–38 | Ohio -2.7 / Miami (OH) -1.5 | 48.4 / 47.5 | no edge | no edge | no edge |  |
| Wed 11/11 TBA | Massachusetts @ Toledo | Massachusetts 17, Toledo 31 | Toledo 83% | Massachusetts +505 / Toledo -505 | 19.1 – 33.5 | 7–31 / 19–49 | Toledo -18.8 / Toledo -14.0 | 48.8 / 53.5 | no edge | no edge | no edge |  |
| Wed 11/11 7:30 PM | Buffalo @ Ball State | Buffalo 27, Ball State 24 | Buffalo 57% | Buffalo -135 / Ball State +135 | 27.2 – 24.6 | 14–42 / 10–38 | Ball State -1.2 / Buffalo -3.0 | 52.9 / 51.5 | no edge | no edge | no edge |  |
| Wed 11/11 7:30 PM | Sacramento State @ Central Michigan | Sacramento State 14, Central Michigan 31 | Central Michigan 86% | Sacramento State +615 / Central Michigan -615 | 14.8 – 29.9 | 3–27 / 15–45 | Central Michigan -10.9 / Central Michigan -15.5 | 45.8 / 44.5 | no edge | no edge | no edge |  |
| Thu 11/12 8:00 PM | Memphis @ South Florida | Memphis 27, South Florida 24 | Memphis 53% | Memphis -110 / South Florida +110 | 27.0 – 26.2 | 14–41 / 13–41 | Memphis -0.8 / – | 55.0 / – | no line yet | no line yet (fair: Memphis -110) | no line yet |  |
| Thu 11/12 9:00 PM | Louisiana @ UL Monroe | Louisiana 31, UL Monroe 24 | Louisiana 65% | Louisiana -185 / UL Monroe +185 | 29.3 – 23.4 | 14–45 / 10–37 | Louisiana -5.9 / – | 52.8 / – | no line yet | no line yet (fair: Louisiana -185) | no line yet |  |
| Fri 11/13 7:00 PM | Florida State @ Pittsburgh | Florida State 28, Pittsburgh 31 | Pittsburgh 56% | Florida State +130 / Pittsburgh -130 | 26.6 – 29.1 | 13–41 / 14–44 | Pittsburgh -2.5 / – | 55.6 / – | no line yet | no line yet (fair: Pittsburgh -130) | no line yet |  |
| Fri 11/13 9:00 PM | Illinois @ UCLA | Illinois 17, UCLA 27 | UCLA 75% | Illinois +305 / UCLA -305 | 19.3 – 29.2 | 7–32 / 14–44 | UCLA -14.2 / UCLA -9.5 | 52.6 / 47.5 | no edge | no edge | no edge |  |
| Fri 11/13 10:15 PM | Houston @ Colorado | Houston 31, Colorado 24 | Houston 64% | Houston -180 / Colorado +180 | 30.0 – 24.3 | 16–45 / 10–38 | Houston -5.7 / – | 54.3 / – | no line yet | no line yet (fair: Houston -180) | no line yet |  |
| Sat 11/14 TBA | Arizona State @ UCF | Arizona State 27, UCF 24 | UCF 51% | Arizona State +105 / UCF -105 | 24.7 – 25.0 | 12–38 / 12–38 | UCF -0.2 / – | 50.3 / – | no line yet | no line yet (fair: UCF -105) | no line yet |  |
| Sat 11/14 TBA | Baylor @ BYU | Baylor 20, BYU 27 | BYU 69% | Baylor +220 / BYU -220 | 20.7 – 27.7 | 7–34 / 14–42 | BYU -6.0 / BYU -7.0 | 52.1 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Cincinnati @ Iowa State | Cincinnati 31, Iowa State 34 | Iowa State 60% | Cincinnati +150 / Iowa State -150 | 28.5 – 32.2 | 14–42 / 17–48 | Iowa State -3.6 / – | 60.7 / – | no line yet | no line yet (fair: Iowa State -150) | no line yet |  |
| Sat 11/14 TBA | Kansas @ West Virginia | Kansas 31, West Virginia 28 | Kansas 60% | Kansas -145 / West Virginia +145 | 32.7 – 28.9 | 17–48 / 14–44 | Kansas -3.8 / – | 61.6 / – | no line yet | no line yet (fair: Kansas -145) | no line yet |  |
| Sat 11/14 TBA | Kansas State @ TCU | Kansas State 24, TCU 27 | TCU 52% | Kansas State +105 / TCU -105 | 23.5 – 24.8 | 10–37 / 12–38 | TCU -1.3 / – | 48.3 / – | no line yet | no line yet (fair: TCU -105) | no line yet |  |
| Sat 11/14 TBA | Texas Tech @ Oklahoma State | Texas Tech 34, Oklahoma State 31 | Texas Tech 55% | Texas Tech -120 / Oklahoma State +120 | 32.0 – 30.0 | 17–47 / 16–45 | Texas Tech -6.7 / Texas Tech -1.5 | 55.8 / 63.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Utah @ Arizona | Utah 27, Arizona 24 | Utah 54% | Utah -115 / Arizona +115 | 27.1 – 25.3 | 14–41 / 13–40 | Utah -5.6 / Utah -1.5 | 56.2 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Missouri @ Georgia | Missouri 17, Georgia 31 | Georgia 80% | Missouri +410 / Georgia -410 | 17.0 – 29.5 | 6–30 / 16–45 | Georgia -12.1 / Georgia -12.5 | 46.4 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Florida @ Kentucky | Florida 24, Kentucky 27 | Kentucky 54% | Florida +115 / Kentucky -115 | 26.7 – 28.0 | 13–41 / 14–42 | Florida -1.2 / Kentucky -1.5 | 51.7 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Texas @ LSU | Texas 21, LSU 24 | LSU 65% | Texas +190 / LSU -190 | 20.3 – 26.1 | 7–34 / 13–41 | LSU -8.3 / LSU -5.5 | 46.1 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Ole Miss @ Oklahoma | Ole Miss 24, Oklahoma 27 | Oklahoma 59% | Ole Miss +145 / Oklahoma -145 | 24.7 – 28.2 | 10–38 / 14–43 | Ole Miss -1.5 / Oklahoma -4.0 | 50.6 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Tennessee @ Texas A&M | Tennessee 24, Texas A&M 31 | Texas A&M 70% | Tennessee +230 / Texas A&M -230 | 23.0 – 30.6 | 10–37 / 17–45 | Tennessee -2.6 / Texas A&M -8.5 | 45.7 / 55.5 | no edge | Tennessee (+285): EV +5.1%, 27%, stake 0.4u | Under 55.5 (-110*): EV +5.6%, 55%, stake 1.5u | * price not posted; assumed -110 |
| Sat 11/14 TBA | Louisville @ North Carolina | Louisville 31, North Carolina 28 | Louisville 57% | Louisville -135 / North Carolina +135 | 31.0 – 28.0 | 17–45 / 14–42 | Louisville -8.2 / Louisville -2.5 | 57.1 / 59.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Stanford @ Virginia Tech | Stanford 21, Virginia Tech 38 | Virginia Tech 86% | Stanford +600 / Virginia Tech -600 | 20.0 – 35.8 | 7–33 / 21–52 | Virginia Tech -15.8 / – | 56.4 / – | no line yet | no line yet (fair: Virginia Tech -600) | no line yet |  |
| Sat 11/14 TBA | Purdue @ Iowa | Purdue 17, Iowa 34 | Iowa 88% | Purdue +715 / Iowa -715 | 16.3 – 32.9 | 6–28 / 17–49 | Iowa -16.6 / – | 49.2 / – | no line yet | no line yet (fair: Iowa -715) | no line yet |  |
| Sat 11/14 12:00 PM | Auburn @ Mississippi State | Auburn 31, Mississippi State 28 | Auburn 51% | Auburn -105 / Mississippi State +105 | 28.5 – 28.2 | 14–43 / 14–42 | Auburn -0.2 / – | 56.7 / – | no line yet | no line yet (fair: Auburn -105) | no line yet |  |
| Sat 11/14 12:00 PM | Duke @ Miami | Duke 17, Miami 38 | Miami 92% | Duke +1125 / Miami -1125 | 17.4 – 38.0 | 6–30 / 23–55 | Miami -16.3 / Miami -21.0 | 56.5 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/14 12:00 PM | Syracuse @ NC State | Syracuse 28, NC State 31 | NC State 57% | Syracuse +135 / NC State -135 | 26.9 – 29.7 | 13–41 / 16–45 | NC State -2.8 / – | 57.4 / – | no line yet | no line yet (fair: NC State -135) | no line yet |  |
| Sat 11/14 12:00 PM | Wake Forest @ SMU | Wake Forest 31, SMU 28 | Wake Forest 57% | Wake Forest -130 / SMU +130 | 29.4 – 26.7 | 16–44 / 13–41 | SMU -0.3 / Wake Forest -3.0 | 54.4 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/14 12:00 PM | Wisconsin @ Maryland | Wisconsin 24, Maryland 21 | Wisconsin 59% | Wisconsin -145 / Maryland +145 | 23.6 – 20.7 | 10–38 / 7–34 | Wisconsin -2.9 / – | 45.0 / – | no line yet | no line yet (fair: Wisconsin -145) | no line yet |  |
| Sat 11/14 12:00 PM | Northwestern @ Ohio State | Northwestern 21, Ohio State 31 | Ohio State 76% | Northwestern +320 / Ohio State -320 | 19.7 – 29.8 | 7–33 / 16–45 | Ohio State -16.7 / Ohio State -9.5 | 54.0 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/14 12:00 PM | James Madison @ UConn | James Madison 31, UConn 28 | James Madison 59% | James Madison -140 / UConn +140 | 29.7 – 26.5 | 16–45 / 13–41 | James Madison -3.2 / – | 56.2 / – | no line yet | no line yet (fair: James Madison -140) | no line yet |  |
| Sat 11/14 12:30 PM | Georgia Tech @ Clemson | Georgia Tech 17, Clemson 31 | Clemson 83% | Georgia Tech +485 / Clemson -485 | 17.8 – 31.2 | 7–31 / 17–46 | Clemson -13.4 / – | 49.5 / – | no line yet | no line yet (fair: Clemson -485) | no line yet |  |
| Sat 11/14 12:30 PM | Nebraska @ Rutgers | Nebraska 34, Rutgers 21 | Nebraska 80% | Nebraska -390 / Rutgers +390 | 33.5 – 20.9 | 18–49 / 7–34 | Nebraska -12.6 / – | 54.5 / – | no line yet | no line yet (fair: Nebraska -390) | no line yet |  |
| Sat 11/14 12:45 PM | Alabama @ Vanderbilt | Alabama 31, Vanderbilt 17 | Alabama 81% | Alabama -425 / Vanderbilt +425 | 32.2 – 19.4 | 17–48 / 7–32 | Alabama -12.8 / – | 51.6 / – | no line yet | no line yet (fair: Alabama -425) | no line yet |  |
| Sat 11/14 1:00 PM | East Carolina @ Charlotte | East Carolina 31, Charlotte 17 | East Carolina 86% | East Carolina -595 / Charlotte +595 | 32.1 – 17.2 | 17–48 / 6–29 | East Carolina -14.9 / – | 50.0 / – | no line yet | no line yet (fair: East Carolina -595) | no line yet |  |
| Sat 11/14 1:00 PM | UAB @ Temple | UAB 24, Temple 27 | Temple 55% | UAB +125 / Temple -125 | 24.6 – 26.9 | 11–38 / 13–41 | Temple -2.2 / – | 51.5 / – | no line yet | no line yet (fair: Temple -125) | no line yet |  |
| Sat 11/14 1:00 PM | Arkansas State @ Coastal Carolina | Arkansas State 24, Coastal Carolina 27 | Coastal Carolina 53% | Arkansas State +115 / Coastal Carolina -115 | 24.3 – 25.9 | 11–38 / 13–40 | Coastal Carolina -1.5 / – | 51.5 / – | no line yet | no line yet (fair: Coastal Carolina -115) | no line yet |  |
| Sat 11/14 2:00 PM | Tulane @ Rice | Tulane 27, Rice 24 | Tulane 61% | Tulane -160 / Rice +160 | 27.3 – 23.1 | 14–42 / 10–37 | Tulane -4.2 / – | 50.5 / – | no line yet | no line yet (fair: Tulane -160) | no line yet |  |
| Sat 11/14 2:00 PM | Kennesaw State @ Sam Houston | Kennesaw State 24, Sam Houston 21 | Kennesaw State 61% | Kennesaw State -155 / Sam Houston +155 | 24.2 – 19.9 | 10–38 / 7–34 | Kennesaw State -4.3 / – | 44.1 / – | no line yet | no line yet (fair: Kennesaw State -155) | no line yet |  |
| Sat 11/14 3:00 PM | New Mexico State @ Missouri State | New Mexico State 24, Missouri State 27 | Missouri State 63% | New Mexico State +170 / Missouri State -170 | 23.3 – 28.7 | 10–37 / 14–44 | Missouri State -5.4 / – | 52.0 / – | no line yet | no line yet (fair: Missouri State -170) | no line yet |  |
| Sat 11/14 3:00 PM | Florida International @ Delaware | Florida International 17, Delaware 31 | Delaware 81% | Florida International +430 / Delaware -430 | 19.5 – 32.0 | 7–33 / 17–48 | Delaware -12.5 / – | 51.9 / – | no line yet | no line yet (fair: Delaware -430) | no line yet |  |
| Sat 11/14 3:30 PM | Boston College @ Notre Dame | Boston College 3, Notre Dame 38 | Notre Dame 100% | Boston College +9900 / Notre Dame -9900 | 5.7 – 39.5 | 0–13 / 24–56 | Notre Dame -33.8 / – | 47.6 / – | no line yet | no line yet (fair: Notre Dame -9900) | no line yet |  |
| Sat 11/14 3:30 PM | California @ Virginia | California 21, Virginia 31 | Virginia 74% | California +285 / Virginia -285 | 20.7 – 30.2 | 9–34 / 16–45 | Virginia -9.5 / – | 50.8 / – | no line yet | no line yet (fair: Virginia -285) | no line yet |  |
| Sat 11/14 3:30 PM | USC @ Indiana | USC 21, Indiana 28 | Indiana 69% | USC +225 / Indiana -225 | 21.2 – 28.5 | 9–34 / 14–43 | Indiana -10.0 / Indiana -7.0 | 50.9 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Michigan @ Oregon | Michigan 17, Oregon 24 | Oregon 66% | Michigan +190 / Oregon -190 | 19.5 – 24.9 | 7–31 / 12–38 | Oregon -4.9 / Oregon -5.5 | 44.1 / 44.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Florida Atlantic @ Tulsa | Florida Atlantic 31, Tulsa 34 | Tulsa 57% | Florida Atlantic +135 / Tulsa -135 | 31.4 – 34.4 | 17–46 / 20–49 | Tulsa -2.9 / – | 65.8 / – | no line yet | no line yet (fair: Tulsa -135) | no line yet |  |
| Sat 11/14 3:30 PM | Nevada @ Northern Illinois | Nevada 27, Northern Illinois 24 | Nevada 56% | Nevada -130 / Northern Illinois +130 | 25.7 – 23.2 | 13–39 / 10–37 | Nevada -2.4 / – | 49.1 / – | no line yet | no line yet (fair: Nevada -130) | no line yet |  |
| Sat 11/14 3:30 PM | Georgia Southern @ Georgia State | Georgia Southern 28, Georgia State 31 | Georgia State 55% | Georgia Southern +125 / Georgia State -125 | 27.7 – 29.7 | 14–42 / 16–44 | Georgia State -2.0 / – | 58.7 / – | no line yet | no line yet (fair: Georgia State -125) | no line yet |  |
| Sat 11/14 3:30 PM | Jacksonville State @ Western Kentucky | Jacksonville State 27, Western Kentucky 24 | Jacksonville State 63% | Jacksonville State -170 / Western Kentucky +170 | 28.8 – 23.7 | 14–43 / 10–38 | Jacksonville State -5.1 / – | 53.5 / – | no line yet | no line yet (fair: Jacksonville State -170) | no line yet |  |
| Sat 11/14 3:30 PM | Middle Tennessee @ Liberty | Middle Tennessee 13, Liberty 34 | Liberty 93% | Middle Tennessee +1330 / Liberty -1330 | 13.6 – 34.6 | 3–24 / 20–50 | Liberty -20.9 / – | 49.2 / – | no line yet | no line yet (fair: Liberty -1330) | no line yet |  |
| Sat 11/14 4:00 PM | Fresno State @ Texas State | Fresno State 28, Texas State 31 | Texas State 60% | Fresno State +150 / Texas State -150 | 28.4 – 32.5 | 14–43 / 17–48 | Texas State -4.1 / – | 60.8 / – | no line yet | no line yet (fair: Texas State -150) | no line yet |  |
| Sat 11/14 4:15 PM | Washington @ Michigan State | Washington 24, Michigan State 17 | Washington 75% | Washington -300 / Michigan State +300 | 27.2 – 17.6 | 14–42 / 7–30 | Washington -9.6 / – | 45.6 / – | no line yet | no line yet (fair: Washington -300) | no line yet |  |
| Sat 11/14 5:00 PM | Southern Miss @ Louisiana Tech | Southern Miss 17, Louisiana Tech 34 | Louisiana Tech 85% | Southern Miss +585 / Louisiana Tech -585 | 18.3 – 33.5 | 7–31 / 19–49 | Louisiana Tech -15.2 / – | 51.8 / – | no line yet | no line yet (fair: Louisiana Tech -585) | no line yet |  |
| Sat 11/14 6:00 PM | Oregon State @ Boise State | Oregon State 28, Boise State 31 | Boise State 62% | Oregon State +165 / Boise State -165 | 28.7 – 33.4 | 14–44 / 19–48 | Boise State -6.7 / Boise State -4.5 | 60.6 / 62.5 | no edge | no edge | no edge |  |
| Sat 11/14 6:00 PM | App State @ Marshall | App State 24, Marshall 31 | Marshall 63% | App State +175 / Marshall -175 | 25.3 – 30.6 | 13–38 / 17–45 | Marshall -5.3 / – | 55.9 / – | no line yet | no line yet (fair: Marshall -175) | no line yet |  |
| Sat 11/14 7:00 PM | Minnesota @ Penn State | Minnesota 17, Penn State 24 | Penn State 77% | Minnesota +340 / Penn State -340 | 15.1 – 25.3 | 5–27 / 13–39 | Penn State -10.2 / – | 41.1 / – | no line yet | no line yet (fair: Penn State -340) | no line yet |  |
| Sat 11/14 7:00 PM | San José State @ Air Force | San José State 20, Air Force 34 | Air Force 82% | San José State +450 / Air Force -450 | 20.4 – 33.6 | 7–34 / 20–49 | Air Force -13.2 / – | 53.9 / – | no line yet | no line yet (fair: Air Force -450) | no line yet |  |
| Sat 11/14 7:00 PM | Troy @ South Alabama | Troy 24, South Alabama 27 | South Alabama 58% | Troy +140 / South Alabama -140 | 25.9 – 28.9 | 13–40 / 14–43 | South Alabama -3.1 / – | 54.8 / – | no line yet | no line yet (fair: South Alabama -140) | no line yet |  |
| Sat 11/14 7:30 PM | UNLV @ New Mexico | UNLV 17, New Mexico 24 | New Mexico 70% | UNLV +235 / New Mexico -235 | 19.6 – 27.0 | 7–32 / 14–41 | New Mexico -7.4 / – | 46.6 / – | no line yet | no line yet (fair: New Mexico -235) | no line yet |  |
| Sat 11/14 7:45 PM | South Carolina @ Arkansas | South Carolina 31, Arkansas 24 | South Carolina 75% | South Carolina -300 / Arkansas +300 | 32.6 – 22.2 | 17–48 / 10–35 | South Carolina -10.3 / – | 54.8 / – | no line yet | no line yet (fair: South Carolina -300) | no line yet |  |
| Sat 11/14 9:00 PM | North Texas @ UTSA | North Texas 31, UTSA 34 | UTSA 52% | North Texas +110 / UTSA -110 | 34.1 – 35.0 | 20–49 / 20–50 | UTSA -0.9 / – | 69.1 / – | no line yet | no line yet (fair: UTSA -110) | no line yet |  |
| Sat 11/14 9:30 PM | Utah State @ San Diego State | Utah State 24, San Diego State 27 | San Diego State 57% | Utah State +135 / San Diego State -135 | 22.9 – 25.6 | 10–37 / 13–39 | San Diego State -2.7 / – | 48.5 / – | no line yet | no line yet (fair: San Diego State -135) | no line yet |  |
| Sat 11/14 10:00 PM | Wyoming @ UTEP | Wyoming 27, UTEP 17 | Wyoming 79% | Wyoming -365 / UTEP +365 | 28.5 – 16.9 | 14–43 / 6–30 | Wyoming -11.6 / – | 45.4 / – | no line yet | no line yet (fair: Wyoming -365) | no line yet |  |
| Sat 11/14 10:30 PM | Colorado State @ Washington State | Colorado State 24, Washington State 31 | Washington State 66% | Colorado State +190 / Washington State -190 | 25.6 – 31.7 | 13–40 / 17–47 | Washington State -6.1 / – | 57.3 / – | no line yet | no line yet (fair: Washington State -190) | no line yet |  |
| Sat 11/14 11:00 PM | North Dakota State @ Hawai'i | North Dakota State 27, Hawai'i 20 | North Dakota State 68% | North Dakota State -215 / Hawai'i +215 | 26.7 – 19.6 | 13–41 / 7–33 | North Dakota State -7.1 / – | 47.5 / – | no line yet | no line yet (fair: North Dakota State -215) | no line yet |  |

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
