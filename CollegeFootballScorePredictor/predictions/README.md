# College football score predictions

Updated Sat Oct 24, 2026 02:23 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 8

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sat 10/24 3:00 PM | Oregon @ Illinois | Oregon 31, Illinois 21 | Oregon 76% | Oregon -310 / Illinois +310 | 30.0 – 19.6 | 16–45 / 7–33 | Oregon -13.7 / Oregon -10.0 | 53.2 / 48.8 | no edge | no edge | no edge |  |
| Sat 10/24 3:30 PM | Texas A&M @ Alabama | Texas A&M 17, Alabama 31 | Alabama 82% | Texas A&M +445 / Alabama -445 | 18.0 – 30.8 | 7–31 / 17–45 | Alabama -8.8 / Alabama -13.2 | 45.8 / 49.5 | no edge | no edge | no edge |  |
| Sat 10/24 3:30 PM | Oklahoma @ Mississippi State | Oklahoma 24, Mississippi State 21 | Oklahoma 55% | Oklahoma -120 / Mississippi State +120 | 25.2 – 23.5 | 12–38 / 10–38 | Oklahoma -3.4 / Oklahoma -1.5 | 47.3 / 49.0 | no edge | no edge | no edge |  |
| Sat 10/24 3:30 PM | Tennessee @ South Carolina | Tennessee 24, South Carolina 27 | South Carolina 56% | Tennessee +125 / South Carolina -125 | 24.3 – 26.1 | 10–38 / 13–40 | Tennessee -6.0 / South Carolina -2.5 | 50.2 / 50.5 | no edge | no edge | no edge |  |
| Sat 10/24 3:30 PM | BYU @ UCF | BYU 24, UCF 17 | BYU 71% | BYU -245 / UCF +245 | 26.0 – 18.3 | 13–41 / 7–31 | BYU -9.3 / BYU -7.5 | 48.4 / 43.5 | no edge | no edge | no edge |  |
| Sat 10/24 3:30 PM | Boston College @ Georgia Tech | Boston College 24, Georgia Tech 31 | Georgia Tech 68% | Boston College +210 / Georgia Tech -210 | 22.1 – 28.8 | 10–35 / 14–44 | Georgia Tech -8.8 / Georgia Tech -6.5 | 52.4 / 50.5 | no edge | no edge | no edge |  |
| Sat 10/24 3:30 PM | Iowa @ Minnesota | Iowa 24, Minnesota 17 | Iowa 71% | Iowa -240 / Minnesota +240 | 24.1 – 16.6 | 10–38 / 6–29 | Iowa -7.4 / Iowa -7.5 | 41.6 / 40.5 | no edge | no edge | no edge |  |
| Sat 10/24 3:30 PM | Michigan State @ UCLA | Michigan State 14, UCLA 31 | UCLA 89% | Michigan State +820 / UCLA -820 | 13.4 – 30.3 | 3–24 / 16–45 | UCLA -21.8 / UCLA -16.5 | 47.8 / 42.8 | no edge | no edge | no edge |  |
| Sat 10/24 3:30 PM | North Texas @ Navy | North Texas 31, Navy 28 | North Texas 58% | North Texas -135 / Navy +135 | 31.9 – 29.0 | 17–47 / 14–44 | North Texas -1.7 / North Texas -3.0 | 62.5 / 60.5 | no edge | no edge | no edge |  |
| Sat 10/24 3:30 PM | Hawai'i @ Northern Illinois | Hawai'i 27, Northern Illinois 24 | Hawai'i 58% | Hawai'i -140 / Northern Illinois +140 | 26.3 – 23.3 | 13–41 / 10–37 | Hawai'i -2.2 / Hawai'i -3.0 | 53.1 / 48.8 | no edge | no edge | no edge |  |
| Sat 10/24 3:30 PM | Sacramento State @ Ball State | Sacramento State 17, Ball State 31 | Ball State 82% | Sacramento State +445 / Ball State -445 | 18.9 – 32.4 | 7–31 / 17–48 | Ball State -3.1 / Ball State -14.5 | 50.0 / 51.5 | no edge | Sacramento State (+385): EV +6.9%, 22%, stake 0.4u | no edge |  |
| Sat 10/24 3:30 PM | Bowling Green @ Buffalo | Bowling Green 21, Buffalo 24 | Buffalo 59% | Bowling Green +145 / Buffalo -145 | 20.6 – 23.6 | 7–34 / 10–38 | Buffalo -2.8 / Buffalo -3.0 | 42.8 / 44.5 | no edge | no edge | no edge |  |
| Sat 10/24 3:45 PM | Kansas State @ Arizona State | Kansas State 27, Arizona State 24 | Kansas State 55% | Kansas State -120 / Arizona State +120 | 27.0 – 25.0 | 14–41 / 13–39 | Kansas State -6.5 / Kansas State -1.5 | 54.2 / 51.5 | no edge | no edge | no edge |  |
| Sat 10/24 4:00 PM | Eastern Michigan @ Ohio | Eastern Michigan 21, Ohio 31 | Ohio 78% | Eastern Michigan +355 / Ohio -355 | 19.2 – 30.3 | 7–31 / 17–45 | Ohio -17.9 / Ohio -10.5 | 52.7 / 48.8 | no edge | no edge | no edge |  |
| Sat 10/24 4:00 PM | UL Monroe @ Troy | UL Monroe 17, Troy 31 | Troy 82% | UL Monroe +460 / Troy -460 | 18.6 – 32.0 | 7–31 / 17–48 | Troy -12.8 / Troy -13.5 | 52.0 / 50.2 | no edge | no edge | no edge |  |
| Sat 10/24 5:00 PM | San José State @ Nevada | San José State 21, Nevada 24 | Nevada 64% | San José State +180 / Nevada -180 | 20.9 – 26.2 | 7–34 / 13–41 | Nevada -3.8 / Nevada -5.5 | 49.7 / 46.5 | no edge | no edge | no edge |  |
| Sat 10/24 5:00 PM | Louisiana @ Southern Miss | Louisiana 31, Southern Miss 24 | Louisiana 74% | Louisiana -290 / Southern Miss +290 | 31.1 – 21.5 | 17–45 / 9–35 | Louisiana -6.0 / Louisiana -10.0 | 53.1 / 52.5 | no edge | no edge | no edge |  |
| Sat 10/24 5:00 PM | Old Dominion @ Louisiana Tech | Old Dominion 13, Louisiana Tech 27 | Louisiana Tech 83% | Old Dominion +500 / Louisiana Tech -500 | 14.9 – 28.3 | 3–27 / 14–43 | Louisiana Tech -9.8 / Louisiana Tech -13.8 | 42.3 / 43.5 | no edge | no edge | no edge |  |
| Sat 10/24 6:00 PM | Boise State @ Washington State | Boise State 31, Washington State 17 | Boise State 83% | Boise State -495 / Washington State +495 | 33.0 – 18.9 | 18–48 / 7–31 | Boise State -10.4 / Boise State -14.5 | 49.6 / 52.5 | no edge | no edge | no edge |  |
| Sat 10/24 6:30 PM | San Diego State @ Colorado State | San Diego State 31, Colorado State 28 | San Diego State 53% | San Diego State -115 / Colorado State +115 | 30.0 – 28.6 | 16–44 / 14–43 | San Diego State -2.8 / San Diego State -1.2 | 55.5 / 59.2 | no edge | no edge | no edge |  |
| Sat 10/24 7:00 PM | Colorado @ Oklahoma State | Colorado 20, Oklahoma State 34 | Oklahoma State 80% | Colorado +410 / Oklahoma State -410 | 20.9 – 33.7 | 7–34 / 19–49 | Oklahoma State -5.2 / Oklahoma State -13.5 | 53.9 / 54.8 | no edge | no edge | no edge |  |
| Sat 10/24 7:00 PM | Virginia Tech @ Clemson | Virginia Tech 24, Clemson 27 | Clemson 58% | Virginia Tech +140 / Clemson -140 | 23.7 – 26.6 | 10–38 / 14–41 | Clemson -2.1 / Clemson -3.0 | 49.1 / 50.5 | no edge | no edge | no edge |  |
| Sat 10/24 7:00 PM | Georgia State @ Arkansas State | Georgia State 31, Arkansas State 28 | Georgia State 57% | Georgia State -130 / Arkansas State +130 | 30.3 – 27.9 | 16–45 / 14–42 | Georgia State -1.1 / Georgia State -2.5 | 56.8 / 58.5 | no edge | no edge | no edge |  |
| Sat 10/24 7:30 PM | Vanderbilt @ Kentucky | Vanderbilt 24, Kentucky 31 | Kentucky 76% | Vanderbilt +310 / Kentucky -310 | 20.4 – 30.4 | 7–34 / 17–45 | Kentucky -5.3 / Kentucky -10.5 | 51.3 / 50.8 | no edge | no edge | no edge |  |
| Sat 10/24 7:30 PM | Ole Miss @ Texas | Ole Miss 24, Texas 27 | Texas 58% | Ole Miss +140 / Texas -140 | 25.6 – 28.4 | 13–40 / 14–43 | Texas -1.1 / Texas -3.0 | 53.2 / 54.2 | no edge | no edge | no edge |  |
| Sat 10/24 7:30 PM | Iowa State @ Arizona | Iowa State 17, Arizona 31 | Arizona 79% | Iowa State +380 / Arizona -380 | 19.8 – 31.6 | 7–33 / 17–47 | Arizona -5.1 / Arizona -12.5 | 51.0 / 51.5 | no edge | no edge | no edge |  |
| Sat 10/24 7:30 PM | Syracuse @ North Carolina | Syracuse 21, North Carolina 28 | North Carolina 74% | Syracuse +280 / North Carolina -280 | 20.5 – 29.5 | 7–34 / 15–44 | North Carolina -3.5 / North Carolina -9.5 | 52.8 / 49.2 | no edge | no edge | no edge |  |
| Sat 10/24 7:30 PM | USC @ Wisconsin | USC 27, Wisconsin 24 | USC 57% | USC -130 / Wisconsin +130 | 26.7 – 24.1 | 14–41 / 10–38 | USC -3.8 / USC -2.5 | 52.4 / 50.5 | no edge | no edge | no edge |  |
| Sat 10/24 7:30 PM | Utah State @ Texas State | Utah State 24, Texas State 38 | Texas State 82% | Utah State +445 / Texas State -445 | 23.3 – 37.0 | 10–37 / 21–52 | Texas State -13.2 / Texas State -13.8 | 59.8 / 60.5 | no edge | no edge | no edge |  |
| Sat 10/24 8:00 PM | UTSA @ Tulane | UTSA 27, Tulane 24 | UTSA 57% | UTSA -135 / Tulane +135 | 27.4 – 24.5 | 14–42 / 10–38 | UTSA -1.8 / UTSA -3.0 | 52.7 / 51.8 | no edge | no edge | no edge |  |
| Sat 10/24 10:00 PM | North Dakota State @ New Mexico | North Dakota State 17, New Mexico 20 | New Mexico 63% | North Dakota State +170 / New Mexico -170 | 17.6 – 22.2 | 7–30 / 10–35 | New Mexico -2.3 / New Mexico -4.8 | 42.7 / 39.8 | no edge | no edge | no edge |  |
| Sat 10/24 10:15 PM | Houston @ Utah | Houston 24, Utah 31 | Utah 68% | Houston +210 / Utah -210 | 25.4 – 32.2 | 13–39 / 17–48 | Utah -9.2 / Utah -6.5 | 58.2 / 57.5 | no edge | no edge | no edge |  |

