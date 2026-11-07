# College football score predictions

Updated Sat Nov 07, 2026 05:18 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 10

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sat 11/07 6:00 PM | Boise State @ Colorado State | Boise State 41, Colorado State 24 | Boise State 85% | Boise State -565 / Colorado State +565 | 42.1 – 25.9 | 27–58 / 13–41 | Boise State -15.8 / Boise State -16.2 | 63.1 / 69.2 | no edge | no edge | no edge |  |
| Sat 11/07 6:15 PM | Kentucky @ Tennessee | Kentucky 21, Tennessee 28 | Tennessee 66% | Kentucky +190 / Tennessee -190 | 21.5 – 27.8 | 10–35 / 14–42 | Tennessee -9.4 / Tennessee -6.0 | 48.3 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:00 PM | Sam Houston @ Jacksonville State | Sam Houston 14, Jacksonville State 31 | Jacksonville State 88% | Sam Houston +735 / Jacksonville State -735 | 14.6 – 31.2 | 3–27 / 17–46 | Jacksonville State -17.8 / Jacksonville State -16.5 | 45.7 / 45.8 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Georgia @ Ole Miss | Georgia 27, Ole Miss 24 | Georgia 58% | Georgia -140 / Ole Miss +140 | 29.8 – 26.3 | 16–45 / 13–41 | Georgia -3.0 / Georgia -3.5 | 54.2 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Colorado @ Arizona State | Colorado 24, Arizona State 27 | Arizona State 60% | Colorado +150 / Arizona State -150 | 22.4 – 25.9 | 10–35 / 13–41 | Arizona State -5.8 / Arizona State -3.2 | 50.0 / 48.0 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Louisville @ Georgia Tech | Louisville 38, Georgia Tech 24 | Louisville 84% | Louisville -510 / Georgia Tech +510 | 38.4 – 23.4 | 24–54 / 10–38 | Louisville -17.4 / Louisville -14.8 | 58.4 / 62.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Miami @ Notre Dame | Miami 24, Notre Dame 31 | Notre Dame 68% | Miami +210 / Notre Dame -210 | 23.8 – 30.6 | 10–38 / 17–45 | Notre Dame -4.5 / Notre Dame -7.0 | 53.9 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Michigan State @ Michigan | Michigan State 14, Michigan 28 | Michigan 86% | Michigan State +635 / Michigan -635 | 12.8 – 27.4 | 3–24 / 14–42 | Michigan -20.6 / Michigan -14.0 | 42.4 / 39.8 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Iowa @ Northwestern | Iowa 24, Northwestern 21 | Iowa 56% | Iowa -130 / Northwestern +130 | 23.2 – 20.8 | 10–37 / 9–34 | Northwestern -0.5 / Iowa -2.8 | 49.4 / 42.8 | no edge | no edge | Over 42.75 (-110*): EV +4.1%, 55%, stake 1.1u | * price not posted; assumed -110 |
| Sat 11/07 7:30 PM | Air Force @ Army | Air Force 21, Army 24 | Army 60% | Air Force +155 / Army -155 | 21.4 – 25.4 | 9–34 / 13–39 | Army -5.9 / Army -3.8 | 60.9 / 43.5 | no edge | no edge | Over 43.5 (-110*): EV +12.9%, 59%, stake 3.0u | * price not posted; assumed -110 |
| Sat 11/07 7:45 PM | Oklahoma @ Florida | Oklahoma 21, Florida 24 | Florida 63% | Oklahoma +170 / Florida -170 | 20.5 – 24.9 | 7–34 / 13–38 | Florida -1.0 / Florida -4.8 | 45.2 / 45.5 | no edge | no edge | no edge |  |
| Sat 11/07 8:00 PM | Liberty @ New Mexico State | Liberty 31, New Mexico State 14 | Liberty 85% | Liberty -585 / New Mexico State +585 | 30.9 – 15.6 | 17–45 / 6–27 | Liberty -16.3 / Liberty -15.2 | 47.4 / 46.2 | no edge | no edge | no edge |  |
| Sat 11/07 9:30 PM | West Virginia @ Texas Tech | West Virginia 24, Texas Tech 41 | Texas Tech 86% | West Virginia +640 / Texas Tech -640 | 23.6 – 40.6 | 10–38 / 26–56 | Texas Tech -21.4 / Texas Tech -16.5 | 56.6 / 66.0 | no edge | no edge | Under 66 (-110*): EV +4.1%, 53%, stake 1.2u | * price not posted; assumed -110 |
| Sat 11/07 9:30 PM | Fresno State @ Utah State | Fresno State 21, Utah State 24 | Utah State 51% | Fresno State +100 / Utah State -100 | 22.0 – 21.9 | 10–35 / 10–35 | Fresno State -2.6 / Utah State -0.2 | 46.7 / 43.2 | no edge | no edge | no edge |  |
| Sat 11/07 9:30 PM | Hawai'i @ UTEP | Hawai'i 28, UTEP 21 | Hawai'i 72% | Hawai'i -260 / UTEP +260 | 28.6 – 20.4 | 14–43 / 7–34 | Hawai'i -12.9 / Hawai'i -7.8 | 50.1 / 48.8 | no edge | no edge | no edge |  |
| Sat 11/07 10:30 PM | Texas State @ Oregon State | Texas State 31, Oregon State 38 | Oregon State 64% | Texas State +180 / Oregon State -180 | 32.6 – 38.2 | 17–48 / 23–54 | Oregon State -5.9 / Oregon State -5.5 | 67.9 / 71.5 | no edge | no edge | no edge |  |
| Sat 11/07 10:30 PM | Wyoming @ UNLV | Wyoming 24, UNLV 27 | UNLV 60% | Wyoming +150 / UNLV -150 | 22.5 – 26.7 | 10–35 / 13–41 | UNLV -8.9 / UNLV -3.8 | 49.8 / 49.0 | no edge | no edge | no edge |  |

