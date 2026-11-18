# College football score predictions

Updated Tue Nov 17, 2026 10:41 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 12

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wed 11/18 7:00 PM | Akron @ Massachusetts | Akron 21, Massachusetts 24 | Massachusetts 61% | Akron +155 / Massachusetts -155 | 21.4 – 25.1 | 9–34 / 13–39 | Massachusetts -8.4 / Massachusetts -3.2 | 46.9 / 46.5 | no edge | no edge | no edge |  |
| Wed 11/18 7:30 PM | Central Michigan @ Buffalo | Central Michigan 21, Buffalo 24 | Buffalo 53% | Central Michigan +115 / Buffalo -115 | 22.5 – 23.8 | 10–36 / 10–38 | Central Michigan -0.7 / Buffalo -1.5 | 49.9 / 45.5 | no edge | no edge | no edge |  |
| Thu 11/19 7:30 PM | Rice @ Temple | Rice 24, Temple 27 | Temple 59% | Rice +140 / Temple -140 | 24.0 – 27.1 | 10–38 / 14–42 | Temple -4.0 / Temple -3.0 | 53.9 / 50.5 | no edge | no edge | no edge |  |
| Fri 11/20 6:00 PM | Iowa State @ UCF | Iowa State 24, UCF 27 | UCF 55% | Iowa State +120 / UCF -120 | 24.0 – 26.0 | 10–38 / 13–41 | Iowa State -3.7 / UCF -2.5 | 52.7 / 49.5 | no edge | no edge | no edge |  |
| Fri 11/20 7:30 PM | Clemson @ Duke | Clemson 14, Duke 27 | Duke 83% | Clemson +485 / Duke -485 | 14.3 – 27.3 | 3–26 / 13–42 | Duke -8.0 / Duke -13.5 | 46.0 / 40.8 | no edge | no edge | no edge |  |
| Fri 11/20 7:30 PM | Bowling Green @ Toledo | Bowling Green 14, Toledo 31 | Toledo 88% | Bowling Green +720 / Toledo -720 | 15.8 – 32.0 | 6–28 / 17–48 | Toledo -19.9 / Toledo -15.8 | 44.5 / 48.5 | no edge | no edge | no edge |  |
| Fri 11/20 8:00 PM | Oregon @ Michigan State | Oregon 31, Michigan State 14 | Oregon 89% | Oregon -780 / Michigan State +780 | 31.4 – 14.4 | 17–47 / 3–26 | Oregon -19.9 / Oregon -16.8 | 46.9 / 45.5 | no edge | no edge | no edge |  |
| Fri 11/20 8:00 PM | UTEP @ Air Force | UTEP 10, Air Force 34 | Air Force 95% | UTEP +2025 / Air Force -2025 | 12.4 – 35.7 | 3–23 / 21–52 | Air Force -24.5 / Air Force -23.2 | 50.7 / 47.5 | no edge | no edge | no edge |  |
| Fri 11/20 9:00 PM | New Mexico @ Wyoming | New Mexico 24, Wyoming 17 | New Mexico 69% | New Mexico -225 / Wyoming +225 | 22.7 – 15.7 | 10–36 / 6–27 | New Mexico -5.1 / New Mexico -7.2 | 43.3 / 37.5 | no edge | no edge | no edge |  |
| Sat 11/21 12:00 PM | Vanderbilt @ Florida | Vanderbilt 17, Florida 31 | Florida 82% | Vanderbilt +460 / Florida -460 | 17.4 – 30.5 | 6–30 / 16–45 | Florida -9.3 / Florida -13.5 | 50.8 / 47.2 | no edge | no edge | no edge |  |
| Sat 11/21 12:00 PM | Wofford @ Ole Miss | Wofford 3, Ole Miss 59 | Ole Miss 100% | Wofford +9900 / Ole Miss -9900 | 3.0 – 58.0 | 0–7 / 44–73 | Ole Miss -55.0 / – | 61.0 / – | no line yet | no line yet (fair: Ole Miss -9900) | no line yet | FCS opponent |
| Sat 11/21 12:00 PM | BYU @ Kansas | BYU 27, Kansas 24 | BYU 64% | BYU -180 / Kansas +180 | 26.6 – 21.2 | 13–41 / 9–34 | BYU -2.2 / BYU -5.8 | 51.6 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/21 12:00 PM | Colorado @ Cincinnati | Colorado 28, Cincinnati 31 | Cincinnati 59% | Colorado +145 / Cincinnati -145 | 27.8 – 30.9 | 14–42 / 17–45 | Cincinnati -4.3 / Cincinnati -3.0 | 59.3 / 58.5 | no edge | no edge | no edge |  |
| Sat 11/21 12:00 PM | Syracuse @ Boston College | Syracuse 27, Boston College 24 | Syracuse 58% | Syracuse -140 / Boston College +140 | 26.9 – 24.0 | 14–41 / 10–38 | Syracuse -7.3 / Syracuse -2.5 | 51.4 / 50.8 | no edge | no edge | no edge |  |
| Sat 11/21 12:00 PM | Wake Forest @ Georgia Tech | Wake Forest 38, Georgia Tech 17 | Wake Forest 92% | Wake Forest -1205 / Georgia Tech +1205 | 38.5 – 17.6 | 24–55 / 6–30 | Wake Forest -22.7 / Wake Forest -20.8 | 54.3 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/21 12:00 PM | Northwestern @ Minnesota | Northwestern 24, Minnesota 21 | Northwestern 58% | Northwestern -140 / Minnesota +140 | 23.1 – 20.0 | 10–37 / 7–33 | Northwestern -4.8 / Northwestern -3.0 | 46.0 / 42.5 | no edge | no edge | no edge |  |
| Sat 11/21 12:00 PM | Ohio State @ Nebraska | Ohio State 24, Nebraska 21 | Ohio State 59% | Ohio State -145 / Nebraska +145 | 23.3 – 19.9 | 10–37 / 7–33 | Ohio State -7.4 / Ohio State -3.0 | 49.4 / 41.8 | no edge | no edge | Over 41.75 (-110*): EV +4.4%, 55%, stake 1.2u | * price not posted; assumed -110 |
| Sat 11/21 12:00 PM | Wisconsin @ Purdue | Wisconsin 24, Purdue 21 | Wisconsin 66% | Wisconsin -195 / Purdue +195 | 26.3 – 20.3 | 13–41 / 7–34 | Wisconsin -6.0 / Wisconsin -6.0 | 47.1 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/21 12:00 PM | East Carolina @ Army | East Carolina 21, Army 24 | Army 63% | East Carolina +175 / Army -175 | 20.7 – 26.0 | 9–34 / 13–40 | Army -2.7 / Army -5.5 | 52.2 / 45.5 | no edge | no edge | no edge |  |
| Sat 11/21 12:00 PM | Memphis @ Navy | Memphis 34, Navy 31 | Memphis 57% | Memphis -130 / Navy +130 | 34.6 – 31.5 | 20–49 / 17–46 | Memphis -1.8 / Memphis -3.2 | 60.6 / 67.2 | no edge | no edge | no edge |  |
| Sat 11/21 12:00 PM | North Texas @ Tulane | North Texas 31, Tulane 24 | North Texas 66% | North Texas -195 / Tulane +195 | 31.4 – 25.2 | 17–47 / 13–39 | North Texas -5.9 / North Texas -6.2 | 61.3 / 55.8 | no edge | no edge | no edge |  |
| Sat 11/21 12:30 PM | North Carolina @ Virginia | North Carolina 21, Virginia 24 | Virginia 54% | North Carolina +115 / Virginia -115 | 21.6 – 23.0 | 10–35 / 10–36 | Virginia -1.0 / Virginia -1.5 | 49.6 / 43.5 | no edge | no edge | no edge |  |
| Sat 11/21 1:00 PM | Tennessee Tech @ Mississippi State | Tennessee Tech 10, Mississippi State 38 | Mississippi State 98% | Tennessee Tech +6475 / Mississippi State -6475 | 11.1 – 40.8 | 0–21 / 26–58 | Mississippi State -29.7 / – | 52.0 / – | no line yet | no line yet (fair: Mississippi State -6475) | no line yet | FCS opponent |
| Sat 11/21 1:00 PM | Houston @ West Virginia | Houston 38, West Virginia 31 | Houston 69% | Houston -225 / West Virginia +225 | 38.9 – 30.7 | 24–55 / 16–45 | Houston -8.0 / Houston -8.2 | 66.2 / 70.2 | no edge | no edge | no edge |  |
| Sat 11/21 1:00 PM | Western Kentucky @ Liberty | Western Kentucky 17, Liberty 34 | Liberty 88% | Western Kentucky +745 / Liberty -745 | 18.0 – 35.0 | 7–30 / 20–50 | Liberty -14.4 / Liberty -17.2 | 52.8 / 53.0 | no edge | no edge | no edge |  |
| Sat 11/21 2:00 PM | Chattanooga @ Alabama | Chattanooga 3, Alabama 55 | Alabama 100% | Chattanooga +9900 / Alabama -9900 | 3.0 – 56.2 | 0–7 / 42–72 | Alabama -53.2 / – | 59.2 / – | no line yet | no line yet (fair: Alabama -9900) | no line yet | FCS opponent |
| Sat 11/21 2:00 PM | Charlotte @ Tulsa | Charlotte 17, Tulsa 38 | Tulsa 94% | Charlotte +1655 / Tulsa -1655 | 14.7 – 37.6 | 3–27 / 23–54 | Tulsa -23.7 / Tulsa -22.8 | 51.9 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/21 2:00 PM | Missouri State @ Jacksonville State | Missouri State 21, Jacksonville State 31 | Jacksonville State 77% | Missouri State +335 / Jacksonville State -335 | 20.9 – 31.8 | 7–34 / 17–47 | Jacksonville State -13.0 / Jacksonville State -10.8 | 53.5 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/21 2:00 PM | Middle Tennessee @ Sam Houston | Middle Tennessee 24, Sam Houston 21 | Middle Tennessee 64% | Middle Tennessee -180 / Sam Houston +180 | 26.4 – 21.1 | 13–41 / 9–34 | Middle Tennessee -3.6 / Middle Tennessee -5.5 | 44.2 / 48.2 | no edge | no edge | no edge |  |
| Sat 11/21 2:30 PM | Iowa @ Illinois | Iowa 24, Illinois 17 | Iowa 72% | Iowa -255 / Illinois +255 | 25.2 – 16.8 | 11–39 / 6–29 | Iowa -6.8 / Iowa -8.5 | 49.0 / 40.5 | no edge | no edge | Over 40.5 (-110*): EV +3.3%, 54%, stake 0.9u | * price not posted; assumed -110 |
| Sat 11/21 2:30 PM | South Florida @ Florida Atlantic | South Florida 34, Florida Atlantic 31 | South Florida 53% | South Florida -110 / Florida Atlantic +110 | 32.6 – 31.5 | 17–48 / 17–45 | Florida Atlantic -0.7 / South Florida -1.2 | 63.0 / 64.2 | no edge | no edge | no edge |  |
| Sat 11/21 2:30 PM | UL Monroe @ App State | UL Monroe 17, App State 31 | App State 82% | UL Monroe +450 / App State -450 | 18.6 – 32.2 | 7–31 / 17–47 | App State -12.3 / App State -13.8 | 54.4 / 50.0 | no edge | no edge | no edge |  |
| Sat 11/21 3:00 PM | Coastal Carolina @ Louisiana | Coastal Carolina 21, Louisiana 31 | Louisiana 76% | Coastal Carolina +310 / Louisiana -310 | 20.3 – 30.4 | 7–34 / 17–45 | Louisiana -5.9 / Louisiana -10.5 | 50.7 / 50.8 | no edge | no edge | no edge |  |
| Sat 11/21 3:00 PM | Delaware @ New Mexico State | Delaware 27, New Mexico State 24 | Delaware 60% | Delaware -150 / New Mexico State +150 | 28.9 – 25.0 | 14–44 / 13–38 | Delaware -8.6 / Delaware -3.5 | 54.5 / 54.2 | no edge | no edge | no edge |  |
| Sat 11/21 3:00 PM | Florida International @ Kennesaw State | Florida International 21, Kennesaw State 24 | Kennesaw State 60% | Florida International +150 / Kennesaw State -150 | 20.6 – 24.4 | 7–34 / 10–38 | Kennesaw State -6.5 / Kennesaw State -3.5 | 47.2 / 44.5 | no edge | no edge | no edge |  |
| Sat 11/21 3:30 PM | Samford @ Auburn | Samford 3, Auburn 52 | Auburn 100% | Samford +9900 / Auburn -9900 | 3.0 – 50.3 | 0–7 / 35–66 | Auburn -47.3 / – | 53.3 / – | no line yet | no line yet (fair: Auburn -9900) | no line yet | FCS opponent |
| Sat 11/21 3:30 PM | LSU @ Tennessee | LSU 24, Tennessee 21 | LSU 53% | LSU -115 / Tennessee +115 | 23.7 – 22.5 | 10–38 / 10–35 | LSU -0.7 / LSU -1.2 | 47.9 / 45.8 | no edge | no edge | no edge |  |
| Sat 11/21 3:30 PM | Arkansas @ Texas | Arkansas 13, Texas 34 | Texas 93% | Arkansas +1400 / Texas -1400 | 13.0 – 33.4 | 3–24 / 19–49 | Texas -20.8 / Texas -20.2 | 45.9 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/21 3:30 PM | Texas Tech @ Baylor | Texas Tech 27, Baylor 24 | Texas Tech 61% | Texas Tech -155 / Baylor +155 | 29.3 – 25.5 | 14–45 / 13–39 | Texas Tech -6.6 / Texas Tech -3.5 | 50.8 / 55.8 | no edge | no edge | no edge |  |
| Sat 11/21 3:30 PM | NC State @ Florida State | NC State 24, Florida State 31 | Florida State 74% | NC State +290 / Florida State -290 | 23.6 – 33.4 | 10–38 / 19–49 | Florida State -7.5 / Florida State -10.0 | 59.7 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/21 3:30 PM | UCLA @ Michigan | UCLA 20, Michigan 17 | UCLA 61% | UCLA -155 / Michigan +155 | 20.9 – 17.3 | 9–34 / 7–30 | UCLA -4.7 / UCLA -3.5 | 41.6 / 37.5 | no edge | no edge | no edge |  |
| Sat 11/21 3:30 PM | Rutgers @ Penn State | Rutgers 14, Penn State 38 | Penn State 96% | Rutgers +2270 / Penn State -2270 | 13.4 – 37.4 | 3–24 / 22–54 | Penn State -21.5 / Penn State -24.2 | 51.6 / 50.8 | no edge | no edge | no edge |  |
| Sat 11/21 3:30 PM | Indiana @ Washington | Indiana 24, Washington 17 | Indiana 72% | Indiana -250 / Washington +250 | 25.8 – 18.1 | 13–41 / 7–31 | Indiana -9.4 / Indiana -7.5 | 44.4 / 43.8 | no edge | no edge | no edge |  |
| Sat 11/21 3:30 PM | Old Dominion @ UConn | Old Dominion 17, UConn 31 | UConn 84% | Old Dominion +510 / UConn -510 | 17.0 – 30.8 | 6–29 / 17–45 | UConn -17.0 / UConn -13.5 | 48.7 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/21 3:45 PM | Texas A&M @ Oklahoma | Texas A&M 17, Oklahoma 24 | Oklahoma 71% | Texas A&M +250 / Oklahoma -250 | 15.4 – 22.9 | 5–27 / 10–37 | Oklahoma -9.7 / Oklahoma -7.2 | 38.7 / 38.5 | no edge | no edge | no edge |  |
| Sat 11/21 4:00 PM | Northern Illinois @ North Dakota State | Northern Illinois 10, North Dakota State 34 | North Dakota State 97% | Northern Illinois +3325 / North Dakota State -3325 | 9.6 – 34.4 | 0–20 / 20–50 | North Dakota State -23.3 / North Dakota State -25.0 | 46.4 / 43.5 | no edge | no edge | no edge |  |
| Sat 11/21 4:00 PM | Georgia Southern @ Troy | Georgia Southern 28, Troy 21 | Georgia Southern 72% | Georgia Southern -255 / Troy +255 | 28.6 – 20.0 | 14–43 / 7–34 | Georgia Southern -6.8 / Georgia Southern -8.8 | 49.2 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/21 4:00 PM | Georgia State @ Marshall | Georgia State 27, Marshall 30 | Marshall 54% | Georgia State +115 / Marshall -115 | 27.4 – 29.1 | 14–42 / 14–44 | Marshall -3.2 / Marshall -1.5 | 56.7 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/21 4:00 PM | South Alabama @ Southern Miss | South Alabama 34, Southern Miss 31 | South Alabama 60% | South Alabama -150 / Southern Miss +150 | 34.3 – 30.4 | 20–49 / 16–45 | South Alabama -4.9 / South Alabama -3.8 | 59.9 / 65.8 | no edge | no edge | no edge |  |
| Sat 11/21 6:00 PM | Washington State @ Texas State | Washington State 24, Texas State 34 | Texas State 77% | Washington State +340 / Texas State -340 | 25.0 – 36.3 | 10–38 / 21–52 | Texas State -9.7 / Texas State -11.5 | 60.0 / 61.5 | no edge | no edge | no edge |  |
| Sat 11/21 6:15 PM | Maryland @ USC | Maryland 21, USC 38 | USC 87% | Maryland +645 / USC -645 | 20.0 – 37.0 | 7–34 / 21–52 | USC -12.2 / USC -17.5 | 54.7 / 57.5 | no edge | no edge | no edge |  |
| Sat 11/21 7:00 PM | Arizona @ Kansas State | Arizona 27, Kansas State 24 | Arizona 67% | Arizona -200 / Kansas State +200 | 29.7 – 23.2 | 16–45 / 10–37 | Arizona -1.9 / Arizona -7.0 | 55.1 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/21 7:00 PM | Virginia Tech @ Miami | Virginia Tech 17, Miami 38 | Miami 91% | Virginia Tech +1045 / Miami -1045 | 20.0 – 40.9 | 7–33 / 26–57 | Miami -24.8 / Miami -20.5 | 59.4 / 61.2 | no edge | no edge | no edge |  |
| Sat 11/21 7:00 PM | UNLV @ San José State | UNLV 27, San José State 20 | UNLV 70% | UNLV -230 / San José State +230 | 27.3 – 20.1 | 14–42 / 7–34 | UNLV -9.5 / UNLV -7.0 | 50.5 / 46.8 | no edge | no edge | no edge |  |
| Sat 11/21 7:00 PM | Arkansas State @ Louisiana Tech | Arkansas State 17, Louisiana Tech 31 | Louisiana Tech 83% | Arkansas State +475 / Louisiana Tech -475 | 19.3 – 33.0 | 7–31 / 17–48 | Louisiana Tech -13.4 / Louisiana Tech -13.8 | 49.8 / 52.8 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | Kentucky @ Missouri | Kentucky 21, Missouri 24 | Missouri 65% | Kentucky +190 / Missouri -190 | 21.4 – 27.1 | 9–34 / 14–41 | Missouri -7.8 / Missouri -5.5 | 48.7 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | Georgia @ South Carolina | Georgia 34, South Carolina 17 | Georgia 87% | Georgia -665 / South Carolina +665 | 33.5 – 17.1 | 17–49 / 6–30 | Georgia -15.8 / Georgia -16.5 | 49.4 / 51.2 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | Pittsburgh @ Louisville | Pittsburgh 17, Louisville 31 | Louisville 83% | Pittsburgh +505 / Louisville -505 | 18.4 – 32.3 | 7–31 / 17–48 | Louisville -16.3 / Louisville -13.8 | 51.6 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | SMU @ Notre Dame | SMU 17, Notre Dame 38 | Notre Dame 92% | SMU +1115 / Notre Dame -1115 | 17.6 – 38.0 | 6–30 / 23–55 | Notre Dame -18.9 / Notre Dame -20.5 | 52.9 / 56.2 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | Stanford @ California | Stanford 31, California 28 | Stanford 55% | Stanford -125 / California +125 | 29.3 – 26.9 | 14–44 / 14–41 | Stanford -0.4 / Stanford -2.5 | 54.8 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | Colorado State @ Fresno State | Colorado State 21, Fresno State 42 | Fresno State 90% | Colorado State +925 / Fresno State -925 | 22.5 – 42.2 | 10–36 / 27–58 | Fresno State -12.1 / Fresno State -20.5 | 61.1 / 65.5 | no edge | Colorado State (+874): EV +5.1%, 11%, stake 0.1u | no edge |  |
| Sat 11/21 8:00 PM | UTSA @ UAB | UTSA 31, UAB 24 | UTSA 65% | UTSA -190 / UAB +190 | 28.9 – 22.6 | 14–44 / 10–37 | UTSA -7.4 / UTSA -6.2 | 51.7 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/21 9:00 PM | Utah @ TCU | Utah 28, TCU 21 | Utah 70% | Utah -230 / TCU +230 | 27.3 – 19.7 | 14–42 / 7–33 | Utah -13.5 / Utah -7.0 | 49.8 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/21 9:30 PM | San Diego State @ Boise State | San Diego State 21, Boise State 38 | Boise State 86% | San Diego State +610 / Boise State -610 | 22.4 – 38.9 | 10–36 / 24–55 | Boise State -13.8 / Boise State -16.8 | 56.7 / 62.2 | no edge | San Diego State (+600): EV +3.6%, 15%, stake 0.1u | no edge |  |
| Sat 11/21 10:15 PM | Oklahoma State @ Arizona State | Oklahoma State 31, Arizona State 28 | Oklahoma State 56% | Oklahoma State -125 / Arizona State +125 | 31.6 – 29.0 | 17–46 / 14–44 | Arizona State -1.1 / Oklahoma State -3.0 | 57.8 / 61.2 | no edge | no edge | no edge |  |
| Sat 11/21 10:30 PM | Utah State @ Oregon State | Utah State 21, Oregon State 31 | Oregon State 75% | Utah State +295 / Oregon State -295 | 20.7 – 30.5 | 7–34 / 16–45 | Oregon State -12.2 / Oregon State -9.5 | 53.2 / 50.8 | no edge | no edge | no edge |  |
| Sat 11/21 10:30 PM | Hawai'i @ Nevada | Hawai'i 21, Nevada 24 | Nevada 61% | Hawai'i +155 / Nevada -155 | 19.1 – 22.6 | 7–31 / 10–36 | Hawai'i -1.3 / Nevada -4.0 | 47.0 / 40.5 | no edge | no edge | no edge |  |

