# College football score predictions

Updated Wed Nov 18, 2026 10:19 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 12

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thu 11/19 7:30 PM | Rice @ Temple | Rice 24, Temple 27 | Temple 58% | Rice +140 / Temple -140 | 24.4 – 27.5 | 10–38 / 14–42 | Temple -4.0 / Temple -3.0 | 53.9 / 51.5 | no edge | no edge | no edge |  |
| Fri 11/20 6:00 PM | Iowa State @ UCF | Iowa State 24, UCF 27 | UCF 54% | Iowa State +120 / UCF -120 | 23.7 – 25.4 | 10–38 / 13–39 | Iowa State -3.7 / UCF -2.2 | 52.7 / 48.5 | no edge | no edge | no edge |  |
| Fri 11/20 7:30 PM | Clemson @ Duke | Clemson 14, Duke 28 | Duke 83% | Clemson +485 / Duke -485 | 14.2 – 27.2 | 3–26 / 14–42 | Duke -8.0 / Duke -13.5 | 46.0 / 40.5 | no edge | no edge | no edge |  |
| Fri 11/20 7:30 PM | Bowling Green @ Toledo | Bowling Green 14, Toledo 31 | Toledo 88% | Bowling Green +750 / Toledo -750 | 15.5 – 32.3 | 3–27 / 17–48 | Toledo -19.9 / Toledo -16.5 | 44.5 / 48.5 | no edge | no edge | no edge |  |
| Fri 11/20 8:00 PM | Oregon @ Michigan State | Oregon 31, Michigan State 14 | Oregon 89% | Oregon -840 / Michigan State +840 | 31.0 – 13.9 | 17–46 / 3–25 | Oregon -19.9 / Oregon -16.8 | 46.9 / 44.5 | no edge | no edge | no edge |  |
| Fri 11/20 8:00 PM | UTEP @ Air Force | UTEP 10, Air Force 34 | Air Force 95% | UTEP +1895 / Air Force -1895 | 12.6 – 35.5 | 3–24 / 20–52 | Air Force -24.5 / Air Force -22.8 | 50.7 / 47.5 | no edge | no edge | no edge |  |
| Fri 11/20 9:00 PM | New Mexico @ Wyoming | New Mexico 24, Wyoming 17 | New Mexico 70% | New Mexico -240 / Wyoming +240 | 22.8 – 15.5 | 10–37 / 6–27 | New Mexico -5.1 / New Mexico -7.5 | 43.3 / 37.5 | no edge | no edge | no edge |  |
| Sat 11/21 12:00 PM | Vanderbilt @ Florida | Vanderbilt 17, Florida 31 | Florida 81% | Vanderbilt +430 / Florida -430 | 17.0 – 30.1 | 6–30 / 16–45 | Florida -9.3 / Florida -13.5 | 50.8 / 46.2 | no edge | no edge | no edge |  |
| Sat 11/21 12:00 PM | Wofford @ Ole Miss | Wofford 3, Ole Miss 55 | Ole Miss 100% | Wofford +9900 / Ole Miss -9900 | 5.3 – 55.3 | 0–12 / 41–71 | Ole Miss -55.0 / Ole Miss -49.5 | 61.0 / 60.5 | no edge | no line yet (fair: Ole Miss -9900) | no edge | FCS opponent |
| Sat 11/21 12:00 PM | BYU @ Kansas | BYU 28, Kansas 21 | BYU 65% | BYU -185 / Kansas +185 | 26.6 – 21.2 | 13–41 / 9–34 | BYU -2.2 / BYU -5.8 | 51.6 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/21 12:00 PM | Colorado @ Cincinnati | Colorado 28, Cincinnati 31 | Cincinnati 58% | Colorado +140 / Cincinnati -140 | 27.7 – 31.0 | 14–42 / 17–45 | Cincinnati -4.3 / Cincinnati -3.2 | 59.3 / 58.5 | no edge | no edge | no edge |  |
| Sat 11/21 12:00 PM | Syracuse @ Boston College | Syracuse 27, Boston College 24 | Syracuse 58% | Syracuse -135 / Boston College +135 | 26.9 – 24.0 | 13–41 / 10–38 | Syracuse -7.3 / Syracuse -2.5 | 51.4 / 50.8 | no edge | no edge | no edge |  |
| Sat 11/21 12:00 PM | Wake Forest @ Georgia Tech | Wake Forest 38, Georgia Tech 17 | Wake Forest 92% | Wake Forest -1120 / Georgia Tech +1120 | 38.1 – 17.4 | 23–54 / 6–31 | Wake Forest -22.7 / Wake Forest -20.5 | 54.3 / 55.8 | no edge | no edge | no edge |  |
| Sat 11/21 12:00 PM | Northwestern @ Minnesota | Northwestern 24, Minnesota 21 | Northwestern 58% | Northwestern -135 / Minnesota +135 | 22.5 – 19.8 | 10–36 / 7–32 | Northwestern -4.8 / Northwestern -2.5 | 46.0 / 41.5 | no edge | no edge | no edge |  |
| Sat 11/21 12:00 PM | Ohio State @ Nebraska | Ohio State 24, Nebraska 21 | Ohio State 61% | Ohio State -155 / Nebraska +155 | 23.4 – 19.7 | 10–37 / 7–31 | Ohio State -7.4 / Ohio State -3.2 | 49.4 / 41.8 | no edge | no edge | no edge |  |
| Sat 11/21 12:00 PM | Wisconsin @ Purdue | Wisconsin 27, Purdue 20 | Wisconsin 66% | Wisconsin -195 / Purdue +195 | 26.3 – 20.3 | 13–41 / 7–34 | Wisconsin -6.0 / Wisconsin -6.0 | 47.1 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/21 12:00 PM | East Carolina @ Army | East Carolina 21, Army 24 | Army 65% | East Carolina +185 / Army -185 | 20.5 – 26.2 | 8–34 / 13–41 | Army -2.7 / Army -6.0 | 52.2 / 45.5 | no edge | no edge | no edge |  |
| Sat 11/21 12:00 PM | Memphis @ Navy | Memphis 34, Navy 31 | Memphis 58% | Memphis -140 / Navy +140 | 34.6 – 31.5 | 20–49 / 17–46 | Memphis -1.8 / Memphis -3.2 | 60.6 / 67.2 | no edge | no edge | no edge |  |
| Sat 11/21 12:00 PM | North Texas @ Tulane | North Texas 31, Tulane 24 | North Texas 67% | North Texas -200 / Tulane +200 | 31.6 – 25.1 | 17–47 / 13–39 | North Texas -5.9 / North Texas -6.5 | 61.3 / 55.8 | no edge | no edge | no edge |  |
| Sat 11/21 12:30 PM | North Carolina @ Virginia | North Carolina 21, Virginia 24 | Virginia 55% | North Carolina +120 / Virginia -120 | 21.5 – 23.1 | 10–35 / 10–37 | Virginia -1.0 / Virginia -1.8 | 49.6 / 43.5 | no edge | no edge | no edge |  |
| Sat 11/21 1:00 PM | Tennessee Tech @ Mississippi State | Tennessee Tech 10, Mississippi State 45 | Mississippi State 99% | Tennessee Tech +9900 / Mississippi State -9900 | 11.6 – 46.6 | 3–21 / 31–63 | Mississippi State -29.7 / Mississippi State -35.5 | 52.0 / 59.5 | no edge | no line yet (fair: Mississippi State -9900) | no edge | FCS opponent |
| Sat 11/21 1:00 PM | Houston @ West Virginia | Houston 38, West Virginia 31 | Houston 70% | Houston -230 / West Virginia +230 | 39.0 – 30.8 | 24–55 / 16–45 | Houston -8.0 / Houston -8.2 | 66.2 / 70.5 | no edge | no edge | no edge |  |
| Sat 11/21 1:00 PM | Western Kentucky @ Liberty | Western Kentucky 17, Liberty 34 | Liberty 88% | Western Kentucky +715 / Liberty -715 | 18.0 – 35.0 | 7–31 / 20–51 | Liberty -14.4 / Liberty -17.2 | 52.8 / 53.0 | no edge | no edge | no edge |  |
| Sat 11/21 2:00 PM | Chattanooga @ Alabama | Chattanooga 3, Alabama 52 | Alabama 100% | Chattanooga +9900 / Alabama -9900 | 4.4 – 54.2 | 0–10 / 40–70 | Alabama -53.2 / Alabama -49.5 | 59.2 / 58.5 | no edge | no line yet (fair: Alabama -9900) | no edge | FCS opponent |
| Sat 11/21 2:00 PM | Charlotte @ Tulsa | Charlotte 14, Tulsa 38 | Tulsa 95% | Charlotte +1835 / Tulsa -1835 | 14.7 – 37.5 | 3–26 / 23–53 | Tulsa -23.7 / Tulsa -22.8 | 51.9 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/21 2:00 PM | Missouri State @ Jacksonville State | Missouri State 21, Jacksonville State 31 | Jacksonville State 77% | Missouri State +330 / Jacksonville State -330 | 21.2 – 32.1 | 9–34 / 17–48 | Jacksonville State -13.0 / Jacksonville State -10.8 | 53.5 / 53.2 | no edge | no edge | no edge |  |
| Sat 11/21 2:00 PM | Middle Tennessee @ Sam Houston | Middle Tennessee 24, Sam Houston 21 | Middle Tennessee 65% | Middle Tennessee -185 / Sam Houston +185 | 26.5 – 21.0 | 13–41 / 9–34 | Middle Tennessee -3.6 / Middle Tennessee -5.8 | 44.2 / 48.2 | no edge | no edge | no edge |  |
| Sat 11/21 2:30 PM | Iowa @ Illinois | Iowa 24, Illinois 17 | Iowa 73% | Iowa -275 / Illinois +275 | 25.3 – 16.7 | 13–39 / 6–28 | Iowa -6.8 / Iowa -8.8 | 49.0 / 40.5 | no edge | no edge | Over 40.5 (-110*): EV +3.0%, 54%, stake 0.8u | * price not posted; assumed -110 |
| Sat 11/21 2:30 PM | South Florida @ Florida Atlantic | South Florida 34, Florida Atlantic 31 | South Florida 52% | South Florida -110 / Florida Atlantic +110 | 32.6 – 31.5 | 17–48 / 17–47 | Florida Atlantic -0.7 / South Florida -1.2 | 63.0 / 64.2 | no edge | no edge | no edge |  |
| Sat 11/21 2:30 PM | UL Monroe @ App State | UL Monroe 17, App State 31 | App State 83% | UL Monroe +500 / App State -500 | 18.6 – 32.4 | 7–31 / 17–48 | App State -12.3 / App State -14.0 | 54.4 / 50.2 | no edge | no edge | no edge |  |
| Sat 11/21 3:00 PM | Coastal Carolina @ Louisiana | Coastal Carolina 21, Louisiana 31 | Louisiana 76% | Coastal Carolina +320 / Louisiana -320 | 20.2 – 30.3 | 7–34 / 16–45 | Louisiana -5.9 / Louisiana -10.5 | 50.7 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/21 3:00 PM | Delaware @ New Mexico State | Delaware 27, New Mexico State 24 | Delaware 59% | Delaware -145 / New Mexico State +145 | 28.7 – 25.1 | 14–43 / 13–38 | Delaware -8.6 / Delaware -3.0 | 54.5 / 54.2 | no edge | no edge | no edge |  |
| Sat 11/21 3:00 PM | Florida International @ Kennesaw State | Florida International 21, Kennesaw State 24 | Kennesaw State 61% | Florida International +155 / Kennesaw State -155 | 20.6 – 24.4 | 7–34 / 10–38 | Kennesaw State -6.5 / Kennesaw State -3.5 | 47.2 / 44.5 | no edge | no edge | no edge |  |
| Sat 11/21 3:30 PM | Samford @ Auburn | Samford 3, Auburn 52 | Auburn 100% | Samford +9900 / Auburn -9900 | 5.0 – 53.4 | 0–10 / 38–69 | Auburn -47.3 / Auburn -48.5 | 53.3 / 59.5 | no edge | no line yet (fair: Auburn -9900) | no edge | FCS opponent |
| Sat 11/21 3:30 PM | LSU @ Tennessee | LSU 24, Tennessee 21 | LSU 53% | LSU -115 / Tennessee +115 | 23.7 – 22.5 | 10–37 / 10–35 | LSU -0.7 / LSU -1.2 | 47.9 / 45.8 | no edge | no edge | no edge |  |
| Sat 11/21 3:30 PM | Arkansas @ Texas | Arkansas 10, Texas 31 | Texas 94% | Arkansas +1445 / Texas -1445 | 12.9 – 33.5 | 3–24 / 19–49 | Texas -20.8 / Texas -20.5 | 45.9 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/21 3:30 PM | Texas Tech @ Baylor | Texas Tech 27, Baylor 24 | Texas Tech 60% | Texas Tech -150 / Baylor +150 | 29.2 – 25.4 | 14–44 / 13–40 | Texas Tech -6.6 / Texas Tech -3.5 | 50.8 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/21 3:30 PM | NC State @ Florida State | NC State 24, Florida State 34 | Florida State 75% | NC State +300 / Florida State -300 | 23.4 – 33.6 | 10–37 / 19–49 | Florida State -7.5 / Florida State -10.5 | 59.7 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/21 3:30 PM | UCLA @ Michigan | UCLA 20, Michigan 17 | UCLA 61% | UCLA -155 / Michigan +155 | 20.9 – 17.3 | 9–34 / 7–29 | UCLA -4.7 / UCLA -3.5 | 41.6 / 37.5 | no edge | no edge | no edge |  |
| Sat 11/21 3:30 PM | Rutgers @ Penn State | Rutgers 14, Penn State 38 | Penn State 96% | Rutgers +2315 / Penn State -2315 | 13.3 – 37.6 | 3–24 / 23–54 | Penn State -21.5 / Penn State -24.5 | 51.6 / 50.8 | no edge | no edge | no edge |  |
| Sat 11/21 3:30 PM | Indiana @ Washington | Indiana 24, Washington 17 | Indiana 71% | Indiana -240 / Washington +240 | 25.8 – 18.1 | 13–41 / 7–31 | Indiana -9.4 / Indiana -7.5 | 44.4 / 43.8 | no edge | no edge | no edge |  |
| Sat 11/21 3:30 PM | Old Dominion @ UConn | Old Dominion 17, UConn 31 | UConn 84% | Old Dominion +530 / UConn -530 | 16.8 – 30.9 | 6–29 / 17–45 | UConn -17.0 / UConn -13.8 | 48.7 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/21 3:45 PM | Texas A&M @ Oklahoma | Texas A&M 17, Oklahoma 24 | Oklahoma 71% | Texas A&M +245 / Oklahoma -245 | 15.3 – 23.0 | 5–27 / 10–37 | Oklahoma -9.7 / Oklahoma -7.5 | 38.7 / 38.5 | no edge | no edge | no edge |  |
| Sat 11/21 4:00 PM | Northern Illinois @ North Dakota State | Northern Illinois 10, North Dakota State 34 | North Dakota State 97% | Northern Illinois +3385 / North Dakota State -3385 | 9.6 – 34.4 | 0–20 / 20–50 | North Dakota State -23.3 / North Dakota State -25.0 | 46.4 / 43.5 | no edge | no edge | no edge |  |
| Sat 11/21 4:00 PM | Georgia Southern @ Troy | Georgia Southern 28, Troy 21 | Georgia Southern 73% | Georgia Southern -265 / Troy +265 | 28.6 – 20.0 | 14–43 / 7–33 | Georgia Southern -6.8 / Georgia Southern -8.8 | 49.2 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/21 4:00 PM | Georgia State @ Marshall | Georgia State 24, Marshall 27 | Marshall 57% | Georgia State +135 / Marshall -135 | 26.5 – 29.0 | 13–41 / 14–44 | Marshall -3.2 / Marshall -2.5 | 56.7 / 55.2 | no edge | no edge | no edge |  |
| Sat 11/21 4:00 PM | South Alabama @ Southern Miss | South Alabama 34, Southern Miss 31 | South Alabama 59% | South Alabama -145 / Southern Miss +145 | 34.7 – 30.8 | 20–50 / 17–45 | South Alabama -4.9 / South Alabama -3.8 | 59.9 / 66.8 | no edge | no edge | no edge |  |
| Sat 11/21 6:00 PM | Washington State @ Texas State | Washington State 24, Texas State 38 | Texas State 78% | Washington State +350 / Texas State -350 | 24.8 – 36.4 | 11–38 / 21–52 | Texas State -9.7 / Texas State -11.8 | 60.0 / 61.5 | no edge | no edge | no edge |  |
| Sat 11/21 6:15 PM | Maryland @ USC | Maryland 21, USC 38 | USC 86% | Maryland +635 / USC -635 | 20.4 – 37.2 | 7–34 / 21–53 | USC -12.2 / USC -17.2 | 54.7 / 58.2 | no edge | Maryland (+600): EV +4.2%, 15%, stake 0.2u | no edge |  |
| Sat 11/21 7:00 PM | Arizona @ Kansas State | Arizona 31, Kansas State 24 | Arizona 66% | Arizona -195 / Kansas State +195 | 29.7 – 23.2 | 15–45 / 10–37 | Arizona -1.9 / Arizona -7.0 | 55.1 / 52.5 | no edge | Kansas State (+256): EV +3.3%, 29%, stake 0.3u | no edge |  |
| Sat 11/21 7:00 PM | Virginia Tech @ Miami | Virginia Tech 20, Miami 41 | Miami 92% | Virginia Tech +1085 / Miami -1085 | 19.8 – 40.7 | 7–33 / 24–56 | Miami -24.8 / Miami -20.5 | 59.4 / 60.8 | no edge | no edge | no edge |  |
| Sat 11/21 7:00 PM | UNLV @ San José State | UNLV 28, San José State 21 | UNLV 69% | UNLV -225 / San José State +225 | 27.3 – 20.1 | 14–42 / 7–33 | UNLV -9.5 / UNLV -7.0 | 50.5 / 46.8 | no edge | no edge | no edge |  |
| Sat 11/21 7:00 PM | Arkansas State @ Louisiana Tech | Arkansas State 17, Louisiana Tech 31 | Louisiana Tech 83% | Arkansas State +480 / Louisiana Tech -480 | 19.7 – 33.4 | 7–33 / 18–49 | Louisiana Tech -13.4 / Louisiana Tech -13.8 | 49.8 / 53.8 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | Kentucky @ Missouri | Kentucky 21, Missouri 24 | Missouri 65% | Kentucky +190 / Missouri -190 | 21.4 – 27.1 | 9–35 / 14–42 | Missouri -7.8 / Missouri -5.5 | 48.7 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | Georgia @ South Carolina | Georgia 31, South Carolina 17 | Georgia 85% | Georgia -575 / South Carolina +575 | 33.0 – 17.9 | 17–49 / 7–31 | Georgia -15.8 / Georgia -15.0 | 49.4 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | Pittsburgh @ Louisville | Pittsburgh 17, Louisville 31 | Louisville 83% | Pittsburgh +490 / Louisville -490 | 18.2 – 32.5 | 7–31 / 17–48 | Louisville -16.3 / Louisville -14.0 | 51.6 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | SMU @ Notre Dame | SMU 17, Notre Dame 38 | Notre Dame 92% | SMU +1150 / Notre Dame -1150 | 17.6 – 38.0 | 6–30 / 23–54 | Notre Dame -18.9 / Notre Dame -20.5 | 52.9 / 56.2 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | Stanford @ California | Stanford 31, California 28 | Stanford 57% | Stanford -130 / California +130 | 29.3 – 26.9 | 14–44 / 13–41 | Stanford -0.4 / Stanford -2.5 | 54.8 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | Colorado State @ Fresno State | Colorado State 24, Fresno State 45 | Fresno State 90% | Colorado State +900 / Fresno State -900 | 22.9 – 42.6 | 10–37 / 27–59 | Fresno State -12.1 / Fresno State -20.5 | 61.1 / 66.5 | no edge | Colorado State (+874): EV +6.8%, 11%, stake 0.2u | no edge |  |
| Sat 11/21 8:00 PM | UTSA @ UAB | UTSA 31, UAB 24 | UTSA 68% | UTSA -210 / UAB +210 | 29.1 – 22.5 | 14–44 / 10–36 | UTSA -7.4 / UTSA -6.5 | 51.7 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/21 9:00 PM | Utah @ TCU | Utah 28, TCU 21 | Utah 70% | Utah -230 / TCU +230 | 27.3 – 19.7 | 14–42 / 7–33 | Utah -13.5 / Utah -7.0 | 49.8 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/21 9:30 PM | San Diego State @ Boise State | San Diego State 21, Boise State 38 | Boise State 86% | San Diego State +635 / Boise State -635 | 21.3 – 38.3 | 9–35 / 23–55 | Boise State -13.8 / Boise State -17.2 | 56.7 / 60.2 | no edge | San Diego State (+600): EV +3.8%, 15%, stake 0.2u | no edge |  |
| Sat 11/21 10:15 PM | Oklahoma State @ Arizona State | Oklahoma State 31, Arizona State 28 | Oklahoma State 56% | Oklahoma State -130 / Arizona State +130 | 30.7 – 28.5 | 17–45 / 14–43 | Arizona State -1.1 / Oklahoma State -2.5 | 57.8 / 59.5 | no edge | no edge | no edge |  |
| Sat 11/21 10:30 PM | Utah State @ Oregon State | Utah State 21, Oregon State 31 | Oregon State 75% | Utah State +305 / Oregon State -305 | 20.6 – 30.4 | 7–34 / 17–45 | Oregon State -12.2 / Oregon State -9.5 | 53.2 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/21 10:30 PM | Hawai'i @ Nevada | Hawai'i 17, Nevada 24 | Nevada 63% | Hawai'i +170 / Nevada -170 | 18.7 – 22.9 | 7–31 / 10–37 | Hawai'i -1.3 / Nevada -4.8 | 47.0 / 40.5 | no edge | no edge | no edge |  |