## 2026 Week 11

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/10 7:00 PM | Western Michigan @ Akron | Western Michigan 31, Akron 17 | Western Michigan 85% | Western Michigan -550 / Akron +550 | 32.2 – 17.4 | 17–48 / 7–30 | Western Michigan -14.8 / – | 49.7 / – | no line yet | no line yet (fair: Western Michigan -550) | no line yet |  |
| Tue 11/10 7:00 PM | Kent State @ Bowling Green | Kent State 17, Bowling Green 24 | Bowling Green 66% | Kent State +190 / Bowling Green -190 | 18.0 – 23.5 | 7–31 / 10–38 | Bowling Green -5.4 / – | 41.5 / – | no line yet | no line yet (fair: Bowling Green -190) | no line yet |  |
| Tue 11/10 8:00 PM | Ohio @ Miami (OH) | Ohio 27, Miami (OH) 24 | Ohio 58% | Ohio -140 / Miami (OH) +140 | 25.5 – 22.8 | 13–39 / 10–35 | Ohio -2.7 / – | 48.2 / – | no line yet | no line yet (fair: Ohio -140) | no line yet |  |
| Wed 11/11 TBA | Massachusetts @ Toledo | Massachusetts 17, Toledo 34 | Toledo 90% | Massachusetts +920 / Toledo -920 | 14.9 – 33.6 | 3–27 / 20–49 | Toledo -18.7 / – | 48.6 / – | no line yet | no line yet (fair: Toledo -920) | no line yet |  |
| Wed 11/11 7:30 PM | Buffalo @ Ball State | Buffalo 24, Ball State 27 | Ball State 53% | Buffalo +115 / Ball State -115 | 25.7 – 27.1 | 13–40 / 14–41 | Ball State -1.4 / – | 52.8 / – | no line yet | no line yet (fair: Ball State -115) | no line yet |  |
| Wed 11/11 7:30 PM | Sacramento State @ Central Michigan | Sacramento State 17, Central Michigan 27 | Central Michigan 78% | Sacramento State +355 / Central Michigan -355 | 17.4 – 28.2 | 7–30 / 14–42 | Central Michigan -10.9 / – | 45.6 / – | no line yet | no line yet (fair: Central Michigan -355) | no line yet |  |
| Thu 11/12 8:00 PM | Memphis @ South Florida | Memphis 27, South Florida 24 | Memphis 52% | Memphis -105 / South Florida +105 | 27.5 – 26.7 | 14–42 / 13–41 | Memphis -0.8 / – | 54.6 / – | no line yet | no line yet (fair: Memphis -105) | no line yet |  |
| Thu 11/12 9:00 PM | Louisiana @ UL Monroe | Louisiana 31, UL Monroe 24 | Louisiana 69% | Louisiana -225 / UL Monroe +225 | 30.0 – 22.7 | 16–44 / 10–37 | Louisiana -7.3 / – | 52.6 / – | no line yet | no line yet (fair: Louisiana -225) | no line yet |  |
| Fri 11/13 7:00 PM | Florida State @ Pittsburgh | Florida State 24, Pittsburgh 27 | Pittsburgh 55% | Florida State +125 / Pittsburgh -125 | 26.5 – 28.6 | 13–41 / 14–42 | Pittsburgh -2.2 / – | 55.3 / – | no line yet | no line yet (fair: Pittsburgh -125) | no line yet |  |
| Fri 11/13 9:00 PM | Illinois @ UCLA | Illinois 17, UCLA 31 | UCLA 79% | Illinois +375 / UCLA -375 | 18.4 – 30.0 | 7–31 / 16–45 | UCLA -13.3 / UCLA -11.5 | 52.1 / 47.5 | no edge | no edge | no edge |  |
| Fri 11/13 10:15 PM | Houston @ Colorado | Houston 31, Colorado 24 | Houston 64% | Houston -175 / Colorado +175 | 29.8 – 24.3 | 16–44 / 10–38 | Houston -5.5 / – | 54.1 / – | no line yet | no line yet (fair: Houston -175) | no line yet |  |
| Sat 11/14 TBA | Arizona State @ UCF | Arizona State 27, UCF 24 | UCF 51% | Arizona State +100 / UCF -100 | 24.4 – 24.3 | 10–38 / 10–38 | Arizona State -0.1 / – | 50.1 / – | no line yet | no line yet (fair: UCF -100) | no line yet |  |
| Sat 11/14 TBA | Baylor @ BYU | Baylor 21, BYU 28 | BYU 67% | Baylor +205 / BYU -205 | 20.7 – 27.6 | 9–34 / 14–42 | BYU -6.0 / BYU -7.0 | 51.9 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Cincinnati @ Iowa State | Cincinnati 28, Iowa State 31 | Iowa State 59% | Cincinnati +145 / Iowa State -145 | 28.1 – 31.6 | 14–42 / 17–45 | Iowa State -3.5 / – | 59.7 / – | no line yet | no line yet (fair: Iowa State -145) | no line yet |  |
| Sat 11/14 TBA | Kansas @ West Virginia | Kansas 31, West Virginia 28 | Kansas 61% | Kansas -155 / West Virginia +155 | 32.7 – 28.5 | 17–48 / 14–42 | Kansas -4.2 / – | 61.3 / – | no line yet | no line yet (fair: Kansas -155) | no line yet |  |
| Sat 11/14 TBA | Kansas State @ TCU | Kansas State 24, TCU 21 | Kansas State 55% | Kansas State -125 / TCU +125 | 25.3 – 23.2 | 13–39 / 10–37 | Kansas State -2.1 / – | 48.5 / – | no line yet | no line yet (fair: Kansas State -125) | no line yet |  |
| Sat 11/14 TBA | Texas Tech @ Oklahoma State | Texas Tech 34, Oklahoma State 31 | Texas Tech 56% | Texas Tech -130 / Oklahoma State +130 | 32.2 – 29.9 | 17–48 / 16–45 | Texas Tech -9.8 / Texas Tech -1.5 | 56.0 / 63.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Utah @ Arizona | Utah 27, Arizona 24 | Utah 55% | Utah -120 / Arizona +120 | 27.2 – 25.3 | 14–42 / 13–39 | Utah -5.9 / Utah -1.5 | 56.5 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Missouri @ Georgia | Missouri 17, Georgia 31 | Georgia 80% | Missouri +400 / Georgia -400 | 17.0 – 29.3 | 6–30 / 15–44 | Georgia -10.4 / Georgia -12.5 | 45.9 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Florida @ Kentucky | Florida 24, Kentucky 27 | Kentucky 54% | Florida +115 / Kentucky -115 | 26.8 – 28.0 | 14–41 / 14–42 | Florida -1.2 / Kentucky -1.5 | 51.7 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Texas @ LSU | Texas 21, LSU 24 | LSU 67% | Texas +200 / LSU -200 | 20.2 – 26.1 | 7–34 / 13–41 | LSU -10.2 / LSU -5.5 | 45.6 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Ole Miss @ Oklahoma | Ole Miss 24, Oklahoma 27 | Oklahoma 60% | Ole Miss +150 / Oklahoma -150 | 24.7 – 28.2 | 12–38 / 14–42 | Ole Miss -1.6 / Oklahoma -4.0 | 50.5 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Tennessee @ Texas A&M | Tennessee 24, Texas A&M 31 | Texas A&M 69% | Tennessee +220 / Texas A&M -220 | 23.0 – 30.5 | 10–37 / 17–45 | Tennessee -1.6 / Texas A&M -8.5 | 45.2 / 55.5 | no edge | no edge | Under 55.5 (-110*): EV +5.0%, 55%, stake 1.4u | * price not posted; assumed -110 |
| Sat 11/14 TBA | Louisville @ North Carolina | Louisville 31, North Carolina 28 | Louisville 58% | Louisville -140 / North Carolina +140 | 31.0 – 28.0 | 17–45 / 14–42 | Louisville -8.9 / Louisville -2.5 | 56.9 / 59.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Stanford @ Virginia Tech | Stanford 21, Virginia Tech 38 | Virginia Tech 85% | Stanford +555 / Virginia Tech -555 | 19.9 – 35.6 | 7–34 / 21–51 | Virginia Tech -15.7 / – | 56.2 / – | no line yet | no line yet (fair: Virginia Tech -555) | no line yet |  |
| Sat 11/14 TBA | Purdue @ Iowa | Purdue 17, Iowa 31 | Iowa 84% | Purdue +510 / Iowa -510 | 16.9 – 31.7 | 6–29 / 17–47 | Iowa -14.8 / – | 48.6 / – | no line yet | no line yet (fair: Iowa -510) | no line yet |  |
| Sat 11/14 12:00 PM | Auburn @ Mississippi State | Auburn 31, Mississippi State 28 | Auburn 52% | Auburn -105 / Mississippi State +105 | 28.5 – 27.9 | 14–43 / 14–42 | Auburn -0.6 / – | 56.5 / – | no line yet | no line yet (fair: Auburn -105) | no line yet |  |
| Sat 11/14 12:00 PM | Duke @ Miami | Duke 17, Miami 38 | Miami 92% | Duke +1115 / Miami -1115 | 17.3 – 38.0 | 7–30 / 23–54 | Miami -18.0 / Miami -21.0 | 56.3 / 55.5 | no edge | Duke (+1000): EV +4.9%, 10%, stake 0.1u | no edge |  |
| Sat 11/14 12:00 PM | Syracuse @ NC State | Syracuse 28, NC State 31 | NC State 60% | Syracuse +150 / NC State -150 | 25.9 – 29.7 | 13–41 / 16–45 | NC State -3.9 / – | 57.7 / – | no line yet | no line yet (fair: NC State -150) | no line yet |  |
| Sat 11/14 12:00 PM | Wake Forest @ SMU | Wake Forest 30, SMU 27 | Wake Forest 56% | Wake Forest -130 / SMU +130 | 29.4 – 26.7 | 16–44 / 13–41 | SMU -0.2 / Wake Forest -3.0 | 54.2 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/14 12:00 PM | Wisconsin @ Maryland | Wisconsin 24, Maryland 21 | Wisconsin 64% | Wisconsin -175 / Maryland +175 | 24.3 – 19.5 | 10–38 / 7–31 | Wisconsin -4.7 / – | 44.4 / – | no line yet | no line yet (fair: Wisconsin -175) | no line yet |  |
| Sat 11/14 12:00 PM | Northwestern @ Ohio State | Northwestern 21, Ohio State 31 | Ohio State 75% | Northwestern +305 / Ohio State -305 | 19.6 – 29.8 | 7–31 / 16–45 | Ohio State -16.6 / Ohio State -9.5 | 53.8 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/14 12:00 PM | James Madison @ UConn | James Madison 27, UConn 24 | James Madison 55% | James Madison -125 / UConn +125 | 29.3 – 26.8 | 15–44 / 14–41 | James Madison -2.5 / – | 56.2 / – | no line yet | no line yet (fair: James Madison -125) | no line yet |  |
| Sat 11/14 12:30 PM | Georgia Tech @ Clemson | Georgia Tech 17, Clemson 31 | Clemson 81% | Georgia Tech +420 / Clemson -420 | 17.9 – 30.8 | 7–31 / 17–45 | Clemson -12.9 / – | 49.9 / – | no line yet | no line yet (fair: Clemson -420) | no line yet |  |
| Sat 11/14 12:30 PM | Nebraska @ Rutgers | Nebraska 31, Rutgers 21 | Nebraska 79% | Nebraska -370 / Rutgers +370 | 33.4 – 20.9 | 17–49 / 8–35 | Nebraska -12.5 / – | 54.4 / – | no line yet | no line yet (fair: Nebraska -370) | no line yet |  |
| Sat 11/14 12:45 PM | Alabama @ Vanderbilt | Alabama 31, Vanderbilt 17 | Alabama 80% | Alabama -400 / Vanderbilt +400 | 32.1 – 19.4 | 17–47 / 7–33 | Alabama -12.7 / – | 51.4 / – | no line yet | no line yet (fair: Alabama -400) | no line yet |  |
| Sat 11/14 1:00 PM | East Carolina @ Charlotte | East Carolina 31, Charlotte 17 | East Carolina 84% | East Carolina -540 / Charlotte +540 | 31.7 – 17.2 | 17–46 / 6–30 | East Carolina -14.5 / – | 49.9 / – | no line yet | no line yet (fair: East Carolina -540) | no line yet |  |
| Sat 11/14 1:00 PM | UAB @ Temple | UAB 24, Temple 27 | Temple 58% | UAB +140 / Temple -140 | 24.3 – 27.1 | 10–38 / 14–42 | Temple -2.7 / – | 51.4 / – | no line yet | no line yet (fair: Temple -140) | no line yet |  |
| Sat 11/14 1:00 PM | Arkansas State @ Coastal Carolina | Arkansas State 24, Coastal Carolina 27 | Coastal Carolina 55% | Arkansas State +125 / Coastal Carolina -125 | 24.3 – 26.2 | 11–38 / 13–40 | Coastal Carolina -1.9 / – | 52.7 / – | no line yet | no line yet (fair: Coastal Carolina -125) | no line yet |  |
| Sat 11/14 2:00 PM | Tulane @ Rice | Tulane 27, Rice 24 | Tulane 64% | Tulane -175 / Rice +175 | 27.8 – 22.2 | 14–42 / 10–35 | Tulane -5.6 / – | 50.0 / – | no line yet | no line yet (fair: Tulane -175) | no line yet |  |
| Sat 11/14 2:00 PM | Kennesaw State @ Sam Houston | Kennesaw State 24, Sam Houston 21 | Kennesaw State 61% | Kennesaw State -155 / Sam Houston +155 | 24.1 – 19.9 | 10–38 / 7–33 | Kennesaw State -4.2 / – | 44.0 / – | no line yet | no line yet (fair: Kennesaw State -155) | no line yet |  |
| Sat 11/14 3:00 PM | New Mexico State @ Missouri State | New Mexico State 24, Missouri State 27 | Missouri State 66% | New Mexico State +190 / Missouri State -190 | 23.2 – 28.7 | 10–37 / 14–43 | Missouri State -5.5 / – | 51.9 / – | no line yet | no line yet (fair: Missouri State -190) | no line yet |  |
| Sat 11/14 3:00 PM | Florida International @ Delaware | Florida International 17, Delaware 31 | Delaware 81% | Florida International +420 / Delaware -420 | 19.4 – 32.2 | 7–33 / 17–48 | Delaware -12.8 / – | 51.7 / – | no line yet | no line yet (fair: Delaware -420) | no line yet |  |
| Sat 11/14 3:30 PM | Boston College @ Notre Dame | Boston College 6, Notre Dame 41 | Notre Dame 100% | Boston College +9900 / Notre Dame -9900 | 6.5 – 40.8 | 0–14 / 27–56 | Notre Dame -34.3 / – | 47.4 / – | no line yet | no line yet (fair: Notre Dame -9900) | no line yet |  |
| Sat 11/14 3:30 PM | California @ Virginia | California 21, Virginia 28 | Virginia 73% | California +275 / Virginia -275 | 20.2 – 29.7 | 7–34 / 16–44 | Virginia -9.5 / – | 50.6 / – | no line yet | no line yet (fair: Virginia -275) | no line yet |  |
| Sat 11/14 3:30 PM | USC @ Indiana | USC 21, Indiana 28 | Indiana 69% | USC +220 / Indiana -220 | 21.6 – 28.9 | 10–35 / 14–44 | Indiana -10.1 / Indiana -7.0 | 50.7 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Michigan @ Oregon | Michigan 17, Oregon 24 | Oregon 64% | Michigan +180 / Oregon -180 | 19.5 – 24.9 | 7–32 / 12–38 | Oregon -4.8 / Oregon -5.5 | 44.0 / 44.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Florida Atlantic @ Tulsa | Florida Atlantic 31, Tulsa 34 | Tulsa 54% | Florida Atlantic +115 / Tulsa -115 | 31.7 – 33.2 | 17–46 / 19–48 | Tulsa -1.4 / – | 65.2 / – | no line yet | no line yet (fair: Tulsa -115) | no line yet |  |
| Sat 11/14 3:30 PM | Nevada @ Northern Illinois | Nevada 24, Northern Illinois 21 | Nevada 56% | Nevada -125 / Northern Illinois +125 | 25.7 – 23.3 | 13–40 / 10–37 | Nevada -2.4 / – | 49.0 / – | no line yet | no line yet (fair: Nevada -125) | no line yet |  |
| Sat 11/14 3:30 PM | Georgia Southern @ Georgia State | Georgia Southern 28, Georgia State 31 | Georgia State 53% | Georgia Southern +110 / Georgia State -110 | 27.9 – 29.0 | 14–42 / 14–44 | Georgia State -1.1 / – | 58.4 / – | no line yet | no line yet (fair: Georgia State -110) | no line yet |  |
| Sat 11/14 3:30 PM | Jacksonville State @ Western Kentucky | Jacksonville State 27, Western Kentucky 24 | Jacksonville State 63% | Jacksonville State -170 / Western Kentucky +170 | 29.2 – 24.2 | 15–44 / 10–38 | Jacksonville State -5.1 / – | 53.4 / – | no line yet | no line yet (fair: Jacksonville State -170) | no line yet |  |
| Sat 11/14 3:30 PM | Middle Tennessee @ Liberty | Middle Tennessee 13, Liberty 34 | Liberty 93% | Middle Tennessee +1380 / Liberty -1380 | 13.1 – 34.1 | 3–24 / 20–49 | Liberty -21.0 / – | 49.0 / – | no line yet | no line yet (fair: Liberty -1380) | no line yet |  |
| Sat 11/14 4:00 PM | Fresno State @ Texas State | Fresno State 28, Texas State 31 | Texas State 60% | Fresno State +150 / Texas State -150 | 28.3 – 32.4 | 14–42 / 17–48 | Texas State -4.0 / – | 60.7 / – | no line yet | no line yet (fair: Texas State -150) | no line yet |  |
| Sat 11/14 4:15 PM | Washington @ Michigan State | Washington 24, Michigan State 17 | Washington 75% | Washington -300 / Michigan State +300 | 27.8 – 17.7 | 14–42 / 7–31 | Washington -10.0 / – | 45.5 / – | no line yet | no line yet (fair: Washington -300) | no line yet |  |
| Sat 11/14 5:00 PM | Southern Miss @ Louisiana Tech | Southern Miss 17, Louisiana Tech 34 | Louisiana Tech 85% | Southern Miss +570 / Louisiana Tech -570 | 18.3 – 33.4 | 7–31 / 19–49 | Louisiana Tech -15.1 / – | 51.7 / – | no line yet | no line yet (fair: Louisiana Tech -570) | no line yet |  |
| Sat 11/14 6:00 PM | Oregon State @ Boise State | Oregon State 28, Boise State 31 | Boise State 62% | Oregon State +160 / Boise State -160 | 28.7 – 33.4 | 14–43 / 19–49 | Boise State -6.8 / Boise State -4.5 | 60.4 / 62.5 | no edge | no edge | no edge |  |
| Sat 11/14 6:00 PM | App State @ Marshall | App State 28, Marshall 31 | Marshall 61% | App State +155 / Marshall -155 | 25.7 – 29.9 | 13–40 / 16–45 | Marshall -4.2 / – | 55.6 / – | no line yet | no line yet (fair: Marshall -155) | no line yet |  |
| Sat 11/14 7:00 PM | Minnesota @ Penn State | Minnesota 17, Penn State 24 | Penn State 75% | Minnesota +295 / Penn State -295 | 14.7 – 23.7 | 3–27 / 10–38 | Penn State -9.0 / – | 40.4 / – | no line yet | no line yet (fair: Penn State -295) | no line yet |  |
| Sat 11/14 7:00 PM | San José State @ Air Force | San José State 20, Air Force 34 | Air Force 82% | San José State +440 / Air Force -440 | 20.2 – 33.6 | 7–34 / 19–49 | Air Force -13.4 / – | 53.8 / – | no line yet | no line yet (fair: Air Force -440) | no line yet |  |
| Sat 11/14 7:00 PM | Troy @ South Alabama | Troy 24, South Alabama 27 | South Alabama 58% | Troy +135 / South Alabama -135 | 25.8 – 29.1 | 13–41 / 14–43 | South Alabama -3.3 / – | 54.8 / – | no line yet | no line yet (fair: South Alabama -135) | no line yet |  |
| Sat 11/14 7:30 PM | UNLV @ New Mexico | UNLV 17, New Mexico 24 | New Mexico 70% | UNLV +230 / New Mexico -230 | 19.5 – 27.0 | 7–32 / 14–41 | New Mexico -7.5 / – | 46.5 / – | no line yet | no line yet (fair: New Mexico -230) | no line yet |  |
| Sat 11/14 7:45 PM | South Carolina @ Arkansas | South Carolina 31, Arkansas 24 | South Carolina 75% | South Carolina -295 / Arkansas +295 | 32.0 – 22.2 | 17–48 / 10–35 | South Carolina -9.8 / – | 54.2 / – | no line yet | no line yet (fair: South Carolina -295) | no line yet |  |
| Sat 11/14 9:00 PM | North Texas @ UTSA | North Texas 31, UTSA 34 | UTSA 53% | North Texas +110 / UTSA -110 | 33.9 – 35.0 | 20–49 / 20–50 | UTSA -1.1 / – | 68.9 / – | no line yet | no line yet (fair: UTSA -110) | no line yet |  |
| Sat 11/14 9:30 PM | Utah State @ San Diego State | Utah State 21, San Diego State 24 | San Diego State 56% | Utah State +130 / San Diego State -130 | 22.8 – 25.6 | 10–37 / 13–38 | San Diego State -2.8 / – | 48.4 / – | no line yet | no line yet (fair: San Diego State -130) | no line yet |  |
| Sat 11/14 10:00 PM | Wyoming @ UTEP | Wyoming 27, UTEP 17 | Wyoming 79% | Wyoming -375 / UTEP +375 | 28.4 – 16.9 | 14–42 / 6–29 | Wyoming -11.5 / – | 45.4 / – | no line yet | no line yet (fair: Wyoming -375) | no line yet |  |
| Sat 11/14 10:30 PM | Colorado State @ Washington State | Colorado State 24, Washington State 31 | Washington State 66% | Colorado State +195 / Washington State -195 | 25.4 – 31.7 | 13–39 / 17–47 | Washington State -6.3 / – | 57.1 / – | no line yet | no line yet (fair: Washington State -195) | no line yet |  |
| Sat 11/14 11:00 PM | North Dakota State @ Hawai'i | North Dakota State 24, Hawai'i 17 | North Dakota State 69% | North Dakota State -220 / Hawai'i +220 | 26.6 – 19.6 | 13–41 / 7–32 | North Dakota State -7.0 / – | 47.3 / – | no line yet | no line yet (fair: North Dakota State -220) | no line yet |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 639 | 11.72 | 12.14 | 8.43 | 80.1% | 0.140 | 82.0% |
| Model only (before blending) | 639 | 12.44 | 12.47 | 8.70 | 77.6% | – | – |
| Betting line when predicted | 637 | 11.71 | 12.10 | 8.42 | 80.1% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin of an FBS game by about 12.5 points.

