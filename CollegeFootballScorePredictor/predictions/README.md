# College football score predictions

Updated Sat Oct 24, 2026 05:11 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 8

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sat 10/24 6:00 PM | Boise State @ Washington State | Boise State 31, Washington State 17 | Boise State 83% | Boise State -490 / Washington State +490 | 32.6 – 18.7 | 17–48 / 7–31 | Boise State -10.3 / Boise State -14.2 | 49.5 / 51.8 | no edge | no edge | no edge |  |
| Sat 10/24 6:30 PM | San Diego State @ Colorado State | San Diego State 31, Colorado State 28 | San Diego State 52% | San Diego State -110 / Colorado State +110 | 30.0 – 28.6 | 16–45 / 14–43 | San Diego State -2.8 / San Diego State -1.2 | 55.5 / 59.2 | no edge | no edge | no edge |  |
| Sat 10/24 7:00 PM | Colorado @ Oklahoma State | Colorado 20, Oklahoma State 34 | Oklahoma State 80% | Colorado +405 / Oklahoma State -405 | 20.9 – 33.7 | 8–34 / 19–49 | Oklahoma State -5.1 / Oklahoma State -13.5 | 54.0 / 54.8 | no edge | Colorado (+405): EV +3.8%, 21%, stake 0.2u | no edge |  |
| Sat 10/24 7:00 PM | Virginia Tech @ Clemson | Virginia Tech 24, Clemson 27 | Clemson 58% | Virginia Tech +140 / Clemson -140 | 23.7 – 26.6 | 10–38 / 13–41 | Clemson -2.1 / Clemson -3.0 | 49.1 / 50.5 | no edge | no edge | no edge |  |
| Sat 10/24 7:00 PM | Georgia State @ Arkansas State | Georgia State 31, Arkansas State 28 | Georgia State 57% | Georgia State -130 / Arkansas State +130 | 30.3 – 27.9 | 16–45 / 14–42 | Georgia State -1.0 / Georgia State -2.5 | 56.9 / 58.5 | no edge | no edge | no edge |  |
| Sat 10/24 7:30 PM | Vanderbilt @ Kentucky | Vanderbilt 21, Kentucky 31 | Kentucky 75% | Vanderbilt +300 / Kentucky -300 | 20.4 – 30.4 | 7–34 / 16–45 | Kentucky -5.0 / Kentucky -10.5 | 51.2 / 50.8 | no edge | no edge | no edge |  |
| Sat 10/24 7:30 PM | Ole Miss @ Texas | Ole Miss 24, Texas 27 | Texas 57% | Ole Miss +135 / Texas -135 | 25.7 – 28.5 | 13–40 / 14–43 | Texas -1.1 / Texas -3.0 | 53.2 / 54.5 | no edge | no edge | no edge |  |
| Sat 10/24 7:30 PM | Iowa State @ Arizona | Iowa State 21, Arizona 31 | Arizona 79% | Iowa State +375 / Arizona -375 | 19.8 – 31.6 | 7–33 / 17–47 | Arizona -5.1 / Arizona -12.5 | 51.1 / 51.5 | no edge | no edge | no edge |  |
| Sat 10/24 7:30 PM | Syracuse @ North Carolina | Syracuse 21, North Carolina 28 | North Carolina 73% | Syracuse +270 / North Carolina -270 | 20.6 – 29.4 | 7–34 / 16–44 | North Carolina -3.5 / North Carolina -9.2 | 53.0 / 49.2 | no edge | no edge | no edge |  |
| Sat 10/24 7:30 PM | USC @ Wisconsin | USC 27, Wisconsin 24 | USC 56% | USC -130 / Wisconsin +130 | 26.7 – 24.1 | 13–41 / 10–38 | USC -3.8 / USC -2.5 | 52.4 / 50.5 | no edge | no edge | no edge |  |
| Sat 10/24 7:30 PM | Utah State @ Texas State | Utah State 24, Texas State 38 | Texas State 81% | Utah State +435 / Texas State -435 | 23.2 – 36.9 | 10–37 / 21–52 | Texas State -13.1 / Texas State -13.8 | 59.9 / 60.2 | no edge | no edge | no edge |  |
| Sat 10/24 8:00 PM | UTSA @ Tulane | UTSA 27, Tulane 24 | UTSA 58% | UTSA -140 / Tulane +140 | 27.4 – 24.5 | 14–42 / 10–38 | UTSA -1.8 / UTSA -3.0 | 52.8 / 51.8 | no edge | no edge | no edge |  |
| Sat 10/24 10:00 PM | North Dakota State @ New Mexico | North Dakota State 17, New Mexico 20 | New Mexico 63% | North Dakota State +170 / New Mexico -170 | 17.6 – 22.1 | 7–30 / 10–35 | New Mexico -2.2 / New Mexico -4.8 | 42.9 / 39.5 | no edge | no edge | no edge |  |
| Sat 10/24 10:15 PM | Houston @ Utah | Houston 24, Utah 31 | Utah 66% | Houston +200 / Utah -200 | 25.4 – 32.2 | 13–40 / 17–48 | Utah -9.3 / Utah -6.5 | 58.2 / 57.5 | no edge | no edge | no edge |  |