## 2026 Week 13

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/24 7:00 PM | Kent State @ Eastern Michigan | Kent State 24, Eastern Michigan 27 | Eastern Michigan 64% | Kent State +180 / Eastern Michigan -180 | 22.5 – 27.3 | 10–35 / 14–42 | Eastern Michigan -4.8 / – | 49.8 / – | no line yet | no line yet (fair: Eastern Michigan -180) | no line yet |  |
| Tue 11/24 7:00 PM | Miami (OH) @ Western Michigan | Miami (OH) 21, Western Michigan 24 | Western Michigan 60% | Miami (OH) +150 / Western Michigan -150 | 22.3 – 25.9 | 10–35 / 13–41 | Western Michigan -3.6 / – | 48.2 / – | no line yet | no line yet (fair: Western Michigan -150) | no line yet |  |
| Thu 11/26 8:00 PM | TCU @ Texas Tech | TCU 17, Texas Tech 27 | Texas Tech 77% | TCU +340 / Texas Tech -340 | 18.0 – 29.1 | 7–31 / 14–44 | Texas Tech -16.9 / Texas Tech -10.5 | 44.9 / 47.5 | no edge | no edge | no edge |  |
| Fri 11/27 TBA | Temple @ Memphis | Temple 21, Memphis 38 | Memphis 88% | Temple +740 / Memphis -740 | 21.1 – 38.9 | 7–34 / 24–55 | Memphis -17.7 / – | 60.0 / – | no line yet | no line yet (fair: Memphis -740) | no line yet |  |
| Fri 11/27 TBA | Tulsa @ UTSA | Tulsa 28, UTSA 31 | UTSA 60% | Tulsa +150 / UTSA -150 | 26.5 – 30.5 | 13–41 / 17–45 | UTSA -4.0 / – | 57.0 / – | no line yet | no line yet (fair: UTSA -150) | no line yet |  |
| Fri 11/27 12:00 PM | Mississippi State @ Ole Miss | Mississippi State 21, Ole Miss 38 | Ole Miss 83% | Mississippi State +490 / Ole Miss -490 | 21.7 – 36.1 | 10–35 / 21–52 | Ole Miss -13.4 / Ole Miss -14.5 | 58.8 / 57.5 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Nebraska @ Iowa | Nebraska 17, Iowa 24 | Iowa 68% | Nebraska +215 / Iowa -215 | 16.6 – 22.9 | 6–28 / 10–37 | Iowa -4.4 / Iowa -6.5 | 43.9 / 38.5 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Buffalo @ Akron | Buffalo 31, Akron 24 | Buffalo 70% | Buffalo -230 / Akron +230 | 29.5 – 21.8 | 14–44 / 10–35 | Buffalo -7.6 / – | 51.3 / – | no line yet | no line yet (fair: Buffalo -230) | no line yet |  |
| Fri 11/27 12:00 PM | Toledo @ Ohio | Toledo 27, Ohio 24 | Toledo 61% | Toledo -160 / Ohio +160 | 26.8 – 22.8 | 14–41 / 10–37 | Toledo -4.0 / – | 49.7 / – | no line yet | no line yet (fair: Toledo -160) | no line yet |  |
| Fri 11/27 3:00 PM | App State @ South Alabama | App State 28, South Alabama 31 | South Alabama 51% | App State +100 / South Alabama -100 | 29.3 – 29.9 | 15–44 / 16–45 | South Alabama -0.6 / – | 59.2 / – | no line yet | no line yet (fair: South Alabama -100) | no line yet |  |
| Fri 11/27 3:30 PM | Florida @ Florida State | Florida 27, Florida State 24 | Florida 61% | Florida -155 / Florida State +155 | 28.7 – 24.4 | 14–43 / 10–38 | Florida -2.4 / Florida -4.5 | 55.5 / 52.5 | no edge | no edge | no edge |  |
| Fri 11/27 3:30 PM | North Dakota State @ San José State | North Dakota State 28, San José State 14 | North Dakota State 85% | North Dakota State -565 / San José State +565 | 28.1 – 14.0 | 14–42 / 3–25 | North Dakota State -14.1 / – | 42.1 / – | no line yet | no line yet (fair: North Dakota State -565) | no line yet |  |
| Fri 11/27 4:30 PM | Air Force @ New Mexico | Air Force 24, New Mexico 27 | New Mexico 63% | Air Force +165 / New Mexico -165 | 21.8 – 26.3 | 9–35 / 13–41 | New Mexico -4.5 / – | 48.2 / – | no line yet | no line yet (fair: New Mexico -165) | no line yet |  |
| Fri 11/27 7:30 PM | Texas @ Texas A&M | Texas 24, Texas A&M 17 | Texas 71% | Texas -245 / Texas A&M +245 | 24.4 – 16.8 | 10–38 / 6–28 | Texas -8.9 / Texas -7.5 | 40.5 / 41.5 | no edge | no edge | no edge |  |
| Fri 11/27 7:30 PM | Minnesota @ Wisconsin | Minnesota 17, Wisconsin 24 | Wisconsin 71% | Minnesota +245 / Wisconsin -245 | 15.0 – 22.4 | 3–27 / 10–35 | Wisconsin -7.4 / – | 37.4 / – | no line yet | no line yet (fair: Wisconsin -245) | no line yet |  |
| Fri 11/27 9:00 PM | West Virginia @ Utah | West Virginia 17, Utah 45 | Utah 95% | West Virginia +1840 / Utah -1840 | 19.6 – 44.4 | 7–32 / 28–60 | Utah -24.7 / – | 64.0 / – | no line yet | no line yet (fair: Utah -1840) | no line yet |  |
| Sat 11/28 TBA | Auburn @ Alabama | Auburn 17, Alabama 34 | Alabama 85% | Auburn +560 / Alabama -560 | 17.8 – 32.8 | 7–31 / 17–48 | Alabama -10.7 / Alabama -15.5 | 50.9 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | LSU @ Arkansas | LSU 34, Arkansas 17 | LSU 90% | LSU -880 / Arkansas +880 | 35.0 – 16.8 | 20–51 / 6–30 | LSU -18.2 / – | 51.7 / – | no line yet | no line yet (fair: LSU -880) | no line yet |  |
| Sat 11/28 TBA | Georgia Tech @ Georgia | Georgia Tech 7, Georgia 45 | Georgia 100% | Georgia Tech +9900 / Georgia -9900 | 6.9 – 43.2 | 0–14 / 28–60 | Georgia -36.3 / – | 50.1 / – | no line yet | no line yet (fair: Georgia -9900) | no line yet |  |
| Sat 11/28 TBA | Louisville @ Kentucky | Louisville 24, Kentucky 27 | Kentucky 52% | Louisville +110 / Kentucky -110 | 26.7 – 27.5 | 13–41 / 14–42 | Louisville -5.7 / Kentucky -1.5 | 52.8 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Oklahoma @ Missouri | Oklahoma 17, Missouri 20 | Missouri 53% | Oklahoma +110 / Missouri -110 | 20.6 – 21.8 | 9–34 / 10–35 | Oklahoma -1.8 / Missouri -1.5 | 42.4 / 42.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | South Carolina @ Clemson | South Carolina 24, Clemson 27 | Clemson 57% | South Carolina +130 / Clemson -130 | 24.9 – 27.4 | 10–38 / 14–42 | South Carolina -2.6 / Clemson -3.0 | 47.1 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Tennessee @ Vanderbilt | Tennessee 27, Vanderbilt 24 | Tennessee 61% | Tennessee -155 / Vanderbilt +155 | 29.8 – 25.8 | 16–45 / 13–41 | Tennessee -13.0 / Tennessee -3.0 | 46.7 / 57.5 | no edge | no edge | Under 57.5 (-110*): EV +3.3%, 54%, stake 0.9u | * price not posted; assumed -110 |
| Sat 11/28 TBA | Arizona State @ Arizona | Arizona State 24, Arizona 27 | Arizona 63% | Arizona State +165 / Arizona -165 | 24.0 – 28.7 | 10–38 / 14–44 | Arizona -6.2 / Arizona -4.5 | 53.8 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Baylor @ Houston | Baylor 28, Houston 31 | Houston 51% | Baylor +105 / Houston -105 | 28.2 – 28.9 | 14–42 / 14–44 | Houston -0.7 / – | 58.0 / – | no line yet | no line yet (fair: Houston -105) | no line yet |  |
| Sat 11/28 TBA | UCF @ Colorado | UCF 24, Colorado 27 | Colorado 59% | UCF +140 / Colorado -140 | 23.9 – 27.2 | 10–38 / 14–41 | Colorado -3.2 / – | 51.1 / – | no line yet | no line yet (fair: Colorado -140) | no line yet |  |
| Sat 11/28 TBA | Cincinnati @ BYU | Cincinnati 24, BYU 34 | BYU 76% | Cincinnati +315 / BYU -315 | 23.8 – 34.2 | 10–38 / 20–49 | BYU -10.4 / – | 58.0 / – | no line yet | no line yet (fair: BYU -315) | no line yet |  |
| Sat 11/28 TBA | Kansas @ Oklahoma State | Kansas 28, Oklahoma State 31 | Oklahoma State 56% | Kansas +125 / Oklahoma State -125 | 29.0 – 31.0 | 14–44 / 17–45 | Oklahoma State -2.0 / – | 60.0 / – | no line yet | no line yet (fair: Oklahoma State -125) | no line yet |  |
| Sat 11/28 TBA | Kansas State @ Iowa State | Kansas State 24, Iowa State 27 | Iowa State 62% | Kansas State +160 / Iowa State -160 | 24.7 – 28.9 | 12–38 / 14–44 | Iowa State -4.2 / – | 53.6 / – | no line yet | no line yet (fair: Iowa State -160) | no line yet |  |
| Sat 11/28 TBA | Boston College @ Miami | Boston College 10, Miami 45 | Miami 99% | Boston College +9900 / Miami -9900 | 9.9 – 43.8 | 0–20 / 28–60 | Miami -33.9 / – | 55.4 / – | no line yet | no line yet (fair: Miami -9900) | no line yet |  |
| Sat 11/28 TBA | Duke @ Wake Forest | Duke 24, Wake Forest 31 | Wake Forest 76% | Duke +325 / Wake Forest -325 | 20.9 – 31.7 | 7–34 / 17–47 | Wake Forest -13.8 / Wake Forest -10.5 | 52.5 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | NC State @ North Carolina | NC State 31, North Carolina 28 | NC State 52% | NC State -110 / North Carolina +110 | 28.3 – 27.5 | 14–43 / 14–42 | North Carolina -5.8 / NC State -1.5 | 57.3 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Notre Dame @ Syracuse | Notre Dame 38, Syracuse 17 | Notre Dame 92% | Notre Dame -1210 / Syracuse +1210 | 37.2 – 16.8 | 22–52 / 6–29 | Notre Dame -20.1 / Notre Dame -20.5 | 51.6 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Pittsburgh @ California | Pittsburgh 31, California 21 | Pittsburgh 74% | Pittsburgh -280 / California +280 | 29.7 – 20.5 | 16–45 / 7–34 | Pittsburgh -9.2 / – | 50.2 / – | no line yet | no line yet (fair: Pittsburgh -280) | no line yet |  |
| Sat 11/28 TBA | SMU @ Stanford | SMU 34, Stanford 20 | SMU 81% | SMU -435 / Stanford +435 | 35.3 – 21.5 | 20–51 / 9–35 | SMU -13.8 / – | 56.7 / – | no line yet | no line yet (fair: SMU -435) | no line yet |  |
| Sat 11/28 TBA | Virginia @ Virginia Tech | Virginia 24, Virginia Tech 27 | Virginia Tech 54% | Virginia +115 / Virginia Tech -115 | 25.8 – 27.2 | 13–40 / 13–42 | Virginia Tech -1.0 / Virginia Tech -1.5 | 50.7 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Illinois @ Northwestern | Illinois 27, Northwestern 24 | Illinois 57% | Illinois -135 / Northwestern +135 | 27.9 – 25.2 | 14–42 / 13–39 | Northwestern -5.7 / Illinois -3.5 | 56.2 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Purdue @ Indiana | Purdue 10, Indiana 38 | Indiana 96% | Purdue +2580 / Indiana -2580 | 12.1 – 36.8 | 3–23 / 21–53 | Indiana -24.7 / – | 48.9 / – | no line yet | no line yet (fair: Indiana -2580) | no line yet |  |
| Sat 11/28 TBA | Penn State @ Maryland | Penn State 28, Maryland 21 | Penn State 69% | Penn State -225 / Maryland +225 | 26.8 – 19.9 | 14–41 / 7–33 | Penn State -6.9 / – | 46.6 / – | no line yet | no line yet (fair: Penn State -225) | no line yet |  |
| Sat 11/28 TBA | Washington @ Oregon | Washington 17, Oregon 31 | Oregon 80% | Washington +410 / Oregon -410 | 18.0 – 30.5 | 7–31 / 16–45 | Oregon -12.9 / Oregon -12.5 | 48.5 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Michigan State @ Rutgers | Michigan State 27, Rutgers 24 | Michigan State 55% | Michigan State -120 / Rutgers +120 | 26.7 – 24.5 | 13–41 / 10–38 | Michigan State -2.2 / – | 51.2 / – | no line yet | no line yet (fair: Michigan State -120) | no line yet |  |
| Sat 11/28 TBA | USC @ UCLA | USC 24, UCLA 27 | UCLA 58% | USC +140 / UCLA -140 | 24.6 – 28.0 | 10–38 / 14–42 | UCLA -7.4 / UCLA -3.0 | 52.8 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | UConn @ Wyoming | UConn 27, Wyoming 24 | UConn 61% | UConn -160 / Wyoming +160 | 29.6 – 25.2 | 16–45 / 13–39 | UConn -4.4 / – | 54.8 / – | no line yet | no line yet (fair: UConn -160) | no line yet |  |
| Sat 11/28 TBA | Florida Atlantic @ East Carolina | Florida Atlantic 28, East Carolina 31 | East Carolina 55% | Florida Atlantic +120 / East Carolina -120 | 28.2 – 30.4 | 14–43 / 17–45 | East Carolina -2.2 / – | 58.7 / – | no line yet | no line yet (fair: East Carolina -120) | no line yet |  |
| Sat 11/28 TBA | Tulane @ South Florida | Tulane 24, South Florida 31 | South Florida 69% | Tulane +220 / South Florida -220 | 21.9 – 29.3 | 10–35 / 15–44 | South Florida -7.4 / – | 51.5 / – | no line yet | no line yet (fair: South Florida -220) | no line yet |  |
| Sat 11/28 TBA | Army @ Rice | Army 31, Rice 24 | Army 71% | Army -240 / Rice +240 | 32.0 – 23.7 | 17–47 / 10–37 | Army -8.3 / – | 56.6 / – | no line yet | no line yet (fair: Army -240) | no line yet |  |
| Sat 11/28 TBA | Navy @ Charlotte | Navy 34, Charlotte 17 | Navy 88% | Navy -770 / Charlotte +770 | 34.8 – 17.7 | 20–51 / 6–30 | Navy -17.1 / – | 52.5 / – | no line yet | no line yet (fair: Navy -770) | no line yet |  |
| Sat 11/28 TBA | UAB @ North Texas | UAB 24, North Texas 34 | North Texas 77% | UAB +325 / North Texas -325 | 23.6 – 34.9 | 10–38 / 20–50 | North Texas -11.3 / – | 58.4 / – | no line yet | no line yet (fair: North Texas -325) | no line yet |  |
| Sat 11/28 TBA | UTEP @ Northern Illinois | UTEP 21, Northern Illinois 28 | Northern Illinois 69% | UTEP +220 / Northern Illinois -220 | 21.3 – 28.8 | 9–35 / 14–43 | Northern Illinois -7.4 / – | 50.1 / – | no line yet | no line yet (fair: Northern Illinois -220) | no line yet |  |
| Sat 11/28 TBA | Coastal Carolina @ James Madison | Coastal Carolina 17, James Madison 34 | James Madison 86% | Coastal Carolina +630 / James Madison -630 | 17.9 – 33.6 | 7–31 / 20–49 | James Madison -15.7 / – | 51.5 / – | no line yet | no line yet (fair: James Madison -630) | no line yet |  |
| Sat 11/28 TBA | Louisiana Tech @ Georgia Southern | Louisiana Tech 27, Georgia Southern 24 | Louisiana Tech 52% | Louisiana Tech -110 / Georgia Southern +110 | 25.9 – 24.7 | 13–40 / 12–38 | Louisiana Tech -1.2 / – | 50.7 / – | no line yet | no line yet (fair: Louisiana Tech -110) | no line yet |  |
| Sat 11/28 TBA | Louisiana @ Georgia State | Louisiana 31, Georgia State 28 | Louisiana 51% | Louisiana -105 / Georgia State +105 | 28.1 – 27.4 | 14–42 / 14–42 | Louisiana -0.7 / – | 55.5 / – | no line yet | no line yet (fair: Louisiana -105) | no line yet |  |
| Sat 11/28 TBA | Marshall @ UL Monroe | Marshall 31, UL Monroe 24 | Marshall 67% | Marshall -200 / UL Monroe +200 | 30.6 – 24.0 | 17–45 / 10–38 | Marshall -6.6 / – | 54.6 / – | no line yet | no line yet (fair: Marshall -200) | no line yet |  |
| Sat 11/28 TBA | Southern Miss @ Old Dominion | Southern Miss 17, Old Dominion 24 | Old Dominion 69% | Southern Miss +225 / Old Dominion -225 | 19.1 – 26.3 | 7–31 / 13–41 | Old Dominion -7.2 / – | 45.4 / – | no line yet | no line yet (fair: Old Dominion -225) | no line yet |  |
| Sat 11/28 12:00 PM | Michigan @ Ohio State | Michigan 14, Ohio State 27 | Ohio State 82% | Michigan +450 / Ohio State -450 | 14.7 – 27.4 | 3–27 / 14–42 | Ohio State -14.5 / Ohio State -12.5 | 45.3 / 41.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Central Michigan @ Ball State | Central Michigan 28, Ball State 21 | Central Michigan 65% | Central Michigan -190 / Ball State +190 | 28.0 – 22.1 | 14–42 / 10–35 | Central Michigan -5.9 / – | 50.0 / – | no line yet | no line yet (fair: Central Michigan -190) | no line yet |  |
| Sat 11/28 12:00 PM | Massachusetts @ Bowling Green | Massachusetts 17, Bowling Green 20 | Bowling Green 60% | Massachusetts +145 / Bowling Green -145 | 18.4 – 21.6 | 7–31 / 10–35 | Bowling Green -3.2 / – | 40.9 / – | no line yet | no line yet (fair: Bowling Green -145) | no line yet |  |
| Sat 11/28 1:00 PM | Kennesaw State @ Western Kentucky | Kennesaw State 24, Western Kentucky 27 | Western Kentucky 58% | Kennesaw State +135 / Western Kentucky -135 | 25.3 – 27.9 | 13–38 / 14–42 | Western Kentucky -2.5 / – | 53.2 / – | no line yet | no line yet (fair: Western Kentucky -135) | no line yet |  |
| Sat 11/28 2:00 PM | Liberty @ Missouri State | Liberty 34, Missouri State 17 | Liberty 85% | Liberty -550 / Missouri State +550 | 34.0 – 19.1 | 20–49 / 7–31 | Liberty -14.9 / – | 53.0 / – | no line yet | no line yet (fair: Liberty -550) | no line yet |  |
| Sat 11/28 2:00 PM | Sam Houston @ Florida International | Sam Houston 14, Florida International 21 | Florida International 72% | Sam Houston +265 / Florida International -265 | 14.3 – 22.5 | 3–26 / 10–36 | Florida International -8.2 / – | 39.0 / – | no line yet | no line yet (fair: Florida International -265) | no line yet |  |
| Sat 11/28 2:00 PM | New Mexico State @ Middle Tennessee | New Mexico State 24, Middle Tennessee 27 | Middle Tennessee 62% | New Mexico State +160 / Middle Tennessee -160 | 22.6 – 27.0 | 10–36 / 13–41 | Middle Tennessee -4.4 / – | 49.7 / – | no line yet | no line yet (fair: Middle Tennessee -160) | no line yet |  |
| Sat 11/28 3:00 PM | Troy @ Arkansas State | Troy 21, Arkansas State 24 | Arkansas State 61% | Troy +160 / Arkansas State -160 | 22.1 – 26.2 | 10–35 / 13–41 | Arkansas State -4.1 / – | 48.3 / – | no line yet | no line yet (fair: Arkansas State -160) | no line yet |  |
| Sat 11/28 3:30 PM | Jacksonville State @ Delaware | Jacksonville State 28, Delaware 31 | Delaware 55% | Jacksonville State +120 / Delaware -120 | 27.7 – 29.5 | 14–42 / 15–44 | Delaware -1.8 / – | 57.2 / – | no line yet | no line yet (fair: Delaware -120) | no line yet |  |
| Sat 11/28 9:00 PM | Nevada @ UNLV | Nevada 17, UNLV 27 | UNLV 78% | Nevada +350 / UNLV -350 | 17.9 – 29.1 | 7–31 / 14–44 | UNLV -11.2 / – | 47.1 / – | no line yet | no line yet (fair: UNLV -350) | no line yet |  |
| Sat 11/28 11:00 PM | Sacramento State @ Hawai'i | Sacramento State 17, Hawai'i 31 | Hawai'i 84% | Sacramento State +530 / Hawai'i -530 | 17.2 – 31.5 | 6–30 / 17–46 | Hawai'i -14.3 / – | 48.6 / – | no line yet | no line yet (fair: Hawai'i -530) | no line yet |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 752 | 11.90 | 12.28 | 8.55 | 78.2% | 0.149 | 81.4% |
| Model only (before blending) | 752 | 12.58 | 12.69 | 8.82 | 76.2% | – | – |
| Betting line when predicted | 750 | 11.89 | 12.22 | 8.54 | 78.3% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin of an FBS game by about 12.5 points.

