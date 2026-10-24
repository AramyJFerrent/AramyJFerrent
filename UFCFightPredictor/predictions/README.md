# UFC fight predictions

Updated Sat Oct 24, 2026 05:34 PM ET. Refreshed automatically every day and several times on fight week; each bout's prediction is locked when its part of the card starts and graded once the result is in.

Each bout gets one consistent breakdown: each fighter's chance to win, split into KO/TKO, submission and decision, and the chance it ends in each round. The win chance blends the model with the betting market (about 81% market, the weight that has predicted best on past fights) and corrects the market's habit of underrating heavy favorites. MMA is high-variance: even the most likely single result is usually well under 50%.

The fair odds are the American odds that match the win chance with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook only offers value on a fighter when its price beats the fair line.

The three edge columns value every side of each market at its posted price: expected value (EV) is the average profit per $1 staked, from the final prediction: the win chance blended with the moneyline (which corrects the market's habit of underrating heavy favorites), and method and round chances anchored to their own props, moved only by what the blend changes. A side is an edge when its EV is at least 3%; each cell names the best side if one clears that bar, with its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, at most 3 units on one bout; else "no edge". Moneylines and props are never priced near -110, so a missing price is never assumed: without one, the round-total cell shows the model's fair odds at the line closest to even and the method cell each fighter's fair KO/TKO, submission and decision odds. Over 1.5 rounds means the fight passes 2:30 of round 2 (a decision is always over); finishes are assumed spread evenly within a round.

See the backtest (backtest.md) for how these edges did against the dataset's closing prices, next to the model alone, which finds a 3% edge in most fights and lost money on them. Treat these columns as a live test, tracked below, not as betting advice.

## UFC Fight Night: Moicano vs. Nolan

Saturday, October 31, 2026 · first bout locks Sat Oct 31, 5:00 PM ET

| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | Most likely result | Moneyline edge | Round total edge | Method edge |
|---|---|---|---|---|---|---|---|---|---|---|
| **Renato Moicano** vs. **Tom Nolan**<br>LW, 5 rds | Moicano 45% – 55% Nolan | +125 / -125 | Moicano 47% (+102 / -122) | Moicano 40% (+150) | Moicano 18% / 11% / 16%<br>Nolan 23% / 14% / 19% | 35% | Nolan by KO/TKO (23%) | no edge | no price yet; fair Over 2.5 -105, Under +105 | no prices yet; fair KO / Sub / Dec<br>Moicano +470 / +775 / +530<br>Nolan +345 / +625 / +430 |
| **Ode' Osbourne** vs. **Cody Durden**<br>FLW, 3 rds | Osbourne 52% – 48% Durden | -110 / +110 | Osbourne 53% (-125 / +105) | Osbourne 45% (+120) | Osbourne 15% / 17% / 21%<br>Durden 8% / 16% / 24% | 45% | Durden by decision (24%) | no edge | no price yet; fair Over 2.5 +105, Under -105 | no prices yet; fair KO / Sub / Dec<br>Osbourne +580 / +500 / +380<br>Durden +1180 / +535 / +315 |
| **Yana Santos** vs. **Luana Santos**<br>W-BW, 3 rds | Santos 26% – 74% Santos | +285 / -285 | Santos 34% (+185 / -225) | Santos 20% (+410) | Santos 3% / 1% / 22%<br>Santos 9% / 17% / 48% | 70% | Santos by decision (48%) | Santos (-225): EV +6.7%, 74%, stake 3.0u | no price yet; fair Over 2.5 -260, Under +260 | no prices yet; fair KO / Sub / Dec<br>Santos +3105 / +6575 / +365<br>Santos +1045 / +485 / +110 |
| **Jean-Paul Lebosnoyani** vs. **Farman Hasanov**<br>WW, 3 rds | Lebosnoyani 71% – 29% Hasanov | -245 / +245 | Lebosnoyani 68% (-245 / +200) | Lebosnoyani 62% (-165) | Lebosnoyani 17% / 16% / 38%<br>Hasanov 4% / 5% / 20% | 58% | Lebosnoyani by decision (38%) | no edge | no price yet; fair Over 2.5 -160, Under +160 | no prices yet; fair KO / Sub / Dec<br>Lebosnoyani +485 / +535 / +160<br>Hasanov +2335 / +1950 / +405 |
| **Francis Marshall** vs. **Dakota Hope**<br>FW, 3 rds | Marshall 71% – 29% Hope | -240 / +240 | Marshall 67% (-230 / +190) | Marshall 66% (-190) | Marshall 20% / 11% / 39%<br>Hope 10% / 2% / 18% | 57% | Marshall by decision (39%) | no edge | no price yet; fair Over 2.5 -150, Under +150 | no prices yet; fair KO / Sub / Dec<br>Marshall +390 / +775 / +155<br>Hope +935 / +4960 / +465 |
| **Azamat Bekoev** vs. **Andre Petroski**<br>MW, 3 rds | Bekoev 41% – 59% Petroski | +145 / -145 | no line yet | Bekoev 41% (+145) | Bekoev 20% / 5% / 16%<br>Petroski 19% / 20% / 20% | 36% | Petroski by decision (20%) | no line yet | no price yet; fair Over 1.5 -125, Under +125 | no prices yet; fair KO / Sub / Dec<br>Bekoev +405 / +1865 / +530<br>Petroski +415 / +405 / +395 |
| **Rodrigo Sezinando** vs. **Theodor Berggren**<br>WW, 3 rds | Sezinando 60% – 40% Berggren | -150 / +150 | Sezinando 62% (-180 / +150) | Sezinando 41% (+145) | Sezinando 32% / 9% / 19%<br>Berggren 20% / 5% / 14% | 33% | Sezinando by KO/TKO (32%) | no edge | no price yet; fair Over 1.5 -110, Under +110 | no prices yet; fair KO / Sub / Dec<br>Sezinando +215 / +975 / +430<br>Berggren +395 / +1730 / +595 |
| **Julian Erosa** vs. **JeongYeong Lee**<br>FW, 3 rds | Erosa 37% – 63% Lee | +170 / -170 | Erosa 38% (+154 / -185) | Erosa 49% (+105) | Erosa 12% / 5% / 20%<br>Lee 26% / 7% / 31% | 51% | Lee by decision (31%) | no edge | no price yet; fair Over 2.5 -120, Under +120 | no prices yet; fair KO / Sub / Dec<br>Erosa +745 / +1765 / +400<br>Lee +290 / +1385 / +230 |
| **Nick Klein** vs. **Joe Kropschot**<br>MW, 3 rds, UFC debut: Kropschot | Klein 26% – 74% Kropschot | +285 / -285 | Klein 27% (+250 / -310) | Klein 46% (+115) | Klein 8% / 8% / 10%<br>Kropschot 36% / 17% / 21% | 31% | Kropschot by KO/TKO (36%) | no edge | no price yet; fair Over 1.5 -105, Under +105 | no prices yet; fair KO / Sub / Dec<br>Klein +1220 / +1125 / +860<br>Kropschot +175 / +490 / +380 |
| **Talita Alencar** vs. **Piera Rodriguez**<br>W-SW, 3 rds | Alencar 29% – 71% Rodriguez | +245 / -245 | Alencar 31% (+210 / -258) | Alencar 42% (+135) | Alencar 2% / 4% / 22%<br>Rodriguez 6% / 6% / 60% | 82% | Rodriguez by decision (60%) | no edge | no price yet; fair Over 2.5 -525, Under +525 | no prices yet; fair KO / Sub / Dec<br>Alencar +4685 / +2135 / +350<br>Rodriguez +1665 / +1705 / -150 |
| **Randy Brown** vs. **Jacobe Smith**<br>WW, 3 rds | Brown 28% – 72% Smith | +260 / -260 | no line yet | Brown 28% (+260) | Brown 9% / 3% / 16%<br>Smith 27% / 13% / 32% | 48% | Smith by decision (32%) | no line yet | no price yet; fair Over 2.5 -110, Under +110 | no prices yet; fair KO / Sub / Dec<br>Brown +985 / +3785 / +520<br>Smith +270 / +645 / +215 |
| **Lucia Szabová** vs. **Tainara Lisboa**<br>W-FLW, 3 rds, UFC debut: Szabová | Szabová 84% – 16% Lisboa | -535 / +535 | Szabová 81% (-550 / +410) | Szabová 67% (-205) | Szabová 14% / 24% / 46%<br>Lisboa 2% / 3% / 11% | 57% | Szabová by decision (46%) | no edge | no price yet; fair Over 2.5 -155, Under +155 | no prices yet; fair KO / Sub / Dec<br>Szabová +630 / +310 / +115<br>Lisboa +5460 / +3290 / +810 |
| **Zach Reese** vs. **Mickey Gall**<br>MW, 3 rds | Reese 70% – 30% Gall | -235 / +235 | no line yet | Reese 70% (-235) | Reese 31% / 17% / 23%<br>Gall 12% / 7% / 11% | 34% | Reese by KO/TKO (31%) | no line yet | no price yet; fair Over 1.5 -115, Under +115 | no prices yet; fair KO / Sub / Dec<br>Reese +225 / +500 / +340<br>Gall +705 / +1405 / +825 |

When it ends (either fighter):

| Bout | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Decision |
|---|---|---|---|---|---|---|
| Moicano vs. Nolan | 24% | 18% | 11% | 6% | 5% | 35% |
| Osbourne vs. Durden | 29% | 18% | 9% |  |  | 45% |
| Santos vs. Santos | 14% | 10% | 6% |  |  | 70% |
| Lebosnoyani vs. Hasanov | 21% | 14% | 7% |  |  | 58% |
| Marshall vs. Hope | 22% | 14% | 7% |  |  | 57% |
| Bekoev vs. Petroski | 35% | 20% | 9% |  |  | 36% |
| Sezinando vs. Berggren | 37% | 20% | 9% |  |  | 33% |
| Erosa vs. Lee | 25% | 16% | 8% |  |  | 51% |
| Klein vs. Kropschot | 39% | 21% | 9% |  |  | 31% |
| Alencar vs. Rodriguez | 8% | 6% | 3% |  |  | 82% |
| Brown vs. Smith | 27% | 17% | 8% |  |  | 48% |
| Szabová vs. Lisboa | 21% | 14% | 7% |  |  | 57% |
| Reese vs. Gall | 37% | 20% | 9% |  |  | 34% |

## UFC Fight Night: Bonfim vs. Brady

Saturday, November 07, 2026 · first bout locks Sat Nov 7, 5:00 PM ET

| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | Most likely result | Moneyline edge | Round total edge | Method edge |
|---|---|---|---|---|---|---|---|---|---|---|
| **Gabriel Bonfim** vs. **Sean Brady**<br>WW, 5 rds | Bonfim 50% – 50% Brady | +100 / -100 | no line yet | Bonfim 50% (+100) | Bonfim 17% / 10% / 23%<br>Brady 12% / 12% / 27% | 50% | Brady by decision (27%) | no line yet | no price yet; fair Over 4.5 -110, Under +110 | no prices yet; fair KO / Sub / Dec<br>Bonfim +495 / +880 / +335<br>Brady +750 / +760 / +275 |
| **Tatiana Suarez** vs. **Virna Jandiroba**<br>W-SW, 3 rds | Suarez 65% – 35% Jandiroba | -185 / +185 | no line yet | Suarez 65% (-185) | Suarez 4% / 16% / 46%<br>Jandiroba 2% / 8% / 25% | 70% | Suarez by decision (46%) | no line yet | no price yet; fair Over 2.5 -270, Under +270 | no prices yet; fair KO / Sub / Dec<br>Suarez +2730 / +530 / +120<br>Jandiroba +5120 / +1095 / +305 |
| **Davey Grant** vs. **Elijah Smith**<br>BW, 3 rds | Grant 18% – 82% Smith | +470 / -470 | no line yet | Grant 18% (+470) | Grant 5% / 1% / 12%<br>Smith 21% / 22% / 40% | 51% | Smith by decision (40%) | no line yet | no price yet; fair Over 2.5 -125, Under +125 | no prices yet; fair KO / Sub / Dec<br>Grant +2100 / +6970 / +765<br>Smith +370 / +365 / +150 |
| **Seokhyeon Ko** vs. **Wellington Turman**<br>WW, 3 rds | Ko 79% – 21% Turman | -375 / +375 | no line yet | Ko 79% (-375) | Ko 20% / 18% / 41%<br>Turman 5% / 4% / 12% | 53% | Ko by decision (41%) | no line yet | no price yet; fair Over 2.5 -130, Under +130 | no prices yet; fair KO / Sub / Dec<br>Ko +400 / +460 / +145<br>Turman +1760 / +2490 / +745 |
| **Billy Elekana** vs. **Lucas Fernando**<br>LHW, 3 rds | Elekana 42% – 58% Fernando | +140 / -140 | no line yet | Elekana 42% (+140) | Elekana 17% / 11% / 14%<br>Fernando 37% / 5% / 15% | 30% | Fernando by KO/TKO (37%) | no line yet | no price yet; fair Over 1.5 +100, Under -100 | no prices yet; fair KO / Sub / Dec<br>Elekana +505 / +790 / +610<br>Fernando +170 / +1765 / +550 |
| **Mantas Kondratavičius** vs. **Wes Schultz**<br>MW, 3 rds | Kondratavičius 74% – 26% Schultz | -280 / +280 | no line yet | Kondratavičius 74% (-280) | Kondratavičius 46% / 10% / 18%<br>Schultz 8% / 13% / 5% | 23% | Kondratavičius by KO/TKO (46%) | no line yet | no price yet; fair Over 1.5 +130, Under -130 | no prices yet; fair KO / Sub / Dec<br>Kondratavičius +120 / +920 / +450<br>Schultz +1190 / +655 / +1790 |
| **Gabriel Lorenço** vs. **Alvin Hines**<br>HW, 3 rds, UFC debut: Lorenço | Lorenço 70% – 30% Hines | -230 / +230 | no line yet | Lorenço 70% (-230) | Lorenço 44% / 8% / 18%<br>Hines 16% / 4% / 11% | 29% | Lorenço by KO/TKO (44%) | no line yet | no price yet; fair Over 1.5 +105, Under -105 | no prices yet; fair KO / Sub / Dec<br>Lorenço +130 / +1110 / +465<br>Hines +525 / +2740 / +805 |
| **Karine Silva** vs. **Gabriella Fernandes**<br>W-FLW, 3 rds | Silva 69% – 31% Fernandes | -220 / +220 | no line yet | Silva 69% (-220) | Silva 9% / 21% / 39%<br>Fernandes 4% / 4% / 23% | 62% | Silva by decision (39%) | no line yet | no price yet; fair Over 2.5 -190, Under +190 | no prices yet; fair KO / Sub / Dec<br>Silva +1010 / +385 / +155<br>Fernandes +2505 / +2230 / +330 |
| **Jose Delano** vs. **Murtazali Magomedov**<br>FW, 3 rds | Delano 46% – 54% Magomedov | +115 / -115 | no line yet | Delano 46% (+115) | Delano 15% / 3% / 28%<br>Magomedov 12% / 19% / 23% | 51% | Delano by decision (28%) | no line yet | no price yet; fair Over 2.5 -120, Under +120 | no prices yet; fair KO / Sub / Dec<br>Delano +580 / +2890 / +255<br>Magomedov +725 / +430 / +340 |
| **Keiichiro Nakamura** vs. **Ollie Schmid**<br>FW, 3 rds | Nakamura 60% – 40% Schmid | -150 / +150 | no line yet | Nakamura 60% (-150) | Nakamura 34% / 6% / 21%<br>Schmid 12% / 6% / 22% | 43% | Nakamura by KO/TKO (34%) | no line yet | no price yet; fair Over 2.5 +110, Under -110 | no prices yet; fair KO / Sub / Dec<br>Nakamura +200 / +1650 / +375<br>Schmid +720 / +1645 / +360 |
| **Austin Bashi** vs. **Lucas Brennan**<br>FW, 3 rds | Bashi 66% – 34% Brennan | -195 / +195 | no line yet | Bashi 66% (-195) | Bashi 15% / 19% / 32%<br>Brennan 9% / 6% / 19% | 51% | Bashi by decision (32%) | no line yet | no price yet; fair Over 2.5 -120, Under +120 | no prices yet; fair KO / Sub / Dec<br>Bashi +560 / +435 / +210<br>Brennan +1015 / +1500 / +430 |
| **Priscila Cachoeira** vs. **Nina Milošević**<br>W-BW, 3 rds | Cachoeira 13% – 87% Milošević | +665 / -665 | no line yet | Cachoeira 13% (+665) | Cachoeira 2% / 1% / 9%<br>Milošević 30% / 15% / 42% | 51% | Milošević by decision (42%) | no line yet | no price yet; fair Over 2.5 -125, Under +125 | no prices yet; fair KO / Sub / Dec<br>Cachoeira +3930 / +7830 / +975<br>Milošević +230 / +580 / +140 |
| **Jonny Parsons** vs. **Jose Henrique**<br>WW, 3 rds, UFC debut: Henrique | Parsons 51% – 49% Henrique | -100 / +100 | no line yet | Parsons 51% (-100) | Parsons 24% / 5% / 21%<br>Henrique 17% / 8% / 25% | 46% | Henrique by decision (25%) | no line yet | no price yet; fair Over 2.5 -100, Under +100 | no prices yet; fair KO / Sub / Dec<br>Parsons +310 / +1990 / +370<br>Henrique +505 / +1130 / +305 |

When it ends (either fighter):

| Bout | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Decision |
|---|---|---|---|---|---|---|
| Bonfim vs. Brady | 17% | 14% | 9% | 5% | 5% | 50% |
| Suarez vs. Jandiroba | 14% | 10% | 5% |  |  | 70% |
| Grant vs. Smith | 25% | 16% | 8% |  |  | 51% |
| Ko vs. Turman | 24% | 16% | 8% |  |  | 53% |
| Elekana vs. Fernando | 40% | 21% | 9% |  |  | 30% |
| Kondratavičius vs. Schultz | 45% | 22% | 9% |  |  | 23% |
| Lorenço vs. Hines | 41% | 21% | 9% |  |  | 29% |
| Silva vs. Fernandes | 18% | 13% | 7% |  |  | 62% |
| Delano vs. Magomedov | 25% | 16% | 8% |  |  | 51% |
| Nakamura vs. Schmid | 30% | 18% | 9% |  |  | 43% |
| Bashi vs. Brennan | 25% | 16% | 8% |  |  | 51% |
| Cachoeira vs. Milošević | 25% | 16% | 8% |  |  | 51% |
| Parsons vs. Henrique | 28% | 17% | 9% |  |  | 46% |

## How the 2026 predictions have done

| Predictor | Fights | Log loss | Brier | Winners |
|---|---|---|---|---|
| Final prediction | 449 | 0.6208 | 0.216 | 63.9% |
| Model alone (before the market) | 449 | 0.6372 | 0.223 | 62.4% |
| Glicko-2 rating alone | 449 | 0.6818 | 0.244 | 57.5% |
| Final, on fights with a price | 114 | 0.5091 | 0.169 | 76.3% |
| Market price when predicted | 114 | 0.5216 | 0.172 | 75.4% |
| Coin flip | 449 | 0.6931 | 0.250 | – |

Log loss scores the win chances (lower is better; a coin flip scores 0.693, and the betting market about 0.61). Brier is the squared error of the win chance. Picking every betting favorite already gets about two thirds of winners right, so the win rate says little on its own.

- Winner and method (six outcomes): log loss 1.585 on 448 fights, against 1.792 for guessing uniformly. The single most likely result happened 33% of the time.
- Went the distance: predicted 48% on average, actual 41%.

449 of these fights happened before the predictor went live. They are backfilled walk-forward (each fight predicted from earlier fights only, with models fitted on earlier years) using the odds dataset's approximate closing prices, which run only through March 2026, so later backfilled fights use the model alone. Every fight since is graded on the prediction logged before it started.

### Edge record

Every edge logged with a live prediction (the last one before the fight), at the stake and price logged with it; edges logged before edges were priced from the final prediction are left out. Pushes return the stake (a no contest voids every bet; a draw refunds the moneyline). Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised.

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Moneyline | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Round total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Method of victory | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

### Latest results: UFC Fight Night: Buckley vs. Malott

| Bout | Predicted | Result | Chance given to the winner | Chance given to the exact result |
|---|---|---|---|---|
| Joaquin Buckley vs. Mike Malott | Buckley 50% | Mike Malott by KO/TKO, R2 | 50% | 24% |
| Erin Blanchfield vs. Jasmine Jasudavicius | Blanchfield 77% | Jasmine Jasudavicius by decision | 23% | 18% |
| Kyle Nelson vs. Cristian Perez | Perez 53% | Cristian Perez by KO/TKO, R1 | 53% | 19% |
| Marc-Andre Barriault vs. Kyle Daukaus | Daukaus 64% | Marc-Andre Barriault by KO/TKO, R1 | 36% | 20% |
| Louis Jourdain vs. Timmy Cuamba | Cuamba 59% | Timmy Cuamba by submission, R2 | 59% | 9% |
| Mandel Nallo vs. Nate Landwehr | Landwehr 60% | Mandel Nallo by KO/TKO, R2 | 40% | 25% |
| Tanner Boser vs. Jhonata Diniz | Boser 54% | Tanner Boser by KO/TKO, R3 | 54% | 30% |
| Julien Leblanc vs. Nick Galanti | Galanti 65% | Nick Galanti by submission, R1 | 65% | 23% |
| Javad Mahjoub vs. Joel Faglier | Faglier 63% | Joel Faglier by KO/TKO, R2 | 63% | 32% |
| Katlyn Cerminara vs. Mackenzie Stiller | Stiller 57% | Katlyn Cerminara by KO/TKO, R1 | 43% | 6% |
| Chad Anheliger vs. Steven Koslow | Koslow 68% | Steven Koslow by submission, R3 | 68% | 22% |
| Melissa Croden vs. Chelsea Chandler | Croden 73% | Chelsea Chandler by submission, R1 | 27% | 3% |
| Cody Chovancek vs. SuYoung You | You 64% | SuYoung You by submission, R3 | 64% | 10% |

14 locked predictions are waiting for official results.

## Top fighters by division

Glicko-2 rating from UFC results, with finishes counting as clearer wins than decisions. ± is two rating deviations (fighters with few or old fights are less certain), and the ranking uses the rating minus that margin so an unproven fighter does not top a division on one big win. Active fighters only (a fight in the last two years).

| Division | # | Fighter | Rating | ± | UFC record | Last fight |
|---|---|---|---|---|---|---|
| Flyweight | 1 | Manel Kape | 1978 | 283 | 8-3 | 2026-06-20 |
|  | 2 | Joshua Van | 1942 | 260 | 11-1 | 2026-09-19 |
|  | 3 | Brandon Moreno | 1895 | 237 | 12-7-2 | 2026-09-12 |
|  | 4 | Alexandre Pantoja | 1894 | 237 | 14-5 | 2026-09-19 |
|  | 5 | Tatsuro Taira | 1963 | 318 | 8-2 | 2026-05-09 |
| Bantamweight | 1 | Merab Dvalishvili | 2150 | 235 | 14-3 | 2025-12-06 |
|  | 2 | Petr Yan | 2123 | 239 | 12-4 | 2025-12-06 |
|  | 3 | Song Yadong | 2064 | 225 | 13-4-1 | 2026-08-29 |
|  | 4 | Cory Sandhagen | 2059 | 231 | 11-6 | 2026-07-11 |
|  | 5 | Sean O'Malley | 2059 | 244 | 12-3 | 2026-06-14 |
| Featherweight | 1 | Alexander Volkanovski | 2192 | 234 | 15-3 | 2026-01-31 |
|  | 2 | Diego Lopes | 2145 | 267 | 7-3 | 2026-06-14 |
|  | 3 | Aljamain Sterling | 2097 | 228 | 18-5 | 2026-04-25 |
|  | 4 | Brian Ortega | 2062 | 272 | 8-5 | 2025-08-23 |
|  | 5 | Jean Silva | 2075 | 301 | 7-1 | 2026-09-12 |
| Lightweight | 1 | Ilia Topuria | 2274 | 296 | 9-1 | 2026-06-14 |
|  | 2 | Justin Gaethje | 2193 | 239 | 11-5 | 2026-06-14 |
|  | 3 | Charles Oliveira | 2146 | 211 | 25-11 | 2026-03-07 |
|  | 4 | Arman Tsarukyan | 2148 | 267 | 11-2 | 2026-09-19 |
|  | 5 | Dustin Poirier | 2096 | 229 | 22-9 | 2025-07-19 |
| Welterweight | 1 | Islam Makhachev | 2278 | 233 | 18-1 | 2026-08-15 |
|  | 2 | Shavkat Rakhmonov | 2401 | 407 | 7-0 | 2024-12-07 |
|  | 3 | Max Holloway | 2190 | 211 | 24-9 | 2026-07-11 |
|  | 4 | Carlos Prates | 2236 | 282 | 7-1 | 2026-05-02 |
|  | 5 | Michael Morales | 2245 | 322 | 7-0 | 2025-11-15 |
| Middleweight | 1 | Dricus Du Plessis | 2231 | 253 | 10-1 | 2026-07-18 |
|  | 2 | Khamzat Chimaev | 2255 | 277 | 9-1 | 2026-05-09 |
|  | 3 | Kamaru Usman | 2181 | 240 | 16-4 | 2026-07-18 |
|  | 4 | Nassourdine Imavov | 2173 | 277 | 9-2 | 2025-09-06 |
|  | 5 | Brendan Allen | 2123 | 228 | 16-4 | 2026-10-10 |
| Light Heavyweight | 1 | Magomed Ankalaev | 2188 | 241 | 13-2-1 | 2026-07-25 |
|  | 2 | Robert Whittaker | 2156 | 230 | 18-7 | 2026-07-11 |
|  | 3 | Carlos Ulberg | 2126 | 273 | 10-1 | 2026-04-11 |
|  | 4 | Jiri Prochazka | 2174 | 329 | 6-3 | 2026-04-11 |
|  | 5 | Paulo Costa | 2107 | 268 | 8-4 | 2026-04-11 |
| Heavyweight | 1 | Jon Jones | 2438 | 281 | 22-1 | 2024-11-16 |
|  | 2 | Ciryl Gane | 2336 | 272 | 11-2 | 2026-06-14 |
|  | 3 | Stipe Miocic | 2319 | 278 | 14-5 | 2024-11-16 |
|  | 4 | Alex Pereira | 2268 | 254 | 10-3 | 2026-06-14 |
|  | 5 | Alexander Volkov | 2221 | 237 | 14-5 | 2026-05-09 |
| Women's Strawweight | 1 | Tatiana Suarez | 2011 | 315 | 9-1 | 2026-04-11 |
|  | 2 | Virna Jandiroba | 1841 | 252 | 9-4 | 2026-04-04 |
|  | 3 | Mackenzie Dern | 1797 | 230 | 12-5 | 2026-08-15 |
|  | 4 | Gillian Robertson | 1785 | 231 | 14-7 | 2026-08-15 |
|  | 5 | Jessica Andrade | 1753 | 220 | 17-13 | 2025-08-16 |
| Women's Flyweight | 1 | Valentina Shevchenko | 1998 | 255 | 15-3-1 | 2025-11-15 |
|  | 2 | Zhang Weili | 1981 | 258 | 10-3 | 2025-11-15 |
|  | 3 | Erin Blanchfield | 1984 | 285 | 8-2 | 2026-10-17 |
|  | 4 | Natalia Silva | 2007 | 311 | 9-0 | 2026-10-03 |
|  | 5 | Manon Fiorot | 1961 | 288 | 8-2 | 2026-09-12 |
| Women's Bantamweight | 1 | Kayla Harrison | 2075 | 468 | 3-0 | 2025-06-07 |
|  | 2 | Ketlen Vieira | 1773 | 250 | 10-5 | 2026-05-16 |
|  | 3 | Julianna Pena | 1821 | 306 | 8-4 | 2025-06-07 |
|  | 4 | Norma Dumont | 1743 | 260 | 9-4 | 2026-09-26 |
|  | 5 | Luana Santos | 1827 | 352 | 6-1 | 2026-06-20 |

## Current model fit

- Fitted on 5330 fights from 2016–2026.
- Market blend: 81% weight on the de-vigged price, total slope 1.28 (above 1 stretches favorites, correcting the favorite-longshot bias). Without a price: slope 1.02 on the model alone.
- Strongest win-model inputs (log-odds per standard deviation, A minus B): age -0.28, glicko_logit +0.21, strike_matchup +0.18, debut -0.12, age_decline -0.11, sapm -0.09.