## 2026 Week 9

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 10/27 7:00 PM | Delaware @ Western Kentucky | Delaware 24, Western Kentucky 27 | Western Kentucky 59% | Delaware +145 / Western Kentucky -145 | 24.5 – 28.3 | 10–38 / 14–42 | Western Kentucky -3.8 / – | 52.8 / – | no line yet | no line yet (fair: Western Kentucky -145) | no line yet |  |
| Tue 10/27 8:00 PM | Sam Houston @ Missouri State | Sam Houston 21, Missouri State 28 | Missouri State 72% | Sam Houston +255 / Missouri State -255 | 19.7 – 28.1 | 7–33 / 14–43 | Missouri State -8.4 / – | 48.2 / – | no line yet | no line yet (fair: Missouri State -255) | no line yet |  |
| Wed 10/28 7:00 PM | Kennesaw State @ Middle Tennessee | Kennesaw State 27, Middle Tennessee 24 | Kennesaw State 54% | Kennesaw State -115 / Middle Tennessee +115 | 26.1 – 24.5 | 13–41 / 10–38 | Kennesaw State -1.7 / – | 50.6 / – | no line yet | no line yet (fair: Kennesaw State -115) | no line yet |  |
| Wed 10/28 8:00 PM | Jacksonville State @ New Mexico State | Jacksonville State 31, New Mexico State 24 | Jacksonville State 68% | Jacksonville State -210 / New Mexico State +210 | 29.0 – 22.1 | 14–43 / 10–35 | Jacksonville State -6.9 / – | 51.0 / – | no line yet | no line yet (fair: Jacksonville State -210) | no line yet |  |
| Thu 10/29 7:30 PM | Florida Atlantic @ North Texas | Florida Atlantic 31, North Texas 38 | North Texas 67% | Florida Atlantic +200 / North Texas -200 | 30.9 – 37.7 | 17–45 / 23–53 | North Texas -6.8 / – | 68.6 / – | no line yet | no line yet (fair: North Texas -200) | no line yet |  |
| Thu 10/29 7:30 PM | Troy @ James Madison | Troy 17, James Madison 38 | James Madison 91% | Troy +1045 / James Madison -1045 | 15.9 – 35.6 | 6–28 / 20–51 | James Madison -19.7 / – | 51.5 / – | no line yet | no line yet (fair: James Madison -1045) | no line yet |  |
| Fri 10/30 7:00 PM | Tulane @ Charlotte | Tulane 31, Charlotte 14 | Tulane 86% | Tulane -635 / Charlotte +635 | 31.5 – 15.8 | 17–47 / 5–28 | Tulane -15.6 / – | 47.3 / – | no line yet | no line yet (fair: Tulane -635) | no line yet |  |
| Fri 10/30 7:30 PM | Baylor @ UCF | Baylor 27, UCF 24 | Baylor 53% | Baylor -115 / UCF +115 | 26.5 – 25.3 | 13–41 / 13–39 | Baylor -1.2 / – | 51.8 / – | no line yet | no line yet (fair: Baylor -115) | no line yet |  |
| Fri 10/30 10:30 PM | Kent State @ Sacramento State | Kent State 21, Sacramento State 24 | Sacramento State 59% | Kent State +145 / Sacramento State -145 | 21.7 – 25.1 | 9–35 / 13–38 | Sacramento State -3.4 / – | 46.7 / – | no line yet | no line yet (fair: Sacramento State -145) | no line yet |  |
| Sat 10/31 TBA | Missouri @ Arkansas | Missouri 31, Arkansas 17 | Missouri 81% | Missouri -440 / Arkansas +440 | 30.9 – 17.9 | 17–45 / 7–31 | Missouri -13.0 / – | 48.9 / – | no line yet | no line yet (fair: Missouri -440) | no line yet |  |
| Sat 10/31 TBA | Auburn @ Ole Miss | Auburn 24, Ole Miss 31 | Ole Miss 75% | Auburn +300 / Ole Miss -300 | 22.0 – 32.3 | 10–35 / 17–48 | Ole Miss -7.4 / Ole Miss -10.5 | 57.7 / 53.5 | no edge | no edge | no edge |  |
| Sat 10/31 TBA | South Carolina @ Oklahoma | South Carolina 17, Oklahoma 24 | Oklahoma 66% | South Carolina +195 / Oklahoma -195 | 18.7 – 24.7 | 7–31 / 10–38 | Oklahoma -10.5 / Oklahoma -5.5 | 44.3 / 43.5 | no edge | no edge | no edge |  |
| Sat 10/31 TBA | Mississippi State @ Texas | Mississippi State 21, Texas 31 | Texas 74% | Mississippi State +280 / Texas -280 | 21.0 – 30.7 | 8–34 / 16–45 | Texas -9.8 / – | 51.7 / – | no line yet | no line yet (fair: Texas -280) | no line yet |  |
| Sat 10/31 TBA | Arizona @ Texas Tech | Arizona 24, Texas Tech 31 | Texas Tech 70% | Arizona +235 / Texas Tech -235 | 22.6 – 30.5 | 10–36 / 16–45 | Texas Tech -11.2 / Texas Tech -7.5 | 48.8 / 54.5 | no edge | no edge | no edge |  |
| Sat 10/31 TBA | Arizona State @ BYU | Arizona State 17, BYU 34 | BYU 87% | Arizona State +690 / BYU -690 | 17.5 – 33.8 | 6–30 / 20–49 | BYU -14.7 / BYU -16.5 | 50.4 / 51.5 | no edge | no edge | no edge |  |
| Sat 10/31 TBA | Kansas @ TCU | Kansas 24, TCU 27 | TCU 52% | Kansas +110 / TCU -110 | 23.8 – 24.4 | 10–38 / 10–38 | TCU -0.6 / – | 49.9 / – | no line yet | no line yet (fair: TCU -110) | no line yet |  |
| Sat 10/31 TBA | Kansas State @ Colorado | Kansas State 28, Colorado 21 | Kansas State 70% | Kansas State -230 / Colorado +230 | 29.9 – 22.3 | 16–45 / 10–36 | Kansas State -7.6 / – | 52.1 / – | no line yet | no line yet (fair: Kansas State -230) | no line yet |  |
| Sat 10/31 TBA | Oklahoma State @ Iowa State | Oklahoma State 24, Iowa State 27 | Iowa State 65% | Oklahoma State +185 / Iowa State -185 | 23.0 – 28.9 | 10–37 / 14–44 | Iowa State -5.9 / – | 53.9 / – | no line yet | no line yet (fair: Iowa State -185) | no line yet |  |
| Sat 10/31 TBA | Utah @ Cincinnati | Utah 31, Cincinnati 24 | Utah 73% | Utah -270 / Cincinnati +270 | 33.4 – 23.9 | 19–48 / 10–38 | Utah -8.7 / Utah -9.5 | 60.7 / 56.5 | no edge | no edge | no edge |  |
| Sat 10/31 TBA | California @ NC State | California 24, NC State 34 | NC State 75% | California +300 / NC State -300 | 24.2 – 34.6 | 10–38 / 20–49 | NC State -10.4 / – | 58.9 / – | no line yet | no line yet (fair: NC State -300) | no line yet |  |
| Sat 10/31 TBA | SMU @ Syracuse | SMU 31, Syracuse 24 | SMU 72% | SMU -255 / Syracuse +255 | 31.3 – 22.5 | 17–46 / 10–36 | SMU -8.8 / – | 53.9 / – | no line yet | no line yet (fair: SMU -255) | no line yet |  |
| Sat 10/31 TBA | Boston College @ Duke | Boston College 17, Duke 31 | Duke 85% | Boston College +555 / Duke -555 | 17.8 – 32.8 | 7–30 / 17–48 | Duke -15.0 / – | 50.6 / – | no line yet | no line yet (fair: Duke -555) | no line yet |  |
| Sat 10/31 TBA | Clemson @ Florida State | Clemson 27, Florida State 24 | Clemson 52% | Clemson -110 / Florida State +110 | 26.3 – 25.3 | 13–41 / 13–40 | Florida State -3.9 / Clemson -1.5 | 52.0 / 51.5 | no edge | no edge | no edge |  |
| Sat 10/31 TBA | Georgia Tech @ Pittsburgh | Georgia Tech 24, Pittsburgh 31 | Pittsburgh 71% | Georgia Tech +245 / Pittsburgh -245 | 22.6 – 31.0 | 10–37 / 17–46 | Pittsburgh -8.4 / – | 53.5 / – | no line yet | no line yet (fair: Pittsburgh -245) | no line yet |  |
| Sat 10/31 TBA | Miami @ North Carolina | Miami 34, North Carolina 17 | Miami 85% | Miami -560 / North Carolina +560 | 32.9 – 18.1 | 17–48 / 7–31 | Miami -18.2 / Miami -14.5 | 53.0 / 50.5 | no edge | no edge | no edge |  |
| Sat 10/31 TBA | Stanford @ Louisville | Stanford 14, Louisville 42 | Louisville 97% | Stanford +3235 / Louisville -3235 | 14.1 – 41.5 | 3–26 / 27–58 | Louisville -27.3 / – | 55.6 / – | no line yet | no line yet (fair: Louisville -3235) | no line yet |  |
| Sat 10/31 TBA | Virginia @ Wake Forest | Virginia 17, Wake Forest 31 | Wake Forest 84% | Virginia +535 / Wake Forest -535 | 17.3 – 31.9 | 6–30 / 17–48 | Wake Forest -14.7 / – | 49.2 / – | no line yet | no line yet (fair: Wake Forest -535) | no line yet |  |
| Sat 10/31 TBA | Minnesota @ Indiana | Minnesota 10, Indiana 31 | Indiana 95% | Minnesota +1890 / Indiana -1890 | 11.2 – 33.6 | 3–21 / 17–49 | Indiana -21.3 / Indiana -22.5 | 41.7 / 45.5 | no edge | no edge | no edge |  |
| Sat 10/31 TBA | Wisconsin @ Iowa | Wisconsin 17, Iowa 24 | Iowa 64% | Wisconsin +175 / Iowa -175 | 17.7 – 22.5 | 7–30 / 10–35 | Iowa -7.2 / Iowa -4.5 | 43.3 / 39.5 | no edge | no edge | no edge |  |
| Sat 10/31 TBA | Illinois @ Maryland | Illinois 24, Maryland 27 | Maryland 56% | Illinois +125 / Maryland -125 | 26.2 – 28.4 | 13–41 / 14–43 | Maryland -2.2 / – | 54.6 / – | no line yet | no line yet (fair: Maryland -125) | no line yet |  |
| Sat 10/31 TBA | Washington @ Nebraska | Washington 17, Nebraska 27 | Nebraska 74% | Washington +280 / Nebraska -280 | 18.8 – 27.8 | 7–31 / 14–42 | Nebraska -9.0 / – | 48.5 / – | no line yet | no line yet (fair: Nebraska -280) | no line yet |  |
| Sat 10/31 TBA | Northwestern @ Oregon | Northwestern 24, Oregon 31 | Oregon 69% | Northwestern +225 / Oregon -225 | 22.3 – 29.9 | 10–35 / 16–45 | Oregon -8.4 / Oregon -7.5 | 50.9 / 52.5 | no edge | no edge | no edge |  |
| Sat 10/31 TBA | Purdue @ Penn State | Purdue 17, Penn State 31 | Penn State 80% | Purdue +405 / Penn State -405 | 19.1 – 31.2 | 7–31 / 17–47 | Penn State -12.1 / – | 50.3 / – | no line yet | no line yet (fair: Penn State -405) | no line yet |  |
| Sat 10/31 TBA | Michigan @ Rutgers | Michigan 34, Rutgers 17 | Michigan 85% | Michigan -570 / Rutgers +570 | 33.5 – 18.0 | 18–49 / 7–31 | Michigan -15.4 / – | 51.5 / – | no line yet | no line yet (fair: Michigan -570) | no line yet |  |
| Sat 10/31 TBA | Nevada @ UCLA | Nevada 7, UCLA 41 | UCLA 99% | Nevada +9900 / UCLA -9900 | 7.2 – 40.8 | 0–14 / 27–57 | UCLA -33.6 / – | 48.0 / – | no line yet | no line yet (fair: UCLA -9900) | no line yet |  |
| Sat 10/31 TBA | Ohio State @ USC | Ohio State 31, USC 24 | Ohio State 67% | Ohio State -205 / USC +205 | 30.4 – 23.6 | 16–45 / 10–38 | Ohio State -9.9 / Ohio State -6.5 | 56.6 / 53.5 | no edge | no edge | no edge |  |
| Sat 10/31 TBA | Oregon State @ Fresno State | Oregon State 31, Fresno State 28 | Oregon State 61% | Oregon State -155 / Fresno State +155 | 30.2 – 26.3 | 16–45 / 13–41 | Oregon State -3.9 / – | 56.5 / – | no line yet | no line yet (fair: Oregon State -155) | no line yet |  |
| Sat 10/31 TBA | Army @ Memphis | Army 28, Memphis 31 | Memphis 63% | Army +170 / Memphis -170 | 27.3 – 31.8 | 13–42 / 17–47 | Memphis -4.6 / – | 59.1 / – | no line yet | no line yet (fair: Memphis -170) | no line yet |  |
| Sat 10/31 TBA | Temple @ East Carolina | Temple 24, East Carolina 31 | East Carolina 73% | Temple +275 / East Carolina -275 | 21.3 – 30.0 | 9–34 / 16–45 | East Carolina -8.7 / – | 51.2 / – | no line yet | no line yet (fair: East Carolina -275) | no line yet |  |
| Sat 10/31 TBA | UAB @ South Florida | UAB 21, South Florida 31 | South Florida 76% | UAB +315 / South Florida -315 | 19.9 – 30.2 | 7–34 / 16–45 | South Florida -10.3 / – | 50.1 / – | no line yet | no line yet (fair: South Florida -315) | no line yet |  |
| Sat 10/31 TBA | New Mexico @ San José State | New Mexico 31, San José State 17 | New Mexico 80% | New Mexico -400 / San José State +400 | 30.7 – 18.6 | 17–45 / 7–31 | New Mexico -12.1 / – | 49.3 / – | no line yet | no line yet (fair: New Mexico -400) | no line yet |  |
| Sat 10/31 TBA | App State @ Georgia Southern | App State 28, Georgia Southern 31 | Georgia Southern 52% | App State +105 / Georgia Southern -105 | 28.4 – 28.9 | 14–42 / 14–44 | Georgia Southern -0.5 / – | 57.3 / – | no line yet | no line yet (fair: Georgia Southern -105) | no line yet |  |
| Sat 10/31 TBA | Coastal Carolina @ Georgia State | Coastal Carolina 24, Georgia State 31 | Georgia State 70% | Coastal Carolina +235 / Georgia State -235 | 24.1 – 32.4 | 10–38 / 17–48 | Georgia State -8.3 / – | 56.5 / – | no line yet | no line yet (fair: Georgia State -235) | no line yet |  |
| Sat 10/31 TBA | Southern Miss @ UL Monroe | Southern Miss 27, UL Monroe 24 | Southern Miss 58% | Southern Miss -135 / UL Monroe +135 | 29.0 – 26.2 | 15–44 / 13–41 | Southern Miss -2.8 / – | 55.2 / – | no line yet | no line yet (fair: Southern Miss -135) | no line yet |  |
| Sat 10/31 TBA | Marshall @ Old Dominion | Marshall 27, Old Dominion 24 | Marshall 59% | Marshall -145 / Old Dominion +145 | 25.3 – 22.2 | 13–39 / 10–35 | Marshall -3.1 / – | 47.5 / – | no line yet | no line yet (fair: Marshall -145) | no line yet |  |
| Sat 10/31 TBA | Louisiana Tech @ South Alabama | Louisiana Tech 31, South Alabama 28 | Louisiana Tech 53% | Louisiana Tech -115 / South Alabama +115 | 29.5 – 28.1 | 14–44 / 14–43 | Louisiana Tech -1.4 / – | 57.6 / – | no line yet | no line yet (fair: Louisiana Tech -115) | no line yet |  |
| Sat 10/31 12:00 PM | Notre Dame vs Navy | Notre Dame 41, Navy 13 | Notre Dame 98% | Notre Dame -4385 / Navy +4385 | 40.6 – 12.2 | 26–57 / 3–23 | Notre Dame -27.3 / Notre Dame -28.5 | 50.3 / 53.5 | no edge | no edge | no edge | neutral site |
| Sat 10/31 12:00 PM | Bowling Green @ Western Michigan | Bowling Green 10, Western Michigan 27 | Western Michigan 85% | Bowling Green +565 / Western Michigan -565 | 13.0 – 27.3 | 3–24 / 13–42 | Western Michigan -14.2 / – | 42.0 / – | no line yet | no line yet (fair: Western Michigan -565) | no line yet |  |
| Sat 10/31 3:00 PM | UConn @ Air Force | UConn 28, Air Force 31 | Air Force 57% | UConn +130 / Air Force -130 | 28.0 – 30.6 | 14–42 / 17–45 | Air Force -2.5 / – | 58.6 / – | no line yet | no line yet (fair: Air Force -130) | no line yet |  |
| Sat 10/31 3:30 PM | Florida vs Georgia | Florida 24, Georgia 34 | Georgia 75% | Florida +305 / Georgia -305 | 22.7 – 33.1 | 10–36 / 17–48 | Georgia -9.2 / Georgia -10.5 | 53.3 / 56.5 | no edge | no edge | no edge | neutral site |
| Sat 10/31 3:30 PM | Colorado State @ Utah State | Colorado State 24, Utah State 27 | Utah State 58% | Colorado State +140 / Utah State -140 | 26.0 – 29.3 | 13–40 / 14–44 | Utah State -3.3 / – | 55.3 / – | no line yet | no line yet (fair: Utah State -140) | no line yet |  |
| Sat 10/31 3:30 PM | UTEP @ North Dakota State | UTEP 6, North Dakota State 34 | North Dakota State 99% | UTEP +8385 / North Dakota State -8385 | 6.7 – 34.7 | 0–14 / 20–50 | North Dakota State -28.0 / – | 41.4 / – | no line yet | no line yet (fair: North Dakota State -8385) | no line yet |  |
| Sat 10/31 3:30 PM | Florida International @ Liberty | Florida International 17, Liberty 27 | Liberty 78% | Florida International +350 / Liberty -350 | 17.9 – 29.0 | 7–31 / 14–44 | Liberty -11.1 / – | 46.9 / – | no line yet | no line yet (fair: Liberty -350) | no line yet |  |
| Sat 10/31 7:00 PM | Washington State @ San Diego State | Washington State 21, San Diego State 24 | San Diego State 56% | Washington State +125 / San Diego State -125 | 21.1 – 23.5 | 9–34 / 10–38 | San Diego State -2.3 / – | 44.6 / – | no line yet | no line yet (fair: San Diego State -125) | no line yet |  |
| Sat 10/31 10:00 PM | Texas State @ Boise State | Texas State 31, Boise State 38 | Boise State 72% | Texas State +260 / Boise State -260 | 28.0 – 37.0 | 14–42 / 22–52 | Boise State -8.9 / – | 65.0 / – | no line yet | no line yet (fair: Boise State -260) | no line yet |  |
| Sat 10/31 10:30 PM | Northern Illinois @ UNLV | Northern Illinois 17, UNLV 34 | UNLV 84% | Northern Illinois +540 / UNLV -540 | 18.8 – 34.0 | 7–31 / 20–49 | UNLV -15.2 / – | 52.8 / – | no line yet | no line yet (fair: UNLV -540) | no line yet |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 510 | 11.63 | 11.97 | 8.34 | 82.2% | 0.126 | 82.8% |
| Model only (before blending) | 510 | 12.42 | 12.30 | 8.63 | 79.6% | – | – |
| Betting line when predicted | 508 | 11.62 | 11.92 | 8.33 | 82.1% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin of an FBS game by about 12.5 points.