501 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 11 | 2-9-0 | 3.5 | +0.18 | +5.2% | +4.7% |
| Total | 8 | 3-5-0 | 11.9 | -2.62 | -22.1% | +7.5% |

8 of these edges were priced at an assumed -110 (price not posted).

Every edge logged before kickoff at the stake and price logged with it (backfilled games, and edges logged before edges were priced from the final prediction, are not included). Units are 1% of the bankroll; ROI is units won per unit staked, pushes returning the stake, and expected ROI is what the edges' EVs promised.

### Week 11 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| Western Michigan @ Akron | 34–17 | 42–14 | 85% | yes |
| Kent State @ Bowling Green | 17–24 | 28–33 | 63% | yes |
| Ohio @ Miami (OH) | 24–21 | 17–34 | 47% | yes |
| Buffalo @ Ball State | 27–24 | 28–7 | 56% | no |
| Sacramento State @ Central Michigan | 14–31 | 7–28 | 90% | yes |
| Massachusetts @ Toledo | 17–31 | 0–24 | 85% | no |
| Memphis @ South Florida | 27–24 | 52–41 | 61% | no |
| Louisiana @ UL Monroe | 31–21 | 42–21 | 75% | yes |
| Florida State @ Pittsburgh | 24–27 | 16–10 | 40% | no |
| Illinois @ UCLA | 17–27 | 14–22 | 77% | yes |
| Houston @ Colorado | 31–24 | 32–42 | 30% | no |
| Cincinnati @ Iowa State | 28–31 | 13–41 | 57% | no |
| Auburn @ Mississippi State | 27–24 | 41–9 | 56% | no |
| Duke @ Miami | 20–34 | 25–36 | 82% | yes |
| Syracuse @ NC State | 31–28 | 34–31 | 57% | yes |
| Wake Forest @ SMU | 28–31 | 49–7 | 48% | no |
| Wisconsin @ Maryland | 24–17 | 21–24 | 28% | yes |
| Northwestern @ Ohio State | 17–31 | 19–28 | 84% | yes |
| James Madison @ UConn | 31–24 | 22–46 | 39% | no |
| Georgia Tech @ Clemson | 17–31 | 20–6 | 14% | no |
| Nebraska @ Rutgers | 34–17 | 31–0 | 85% | no |
| Alabama @ Vanderbilt | 31–17 | 21–6 | 84% | yes |
| East Carolina @ Charlotte | 27–17 | 17–16 | 79% | yes |
| UAB @ Temple | 21–24 | 36–10 | 44% | no |
| Arkansas State @ Coastal Carolina | 24–27 | 21–28 | 55% | yes |
| Kansas State @ TCU | 17–31 | 10–20 | 81% | yes |
| Tulane @ Rice | 21–24 | 20–17 | 43% | yes |
| Kennesaw State @ Sam Houston | 24–17 | 26–7 | 73% | yes |
| Tennessee @ Texas A&M | 24–21 | 22–7 | 56% | no |
| New Mexico State @ Missouri State | 24–27 | 21–27 | 55% | yes |
| Florida International @ Delaware | 24–27 | 16–24 | 62% | yes |
| Arizona State @ UCF | 21–24 | 26–13 | 40% | yes |
| Missouri @ Georgia | 14–31 | 21–48 | 87% | yes |
| Boston College @ Notre Dame | 10–38 | 7–41 | 98% | yes |
| California @ Virginia | 17–31 | 7–36 | 78% | yes |
| USC @ Indiana | 21–31 | 13–27 | 74% | yes |
| Michigan @ Oregon | 17–24 | 7–31 | 77% | yes |
| Nevada @ Northern Illinois | 28–21 | 28–7 | 68% | no |
| Georgia Southern @ Georgia State | 31–24 | 34–17 | 62% | yes |
| Jacksonville State @ Western Kentucky | 31–24 | 24–34 | 31% | yes |
| Middle Tennessee @ Liberty | 17–38 | 23–28 | 93% | yes |
| Fresno State @ Texas State | 27–34 | 35–37 | 75% | yes |
| Washington @ Michigan State | 24–21 | 21–14 | 59% | yes |
| Southern Miss @ Louisiana Tech | 17–34 | 31–63 | 88% | no |
| Kansas @ West Virginia | 31–34 | 37–14 | 46% | no |
| Oregon State @ Boise State | 24–41 | 41–46 | 85% | no |
| App State @ Marshall | 24–27 | 20–16 | 47% | yes |
| Florida @ Kentucky | 24–27 | 21–14 | 42% | yes |
| Baylor @ BYU | 21–28 | 7–28 | 71% | no |
| Louisville @ North Carolina | 31–28 | 16–14 | 61% | no |
| Minnesota @ Penn State | 14–28 | 14–42 | 81% | yes |
| San José State @ Air Force | 17–31 | 3–24 | 83% | no |
| Troy @ South Alabama | 24–27 | 14–27 | 59% | yes |
| Florida Atlantic @ Tulsa | 31–38 | 21–38 | 66% | yes |
| Texas @ LSU | 21–24 | 22–21 | 38% | yes |
| Stanford @ Virginia Tech | 21–38 | 40–22 | 12% | no |
| Purdue @ Iowa | 14–31 | 7–28 | 90% | yes |
| UNLV @ New Mexico | 14–31 | 21–17 | 12% | yes |
| South Carolina @ Arkansas | 31–24 | 6–34 | 30% | no |
| North Texas @ UTSA | 38–35 | 16–35 | 44% | no |
| Texas Tech @ Oklahoma State | 34–37 | 52–27 | 42% | no |
| Utah State @ San Diego State | 24–21 | 13–30 | 42% | yes |
| Wyoming @ UTEP | 24–17 | 27–15 | 72% | yes |
| Utah @ Arizona | 31–28 | 40–39 | 56% | yes |
| Colorado State @ Washington State | 27–34 | 7–73 | 70% | no |
| North Dakota State @ Hawai'i | 24–17 | 21–13 | 70% | yes |
| Ole Miss @ Oklahoma | 24–27 | 17–24 | 57% | yes |

