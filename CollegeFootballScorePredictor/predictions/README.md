# College football score predictions

Updated Sun Nov 22, 2026 03:51 AM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 13

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/24 7:00 PM | Kent State @ Eastern Michigan | Kent State 21, Eastern Michigan 28 | Eastern Michigan 67% | Kent State +210 / Eastern Michigan -210 | 20.3 – 26.8 | 7–33 / 13–41 | Eastern Michigan -6.6 / Eastern Michigan -6.5 | 49.6 / 46.5 | no edge | no edge | no edge |  |
| Tue 11/24 7:00 PM | Miami (OH) @ Western Michigan | Miami (OH) 20, Western Michigan 27 | Western Michigan 68% | Miami (OH) +215 / Western Michigan -215 | 19.9 – 26.9 | 7–32 / 13–41 | Western Michigan -1.9 / Western Michigan -7.5 | 47.9 / 46.5 | no edge | Miami (OH) (+240): EV +4.3%, 31%, stake 0.4u | no edge |  |
| Thu 11/26 8:00 PM | TCU @ Texas Tech | TCU 17, Texas Tech 31 | Texas Tech 78% | TCU +360 / Texas Tech -360 | 17.8 – 29.0 | 7–31 / 14–44 | Texas Tech -17.7 / Texas Tech -10.5 | 44.0 / 47.5 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Mississippi State @ Ole Miss | Mississippi State 17, Ole Miss 38 | Ole Miss 90% | Mississippi State +910 / Ole Miss -910 | 18.9 – 38.8 | 7–31 / 24–55 | Ole Miss -14.8 / Ole Miss -20.5 | 58.8 / 57.5 | no edge | Mississippi State (+800): EV +9.8%, 12%, stake 0.3u | no edge |  |
| Fri 11/27 12:00 PM | Nebraska @ Iowa | Nebraska 17, Iowa 24 | Iowa 68% | Nebraska +210 / Iowa -210 | 16.8 – 22.8 | 6–28 / 10–37 | Iowa -5.5 / Iowa -6.0 | 44.8 / 38.5 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Tulsa @ UTSA | Tulsa 28, UTSA 31 | UTSA 60% | Tulsa +150 / UTSA -150 | 26.5 – 30.3 | 13–41 / 16–45 | UTSA -3.8 / – | 56.8 / – | no line yet | no line yet (fair: UTSA -150) | no line yet |  |
| Fri 11/27 12:00 PM | Buffalo @ Akron | Buffalo 28, Akron 21 | Buffalo 74% | Buffalo -285 / Akron +285 | 29.8 – 20.0 | 16–45 / 7–34 | Buffalo -8.1 / Buffalo -10.0 | 51.9 / 49.5 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Toledo @ Ohio | Toledo 24, Ohio 21 | Toledo 61% | Toledo -155 / Ohio +155 | 25.8 – 21.8 | 13–40 / 10–35 | Toledo -4.0 / – | 48.2 / – | no line yet | no line yet (fair: Toledo -155) | no line yet |  |
| Fri 11/27 3:00 PM | App State @ South Alabama | App State 28, South Alabama 31 | South Alabama 57% | App State +130 / South Alabama -130 | 28.2 – 31.0 | 14–42 / 17–45 | South Alabama -2.8 / – | 59.2 / – | no line yet | no line yet (fair: South Alabama -130) | no line yet |  |
| Fri 11/27 3:30 PM | Florida @ Florida State | Florida 27, Florida State 24 | Florida 62% | Florida -165 / Florida State +165 | 29.7 – 25.0 | 16–44 / 12–38 | Florida -5.8 / Florida -4.5 | 55.5 / 54.5 | no edge | no edge | no edge |  |
| Fri 11/27 3:30 PM | Temple @ Memphis | Temple 21, Memphis 38 | Memphis 88% | Temple +730 / Memphis -730 | 21.6 – 39.4 | 9–35 / 24–55 | Memphis -17.8 / – | 61.0 / – | no line yet | no line yet (fair: Memphis -730) | no line yet |  |
| Fri 11/27 3:30 PM | North Dakota State @ San José State | North Dakota State 31, San José State 17 | North Dakota State 82% | North Dakota State -450 / San José State +450 | 27.8 – 15.2 | 14–42 / 5–27 | North Dakota State -12.6 / – | 43.0 / – | no line yet | no line yet (fair: North Dakota State -450) | no line yet |  |
| Fri 11/27 4:30 PM | Air Force @ New Mexico | Air Force 21, New Mexico 24 | New Mexico 63% | Air Force +165 / New Mexico -165 | 20.7 – 25.4 | 7–34 / 13–40 | New Mexico -4.7 / – | 48.4 / – | no line yet | no line yet (fair: New Mexico -165) | no line yet |  |
| Fri 11/27 7:30 PM | Texas @ Texas A&M | Texas 24, Texas A&M 17 | Texas 76% | Texas -320 / Texas A&M +320 | 24.7 – 15.0 | 10–38 / 3–27 | Texas -12.3 / Texas -9.5 | 40.6 / 39.5 | no edge | no edge | no edge |  |
| Fri 11/27 7:30 PM | Minnesota @ Wisconsin | Minnesota 17, Wisconsin 24 | Wisconsin 73% | Minnesota +275 / Wisconsin -275 | 15.2 – 23.7 | 5–27 / 10–37 | Wisconsin -8.5 / – | 38.9 / – | no line yet | no line yet (fair: Wisconsin -275) | no line yet |  |
| Fri 11/27 9:00 PM | West Virginia @ Utah | West Virginia 17, Utah 45 | Utah 95% | West Virginia +1815 / Utah -1815 | 19.7 – 44.3 | 7–32 / 29–60 | Utah -24.5 / – | 64.0 / – | no line yet | no line yet (fair: Utah -1815) | no line yet |  |
| Sat 11/28 TBA | Auburn @ Alabama | Auburn 17, Alabama 31 | Alabama 83% | Auburn +475 / Alabama -475 | 18.5 – 32.1 | 7–31 / 17–48 | Alabama -10.0 / Alabama -14.0 | 51.2 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | LSU @ Arkansas | LSU 38, Arkansas 17 | LSU 91% | LSU -995 / Arkansas +995 | 35.6 – 16.4 | 21–52 / 6–28 | LSU -19.3 / – | 52.0 / – | no line yet | no line yet (fair: LSU -995) | no line yet |  |
| Sat 11/28 TBA | Georgia Tech @ Georgia | Georgia Tech 7, Georgia 45 | Georgia 100% | Georgia Tech +9900 / Georgia -9900 | 6.4 – 43.8 | 0–13 / 29–60 | Georgia -37.4 / – | 50.2 / – | no line yet | no line yet (fair: Georgia -9900) | no line yet |  |
| Sat 11/28 TBA | Louisville @ Kentucky | Louisville 27, Kentucky 24 | Louisville 55% | Louisville -125 / Kentucky +125 | 27.6 – 25.7 | 14–42 / 13–40 | Louisville -5.5 / Louisville -1.5 | 52.5 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | South Carolina @ Clemson | South Carolina 24, Clemson 21 | South Carolina 59% | South Carolina -145 / Clemson +145 | 23.3 – 20.0 | 10–37 / 7–33 | South Carolina -0.5 / South Carolina -3.5 | 46.9 / 42.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Tennessee @ Vanderbilt | Tennessee 31, Vanderbilt 17 | Tennessee 83% | Tennessee -495 / Vanderbilt +495 | 29.2 – 15.7 | 15–44 / 5–28 | Tennessee -13.3 / Tennessee -13.5 | 47.2 / 44.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Duke @ Wake Forest | Duke 20, Wake Forest 34 | Wake Forest 82% | Duke +450 / Wake Forest -450 | 20.5 – 34.4 | 7–34 / 20–50 | Wake Forest -17.4 / Wake Forest -13.5 | 52.5 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | SMU @ Stanford | SMU 34, Stanford 20 | SMU 81% | SMU -435 / Stanford +435 | 35.1 – 21.4 | 20–50 / 9–35 | SMU -13.7 / – | 56.5 / – | no line yet | no line yet (fair: SMU -435) | no line yet |  |
| Sat 11/28 TBA | Purdue @ Indiana | Purdue 10, Indiana 38 | Indiana 97% | Purdue +2950 / Indiana -2950 | 12.3 – 37.5 | 3–23 / 23–53 | Indiana -25.1 / – | 49.8 / – | no line yet | no line yet (fair: Indiana -2950) | no line yet |  |
| Sat 11/28 TBA | Washington @ Oregon | Washington 17, Oregon 31 | Oregon 80% | Washington +400 / Oregon -400 | 18.4 – 31.0 | 7–31 / 17–46 | Oregon -13.5 / Oregon -12.5 | 49.0 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Boston College @ Miami | Boston College 10, Miami 42 | Miami 99% | Boston College +9060 / Miami -9060 | 11.5 – 44.1 | 3–21 / 30–60 | Miami -32.7 / – | 55.6 / – | no line yet | no line yet (fair: Miami -9060) | no line yet |  |
| Sat 11/28 12:00 PM | NC State @ North Carolina | NC State 31, North Carolina 28 | NC State 53% | NC State -110 / North Carolina +110 | 28.6 – 27.4 | 14–43 / 14–42 | North Carolina -1.7 / NC State -1.5 | 58.2 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Notre Dame @ Syracuse | Notre Dame 38, Syracuse 14 | Notre Dame 95% | Notre Dame -1915 / Syracuse +1915 | 38.2 – 14.1 | 23–54 / 3–26 | Notre Dame -20.9 / Notre Dame -24.5 | 51.5 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Michigan @ Ohio State | Michigan 14, Ohio State 24 | Ohio State 80% | Michigan +410 / Ohio State -410 | 14.0 – 25.8 | 3–25 / 13–40 | Ohio State -14.2 / Ohio State -11.5 | 45.6 / 38.5 | no edge | no edge | Over 38.5 (-110*): EV +3.3%, 54%, stake 0.9u | * price not posted; assumed -110 |
| Sat 11/28 12:00 PM | UConn @ Wyoming | UConn 27, Wyoming 24 | UConn 61% | UConn -160 / Wyoming +160 | 28.0 – 23.7 | 14–42 / 10–37 | UConn -4.3 / – | 55.7 / – | no line yet | no line yet (fair: UConn -160) | no line yet |  |
| Sat 11/28 12:00 PM | Navy @ Charlotte | Navy 34, Charlotte 17 | Navy 89% | Navy -840 / Charlotte +840 | 35.1 – 17.1 | 20–51 / 6–30 | Navy -18.0 / – | 52.2 / – | no line yet | no line yet (fair: Navy -840) | no line yet |  |
| Sat 11/28 12:00 PM | Central Michigan @ Ball State | Central Michigan 27, Ball State 24 | Central Michigan 61% | Central Michigan -160 / Ball State +160 | 26.9 – 22.7 | 14–41 / 10–37 | Central Michigan -4.2 / – | 51.0 / – | no line yet | no line yet (fair: Central Michigan -160) | no line yet |  |
| Sat 11/28 12:00 PM | Louisiana Tech @ Georgia Southern | Louisiana Tech 24, Georgia Southern 27 | Louisiana Tech 50% | Louisiana Tech -100 / Georgia Southern +100 | 25.2 – 24.9 | 13–38 / 12–38 | Louisiana Tech -0.3 / – | 50.0 / – | no line yet | no line yet (fair: Louisiana Tech -100) | no line yet |  |
| Sat 11/28 12:30 PM | Illinois @ Northwestern | Illinois 24, Northwestern 27 | Northwestern 62% | Illinois +160 / Northwestern -160 | 22.4 – 26.7 | 10–35 / 14–41 | Northwestern -7.1 / Northwestern -4.0 | 56.5 / 47.5 | no edge | no edge | Over 47.5 (-110*): EV +3.8%, 54%, stake 1.1u | * price not posted; assumed -110 |
| Sat 11/28 1:00 PM | Florida Atlantic @ East Carolina | Florida Atlantic 28, East Carolina 31 | East Carolina 60% | Florida Atlantic +150 / East Carolina -150 | 27.2 – 30.7 | 14–41 / 17–45 | East Carolina -3.5 / – | 57.8 / – | no line yet | no line yet (fair: East Carolina -150) | no line yet |  |
| Sat 11/28 1:00 PM | Kennesaw State @ Western Kentucky | Kennesaw State 24, Western Kentucky 27 | Western Kentucky 52% | Kennesaw State +105 / Western Kentucky -105 | 25.9 – 26.4 | 13–40 / 13–41 | Western Kentucky -0.6 / – | 54.1 / – | no line yet | no line yet (fair: Western Kentucky -105) | no line yet |  |
| Sat 11/28 1:00 PM | Marshall @ UL Monroe | Marshall 31, UL Monroe 24 | Marshall 65% | Marshall -190 / UL Monroe +190 | 30.0 – 24.0 | 16–45 / 10–38 | Marshall -6.0 / – | 53.9 / – | no line yet | no line yet (fair: Marshall -190) | no line yet |  |
| Sat 11/28 1:00 PM | Southern Miss @ Old Dominion | Southern Miss 20, Old Dominion 27 | Old Dominion 73% | Southern Miss +270 / Old Dominion -270 | 18.9 – 28.1 | 7–31 / 14–42 | Old Dominion -9.1 / – | 47.0 / – | no line yet | no line yet (fair: Old Dominion -270) | no line yet |  |
| Sat 11/28 2:00 PM | UCF @ Colorado | UCF 24, Colorado 27 | Colorado 54% | UCF +120 / Colorado -120 | 25.0 – 26.6 | 13–39 / 13–41 | Colorado -1.6 / – | 51.6 / – | no line yet | no line yet (fair: Colorado -120) | no line yet |  |
| Sat 11/28 2:00 PM | Kansas State @ Iowa State | Kansas State 24, Iowa State 27 | Iowa State 56% | Kansas State +130 / Iowa State -130 | 24.8 – 26.9 | 10–38 / 14–41 | Iowa State -2.1 / – | 53.9 / – | no line yet | no line yet (fair: Iowa State -130) | no line yet |  |
| Sat 11/28 2:00 PM | Army @ Rice | Army 31, Rice 24 | Army 65% | Army -190 / Rice +190 | 31.4 – 25.5 | 17–45 / 13–40 | Army -5.9 / – | 56.9 / – | no line yet | no line yet (fair: Army -190) | no line yet |  |
| Sat 11/28 2:00 PM | Coastal Carolina @ James Madison | Coastal Carolina 17, James Madison 34 | James Madison 86% | Coastal Carolina +625 / James Madison -625 | 17.7 – 33.7 | 7–30 / 20–49 | James Madison -16.0 / – | 51.4 / – | no line yet | no line yet (fair: James Madison -625) | no line yet |  |
| Sat 11/28 2:00 PM | Louisiana @ Georgia State | Louisiana 31, Georgia State 28 | Louisiana 53% | Louisiana -115 / Georgia State +115 | 28.5 – 27.2 | 14–42 / 13–41 | Louisiana -1.3 / – | 55.6 / – | no line yet | no line yet (fair: Louisiana -115) | no line yet |  |
| Sat 11/28 2:00 PM | Liberty @ Missouri State | Liberty 34, Missouri State 17 | Liberty 88% | Liberty -745 / Missouri State +745 | 34.1 – 17.3 | 20–49 / 6–30 | Liberty -16.9 / – | 52.6 / – | no line yet | no line yet (fair: Liberty -745) | no line yet |  |
| Sat 11/28 2:00 PM | Sam Houston @ Florida International | Sam Houston 17, Florida International 24 | Florida International 73% | Sam Houston +275 / Florida International -275 | 16.2 – 24.5 | 6–28 / 10–38 | Florida International -8.4 / – | 40.7 / – | no line yet | no line yet (fair: Florida International -275) | no line yet |  |
| Sat 11/28 2:00 PM | New Mexico State @ Middle Tennessee | New Mexico State 24, Middle Tennessee 27 | Middle Tennessee 64% | New Mexico State +180 / Middle Tennessee -180 | 22.7 – 28.3 | 10–36 / 14–42 | Middle Tennessee -5.6 / – | 51.1 / – | no line yet | no line yet (fair: Middle Tennessee -180) | no line yet |  |
| Sat 11/28 3:00 PM | Virginia @ Virginia Tech | Virginia 24, Virginia Tech 27 | Virginia Tech 57% | Virginia +130 / Virginia Tech -130 | 25.2 – 27.9 | 13–38 / 14–42 | Virginia -0.4 / Virginia Tech -3.0 | 51.7 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/28 3:00 PM | Troy @ Arkansas State | Troy 21, Arkansas State 24 | Arkansas State 64% | Troy +175 / Arkansas State -175 | 20.4 – 25.4 | 7–34 / 13–39 | Arkansas State -5.0 / – | 47.3 / – | no line yet | no line yet (fair: Arkansas State -175) | no line yet |  |
| Sat 11/28 3:30 PM | Cincinnati @ BYU | Cincinnati 24, BYU 34 | BYU 76% | Cincinnati +315 / BYU -315 | 23.2 – 34.4 | 10–38 / 20–49 | BYU -11.2 / – | 57.7 / – | no line yet | no line yet (fair: BYU -315) | no line yet |  |
| Sat 11/28 3:30 PM | Penn State @ Maryland | Penn State 24, Maryland 21 | Penn State 66% | Penn State -195 / Maryland +195 | 26.0 – 20.1 | 13–41 / 7–34 | Penn State -5.9 / – | 46.2 / – | no line yet | no line yet (fair: Penn State -195) | no line yet |  |
| Sat 11/28 3:30 PM | USC @ UCLA | USC 27, UCLA 24 | USC 63% | USC -175 / UCLA +175 | 26.8 – 21.5 | 13–41 / 10–35 | UCLA -7.2 / USC -6.5 | 52.0 / 47.5 | no edge | UCLA (+200): EV +4.6%, 35%, stake 0.6u | no edge |  |
| Sat 11/28 3:30 PM | Tulane @ South Florida | Tulane 24, South Florida 27 | South Florida 66% | Tulane +190 / South Florida -190 | 22.5 – 28.7 | 10–36 / 14–44 | South Florida -6.2 / – | 51.2 / – | no line yet | no line yet (fair: South Florida -190) | no line yet |  |
| Sat 11/28 3:30 PM | UTEP @ Northern Illinois | UTEP 21, Northern Illinois 31 | Northern Illinois 75% | UTEP +300 / Northern Illinois -300 | 20.5 – 30.3 | 7–34 / 16–45 | Northern Illinois -9.8 / – | 50.7 / – | no line yet | no line yet (fair: Northern Illinois -300) | no line yet |  |
| Sat 11/28 3:30 PM | Massachusetts @ Bowling Green | Massachusetts 17, Bowling Green 20 | Bowling Green 61% | Massachusetts +160 / Bowling Green -160 | 17.3 – 21.2 | 7–30 / 9–34 | Bowling Green -3.9 / – | 39.7 / – | no line yet | no line yet (fair: Bowling Green -160) | no line yet |  |
| Sat 11/28 3:30 PM | Jacksonville State @ Delaware | Jacksonville State 28, Delaware 31 | Delaware 55% | Jacksonville State +120 / Delaware -120 | 27.9 – 29.8 | 14–42 / 16–45 | Delaware -2.0 / – | 57.7 / – | no line yet | no line yet (fair: Delaware -120) | no line yet |  |
| Sat 11/28 4:00 PM | UAB @ North Texas | UAB 24, North Texas 34 | North Texas 74% | UAB +290 / North Texas -290 | 24.0 – 34.1 | 10–38 / 20–49 | North Texas -10.0 / – | 58.1 / – | no line yet | no line yet (fair: North Texas -290) | no line yet |  |
| Sat 11/28 4:15 PM | Oklahoma @ Missouri | Oklahoma 21, Missouri 24 | Missouri 53% | Oklahoma +115 / Missouri -115 | 20.7 – 21.7 | 9–34 / 10–35 | Oklahoma -3.7 / Missouri -1.5 | 42.2 / 42.5 | no edge | no edge | no edge |  |
| Sat 11/28 4:15 PM | Michigan State @ Rutgers | Michigan State 27, Rutgers 24 | Rutgers 51% | Michigan State +105 / Rutgers -105 | 25.4 – 25.6 | 13–39 / 13–40 | Rutgers -0.2 / – | 51.1 / – | no line yet | no line yet (fair: Rutgers -105) | no line yet |  |
| Sat 11/28 6:15 PM | Kansas @ Oklahoma State | Kansas 28, Oklahoma State 31 | Oklahoma State 55% | Kansas +125 / Oklahoma State -125 | 28.5 – 30.8 | 14–43 / 17–45 | Oklahoma State -2.3 / – | 59.3 / – | no line yet | no line yet (fair: Oklahoma State -125) | no line yet |  |
| Sat 11/28 7:30 PM | Pittsburgh @ California | Pittsburgh 31, California 21 | Pittsburgh 72% | Pittsburgh -255 / California +255 | 29.4 – 20.7 | 15–44 / 7–34 | Pittsburgh -8.7 / – | 50.0 / – | no line yet | no line yet (fair: Pittsburgh -255) | no line yet |  |
| Sat 11/28 9:00 PM | Arizona State @ Arizona | Arizona State 24, Arizona 27 | Arizona 63% | Arizona State +165 / Arizona -165 | 24.0 – 28.7 | 10–38 / 14–44 | Arizona -6.1 / Arizona -4.5 | 53.8 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/28 9:00 PM | Nevada @ UNLV | Nevada 17, UNLV 27 | UNLV 78% | Nevada +350 / UNLV -350 | 17.8 – 29.0 | 7–31 / 14–44 | UNLV -11.3 / – | 46.8 / – | no line yet | no line yet (fair: UNLV -350) | no line yet |  |
| Sat 11/28 9:30 PM | Baylor @ Houston | Baylor 27, Houston 30 | Houston 54% | Baylor +120 / Houston -120 | 27.8 – 29.4 | 14–42 / 16–44 | Houston -1.6 / – | 57.2 / – | no line yet | no line yet (fair: Houston -120) | no line yet |  |
| Sat 11/28 11:00 PM | Sacramento State @ Hawai'i | Sacramento State 17, Hawai'i 31 | Hawai'i 84% | Sacramento State +545 / Hawai'i -545 | 17.2 – 31.4 | 6–30 / 17–47 | Hawai'i -14.3 / – | 48.6 / – | no line yet | no line yet (fair: Hawai'i -545) | no line yet |  |

## 2026 Week 15

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sat 12/12 3:00 PM | Navy vs Army | Navy 20, Army 17 | Navy 59% | Navy -140 / Army +140 | 21.9 – 19.2 | 10–35 / 7–31 | Navy -4.2 / Navy -2.5 | 57.7 / 37.5 | no edge | no edge | Over 37.5 (-110*): EV +15.5%, 60%, stake 3.0u | neutral site, * price not posted; assumed -110 |

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