501 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Every edge logged before kickoff at the stake and price logged with it (backfilled games, and edges logged before edges were priced from the final prediction, are not included). Units are 1% of the bankroll; ROI is units won per unit staked, pushes returning the stake, and expected ROI is what the edges' EVs promised.

### Week 7 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| Delaware @ Middle Tennessee | 27–24 | 30–33 | 45% | yes |
| Florida International @ Jacksonville State | 21–24 | 24–27 | 61% | yes |
| Kennesaw State @ Missouri State | 27–24 | 21–24 | 45% | yes |
| Western Kentucky @ Sam Houston | 27–24 | 16–3 | 54% | no |
| East Carolina @ UAB | 27–24 | 17–30 | 34% | yes |
| Georgia Southern @ Old Dominion | 24–21 | 23–15 | 57% | yes |
| Colorado State @ Texas State | 24–41 | 27–66 | 83% | no |
| Memphis @ Tulane | 31–24 | 17–31 | 34% | yes |
| Washington @ Purdue | 24–27 | 38–26 | 43% | yes |
| App State @ Coastal Carolina | 27–24 | 35–32 | 53% | yes |
| Mississippi State @ LSU | 20–38 | 0–31 | 87% | no |
| Florida @ Texas | 17–31 | 27–24 | 19% | yes |
| Cincinnati @ West Virginia | 31–34 | 42–45 | 53% | yes |
| Kansas @ Kansas State | 28–31 | 24–35 | 58% | yes |
| Charleston Southern @ Clemson | 3–45 | 0–37 | 100% | yes |
| Pittsburgh @ Boston College | 24–17 | 21–27 | 32% | yes |
| Virginia @ SMU | 21–31 | 13–23 | 75% | yes |
| Ohio State @ Indiana | 27–24 | 19–15 | 57% | yes |
| Northwestern @ Michigan State | 31–24 | 24–21 | 70% | yes |
| Florida Atlantic @ Army | 24–27 | 24–56 | 57% | no |
| Ball State @ Bowling Green | 17–24 | 32–31 | 34% | yes |
| Georgia State @ James Madison | 24–31 | 22–49 | 70% | no |
| Rutgers @ Maryland | 24–31 | 37–30 | 34% | yes |
| The Citadel @ Texas A&M | 3–52 | 0–41 | 100% | yes |
| Charlotte @ Temple | 14–31 | 38–31 | 11% | no |
| Massachusetts @ Buffalo | 17–24 | 18–25 | 67% | yes |
| Western Michigan @ Central Michigan | 24–17 | 21–14 | 69% | yes |
| Auburn @ Georgia | 17–34 | 27–24 | 9% | yes |
| Missouri @ Ole Miss | 28–31 | 3–31 | 60% | no |
| Alabama @ Tennessee | 31–24 | 10–26 | 30% | no |
| Arizona State @ Texas Tech | 17–34 | 25–53 | 87% | no |
| Georgia Tech @ Virginia Tech | 24–31 | 24–34 | 72% | yes |
| North Carolina @ Duke | 24–27 | 24–20 | 40% | yes |
| Penn State @ Michigan | 17–24 | 18–21 | 67% | yes |
| Northern Illinois @ Wyoming | 17–24 | 23–41 | 70% | no |
| UNLV @ Air Force | 24–27 | 31–41 | 55% | yes |
| Toledo @ Eastern Michigan | 31–24 | 34–14 | 71% | yes |
| Akron @ Miami (OH) | 17–27 | 14–34 | 77% | yes |
| Tulsa @ Rice | 24–21 | 38–17 | 59% | yes |
| Troy @ Louisiana | 24–27 | 6–33 | 57% | no |
| Washington State @ Oregon State | 17–34 | 30–48 | 89% | yes |
| Arkansas @ Vanderbilt | 24–27 | 31–21 | 33% | yes |
| TCU @ Baylor | 24–27 | 17–6 | 39% | no |
| Florida State @ Miami | 17–38 | 35–43 | 91% | no |
| Kent State @ South Florida | 13–34 | 2–29 | 93% | no |
| Nevada @ North Dakota State | 14–31 | 17–31 | 86% | yes |
| Arkansas State @ Southern Miss | 31–28 | 23–13 | 63% | no |
| Kentucky @ Oklahoma | 17–24 | 21–13 | 29% | yes |
| Notre Dame @ BYU | 27–17 | 24–28 | 25% | yes |
| Oklahoma State @ Houston | 28–31 | 32–35 | 62% | yes |
| Elon @ Stanford | 10–45 | 7–34 | 99% | yes |
| Louisville @ Syracuse | 34–20 | 34–26 | 83% | yes |
| Wisconsin @ UCLA | 21–24 | 7–17 | 57% | yes |
| Navy @ UTSA | 24–31 | 34–38 | 67% | yes |
| Louisiana Tech @ UL Monroe | 34–24 | 24–0 | 76% | no |
| San José State @ UTEP | 27–20 | 24–11 | 67% | yes |
| Ohio @ Sacramento State | 31–14 | 48–7 | 87% | yes |
| Utah @ Colorado | 34–17 | 27–24 | 85% | yes |
| Wake Forest @ California | 31–24 | 41–7 | 74% | no |
| Fresno State @ San Diego State | 27–20 | 23–26 | 33% | yes |
| New Mexico @ Hawai'i | 31–17 | 21–10 | 82% | yes |
| Nebraska @ Oregon | 21–28 | 14–17 | 66% | yes |

