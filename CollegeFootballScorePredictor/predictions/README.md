# College football score predictions

Updated Sun Nov 08, 2026 01:27 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 11

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/10 7:00 PM | Western Michigan @ Akron | Western Michigan 31, Akron 17 | Western Michigan 84% | Western Michigan -525 / Akron +525 | 31.0 – 16.9 | 17–46 / 6–29 | Western Michigan -14.8 / Western Michigan -14.0 | 49.8 / 47.5 | no edge | no edge | no edge |  |
| Tue 11/10 7:00 PM | Kent State @ Bowling Green | Kent State 17, Bowling Green 24 | Bowling Green 66% | Kent State +190 / Bowling Green -190 | 19.2 – 24.7 | 7–31 / 10–38 | Bowling Green -5.4 / Bowling Green -5.5 | 41.5 / 44.5 | no edge | no edge | no edge |  |
| Tue 11/10 8:00 PM | Ohio @ Miami (OH) | Ohio 21, Miami (OH) 24 | Miami (OH) 53% | Ohio +110 / Miami (OH) -110 | 23.3 – 24.4 | 10–37 / 10–38 | Ohio -2.8 / Miami (OH) -1.5 | 48.5 / 47.5 | no edge | no edge | no edge |  |
| Wed 11/11 7:30 PM | Buffalo @ Ball State | Buffalo 27, Ball State 24 | Buffalo 57% | Buffalo -130 / Ball State +130 | 27.2 – 24.5 | 14–41 / 10–38 | Ball State -0.9 / Buffalo -3.0 | 52.9 / 51.5 | no edge | no edge | no edge |  |
| Wed 11/11 7:30 PM | Sacramento State @ Central Michigan | Sacramento State 17, Central Michigan 31 | Central Michigan 87% | Sacramento State +640 / Central Michigan -640 | 14.8 – 29.9 | 3–27 / 16–45 | Central Michigan -11.0 / Central Michigan -15.5 | 45.8 / 44.5 | no edge | no edge | no edge |  |
| Wed 11/11 7:30 PM | Massachusetts @ Toledo | Massachusetts 17, Toledo 31 | Toledo 83% | Massachusetts +505 / Toledo -505 | 19.1 – 33.5 | 7–31 / 19–49 | Toledo -18.9 / Toledo -14.0 | 48.8 / 53.5 | no edge | no edge | no edge |  |
| Thu 11/12 8:00 PM | Memphis @ South Florida | Memphis 27, South Florida 24 | Memphis 66% | Memphis -190 / South Florida +190 | 27.8 – 21.8 | 14–42 / 10–35 | Memphis -0.8 / Memphis -6.5 | 55.1 / 48.5 | no edge | no edge | no edge |  |
| Thu 11/12 9:00 PM | Louisiana @ UL Monroe | Louisiana 31, UL Monroe 17 | Louisiana 78% | Louisiana -350 / UL Monroe +350 | 30.2 – 19.1 | 16–45 / 7–31 | Louisiana -6.0 / Louisiana -11.5 | 52.7 / 48.5 | no edge | no edge | no edge |  |
| Fri 11/13 7:00 PM | Florida State @ Pittsburgh | Florida State 24, Pittsburgh 27 | Pittsburgh 59% | Florida State +145 / Pittsburgh -145 | 25.2 – 28.6 | 12–39 / 14–43 | Pittsburgh -2.2 / Pittsburgh -3.5 | 55.5 / 53.5 | no edge | no edge | no edge |  |
| Fri 11/13 9:00 PM | Illinois @ UCLA | Illinois 17, UCLA 27 | UCLA 76% | Illinois +310 / UCLA -310 | 18.9 – 28.8 | 7–31 / 14–44 | UCLA -14.2 / UCLA -9.5 | 52.6 / 46.5 | no edge | no edge | no edge |  |
| Fri 11/13 10:15 PM | Houston @ Colorado | Houston 28, Colorado 21 | Houston 76% | Houston -315 / Colorado +315 | 30.3 – 20.1 | 16–45 / 7–33 | Houston -6.9 / Houston -10.5 | 54.1 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Arizona State @ UCF | Arizona State 24, UCF 27 | UCF 57% | Arizona State +135 / UCF -135 | 24.2 – 27.0 | 10–38 / 14–42 | UCF -0.7 / UCF -3.0 | 50.4 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Baylor @ BYU | Baylor 21, BYU 28 | BYU 68% | Baylor +215 / BYU -215 | 21.1 – 28.0 | 9–34 / 14–42 | BYU -6.1 / BYU -7.0 | 52.2 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Cincinnati @ Iowa State | Cincinnati 28, Iowa State 31 | Iowa State 54% | Cincinnati +120 / Iowa State -120 | 29.4 – 31.1 | 14–44 / 17–46 | Iowa State -4.1 / Iowa State -1.5 | 60.9 / 60.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Kansas @ West Virginia | Kansas 31, West Virginia 34 | West Virginia 55% | Kansas +125 / West Virginia -125 | 31.1 – 33.3 | 17–45 / 19–48 | Kansas -2.2 / West Virginia -2.5 | 64.0 / 64.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Kansas State @ TCU | Kansas State 17, TCU 24 | TCU 73% | Kansas State +275 / TCU -275 | 18.6 – 27.4 | 7–31 / 14–42 | TCU -1.3 / TCU -9.5 | 48.2 / 45.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Texas Tech @ Oklahoma State | Texas Tech 31, Oklahoma State 34 | Oklahoma State 56% | Texas Tech +125 / Oklahoma State -125 | 33.7 – 36.0 | 20–49 / 21–51 | Texas Tech -5.9 / Oklahoma State -3.0 | 57.5 / 72.5 | no edge | no edge | Under 72.5 (-110*): EV +7.9%, 57%, stake 2.2u | * price not posted; assumed -110 |
| Sat 11/14 TBA | Utah @ Arizona | Utah 27, Arizona 24 | Utah 57% | Utah -130 / Arizona +130 | 28.4 – 25.6 | 14–43 / 13–40 | Utah -5.7 / Utah -2.5 | 56.1 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Missouri @ Georgia | Missouri 17, Georgia 31 | Georgia 83% | Missouri +470 / Georgia -470 | 16.8 – 30.3 | 6–28 / 16–45 | Georgia -14.2 / Georgia -13.5 | 45.8 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Florida @ Kentucky | Florida 24, Kentucky 27 | Kentucky 57% | Florida +135 / Kentucky -135 | 24.6 – 27.3 | 10–38 / 14–42 | Florida -0.6 / Kentucky -3.0 | 51.3 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Texas @ LSU | Texas 21, LSU 24 | LSU 60% | Texas +150 / LSU -150 | 21.1 – 25.3 | 9–35 / 13–40 | LSU -5.6 / LSU -4.0 | 45.9 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Ole Miss @ Oklahoma | Ole Miss 27, Oklahoma 24 | Ole Miss 55% | Ole Miss -125 / Oklahoma +125 | 26.3 – 24.1 | 13–40 / 10–38 | Oklahoma -2.2 / Ole Miss -2.5 | 49.9 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Tennessee @ Texas A&M | Tennessee 24, Texas A&M 21 | Tennessee 59% | Tennessee -145 / Texas A&M +145 | 23.1 – 19.9 | 10–37 / 7–33 | Tennessee -4.6 / Tennessee -3.0 | 45.4 / 42.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Louisville @ North Carolina | Louisville 31, North Carolina 28 | Louisville 57% | Louisville -130 / North Carolina +130 | 31.4 – 28.3 | 17–46 / 14–43 | Louisville -9.8 / Louisville -2.5 | 57.2 / 60.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Stanford @ Virginia Tech | Stanford 21, Virginia Tech 38 | Virginia Tech 86% | Stanford +625 / Virginia Tech -625 | 21.1 – 37.5 | 7–35 / 22–52 | Virginia Tech -15.5 / Virginia Tech -16.5 | 56.3 / 59.5 | no edge | no edge | no edge |  |
| Sat 11/14 12:00 PM | Auburn @ Mississippi State | Auburn 27, Mississippi State 24 | Auburn 60% | Auburn -150 / Mississippi State +150 | 27.4 – 24.1 | 14–42 / 10–38 | Auburn -1.4 / Auburn -3.5 | 55.9 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/14 12:00 PM | Duke @ Miami | Duke 17, Miami 34 | Miami 84% | Duke +510 / Miami -510 | 20.1 – 34.7 | 7–34 / 20–50 | Miami -16.1 / Miami -14.5 | 56.8 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/14 12:00 PM | Syracuse @ NC State | Syracuse 31, NC State 28 | Syracuse 55% | Syracuse -120 / NC State +120 | 29.2 – 27.2 | 14–44 / 14–42 | NC State -2.9 / Syracuse -2.5 | 57.5 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/14 12:00 PM | Wake Forest @ SMU | Wake Forest 31, SMU 28 | Wake Forest 56% | Wake Forest -125 / SMU +125 | 31.3 – 28.9 | 17–45 / 14–44 | Wake Forest -1.1 / Wake Forest -2.5 | 54.6 / 61.5 | no edge | no edge | no edge |  |
| Sat 11/14 12:00 PM | Wisconsin @ Maryland | Wisconsin 24, Maryland 17 | Wisconsin 70% | Wisconsin -230 / Maryland +230 | 25.4 – 18.2 | 12–40 / 7–31 | Wisconsin -3.8 / Wisconsin -7.5 | 44.5 / 43.5 | no edge | no edge | no edge |  |
| Sat 11/14 12:00 PM | Northwestern @ Ohio State | Northwestern 17, Ohio State 27 | Ohio State 78% | Northwestern +350 / Ohio State -350 | 18.8 – 29.7 | 7–31 / 16–45 | Ohio State -15.7 / Ohio State -10.5 | 54.1 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/14 12:00 PM | James Madison @ UConn | James Madison 31, UConn 28 | James Madison 58% | James Madison -140 / UConn +140 | 29.8 – 26.7 | 16–45 / 13–41 | James Madison -3.3 / James Madison -3.0 | 56.4 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/14 12:30 PM | Georgia Tech @ Clemson | Georgia Tech 17, Clemson 31 | Clemson 82% | Georgia Tech +470 / Clemson -470 | 17.9 – 31.5 | 7–31 / 17–47 | Clemson -15.0 / Clemson -13.5 | 49.7 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/14 12:30 PM | Nebraska @ Rutgers | Nebraska 34, Rutgers 17 | Nebraska 82% | Nebraska -460 / Rutgers +460 | 33.5 – 19.9 | 19–48 / 7–33 | Nebraska -13.7 / Nebraska -13.5 | 54.0 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/14 12:45 PM | Alabama @ Vanderbilt | Alabama 38, Vanderbilt 17 | Alabama 91% | Alabama -975 / Vanderbilt +975 | 36.4 – 17.3 | 21–52 / 6–30 | Alabama -14.6 / Alabama -19.5 | 50.4 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/14 1:00 PM | East Carolina @ Charlotte | East Carolina 31, Charlotte 17 | East Carolina 79% | East Carolina -385 / Charlotte +385 | 29.0 – 17.2 | 14–44 / 7–30 | East Carolina -15.5 / East Carolina -11.5 | 49.1 / 45.5 | no edge | no edge | no edge |  |
| Sat 11/14 1:00 PM | UAB @ Temple | UAB 24, Temple 27 | Temple 57% | UAB +135 / Temple -135 | 24.4 – 26.8 | 10–38 / 14–41 | Temple -2.3 / Temple -2.5 | 50.6 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/14 1:00 PM | Arkansas State @ Coastal Carolina | Arkansas State 24, Coastal Carolina 27 | Coastal Carolina 54% | Arkansas State +115 / Coastal Carolina -115 | 24.5 – 26.0 | 10–38 / 13–41 | Coastal Carolina -1.5 / Coastal Carolina -1.5 | 51.4 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/14 2:00 PM | Tulane @ Rice | Tulane 21, Rice 24 | Rice 53% | Tulane +110 / Rice -110 | 24.0 – 25.0 | 10–38 / 12–38 | Tulane -4.6 / Rice -1.5 | 50.8 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/14 2:00 PM | Kennesaw State @ Sam Houston | Kennesaw State 24, Sam Houston 17 | Kennesaw State 72% | Kennesaw State -255 / Sam Houston +255 | 26.8 – 18.5 | 13–41 / 7–31 | Kennesaw State -6.0 / Kennesaw State -8.5 | 44.5 / 45.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:00 PM | New Mexico State @ Missouri State | New Mexico State 24, Missouri State 27 | Missouri State 57% | New Mexico State +135 / Missouri State -135 | 24.1 – 26.8 | 10–38 / 13–41 | Missouri State -4.7 / Missouri State -2.5 | 52.3 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:00 PM | Florida International @ Delaware | Florida International 24, Delaware 31 | Delaware 65% | Florida International +190 / Delaware -190 | 23.8 – 30.1 | 10–38 / 16–45 | Delaware -10.5 / Delaware -6.0 | 52.4 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Boston College @ Notre Dame | Boston College 10, Notre Dame 42 | Notre Dame 99% | Boston College +9275 / Notre Dame -9275 | 10.3 – 42.0 | 0–20 / 27–59 | Notre Dame -34.3 / Notre Dame -31.5 | 47.9 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | California @ Virginia | California 17, Virginia 31 | Virginia 80% | California +395 / Virginia -395 | 17.9 – 30.1 | 7–31 / 16–45 | Virginia -9.5 / Virginia -12.5 | 50.6 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | USC @ Indiana | USC 21, Indiana 28 | Indiana 70% | USC +230 / Indiana -230 | 21.3 – 28.5 | 9–35 / 14–43 | Indiana -9.7 / Indiana -7.0 | 50.8 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Michigan @ Oregon | Michigan 14, Oregon 24 | Oregon 78% | Michigan +350 / Oregon -350 | 15.4 – 25.8 | 3–27 / 13–41 | Oregon -10.3 / Oregon -10.5 | 44.3 / 40.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Florida Atlantic @ Tulsa | Florida Atlantic 31, Tulsa 38 | Tulsa 63% | Florida Atlantic +170 / Tulsa -170 | 32.2 – 37.4 | 17–48 / 23–53 | Tulsa -2.8 / Tulsa -5.5 | 66.0 / 70.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Nevada @ Northern Illinois | Nevada 27, Northern Illinois 17 | Nevada 74% | Nevada -290 / Northern Illinois +290 | 27.9 – 19.0 | 14–42 / 7–31 | Nevada -2.6 / Nevada -9.5 | 48.8 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Georgia Southern @ Georgia State | Georgia Southern 31, Georgia State 24 | Georgia Southern 63% | Georgia Southern -170 / Georgia State +170 | 30.4 – 25.4 | 17–45 / 13–40 | PK / Georgia Southern -5.5 | 57.9 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Jacksonville State @ Western Kentucky | Jacksonville State 31, Western Kentucky 24 | Jacksonville State 67% | Jacksonville State -200 / Western Kentucky +200 | 29.7 – 23.2 | 16–44 / 10–37 | Jacksonville State -5.8 / Jacksonville State -6.5 | 54.9 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Middle Tennessee @ Liberty | Middle Tennessee 17, Liberty 38 | Liberty 92% | Middle Tennessee +1175 / Liberty -1175 | 16.2 – 36.8 | 6–28 / 21–52 | Liberty -21.6 / Liberty -20.5 | 51.6 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/14 4:00 PM | Fresno State @ Texas State | Fresno State 24, Texas State 31 | Texas State 69% | Fresno State +220 / Texas State -220 | 25.6 – 33.1 | 13–40 / 18–49 | Texas State -6.9 / Texas State -7.5 | 60.1 / 58.5 | no edge | no edge | no edge |  |
| Sat 11/14 4:15 PM | Washington @ Michigan State | Washington 24, Michigan State 21 | Washington 60% | Washington -150 / Michigan State +150 | 24.6 – 20.8 | 10–38 / 7–34 | Washington -7.0 / Washington -3.5 | 45.6 / 45.5 | no edge | no edge | no edge |  |
| Sat 11/14 5:00 PM | Southern Miss @ Louisiana Tech | Southern Miss 17, Louisiana Tech 34 | Louisiana Tech 90% | Southern Miss +860 / Louisiana Tech -860 | 17.8 – 36.1 | 7–31 / 21–52 | Louisiana Tech -15.8 / Louisiana Tech -18.5 | 51.7 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/14 6:00 PM | Oregon State @ Boise State | Oregon State 28, Boise State 35 | Boise State 73% | Oregon State +265 / Boise State -265 | 27.3 – 36.7 | 14–42 / 21–52 | Boise State -8.8 / Boise State -9.5 | 61.7 / 64.5 | no edge | no edge | no edge |  |
| Sat 11/14 6:00 PM | App State @ Marshall | App State 27, Marshall 24 | App State 55% | App State -120 / Marshall +120 | 27.9 – 25.9 | 14–42 / 13–40 | Marshall -2.9 / App State -2.5 | 55.2 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/14 7:00 PM | Minnesota @ Penn State | Minnesota 17, Penn State 24 | Penn State 72% | Minnesota +250 / Penn State -250 | 17.6 – 25.3 | 7–30 / 13–39 | Penn State -10.3 / Penn State -7.5 | 41.6 / 43.5 | no edge | no edge | no edge |  |
| Sat 11/14 7:00 PM | San José State @ Air Force | San José State 17, Air Force 31 | Air Force 77% | San José State +335 / Air Force -335 | 19.7 – 30.5 | 7–33 / 17–45 | Air Force -13.7 / Air Force -10.5 | 53.1 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/14 7:00 PM | Troy @ South Alabama | Troy 24, South Alabama 27 | South Alabama 59% | Troy +145 / South Alabama -145 | 26.5 – 29.6 | 13–41 / 16–45 | South Alabama -4.0 / South Alabama -3.0 | 54.4 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/14 7:30 PM | Purdue @ Iowa | Purdue 14, Iowa 31 | Iowa 89% | Purdue +790 / Iowa -790 | 14.7 – 31.3 | 3–27 / 17–47 | Iowa -18.0 / Iowa -16.5 | 48.4 / 45.5 | no edge | no edge | no edge |  |
| Sat 11/14 7:30 PM | UNLV @ New Mexico | UNLV 17, New Mexico 31 | New Mexico 82% | UNLV +445 / New Mexico -445 | 17.2 – 30.3 | 6–30 / 16–45 | New Mexico -8.8 / New Mexico -13.5 | 47.1 / 47.5 | no edge | UNLV (+470): EV +3.7%, 18%, stake 0.2u | no edge |  |
| Sat 11/14 7:45 PM | South Carolina @ Arkansas | South Carolina 31, Arkansas 24 | South Carolina 73% | South Carolina -265 / Arkansas +265 | 30.4 – 21.7 | 17–45 / 10–35 | South Carolina -10.4 / South Carolina -8.5 | 54.9 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/14 9:00 PM | North Texas @ UTSA | North Texas 38, UTSA 35 | North Texas 53% | North Texas -115 / UTSA +115 | 37.8 – 36.5 | 23–54 / 21–52 | UTSA -0.7 / North Texas -1.5 | 69.1 / 75.5 | no edge | no edge | no edge |  |
| Sat 11/14 9:30 PM | Utah State @ San Diego State | Utah State 24, San Diego State 21 | Utah State 56% | Utah State -130 / San Diego State +130 | 23.6 – 21.5 | 10–38 / 9–35 | San Diego State -1.9 / Utah State -2.5 | 47.6 / 44.5 | no edge | no edge | no edge |  |
| Sat 11/14 10:00 PM | Wyoming @ UTEP | Wyoming 24, UTEP 17 | Wyoming 75% | Wyoming -305 / UTEP +305 | 26.9 – 17.0 | 13–41 / 6–30 | Wyoming -14.0 / Wyoming -9.5 | 45.9 / 43.5 | no edge | no edge | no edge |  |
| Sat 11/14 10:30 PM | Colorado State @ Washington State | Colorado State 27, Washington State 34 | Washington State 67% | Colorado State +205 / Washington State -205 | 27.9 – 34.8 | 14–42 / 20–50 | Washington State -5.2 / Washington State -7.0 | 58.9 / 63.5 | no edge | no edge | no edge |  |
| Sat 11/14 11:00 PM | North Dakota State @ Hawai'i | North Dakota State 24, Hawai'i 17 | North Dakota State 73% | North Dakota State -275 / Hawai'i +275 | 25.0 – 16.6 | 11–38 / 6–28 | North Dakota State -6.8 / North Dakota State -8.5 | 47.4 / 40.5 | no edge | no edge | no edge |  |

