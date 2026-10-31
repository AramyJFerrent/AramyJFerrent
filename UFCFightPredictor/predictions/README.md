# UFC fight predictions

Updated Sat Oct 31, 2026 03:57 PM ET. Refreshed automatically every day and several times on fight week; each bout's prediction is locked when its part of the card starts and graded once the result is in.

Each bout gets one consistent breakdown: each fighter's chance to win, split into KO/TKO, submission and decision, and the chance it ends in each round. The win chance blends the model with the betting market (about 81% market, the weight that has predicted best on past fights) and corrects the market's habit of underrating heavy favorites. MMA is high-variance: even the most likely single result is usually well under 50%.

The fair odds are the American odds that match the win chance with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook only offers value on a fighter when its price beats the fair line.

The three edge columns value every side of each market at its posted price: expected value (EV) is the average profit per $1 staked, from the final prediction: the win chance blended with the moneyline (which corrects the market's habit of underrating heavy favorites), and method and round chances anchored to their own props, moved only by what the blend changes. A side is an edge when its EV is at least 3%; each cell names the best side if one clears that bar, with its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, at most 3 units on one bout; else "no edge". Moneylines and props are never priced near -110, so a missing price is never assumed: without one, the round-total cell shows the model's fair odds at the line closest to even and the method cell each fighter's fair KO/TKO, submission and decision odds. Over 1.5 rounds means the fight passes 2:30 of round 2 (a decision is always over); finishes are assumed spread evenly within a round.

See the backtest (backtest.md) for how these edges did against the dataset's closing prices, next to the model alone, which finds a 3% edge in most fights and lost money on them. Treat these columns as a live test, tracked below, not as betting advice.

## UFC Fight Night: Moicano vs. Nolan

Saturday, October 31, 2026 · first bout locks Sat Oct 31, 5:00 PM ET

| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | Most likely result | Moneyline edge | Round total edge | Method edge |
|---|---|---|---|---|---|---|---|---|---|---|
| **Renato Moicano** vs. **Tom Nolan**<br>LW, 5 rds | Moicano 50% – 50% Nolan | +100 / -100 | Moicano 52% (-120 / +100) | Moicano 40% (+150) | Moicano 19% / 13% / 17%<br>Nolan 21% / 12% / 17% | 35% | Nolan by KO/TKO (21%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Moicano +415 / +675 / +475<br>Nolan +390 / +705 / +480 |
| **Randy Brown** vs. **Jacobe Smith**<br>WW, 3 rds | Brown 25% – 75% Smith | +300 / -300 | Brown 30% (+220 / -270) | Brown 28% (+255) | Brown 8% / 2% / 14%<br>Smith 28% / 14% / 33% | 47% | Smith by decision (33%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Brown +1115 / +4285 / +590<br>Smith +255 / +610 / +205 |
| **Ode' Osbourne** vs. **Cody Durden**<br>FLW, 3 rds | Osbourne 47% – 53% Durden | +115 / -115 | Osbourne 48% (-102 / -120) | Osbourne 45% (+120) | Osbourne 13% / 15% / 19%<br>Durden 9% / 18% / 27% | 45% | Durden by decision (27%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Osbourne +650 / +580 / +430<br>Durden +1045 / +465 / +275 |
| **Yana Santos** vs. **Luana Santos**<br>W-BW, 3 rds | Santos 20% – 80% Santos | +410 / -410 | Santos 26% (+270 / -340) | Santos 20% (+405) | Santos 2% / 1% / 16%<br>Santos 10% / 19% / 52% | 68% | Santos by decision (52%) | Santos (-340): EV +4.2%, 80%, stake 3.0u | no edge | no prices yet; fair KO / Sub / Dec<br>Santos +4220 / +9150 / +520<br>Santos +950 / +420 / -110 |
| **Jean-Paul Lebosnoyani** vs. **Farman Hasanov**<br>WW, 3 rds | Lebosnoyani 75% – 25% Hasanov | -295 / +295 | Lebosnoyani 72% (-298 / +240) | Lebosnoyani 62% (-165) | Lebosnoyani 18% / 17% / 40%<br>Hasanov 4% / 4% / 17% | 58% | Lebosnoyani by decision (40%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Lebosnoyani +455 / +500 / +150<br>Hasanov +2695 / +2290 / +475 |
| **Francis Marshall** vs. **Dakota Hope**<br>FW, 3 rds | Marshall 68% – 32% Hope | -215 / +215 | Marshall 64% (-205 / +170) | Marshall 66% (-190) | Marshall 20% / 11% / 38%<br>Hope 11% / 2% / 19% | 57% | Marshall by decision (38%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Marshall +405 / +815 / +165<br>Hope +845 / +4575 / +430 |
| **Rodrigo Sezinando** vs. **Theodor Berggren**<br>WW, 3 rds | Sezinando 61% – 39% Berggren | -160 / +160 | Sezinando 63% (-192 / +160) | Sezinando 41% (+145) | Sezinando 33% / 10% / 19%<br>Berggren 19% / 5% / 14% | 33% | Sezinando by KO/TKO (33%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Sezinando +205 / +945 / +415<br>Berggren +415 / +1810 / +615 |
| **Julian Erosa** vs. **JeongYeong Lee**<br>FW, 3 rds | Erosa 42% – 58% Lee | +140 / -140 | Erosa 42% (+130 / -148) | Erosa 49% (+105) | Erosa 13% / 6% / 22%<br>Lee 24% / 6% / 28% | 51% | Lee by decision (28%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Erosa +650 / +1550 / +350<br>Lee +320 / +1530 / +250 |
| **Zach Reese** vs. **Mickey Gall**<br>MW, 3 rds | Reese 82% – 18% Gall | -455 / +455 | Reese 78% (-440 / +340) | Reese 70% (-230) | Reese 36% / 20% / 26%<br>Gall 7% / 4% / 7% | 33% | Reese by KO/TKO (36%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Reese +180 / +390 / +285<br>Gall +1235 / +2510 / +1410 |
| **Nick Klein** vs. **Joe Kropschot**<br>MW, 3 rds, UFC debut: Kropschot | Klein 26% – 74% Kropschot | +280 / -280 | Klein 27% (+250 / -310) | Klein 47% (+115) | Klein 8% / 8% / 10%<br>Kropschot 36% / 17% / 21% | 31% | Kropschot by KO/TKO (36%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Klein +1220 / +1120 / +860<br>Kropschot +180 / +485 / +380 |
| **Talita Alencar** vs. **Piera Rodriguez**<br>W-SW, 3 rds | Alencar 27% – 73% Rodriguez | +270 / -270 | Alencar 29% (+230 / -285) | Alencar 42% (+140) | Alencar 2% / 4% / 21%<br>Rodriguez 6% / 6% / 62% | 82% | Rodriguez by decision (62%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Alencar +5070 / +2320 / +380<br>Rodriguez +1620 / +1650 / -160 |
| **Lucia Szabová** vs. **Tainara Lisboa**<br>W-FLW, 3 rds, UFC debut: Szabová | Szabová 87% – 13% Lisboa | -655 / +655 | Szabová 84% (-700 / +500) | Szabová 67% (-205) | Szabová 14% / 25% / 47%<br>Lisboa 2% / 2% / 9% | 56% | Szabová by decision (47%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Szabová +610 / +295 / +110<br>Lisboa +6520 / +3975 / +980 |

When it ends (either fighter):

| Bout | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Decision |
|---|---|---|---|---|---|---|
| Moicano vs. Nolan | 24% | 19% | 11% | 6% | 5% | 35% |
| Brown vs. Smith | 27% | 17% | 8% |  |  | 47% |
| Osbourne vs. Durden | 28% | 17% | 9% |  |  | 45% |
| Santos vs. Santos | 15% | 11% | 6% |  |  | 68% |
| Lebosnoyani vs. Hasanov | 21% | 14% | 7% |  |  | 58% |
| Marshall vs. Hope | 22% | 14% | 7% |  |  | 57% |
| Sezinando vs. Berggren | 37% | 20% | 9% |  |  | 33% |
| Erosa vs. Lee | 25% | 16% | 8% |  |  | 51% |
| Reese vs. Gall | 38% | 21% | 9% |  |  | 33% |
| Klein vs. Kropschot | 39% | 21% | 9% |  |  | 31% |
| Alencar vs. Rodriguez | 8% | 6% | 3% |  |  | 82% |
| Szabová vs. Lisboa | 22% | 14% | 7% |  |  | 56% |

## UFC Fight Night: Cortes Acosta vs. Walker

Saturday, November 07, 2026 · first bout locks Sat Nov 7, 5:00 PM ET

| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | Most likely result | Moneyline edge | Round total edge | Method edge |
|---|---|---|---|---|---|---|---|---|---|---|
| **Waldo Cortes Acosta** vs. **Johnny Walker**<br>HW, 5 rds | Acosta 65% – 35% Walker | -190 / +190 | Acosta 63% (-192 / +160) | Acosta 58% (-140) | Acosta 46% / 4% / 15%<br>Walker 22% / 2% / 10% | 25% | Acosta by KO/TKO (46%) | no edge | no price yet; fair Over 2.5 +135, Under -135 | no prices yet; fair KO / Sub / Dec<br>Acosta +115 / +2460 / +565<br>Walker +360 / +3940 / +860 |
| **Tatiana Suarez** vs. **Virna Jandiroba**<br>W-SW, 3 rds | Suarez 65% – 35% Jandiroba | -185 / +185 | Suarez 61% (-175 / +145) | Suarez 65% (-185) | Suarez 4% / 16% / 45%<br>Jandiroba 2% / 8% / 25% | 70% | Suarez by decision (45%) | no edge | no price yet; fair Over 2.5 -270, Under +270 | no prices yet; fair KO / Sub / Dec<br>Suarez +2740 / +535 / +120<br>Jandiroba +5085 / +1090 / +300 |
| **Davey Grant** vs. **Elijah Smith**<br>BW, 3 rds | Grant 26% – 74% Smith | +290 / -290 | Grant 34% (+185 / -225) | Grant 18% (+465) | Grant 7% / 2% / 17%<br>Smith 19% / 19% / 37% | 53% | Smith by decision (37%) | Smith (-225): EV +7.5%, 74%, stake 3.0u | no price yet; fair Over 2.5 -135, Under +135 | no prices yet; fair KO / Sub / Dec<br>Grant +1405 / +4595 / +495<br>Smith +420 / +435 / +175 |
| **Seokhyeon Ko** vs. **Wellington Turman**<br>WW, 3 rds | Ko 86% – 14% Turman | -620 / +620 | Ko 81% (-550 / +410) | Ko 79% (-370) | Ko 22% / 20% / 44%<br>Turman 4% / 2% / 8% | 52% | Ko by decision (44%) | no edge | no price yet; fair Over 2.5 -125, Under +125 | no prices yet; fair KO / Sub / Dec<br>Ko +360 / +395 / +125<br>Turman +2705 / +3950 / +1165 |
| **Billy Elekana** vs. **Lucas Fernando**<br>LHW, 3 rds | Elekana 29% – 71% Fernando | +245 / -245 | Elekana 31% (+210 / -258) | Elekana 42% (+135) | Elekana 12% / 7% / 10%<br>Fernando 46% / 7% / 18% | 28% | Fernando by KO/TKO (46%) | no edge | no price yet; fair Over 1.5 +105, Under -105 | no prices yet; fair KO / Sub / Dec<br>Elekana +770 / +1245 / +920<br>Fernando +120 / +1375 / +440 |
| **Mantas Kondratavičius** vs. **Andre Petroski**<br>MW, 3 rds | Kondratavičius 76% – 24% Petroski | -310 / +310 | Kondratavičius 71% (-278 / +225) | Kondratavičius 73% (-265) | Kondratavičius 38% / 10% / 28%<br>Petroski 6% / 5% / 13% | 41% | Kondratavičius by KO/TKO (38%) | no edge | no price yet; fair Over 2.5 +120, Under -120 | no prices yet; fair KO / Sub / Dec<br>Kondratavičius +165 / +940 / +260<br>Petroski +1440 / +1800 / +695 |
| **Karine Silva** vs. **Gabriella Fernandes**<br>W-FLW, 3 rds | Silva 64% – 36% Fernandes | -180 / +180 | Silva 59% (-162 / +136) | Silva 69% (-220) | Silva 8% / 19% / 37%<br>Fernandes 4% / 5% / 26% | 63% | Silva by decision (37%) | Silva (-162): EV +3.6%, 64%, stake 1.5u | no price yet; fair Over 2.5 -195, Under +195 | no prices yet; fair KO / Sub / Dec<br>Silva +1090 / +425 / +175<br>Fernandes +2145 / +1880 / +280 |
| **Mitch Raposo** vs. **Marcos Degli**<br>FLW, 3 rds, UFC debut: Degli | Raposo 33% – 67% Degli | +200 / -200 | Raposo 32% (+200 / -245) | Raposo 58% (-140) | Raposo 7% / 6% / 21%<br>Degli 14% / 14% / 39% | 60% | Degli by decision (39%) | no edge | no price yet; fair Over 2.5 -170, Under +170 | no prices yet; fair KO / Sub / Dec<br>Raposo +1405 / +1605 / +385<br>Degli +605 / +630 / +155 |
| **Jose Delano** vs. **Murtazali Magomedov**<br>FW, 3 rds | Delano 50% – 50% Magomedov | -100 / +100 | Delano 51% (-115 / -105) | Delano 46% (+115) | Delano 16% / 4% / 31%<br>Magomedov 11% / 17% / 21% | 52% | Delano by decision (31%) | no edge | no price yet; fair Over 2.5 -125, Under +125 | no prices yet; fair KO / Sub / Dec<br>Delano +525 / +2635 / +225<br>Magomedov +780 / +480 / +370 |
| **Keiichiro Nakamura** vs. **Ollie Schmid**<br>FW, 3 rds | Nakamura 77% – 23% Schmid | -340 / +340 | Nakamura 75% (-355 / +280) | Nakamura 60% (-150) | Nakamura 43% / 8% / 26%<br>Schmid 7% / 3% / 13% | 39% | Nakamura by KO/TKO (43%) | no edge | no price yet; fair Over 2.5 +130, Under -130 | no prices yet; fair KO / Sub / Dec<br>Nakamura +130 / +1195 / +280<br>Schmid +1320 / +3140 / +690 |
| **Austin Bashi** vs. **Lucas Brennan**<br>FW, 3 rds | Bashi 66% – 34% Brennan | -195 / +195 | no line yet | Bashi 66% (-195) | Bashi 15% / 19% / 32%<br>Brennan 9% / 6% / 19% | 51% | Bashi by decision (32%) | no line yet | no price yet; fair Over 2.5 -120, Under +120 | no prices yet; fair KO / Sub / Dec<br>Bashi +555 / +435 / +210<br>Brennan +1005 / +1500 / +435 |
| **Priscila Cachoeira** vs. **Nina Milošević**<br>W-BW, 3 rds | Cachoeira 14% – 86% Milošević | +600 / -600 | Cachoeira 21% (+350 / -455) | Cachoeira 13% (+655) | Cachoeira 3% / 1% / 10%<br>Milošević 30% / 14% / 42% | 52% | Milošević by decision (42%) | Milošević (-455): EV +4.6%, 86%, stake 3.0u | no price yet; fair Over 2.5 -125, Under +125 | no prices yet; fair KO / Sub / Dec<br>Cachoeira +3590 / +7090 / +885<br>Milošević +240 / +595 / +140 |
| **Jonny Parsons** vs. **Jose Henrique**<br>WW, 3 rds, UFC debut: Henrique | Parsons 39% – 61% Henrique | +155 / -155 | Parsons 39% (+145 / -175) | Parsons 51% (-100) | Parsons 19% / 4% / 17%<br>Henrique 21% / 10% / 30% | 47% | Henrique by decision (30%) | no edge | no price yet; fair Over 2.5 -105, Under +105 | no prices yet; fair KO / Sub / Dec<br>Parsons +435 / +2730 / +505<br>Henrique +385 / +860 / +230 |
| **Gabriel Lorenço** vs. **Thomas Petersen**<br>HW, 3 rds, UFC debut: Lorenço | Lorenço 37% – 63% Petersen | +170 / -170 | Lorenço 40% (+142 / -170) | Lorenço 39% (+160) | Lorenço 19% / 6% / 12%<br>Petersen 27% / 9% / 27% | 39% | Petersen by decision (27%) | no edge | no price yet; fair Over 2.5 +130, Under -130 | no prices yet; fair KO / Sub / Dec<br>Lorenço +415 / +1680 / +755<br>Petersen +275 / +990 / +265 |

When it ends (either fighter):

| Bout | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Decision |
|---|---|---|---|---|---|---|
| Acosta vs. Walker | 30% | 21% | 12% | 6% | 5% | 25% |
| Suarez vs. Jandiroba | 14% | 10% | 5% |  |  | 70% |
| Grant vs. Smith | 24% | 15% | 8% |  |  | 53% |
| Ko vs. Turman | 24% | 16% | 8% |  |  | 52% |
| Elekana vs. Fernando | 41% | 21% | 9% |  |  | 28% |
| Kondratavičius vs. Petroski | 32% | 19% | 9% |  |  | 41% |
| Silva vs. Fernandes | 18% | 12% | 7% |  |  | 63% |
| Raposo vs. Degli | 20% | 13% | 7% |  |  | 60% |
| Delano vs. Magomedov | 24% | 16% | 8% |  |  | 52% |
| Nakamura vs. Schmid | 33% | 19% | 9% |  |  | 39% |
| Bashi vs. Brennan | 25% | 16% | 8% |  |  | 51% |
| Cachoeira vs. Milošević | 24% | 16% | 8% |  |  | 52% |
| Parsons vs. Henrique | 28% | 17% | 8% |  |  | 47% |
| Lorenço vs. Petersen | 33% | 19% | 9% |  |  | 39% |

## UFC 334: Gane vs. Hokit

Saturday, November 14, 2026 · first bout locks Sat Nov 14, 5:00 PM ET

| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | Most likely result | Moneyline edge | Round total edge | Method edge |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ciryl Gane** vs. **Josh Hokit**<br>HW, title, 5 rds | Gane 72% – 28% Hokit | -260 / +260 | Gane 70% (-265 / +215) | Gane 61% (-160) | Gane 49% / 5% / 18%<br>Hokit 21% / 1% / 6% | 24% | Gane by KO/TKO (49%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Gane +105 / +1755 / +455<br>Hokit +380 / +9900 / +1595 |
| **Kayla Harrison** vs. **Amanda Nunes**<br>W-BW, title, 5 rds | Harrison 67% – 33% Nunes | -200 / +200 | Harrison 63% (-192 / +160) | Harrison 65% (-185) | Harrison 8% / 23% / 35%<br>Nunes 6% / 5% / 22% | 57% | Harrison by decision (35%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Harrison +1125 / +330 / +180<br>Nunes +1485 / +1830 / +360 |
| **Caio Borralho** vs. **Yousri Belgaroui**<br>MW, 3 rds | Borralho 55% – 45% Belgaroui | -120 / +120 | Borralho 57% (-148 / +124) | Borralho 39% (+155) | Borralho 18% / 7% / 30%<br>Belgaroui 24% / 3% / 19% | 49% | Borralho by decision (30%) | no edge | no price yet; fair Over 2.5 -115, Under +115 | no prices yet; fair KO / Sub / Dec<br>Borralho +450 / +1410 / +230<br>Belgaroui +325 / +3675 / +430 |
| **Uroš Medić** vs. **Kevin Holland**<br>WW, 3 rds | Medić 58% – 42% Holland | -135 / +135 | Medić 59% (-162 / +136) | Medić 42% (+135) | Medić 38% / 2% / 18%<br>Holland 17% / 7% / 18% | 36% | Medić by KO/TKO (38%) | no edge | no price yet; fair Over 1.5 -120, Under +120 | no prices yet; fair KO / Sub / Dec<br>Medić +165 / +4570 / +460<br>Holland +490 / +1285 / +460 |
| **Bilal Hasan** vs. **Luis Gurule**<br>FLW, 3 rds | Hasan 91% – 9% Gurule | -995 / +995 | Hasan 87% (-950 / +625) | Hasan 82% (-445) | Hasan 35% / 17% / 39%<br>Gurule 2% / 1% / 6% | 45% | Hasan by decision (39%) | no edge | no price yet; fair Over 2.5 +105, Under -105 | no prices yet; fair KO / Sub / Dec<br>Hasan +185 / +500 / +155<br>Gurule +4295 / +7580 / +1700 |
| **Stephen Thompson** vs. **Charles Radtke**<br>WW, 3 rds | Thompson 35% – 65% Radtke | +185 / -185 | no line yet | Thompson 35% (+185) | Thompson 14% / 3% / 18%<br>Radtke 19% / 16% / 31% | 48% | Radtke by decision (31%) | no line yet | no price yet; fair Over 2.5 -110, Under +110 | no prices yet; fair KO / Sub / Dec<br>Thompson +620 / +2970 / +465<br>Radtke +425 / +545 / +225 |
| **Drew Dober** vs. **Chris Duncan**<br>LW, 3 rds | Dober 32% – 68% Duncan | +210 / -210 | no line yet | Dober 32% (+210) | Dober 15% / 4% / 13%<br>Duncan 21% / 17% / 30% | 43% | Duncan by decision (30%) | no line yet | no price yet; fair Over 2.5 +110, Under -110 | no prices yet; fair KO / Sub / Dec<br>Dober +585 / +2165 / +655<br>Duncan +375 / +495 / +235 |
| **Jim Miller** vs. **Terrance McKinney**<br>LW, 3 rds | Miller 22% – 78% McKinney | +360 / -360 | no line yet | Miller 22% (+360) | Miller 9% / 7% / 5%<br>McKinney 32% / 19% / 27% | 32% | McKinney by KO/TKO (32%) | no line yet | no price yet; fair Over 1.5 -110, Under +110 | no prices yet; fair KO / Sub / Dec<br>Miller +1015 / +1245 / +1735<br>McKinney +210 / +425 / +275 |
| **Donte Johnson** vs. **Cesar Almeida**<br>MW, 3 rds | Johnson 80% – 20% Almeida | -410 / +410 | no line yet | Johnson 80% (-410) | Johnson 34% / 17% / 30%<br>Almeida 7% / 3% / 10% | 40% | Johnson by KO/TKO (34%) | no line yet | no price yet; fair Over 2.5 +125, Under -125 | no prices yet; fair KO / Sub / Dec<br>Johnson +195 / +500 / +235<br>Almeida +1240 / +3895 / +935 |
| **Macy Chiasson** vs. **Bia Mesquita**<br>W-BW, 3 rds | Chiasson 31% – 69% Mesquita | +225 / -225 | no line yet | Chiasson 31% (+225) | Chiasson 4% / 5% / 22%<br>Mesquita 5% / 40% / 24% | 46% | Mesquita by submission (40%) | no line yet | no price yet; fair Over 2.5 -100, Under +100 | no prices yet; fair KO / Sub / Dec<br>Chiasson +2540 / +1840 / +360<br>Mesquita +1990 / +150 / +315 |
| **Adrian Yañez** vs. **Juan Diaz**<br>BW, 3 rds | Yañez 37% – 63% Diaz | +170 / -170 | no line yet | Yañez 37% (+170) | Yañez 14% / 3% / 20%<br>Diaz 11% / 22% / 30% | 50% | Diaz by decision (30%) | no line yet | no price yet; fair Over 2.5 -115, Under +115 | no prices yet; fair KO / Sub / Dec<br>Yañez +590 / +3610 / +410<br>Diaz +815 / +355 / +230 |
| **Nazim Sadykhov** vs. **Jefferson Nascimento**<br>LW, 3 rds | Sadykhov 49% – 51% Nascimento | +105 / -105 | no line yet | Sadykhov 49% (+105) | Sadykhov 23% / 8% / 18%<br>Nascimento 24% / 8% / 19% | 37% | Nascimento by KO/TKO (24%) | no line yet | no price yet; fair Over 1.5 -125, Under +125 | no prices yet; fair KO / Sub / Dec<br>Sadykhov +340 / +1125 / +470<br>Nascimento +315 / +1180 / +415 |
| **Jared Gordon** vs. **Melquizael Costa**<br>LW, 3 rds | Gordon 27% – 73% Costa | +265 / -265 | no line yet | Gordon 27% (+265) | Gordon 9% / 3% / 15%<br>Costa 27% / 18% / 28% | 42% | Costa by decision (28%) | no line yet | no price yet; fair Over 2.5 +115, Under -115 | no prices yet; fair KO / Sub / Dec<br>Gordon +955 / +3020 / +580<br>Costa +270 / +460 / +260 |
| **Evan Elder** vs. **Samuel Sanches**<br>LW, 3 rds, UFC debut: Sanches | Elder 54% – 46% Sanches | -115 / +115 | no line yet | Elder 54% (-115) | Elder 20% / 8% / 25%<br>Sanches 17% / 8% / 21% | 46% | Elder by decision (25%) | no line yet | no price yet; fair Over 2.5 -100, Under +100 | no prices yet; fair KO / Sub / Dec<br>Elder +395 / +1085 / +295<br>Sanches +495 / +1085 / +380 |

When it ends (either fighter):

| Bout | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Decision |
|---|---|---|---|---|---|---|
| Gane vs. Hokit | 31% | 22% | 12% | 6% | 5% | 24% |
| Harrison vs. Nunes | 14% | 12% | 8% | 5% | 4% | 57% |
| Borralho vs. Belgaroui | 26% | 17% | 8% |  |  | 49% |
| Medić vs. Holland | 35% | 20% | 9% |  |  | 36% |
| Hasan vs. Gurule | 29% | 18% | 9% |  |  | 45% |
| Thompson vs. Radtke | 27% | 17% | 8% |  |  | 48% |
| Dober vs. Duncan | 30% | 18% | 9% |  |  | 43% |
| Miller vs. McKinney | 38% | 21% | 9% |  |  | 32% |
| Johnson vs. Almeida | 32% | 19% | 9% |  |  | 40% |
| Chiasson vs. Mesquita | 28% | 17% | 9% |  |  | 46% |
| Yañez vs. Diaz | 26% | 16% | 8% |  |  | 50% |
| Sadykhov vs. Nascimento | 34% | 20% | 9% |  |  | 37% |
| Gordon vs. Costa | 31% | 18% | 9% |  |  | 42% |
| Elder vs. Sanches | 28% | 17% | 9% |  |  | 46% |

## How the 2026 predictions have done

| Predictor | Fights | Log loss | Brier | Winners |
|---|---|---|---|---|
| Final prediction | 463 | 0.6228 | 0.217 | 63.7% |
| Model alone (before the market) | 463 | 0.6409 | 0.224 | 61.8% |
| Glicko-2 rating alone | 463 | 0.6827 | 0.245 | 57.2% |
| Final, on fights with a price | 128 | 0.5286 | 0.177 | 74.2% |
| Market price when predicted | 128 | 0.5386 | 0.180 | 75.8% |
| Coin flip | 463 | 0.6931 | 0.250 | – |

Log loss scores the win chances (lower is better; a coin flip scores 0.693, and the betting market about 0.61). Brier is the squared error of the win chance. Picking every betting favorite already gets about two thirds of winners right, so the win rate says little on its own.

- Winner and method (six outcomes): log loss 1.584 on 462 fights, against 1.792 for guessing uniformly. The single most likely result happened 34% of the time.
- Went the distance: predicted 48% on average, actual 42%.

449 of these fights happened before the predictor went live. They are backfilled walk-forward (each fight predicted from earlier fights only, with models fitted on earlier years) using the odds dataset's approximate closing prices, which run only through March 2026, so later backfilled fights use the model alone. Every fight since is graded on the prediction logged before it started.

### Edge record

Every edge logged with a live prediction (the last one before the fight), at the stake and price logged with it; edges logged before edges were priced from the final prediction are left out. Pushes return the stake (a no contest voids every bet; a draw refunds the moneyline). Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised.

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Moneyline | 2 | 0-2-0 | 2.9 | -2.87 | -100.0% | +7.3% |
| Round total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Method of victory | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

### Latest results: UFC 333: Volkanovski vs. Evloev

| Bout | Predicted | Result | Chance given to the winner | Chance given to the exact result |
|---|---|---|---|---|
| Alexander Volkanovski vs. Movsar Evloev | Evloev 52% | Alexander Volkanovski by KO/TKO, R2 | 48% | 16% |
| Petr Yan vs. Merab Dvalishvili | Yan 57% | Petr Yan by decision | 57% | 36% |
| Lone'er Kavanagh vs. Ramazan Temirov | Temirov 51% | Lone'er Kavanagh by KO/TKO, R1 | 49% | 10% |
| Alexander Volkov vs. Rizvan Kuniev | Volkov 52% | Alexander Volkov by decision | 52% | 26% |
| Aaron Pico vs. Losene Keita | Pico 52% | Aaron Pico by KO/TKO, R1 | 52% | 10% |
| Azamat Murzakanov vs. Dominick Reyes | Murzakanov 62% | Dominick Reyes by KO/TKO, R1 | 38% | 23% |
| Nikita Krylov vs. Abdul-Rakhman Yakhyaev | Yakhyaev 84% | Abdul-Rakhman Yakhyaev by KO/TKO, R1 | 84% | 48% |
| Abus Magomedov vs. Cam Rowston | Rowston 52% | Abus Magomedov by submission, R1 | 48% | 12% |
| Grant Dawson vs. Nurullo Aliev | Aliev 50% | Grant Dawson by decision | 50% | 25% |
| Colby Thicknesse vs. Asaf Chopurov | Chopurov 82% | Colby Thicknesse by decision | 18% | 9% |
| Abubakar Vagaev vs. Jacob Malkoun | Vagaev 57% | Abubakar Vagaev by decision | 57% | 34% |
| Bolaji Oki vs. Daniel Santos | Santos 54% | Daniel Santos by decision | 54% | 24% |
| Kody Steele vs. Noah Gugnon | Steele 53% | Kody Steele by KO/TKO, R1 | 53% | 12% |
| Iasmin Lucindo vs. Nicolle Caliari | Lucindo 82% | Iasmin Lucindo by decision | 82% | 61% |

## Top fighters by division

Glicko-2 rating from UFC results, with finishes counting as clearer wins than decisions. ± is two rating deviations (fighters with few or old fights are less certain), and the ranking uses the rating minus that margin so an unproven fighter does not top a division on one big win. Active fighters only (a fight in the last two years).

| Division | # | Fighter | Rating | ± | UFC record | Last fight |
|---|---|---|---|---|---|---|
| Flyweight | 1 | Manel Kape | 1978 | 284 | 8-3 | 2026-06-20 |
|  | 2 | Joshua Van | 1942 | 261 | 11-1 | 2026-09-19 |
|  | 3 | Brandon Moreno | 1895 | 237 | 12-7-2 | 2026-09-12 |
|  | 4 | Alexandre Pantoja | 1894 | 237 | 14-5 | 2026-09-19 |
|  | 5 | Tatsuro Taira | 1963 | 318 | 8-2 | 2026-05-09 |
| Bantamweight | 1 | Petr Yan | 2147 | 228 | 13-4 | 2026-10-24 |
|  | 2 | Merab Dvalishvili | 2128 | 224 | 14-4 | 2026-10-24 |
|  | 3 | Song Yadong | 2064 | 225 | 13-4-1 | 2026-08-29 |
|  | 4 | Cory Sandhagen | 2059 | 231 | 11-6 | 2026-07-11 |
|  | 5 | Sean O'Malley | 2059 | 244 | 12-3 | 2026-06-14 |
| Featherweight | 1 | Alexander Volkanovski | 2214 | 225 | 16-3 | 2026-10-24 |
|  | 2 | Diego Lopes | 2145 | 267 | 7-3 | 2026-06-14 |
|  | 3 | Aljamain Sterling | 2097 | 229 | 18-5 | 2026-04-25 |
|  | 4 | Brian Ortega | 2062 | 272 | 8-5 | 2025-08-23 |
|  | 5 | Jean Silva | 2075 | 301 | 7-1 | 2026-09-12 |
| Lightweight | 1 | Ilia Topuria | 2274 | 296 | 9-1 | 2026-06-14 |
|  | 2 | Justin Gaethje | 2193 | 240 | 11-5 | 2026-06-14 |
|  | 3 | Charles Oliveira | 2146 | 212 | 25-11 | 2026-03-07 |
|  | 4 | Arman Tsarukyan | 2148 | 267 | 11-2 | 2026-09-19 |
|  | 5 | Dustin Poirier | 2096 | 230 | 22-9 | 2025-07-19 |
| Welterweight | 1 | Islam Makhachev | 2278 | 233 | 18-1 | 2026-08-15 |
|  | 2 | Shavkat Rakhmonov | 2401 | 407 | 7-0 | 2024-12-07 |
|  | 3 | Max Holloway | 2190 | 211 | 24-9 | 2026-07-11 |
|  | 4 | Carlos Prates | 2236 | 282 | 7-1 | 2026-05-02 |
|  | 5 | Michael Morales | 2245 | 323 | 7-0 | 2025-11-15 |
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
|  | 4 | Alexander Volkov | 2247 | 230 | 15-5 | 2026-10-24 |
|  | 5 | Alex Pereira | 2268 | 255 | 10-3 | 2026-06-14 |
| Women's Strawweight | 1 | Tatiana Suarez | 2011 | 315 | 9-1 | 2026-04-11 |
|  | 2 | Virna Jandiroba | 1841 | 252 | 9-4 | 2026-04-04 |
|  | 3 | Mackenzie Dern | 1797 | 230 | 12-5 | 2026-08-15 |
|  | 4 | Gillian Robertson | 1785 | 231 | 14-7 | 2026-08-15 |
|  | 5 | Jessica Andrade | 1753 | 221 | 17-13 | 2025-08-16 |
| Women's Flyweight | 1 | Valentina Shevchenko | 1998 | 255 | 15-3-1 | 2025-11-15 |
|  | 2 | Zhang Weili | 1981 | 258 | 10-3 | 2025-11-15 |
|  | 3 | Erin Blanchfield | 1984 | 285 | 8-2 | 2026-10-17 |
|  | 4 | Natalia Silva | 2007 | 311 | 9-0 | 2026-10-03 |
|  | 5 | Manon Fiorot | 1961 | 288 | 8-2 | 2026-09-12 |
| Women's Bantamweight | 1 | Kayla Harrison | 2075 | 468 | 3-0 | 2025-06-07 |
|  | 2 | Ketlen Vieira | 1773 | 250 | 10-5 | 2026-05-16 |
|  | 3 | Julianna Pena | 1821 | 307 | 8-4 | 2025-06-07 |
|  | 4 | Norma Dumont | 1743 | 260 | 9-4 | 2026-09-26 |
|  | 5 | Luana Santos | 1827 | 352 | 6-1 | 2026-06-20 |

## Current model fit

- Fitted on 5344 fights from 2016–2026.
- Market blend: 81% weight on the de-vigged price, total slope 1.28 (above 1 stretches favorites, correcting the favorite-longshot bias). Without a price: slope 1.02 on the model alone.
- Strongest win-model inputs (log-odds per standard deviation, A minus B): age -0.28, glicko_logit +0.21, strike_matchup +0.18, debut -0.12, age_decline -0.11, sapm -0.09.