## 2026 Week 9

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 10/27 7:00 PM | Delaware @ Western Kentucky | Delaware 24, Western Kentucky 27 | Western Kentucky 51% | Delaware +105 / Western Kentucky -105 | 27.0 – 27.3 | 13–41 / 14–42 | Western Kentucky -0.4 / – | 54.3 / – | no line yet | no line yet (fair: Western Kentucky -105) | no line yet |  |
| Tue 10/27 8:00 PM | Sam Houston @ Missouri State | Sam Houston 21, Missouri State 28 | Missouri State 66% | Sam Houston +195 / Missouri State -195 | 21.3 – 27.4 | 9–35 / 14–42 | Missouri State -6.1 / – | 49.1 / – | no line yet | no line yet (fair: Missouri State -195) | no line yet |  |
| Wed 10/28 7:00 PM | Kennesaw State @ Middle Tennessee | Kennesaw State 24, Middle Tennessee 27 | Middle Tennessee 59% | Kennesaw State +145 / Middle Tennessee -145 | 23.5 – 26.7 | 10–38 / 13–41 | Middle Tennessee -3.1 / – | 50.2 / – | no line yet | no line yet (fair: Middle Tennessee -145) | no line yet |  |
| Wed 10/28 8:00 PM | Jacksonville State @ New Mexico State | Jacksonville State 28, New Mexico State 21 | Jacksonville State 68% | Jacksonville State -210 / New Mexico State +210 | 28.7 – 22.0 | 14–43 / 10–35 | Jacksonville State -6.8 / – | 50.7 / – | no line yet | no line yet (fair: Jacksonville State -210) | no line yet |  |
| Thu 10/29 7:30 PM | Florida Atlantic @ North Texas | Florida Atlantic 31, North Texas 38 | North Texas 67% | Florida Atlantic +205 / North Texas -205 | 30.8 – 37.8 | 17–45 / 23–54 | North Texas -7.0 / – | 68.6 / – | no line yet | no line yet (fair: North Texas -205) | no line yet |  |
| Thu 10/29 7:30 PM | Troy @ James Madison | Troy 17, James Madison 34 | James Madison 90% | Troy +880 / James Madison -880 | 16.6 – 34.9 | 6–29 / 20–51 | James Madison -18.2 / – | 51.5 / – | no line yet | no line yet (fair: James Madison -880) | no line yet |  |
| Fri 10/30 7:00 PM | Tulane @ Charlotte | Tulane 31, Charlotte 17 | Tulane 86% | Tulane -620 / Charlotte +620 | 31.5 – 16.0 | 17–47 / 6–28 | Tulane -15.5 / – | 47.5 / – | no line yet | no line yet (fair: Tulane -620) | no line yet |  |
| Fri 10/30 7:30 PM | Baylor @ UCF | Baylor 27, UCF 24 | Baylor 53% | Baylor -115 / UCF +115 | 26.5 – 25.3 | 13–41 / 13–40 | Baylor -1.1 / – | 51.8 / – | no line yet | no line yet (fair: Baylor -115) | no line yet |  |
| Fri 10/30 10:30 PM | Kent State @ Sacramento State | Kent State 21, Sacramento State 24 | Sacramento State 59% | Kent State +145 / Sacramento State -145 | 21.7 – 25.2 | 10–35 / 13–38 | Sacramento State -3.5 / – | 46.9 / – | no line yet | no line yet (fair: Sacramento State -145) | no line yet |  |
| Sat 10/31 TBA | Northwestern @ Oregon | Northwestern 24, Oregon 31 | Oregon 70% | Northwestern +235 / Oregon -235 | 22.3 – 29.9 | 10–35 / 16–45 | Oregon -8.5 / Oregon -7.5 | 50.9 / 52.5 | no edge | no edge | no edge |  |
| Sat 10/31 TBA | Purdue @ Penn State | Purdue 17, Penn State 31 | Penn State 80% | Purdue +410 / Penn State -410 | 19.1 – 31.3 | 7–31 / 17–46 | Penn State -12.2 / – | 50.3 / – | no line yet | no line yet (fair: Penn State -410) | no line yet |  |
| Sat 10/31 12:00 PM | Arizona @ Texas Tech | Arizona 24, Texas Tech 31 | Texas Tech 71% | Arizona +245 / Texas Tech -245 | 22.7 – 30.5 | 10–36 / 17–45 | Texas Tech -11.2 / Texas Tech -7.5 | 48.9 / 54.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | California @ NC State | California 24, NC State 34 | NC State 75% | California +300 / NC State -300 | 24.4 – 34.7 | 10–38 / 20–50 | NC State -10.3 / – | 59.5 / – | no line yet | no line yet (fair: NC State -300) | no line yet |  |
| Sat 10/31 12:00 PM | SMU @ Syracuse | SMU 31, Syracuse 24 | SMU 71% | SMU -250 / Syracuse +250 | 31.3 – 22.7 | 17–45 / 10–37 | SMU -8.5 / – | 54.0 / – | no line yet | no line yet (fair: SMU -250) | no line yet |  |
| Sat 10/31 12:00 PM | Boston College @ Duke | Boston College 17, Duke 34 | Duke 86% | Boston College +630 / Duke -630 | 17.0 – 32.6 | 6–29 / 17–48 | Duke -15.6 / – | 49.7 / – | no line yet | no line yet (fair: Duke -630) | no line yet |  |
| Sat 10/31 12:00 PM | Wisconsin @ Iowa | Wisconsin 17, Iowa 20 | Iowa 63% | Wisconsin +170 / Iowa -170 | 17.7 – 22.4 | 7–30 / 10–36 | Iowa -7.2 / Iowa -4.5 | 43.3 / 39.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | Illinois @ Maryland | Illinois 24, Maryland 27 | Maryland 56% | Illinois +130 / Maryland -130 | 26.2 – 28.5 | 13–41 / 14–43 | Maryland -2.2 / – | 54.7 / – | no line yet | no line yet (fair: Maryland -130) | no line yet |  |
| Sat 10/31 12:00 PM | Notre Dame vs Navy | Notre Dame 38, Navy 10 | Notre Dame 98% | Notre Dame -4285 / Navy +4285 | 40.6 – 12.2 | 24–57 / 3–23 | Notre Dame -27.3 / Notre Dame -28.5 | 50.3 / 53.5 | no edge | no edge | no edge | neutral site |
| Sat 10/31 12:00 PM | UAB @ South Florida | UAB 21, South Florida 31 | South Florida 76% | UAB +310 / South Florida -310 | 20.0 – 30.1 | 7–33 / 16–45 | South Florida -10.1 / – | 50.1 / – | no line yet | no line yet (fair: South Florida -310) | no line yet |  |
| Sat 10/31 12:00 PM | Bowling Green @ Western Michigan | Bowling Green 13, Western Michigan 27 | Western Michigan 86% | Bowling Green +590 / Western Michigan -590 | 13.1 – 27.2 | 3–24 / 13–42 | Western Michigan -14.1 / – | 42.1 / – | no line yet | no line yet (fair: Western Michigan -590) | no line yet |  |
| Sat 10/31 12:30 PM | Michigan @ Rutgers | Michigan 34, Rutgers 17 | Michigan 85% | Michigan -575 / Rutgers +575 | 33.5 – 18.1 | 19–49 / 7–31 | Michigan -15.4 / – | 51.5 / – | no line yet | no line yet (fair: Michigan -575) | no line yet |  |
| Sat 10/31 12:45 PM | Auburn @ Ole Miss | Auburn 24, Ole Miss 31 | Ole Miss 75% | Auburn +310 / Ole Miss -310 | 22.1 – 32.3 | 10–35 / 17–48 | Ole Miss -7.3 / Ole Miss -10.5 | 57.7 / 53.5 | no edge | no edge | no edge |  |
| Sat 10/31 1:00 PM | Marshall @ Old Dominion | Marshall 24, Old Dominion 21 | Marshall 63% | Marshall -170 / Old Dominion +170 | 24.8 – 20.7 | 13–38 / 7–34 | Marshall -4.1 / – | 46.8 / – | no line yet | no line yet (fair: Marshall -170) | no line yet |  |
| Sat 10/31 2:00 PM | Kansas State @ Colorado | Kansas State 28, Colorado 21 | Kansas State 69% | Kansas State -225 / Colorado +225 | 28.7 – 21.2 | 14–44 / 9–34 | Kansas State -7.5 / – | 52.2 / – | no line yet | no line yet (fair: Kansas State -225) | no line yet |  |
| Sat 10/31 2:00 PM | Coastal Carolina @ Georgia State | Coastal Carolina 24, Georgia State 31 | Georgia State 69% | Coastal Carolina +220 / Georgia State -220 | 24.4 – 32.1 | 10–38 / 17–48 | Georgia State -7.7 / – | 56.5 / – | no line yet | no line yet (fair: Georgia State -220) | no line yet |  |
| Sat 10/31 3:00 PM | UConn @ Air Force | UConn 28, Air Force 31 | Air Force 54% | UConn +120 / Air Force -120 | 28.6 – 30.1 | 14–43 / 16–45 | Air Force -1.5 / – | 58.7 / – | no line yet | no line yet (fair: Air Force -120) | no line yet |  |
| Sat 10/31 3:00 PM | Temple @ East Carolina | Temple 21, East Carolina 28 | East Carolina 71% | Temple +250 / East Carolina -250 | 20.8 – 29.2 | 8–34 / 14–44 | East Carolina -8.4 / – | 52.3 / – | no line yet | no line yet (fair: East Carolina -250) | no line yet |  |
| Sat 10/31 3:00 PM | Louisiana Tech @ South Alabama | Louisiana Tech 31, South Alabama 28 | Louisiana Tech 56% | Louisiana Tech -130 / South Alabama +130 | 29.7 – 27.2 | 16–45 / 14–42 | Louisiana Tech -2.6 / – | 56.9 / – | no line yet | no line yet (fair: Louisiana Tech -130) | no line yet |  |
| Sat 10/31 3:15 PM | Stanford @ Louisville | Stanford 13, Louisville 41 | Louisville 97% | Stanford +3165 / Louisville -3165 | 14.7 – 41.5 | 3–27 / 27–58 | Louisville -26.8 / – | 56.2 / – | no line yet | no line yet (fair: Louisville -3165) | no line yet |  |
| Sat 10/31 3:30 PM | Florida vs Georgia | Florida 24, Georgia 31 | Georgia 75% | Florida +305 / Georgia -305 | 22.7 – 33.1 | 10–37 / 17–48 | Georgia -9.2 / Georgia -10.5 | 53.3 / 56.5 | no edge | no edge | no edge | neutral site |
| Sat 10/31 3:30 PM | Arizona State @ BYU | Arizona State 17, BYU 34 | BYU 87% | Arizona State +670 / BYU -670 | 17.5 – 33.8 | 6–30 / 20–49 | BYU -14.6 / BYU -16.5 | 50.4 / 51.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Kansas @ TCU | Kansas 21, TCU 24 | TCU 51% | Kansas +105 / TCU -105 | 23.4 – 23.9 | 10–37 / 10–38 | TCU -0.5 / – | 50.0 / – | no line yet | no line yet (fair: TCU -105) | no line yet |  |
| Sat 10/31 3:30 PM | Minnesota @ Indiana | Minnesota 10, Indiana 31 | Indiana 95% | Minnesota +1905 / Indiana -1905 | 11.2 – 33.6 | 3–21 / 17–49 | Indiana -21.1 / Indiana -22.5 | 41.8 / 45.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Colorado State @ Utah State | Colorado State 24, Utah State 27 | Utah State 59% | Colorado State +145 / Utah State -145 | 26.0 – 29.3 | 13–41 / 16–44 | Utah State -3.4 / – | 55.3 / – | no line yet | no line yet (fair: Utah State -145) | no line yet |  |
| Sat 10/31 3:30 PM | UTEP @ North Dakota State | UTEP 7, North Dakota State 35 | North Dakota State 99% | UTEP +8370 / North Dakota State -8370 | 6.8 – 34.7 | 0–14 / 20–51 | North Dakota State -27.9 / – | 41.5 / – | no line yet | no line yet (fair: North Dakota State -8370) | no line yet |  |
| Sat 10/31 3:30 PM | Florida International @ Liberty | Florida International 17, Liberty 31 | Liberty 86% | Florida International +605 / Liberty -605 | 15.8 – 30.8 | 6–28 / 17–45 | Liberty -15.0 / – | 46.6 / – | no line yet | no line yet (fair: Liberty -605) | no line yet |  |
| Sat 10/31 3:30 PM | Southern Miss @ UL Monroe | Southern Miss 27, UL Monroe 24 | Southern Miss 58% | Southern Miss -135 / UL Monroe +135 | 28.7 – 25.9 | 14–43 / 13–40 | Southern Miss -2.8 / – | 55.2 / – | no line yet | no line yet (fair: Southern Miss -135) | no line yet |  |
| Sat 10/31 3:45 PM | Utah @ Cincinnati | Utah 31, Cincinnati 24 | Utah 73% | Utah -275 / Cincinnati +275 | 33.4 – 23.9 | 19–49 / 10–38 | Utah -8.7 / Utah -9.5 | 60.6 / 56.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:45 PM | Virginia @ Wake Forest | Virginia 17, Wake Forest 34 | Wake Forest 86% | Virginia +615 / Wake Forest -615 | 16.5 – 31.8 | 6–29 / 17–48 | Wake Forest -15.3 / – | 48.3 / – | no line yet | no line yet (fair: Wake Forest -615) | no line yet |  |
| Sat 10/31 4:00 PM | New Mexico @ San José State | New Mexico 31, San José State 17 | New Mexico 79% | New Mexico -365 / San José State +365 | 30.7 – 18.8 | 16–45 / 7–31 | New Mexico -11.9 / – | 49.4 / – | no line yet | no line yet (fair: New Mexico -365) | no line yet |  |
| Sat 10/31 4:15 PM | South Carolina @ Oklahoma | South Carolina 17, Oklahoma 24 | Oklahoma 67% | South Carolina +200 / Oklahoma -200 | 18.5 – 24.5 | 7–31 / 10–38 | Oklahoma -10.5 / Oklahoma -5.5 | 44.4 / 43.5 | no edge | no edge | no edge |  |
| Sat 10/31 4:15 PM | Nevada @ UCLA | Nevada 6, UCLA 41 | UCLA 99% | Nevada +9900 / UCLA -9900 | 7.3 – 40.7 | 0–15 / 27–57 | UCLA -33.5 / – | 48.0 / – | no line yet | no line yet (fair: UCLA -9900) | no line yet |  |
| Sat 10/31 6:30 PM | App State @ Georgia Southern | App State 31, Georgia Southern 28 | App State 53% | App State -110 / Georgia Southern +110 | 29.1 – 28.1 | 14–44 / 14–42 | App State -1.0 / – | 57.1 / – | no line yet | no line yet (fair: App State -110) | no line yet |  |
| Sat 10/31 7:00 PM | Oklahoma State @ Iowa State | Oklahoma State 24, Iowa State 31 | Iowa State 66% | Oklahoma State +190 / Iowa State -190 | 24.0 – 29.9 | 10–38 / 16–45 | Iowa State -5.9 / – | 53.9 / – | no line yet | no line yet (fair: Iowa State -190) | no line yet |  |
| Sat 10/31 7:00 PM | Clemson @ Florida State | Clemson 27, Florida State 24 | Clemson 53% | Clemson -115 / Florida State +115 | 26.3 – 25.3 | 13–41 / 13–39 | Florida State -3.9 / Clemson -1.5 | 52.1 / 51.5 | no edge | no edge | no edge |  |
| Sat 10/31 7:00 PM | Washington State @ San Diego State | Washington State 21, San Diego State 24 | San Diego State 57% | Washington State +130 / San Diego State -130 | 21.2 – 23.5 | 9–34 / 10–38 | San Diego State -2.3 / – | 44.7 / – | no line yet | no line yet (fair: San Diego State -130) | no line yet |  |
| Sat 10/31 7:30 PM | Mississippi State @ Texas | Mississippi State 21, Texas 31 | Texas 75% | Mississippi State +300 / Texas -300 | 20.9 – 30.8 | 9–34 / 17–45 | Texas -9.9 / – | 51.7 / – | no line yet | no line yet (fair: Texas -300) | no line yet |  |
| Sat 10/31 7:30 PM | Georgia Tech @ Pittsburgh | Georgia Tech 24, Pittsburgh 31 | Pittsburgh 72% | Georgia Tech +255 / Pittsburgh -255 | 22.6 – 30.9 | 10–36 / 17–45 | Pittsburgh -8.3 / – | 53.5 / – | no line yet | no line yet (fair: Pittsburgh -255) | no line yet |  |
| Sat 10/31 7:30 PM | Miami @ North Carolina | Miami 31, North Carolina 17 | Miami 85% | Miami -565 / North Carolina +565 | 32.9 – 18.1 | 17–48 / 7–31 | Miami -18.1 / Miami -14.5 | 53.0 / 50.5 | no edge | no edge | no edge |  |
| Sat 10/31 7:30 PM | Ohio State @ USC | Ohio State 31, USC 24 | Ohio State 67% | Ohio State -205 / USC +205 | 30.4 – 23.6 | 17–45 / 10–38 | Ohio State -9.9 / Ohio State -6.5 | 56.5 / 53.5 | no edge | no edge | no edge |  |
| Sat 10/31 7:45 PM | Missouri @ Arkansas | Missouri 31, Arkansas 17 | Missouri 82% | Missouri -450 / Arkansas +450 | 30.1 – 17.3 | 16–45 / 6–30 | Missouri -12.8 / – | 49.0 / – | no line yet | no line yet (fair: Missouri -450) | no line yet |  |
| Sat 10/31 8:00 PM | Washington @ Nebraska | Washington 21, Nebraska 28 | Nebraska 73% | Washington +270 / Nebraska -270 | 19.9 – 28.7 | 7–33 / 14–44 | Nebraska -8.8 / – | 48.5 / – | no line yet | no line yet (fair: Nebraska -270) | no line yet |  |
| Sat 10/31 8:00 PM | Army @ Memphis | Army 28, Memphis 31 | Memphis 64% | Army +180 / Memphis -180 | 27.3 – 32.9 | 14–42 / 19–48 | Memphis -5.6 / – | 60.2 / – | no line yet | no line yet (fair: Memphis -180) | no line yet |  |
| Sat 10/31 10:00 PM | Texas State @ Boise State | Texas State 31, Boise State 38 | Boise State 72% | Texas State +260 / Boise State -260 | 28.0 – 36.9 | 14–42 / 22–52 | Boise State -8.9 / – | 64.8 / – | no line yet | no line yet (fair: Boise State -260) | no line yet |  |
| Sat 10/31 10:30 PM | Northern Illinois @ UNLV | Northern Illinois 17, UNLV 34 | UNLV 85% | Northern Illinois +555 / UNLV -555 | 18.7 – 33.9 | 7–31 / 19–49 | UNLV -15.2 / – | 52.6 / – | no line yet | no line yet (fair: UNLV -555) | no line yet |  |
| Sat 10/31 11:00 PM | Oregon State @ Fresno State | Oregon State 31, Fresno State 28 | Oregon State 60% | Oregon State -150 / Fresno State +150 | 30.2 – 26.3 | 16–45 / 13–41 | Oregon State -3.9 / – | 56.4 / – | no line yet | no line yet (fair: Oregon State -150) | no line yet |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 522 | 11.61 | 12.02 | 8.36 | 81.2% | 0.130 | 83.0% |
| Model only (before blending) | 522 | 12.35 | 12.35 | 8.64 | 78.9% | – | – |
| Betting line when predicted | 520 | 11.60 | 11.98 | 8.35 | 81.2% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin of an FBS game by about 12.5 points.