## 2026 Week 12

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/17 7:00 PM | Ball State @ Ohio | Ball State 17, Ohio 34 | Ohio 88% | Ball State +705 / Ohio -705 | 17.2 – 34.0 | 6–30 / 20–49 | Ohio -16.8 / – | 51.3 / – | no line yet | no line yet (fair: Ohio -705) | no line yet |  |
| Tue 11/17 7:00 PM | Eastern Michigan @ Western Michigan | Eastern Michigan 17, Western Michigan 31 | Western Michigan 86% | Eastern Michigan +640 / Western Michigan -640 | 17.2 – 33.1 | 6–30 / 18–49 | Western Michigan -15.8 / – | 51.0 / – | no line yet | no line yet (fair: Western Michigan -640) | no line yet |  |
| Tue 11/17 7:00 PM | Miami (OH) @ Kent State | Miami (OH) 27, Kent State 17 | Miami (OH) 77% | Miami (OH) -330 / Kent State +330 | 28.6 – 18.0 | 14–44 / 7–31 | Miami (OH) -10.6 / – | 46.6 / – | no line yet | no line yet (fair: Miami (OH) -330) | no line yet |  |
| Wed 11/18 TBA | Akron @ Massachusetts | Akron 21, Massachusetts 28 | Massachusetts 72% | Akron +265 / Massachusetts -265 | 19.7 – 28.0 | 7–32 / 14–42 | Massachusetts -8.3 / – | 47.7 / – | no line yet | no line yet (fair: Massachusetts -265) | no line yet |  |
| Wed 11/18 7:30 PM | Central Michigan @ Buffalo | Central Michigan 27, Buffalo 24 | Central Michigan 56% | Central Michigan -130 / Buffalo +130 | 26.3 – 23.9 | 13–41 / 10–38 | Central Michigan -2.4 / – | 50.1 / – | no line yet | no line yet (fair: Central Michigan -130) | no line yet |  |
| Thu 11/19 7:30 PM | Rice @ Temple | Rice 24, Temple 31 | Temple 65% | Rice +185 / Temple -185 | 23.9 – 29.8 | 10–38 / 16–45 | Temple -6.0 / – | 53.7 / – | no line yet | no line yet (fair: Temple -185) | no line yet |  |
| Fri 11/20 6:00 PM | Iowa State @ UCF | Iowa State 27, UCF 24 | Iowa State 55% | Iowa State -120 / UCF +120 | 27.0 – 25.3 | 13–41 / 13–39 | Iowa State -1.6 / – | 52.3 / – | no line yet | no line yet (fair: Iowa State -120) | no line yet |  |
| Fri 11/20 7:30 PM | Clemson @ Duke | Clemson 21, Duke 24 | Duke 65% | Clemson +185 / Duke -185 | 20.4 – 25.9 | 7–34 / 13–41 | Duke -5.5 / – | 46.3 / – | no line yet | no line yet (fair: Duke -185) | no line yet |  |
| Fri 11/20 7:30 PM | Bowling Green @ Toledo | Bowling Green 10, Toledo 31 | Toledo 93% | Bowling Green +1430 / Toledo -1430 | 12.4 – 32.5 | 3–23 / 17–48 | Toledo -20.1 / – | 44.9 / – | no line yet | no line yet (fair: Toledo -1430) | no line yet |  |
| Fri 11/20 8:00 PM | Oregon @ Michigan State | Oregon 31, Michigan State 14 | Oregon 91% | Oregon -965 / Michigan State +965 | 32.3 – 14.2 | 17–48 / 3–25 | Oregon -18.1 / – | 46.5 / – | no line yet | no line yet (fair: Oregon -965) | no line yet |  |
| Fri 11/20 8:00 PM | UTEP @ Air Force | UTEP 14, Air Force 38 | Air Force 95% | UTEP +2035 / Air Force -2035 | 13.8 – 37.4 | 3–24 / 23–54 | Air Force -23.7 / – | 51.2 / – | no line yet | no line yet (fair: Air Force -2035) | no line yet |  |
| Fri 11/20 9:00 PM | New Mexico @ Wyoming | New Mexico 24, Wyoming 17 | New Mexico 69% | New Mexico -220 / Wyoming +220 | 25.4 – 18.2 | 13–39 / 7–31 | New Mexico -7.1 / – | 43.6 / – | no line yet | no line yet (fair: New Mexico -220) | no line yet |  |
| Sat 11/21 TBA | Vanderbilt @ Florida | Vanderbilt 24, Florida 31 | Florida 70% | Vanderbilt +240 / Florida -240 | 22.1 – 30.5 | 10–35 / 16–45 | Florida -8.4 / – | 52.6 / – | no line yet | no line yet (fair: Florida -240) | no line yet |  |
| Sat 11/21 TBA | Kentucky @ Missouri | Kentucky 21, Missouri 28 | Missouri 72% | Kentucky +255 / Missouri -255 | 20.2 – 28.9 | 7–33 / 14–44 | Missouri -8.7 / – | 49.1 / – | no line yet | no line yet (fair: Missouri -255) | no line yet |  |
| Sat 11/21 TBA | Texas A&M @ Oklahoma | Texas A&M 21, Oklahoma 24 | Oklahoma 58% | Texas A&M +140 / Oklahoma -140 | 23.2 – 26.2 | 10–37 / 13–41 | Oklahoma -7.8 / Oklahoma -2.5 | 40.1 / 51.5 | no edge | no edge | Under 51.5 (-110*): EV +7.5%, 56%, stake 2.0u | * price not posted; assumed -110 |
| Sat 11/21 TBA | Georgia @ South Carolina | Georgia 31, South Carolina 21 | Georgia 78% | Georgia -360 / South Carolina +360 | 30.6 – 19.5 | 17–45 / 7–32 | Georgia -11.1 / – | 50.1 / – | no line yet | no line yet (fair: Georgia -360) | no line yet |  |
| Sat 11/21 TBA | LSU @ Tennessee | LSU 31, Tennessee 28 | LSU 54% | LSU -120 / Tennessee +120 | 28.8 – 27.2 | 14–43 / 14–41 | LSU -2.9 / LSU -1.5 | 49.2 / 57.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | Arkansas @ Texas | Arkansas 10, Texas 34 | Texas 95% | Arkansas +2045 / Texas -2045 | 11.8 – 34.6 | 3–22 / 20–51 | Texas -22.7 / – | 46.4 / – | no line yet | no line yet (fair: Texas -2045) | no line yet |  |
| Sat 11/21 TBA | Arizona @ Kansas State | Arizona 27, Kansas State 24 | Arizona 59% | Arizona -145 / Kansas State +145 | 29.0 – 25.8 | 14–44 / 13–40 | Arizona -3.1 / – | 54.8 / – | no line yet | no line yet (fair: Arizona -145) | no line yet |  |
| Sat 11/21 TBA | BYU @ Kansas | BYU 27, Kansas 24 | BYU 64% | BYU -180 / Kansas +180 | 29.1 – 23.6 | 15–44 / 10–38 | BYU -5.5 / – | 52.8 / – | no line yet | no line yet (fair: BYU -180) | no line yet |  |
| Sat 11/21 TBA | Colorado @ Cincinnati | Colorado 24, Cincinnati 31 | Cincinnati 67% | Colorado +200 / Cincinnati -200 | 25.6 – 32.5 | 13–40 / 17–48 | Cincinnati -6.9 / – | 58.1 / – | no line yet | no line yet (fair: Cincinnati -200) | no line yet |  |
| Sat 11/21 TBA | Houston @ West Virginia | Houston 38, West Virginia 31 | Houston 67% | Houston -200 / West Virginia +200 | 36.4 – 29.4 | 21–52 / 16–44 | Houston -6.9 / – | 65.8 / – | no line yet | no line yet (fair: Houston -200) | no line yet |  |
| Sat 11/21 TBA | Oklahoma State @ Arizona State | Oklahoma State 31, Arizona State 28 | Oklahoma State 56% | Oklahoma State -130 / Arizona State +130 | 30.2 – 27.7 | 16–45 / 14–42 | Oklahoma State -2.5 / – | 57.9 / – | no line yet | no line yet (fair: Oklahoma State -130) | no line yet |  |
| Sat 11/21 TBA | Texas Tech @ Baylor | Texas Tech 31, Baylor 24 | Texas Tech 65% | Texas Tech -190 / Baylor +190 | 29.0 – 23.1 | 14–44 / 10–37 | Texas Tech -5.9 / – | 52.1 / – | no line yet | no line yet (fair: Texas Tech -190) | no line yet |  |
| Sat 11/21 TBA | Utah @ TCU | Utah 31, TCU 17 | Utah 81% | Utah -420 / TCU +420 | 30.9 – 18.6 | 16–45 / 7–31 | Utah -12.3 / – | 49.5 / – | no line yet | no line yet (fair: Utah -420) | no line yet |  |
| Sat 11/21 TBA | Virginia Tech @ Miami | Virginia Tech 21, Miami 38 | Miami 87% | Virginia Tech +645 / Miami -645 | 20.0 – 36.9 | 7–34 / 21–52 | Miami -21.1 / Miami -16.5 | 58.6 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | NC State @ Florida State | NC State 28, Florida State 31 | Florida State 64% | NC State +180 / Florida State -180 | 27.5 – 33.3 | 14–42 / 19–49 | Florida State -5.8 / – | 60.9 / – | no line yet | no line yet (fair: Florida State -180) | no line yet |  |
| Sat 11/21 TBA | North Carolina @ Virginia | North Carolina 27, Virginia 24 | North Carolina 53% | North Carolina -115 / Virginia +115 | 26.3 – 25.0 | 13–41 / 12–38 | North Carolina -1.2 / – | 51.3 / – | no line yet | no line yet (fair: North Carolina -115) | no line yet |  |
| Sat 11/21 TBA | Pittsburgh @ Louisville | Pittsburgh 21, Louisville 35 | Louisville 84% | Pittsburgh +530 / Louisville -530 | 19.8 – 34.3 | 7–33 / 20–49 | Louisville -14.4 / – | 54.1 / – | no line yet | no line yet (fair: Louisville -530) | no line yet |  |
| Sat 11/21 TBA | Stanford @ California | Stanford 28, California 31 | California 62% | Stanford +160 / California -160 | 25.5 – 30.1 | 13–40 / 16–45 | California -4.6 / – | 55.6 / – | no line yet | no line yet (fair: California -160) | no line yet |  |
| Sat 11/21 TBA | Syracuse @ Boston College | Syracuse 27, Boston College 24 | Syracuse 61% | Syracuse -160 / Boston College +160 | 27.7 – 23.3 | 14–42 / 10–37 | Syracuse -4.4 / – | 50.9 / – | no line yet | no line yet (fair: Syracuse -160) | no line yet |  |
| Sat 11/21 TBA | Wake Forest @ Georgia Tech | Wake Forest 38, Georgia Tech 17 | Wake Forest 93% | Wake Forest -1280 / Georgia Tech +1280 | 38.4 – 17.0 | 23–55 / 6–29 | Wake Forest -21.4 / – | 55.5 / – | no line yet | no line yet (fair: Wake Forest -1280) | no line yet |  |
| Sat 11/21 TBA | Iowa @ Illinois | Iowa 27, Illinois 20 | Iowa 66% | Iowa -195 / Illinois +195 | 28.1 – 21.8 | 14–42 / 9–35 | Iowa -6.3 / – | 49.9 / – | no line yet | no line yet (fair: Iowa -195) | no line yet |  |
| Sat 11/21 TBA | UCLA @ Michigan | UCLA 24, Michigan 21 | UCLA 62% | UCLA -160 / Michigan +160 | 23.3 – 19.3 | 10–37 / 7–31 | UCLA -4.1 / – | 42.6 / – | no line yet | no line yet (fair: UCLA -160) | no line yet |  |
| Sat 11/21 TBA | Northwestern @ Minnesota | Northwestern 24, Minnesota 21 | Northwestern 60% | Northwestern -155 / Minnesota +155 | 25.3 – 21.5 | 13–39 / 9–35 | Northwestern -3.8 / – | 46.7 / – | no line yet | no line yet (fair: Northwestern -155) | no line yet |  |
| Sat 11/21 TBA | Ohio State @ Nebraska | Ohio State 28, Nebraska 21 | Ohio State 74% | Ohio State -285 / Nebraska +285 | 29.8 – 20.7 | 16–45 / 7–34 | Ohio State -9.1 / – | 50.5 / – | no line yet | no line yet (fair: Ohio State -285) | no line yet |  |
| Sat 11/21 TBA | Rutgers @ Penn State | Rutgers 17, Penn State 34 | Penn State 90% | Rutgers +895 / Penn State -895 | 17.0 – 35.4 | 6–29 / 20–51 | Penn State -18.4 / – | 52.4 / – | no line yet | no line yet (fair: Penn State -895) | no line yet |  |
| Sat 11/21 TBA | Wisconsin @ Purdue | Wisconsin 27, Purdue 20 | Wisconsin 68% | Wisconsin -215 / Purdue +215 | 27.5 – 20.5 | 14–42 / 7–34 | Wisconsin -7.0 / – | 48.0 / – | no line yet | no line yet (fair: Wisconsin -215) | no line yet |  |
| Sat 11/21 TBA | Maryland @ USC | Maryland 21, USC 34 | USC 82% | Maryland +445 / USC -445 | 20.9 – 34.4 | 7–34 / 20–49 | USC -13.5 / – | 55.3 / – | no line yet | no line yet (fair: USC -445) | no line yet |  |
| Sat 11/21 TBA | Indiana @ Washington | Indiana 27, Washington 17 | Indiana 77% | Indiana -340 / Washington +340 | 27.1 – 16.8 | 13–42 / 6–29 | Indiana -10.2 / – | 43.9 / – | no line yet | no line yet (fair: Indiana -340) | no line yet |  |
| Sat 11/21 TBA | Charlotte @ Tulsa | Charlotte 17, Tulsa 38 | Tulsa 94% | Charlotte +1465 / Tulsa -1465 | 16.1 – 38.2 | 6–28 / 23–55 | Tulsa -22.0 / – | 54.3 / – | no line yet | no line yet (fair: Tulsa -1465) | no line yet |  |
| Sat 11/21 TBA | South Florida @ Florida Atlantic | South Florida 28, Florida Atlantic 31 | Florida Atlantic 56% | South Florida +130 / Florida Atlantic -130 | 29.9 – 31.8 | 15–45 / 17–47 | Florida Atlantic -2.0 / – | 61.7 / – | no line yet | no line yet (fair: Florida Atlantic -130) | no line yet |  |
| Sat 11/21 TBA | North Texas @ Tulane | North Texas 34, Tulane 27 | North Texas 69% | North Texas -220 / Tulane +220 | 35.1 – 27.7 | 20–51 / 14–42 | North Texas -7.4 / – | 62.8 / – | no line yet | no line yet (fair: North Texas -220) | no line yet |  |
| Sat 11/21 TBA | UTSA @ UAB | UTSA 31, UAB 24 | UTSA 73% | UTSA -265 / UAB +265 | 31.5 – 22.5 | 17–46 / 10–36 | UTSA -9.0 / – | 54.0 / – | no line yet | no line yet (fair: UTSA -265) | no line yet |  |
| Sat 11/21 TBA | Hawai'i @ Nevada | Hawai'i 27, Nevada 24 | Hawai'i 57% | Hawai'i -130 / Nevada +130 | 25.4 – 22.9 | 13–39 / 10–37 | Hawai'i -2.5 / – | 48.2 / – | no line yet | no line yet (fair: Hawai'i -130) | no line yet |  |
| Sat 11/21 TBA | UL Monroe @ App State | UL Monroe 24, App State 34 | App State 76% | UL Monroe +310 / App State -310 | 21.9 – 32.3 | 10–35 / 17–48 | App State -10.4 / – | 54.2 / – | no line yet | no line yet (fair: App State -310) | no line yet |  |
| Sat 11/21 TBA | Arkansas State @ Louisiana Tech | Arkansas State 17, Louisiana Tech 31 | Louisiana Tech 76% | Arkansas State +325 / Louisiana Tech -325 | 19.8 – 30.7 | 7–34 / 17–45 | Louisiana Tech -11.0 / – | 50.5 / – | no line yet | no line yet (fair: Louisiana Tech -325) | no line yet |  |
| Sat 11/21 TBA | Coastal Carolina @ Louisiana | Coastal Carolina 24, Louisiana 27 | Louisiana 64% | Coastal Carolina +180 / Louisiana -180 | 22.7 – 27.7 | 10–36 / 14–42 | Louisiana -5.0 / – | 50.4 / – | no line yet | no line yet (fair: Louisiana -180) | no line yet |  |
| Sat 11/21 TBA | Georgia Southern @ Troy | Georgia Southern 27, Troy 24 | Georgia Southern 61% | Georgia Southern -155 / Troy +155 | 27.2 – 22.8 | 14–41 / 10–37 | Georgia Southern -4.4 / – | 50.0 / – | no line yet | no line yet (fair: Georgia Southern -155) | no line yet |  |
| Sat 11/21 TBA | Georgia State @ Marshall | Georgia State 28, Marshall 31 | Marshall 54% | Georgia State +115 / Marshall -115 | 28.2 – 29.7 | 14–42 / 16–45 | Marshall -1.5 / – | 57.9 / – | no line yet | no line yet (fair: Marshall -115) | no line yet |  |
| Sat 11/21 TBA | South Alabama @ Southern Miss | South Alabama 31, Southern Miss 28 | South Alabama 57% | South Alabama -130 / Southern Miss +130 | 31.3 – 28.8 | 17–47 / 14–43 | South Alabama -2.5 / – | 60.1 / – | no line yet | no line yet (fair: South Alabama -130) | no line yet |  |
| Sat 11/21 12:00 PM | Wofford @ Ole Miss | Wofford 3, Ole Miss 59 | Ole Miss 100% | Wofford +9900 / Ole Miss -9900 | 3.0 – 57.6 | 0–7 / 44–73 | Ole Miss -54.6 / – | 60.6 / – | no line yet | no line yet (fair: Ole Miss -9900) | no line yet | FCS opponent |
| Sat 11/21 12:00 PM | East Carolina @ Army | East Carolina 24, Army 27 | Army 54% | East Carolina +120 / Army -120 | 26.0 – 28.0 | 13–41 / 14–42 | Army -2.1 / – | 54.0 / – | no line yet | no line yet (fair: Army -120) | no line yet |  |
| Sat 11/21 12:00 PM | Memphis @ Navy | Memphis 31, Navy 28 | Memphis 52% | Memphis -110 / Navy +110 | 29.7 – 29.0 | 16–45 / 14–44 | Memphis -0.7 / – | 58.7 / – | no line yet | no line yet (fair: Memphis -110) | no line yet |  |
| Sat 11/21 1:00 PM | Tennessee Tech @ Mississippi State | Tennessee Tech 10, Mississippi State 42 | Mississippi State 99% | Tennessee Tech +8830 / Mississippi State -8830 | 10.2 – 41.5 | 0–20 / 27–58 | Mississippi State -31.4 / – | 51.7 / – | no line yet | no line yet (fair: Mississippi State -8830) | no line yet | FCS opponent |
| Sat 11/21 1:00 PM | Western Kentucky @ Liberty | Western Kentucky 17, Liberty 34 | Liberty 89% | Western Kentucky +780 / Liberty -780 | 18.1 – 35.4 | 7–31 / 20–51 | Liberty -17.3 / – | 53.5 / – | no line yet | no line yet (fair: Liberty -780) | no line yet |  |
| Sat 11/21 2:00 PM | Chattanooga @ Alabama | Chattanooga 0, Alabama 55 | Alabama 100% | Chattanooga +9900 / Alabama -9900 | 3.0 – 56.0 | 0–7 / 42–71 | Alabama -53.0 / – | 59.0 / – | no line yet | no line yet (fair: Alabama -9900) | no line yet | FCS opponent |
| Sat 11/21 2:00 PM | Missouri State @ Jacksonville State | Missouri State 21, Jacksonville State 35 | Jacksonville State 82% | Missouri State +450 / Jacksonville State -450 | 20.8 – 34.5 | 7–34 / 20–50 | Jacksonville State -13.7 / – | 55.3 / – | no line yet | no line yet (fair: Jacksonville State -450) | no line yet |  |
| Sat 11/21 2:00 PM | Middle Tennessee @ Sam Houston | Middle Tennessee 24, Sam Houston 21 | Middle Tennessee 53% | Middle Tennessee -115 / Sam Houston +115 | 22.8 – 21.6 | 10–36 / 10–35 | Middle Tennessee -1.3 / – | 44.4 / – | no line yet | no line yet (fair: Middle Tennessee -115) | no line yet |  |
| Sat 11/21 3:00 PM | Delaware @ New Mexico State | Delaware 31, New Mexico State 24 | Delaware 71% | Delaware -250 / New Mexico State +250 | 31.6 – 23.2 | 17–47 / 10–37 | Delaware -8.4 / – | 54.8 / – | no line yet | no line yet (fair: Delaware -250) | no line yet |  |
| Sat 11/21 3:00 PM | Florida International @ Kennesaw State | Florida International 21, Kennesaw State 24 | Kennesaw State 65% | Florida International +185 / Kennesaw State -185 | 21.1 – 26.6 | 9–34 / 13–41 | Kennesaw State -5.5 / – | 47.7 / – | no line yet | no line yet (fair: Kennesaw State -185) | no line yet |  |
| Sat 11/21 3:30 PM | Samford @ Auburn | Samford 0, Auburn 45 | Auburn 100% | Samford +9900 / Auburn -9900 | 3.0 – 47.4 | 0–7 / 33–63 | Auburn -44.4 / – | 50.4 / – | no line yet | no line yet (fair: Auburn -9900) | no line yet | FCS opponent |
| Sat 11/21 3:30 PM | Old Dominion @ UConn | Old Dominion 17, UConn 31 | UConn 83% | Old Dominion +480 / UConn -480 | 16.7 – 30.6 | 6–29 / 16–45 | UConn -13.9 / – | 47.3 / – | no line yet | no line yet (fair: UConn -480) | no line yet |  |
| Sat 11/21 4:00 PM | Northern Illinois @ North Dakota State | Northern Illinois 14, North Dakota State 35 | North Dakota State 94% | Northern Illinois +1535 / North Dakota State -1535 | 13.3 – 34.7 | 3–24 / 20–50 | North Dakota State -21.4 / – | 48.0 / – | no line yet | no line yet (fair: North Dakota State -1535) | no line yet |  |
| Sat 11/21 6:00 PM | Washington State @ Texas State | Washington State 24, Texas State 34 | Texas State 78% | Washington State +355 / Texas State -355 | 23.6 – 35.3 | 10–38 / 20–51 | Texas State -11.7 / – | 58.8 / – | no line yet | no line yet (fair: Texas State -355) | no line yet |  |
| Sat 11/21 7:00 PM | UNLV @ San José State | UNLV 31, San José State 24 | UNLV 68% | UNLV -215 / San José State +215 | 29.2 – 22.1 | 15–44 / 10–35 | UNLV -7.2 / – | 51.3 / – | no line yet | no line yet (fair: UNLV -215) | no line yet |  |
| Sat 11/21 7:30 PM | SMU @ Notre Dame | SMU 21, Notre Dame 38 | Notre Dame 87% | SMU +675 / Notre Dame -675 | 19.3 – 36.5 | 7–32 / 21–52 | Notre Dame -14.1 / Notre Dame -17.5 | 53.1 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | Colorado State @ Fresno State | Colorado State 24, Fresno State 34 | Fresno State 76% | Colorado State +310 / Fresno State -310 | 25.1 – 35.1 | 13–38 / 20–51 | Fresno State -10.0 / – | 60.2 / – | no line yet | no line yet (fair: Fresno State -310) | no line yet |  |
| Sat 11/21 9:30 PM | San Diego State @ Boise State | San Diego State 21, Boise State 38 | Boise State 87% | San Diego State +660 / Boise State -660 | 20.0 – 36.4 | 7–33 / 21–52 | Boise State -16.4 / – | 56.3 / – | no line yet | no line yet (fair: Boise State -660) | no line yet |  |
| Sat 11/21 10:30 PM | Utah State @ Oregon State | Utah State 21, Oregon State 31 | Oregon State 75% | Utah State +300 / Oregon State -300 | 21.7 – 31.3 | 9–35 / 17–46 | Oregon State -9.5 / – | 53.0 / – | no line yet | no line yet (fair: Oregon State -300) | no line yet |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 685 | 11.76 | 12.26 | 8.47 | 79.1% | 0.145 | 81.8% |
| Model only (before blending) | 685 | 12.51 | 12.62 | 8.76 | 76.2% | – | – |
| Betting line when predicted | 683 | 11.75 | 12.21 | 8.46 | 79.2% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin of an FBS game by about 12.5 points.

