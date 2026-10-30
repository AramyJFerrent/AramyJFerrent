# UFC fight predictions

Updated Fri Oct 30, 2026 02:49 PM ET. Refreshed automatically every day and several times on fight week; each bout's prediction is locked when its part of the card starts and graded once the result is in.

Each bout gets one consistent breakdown: each fighter's chance to win, split into KO/TKO, submission and decision, and the chance it ends in each round. The win chance blends the model with the betting market (about 81% market, the weight that has predicted best on past fights) and corrects the market's habit of underrating heavy favorites. MMA is high-variance: even the most likely single result is usually well under 50%.

The fair odds are the American odds that match the win chance with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook only offers value on a fighter when its price beats the fair line.

The three edge columns value every side of each market at its posted price: expected value (EV) is the average profit per $1 staked, from the final prediction: the win chance blended with the moneyline (which corrects the market's habit of underrating heavy favorites), and method and round chances anchored to their own props, moved only by what the blend changes. A side is an edge when its EV is at least 3%; each cell names the best side if one clears that bar, with its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, at most 3 units on one bout; else "no edge". Moneylines and props are never priced near -110, so a missing price is never assumed: without one, the round-total cell shows the model's fair odds at the line closest to even and the method cell each fighter's fair KO/TKO, submission and decision odds. Over 1.5 rounds means the fight passes 2:30 of round 2 (a decision is always over); finishes are assumed spread evenly within a round.

See the backtest (backtest.md) for how these edges did against the dataset's closing prices, next to the model alone, which finds a 3% edge in most fights and lost money on them. Treat these columns as a live test, tracked below, not as betting advice.

## UFC Fight Night: Moicano vs. Nolan

Saturday, October 31, 2026 · first bout locks Sat Oct 31, 5:00 PM ET

| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | Most likely result | Moneyline edge | Round total edge | Method edge |
|---|---|---|---|---|---|---|---|---|---|---|
| **Renato Moicano** vs. **Tom Nolan**<br>LW, 5 rds | Moicano 51% – 49% Nolan | -105 / +105 | Moicano 53% (-125 / +105) | Moicano 40% (+150) | Moicano 20% / 13% / 18%<br>Nolan 20% / 12% / 17% | 35% | Nolan by KO/TKO (20%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Moicano +405 / +655 / +460<br>Nolan +400 / +725 / +490 |
| **Randy Brown** vs. **Jacobe Smith**<br>WW, 3 rds | Brown 25% – 75% Smith | +295 / -295 | Brown 30% (+215 / -265) | Brown 28% (+255) | Brown 8% / 2% / 15%<br>Smith 28% / 14% / 33% | 47% | Smith by decision (33%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Brown +1095 / +4205 / +580<br>Smith +260 / +615 / +205 |
| **Ode' Osbourne** vs. **Cody Durden**<br>FLW, 3 rds | Osbourne 47% – 53% Durden | +110 / -110 | Osbourne 48% (-102 / -118) | Osbourne 45% (+120) | Osbourne 13% / 15% / 19%<br>Durden 9% / 18% / 27% | 45% | Durden by decision (27%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Osbourne +645 / +575 / +430<br>Durden +1045 / +465 / +275 |
| **Yana Santos** vs. **Luana Santos**<br>W-BW, 3 rds | Santos 20% – 80% Santos | +395 / -395 | Santos 27% (+260 / -325) | Santos 20% (+405) | Santos 2% / 1% / 17%<br>Santos 9% / 19% / 51% | 68% | Santos by decision (51%) | Santos (-325): EV +4.4%, 80%, stake 3.0u | no edge | no prices yet; fair KO / Sub / Dec<br>Santos +4085 / +8835 / +500<br>Santos +960 / +430 / -105 |
| **Jean-Paul Lebosnoyani** vs. **Farman Hasanov**<br>WW, 3 rds | Lebosnoyani 74% – 26% Hasanov | -280 / +280 | Lebosnoyani 71% (-278 / +225) | Lebosnoyani 62% (-165) | Lebosnoyani 18% / 16% / 40%<br>Hasanov 4% / 4% / 18% | 58% | Lebosnoyani by decision (40%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Lebosnoyani +465 / +515 / +155<br>Hasanov +2560 / +2165 / +445 |
| **Francis Marshall** vs. **Dakota Hope**<br>FW, 3 rds | Marshall 70% – 30% Hope | -230 / +230 | Marshall 66% (-218 / +180) | Marshall 66% (-190) | Marshall 20% / 11% / 38%<br>Hope 10% / 2% / 18% | 57% | Marshall by decision (38%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Marshall +395 / +795 / +160<br>Hope +885 / +4785 / +450 |
| **Rodrigo Sezinando** vs. **Theodor Berggren**<br>WW, 3 rds | Sezinando 61% – 39% Berggren | -155 / +155 | Sezinando 62% (-185 / +154) | Sezinando 41% (+145) | Sezinando 32% / 9% / 19%<br>Berggren 20% / 5% / 14% | 33% | Sezinando by KO/TKO (32%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Sezinando +210 / +960 / +425<br>Berggren +405 / +1760 / +600 |
| **Julian Erosa** vs. **JeongYeong Lee**<br>FW, 3 rds | Erosa 41% – 59% Lee | +145 / -145 | Erosa 42% (+130 / -155) | Erosa 49% (+105) | Erosa 13% / 6% / 22%<br>Lee 24% / 6% / 29% | 51% | Lee by decision (29%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Erosa +660 / +1570 / +355<br>Lee +320 / +1515 / +250 |
| **Zach Reese** vs. **Mickey Gall**<br>MW, 3 rds | Reese 82% – 18% Gall | -445 / +445 | Reese 78% (-425 / +330) | Reese 70% (-230) | Reese 35% / 20% / 26%<br>Gall 8% / 4% / 7% | 33% | Reese by KO/TKO (35%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Reese +180 / +395 / +285<br>Gall +1200 / +2440 / +1370 |
| **Nick Klein** vs. **Joe Kropschot**<br>MW, 3 rds, UFC debut: Kropschot | Klein 26% – 74% Kropschot | +280 / -280 | Klein 27% (+250 / -310) | Klein 47% (+115) | Klein 8% / 8% / 10%<br>Kropschot 36% / 17% / 21% | 31% | Kropschot by KO/TKO (36%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Klein +1220 / +1120 / +860<br>Kropschot +180 / +485 / +380 |
| **Talita Alencar** vs. **Piera Rodriguez**<br>W-SW, 3 rds | Alencar 27% – 73% Rodriguez | +265 / -265 | Alencar 29% (+225 / -278) | Alencar 42% (+140) | Alencar 2% / 4% / 21%<br>Rodriguez 6% / 6% / 61% | 82% | Rodriguez by decision (61%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Alencar +4985 / +2275 / +370<br>Rodriguez +1630 / +1665 / -160 |
| **Lucia Szabová** vs. **Tainara Lisboa**<br>W-FLW, 3 rds, UFC debut: Szabová | Szabová 86% – 14% Lisboa | -615 / +615 | Szabová 83% (-650 / +470) | Szabová 67% (-205) | Szabová 14% / 25% / 47%<br>Lisboa 2% / 3% / 10% | 57% | Szabová by decision (47%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Szabová +615 / +300 / +115<br>Lisboa +6165 / +3745 / +925 |

When it ends (either fighter):

| Bout | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Decision |
|---|---|---|---|---|---|---|
| Moicano vs. Nolan | 24% | 19% | 11% | 6% | 5% | 35% |
| Brown vs. Smith | 27% | 17% | 8% |  |  | 47% |
| Osbourne vs. Durden | 28% | 18% | 9% |  |  | 45% |
| Santos vs. Santos | 15% | 11% | 6% |  |  | 68% |
| Lebosnoyani vs. Hasanov | 21% | 14% | 7% |  |  | 58% |
| Marshall vs. Hope | 22% | 14% | 7% |  |  | 57% |
| Sezinando vs. Berggren | 37% | 20% | 9% |  |  | 33% |
| Erosa vs. Lee | 25% | 16% | 8% |  |  | 51% |
| Reese vs. Gall | 37% | 20% | 9% |  |  | 33% |
| Klein vs. Kropschot | 39% | 21% | 9% |  |  | 31% |
| Alencar vs. Rodriguez | 8% | 6% | 3% |  |  | 82% |
| Szabová vs. Lisboa | 22% | 14% | 7% |  |  | 57% |

## UFC Fight Night: Bonfim vs. Brady

Saturday, November 07, 2026 · first bout locks Sat Nov 7, 5:00 PM ET

| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | Most likely result | Moneyline edge | Round total edge | Method edge |
|---|---|---|---|---|---|---|---|---|---|---|
| **Gabriel Bonfim** vs. **Sean Brady**<br>WW, 5 rds | Bonfim 50% – 50% Brady | +100 / -100 | no line yet | Bonfim 50% (+100) | Bonfim 17% / 10% / 23%<br>Brady 12% / 12% / 27% | 50% | Brady by decision (27%) | no line yet | no price yet; fair Over 4.5 -110, Under +110 | no prices yet; fair KO / Sub / Dec<br>Bonfim +495 / +885 / +335<br>Brady +745 / +760 / +275 |
| **Tatiana Suarez** vs. **Virna Jandiroba**<br>W-SW, 3 rds | Suarez 66% – 34% Jandiroba | -195 / +195 | Suarez 62% (-185 / +154) | Suarez 65% (-185) | Suarez 4% / 16% / 46%<br>Jandiroba 2% / 8% / 24% | 70% | Suarez by decision (46%) | no edge | no price yet; fair Over 2.5 -270, Under +270 | no prices yet; fair KO / Sub / Dec<br>Suarez +2685 / +520 / +115<br>Jandiroba +5285 / +1140 / +315 |
| **Davey Grant** vs. **Elijah Smith**<br>BW, 3 rds | Grant 18% – 82% Smith | +465 / -465 | no line yet | Grant 18% (+465) | Grant 5% / 1% / 12%<br>Smith 21% / 21% / 40% | 51% | Smith by decision (40%) | no line yet | no price yet; fair Over 2.5 -125, Under +125 | no prices yet; fair KO / Sub / Dec<br>Grant +2095 / +6955 / +755<br>Smith +375 / +370 / +150 |
| **Seokhyeon Ko** vs. **Wellington Turman**<br>WW, 3 rds | Ko 86% – 14% Turman | -620 / +620 | Ko 81% (-550 / +410) | Ko 79% (-370) | Ko 22% / 20% / 44%<br>Turman 4% / 2% / 8% | 52% | Ko by decision (44%) | no edge | no price yet; fair Over 2.5 -125, Under +125 | no prices yet; fair KO / Sub / Dec<br>Ko +360 / +395 / +125<br>Turman +2705 / +3950 / +1165 |
| **Billy Elekana** vs. **Lucas Fernando**<br>LHW, 3 rds | Elekana 29% – 71% Fernando | +245 / -245 | Elekana 31% (+210 / -258) | Elekana 42% (+135) | Elekana 12% / 7% / 10%<br>Fernando 46% / 7% / 18% | 28% | Fernando by KO/TKO (46%) | no edge | no price yet; fair Over 1.5 +105, Under -105 | no prices yet; fair KO / Sub / Dec<br>Elekana +770 / +1245 / +920<br>Fernando +120 / +1375 / +440 |
| **Mantas Kondratavičius** vs. **Andre Petroski**<br>MW, 3 rds | Kondratavičius 73% – 27% Petroski | -265 / +265 | no line yet | Kondratavičius 73% (-265) | Kondratavičius 37% / 9% / 27%<br>Petroski 7% / 6% / 14% | 41% | Kondratavičius by KO/TKO (37%) | no line yet | no price yet; fair Over 2.5 +120, Under -120 | no prices yet; fair KO / Sub / Dec<br>Kondratavičius +175 / +995 / +270<br>Petroski +1275 / +1580 / +610 |
| **Gabriel Lorenço** vs. **Alvin Hines**<br>HW, 3 rds, UFC debut: Lorenço | Lorenço 70% – 30% Hines | -230 / +230 | no line yet | Lorenço 70% (-230) | Lorenço 43% / 8% / 18%<br>Hines 16% / 4% / 11% | 29% | Lorenço by KO/TKO (43%) | no line yet | no price yet; fair Over 1.5 +105, Under -105 | no prices yet; fair KO / Sub / Dec<br>Lorenço +130 / +1110 / +460<br>Hines +530 / +2755 / +805 |
| **Karine Silva** vs. **Gabriella Fernandes**<br>W-FLW, 3 rds | Silva 64% – 36% Fernandes | -180 / +180 | Silva 59% (-162 / +136) | Silva 69% (-220) | Silva 8% / 19% / 37%<br>Fernandes 4% / 5% / 26% | 63% | Silva by decision (37%) | Silva (-162): EV +3.6%, 64%, stake 1.5u | no price yet; fair Over 2.5 -195, Under +195 | no prices yet; fair KO / Sub / Dec<br>Silva +1090 / +425 / +175<br>Fernandes +2145 / +1880 / +280 |
| **Mitch Raposo** vs. **Marcos Degli**<br>FLW, 3 rds, UFC debut: Degli | Raposo 33% – 67% Degli | +200 / -200 | Raposo 32% (+200 / -245) | Raposo 58% (-140) | Raposo 7% / 6% / 21%<br>Degli 14% / 14% / 39% | 60% | Degli by decision (39%) | no edge | no price yet; fair Over 2.5 -170, Under +170 | no prices yet; fair KO / Sub / Dec<br>Raposo +1405 / +1605 / +385<br>Degli +605 / +630 / +155 |
| **Jose Delano** vs. **Murtazali Magomedov**<br>FW, 3 rds | Delano 50% – 50% Magomedov | -100 / +100 | Delano 51% (-115 / -105) | Delano 46% (+115) | Delano 16% / 4% / 31%<br>Magomedov 11% / 17% / 21% | 52% | Delano by decision (31%) | no edge | no price yet; fair Over 2.5 -125, Under +125 | no prices yet; fair KO / Sub / Dec<br>Delano +525 / +2635 / +225<br>Magomedov +780 / +480 / +370 |
| **Keiichiro Nakamura** vs. **Ollie Schmid**<br>FW, 3 rds | Nakamura 77% – 23% Schmid | -330 / +330 | Nakamura 74% (-345 / +275) | Nakamura 60% (-150) | Nakamura 43% / 8% / 26%<br>Schmid 7% / 3% / 13% | 39% | Nakamura by KO/TKO (43%) | no edge | no price yet; fair Over 2.5 +130, Under -130 | no prices yet; fair KO / Sub / Dec<br>Nakamura +135 / +1205 / +280<br>Schmid +1300 / +3085 / +675 |
| **Austin Bashi** vs. **Lucas Brennan**<br>FW, 3 rds | Bashi 66% – 34% Brennan | -195 / +195 | no line yet | Bashi 66% (-195) | Bashi 15% / 19% / 32%<br>Brennan 9% / 6% / 19% | 51% | Bashi by decision (32%) | no line yet | no price yet; fair Over 2.5 -120, Under +120 | no prices yet; fair KO / Sub / Dec<br>Bashi +555 / +435 / +210<br>Brennan +1005 / +1500 / +435 |
| **Priscila Cachoeira** vs. **Nina Milošević**<br>W-BW, 3 rds | Cachoeira 14% – 86% Milošević | +600 / -600 | Cachoeira 21% (+350 / -455) | Cachoeira 13% (+655) | Cachoeira 3% / 1% / 10%<br>Milošević 30% / 14% / 42% | 52% | Milošević by decision (42%) | Milošević (-455): EV +4.6%, 86%, stake 3.0u | no price yet; fair Over 2.5 -125, Under +125 | no prices yet; fair KO / Sub / Dec<br>Cachoeira +3590 / +7090 / +885<br>Milošević +240 / +595 / +140 |
| **Jonny Parsons** vs. **Jose Henrique**<br>WW, 3 rds, UFC debut: Henrique | Parsons 38% – 62% Henrique | +160 / -160 | Parsons 38% (+150 / -180) | Parsons 51% (-100) | Parsons 18% / 3% / 16%<br>Henrique 21% / 11% / 31% | 47% | Henrique by decision (31%) | no edge | no price yet; fair Over 2.5 -105, Under +105 | no prices yet; fair KO / Sub / Dec<br>Parsons +445 / +2795 / +515<br>Henrique +380 / +845 / +225 |

When it ends (either fighter):

| Bout | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Decision |
|---|---|---|---|---|---|---|
| Bonfim vs. Brady | 17% | 14% | 9% | 5% | 5% | 50% |
| Suarez vs. Jandiroba | 14% | 10% | 5% |  |  | 70% |
| Grant vs. Smith | 25% | 16% | 8% |  |  | 51% |
| Ko vs. Turman | 24% | 16% | 8% |  |  | 52% |
| Elekana vs. Fernando | 41% | 21% | 9% |  |  | 28% |
| Kondratavičius vs. Petroski | 31% | 19% | 9% |  |  | 41% |
| Lorenço vs. Hines | 41% | 21% | 9% |  |  | 29% |
| Silva vs. Fernandes | 18% | 12% | 7% |  |  | 63% |
| Raposo vs. Degli | 20% | 13% | 7% |  |  | 60% |
| Delano vs. Magomedov | 24% | 16% | 8% |  |  | 52% |
| Nakamura vs. Schmid | 33% | 19% | 9% |  |  | 39% |
| Bashi vs. Brennan | 25% | 16% | 8% |  |  | 51% |
| Cachoeira vs. Milošević | 24% | 16% | 8% |  |  | 52% |
| Parsons vs. Henrique | 28% | 17% | 8% |  |  | 47% |

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
