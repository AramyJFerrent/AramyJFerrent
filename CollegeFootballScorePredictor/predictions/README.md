# College football score predictions

Updated Sun Nov 22, 2026 03:27 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 13

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/24 7:00 PM | Kent State @ Eastern Michigan | Kent State 20, Eastern Michigan 27 | Eastern Michigan 67% | Kent State +200 / Eastern Michigan -200 | 20.1 – 26.1 | 7–33 / 13–41 | Eastern Michigan -6.6 / Eastern Michigan -6.0 | 49.6 / 45.5 | no edge | no edge | no edge |  |
| Tue 11/24 7:00 PM | Miami (OH) @ Western Michigan | Miami (OH) 17, Western Michigan 24 | Western Michigan 68% | Miami (OH) +210 / Western Michigan -210 | 19.7 – 26.2 | 7–32 / 13–41 | Western Michigan -1.9 / Western Michigan -7.0 | 47.9 / 45.5 | no edge | no edge | no edge |  |
| Thu 11/26 8:00 PM | TCU @ Texas Tech | TCU 17, Texas Tech 31 | Texas Tech 82% | TCU +470 / Texas Tech -470 | 16.5 – 29.5 | 6–28 / 15–45 | Texas Tech -17.7 / Texas Tech -12.5 | 44.0 / 46.5 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Mississippi State @ Ole Miss | Mississippi State 17, Ole Miss 38 | Ole Miss 88% | Mississippi State +760 / Ole Miss -760 | 19.4 – 37.5 | 7–32 / 22–53 | Ole Miss -14.8 / Ole Miss -18.5 | 58.8 / 56.5 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Nebraska @ Iowa | Nebraska 17, Iowa 24 | Iowa 66% | Nebraska +195 / Iowa -195 | 17.9 – 23.4 | 7–30 / 10–37 | Iowa -5.5 / Iowa -5.5 | 44.8 / 40.5 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Tulsa @ UTSA | Tulsa 28, UTSA 31 | UTSA 54% | Tulsa +120 / UTSA -120 | 28.6 – 30.4 | 14–43 / 17–45 | UTSA -3.8 / UTSA -1.5 | 56.8 / 59.5 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Buffalo @ Akron | Buffalo 28, Akron 21 | Buffalo 72% | Buffalo -250 / Akron +250 | 29.5 – 21.0 | 15–44 / 8–35 | Buffalo -8.1 / Buffalo -8.5 | 51.9 / 50.5 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Toledo @ Ohio | Toledo 27, Ohio 24 | Toledo 60% | Toledo -150 / Ohio +150 | 26.6 – 22.6 | 13–41 / 10–36 | Toledo -4.0 / Toledo -4.0 | 48.2 / 49.5 | no edge | no edge | no edge |  |
| Fri 11/27 3:00 PM | App State @ South Alabama | App State 28, South Alabama 31 | South Alabama 56% | App State +130 / South Alabama -130 | 27.2 – 29.8 | 14–41 / 16–45 | South Alabama -2.8 / South Alabama -2.5 | 59.2 / 56.5 | no edge | no edge | no edge |  |
| Fri 11/27 3:30 PM | Florida @ Florida State | Florida 31, Florida State 24 | Florida 64% | Florida -175 / Florida State +175 | 29.3 – 23.8 | 15–44 / 10–38 | Florida -5.8 / Florida -5.5 | 55.5 / 52.5 | no edge | no edge | no edge |  |
| Fri 11/27 3:30 PM | Temple @ Memphis | Temple 24, Memphis 41 | Memphis 87% | Temple +655 / Memphis -655 | 23.2 – 40.7 | 10–37 / 25–56 | Memphis -17.8 / Memphis -17.5 | 61.0 / 64.5 | no edge | no edge | no edge |  |
| Fri 11/27 3:30 PM | North Dakota State @ San José State | North Dakota State 24, San José State 14 | North Dakota State 80% | North Dakota State -410 / San José State +410 | 25.9 – 14.3 | 13–41 / 3–26 | North Dakota State -12.6 / North Dakota State -11.5 | 43.0 / 39.5 | no edge | no edge | no edge |  |
| Fri 11/27 4:30 PM | Air Force @ New Mexico | Air Force 17, New Mexico 24 | New Mexico 67% | Air Force +205 / New Mexico -205 | 18.2 – 24.5 | 7–31 / 10–38 | New Mexico -4.7 / New Mexico -6.5 | 48.4 / 41.5 | no edge | no edge | no edge |  |
| Fri 11/27 7:30 PM | Texas @ Texas A&M | Texas 24, Texas A&M 14 | Texas 78% | Texas -355 / Texas A&M +355 | 25.2 – 14.5 | 12–39 / 3–27 | Texas -12.3 / Texas -10.5 | 40.6 / 39.5 | no edge | no edge | no edge |  |
| Fri 11/27 7:30 PM | Minnesota @ Wisconsin | Minnesota 14, Wisconsin 21 | Wisconsin 70% | Minnesota +230 / Wisconsin -230 | 14.9 – 22.0 | 3–27 / 10–35 | Wisconsin -8.5 / Wisconsin -7.0 | 38.9 / 36.5 | no edge | no edge | no edge |  |
| Fri 11/27 9:00 PM | West Virginia @ Utah | West Virginia 24, Utah 45 | Utah 91% | West Virginia +960 / Utah -960 | 23.8 – 44.7 | 10–38 / 30–60 | Utah -24.5 / Utah -20.5 | 64.0 / 69.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Auburn @ Alabama | Auburn 17, Alabama 34 | Alabama 86% | Auburn +615 / Alabama -615 | 17.4 – 33.3 | 6–30 / 17–49 | Alabama -10.0 / Alabama -16.5 | 51.2 / 50.5 | no edge | Auburn (+470): EV +3.4%, 18%, stake 0.2u | no edge |  |
| Sat 11/28 TBA | LSU @ Arkansas | LSU 31, Arkansas 17 | LSU 84% | LSU -525 / Arkansas +525 | 31.1 – 17.1 | 17–46 / 6–30 | LSU -19.3 / LSU -13.5 | 52.0 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Georgia Tech @ Georgia | Georgia Tech 10, Georgia 45 | Georgia 99% | Georgia Tech +9900 / Georgia -9900 | 9.4 – 45.1 | 0–18 / 31–62 | Georgia -37.4 / Georgia -35.5 | 50.2 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Louisville @ Kentucky | Louisville 27, Kentucky 24 | Louisville 58% | Louisville -140 / Kentucky +140 | 28.9 – 26.1 | 14–43 / 13–41 | Louisville -5.5 / Louisville -2.5 | 52.5 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | South Carolina @ Clemson | South Carolina 24, Clemson 21 | South Carolina 60% | South Carolina -150 / Clemson +150 | 22.3 – 18.6 | 10–35 / 7–31 | South Carolina -0.5 / South Carolina -4.0 | 46.9 / 39.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Tennessee @ Vanderbilt | Tennessee 27, Vanderbilt 17 | Tennessee 78% | Tennessee -350 / Vanderbilt +350 | 27.5 – 16.7 | 14–42 / 6–29 | Tennessee -13.3 / Tennessee -10.5 | 47.2 / 43.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Duke @ Wake Forest | Duke 17, Wake Forest 34 | Wake Forest 83% | Duke +475 / Wake Forest -475 | 20.7 – 35.0 | 7–34 / 20–51 | Wake Forest -17.4 / Wake Forest -14.0 | 52.5 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | SMU @ Stanford | SMU 31, Stanford 24 | SMU 71% | SMU -250 / Stanford +250 | 34.4 – 25.4 | 20–49 / 13–40 | SMU -13.7 / SMU -8.5 | 56.5 / 60.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Purdue @ Indiana | Purdue 14, Indiana 38 | Indiana 94% | Purdue +1620 / Indiana -1620 | 14.6 – 37.4 | 3–26 / 21–53 | Indiana -25.1 / Indiana -22.5 | 49.8 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Washington @ Oregon | Washington 17, Oregon 31 | Oregon 82% | Washington +450 / Oregon -450 | 18.0 – 31.5 | 7–31 / 17–47 | Oregon -13.5 / Oregon -13.5 | 49.0 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Boston College @ Miami | Boston College 13, Miami 41 | Miami 97% | Boston College +2960 / Miami -2960 | 13.9 – 40.0 | 3–24 / 24–56 | Miami -32.7 / Miami -25.5 | 55.6 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | NC State @ North Carolina | NC State 28, North Carolina 31 | North Carolina 63% | NC State +170 / North Carolina -170 | 25.4 – 30.6 | 13–40 / 17–45 | North Carolina -1.7 / North Carolina -5.5 | 58.2 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Notre Dame @ Syracuse | Notre Dame 38, Syracuse 10 | Notre Dame 96% | Notre Dame -2295 / Syracuse +2295 | 38.7 – 13.6 | 24–55 / 3–24 | Notre Dame -20.9 / Notre Dame -25.5 | 51.5 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Michigan @ Ohio State | Michigan 17, Ohio State 24 | Ohio State 78% | Michigan +355 / Ohio State -355 | 14.7 – 25.0 | 3–27 / 13–38 | Ohio State -14.2 / Ohio State -10.0 | 45.6 / 38.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | UConn @ Wyoming | UConn 27, Wyoming 24 | UConn 60% | UConn -150 / Wyoming +150 | 26.6 – 23.0 | 13–41 / 10–36 | UConn -4.3 / UConn -3.5 | 55.7 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Navy @ Charlotte | Navy 38, Charlotte 21 | Navy 86% | Navy -625 / Charlotte +625 | 36.2 – 19.5 | 21–52 / 7–33 | Navy -18.0 / Navy -16.5 | 52.2 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Central Michigan @ Ball State | Central Michigan 24, Ball State 21 | Central Michigan 64% | Central Michigan -180 / Ball State +180 | 26.2 – 20.8 | 13–41 / 8–34 | Central Michigan -4.2 / Central Michigan -5.5 | 51.0 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Louisiana Tech @ Georgia Southern | Louisiana Tech 24, Georgia Southern 27 | Georgia Southern 56% | Louisiana Tech +130 / Georgia Southern -130 | 24.9 – 27.1 | 13–38 / 14–42 | Louisiana Tech -0.3 / Georgia Southern -2.5 | 50.0 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:30 PM | Illinois @ Northwestern | Illinois 24, Northwestern 27 | Northwestern 59% | Illinois +145 / Northwestern -145 | 23.7 – 27.1 | 10–37 / 14–42 | Northwestern -7.1 / Northwestern -3.0 | 56.5 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/28 1:00 PM | Florida Atlantic @ East Carolina | Florida Atlantic 28, East Carolina 31 | East Carolina 58% | Florida Atlantic +135 / East Carolina -135 | 26.7 – 29.3 | 13–41 / 16–44 | East Carolina -3.5 / East Carolina -2.5 | 57.8 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/28 1:00 PM | Kennesaw State @ Western Kentucky | Kennesaw State 27, Western Kentucky 24 | Kennesaw State 56% | Kennesaw State -125 / Western Kentucky +125 | 27.8 – 25.6 | 14–42 / 13–40 | Western Kentucky -0.6 / Kennesaw State -2.5 | 54.1 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/28 1:00 PM | Marshall @ UL Monroe | Marshall 27, UL Monroe 24 | Marshall 62% | Marshall -165 / UL Monroe +165 | 27.9 – 23.2 | 14–42 / 10–37 | Marshall -6.0 / Marshall -4.5 | 53.9 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/28 1:00 PM | Southern Miss @ Old Dominion | Southern Miss 24, Old Dominion 27 | Old Dominion 63% | Southern Miss +170 / Old Dominion -170 | 22.5 – 27.4 | 10–36 / 14–42 | Old Dominion -9.1 / Old Dominion -4.5 | 47.0 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/28 2:00 PM | UCF @ Colorado | UCF 24, Colorado 27 | Colorado 56% | UCF +130 / Colorado -130 | 24.6 – 27.0 | 10–38 / 13–41 | Colorado -1.6 / Colorado -2.5 | 51.6 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/28 2:00 PM | Kansas State @ Iowa State | Kansas State 24, Iowa State 27 | Iowa State 61% | Kansas State +155 / Iowa State -155 | 24.9 – 29.2 | 12–38 / 15–44 | Iowa State -2.1 / Iowa State -4.5 | 53.9 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/28 2:00 PM | Army @ Rice | Army 28, Rice 21 | Army 67% | Army -200 / Rice +200 | 28.2 – 21.8 | 14–42 / 10–35 | Army -5.9 / Army -6.5 | 56.9 / 48.5 | no edge | no edge | Over 48.5 (-110*): EV +4.7%, 55%, stake 1.3u | * price not posted; assumed -110 |
| Sat 11/28 2:00 PM | Coastal Carolina @ James Madison | Coastal Carolina 17, James Madison 34 | James Madison 85% | Coastal Carolina +560 / James Madison -560 | 19.6 – 35.2 | 7–33 / 20–51 | James Madison -16.0 / James Madison -15.5 | 51.4 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/28 2:00 PM | Louisiana @ Georgia State | Louisiana 31, Georgia State 28 | Louisiana 64% | Louisiana -175 / Georgia State +175 | 30.7 – 25.6 | 17–45 / 13–39 | Louisiana -1.3 / Louisiana -5.5 | 55.6 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/28 2:00 PM | Liberty @ Missouri State | Liberty 31, Missouri State 17 | Liberty 84% | Liberty -530 / Missouri State +530 | 33.2 – 18.5 | 18–48 / 7–31 | Liberty -16.9 / Liberty -14.5 | 52.6 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/28 2:00 PM | Sam Houston @ Florida International | Sam Houston 14, Florida International 24 | Florida International 80% | Sam Houston +390 / Florida International -390 | 14.7 – 25.9 | 3–26 / 13–41 | Florida International -8.4 / Florida International -11.5 | 40.7 / 40.5 | no edge | no edge | no edge |  |
| Sat 11/28 2:00 PM | New Mexico State @ Middle Tennessee | New Mexico State 24, Middle Tennessee 27 | Middle Tennessee 59% | New Mexico State +140 / Middle Tennessee -140 | 24.5 – 27.7 | 10–38 / 14–42 | Middle Tennessee -5.6 / Middle Tennessee -3.0 | 51.1 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/28 3:00 PM | Virginia @ Virginia Tech | Virginia 24, Virginia Tech 27 | Virginia Tech 58% | Virginia +140 / Virginia Tech -140 | 24.6 – 27.7 | 10–38 / 14–42 | Virginia -0.4 / Virginia Tech -3.5 | 51.7 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/28 3:00 PM | Troy @ Arkansas State | Troy 21, Arkansas State 24 | Arkansas State 60% | Troy +150 / Arkansas State -150 | 21.5 – 25.1 | 9–35 / 13–38 | Arkansas State -5.0 / Arkansas State -3.5 | 47.3 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/28 3:30 PM | Cincinnati @ BYU | Cincinnati 24, BYU 38 | BYU 81% | Cincinnati +420 / BYU -420 | 21.5 – 35.2 | 9–35 / 20–50 | BYU -11.2 / BYU -14.0 | 57.7 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/28 3:30 PM | Penn State @ Maryland | Penn State 28, Maryland 21 | Penn State 70% | Penn State -230 / Maryland +230 | 28.1 – 20.8 | 14–42 / 7–34 | Penn State -5.9 / Penn State -7.5 | 46.2 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/28 3:30 PM | USC @ UCLA | USC 24, UCLA 21 | USC 64% | USC -180 / UCLA +180 | 26.6 – 20.9 | 13–41 / 9–34 | UCLA -7.2 / USC -7.0 | 52.0 / 46.5 | UCLA +7.0 (-110*): EV +4.0%, 51%, stake 1.2u | UCLA (+210): EV +7.9%, 35%, stake 0.9u | no edge | * price not posted; assumed -110 |
| Sat 11/28 3:30 PM | Tulane @ South Florida | Tulane 17, South Florida 24 | South Florida 67% | Tulane +205 / South Florida -205 | 18.8 – 25.3 | 7–31 / 13–40 | South Florida -6.2 / South Florida -6.5 | 51.2 / 42.5 | no edge | no edge | Over 42.5 (-110*): EV +3.6%, 54%, stake 1.0u | * price not posted; assumed -110 |
| Sat 11/28 3:30 PM | UTEP @ Northern Illinois | UTEP 24, Northern Illinois 27 | Northern Illinois 66% | UTEP +195 / Northern Illinois -195 | 21.4 – 27.3 | 9–35 / 14–42 | Northern Illinois -9.8 / Northern Illinois -5.5 | 50.7 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/28 3:30 PM | Massachusetts @ Bowling Green | Massachusetts 21, Bowling Green 24 | Bowling Green 55% | Massachusetts +120 / Bowling Green -120 | 20.4 – 22.1 | 7–34 / 10–35 | Bowling Green -3.9 / Bowling Green -1.5 | 39.7 / 43.5 | no edge | no edge | no edge |  |
| Sat 11/28 3:30 PM | Jacksonville State @ Delaware | Jacksonville State 28, Delaware 31 | Delaware 56% | Jacksonville State +125 / Delaware -125 | 27.5 – 30.0 | 14–42 / 16–45 | Delaware -2.0 / Delaware -2.5 | 57.7 / 57.5 | no edge | no edge | no edge |  |
| Sat 11/28 4:00 PM | UAB @ North Texas | UAB 24, North Texas 27 | North Texas 63% | UAB +170 / North Texas -170 | 22.1 – 27.2 | 10–35 / 14–42 | North Texas -10.0 / North Texas -4.5 | 58.1 / 47.5 | no edge | no edge | Over 47.5 (-110*): EV +3.0%, 54%, stake 0.8u | * price not posted; assumed -110 |
| Sat 11/28 4:15 PM | Oklahoma @ Missouri | Oklahoma 17, Missouri 20 | Missouri 54% | Oklahoma +115 / Missouri -115 | 19.9 – 20.9 | 7–33 / 9–34 | Oklahoma -3.7 / Missouri -1.5 | 42.2 / 40.5 | no edge | no edge | no edge |  |
| Sat 11/28 4:15 PM | Michigan State @ Rutgers | Michigan State 27, Rutgers 24 | Michigan State 57% | Michigan State -130 / Rutgers +130 | 25.8 – 23.1 | 13–40 / 10–37 | Rutgers -0.2 / Michigan State -3.0 | 51.1 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/28 6:15 PM | Kansas @ Oklahoma State | Kansas 31, Oklahoma State 34 | Oklahoma State 65% | Kansas +185 / Oklahoma State -185 | 29.6 – 35.7 | 16–44 / 21–51 | Oklahoma State -2.3 / Oklahoma State -6.5 | 59.3 / 66.5 | no edge | no edge | no edge |  |
| Sat 11/28 7:30 PM | Pittsburgh @ California | Pittsburgh 28, California 21 | Pittsburgh 72% | Pittsburgh -260 / California +260 | 28.2 – 19.7 | 14–42 / 7–33 | Pittsburgh -8.7 / Pittsburgh -8.5 | 50.0 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/28 9:00 PM | Arizona State @ Arizona | Arizona State 24, Arizona 31 | Arizona 69% | Arizona State +225 / Arizona -225 | 23.5 – 30.9 | 10–37 / 17–45 | Arizona -6.1 / Arizona -7.5 | 53.8 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/28 9:00 PM | Nevada @ UNLV | Nevada 21, UNLV 24 | UNLV 64% | Nevada +180 / UNLV -180 | 19.1 – 24.2 | 7–31 / 10–38 | UNLV -11.3 / UNLV -4.5 | 46.8 / 42.5 | no edge | no edge | no edge |  |
| Sat 11/28 9:30 PM | Baylor @ Houston | Baylor 24, Houston 27 | Houston 61% | Baylor +155 / Houston -155 | 25.8 – 30.0 | 13–40 / 17–45 | Houston -1.6 / Houston -4.5 | 57.2 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/28 11:00 PM | Sacramento State @ Hawai'i | Sacramento State 13, Hawai'i 27 | Hawai'i 84% | Sacramento State +540 / Hawai'i -540 | 13.4 – 26.9 | 3–24 / 13–41 | Hawai'i -14.3 / Hawai'i -13.5 | 48.6 / 38.5 | no edge | no edge | Over 38.5 (-110*): EV +6.9%, 56%, stake 1.9u | * price not posted; assumed -110 |

## 2026 Week 15

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sat 12/12 3:00 PM | Navy vs Army | Navy 20, Army 17 | Navy 58% | Navy -140 / Army +140 | 21.9 – 19.2 | 10–35 / 7–31 | Navy -4.2 / Navy -2.5 | 57.7 / 37.5 | no edge | no edge | Over 37.5 (-110*): EV +16.1%, 61%, stake 3.0u | neutral site, * price not posted; assumed -110 |

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