501 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 8 | 1-7-0 | 2.7 | -0.68 | -25.4% | +4.6% |
| Total | 6 | 2-4-0 | 8.3 | -0.81 | -9.8% | +7.2% |

6 of these edges were priced at an assumed -110 (price not posted).

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
| Alabama @ LSU | 24–31 | 31–13 | 33% | no |
| Cincinnati @ Houston | 24–34 | 24–31 | 75% | yes |
| Merrimack @ Wake Forest | 3–52 | 0–77 | 100% | no |
| Oregon @ Ohio State | 17–24 | 41–28 | 29% | no |
| Penn State @ Washington | 21–24 | 28–25 | 44% | yes |
| Charlotte @ UAB | 20–27 | 12–23 | 74% | yes |
| Temple @ Navy | 24–31 | 35–42 | 69% | yes |
| Marshall @ Georgia Southern | 24–31 | 13–49 | 68% | no |
| Western Kentucky @ Middle Tennessee | 27–24 | 42–51 | 44% | no |
| UCF @ Kansas | 21–24 | 33–32 | 37% | yes |
| Rice @ North Texas | 24–41 | 23–52 | 84% | yes |
| Northern Illinois @ San José State | 21–31 | 19–30 | 79% | yes |
| Missouri State @ Florida International | 24–27 | 20–23 | 62% | yes |
| Louisiana Tech @ Troy | 28–21 | 41–17 | 68% | yes |
| Vanderbilt @ Mississippi State | 24–27 | 25–23 | 42% | yes |
| Rutgers @ Wisconsin | 14–31 | 10–31 | 92% | yes |
| South Alabama @ Louisiana | 24–31 | 26–28 | 67% | yes |
| Boise State @ Colorado State | 41–24 | 64–38 | 85% | no |
| Kentucky @ Tennessee | 21–28 | 6–34 | 66% | no |
| Sam Houston @ Jacksonville State | 14–31 | 14–47 | 88% | no |
| Georgia @ Ole Miss | 27–24 | 42–7 | 58% | no |
| Colorado @ Arizona State | 24–27 | 10–20 | 60% | yes |
| Louisville @ Georgia Tech | 38–24 | 44–17 | 84% | yes |
| Miami @ Notre Dame | 24–31 | 24–31 | 68% | yes |
| Michigan State @ Michigan | 14–28 | 15–6 | 14% | no |
| Iowa @ Northwestern | 24–21 | 24–10 | 56% | yes |
| Air Force @ Army | 21–24 | 24–21 | 40% | yes |
| Oklahoma @ Florida | 21–24 | 23–7 | 37% | no |
| Liberty @ New Mexico State | 31–14 | 30–14 | 85% | yes |
| West Virginia @ Texas Tech | 24–41 | 48–53 | 86% | no |
| Fresno State @ Utah State | 24–21 | 10–17 | 51% | yes |
| Hawai'i @ UTEP | 28–21 | 17–14 | 71% | yes |
| Texas State @ Oregon State | 31–38 | 42–21 | 36% | no |
| Wyoming @ UNLV | 24–27 | 41–35 | 39% | no |