## FBS power ratings

Points per game better than an average FBS team on a neutral field, from opponent-adjusted EPA (garbage time removed) with this season's games weighted against a preseason prior, plus the weight the margin model puts on Elo (a rating built from game results alone). Defense is positive when it holds opponents below average.

| # | Team | Conference | Net | Offense | Defense | Special teams | Results (Elo) | Elo rating |
|---|---|---|---|---|---|---|---|---|
| 1 | Ohio State | Big Ten | +26.8 | +10.7 | +10.5 | +0.4 | +5.1 | 1934 |
| 2 | LSU | SEC | +24.4 | +9.0 | +12.7 | +0.2 | +2.5 | 1717 |
| 3 | Notre Dame | FBS Independents | +24.1 | +8.7 | +10.1 | +1.3 | +4.1 | 1849 |
| 4 | Georgia | SEC | +23.4 | +9.6 | +8.6 | +0.9 | +4.3 | 1866 |
| 5 | Miami | ACC | +22.7 | +11.6 | +6.5 | +0.1 | +4.5 | 1881 |
| 6 | Indiana | Big Ten | +22.2 | +7.9 | +9.1 | +0.3 | +5.0 | 1921 |
| 7 | Texas Tech | Big 12 | +19.1 | +1.8 | +12.6 | +1.2 | +3.6 | 1803 |
| 8 | Alabama | SEC | +19.1 | +8.4 | +7.4 | +0.3 | +3.0 | 1760 |
| 9 | Ole Miss | SEC | +19.1 | +11.1 | +3.4 | +0.7 | +3.9 | 1834 |
| 10 | Texas | SEC | +18.0 | +3.4 | +10.9 | +0.5 | +3.2 | 1770 |
| 11 | Utah | Big 12 | +17.7 | +8.6 | +5.3 | +0.3 | +3.5 | 1801 |
| 12 | Oregon | Big Ten | +17.7 | +4.0 | +10.0 | +0.4 | +3.3 | 1784 |
| 13 | Tennessee | SEC | +16.4 | +3.4 | +9.3 | +0.7 | +3.0 | 1753 |
| 14 | Oklahoma | SEC | +16.1 | +0.4 | +13.3 | +0.8 | +1.7 | 1649 |
| 15 | UCLA | Big Ten | +16.0 | +6.4 | +7.3 | +0.6 | +1.8 | 1657 |
| 16 | BYU | Big 12 | +15.6 | +6.1 | +5.4 | +0.4 | +3.7 | 1814 |
| 17 | Missouri | SEC | +15.5 | +3.9 | +8.9 | +0.5 | +2.1 | 1686 |
| 18 | Wake Forest | ACC | +15.0 | +5.8 | +6.9 | +0.1 | +2.2 | 1688 |
| 19 | Louisville | ACC | +14.9 | +8.7 | +4.0 | +0.3 | +1.9 | 1663 |
| 20 | Michigan | Big Ten | +14.9 | +4.2 | +8.4 | +0.4 | +2.0 | 1674 |
| 21 | USC | Big Ten | +14.6 | +12.3 | -0.7 | +0.3 | +2.7 | 1734 |
| 22 | Auburn | SEC | +14.1 | +4.9 | +7.6 | +0.7 | +0.9 | 1584 |
| 23 | Nebraska | Big Ten | +14.1 | +4.7 | +7.5 | +0.5 | +1.4 | 1622 |
| 24 | Florida | SEC | +14.0 | +9.0 | +3.1 | +1.0 | +1.0 | 1592 |
| 25 | Iowa | Big Ten | +12.5 | +2.3 | +6.2 | +1.0 | +3.0 | 1756 |
| 26 | Texas A&M | SEC | +12.4 | +2.3 | +8.2 | +0.6 | +1.3 | 1618 |
| 27 | Kansas State | Big 12 | +12.3 | +7.9 | +3.1 | +0.3 | +1.1 | 1599 |
| 28 | SMU | ACC | +12.2 | +5.8 | +4.0 | +0.1 | +2.4 | 1705 |
| 29 | Arizona | Big 12 | +11.6 | +5.5 | +3.6 | -0.0 | +2.4 | 1710 |
| 30 | Houston | Big 12 | +11.1 | +8.7 | +0.2 | +0.0 | +2.2 | 1690 |
| 31 | Mississippi State | SEC | +10.8 | +7.2 | +2.8 | +0.3 | +0.5 | 1551 |
| 32 | Northwestern | Big Ten | +10.8 | +5.6 | +2.3 | +1.3 | +1.6 | 1640 |
| 33 | Penn State | Big Ten | +10.6 | +2.4 | +6.7 | +0.5 | +1.0 | 1593 |
| 34 | Wisconsin | Big Ten | +8.5 | +0.9 | +6.8 | +0.2 | +0.6 | 1559 |
| 35 | Kentucky | SEC | +8.3 | +1.8 | +4.5 | +0.2 | +1.7 | 1653 |
| 36 | Washington | Big Ten | +8.1 | +2.3 | +4.3 | -0.1 | +1.5 | 1635 |
| 37 | South Carolina | SEC | +8.0 | +3.8 | +2.6 | +0.8 | +0.7 | 1569 |
| 38 | Kansas | Big 12 | +7.9 | +6.0 | +2.6 | +0.2 | -0.8 | 1441 |
| 39 | Iowa State | Big 12 | +7.9 | +3.0 | +3.2 | +0.9 | +0.8 | 1578 |
| 40 | Baylor | Big 12 | +6.8 | -0.4 | +5.5 | +1.1 | +0.6 | 1559 |
| 41 | Cincinnati | Big 12 | +6.5 | +8.8 | -2.8 | +0.3 | +0.2 | 1522 |
| 42 | Florida State | ACC | +6.1 | +7.9 | -1.6 | -0.1 | -0.1 | 1497 |
| 43 | TCU | Big 12 | +5.8 | -1.3 | +5.4 | +0.5 | +1.3 | 1613 |
| 44 | Boise State | Pac-12 | +5.5 | +4.2 | -1.2 | +0.2 | +2.3 | 1702 |
| 45 | Vanderbilt | SEC | +5.2 | +4.2 | +0.1 | +0.4 | +0.5 | 1553 |
| 46 | James Madison | Sun Belt | +5.0 | +0.4 | +0.6 | +0.6 | +3.4 | 1789 |
| 47 | Oklahoma State | Big 12 | +4.9 | +5.2 | -0.2 | +0.5 | -0.5 | 1464 |
| 48 | Duke | ACC | +4.6 | +2.6 | -0.3 | +0.7 | +1.5 | 1635 |
| 49 | Virginia Tech | ACC | +4.5 | +3.7 | +0.2 | +0.3 | +0.3 | 1531 |
| 50 | Pittsburgh | ACC | +4.4 | -0.4 | +3.6 | +0.7 | +0.5 | 1551 |
| 51 | UCF | Big 12 | +4.2 | +0.9 | +4.1 | +0.0 | -0.7 | 1448 |
| 52 | Clemson | ACC | +4.1 | -4.2 | +6.6 | +0.4 | +1.3 | 1613 |
| 53 | Arizona State | Big 12 | +3.4 | +1.0 | +1.9 | +0.3 | +0.2 | 1521 |
| 54 | Colorado | Big 12 | +3.3 | -0.3 | +6.0 | -0.7 | -1.6 | 1377 |
| 55 | Minnesota | Big Ten | +3.2 | -2.5 | +4.9 | +0.5 | +0.3 | 1532 |
| 56 | Virginia | ACC | +3.1 | -0.0 | +3.0 | -0.2 | +0.3 | 1534 |
| 57 | North Texas | American Athletic | +3.0 | +9.1 | -6.3 | -0.9 | +1.1 | 1603 |
| 58 | Oregon State | Pac-12 | +3.0 | +5.4 | -2.3 | +0.1 | -0.1 | 1498 |
| 59 | NC State | ACC | +2.9 | +6.3 | -3.3 | -0.5 | +0.4 | 1539 |
| 60 | Illinois | Big Ten | +1.6 | +5.3 | -4.4 | +0.3 | +0.4 | 1539 |
| 61 | North Carolina | ACC | +1.6 | +0.9 | -0.2 | +0.6 | +0.3 | 1532 |
| 62 | Syracuse | ACC | +1.4 | +1.0 | +2.7 | -0.3 | -1.9 | 1347 |
| 63 | Maryland | Big Ten | +1.3 | -0.7 | +3.4 | +0.5 | -2.0 | 1343 |
| 64 | UTSA | American Athletic | +1.0 | +2.7 | -3.1 | -0.1 | +1.5 | 1636 |
| 65 | Purdue | Big Ten | +0.9 | +3.1 | -1.9 | +0.5 | -0.8 | 1444 |
| 66 | Arkansas | SEC | +0.9 | +1.0 | +0.4 | -0.4 | -0.2 | 1496 |
| 67 | Texas State | Pac-12 | +0.7 | +7.4 | -5.8 | -1.5 | +0.6 | 1559 |
| 68 | Memphis | American Athletic | +0.4 | +2.2 | -1.8 | -0.4 | +0.4 | 1544 |
| 69 | Toledo | Mid-American | -0.1 | -2.0 | +1.3 | +0.4 | +0.2 | 1522 |
| 70 | New Mexico | Mountain West | -0.2 | -2.1 | +0.6 | +0.2 | +1.1 | 1598 |
| 71 | Georgia Tech | ACC | -0.9 | +3.3 | -3.9 | -0.0 | -0.3 | 1480 |
| 72 | West Virginia | Big 12 | -0.9 | +4.1 | -5.1 | +0.6 | -0.6 | 1462 |
| 73 | North Dakota State | Mountain West | -1.2 | -4.7 | +3.4 | +1.2 | -1.1 | 1419 |
| 74 | Navy | American Athletic | -1.4 | +2.1 | -3.0 | -0.5 | +0.0 | 1512 |
| 75 | South Florida | American Athletic | -1.4 | -1.1 | -0.9 | -0.1 | +0.8 | 1572 |
| 76 | Army | American Athletic | -1.8 | +4.8 | -7.2 | -0.4 | +1.0 | 1591 |
| 77 | UConn | FBS Independents | -2.4 | +2.1 | -4.0 | -0.3 | -0.2 | 1496 |
| 78 | Florida Atlantic | American Athletic | -2.6 | +2.8 | -4.8 | +0.4 | -1.1 | 1419 |
| 79 | Rutgers | Big Ten | -2.8 | +3.2 | -5.2 | +0.3 | -1.1 | 1417 |
| 80 | Liberty | Conference USA | -2.8 | -0.4 | -2.1 | -0.2 | -0.2 | 1495 |
| 81 | Michigan State | Big Ten | -3.0 | -2.2 | +0.3 | +0.2 | -1.3 | 1399 |
| 82 | East Carolina | American Athletic | -3.0 | -5.3 | +3.1 | -0.8 | -0.0 | 1507 |
| 83 | Ohio | Mid-American | -3.0 | -0.7 | -3.7 | +0.6 | +0.8 | 1571 |
| 84 | Fresno State | Pac-12 | -3.3 | -2.3 | -1.3 | -0.0 | +0.4 | 1544 |
| 85 | Tulane | American Athletic | -3.4 | -4.6 | +0.1 | +0.0 | +1.2 | 1604 |
| 86 | Air Force | Mountain West | -3.8 | +1.9 | -5.4 | -0.3 | -0.0 | 1507 |
| 87 | Tulsa | American Athletic | -4.2 | -1.8 | -0.4 | -0.3 | -1.7 | 1369 |
| 88 | UNLV | Mountain West | -4.8 | -2.9 | -2.3 | +0.0 | +0.4 | 1540 |
| 89 | California | ACC | -5.0 | -0.8 | -2.4 | -0.5 | -1.3 | 1403 |
| 90 | Louisiana Tech | Sun Belt | -5.3 | -3.5 | -0.4 | -0.8 | -0.5 | 1464 |
| 91 | Jacksonville State | Conference USA | -6.0 | -0.6 | -4.5 | -0.4 | -0.5 | 1465 |
| 92 | Boston College | ACC | -6.5 | -4.8 | +0.0 | -0.8 | -1.0 | 1430 |
| 93 | Washington State | Pac-12 | -6.8 | -6.2 | +1.3 | -0.4 | -1.5 | 1388 |
| 94 | Western Michigan | Mid-American | -7.3 | -5.1 | -3.5 | +0.4 | +0.9 | 1584 |
| 95 | Georgia State | Sun Belt | -7.4 | +0.5 | -6.9 | -0.1 | -1.0 | 1424 |
| 96 | Marshall | Sun Belt | -7.6 | -1.5 | -4.8 | -0.4 | -0.9 | 1433 |
| 97 | Miami (OH) | Mid-American | -7.6 | -3.9 | -3.5 | +0.6 | -0.9 | 1435 |
| 98 | San Diego State | Pac-12 | -7.8 | -7.5 | +0.2 | +0.6 | -1.0 | 1425 |
| 99 | App State | Sun Belt | -8.3 | -2.8 | -3.9 | -0.4 | -1.2 | 1411 |
| 100 | Louisiana | Sun Belt | -8.4 | -4.4 | -4.2 | -0.0 | +0.1 | 1520 |
| 101 | Stanford | ACC | -9.3 | -4.0 | -4.2 | -0.4 | -0.8 | 1441 |
| 102 | Temple | American Athletic | -9.4 | +1.2 | -7.6 | -0.6 | -2.5 | 1303 |
| 103 | UAB | American Athletic | -9.4 | -5.0 | -3.4 | -0.0 | -1.0 | 1427 |
| 104 | Georgia Southern | Sun Belt | -9.5 | -2.1 | -6.0 | -1.0 | -0.3 | 1481 |
| 105 | Western Kentucky | Conference USA | -10.2 | -6.9 | -1.8 | -0.2 | -1.3 | 1399 |
| 106 | South Alabama | Sun Belt | -10.2 | +1.4 | -11.5 | +0.4 | -0.5 | 1468 |
| 107 | Utah State | Pac-12 | -10.3 | -8.3 | +0.7 | -1.3 | -1.4 | 1393 |
| 108 | Troy | Sun Belt | -10.4 | -5.8 | -2.3 | -1.2 | -1.1 | 1416 |
| 109 | Arkansas State | Sun Belt | -11.0 | -3.5 | -6.4 | -0.0 | -1.1 | 1416 |
| 110 | Florida International | Conference USA | -11.2 | -9.4 | -0.2 | -0.5 | -1.2 | 1411 |
| 111 | Delaware | Conference USA | -11.3 | -4.0 | -4.6 | -0.4 | -2.3 | 1316 |
| 112 | Colorado State | Pac-12 | -11.8 | +1.3 | -9.6 | -0.6 | -2.9 | 1271 |
| 113 | Wyoming | Mountain West | -12.1 | -7.3 | -2.8 | -0.2 | -1.8 | 1359 |
| 114 | Old Dominion | Sun Belt | -12.2 | -12.8 | +2.8 | -1.3 | -0.9 | 1431 |
| 115 | Missouri State | Conference USA | -12.3 | -2.6 | -6.2 | -0.8 | -2.7 | 1289 |
| 116 | Kennesaw State | Conference USA | -12.6 | -5.0 | -4.7 | -0.7 | -2.2 | 1327 |
| 117 | Hawai'i | Mountain West | -13.6 | -6.2 | -5.8 | +0.6 | -2.2 | 1326 |
| 118 | Nevada | Mountain West | -13.6 | -8.2 | -3.2 | +0.4 | -2.6 | 1292 |
| 119 | Coastal Carolina | Sun Belt | -13.7 | -5.9 | -6.0 | +0.4 | -2.1 | 1332 |
| 120 | Central Michigan | Mid-American | -14.3 | -7.2 | -5.3 | -0.4 | -1.5 | 1386 |
| 121 | San José State | Mountain West | -14.3 | -7.8 | -4.4 | -0.3 | -1.8 | 1356 |
| 122 | New Mexico State | Conference USA | -14.5 | -7.6 | -2.8 | -1.2 | -2.8 | 1281 |
| 123 | Rice | American Athletic | -14.9 | -6.3 | -4.7 | -0.8 | -3.1 | 1252 |
| 124 | Southern Miss | Sun Belt | -15.3 | -6.5 | -4.2 | -1.5 | -3.1 | 1254 |
| 125 | Massachusetts | Mid-American | -16.7 | -8.7 | -4.5 | -0.1 | -3.4 | 1230 |
| 126 | Northern Illinois | Mountain West | -16.8 | -5.0 | -7.2 | -0.8 | -3.9 | 1188 |
| 127 | Eastern Michigan | Mid-American | -17.1 | -6.7 | -7.6 | -0.8 | -2.1 | 1337 |
| 128 | Middle Tennessee | Conference USA | -17.2 | -6.8 | -7.4 | -0.2 | -2.8 | 1275 |
| 129 | Sam Houston | Conference USA | -17.6 | -11.3 | -1.0 | -1.5 | -3.7 | 1199 |
| 130 | Ball State | Mid-American | -18.4 | -6.4 | -7.5 | -1.1 | -3.4 | 1230 |
| 131 | Bowling Green | Mid-American | -18.5 | -12.2 | -3.5 | -0.2 | -2.6 | 1294 |
| 132 | Buffalo | Mid-American | -18.9 | -13.7 | -4.9 | +0.6 | -1.0 | 1429 |
| 133 | Kent State | Mid-American | -20.2 | -10.4 | -6.1 | -1.0 | -2.6 | 1290 |
| 134 | UL Monroe | Sun Belt | -20.5 | -6.3 | -8.2 | -1.5 | -4.5 | 1139 |
| 135 | Sacramento State | Mid-American | -20.7 | -9.9 | -6.2 | +0.4 | -5.0 | 1095 |
| 136 | Charlotte | American Athletic | -20.9 | -8.6 | -8.3 | -0.4 | -3.6 | 1211 |
| 137 | Akron | Mid-American | -22.0 | -10.8 | -6.8 | -1.2 | -3.3 | 1233 |
| 138 | UTEP | Mountain West | -24.1 | -12.0 | -6.1 | -1.4 | -4.7 | 1123 |

## Current model fit

- Fitted on 4127 games from seasons 2022–2026.
- Home field on top of the ratings: 3.2 points (1.8 in conference games).
- Extra FBS edge over FCS opponents beyond their ratings: 14.0 points.
- Elo weight: 0.19 points of margin per point of Elo spread.
- Weight on the betting line: 91% for the margin, 81% for the total.