## 2026 Week 13

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/24 7:00 PM | Kent State @ Eastern Michigan | Kent State 24, Eastern Michigan 27 | Eastern Michigan 63% | Kent State +170 / Eastern Michigan -170 | 22.5 – 27.3 | 10–36 / 14–42 | Eastern Michigan -4.8 / – | 49.8 / – | no line yet | no line yet (fair: Eastern Michigan -170) | no line yet |  |
| Tue 11/24 7:00 PM | Miami (OH) @ Western Michigan | Miami (OH) 24, Western Michigan 27 | Western Michigan 60% | Miami (OH) +150 / Western Michigan -150 | 22.3 – 25.9 | 10–35 / 13–41 | Western Michigan -3.6 / – | 48.2 / – | no line yet | no line yet (fair: Western Michigan -150) | no line yet |  |
| Thu 11/26 8:00 PM | TCU @ Texas Tech | TCU 17, Texas Tech 34 | Texas Tech 87% | TCU +695 / Texas Tech -695 | 18.5 – 35.1 | 7–31 / 20–51 | Texas Tech -16.9 / Texas Tech -16.5 | 44.9 / 55.5 | no edge | no edge | Under 55.5 (-110*): EV +3.9%, 54%, stake 1.1u | * price not posted; assumed -110 |
| Fri 11/27 TBA | Temple @ Memphis | Temple 21, Memphis 38 | Memphis 88% | Temple +730 / Memphis -730 | 21.1 – 38.9 | 9–35 / 24–55 | Memphis -17.7 / – | 60.0 / – | no line yet | no line yet (fair: Memphis -730) | no line yet |  |
| Fri 11/27 TBA | Tulsa @ UTSA | Tulsa 28, UTSA 31 | UTSA 60% | Tulsa +150 / UTSA -150 | 26.5 – 30.5 | 13–41 / 17–45 | UTSA -4.0 / – | 57.0 / – | no line yet | no line yet (fair: UTSA -150) | no line yet |  |
| Fri 11/27 12:00 PM | Mississippi State @ Ole Miss | Mississippi State 24, Ole Miss 38 | Ole Miss 83% | Mississippi State +485 / Ole Miss -485 | 21.7 – 36.1 | 9–35 / 21–52 | Ole Miss -13.4 / Ole Miss -14.5 | 58.8 / 57.5 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Nebraska @ Iowa | Nebraska 21, Iowa 24 | Iowa 62% | Nebraska +165 / Iowa -165 | 19.7 – 24.2 | 7–33 / 10–38 | Iowa -4.4 / – | 43.9 / – | no line yet | no line yet (fair: Iowa -165) | no line yet |  |
| Fri 11/27 12:00 PM | Buffalo @ Akron | Buffalo 31, Akron 24 | Buffalo 69% | Buffalo -225 / Akron +225 | 29.5 – 21.8 | 15–45 / 10–35 | Buffalo -7.6 / – | 51.3 / – | no line yet | no line yet (fair: Buffalo -225) | no line yet |  |
| Fri 11/27 12:00 PM | Toledo @ Ohio | Toledo 27, Ohio 24 | Toledo 61% | Toledo -155 / Ohio +155 | 26.8 – 22.8 | 14–42 / 10–37 | Toledo -4.0 / – | 49.7 / – | no line yet | no line yet (fair: Toledo -155) | no line yet |  |
| Fri 11/27 3:00 PM | App State @ South Alabama | App State 31, South Alabama 28 | South Alabama 51% | App State +105 / South Alabama -105 | 29.3 – 29.9 | 14–44 / 16–45 | South Alabama -0.6 / – | 59.2 / – | no line yet | no line yet (fair: South Alabama -105) | no line yet |  |
| Fri 11/27 3:30 PM | Florida @ Florida State | Florida 27, Florida State 24 | Florida 62% | Florida -160 / Florida State +160 | 28.7 – 24.4 | 14–44 / 10–38 | Florida -2.4 / Florida -4.5 | 55.5 / 52.5 | no edge | no edge | no edge |  |
| Fri 11/27 3:30 PM | North Dakota State @ San José State | North Dakota State 28, San José State 14 | North Dakota State 85% | North Dakota State -565 / San José State +565 | 28.1 – 14.0 | 14–43 / 3–25 | North Dakota State -14.1 / – | 42.1 / – | no line yet | no line yet (fair: North Dakota State -565) | no line yet |  |
| Fri 11/27 4:30 PM | Air Force @ New Mexico | Air Force 21, New Mexico 24 | New Mexico 62% | Air Force +165 / New Mexico -165 | 21.8 – 26.3 | 10–35 / 13–41 | New Mexico -4.5 / – | 48.2 / – | no line yet | no line yet (fair: New Mexico -165) | no line yet |  |
| Fri 11/27 7:30 PM | Texas @ Texas A&M | Texas 27, Texas A&M 24 | Texas 58% | Texas -140 / Texas A&M +140 | 27.1 – 24.1 | 14–41 / 10–38 | Texas -8.9 / Texas -2.5 | 40.5 / 53.5 | no edge | no edge | Under 53.5 (-110*): EV +6.5%, 56%, stake 1.8u | * price not posted; assumed -110 |
| Fri 11/27 7:30 PM | Minnesota @ Wisconsin | Minnesota 17, Wisconsin 24 | Wisconsin 70% | Minnesota +240 / Wisconsin -240 | 15.0 – 22.4 | 3–27 / 10–36 | Wisconsin -7.4 / – | 37.4 / – | no line yet | no line yet (fair: Wisconsin -240) | no line yet |  |
| Fri 11/27 9:00 PM | West Virginia @ Utah | West Virginia 17, Utah 45 | Utah 96% | West Virginia +2240 / Utah -2240 | 19.6 – 44.4 | 7–32 / 30–60 | Utah -24.7 / – | 64.0 / – | no line yet | no line yet (fair: Utah -2240) | no line yet |  |
| Sat 11/28 TBA | Auburn @ Alabama | Auburn 24, Alabama 31 | Alabama 75% | Auburn +300 / Alabama -300 | 21.1 – 31.1 | 9–35 / 17–46 | Alabama -10.7 / Alabama -10.0 | 50.9 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | LSU @ Arkansas | LSU 34, Arkansas 17 | LSU 90% | LSU -860 / Arkansas +860 | 35.0 – 16.8 | 20–51 / 6–29 | LSU -18.2 / – | 51.7 / – | no line yet | no line yet (fair: LSU -860) | no line yet |  |
| Sat 11/28 TBA | Georgia Tech @ Georgia | Georgia Tech 7, Georgia 42 | Georgia 100% | Georgia Tech +9900 / Georgia -9900 | 6.9 – 43.2 | 0–14 / 28–60 | Georgia -36.3 / – | 50.1 / – | no line yet | no line yet (fair: Georgia -9900) | no line yet |  |
| Sat 11/28 TBA | Louisville @ Kentucky | Louisville 27, Kentucky 24 | Louisville 64% | Louisville -175 / Kentucky +175 | 29.2 – 23.6 | 14–44 / 10–38 | Louisville -5.7 / – | 52.8 / – | no line yet | no line yet (fair: Louisville -175) | no line yet |  |
| Sat 11/28 TBA | Oklahoma @ Missouri | Oklahoma 24, Missouri 21 | Oklahoma 56% | Oklahoma -125 / Missouri +125 | 22.1 – 20.3 | 10–35 / 7–33 | Oklahoma -1.8 / – | 42.4 / – | no line yet | no line yet (fair: Oklahoma -125) | no line yet |  |
| Sat 11/28 TBA | South Carolina @ Clemson | South Carolina 24, Clemson 27 | Clemson 56% | South Carolina +130 / Clemson -130 | 24.9 – 27.4 | 12–38 / 14–42 | South Carolina -2.6 / Clemson -3.0 | 47.1 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Tennessee @ Vanderbilt | Tennessee 27, Vanderbilt 24 | Tennessee 60% | Tennessee -150 / Vanderbilt +150 | 29.8 – 25.8 | 16–45 / 13–40 | Tennessee -13.0 / Tennessee -3.0 | 46.7 / 57.5 | no edge | no edge | Under 57.5 (-110*): EV +6.4%, 56%, stake 1.8u | * price not posted; assumed -110 |
| Sat 11/28 TBA | Arizona State @ Arizona | Arizona State 24, Arizona 27 | Arizona 62% | Arizona State +165 / Arizona -165 | 24.0 – 28.7 | 10–38 / 14–44 | Arizona -6.2 / Arizona -4.5 | 53.8 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Baylor @ Houston | Baylor 28, Houston 31 | Houston 52% | Baylor +110 / Houston -110 | 28.6 – 29.3 | 14–42 / 16–44 | Houston -0.7 / – | 58.0 / – | no line yet | no line yet (fair: Houston -110) | no line yet |  |
| Sat 11/28 TBA | UCF @ Colorado | UCF 24, Colorado 27 | Colorado 58% | UCF +140 / Colorado -140 | 23.9 – 27.2 | 10–38 / 14–42 | Colorado -3.2 / – | 51.1 / – | no line yet | no line yet (fair: Colorado -140) | no line yet |  |
| Sat 11/28 TBA | Cincinnati @ BYU | Cincinnati 24, BYU 31 | BYU 76% | Cincinnati +315 / BYU -315 | 23.8 – 34.2 | 10–38 / 20–49 | BYU -10.4 / – | 58.0 / – | no line yet | no line yet (fair: BYU -315) | no line yet |  |
| Sat 11/28 TBA | Kansas @ Oklahoma State | Kansas 27, Oklahoma State 30 | Oklahoma State 55% | Kansas +120 / Oklahoma State -120 | 29.0 – 31.0 | 14–44 / 17–45 | Oklahoma State -2.0 / – | 60.0 / – | no line yet | no line yet (fair: Oklahoma State -120) | no line yet |  |
| Sat 11/28 TBA | Kansas State @ Iowa State | Kansas State 24, Iowa State 27 | Iowa State 61% | Kansas State +155 / Iowa State -155 | 24.7 – 28.9 | 13–38 / 14–44 | Iowa State -4.2 / – | 53.6 / – | no line yet | no line yet (fair: Iowa State -155) | no line yet |  |
| Sat 11/28 TBA | Boston College @ Miami | Boston College 10, Miami 45 | Miami 99% | Boston College +9900 / Miami -9900 | 10.8 – 44.6 | 0–21 / 30–62 | Miami -33.9 / – | 55.4 / – | no line yet | no line yet (fair: Miami -9900) | no line yet |  |
| Sat 11/28 TBA | Duke @ Wake Forest | Duke 17, Wake Forest 31 | Wake Forest 83% | Duke +495 / Wake Forest -495 | 19.3 – 33.2 | 7–32 / 17–49 | Wake Forest -13.8 / – | 52.5 / – | no line yet | no line yet (fair: Wake Forest -495) | no line yet |  |
| Sat 11/28 TBA | NC State @ North Carolina | NC State 31, North Carolina 28 | NC State 53% | NC State -110 / North Carolina +110 | 28.3 – 27.5 | 14–43 / 14–42 | North Carolina -5.8 / NC State -1.5 | 57.3 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Notre Dame @ Syracuse | Notre Dame 35, Syracuse 14 | Notre Dame 92% | Notre Dame -1215 / Syracuse +1215 | 35.8 – 15.8 | 21–52 / 6–28 | Notre Dame -20.1 / – | 51.6 / – | no line yet | no line yet (fair: Notre Dame -1215) | no line yet |  |
| Sat 11/28 TBA | Pittsburgh @ California | Pittsburgh 31, California 24 | Pittsburgh 74% | Pittsburgh -285 / California +285 | 29.7 – 20.5 | 16–45 / 7–34 | Pittsburgh -9.2 / – | 50.2 / – | no line yet | no line yet (fair: Pittsburgh -285) | no line yet |  |
| Sat 11/28 TBA | SMU @ Stanford | SMU 35, Stanford 21 | SMU 83% | SMU -480 / Stanford +480 | 35.3 – 21.5 | 21–51 / 9–35 | SMU -13.8 / – | 56.7 / – | no line yet | no line yet (fair: SMU -480) | no line yet |  |
| Sat 11/28 TBA | Virginia @ Virginia Tech | Virginia 24, Virginia Tech 27 | Virginia Tech 54% | Virginia +115 / Virginia Tech -115 | 25.8 – 27.2 | 13–40 / 14–42 | Virginia Tech -1.0 / Virginia Tech -1.5 | 50.7 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Illinois @ Northwestern | Illinois 27, Northwestern 24 | Illinois 57% | Illinois -130 / Northwestern +130 | 27.9 – 25.2 | 14–42 / 13–40 | Northwestern -5.7 / Illinois -3.5 | 56.2 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Purdue @ Indiana | Purdue 10, Indiana 38 | Indiana 96% | Purdue +2530 / Indiana -2530 | 12.1 – 36.8 | 3–23 / 21–52 | Indiana -24.7 / – | 48.9 / – | no line yet | no line yet (fair: Indiana -2530) | no line yet |  |
| Sat 11/28 TBA | Penn State @ Maryland | Penn State 24, Maryland 17 | Penn State 68% | Penn State -210 / Maryland +210 | 26.8 – 19.9 | 13–41 / 7–33 | Penn State -6.9 / – | 46.6 / – | no line yet | no line yet (fair: Penn State -210) | no line yet |  |
| Sat 11/28 TBA | Washington @ Oregon | Washington 17, Oregon 34 | Oregon 85% | Washington +575 / Oregon -575 | 19.1 – 34.4 | 7–31 / 20–51 | Oregon -12.9 / Oregon -15.5 | 48.5 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Michigan State @ Rutgers | Michigan State 27, Rutgers 24 | Michigan State 56% | Michigan State -125 / Rutgers +125 | 26.7 – 24.5 | 13–41 / 12–38 | Michigan State -2.2 / – | 51.2 / – | no line yet | no line yet (fair: Michigan State -125) | no line yet |  |
| Sat 11/28 TBA | USC @ UCLA | USC 31, UCLA 24 | USC 73% | USC -270 / UCLA +270 | 31.9 – 23.1 | 17–48 / 10–37 | UCLA -7.4 / USC -10.5 | 52.8 / 55.5 | UCLA +10.5 (-110*): EV +4.2%, 55%, stake 1.1u | UCLA (+360): EV +14.2%, 25%, stake 1.0u | no edge | * price not posted; assumed -110 |
| Sat 11/28 TBA | UConn @ Wyoming | UConn 27, Wyoming 24 | UConn 62% | UConn -160 / Wyoming +160 | 29.6 – 25.2 | 16–44 / 12–39 | UConn -4.4 / – | 54.8 / – | no line yet | no line yet (fair: UConn -160) | no line yet |  |
| Sat 11/28 TBA | Florida Atlantic @ East Carolina | Florida Atlantic 28, East Carolina 31 | East Carolina 56% | Florida Atlantic +130 / East Carolina -130 | 28.2 – 30.4 | 14–42 / 17–45 | East Carolina -2.2 / – | 58.7 / – | no line yet | no line yet (fair: East Carolina -130) | no line yet |  |
| Sat 11/28 TBA | Tulane @ South Florida | Tulane 21, South Florida 28 | South Florida 69% | Tulane +220 / South Florida -220 | 22.1 – 29.4 | 10–35 / 16–44 | South Florida -7.4 / – | 51.5 / – | no line yet | no line yet (fair: South Florida -220) | no line yet |  |
| Sat 11/28 TBA | Army @ Rice | Army 31, Rice 24 | Army 70% | Army -230 / Rice +230 | 32.4 – 24.2 | 17–48 / 10–38 | Army -8.3 / – | 56.6 / – | no line yet | no line yet (fair: Army -230) | no line yet |  |
| Sat 11/28 TBA | Navy @ Charlotte | Navy 34, Charlotte 17 | Navy 87% | Navy -690 / Charlotte +690 | 34.8 – 17.7 | 20–51 / 7–31 | Navy -17.1 / – | 52.5 / – | no line yet | no line yet (fair: Navy -690) | no line yet |  |
| Sat 11/28 TBA | UAB @ North Texas | UAB 24, North Texas 34 | North Texas 77% | UAB +335 / North Texas -335 | 23.6 – 34.9 | 10–38 / 20–51 | North Texas -11.3 / – | 58.4 / – | no line yet | no line yet (fair: North Texas -335) | no line yet |  |
| Sat 11/28 TBA | UTEP @ Northern Illinois | UTEP 21, Northern Illinois 28 | Northern Illinois 69% | UTEP +225 / Northern Illinois -225 | 21.3 – 28.8 | 9–35 / 14–43 | Northern Illinois -7.4 / – | 50.1 / – | no line yet | no line yet (fair: Northern Illinois -225) | no line yet |  |
| Sat 11/28 TBA | Coastal Carolina @ James Madison | Coastal Carolina 17, James Madison 34 | James Madison 86% | Coastal Carolina +605 / James Madison -605 | 17.9 – 33.6 | 7–31 / 20–49 | James Madison -15.7 / – | 51.5 / – | no line yet | no line yet (fair: James Madison -605) | no line yet |  |
| Sat 11/28 TBA | Louisiana Tech @ Georgia Southern | Louisiana Tech 27, Georgia Southern 24 | Louisiana Tech 53% | Louisiana Tech -115 / Georgia Southern +115 | 25.9 – 24.7 | 13–41 / 10–38 | Louisiana Tech -1.2 / – | 50.7 / – | no line yet | no line yet (fair: Louisiana Tech -115) | no line yet |  |
| Sat 11/28 TBA | Louisiana @ Georgia State | Louisiana 27, Georgia State 24 | Louisiana 53% | Louisiana -110 / Georgia State +110 | 28.1 – 27.4 | 14–42 / 14–42 | Louisiana -0.7 / – | 55.5 / – | no line yet | no line yet (fair: Louisiana -110) | no line yet |  |
| Sat 11/28 TBA | Marshall @ UL Monroe | Marshall 31, UL Monroe 24 | Marshall 67% | Marshall -205 / UL Monroe +205 | 30.6 – 24.0 | 17–45 / 10–38 | Marshall -6.6 / – | 54.6 / – | no line yet | no line yet (fair: Marshall -205) | no line yet |  |
| Sat 11/28 TBA | Southern Miss @ Old Dominion | Southern Miss 20, Old Dominion 27 | Old Dominion 69% | Southern Miss +225 / Old Dominion -225 | 19.1 – 26.3 | 7–31 / 13–41 | Old Dominion -7.2 / – | 45.4 / – | no line yet | no line yet (fair: Old Dominion -225) | no line yet |  |
| Sat 11/28 12:00 PM | Michigan @ Ohio State | Michigan 17, Ohio State 31 | Ohio State 83% | Michigan +500 / Ohio State -500 | 16.3 – 29.9 | 6–28 / 16–45 | Ohio State -14.5 / Ohio State -13.5 | 45.3 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Central Michigan @ Ball State | Central Michigan 27, Ball State 24 | Central Michigan 66% | Central Michigan -190 / Ball State +190 | 28.0 – 22.1 | 14–42 / 10–35 | Central Michigan -5.9 / – | 50.0 / – | no line yet | no line yet (fair: Central Michigan -190) | no line yet |  |
| Sat 11/28 12:00 PM | Massachusetts @ Bowling Green | Massachusetts 17, Bowling Green 20 | Bowling Green 58% | Massachusetts +135 / Bowling Green -135 | 18.8 – 22.1 | 7–31 / 10–35 | Bowling Green -3.2 / – | 40.9 / – | no line yet | no line yet (fair: Bowling Green -135) | no line yet |  |
| Sat 11/28 1:00 PM | Kennesaw State @ Western Kentucky | Kennesaw State 24, Western Kentucky 27 | Western Kentucky 57% | Kennesaw State +130 / Western Kentucky -130 | 25.3 – 27.9 | 12–38 / 14–42 | Western Kentucky -2.5 / – | 53.2 / – | no line yet | no line yet (fair: Western Kentucky -130) | no line yet |  |
| Sat 11/28 2:00 PM | Liberty @ Missouri State | Liberty 34, Missouri State 17 | Liberty 85% | Liberty -555 / Missouri State +555 | 34.0 – 19.1 | 20–49 / 7–31 | Liberty -14.9 / – | 53.0 / – | no line yet | no line yet (fair: Liberty -555) | no line yet |  |
| Sat 11/28 2:00 PM | Sam Houston @ Florida International | Sam Houston 17, Florida International 24 | Florida International 73% | Sam Houston +275 / Florida International -275 | 15.4 – 23.6 | 5–27 / 10–38 | Florida International -8.2 / – | 39.0 / – | no line yet | no line yet (fair: Florida International -275) | no line yet |  |
| Sat 11/28 2:00 PM | New Mexico State @ Middle Tennessee | New Mexico State 24, Middle Tennessee 27 | Middle Tennessee 61% | New Mexico State +155 / Middle Tennessee -155 | 22.6 – 27.0 | 10–36 / 13–41 | Middle Tennessee -4.4 / – | 49.7 / – | no line yet | no line yet (fair: Middle Tennessee -155) | no line yet |  |
| Sat 11/28 3:00 PM | Troy @ Arkansas State | Troy 21, Arkansas State 24 | Arkansas State 61% | Troy +155 / Arkansas State -155 | 22.1 – 26.2 | 10–35 / 13–41 | Arkansas State -4.1 / – | 48.3 / – | no line yet | no line yet (fair: Arkansas State -155) | no line yet |  |
| Sat 11/28 3:30 PM | Jacksonville State @ Delaware | Jacksonville State 28, Delaware 31 | Delaware 54% | Jacksonville State +120 / Delaware -120 | 27.7 – 29.5 | 14–42 / 16–44 | Delaware -1.8 / – | 57.2 / – | no line yet | no line yet (fair: Delaware -120) | no line yet |  |
| Sat 11/28 9:00 PM | Nevada @ UNLV | Nevada 17, UNLV 27 | UNLV 78% | Nevada +365 / UNLV -365 | 17.9 – 29.1 | 7–31 / 14–44 | UNLV -11.2 / – | 47.1 / – | no line yet | no line yet (fair: UNLV -365) | no line yet |  |
| Sat 11/28 11:00 PM | Sacramento State @ Hawai'i | Sacramento State 17, Hawai'i 31 | Hawai'i 84% | Sacramento State +520 / Hawai'i -520 | 17.2 – 31.5 | 6–30 / 17–46 | Hawai'i -14.3 / – | 48.6 / – | no line yet | no line yet (fair: Hawai'i -520) | no line yet |  |

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