## FBS power ratings

Points per game better than an average FBS team on a neutral field, from opponent-adjusted EPA (garbage time removed) with this season's games weighted against a preseason prior, plus the weight the margin model puts on Elo (a rating built from game results alone). Defense is positive when it holds opponents below average.

| # | Team | Conference | Net | Offense | Defense | Special teams | Results (Elo) | Elo rating |
|---|---|---|---|---|---|---|---|---|
| 1 | Georgia | SEC | +25.7 | +8.2 | +11.6 | +0.8 | +5.1 | 1931 |
| 2 | LSU | SEC | +23.8 | +9.6 | +11.8 | +0.0 | +2.4 | 1703 |
| 3 | Notre Dame | FBS Independents | +23.4 | +8.6 | +9.2 | +1.0 | +4.6 | 1888 |
| 4 | Ohio State | Big Ten | +23.3 | +10.2 | +9.2 | +0.3 | +3.6 | 1805 |
| 5 | Miami | ACC | +22.8 | +14.1 | +4.1 | +0.4 | +4.3 | 1865 |
| 6 | Alabama | SEC | +22.0 | +9.6 | +8.3 | +0.3 | +3.8 | 1825 |
| 7 | Indiana | Big Ten | +21.3 | +5.4 | +10.5 | +0.1 | +5.2 | 1939 |
| 8 | Utah | Big 12 | +20.3 | +10.2 | +6.0 | -0.1 | +4.3 | 1862 |
| 9 | Texas | SEC | +19.8 | +2.3 | +12.6 | +0.8 | +4.1 | 1848 |
| 10 | Oregon | Big Ten | +19.5 | +5.8 | +9.6 | +0.5 | +3.6 | 1806 |
| 11 | UCLA | Big Ten | +17.7 | +5.5 | +9.0 | +0.8 | +2.4 | 1709 |
| 12 | Texas Tech | Big 12 | +17.4 | +2.9 | +10.1 | +1.3 | +3.1 | 1767 |
| 13 | Tennessee | SEC | +17.4 | +4.3 | +8.8 | +1.2 | +3.0 | 1758 |
| 14 | Wake Forest | ACC | +17.2 | +6.6 | +7.6 | +0.5 | +2.5 | 1712 |
| 15 | Ole Miss | SEC | +16.5 | +9.4 | +3.4 | +0.7 | +3.1 | 1764 |
| 16 | Louisville | ACC | +16.4 | +9.8 | +4.1 | +0.2 | +2.3 | 1699 |
| 17 | Oklahoma | SEC | +16.4 | +1.0 | +13.0 | +0.6 | +1.8 | 1659 |
| 18 | Iowa | Big Ten | +14.4 | +1.5 | +8.6 | +1.0 | +3.3 | 1783 |
| 19 | Missouri | SEC | +14.4 | +4.2 | +7.7 | +0.4 | +2.1 | 1680 |
| 20 | USC | Big Ten | +13.9 | +10.5 | +0.4 | +0.3 | +2.8 | 1738 |
| 21 | SMU | ACC | +13.8 | +8.1 | +3.1 | +0.3 | +2.3 | 1700 |
| 22 | BYU | Big 12 | +13.3 | +5.3 | +4.5 | +0.7 | +2.8 | 1739 |
| 23 | South Carolina | SEC | +12.4 | +5.8 | +4.0 | +0.6 | +2.1 | 1683 |
| 24 | Michigan | Big Ten | +12.3 | +2.2 | +9.2 | -0.3 | +1.1 | 1602 |
| 25 | Arizona | Big 12 | +12.0 | +5.9 | +3.5 | +0.1 | +2.5 | 1713 |
| 26 | Penn State | Big Ten | +11.9 | +3.7 | +6.5 | +0.0 | +1.6 | 1640 |
| 27 | Nebraska | Big Ten | +11.7 | +3.4 | +7.3 | +0.3 | +0.6 | 1558 |
| 28 | Auburn | SEC | +11.5 | +5.0 | +5.5 | +0.6 | +0.5 | 1550 |
| 29 | Texas A&M | SEC | +11.2 | +2.4 | +7.6 | +0.4 | +0.9 | 1579 |
| 30 | Houston | Big 12 | +10.7 | +8.4 | -0.2 | +0.3 | +2.2 | 1690 |
| 31 | Florida | SEC | +10.6 | +5.6 | +3.8 | +0.8 | +0.3 | 1534 |
| 32 | Oklahoma State | Big 12 | +9.9 | +9.2 | -0.3 | +0.5 | +0.6 | 1556 |
| 33 | Northwestern | Big Ten | +9.6 | +6.0 | +1.9 | +0.6 | +1.1 | 1602 |
| 34 | Baylor | Big 12 | +9.4 | +0.8 | +6.3 | +0.9 | +1.4 | 1628 |
| 35 | Duke | ACC | +8.8 | +3.7 | +1.9 | +0.7 | +2.5 | 1716 |
| 36 | Wisconsin | Big Ten | +8.7 | -0.2 | +7.3 | +0.4 | +1.2 | 1608 |
| 37 | Washington | Big Ten | +8.7 | +2.2 | +4.7 | +0.1 | +1.6 | 1642 |
| 38 | Mississippi State | SEC | +8.4 | +4.5 | +4.1 | -0.1 | -0.2 | 1493 |
| 39 | Kentucky | SEC | +8.3 | +2.6 | +4.0 | +0.1 | +1.6 | 1642 |
| 40 | Iowa State | Big 12 | +6.8 | +4.7 | +0.8 | +1.0 | +0.3 | 1536 |
| 41 | Boise State | Pac-12 | +6.4 | +6.3 | -2.3 | -0.2 | +2.7 | 1730 |
| 42 | Illinois | Big Ten | +6.4 | +6.8 | -2.2 | +0.3 | +1.6 | 1638 |
| 43 | Kansas State | Big 12 | +6.4 | +4.6 | +2.2 | +0.2 | -0.7 | 1454 |
| 44 | Kansas | Big 12 | +6.4 | +4.7 | +2.8 | -0.2 | -1.0 | 1428 |
| 45 | Cincinnati | Big 12 | +5.8 | +9.2 | -4.2 | +0.3 | +0.5 | 1551 |
| 46 | Clemson | ACC | +5.7 | -4.7 | +8.2 | +0.7 | +1.4 | 1627 |
| 47 | Arizona State | Big 12 | +5.6 | +0.9 | +4.2 | -0.1 | +0.7 | 1565 |
| 48 | TCU | Big 12 | +5.4 | -2.1 | +6.5 | +0.1 | +0.9 | 1582 |
| 49 | Florida State | ACC | +5.4 | +7.4 | -1.2 | -0.7 | -0.1 | 1499 |
| 50 | Vanderbilt | SEC | +4.9 | +3.6 | +0.4 | +0.5 | +0.5 | 1547 |
| 51 | Virginia Tech | ACC | +4.4 | +4.0 | -0.1 | +0.1 | +0.4 | 1541 |
| 52 | Pittsburgh | ACC | +4.0 | -1.2 | +4.0 | +0.6 | +0.7 | 1566 |
| 53 | North Texas | American Athletic | +3.7 | +10.4 | -7.5 | -0.8 | +1.7 | 1651 |
| 54 | North Carolina | ACC | +3.7 | +3.4 | -1.0 | +0.7 | +0.6 | 1554 |
| 55 | UCF | Big 12 | +3.7 | +1.4 | +2.6 | +0.1 | -0.5 | 1470 |
| 56 | James Madison | Sun Belt | +3.2 | -1.1 | +1.5 | +0.4 | +2.4 | 1711 |
| 57 | Minnesota | Big Ten | +3.1 | -3.5 | +5.5 | +0.9 | +0.2 | 1529 |
| 58 | Colorado | Big 12 | +2.2 | -0.0 | +4.5 | -0.6 | -1.7 | 1364 |
| 59 | Maryland | Big Ten | +2.2 | -0.2 | +3.2 | +0.8 | -1.6 | 1374 |
| 60 | Memphis | American Athletic | +1.9 | +3.4 | -2.4 | -0.4 | +1.3 | 1614 |
| 61 | NC State | ACC | +1.7 | +5.0 | -2.8 | -0.4 | -0.1 | 1498 |
| 62 | Liberty | Conference USA | +1.7 | +1.8 | -1.2 | +0.4 | +0.7 | 1568 |
| 63 | Texas State | Pac-12 | +1.6 | +6.1 | -4.5 | -1.1 | +1.1 | 1602 |
| 64 | Syracuse | ACC | +1.5 | +1.1 | +2.6 | -0.8 | -1.4 | 1392 |
| 65 | Virginia | ACC | +1.3 | -1.3 | +3.3 | -0.5 | -0.2 | 1494 |
| 66 | UTSA | American Athletic | +1.2 | +3.6 | -3.5 | -0.0 | +1.1 | 1596 |
| 67 | West Virginia | Big 12 | +1.2 | +6.0 | -5.1 | +0.4 | -0.2 | 1495 |
| 68 | Arkansas | SEC | +0.9 | +1.4 | +0.8 | -0.7 | -0.6 | 1455 |
| 69 | New Mexico | Mountain West | +0.3 | -4.1 | +3.0 | -0.2 | +1.5 | 1636 |
| 70 | Oregon State | Pac-12 | -0.2 | +3.4 | -2.7 | +0.0 | -1.0 | 1428 |
| 71 | Toledo | Mid-American | -0.7 | -2.4 | +1.4 | -0.3 | +0.6 | 1559 |
| 72 | Purdue | Big Ten | -1.0 | +2.8 | -3.0 | +0.7 | -1.5 | 1386 |
| 73 | Navy | American Athletic | -1.0 | +3.5 | -3.6 | -0.6 | -0.3 | 1484 |
| 74 | Tulsa | American Athletic | -1.1 | +0.0 | -0.0 | -0.6 | -0.5 | 1466 |
| 75 | Michigan State | Big Ten | -1.1 | -3.3 | +2.1 | +0.6 | -0.6 | 1459 |
| 76 | North Dakota State | Mountain West | -1.5 | -4.9 | +3.4 | +1.1 | -1.1 | 1419 |
| 77 | South Florida | American Athletic | -1.8 | -2.3 | -0.3 | +0.1 | +0.7 | 1569 |
| 78 | Louisiana Tech | Sun Belt | -2.3 | -3.3 | +0.9 | -0.8 | +0.8 | 1575 |
| 79 | Florida Atlantic | American Athletic | -2.8 | +4.7 | -8.1 | +0.7 | -0.0 | 1506 |
| 80 | East Carolina | American Athletic | -3.0 | -5.3 | +2.7 | -0.5 | +0.1 | 1520 |
| 81 | UConn | FBS Independents | -3.3 | +1.4 | -3.6 | -0.1 | -1.0 | 1427 |
| 82 | Fresno State | Pac-12 | -3.6 | -2.8 | -0.8 | -0.3 | +0.3 | 1530 |
| 83 | Ohio | Mid-American | -3.7 | -1.9 | -2.9 | +0.2 | +0.9 | 1586 |
| 84 | Army | American Athletic | -3.8 | +4.5 | -8.4 | -0.1 | +0.2 | 1525 |
| 85 | Air Force | Mountain West | -4.3 | +2.2 | -6.3 | -0.2 | +0.1 | 1517 |
| 86 | Jacksonville State | Conference USA | -4.5 | -0.2 | -4.1 | -0.1 | -0.0 | 1505 |
| 87 | Rutgers | Big Ten | -4.8 | +2.4 | -6.2 | +0.7 | -1.6 | 1373 |
| 88 | Boston College | ACC | -5.5 | -3.6 | -0.4 | -0.6 | -0.9 | 1431 |
| 89 | Georgia Southern | Sun Belt | -5.7 | -1.6 | -4.0 | -0.7 | +0.6 | 1556 |
| 90 | Georgia Tech | ACC | -6.0 | +0.5 | -4.6 | -0.2 | -1.6 | 1375 |
| 91 | California | ACC | -6.0 | -2.2 | -1.7 | -0.4 | -1.7 | 1369 |
| 92 | Utah State | Pac-12 | -6.2 | -6.9 | +2.5 | -1.1 | -0.6 | 1455 |
| 93 | UNLV | Mountain West | -6.5 | -2.8 | -3.8 | +0.2 | -0.1 | 1497 |
| 94 | Western Michigan | Mid-American | -7.0 | -4.9 | -3.6 | +0.8 | +0.6 | 1561 |
| 95 | Tulane | American Athletic | -7.1 | -4.1 | -2.5 | +0.2 | -0.7 | 1454 |
| 96 | Delaware | Conference USA | -7.4 | -0.4 | -5.6 | +0.0 | -1.4 | 1389 |
| 97 | San Diego State | Pac-12 | -8.1 | -4.6 | -2.5 | +0.3 | -1.2 | 1406 |
| 98 | Washington State | Pac-12 | -8.4 | -6.1 | -0.1 | -0.4 | -1.9 | 1349 |
| 99 | Stanford | ACC | -8.6 | -2.6 | -5.1 | -0.1 | -0.7 | 1448 |
| 100 | Georgia State | Sun Belt | -8.9 | -0.5 | -7.1 | -0.0 | -1.2 | 1407 |
| 101 | Wyoming | Mountain West | -9.2 | -5.4 | -3.0 | -0.2 | -0.6 | 1460 |
| 102 | Miami (OH) | Mid-American | -9.3 | -4.9 | -4.1 | +0.7 | -1.1 | 1421 |
| 103 | Louisiana | Sun Belt | -9.7 | -4.8 | -4.6 | -0.2 | -0.2 | 1488 |
| 104 | Marshall | Sun Belt | -9.7 | -5.0 | -4.1 | -0.0 | -0.6 | 1456 |
| 105 | App State | Sun Belt | -9.8 | -3.7 | -3.7 | -0.5 | -1.8 | 1361 |
| 106 | Temple | American Athletic | -9.9 | +0.4 | -7.1 | -0.4 | -2.8 | 1279 |
| 107 | UAB | American Athletic | -10.0 | -7.1 | -1.7 | -0.2 | -1.1 | 1419 |
| 108 | Hawai'i | Mountain West | -10.5 | -3.8 | -6.1 | +1.0 | -1.6 | 1374 |
| 109 | Colorado State | Pac-12 | -11.4 | +4.8 | -13.3 | -0.2 | -2.8 | 1278 |
| 110 | Central Michigan | Mid-American | -11.5 | -6.1 | -4.3 | -0.1 | -1.1 | 1418 |
| 111 | Arkansas State | Sun Belt | -11.7 | -3.2 | -7.3 | +0.0 | -1.2 | 1408 |
| 112 | Troy | Sun Belt | -11.9 | -8.5 | -0.3 | -1.3 | -1.7 | 1366 |
| 113 | Old Dominion | Sun Belt | -11.9 | -13.8 | +4.7 | -1.6 | -1.2 | 1407 |
| 114 | South Alabama | Sun Belt | -11.9 | -0.0 | -10.7 | +0.3 | -1.5 | 1388 |
| 115 | Kennesaw State | Conference USA | -11.9 | -6.1 | -3.6 | -0.5 | -1.8 | 1363 |
| 116 | Western Kentucky | Conference USA | -12.6 | -5.4 | -4.5 | -0.2 | -2.4 | 1306 |
| 117 | Coastal Carolina | Sun Belt | -12.9 | -7.5 | -3.8 | +0.4 | -2.1 | 1334 |
| 118 | Rice | American Athletic | -13.1 | -3.6 | -5.4 | -0.8 | -3.2 | 1240 |
| 119 | Florida International | Conference USA | -14.0 | -10.0 | -0.7 | -1.6 | -1.7 | 1366 |
| 120 | Missouri State | Conference USA | -14.7 | -3.0 | -7.6 | -1.2 | -2.9 | 1268 |
| 121 | Nevada | Mountain West | -14.8 | -11.0 | -1.7 | +0.3 | -2.4 | 1309 |
| 122 | Southern Miss | Sun Belt | -15.3 | -8.0 | -3.8 | -1.2 | -2.3 | 1318 |
| 123 | San José State | Mountain West | -15.9 | -10.1 | -3.5 | +0.0 | -2.3 | 1318 |
| 124 | New Mexico State | Conference USA | -16.3 | -7.9 | -3.5 | -1.9 | -3.0 | 1258 |
| 125 | Buffalo | Mid-American | -16.7 | -11.4 | -5.2 | +0.4 | -0.5 | 1469 |
| 126 | UL Monroe | Sun Belt | -16.9 | -5.7 | -6.1 | -1.3 | -3.7 | 1201 |
| 127 | Middle Tennessee | Conference USA | -17.1 | -5.8 | -8.7 | -0.0 | -2.6 | 1296 |
| 128 | Massachusetts | Mid-American | -17.2 | -9.1 | -4.4 | -0.3 | -3.4 | 1229 |
| 129 | Ball State | Mid-American | -17.3 | -5.8 | -7.7 | -0.6 | -3.2 | 1241 |
| 130 | Northern Illinois | Mountain West | -18.3 | -3.8 | -8.8 | -1.1 | -4.6 | 1130 |
| 131 | Bowling Green | Mid-American | -18.6 | -11.8 | -4.0 | -0.0 | -2.9 | 1270 |
| 132 | Eastern Michigan | Mid-American | -19.0 | -7.9 | -7.8 | -0.6 | -2.7 | 1287 |
| 133 | Sam Houston | Conference USA | -19.5 | -12.9 | -0.7 | -1.3 | -4.5 | 1136 |
| 134 | Sacramento State | Mid-American | -20.4 | -11.9 | -4.4 | +0.3 | -4.4 | 1147 |
| 135 | Charlotte | American Athletic | -20.7 | -8.1 | -8.1 | -0.7 | -3.8 | 1190 |
| 136 | Kent State | Mid-American | -20.9 | -10.7 | -6.1 | -0.8 | -3.2 | 1241 |
| 137 | Akron | Mid-American | -22.7 | -10.3 | -7.9 | -0.7 | -3.8 | 1198 |
| 138 | UTEP | Mountain West | -24.6 | -11.6 | -6.8 | -1.2 | -4.9 | 1103 |

## Current model fit

- Fitted on 4302 games from seasons 2022–2026.
- Home field on top of the ratings: 3.2 points (1.8 in conference games).
- Extra FBS edge over FCS opponents beyond their ratings: 14.1 points.
- Elo weight: 0.19 points of margin per point of Elo spread.
- Weight on the betting line: 92% for the margin, 82% for the total.