501 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
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

## FBS power ratings

Points per game better than an average FBS team on a neutral field, from opponent-adjusted EPA (garbage time removed) with this season's games weighted against a preseason prior, plus the weight the margin model puts on Elo (a rating built from game results alone). Defense is positive when it holds opponents below average.

| # | Team | Conference | Net | Offense | Defense | Special teams | Results (Elo) | Elo rating |
|---|---|---|---|---|---|---|---|---|
| 1 | Ohio State | Big Ten | +26.8 | +10.7 | +10.5 | +0.4 | +5.1 | 1934 |
| 2 | LSU | SEC | +24.3 | +9.0 | +12.6 | +0.2 | +2.5 | 1717 |
| 3 | Notre Dame | FBS Independents | +24.1 | +8.5 | +10.1 | +1.3 | +4.1 | 1849 |
| 4 | Georgia | SEC | +23.4 | +9.6 | +8.6 | +0.9 | +4.3 | 1866 |
| 5 | Miami | ACC | +22.6 | +11.5 | +6.5 | +0.1 | +4.5 | 1881 |
| 6 | Indiana | Big Ten | +22.2 | +7.9 | +9.0 | +0.3 | +5.0 | 1921 |
| 7 | Texas Tech | Big 12 | +19.1 | +1.8 | +12.6 | +1.2 | +3.5 | 1803 |
| 8 | Ole Miss | SEC | +19.0 | +11.0 | +3.4 | +0.7 | +3.9 | 1834 |
| 9 | Alabama | SEC | +19.0 | +8.3 | +7.4 | +0.3 | +3.0 | 1760 |
| 10 | Texas | SEC | +18.0 | +3.5 | +10.9 | +0.5 | +3.2 | 1770 |
| 11 | Utah | Big 12 | +17.7 | +8.6 | +5.3 | +0.3 | +3.5 | 1801 |
| 12 | Oregon | Big Ten | +17.7 | +4.1 | +9.9 | +0.4 | +3.3 | 1784 |
| 13 | Tennessee | SEC | +16.3 | +3.4 | +9.2 | +0.7 | +3.0 | 1753 |
| 14 | Oklahoma | SEC | +16.1 | +0.4 | +13.3 | +0.7 | +1.7 | 1649 |
| 15 | UCLA | Big Ten | +16.0 | +6.4 | +7.2 | +0.6 | +1.8 | 1657 |
| 16 | BYU | Big 12 | +15.5 | +6.1 | +5.4 | +0.4 | +3.7 | 1814 |
| 17 | Missouri | SEC | +15.4 | +3.9 | +8.9 | +0.5 | +2.1 | 1686 |
| 18 | Michigan | Big Ten | +14.9 | +4.2 | +8.3 | +0.4 | +2.0 | 1674 |
| 19 | Louisville | ACC | +14.9 | +8.6 | +4.1 | +0.3 | +1.9 | 1663 |
| 20 | Wake Forest | ACC | +14.9 | +5.6 | +6.9 | +0.1 | +2.2 | 1688 |
| 21 | USC | Big Ten | +14.6 | +12.2 | -0.6 | +0.3 | +2.7 | 1734 |
| 22 | Auburn | SEC | +14.2 | +5.0 | +7.6 | +0.6 | +0.9 | 1584 |
| 23 | Florida | SEC | +14.0 | +8.9 | +3.1 | +1.0 | +1.0 | 1592 |
| 24 | Nebraska | Big Ten | +14.0 | +4.6 | +7.5 | +0.5 | +1.4 | 1622 |
| 25 | Iowa | Big Ten | +12.4 | +2.2 | +6.3 | +1.0 | +3.0 | 1756 |
| 26 | Kansas State | Big 12 | +12.3 | +7.9 | +3.1 | +0.3 | +1.1 | 1599 |
| 27 | Texas A&M | SEC | +12.3 | +2.2 | +8.2 | +0.5 | +1.3 | 1618 |
| 28 | SMU | ACC | +12.0 | +5.7 | +4.0 | +0.0 | +2.4 | 1705 |
| 29 | Arizona | Big 12 | +11.5 | +5.5 | +3.6 | -0.0 | +2.4 | 1710 |
| 30 | Houston | Big 12 | +11.1 | +8.7 | +0.2 | +0.0 | +2.2 | 1690 |
| 31 | Mississippi State | SEC | +10.7 | +7.1 | +2.8 | +0.3 | +0.5 | 1551 |
| 32 | Northwestern | Big Ten | +10.7 | +5.5 | +2.3 | +1.3 | +1.6 | 1640 |
| 33 | Penn State | Big Ten | +10.7 | +2.5 | +6.7 | +0.5 | +1.0 | 1593 |
| 34 | Wisconsin | Big Ten | +8.4 | +0.9 | +6.7 | +0.2 | +0.6 | 1559 |
| 35 | Washington | Big Ten | +8.2 | +2.4 | +4.3 | -0.1 | +1.5 | 1635 |
| 36 | Kentucky | SEC | +8.1 | +1.8 | +4.5 | +0.2 | +1.7 | 1653 |
| 37 | Kansas | Big 12 | +8.0 | +6.1 | +2.6 | +0.2 | -0.8 | 1441 |
| 38 | South Carolina | SEC | +7.9 | +3.8 | +2.6 | +0.8 | +0.7 | 1569 |
| 39 | Iowa State | Big 12 | +7.9 | +3.0 | +3.2 | +0.9 | +0.8 | 1578 |
| 40 | Baylor | Big 12 | +6.8 | -0.4 | +5.5 | +1.1 | +0.6 | 1559 |
| 41 | Cincinnati | Big 12 | +6.5 | +8.7 | -2.7 | +0.3 | +0.2 | 1522 |
| 42 | Florida State | ACC | +6.1 | +7.9 | -1.6 | -0.1 | -0.1 | 1497 |
| 43 | TCU | Big 12 | +5.8 | -1.2 | +5.4 | +0.5 | +1.3 | 1613 |
| 44 | Boise State | Pac-12 | +5.5 | +4.1 | -1.1 | +0.2 | +2.3 | 1702 |
| 45 | Vanderbilt | SEC | +5.4 | +4.2 | +0.3 | +0.4 | +0.5 | 1553 |
| 46 | Duke | ACC | +5.3 | +2.1 | +0.7 | +0.7 | +1.7 | 1653 |
| 47 | Oklahoma State | Big 12 | +4.9 | +5.2 | -0.2 | +0.5 | -0.5 | 1464 |
| 48 | Virginia Tech | ACC | +4.5 | +3.7 | +0.3 | +0.3 | +0.3 | 1531 |
| 49 | Pittsburgh | ACC | +4.4 | -0.4 | +3.6 | +0.7 | +0.5 | 1551 |
| 50 | UCF | Big 12 | +4.3 | +0.9 | +4.1 | +0.0 | -0.7 | 1448 |
| 51 | Clemson | ACC | +4.1 | -4.1 | +6.6 | +0.4 | +1.3 | 1613 |
| 52 | James Madison | Sun Belt | +3.8 | -0.1 | +0.6 | +0.4 | +2.9 | 1747 |
| 53 | Arizona State | Big 12 | +3.4 | +1.1 | +1.9 | +0.3 | +0.2 | 1521 |
| 54 | Colorado | Big 12 | +3.4 | -0.3 | +6.0 | -0.7 | -1.6 | 1377 |
| 55 | Minnesota | Big Ten | +3.2 | -2.4 | +4.9 | +0.5 | +0.3 | 1532 |
| 56 | North Texas | American Athletic | +3.0 | +9.0 | -6.3 | -0.9 | +1.1 | 1603 |
| 57 | NC State | ACC | +3.0 | +7.2 | -3.8 | -0.6 | +0.1 | 1515 |
| 58 | Oregon State | Pac-12 | +3.0 | +5.3 | -2.3 | +0.0 | -0.1 | 1498 |
| 59 | Virginia | ACC | +2.3 | -1.2 | +3.5 | -0.2 | +0.1 | 1517 |
| 60 | Illinois | Big Ten | +1.8 | +5.4 | -4.3 | +0.3 | +0.4 | 1539 |
| 61 | North Carolina | ACC | +1.6 | +0.9 | -0.2 | +0.6 | +0.3 | 1532 |
| 62 | Syracuse | ACC | +1.4 | +1.1 | +2.6 | -0.3 | -1.9 | 1347 |
| 63 | Maryland | Big Ten | +1.4 | -0.6 | +3.4 | +0.5 | -2.0 | 1343 |
| 64 | Memphis | American Athletic | +1.2 | +3.0 | -2.0 | -0.5 | +0.7 | 1566 |
| 65 | UTSA | American Athletic | +1.0 | +2.7 | -3.1 | -0.1 | +1.5 | 1636 |
| 66 | Arkansas | SEC | +1.0 | +1.0 | +0.4 | -0.4 | -0.2 | 1496 |
| 67 | Purdue | Big Ten | +0.9 | +3.1 | -1.8 | +0.5 | -0.8 | 1444 |
| 68 | Texas State | Pac-12 | +0.7 | +7.3 | -5.8 | -1.5 | +0.6 | 1559 |
| 69 | Toledo | Mid-American | -0.2 | -2.1 | +1.3 | +0.4 | +0.2 | 1522 |
| 70 | New Mexico | Mountain West | -0.3 | -2.1 | +0.5 | +0.2 | +1.1 | 1598 |
| 71 | Georgia Tech | ACC | -0.8 | +3.3 | -3.8 | -0.0 | -0.3 | 1480 |
| 72 | West Virginia | Big 12 | -0.9 | +4.1 | -5.0 | +0.6 | -0.6 | 1462 |
| 73 | Liberty | Conference USA | -1.1 | -0.5 | -0.7 | -0.1 | +0.2 | 1527 |
| 74 | North Dakota State | Mountain West | -1.1 | -4.7 | +3.5 | +1.1 | -1.1 | 1419 |
| 75 | Navy | American Athletic | -1.4 | +1.9 | -2.9 | -0.5 | +0.0 | 1512 |
| 76 | South Florida | American Athletic | -1.6 | -1.3 | -1.0 | -0.1 | +0.8 | 1572 |
| 77 | UConn | FBS Independents | -2.3 | +1.4 | -3.4 | -0.3 | -0.0 | 1507 |
| 78 | Army | American Athletic | -2.3 | +4.9 | -8.0 | -0.2 | +1.1 | 1602 |
| 79 | Florida Atlantic | American Athletic | -2.8 | +2.7 | -4.8 | +0.4 | -1.1 | 1419 |
| 80 | Rutgers | Big Ten | -2.8 | +3.2 | -5.2 | +0.3 | -1.1 | 1417 |
| 81 | Michigan State | Big Ten | -2.9 | -2.2 | +0.3 | +0.2 | -1.3 | 1399 |
| 82 | Ohio | Mid-American | -3.1 | -0.7 | -3.8 | +0.6 | +0.8 | 1571 |
| 83 | Fresno State | Pac-12 | -3.3 | -2.4 | -1.3 | -0.0 | +0.4 | 1544 |
| 84 | Tulane | American Athletic | -3.4 | -4.6 | +0.0 | +0.0 | +1.2 | 1604 |
| 85 | East Carolina | American Athletic | -3.5 | -5.0 | +2.4 | -0.6 | -0.3 | 1484 |
| 86 | Tulsa | American Athletic | -3.7 | -0.9 | -0.6 | -0.4 | -1.8 | 1358 |
| 87 | Air Force | Mountain West | -4.6 | +2.6 | -6.3 | -0.2 | -0.7 | 1453 |
| 88 | UNLV | Mountain West | -4.8 | -2.9 | -2.3 | +0.0 | +0.4 | 1540 |
| 89 | California | ACC | -4.9 | -0.8 | -2.3 | -0.5 | -1.3 | 1403 |
| 90 | Louisiana Tech | Sun Belt | -5.4 | -3.7 | -0.4 | -0.8 | -0.5 | 1464 |
| 91 | Jacksonville State | Conference USA | -6.1 | -0.6 | -4.6 | -0.4 | -0.5 | 1465 |
| 92 | Boston College | ACC | -6.5 | -4.7 | +0.0 | -0.8 | -0.9 | 1430 |
| 93 | Marshall | Sun Belt | -6.7 | -2.2 | -3.7 | -0.2 | -0.6 | 1462 |
| 94 | Washington State | Pac-12 | -6.7 | -6.2 | +1.3 | -0.4 | -1.5 | 1388 |
| 95 | App State | Sun Belt | -7.1 | -2.9 | -3.3 | -0.2 | -0.7 | 1454 |
| 96 | Western Michigan | Mid-American | -7.3 | -5.1 | -3.5 | +0.4 | +0.9 | 1584 |
| 97 | Georgia State | Sun Belt | -7.6 | +0.4 | -6.9 | -0.1 | -1.0 | 1424 |
| 98 | Miami (OH) | Mid-American | -7.7 | -3.9 | -3.6 | +0.6 | -0.9 | 1435 |
| 99 | San Diego State | Pac-12 | -7.7 | -7.4 | +0.1 | +0.6 | -1.0 | 1425 |
| 100 | Louisiana | Sun Belt | -8.4 | -4.4 | -4.2 | +0.0 | +0.1 | 1520 |
| 101 | Delaware | Conference USA | -8.7 | -1.7 | -5.3 | +0.2 | -1.9 | 1352 |
| 102 | Stanford | ACC | -9.0 | -3.4 | -4.8 | -0.2 | -0.5 | 1465 |
| 103 | UAB | American Athletic | -9.4 | -5.1 | -3.4 | -0.0 | -1.0 | 1427 |
| 104 | Temple | American Athletic | -9.5 | +1.0 | -7.6 | -0.5 | -2.5 | 1303 |
| 105 | Georgia Southern | Sun Belt | -9.6 | -2.2 | -6.0 | -1.0 | -0.3 | 1481 |
| 106 | Utah State | Pac-12 | -10.2 | -8.2 | +0.7 | -1.3 | -1.4 | 1393 |
| 107 | Western Kentucky | Conference USA | -10.3 | -7.0 | -1.8 | -0.2 | -1.3 | 1399 |
| 108 | Troy | Sun Belt | -10.4 | -5.9 | -2.2 | -1.2 | -1.1 | 1416 |
| 109 | Wyoming | Mountain West | -11.0 | -6.3 | -3.4 | -0.2 | -1.1 | 1413 |
| 110 | Arkansas State | Sun Belt | -11.1 | -3.5 | -6.5 | -0.0 | -1.1 | 1416 |
| 111 | South Alabama | Sun Belt | -11.3 | +0.2 | -10.9 | +0.2 | -0.8 | 1438 |
| 112 | Colorado State | Pac-12 | -11.8 | +1.2 | -9.5 | -0.6 | -2.9 | 1271 |
| 113 | Old Dominion | Sun Belt | -12.2 | -12.8 | +2.8 | -1.2 | -0.9 | 1431 |
| 114 | Florida International | Conference USA | -12.9 | -9.5 | -1.1 | -0.7 | -1.6 | 1377 |
| 115 | Coastal Carolina | Sun Belt | -13.3 | -5.8 | -5.9 | +0.4 | -2.1 | 1332 |
| 116 | Nevada | Mountain West | -13.5 | -8.2 | -3.1 | +0.4 | -2.6 | 1292 |
| 117 | Hawai'i | Mountain West | -13.5 | -6.2 | -5.7 | +0.6 | -2.2 | 1326 |
| 118 | Missouri State | Conference USA | -14.1 | -1.6 | -8.0 | -1.4 | -3.1 | 1253 |
| 119 | New Mexico State | Conference USA | -14.2 | -7.8 | -2.6 | -1.4 | -2.4 | 1307 |
| 120 | San José State | Mountain West | -14.3 | -7.8 | -4.4 | -0.3 | -1.8 | 1356 |
| 121 | Central Michigan | Mid-American | -14.3 | -7.2 | -5.2 | -0.4 | -1.5 | 1386 |
| 122 | Kennesaw State | Conference USA | -14.9 | -6.7 | -4.7 | -0.8 | -2.6 | 1295 |
| 123 | Rice | American Athletic | -14.9 | -6.4 | -4.6 | -0.8 | -3.1 | 1252 |
| 124 | Middle Tennessee | Conference USA | -15.1 | -5.7 | -7.1 | +0.1 | -2.4 | 1309 |
| 125 | Southern Miss | Sun Belt | -15.2 | -6.5 | -4.2 | -1.5 | -3.1 | 1254 |
| 126 | Northern Illinois | Mountain West | -16.8 | -5.1 | -7.1 | -0.7 | -3.9 | 1188 |
| 127 | Eastern Michigan | Mid-American | -17.1 | -6.6 | -7.6 | -0.8 | -2.1 | 1337 |
| 128 | Massachusetts | Mid-American | -17.2 | -9.4 | -4.1 | -0.2 | -3.5 | 1219 |
| 129 | Sam Houston | Conference USA | -17.8 | -11.6 | -0.9 | -1.3 | -4.0 | 1173 |
| 130 | Ball State | Mid-American | -18.4 | -6.4 | -7.5 | -1.1 | -3.4 | 1230 |
| 131 | Bowling Green | Mid-American | -18.4 | -12.2 | -3.5 | -0.2 | -2.6 | 1294 |
| 132 | Buffalo | Mid-American | -18.8 | -13.7 | -4.8 | +0.6 | -1.0 | 1429 |
| 133 | Kent State | Mid-American | -20.2 | -10.4 | -6.2 | -1.0 | -2.6 | 1290 |
| 134 | UL Monroe | Sun Belt | -20.5 | -6.3 | -8.2 | -1.5 | -4.5 | 1139 |
| 135 | Sacramento State | Mid-American | -20.6 | -9.8 | -6.2 | +0.4 | -5.0 | 1095 |
| 136 | Charlotte | American Athletic | -20.8 | -8.6 | -8.2 | -0.4 | -3.6 | 1211 |
| 137 | Akron | Mid-American | -22.0 | -10.7 | -6.7 | -1.2 | -3.3 | 1233 |
| 138 | UTEP | Mountain West | -24.0 | -11.9 | -6.0 | -1.4 | -4.7 | 1123 |

## Current model fit

- Fitted on 4139 games from seasons 2022–2026.
- Home field on top of the ratings: 3.2 points (1.8 in conference games).
- Extra FBS edge over FCS opponents beyond their ratings: 14.0 points.
- Elo weight: 0.19 points of margin per point of Elo spread.
- Weight on the betting line: 91% for the margin, 81% for the total.