## FBS power ratings

Points per game better than an average FBS team on a neutral field, from opponent-adjusted EPA (garbage time removed) with this season's games weighted against a preseason prior, plus the weight the margin model puts on Elo (a rating built from game results alone). Defense is positive when it holds opponents below average.

| # | Team | Conference | Net | Offense | Defense | Special teams | Results (Elo) | Elo rating |
|---|---|---|---|---|---|---|---|---|
| 1 | Georgia | SEC | +27.7 | +9.4 | +12.2 | +0.9 | +5.3 | 1944 |
| 2 | Notre Dame | FBS Independents | +24.7 | +9.2 | +9.8 | +1.1 | +4.7 | 1892 |
| 3 | LSU | SEC | +23.6 | +9.7 | +11.8 | -0.2 | +2.3 | 1696 |
| 4 | Ohio State | Big Ten | +23.3 | +10.1 | +9.3 | +0.2 | +3.8 | 1817 |
| 5 | Miami | ACC | +23.3 | +15.0 | +3.4 | +0.3 | +4.5 | 1881 |
| 6 | Alabama | SEC | +22.0 | +8.4 | +9.3 | +0.3 | +4.0 | 1841 |
| 7 | Indiana | Big Ten | +21.6 | +5.6 | +10.3 | +0.3 | +5.4 | 1953 |
| 8 | Utah | Big 12 | +21.6 | +11.4 | +5.7 | +0.1 | +4.4 | 1869 |
| 9 | Wake Forest | ACC | +20.5 | +7.7 | +8.9 | +0.7 | +3.3 | 1776 |
| 10 | Oregon | Big Ten | +20.5 | +6.7 | +9.8 | +0.2 | +3.8 | 1823 |
| 11 | Texas | SEC | +20.2 | +2.4 | +12.6 | +1.1 | +4.2 | 1856 |
| 12 | Tennessee | SEC | +19.0 | +4.3 | +10.1 | +1.4 | +3.3 | 1784 |
| 13 | Texas Tech | Big 12 | +18.7 | +2.7 | +11.0 | +1.6 | +3.5 | 1793 |
| 14 | UCLA | Big Ten | +17.8 | +4.9 | +9.6 | +0.7 | +2.7 | 1729 |
| 15 | Oklahoma | SEC | +16.7 | +1.3 | +12.4 | +0.7 | +2.3 | 1696 |
| 16 | Louisville | ACC | +16.6 | +9.2 | +4.3 | +0.7 | +2.5 | 1711 |
| 17 | Ole Miss | SEC | +16.5 | +10.0 | +3.1 | +0.7 | +2.7 | 1727 |
| 18 | Iowa | Big Ten | +15.0 | +1.9 | +8.9 | +0.9 | +3.4 | 1789 |
| 19 | Auburn | SEC | +13.5 | +5.3 | +6.6 | +0.5 | +1.1 | 1601 |
| 20 | USC | Big Ten | +13.5 | +10.5 | +0.3 | +0.1 | +2.6 | 1724 |
| 21 | Nebraska | Big Ten | +13.5 | +4.0 | +8.1 | +0.4 | +1.0 | 1589 |
| 22 | Missouri | SEC | +12.9 | +3.8 | +6.9 | +0.3 | +1.9 | 1667 |
| 23 | Penn State | Big Ten | +12.9 | +4.2 | +6.6 | +0.2 | +1.9 | 1666 |
| 24 | BYU | Big 12 | +12.5 | +4.3 | +4.2 | +0.9 | +3.1 | 1764 |
| 25 | Michigan | Big Ten | +11.5 | +1.9 | +8.7 | -0.0 | +0.9 | 1586 |
| 26 | Florida | SEC | +11.3 | +5.8 | +4.0 | +0.6 | +0.9 | 1582 |
| 27 | Arizona | Big 12 | +11.1 | +6.4 | +2.3 | -0.1 | +2.4 | 1706 |
| 28 | Baylor | Big 12 | +10.6 | +1.5 | +7.1 | +0.8 | +1.2 | 1604 |
| 29 | SMU | ACC | +10.5 | +6.8 | +1.9 | +0.2 | +1.6 | 1637 |
| 30 | South Carolina | SEC | +10.1 | +4.6 | +4.0 | +0.4 | +1.1 | 1602 |
| 31 | Washington | Big Ten | +10.0 | +3.1 | +4.8 | +0.2 | +1.8 | 1660 |
| 32 | Texas A&M | SEC | +9.8 | +1.0 | +8.0 | +0.3 | +0.6 | 1554 |
| 33 | Northwestern | Big Ten | +9.5 | +5.9 | +2.0 | +0.6 | +1.0 | 1591 |
| 34 | Houston | Big 12 | +9.4 | +9.0 | -1.2 | +0.3 | +1.4 | 1621 |
| 35 | Duke | ACC | +9.0 | +4.6 | +1.2 | +0.8 | +2.3 | 1700 |
| 36 | Kansas | Big 12 | +8.9 | +5.3 | +3.9 | -0.1 | -0.2 | 1495 |
| 37 | Oklahoma State | Big 12 | +8.3 | +8.2 | -0.3 | +0.1 | +0.3 | 1530 |
| 38 | Iowa State | Big 12 | +7.6 | +4.8 | +1.0 | +0.9 | +0.9 | 1581 |
| 39 | Kentucky | SEC | +7.5 | +2.5 | +3.7 | +0.3 | +1.0 | 1594 |
| 40 | Wisconsin | Big Ten | +7.2 | -1.5 | +7.1 | +0.8 | +0.8 | 1575 |
| 41 | Arizona State | Big 12 | +7.1 | +1.7 | +4.1 | +0.1 | +1.1 | 1599 |
| 42 | Kansas State | Big 12 | +6.5 | +4.7 | +2.4 | +0.3 | -0.9 | 1436 |
| 43 | Boise State | Pac-12 | +6.5 | +7.4 | -3.6 | -0.1 | +2.8 | 1735 |
| 44 | Illinois | Big Ten | +6.4 | +6.2 | -1.5 | +0.4 | +1.3 | 1617 |
| 45 | Florida State | ACC | +6.2 | +6.6 | -0.2 | -0.5 | +0.4 | 1540 |
| 46 | Mississippi State | SEC | +6.2 | +3.1 | +3.9 | -0.0 | -0.8 | 1442 |
| 47 | TCU | Big 12 | +5.8 | -1.8 | +6.4 | +0.1 | +1.1 | 1599 |
| 48 | Cincinnati | Big 12 | +5.0 | +9.1 | -4.3 | +0.3 | -0.0 | 1507 |
| 49 | Vanderbilt | SEC | +4.5 | +2.2 | +1.5 | +0.5 | +0.3 | 1531 |
| 50 | Colorado | Big 12 | +4.0 | +1.5 | +4.0 | -0.6 | -0.9 | 1432 |
| 51 | North Carolina | ACC | +3.6 | +3.2 | -0.3 | +0.3 | +0.4 | 1542 |
| 52 | Maryland | Big Ten | +3.3 | +0.1 | +4.0 | +0.5 | -1.2 | 1408 |
| 53 | Arkansas | SEC | +3.3 | +1.5 | +1.8 | -0.4 | +0.3 | 1536 |
| 54 | Clemson | ACC | +3.1 | -6.4 | +8.0 | +1.0 | +0.5 | 1547 |
| 55 | Memphis | American Athletic | +3.1 | +5.0 | -3.2 | -0.5 | +1.7 | 1652 |
| 56 | Pittsburgh | ACC | +2.9 | -2.5 | +4.8 | +0.5 | +0.2 | 1525 |
| 57 | Virginia | ACC | +2.7 | -1.2 | +3.9 | -0.1 | +0.1 | 1519 |
| 58 | UCF | Big 12 | +2.6 | +1.7 | +1.8 | -0.1 | -0.9 | 1436 |
| 59 | Syracuse | ACC | +2.5 | +1.7 | +2.5 | -0.7 | -1.0 | 1424 |
| 60 | Minnesota | Big Ten | +2.1 | -3.6 | +5.0 | +0.8 | -0.1 | 1502 |
| 61 | UTSA | American Athletic | +2.0 | +2.4 | -2.0 | -0.1 | +1.6 | 1642 |
| 62 | North Texas | American Athletic | +1.9 | +8.4 | -6.9 | -0.8 | +1.2 | 1605 |
| 63 | Texas State | Pac-12 | +1.9 | +7.3 | -5.5 | -1.2 | +1.3 | 1613 |
| 64 | Virginia Tech | ACC | +1.4 | +2.8 | -0.7 | -0.2 | -0.4 | 1475 |
| 65 | James Madison | Sun Belt | +1.0 | -0.6 | -0.0 | +0.2 | +1.4 | 1625 |
| 66 | Tulsa | American Athletic | +0.9 | -0.3 | +1.9 | -0.6 | -0.0 | 1508 |
| 67 | NC State | ACC | +0.9 | +5.1 | -3.3 | -0.4 | -0.5 | 1467 |
| 68 | Liberty | Conference USA | +0.4 | +1.3 | -1.8 | +0.1 | +0.8 | 1574 |
| 69 | Toledo | Mid-American | +0.3 | -2.2 | +2.3 | -0.4 | +0.7 | 1567 |
| 70 | Oregon State | Pac-12 | -0.0 | +4.9 | -3.8 | -0.1 | -1.0 | 1423 |
| 71 | Louisiana Tech | Sun Belt | -0.3 | -2.4 | +1.9 | -0.8 | +1.0 | 1588 |
| 72 | North Dakota State | Mountain West | -0.8 | -5.6 | +4.6 | +0.9 | -0.7 | 1453 |
| 73 | West Virginia | Big 12 | -0.9 | +5.1 | -5.4 | +0.3 | -1.0 | 1429 |
| 74 | UConn | FBS Independents | -0.9 | +3.1 | -4.1 | +0.1 | +0.0 | 1512 |
| 75 | Navy | American Athletic | -1.0 | +4.0 | -4.1 | -0.6 | -0.3 | 1484 |
| 76 | Purdue | Big Ten | -1.2 | +2.9 | -3.4 | +0.8 | -1.6 | 1381 |
| 77 | New Mexico | Mountain West | -1.5 | -4.6 | +2.2 | -0.2 | +1.1 | 1596 |
| 78 | Michigan State | Big Ten | -2.1 | -3.1 | +1.3 | +0.5 | -0.8 | 1440 |
| 79 | South Florida | American Athletic | -2.4 | -1.2 | -1.6 | +0.1 | +0.3 | 1531 |
| 80 | East Carolina | American Athletic | -3.4 | -6.6 | +3.8 | -0.7 | +0.2 | 1524 |
| 81 | Georgia Tech | ACC | -3.4 | +0.8 | -3.2 | -0.4 | -0.7 | 1455 |
| 82 | Fresno State | Pac-12 | -3.6 | -1.8 | -1.8 | -0.2 | +0.1 | 1520 |
| 83 | Army | American Athletic | -3.7 | +4.6 | -8.5 | -0.1 | +0.2 | 1525 |
| 84 | Air Force | Mountain West | -3.9 | +2.0 | -6.3 | +0.1 | +0.3 | 1533 |
| 85 | Georgia Southern | Sun Belt | -4.1 | -1.1 | -3.5 | -0.5 | +0.9 | 1586 |
| 86 | Florida Atlantic | American Athletic | -4.6 | +2.8 | -7.5 | +0.7 | -0.5 | 1464 |
| 87 | UNLV | Mountain West | -4.7 | -2.0 | -3.2 | +0.2 | +0.3 | 1536 |
| 88 | San Diego State | Pac-12 | -5.3 | -3.9 | -0.9 | +0.3 | -0.7 | 1449 |
| 89 | Western Michigan | Mid-American | -5.4 | -3.4 | -3.4 | +0.6 | +0.8 | 1574 |
| 90 | Stanford | ACC | -5.6 | -2.0 | -3.9 | +0.2 | +0.1 | 1513 |
| 91 | Washington State | Pac-12 | -6.3 | -4.6 | +0.1 | -0.3 | -1.5 | 1389 |
| 92 | Jacksonville State | Conference USA | -6.4 | -1.4 | -4.5 | +0.2 | -0.7 | 1451 |
| 93 | Ohio | Mid-American | -6.5 | -3.7 | -3.1 | +0.1 | +0.2 | 1525 |
| 94 | Rutgers | Big Ten | -6.8 | +1.5 | -6.9 | +0.6 | -2.0 | 1342 |
| 95 | Delaware | Conference USA | -6.8 | +0.7 | -6.5 | +0.1 | -1.1 | 1414 |
| 96 | Miami (OH) | Mid-American | -6.9 | -4.6 | -2.8 | +0.9 | -0.3 | 1482 |
| 97 | Boston College | ACC | -7.2 | -4.1 | -1.5 | -0.6 | -1.0 | 1427 |
| 98 | Tulane | American Athletic | -7.4 | -4.2 | -2.9 | +0.2 | -0.5 | 1465 |
| 99 | California | ACC | -7.4 | -2.7 | -2.0 | -0.7 | -2.0 | 1344 |
| 100 | UAB | American Athletic | -7.7 | -6.4 | -0.5 | -0.1 | -0.7 | 1455 |
| 101 | Louisiana | Sun Belt | -8.5 | -3.5 | -5.0 | -0.0 | -0.0 | 1505 |
| 102 | Utah State | Pac-12 | -8.9 | -8.7 | +2.2 | -1.2 | -1.2 | 1412 |
| 103 | Wyoming | Mountain West | -8.9 | -4.9 | -3.3 | -0.3 | -0.5 | 1470 |
| 104 | App State | Sun Belt | -9.1 | -3.5 | -3.5 | -0.7 | -1.4 | 1397 |
| 105 | Marshall | Sun Belt | -10.8 | -5.6 | -4.3 | +0.1 | -1.1 | 1420 |
| 106 | Hawai'i | Mountain West | -10.9 | -4.7 | -5.4 | +1.2 | -2.0 | 1341 |
| 107 | Western Kentucky | Conference USA | -11.0 | -5.2 | -3.6 | -0.5 | -1.8 | 1360 |
| 108 | Kennesaw State | Conference USA | -11.1 | -6.1 | -3.0 | -0.5 | -1.5 | 1386 |
| 109 | Georgia State | Sun Belt | -11.3 | -1.5 | -7.9 | -0.3 | -1.6 | 1377 |
| 110 | Central Michigan | Mid-American | -11.5 | -5.9 | -4.7 | +0.0 | -1.0 | 1429 |
| 111 | South Alabama | Sun Belt | -11.8 | +0.0 | -10.9 | +0.2 | -1.1 | 1419 |
| 112 | Arkansas State | Sun Belt | -12.2 | -3.7 | -7.0 | +0.1 | -1.6 | 1374 |
| 113 | Old Dominion | Sun Belt | -12.3 | -13.1 | +3.8 | -1.7 | -1.2 | 1407 |
| 114 | Temple | American Athletic | -12.3 | -0.9 | -7.7 | -0.5 | -3.2 | 1244 |
| 115 | Coastal Carolina | Sun Belt | -12.4 | -7.1 | -3.8 | +0.3 | -1.7 | 1368 |
| 116 | Troy | Sun Belt | -12.5 | -8.5 | -0.6 | -1.3 | -2.1 | 1336 |
| 117 | Colorado State | Pac-12 | -13.4 | +4.7 | -14.6 | -0.2 | -3.3 | 1238 |
| 118 | Rice | American Athletic | -13.5 | -3.3 | -6.0 | -0.9 | -3.4 | 1229 |
| 119 | Nevada | Mountain West | -13.9 | -10.8 | -1.5 | +0.5 | -2.1 | 1337 |
| 120 | Florida International | Conference USA | -14.3 | -9.3 | -1.5 | -1.5 | -2.0 | 1341 |
| 121 | Buffalo | Mid-American | -14.9 | -10.6 | -4.5 | +0.3 | -0.2 | 1491 |
| 122 | Missouri State | Conference USA | -15.6 | -4.5 | -7.3 | -1.2 | -2.6 | 1292 |
| 123 | New Mexico State | Conference USA | -15.9 | -7.8 | -2.9 | -1.9 | -3.3 | 1235 |
| 124 | Middle Tennessee | Conference USA | -16.0 | -5.2 | -8.4 | +0.3 | -2.7 | 1290 |
| 125 | San José State | Mountain West | -16.1 | -10.0 | -3.4 | -0.3 | -2.5 | 1302 |
| 126 | Southern Miss | Sun Belt | -17.6 | -9.2 | -4.7 | -1.2 | -2.5 | 1305 |
| 127 | Bowling Green | Mid-American | -17.7 | -10.9 | -4.2 | +0.1 | -2.7 | 1290 |
| 128 | UL Monroe | Sun Belt | -18.2 | -5.3 | -7.5 | -1.5 | -3.9 | 1184 |
| 129 | Massachusetts | Mid-American | -18.4 | -10.1 | -4.6 | -0.2 | -3.5 | 1221 |
| 130 | Ball State | Mid-American | -19.1 | -6.7 | -8.2 | -0.7 | -3.5 | 1218 |
| 131 | Eastern Michigan | Mid-American | -19.3 | -7.7 | -8.2 | -0.7 | -2.7 | 1287 |
| 132 | Northern Illinois | Mountain West | -19.6 | -4.5 | -8.9 | -1.3 | -4.9 | 1101 |
| 133 | Sacramento State | Mid-American | -20.2 | -11.2 | -4.7 | +0.1 | -4.5 | 1136 |
| 134 | Sam Houston | Conference USA | -20.3 | -13.2 | -1.0 | -1.3 | -4.8 | 1114 |
| 135 | Charlotte | American Athletic | -20.5 | -9.2 | -6.8 | -0.5 | -3.9 | 1187 |
| 136 | Kent State | Mid-American | -21.5 | -10.3 | -6.8 | -0.9 | -3.5 | 1221 |
| 137 | Akron | Mid-American | -23.9 | -10.1 | -9.2 | -0.7 | -3.9 | 1185 |
| 138 | UTEP | Mountain West | -24.7 | -11.2 | -7.3 | -1.2 | -5.0 | 1093 |

## Current model fit

- Fitted on 4369 games from seasons 2022–2026.
- Home field on top of the ratings: 3.3 points (1.8 in conference games).
- Extra FBS edge over FCS opponents beyond their ratings: 14.1 points.
- Elo weight: 0.19 points of margin per point of Elo spread.
- Weight on the betting line: 91% for the margin, 82% for the total.