501 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 6 | 1-5-0 | 1.8 | +0.17 | +9.3% | +5.0% |
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
| BYU @ Utah | 24–27 | 20–28 | 63% | yes |
| Clemson @ Syracuse | 27–24 | 18–13 | 56% | yes |
| Florida State @ Boston College | 31–24 | 31–24 | 67% | yes |
| North Carolina @ UConn | 31–24 | 38–21 | 67% | yes |
| Tulsa @ Tulane | 27–24 | 60–10 | 55% | no |

## FBS power ratings

Points per game better than an average FBS team on a neutral field, from opponent-adjusted EPA (garbage time removed) with this season's games weighted against a preseason prior, plus the weight the margin model puts on Elo (a rating built from game results alone). Defense is positive when it holds opponents below average.

| # | Team | Conference | Net | Offense | Defense | Special teams | Results (Elo) | Elo rating |
|---|---|---|---|---|---|---|---|---|
| 1 | LSU | SEC | +26.3 | +10.8 | +12.5 | +0.2 | +2.9 | 1751 |
| 2 | Ohio State | Big Ten | +25.7 | +10.8 | +10.3 | +0.3 | +4.2 | 1868 |
| 3 | Georgia | SEC | +23.8 | +7.9 | +10.7 | +0.8 | +4.4 | 1880 |
| 4 | Notre Dame | FBS Independents | +23.0 | +8.8 | +9.1 | +1.0 | +4.1 | 1858 |
| 5 | Miami | ACC | +23.0 | +14.2 | +3.8 | +0.4 | +4.6 | 1894 |
| 6 | Indiana | Big Ten | +21.5 | +5.7 | +10.6 | +0.2 | +5.1 | 1939 |
| 7 | Utah | Big 12 | +20.5 | +10.6 | +5.7 | -0.0 | +4.2 | 1862 |
| 8 | Alabama | SEC | +19.6 | +9.0 | +7.2 | +0.3 | +3.2 | 1777 |
| 9 | Ole Miss | SEC | +18.5 | +10.4 | +3.7 | +0.7 | +3.6 | 1815 |
| 10 | Texas | SEC | +18.3 | +1.7 | +12.4 | +0.5 | +3.6 | 1814 |
| 11 | Texas Tech | Big 12 | +18.2 | +2.1 | +11.9 | +1.2 | +3.0 | 1761 |
| 12 | Oregon | Big Ten | +16.7 | +4.5 | +9.0 | +0.4 | +2.8 | 1743 |
| 13 | UCLA | Big Ten | +16.5 | +4.6 | +9.2 | +0.7 | +2.0 | 1676 |
| 14 | Missouri | SEC | +16.1 | +4.5 | +8.4 | +0.7 | +2.4 | 1714 |
| 15 | Wake Forest | ACC | +16.0 | +6.0 | +7.2 | +0.4 | +2.4 | 1710 |
| 16 | Tennessee | SEC | +15.7 | +3.7 | +8.5 | +1.0 | +2.5 | 1723 |
| 17 | Louisville | ACC | +15.0 | +9.3 | +3.6 | +0.1 | +2.0 | 1681 |
| 18 | Michigan | Big Ten | +14.8 | +3.5 | +9.3 | +0.0 | +2.0 | 1674 |
| 19 | Oklahoma | SEC | +14.5 | +0.3 | +12.3 | +0.6 | +1.3 | 1615 |
| 20 | USC | Big Ten | +13.9 | +10.6 | +0.3 | +0.3 | +2.7 | 1738 |
| 21 | SMU | ACC | +13.8 | +8.0 | +3.2 | +0.3 | +2.3 | 1700 |
| 22 | BYU | Big 12 | +13.1 | +5.6 | +4.2 | +0.6 | +2.7 | 1739 |
| 23 | Iowa | Big Ten | +13.0 | +1.6 | +7.8 | +0.8 | +2.9 | 1751 |
| 24 | Florida | SEC | +12.6 | +6.5 | +4.3 | +0.9 | +0.8 | 1579 |
| 25 | Texas A&M | SEC | +12.1 | +2.6 | +7.8 | +0.5 | +1.1 | 1601 |
| 26 | Auburn | SEC | +12.1 | +5.5 | +5.6 | +0.6 | +0.3 | 1536 |
| 27 | Arizona | Big 12 | +12.0 | +6.1 | +3.3 | +0.1 | +2.4 | 1713 |
| 28 | South Carolina | SEC | +11.6 | +5.5 | +3.8 | +0.5 | +1.8 | 1662 |
| 29 | Penn State | Big Ten | +11.5 | +3.1 | +7.1 | +0.1 | +1.2 | 1611 |
| 30 | Nebraska | Big Ten | +11.4 | +3.4 | +7.2 | +0.3 | +0.6 | 1558 |
| 31 | Northwestern | Big Ten | +11.1 | +7.0 | +1.9 | +0.8 | +1.5 | 1634 |
| 32 | Houston | Big 12 | +10.1 | +7.8 | +0.2 | +0.2 | +1.9 | 1673 |
| 33 | Kansas State | Big 12 | +9.8 | +6.3 | +3.0 | +0.3 | +0.2 | 1526 |
| 34 | Kentucky | SEC | +9.5 | +2.8 | +4.5 | +0.3 | +2.0 | 1677 |
| 35 | Mississippi State | SEC | +9.3 | +5.8 | +3.4 | +0.2 | +0.0 | 1512 |
| 36 | Baylor | Big 12 | +9.3 | +0.3 | +6.8 | +1.0 | +1.1 | 1601 |
| 37 | Washington | Big Ten | +9.2 | +1.9 | +5.3 | +0.0 | +1.9 | 1670 |
| 38 | Wisconsin | Big Ten | +8.0 | -0.2 | +6.9 | +0.3 | +1.0 | 1593 |
| 39 | Kansas | Big 12 | +7.3 | +4.7 | +3.4 | -0.0 | -0.8 | 1439 |
| 40 | Duke | ACC | +7.0 | +2.7 | +1.4 | +0.9 | +2.0 | 1677 |
| 41 | Oklahoma State | Big 12 | +6.7 | +8.5 | -1.9 | +0.4 | -0.3 | 1484 |
| 42 | Iowa State | Big 12 | +6.6 | +3.9 | +1.1 | +1.0 | +0.6 | 1563 |
| 43 | Cincinnati | Big 12 | +6.3 | +9.0 | -3.7 | +0.3 | +0.7 | 1568 |
| 44 | Boise State | Pac-12 | +6.3 | +4.8 | -0.9 | -0.1 | +2.5 | 1721 |
| 45 | Illinois | Big Ten | +6.2 | +6.8 | -2.3 | +0.2 | +1.5 | 1638 |
| 46 | Arizona State | Big 12 | +5.5 | +1.1 | +4.0 | +0.0 | +0.5 | 1550 |
| 47 | TCU | Big 12 | +5.4 | -2.0 | +6.4 | +0.1 | +0.9 | 1582 |
| 48 | Florida State | ACC | +5.3 | +7.2 | -1.3 | -0.4 | -0.1 | 1499 |
| 49 | Clemson | ACC | +4.9 | -4.9 | +7.6 | +0.7 | +1.4 | 1627 |
| 50 | Vanderbilt | SEC | +4.5 | +4.6 | -0.6 | +0.2 | +0.2 | 1529 |
| 51 | Virginia Tech | ACC | +4.3 | +4.0 | -0.1 | +0.1 | +0.4 | 1541 |
| 52 | Minnesota | Big Ten | +4.1 | -4.0 | +6.4 | +1.1 | +0.6 | 1561 |
| 53 | Pittsburgh | ACC | +4.0 | -1.2 | +4.0 | +0.6 | +0.7 | 1566 |
| 54 | North Texas | American Athletic | +3.4 | +10.1 | -7.4 | -0.9 | +1.6 | 1645 |
| 55 | NC State | ACC | +3.3 | +5.6 | -2.1 | -0.6 | +0.3 | 1538 |
| 56 | James Madison | Sun Belt | +3.2 | -1.1 | +1.5 | +0.4 | +2.4 | 1711 |
| 57 | Colorado | Big 12 | +3.0 | +0.6 | +4.7 | -0.7 | -1.5 | 1378 |
| 58 | North Carolina | ACC | +2.9 | +3.3 | -1.7 | +0.8 | +0.5 | 1554 |
| 59 | UCF | Big 12 | +2.9 | +0.7 | +2.8 | +0.0 | -0.6 | 1459 |
| 60 | Syracuse | ACC | +2.1 | +1.7 | +2.6 | -0.8 | -1.4 | 1392 |
| 61 | Memphis | American Athletic | +2.0 | +3.5 | -2.3 | -0.4 | +1.2 | 1614 |
| 62 | Oregon State | Pac-12 | +1.8 | +4.5 | -2.4 | +0.1 | -0.5 | 1468 |
| 63 | Virginia | ACC | +1.1 | -1.3 | +3.0 | -0.5 | -0.2 | 1494 |
| 64 | UTSA | American Athletic | +1.1 | +3.8 | -3.7 | -0.1 | +1.0 | 1596 |
| 65 | Liberty | Conference USA | +0.9 | +0.6 | -0.5 | +0.3 | +0.5 | 1551 |
| 66 | Purdue | Big Ten | +0.7 | +3.0 | -2.1 | +0.8 | -1.0 | 1426 |
| 67 | Arkansas | SEC | +0.4 | +1.3 | +0.3 | -0.7 | -0.5 | 1468 |
| 68 | Maryland | Big Ten | +0.3 | -1.6 | +3.1 | +0.8 | -2.1 | 1334 |
| 69 | New Mexico | Mountain West | +0.2 | -4.0 | +3.0 | -0.2 | +1.5 | 1636 |
| 70 | West Virginia | Big 12 | -0.1 | +3.8 | -4.4 | +0.6 | -0.1 | 1502 |
| 71 | Texas State | Pac-12 | -0.2 | +5.7 | -5.4 | -1.2 | +0.6 | 1563 |
| 72 | Toledo | Mid-American | -0.8 | -2.5 | +1.4 | -0.3 | +0.6 | 1559 |
| 73 | Navy | American Athletic | -1.3 | +3.5 | -3.8 | -0.5 | -0.4 | 1473 |
| 74 | North Dakota State | Mountain West | -1.5 | -5.0 | +3.4 | +1.1 | -1.1 | 1419 |
| 75 | South Florida | American Athletic | -1.9 | -2.5 | -0.1 | +0.1 | +0.7 | 1569 |
| 76 | UConn | FBS Independents | -2.5 | +2.2 | -3.5 | -0.2 | -1.0 | 1427 |
| 77 | Tulsa | American Athletic | -2.5 | -1.0 | -0.4 | -0.6 | -0.5 | 1466 |
| 78 | Fresno State | Pac-12 | -2.8 | -2.3 | -1.0 | -0.2 | +0.8 | 1574 |
| 79 | Florida Atlantic | American Athletic | -2.8 | +4.7 | -8.2 | +0.7 | -0.0 | 1506 |
| 80 | Army | American Athletic | -3.0 | +5.2 | -8.7 | -0.1 | +0.5 | 1554 |
| 81 | Louisiana Tech | Sun Belt | -3.0 | -3.2 | +0.6 | -0.8 | +0.4 | 1540 |
| 82 | East Carolina | American Athletic | -3.0 | -5.3 | +2.7 | -0.6 | +0.1 | 1520 |
| 83 | Michigan State | Big Ten | -3.6 | -3.5 | +1.1 | +0.3 | -1.4 | 1388 |
| 84 | Ohio | Mid-American | -3.6 | -1.8 | -2.8 | +0.2 | +0.9 | 1586 |
| 85 | Rutgers | Big Ten | -4.1 | +2.8 | -6.2 | +0.8 | -1.4 | 1388 |
| 86 | Georgia Tech | ACC | -4.7 | +1.1 | -4.3 | -0.1 | -1.4 | 1393 |
| 87 | Jacksonville State | Conference USA | -4.9 | -0.2 | -4.4 | -0.1 | -0.1 | 1497 |
| 88 | Air Force | Mountain West | -4.9 | +2.4 | -6.8 | -0.2 | -0.2 | 1488 |
| 89 | UNLV | Mountain West | -5.1 | -2.6 | -3.0 | +0.2 | +0.4 | 1543 |
| 90 | Boston College | ACC | -5.7 | -3.6 | -0.4 | -0.8 | -0.9 | 1431 |
| 91 | Tulane | American Athletic | -5.8 | -3.7 | -1.6 | +0.2 | -0.6 | 1454 |
| 92 | California | ACC | -5.9 | -2.1 | -1.8 | -0.4 | -1.6 | 1369 |
| 93 | Delaware | Conference USA | -6.4 | -0.2 | -5.2 | +0.3 | -1.2 | 1406 |
| 94 | Utah State | Pac-12 | -6.9 | -6.6 | +2.1 | -1.2 | -1.1 | 1412 |
| 95 | Western Michigan | Mid-American | -6.9 | -4.8 | -3.6 | +0.8 | +0.6 | 1561 |
| 96 | Marshall | Sun Belt | -7.2 | -3.6 | -3.6 | +0.1 | -0.1 | 1500 |
| 97 | Washington State | Pac-12 | -8.1 | -6.0 | +0.1 | -0.3 | -1.9 | 1349 |
| 98 | San Diego State | Pac-12 | -8.1 | -4.5 | -2.6 | +0.3 | -1.2 | 1406 |
| 99 | Georgia Southern | Sun Belt | -8.1 | -2.1 | -5.2 | -0.9 | +0.1 | 1513 |
| 100 | App State | Sun Belt | -8.4 | -3.8 | -3.3 | -0.3 | -1.0 | 1422 |
| 101 | Stanford | ACC | -8.7 | -2.7 | -5.2 | -0.1 | -0.7 | 1448 |
| 102 | Miami (OH) | Mid-American | -9.3 | -4.8 | -4.1 | +0.7 | -1.0 | 1421 |
| 103 | Louisiana | Sun Belt | -9.6 | -5.0 | -4.1 | -0.1 | -0.4 | 1478 |
| 104 | Temple | American Athletic | -9.6 | +0.7 | -7.2 | -0.5 | -2.6 | 1291 |
| 105 | UAB | American Athletic | -9.9 | -5.7 | -2.6 | -0.4 | -1.2 | 1407 |
| 106 | Georgia State | Sun Belt | -10.2 | -0.9 | -7.1 | -0.3 | -1.9 | 1347 |
| 107 | Arkansas State | Sun Belt | -10.5 | -2.8 | -6.9 | +0.1 | -0.8 | 1441 |
| 108 | Hawai'i | Mountain West | -10.9 | -4.0 | -6.2 | +1.0 | -1.7 | 1365 |
| 109 | Troy | Sun Belt | -11.0 | -8.0 | -0.5 | -1.3 | -1.3 | 1401 |
| 110 | Wyoming | Mountain West | -11.1 | -6.5 | -3.3 | -0.2 | -1.1 | 1413 |
| 111 | Coastal Carolina | Sun Belt | -11.5 | -5.8 | -4.7 | +0.5 | -1.5 | 1384 |
| 112 | Central Michigan | Mid-American | -11.6 | -6.2 | -4.3 | -0.1 | -1.1 | 1418 |
| 113 | South Alabama | Sun Belt | -11.8 | -0.2 | -10.6 | +0.3 | -1.3 | 1398 |
| 114 | Colorado State | Pac-12 | -11.9 | +3.0 | -12.0 | -0.3 | -2.6 | 1286 |
| 115 | Western Kentucky | Conference USA | -12.3 | -6.8 | -3.3 | -0.3 | -1.9 | 1345 |
| 116 | Rice | American Athletic | -12.8 | -3.7 | -5.1 | -0.8 | -3.1 | 1246 |
| 117 | Kennesaw State | Conference USA | -12.8 | -6.5 | -3.6 | -0.8 | -1.9 | 1346 |
| 118 | Old Dominion | Sun Belt | -12.9 | -13.0 | +3.4 | -1.6 | -1.8 | 1357 |
| 119 | Missouri State | Conference USA | -13.1 | -1.6 | -7.4 | -1.4 | -2.7 | 1281 |
| 120 | Nevada | Mountain West | -14.7 | -10.9 | -1.9 | +0.3 | -2.4 | 1309 |
| 121 | Florida International | Conference USA | -15.0 | -10.1 | -1.8 | -1.4 | -1.8 | 1353 |
| 122 | Southern Miss | Sun Belt | -15.2 | -7.9 | -3.8 | -1.2 | -2.2 | 1318 |
| 123 | New Mexico State | Conference USA | -15.7 | -8.5 | -2.7 | -1.8 | -2.8 | 1275 |
| 124 | San José State | Mountain West | -15.9 | -9.8 | -3.5 | -0.1 | -2.4 | 1303 |
| 125 | Buffalo | Mid-American | -16.9 | -11.6 | -5.3 | +0.4 | -0.5 | 1469 |
| 126 | Massachusetts | Mid-American | -16.9 | -9.0 | -4.3 | -0.3 | -3.3 | 1229 |
| 127 | Ball State | Mid-American | -17.1 | -5.7 | -7.7 | -0.6 | -3.2 | 1241 |
| 128 | Middle Tennessee | Conference USA | -17.3 | -7.1 | -7.3 | +0.1 | -3.0 | 1257 |
| 129 | UL Monroe | Sun Belt | -18.1 | -6.4 | -6.2 | -1.4 | -4.0 | 1168 |
| 130 | Northern Illinois | Mountain West | -18.2 | -3.7 | -9.3 | -1.0 | -4.3 | 1145 |
| 131 | Bowling Green | Mid-American | -18.6 | -11.7 | -4.1 | -0.0 | -2.8 | 1270 |
| 132 | Sam Houston | Conference USA | -19.0 | -12.6 | -0.9 | -1.3 | -4.3 | 1145 |
| 133 | Eastern Michigan | Mid-American | -19.1 | -8.0 | -7.8 | -0.7 | -2.6 | 1287 |
| 134 | Charlotte | American Athletic | -20.1 | -6.9 | -9.2 | -0.5 | -3.6 | 1203 |
| 135 | Sacramento State | Mid-American | -20.3 | -12.0 | -4.4 | +0.3 | -4.3 | 1147 |
| 136 | Kent State | Mid-American | -20.8 | -10.8 | -6.1 | -0.8 | -3.2 | 1241 |
| 137 | Akron | Mid-American | -22.7 | -10.3 | -8.0 | -0.8 | -3.7 | 1198 |
| 138 | UTEP | Mountain West | -24.0 | -11.6 | -6.5 | -1.3 | -4.7 | 1112 |

## Current model fit

- Fitted on 4256 games from seasons 2022–2026.
- Home field on top of the ratings: 3.2 points (1.9 in conference games).
- Extra FBS edge over FCS opponents beyond their ratings: 14.1 points.
- Elo weight: 0.19 points of margin per point of Elo spread.
- Weight on the betting line: 91% for the margin, 81% for the total.
