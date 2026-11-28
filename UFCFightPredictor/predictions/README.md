# UFC fight predictions

Updated Fri Nov 27, 2026 09:10 PM ET. Refreshed automatically every day and several times on fight week; each bout's prediction is locked when its part of the card starts and graded once the result is in.

Each bout gets one consistent breakdown: each fighter's chance to win, split into KO/TKO, submission and decision, and the chance it ends in each round. The win chance blends the model with the betting market (about 80% market, the weight that has predicted best on past fights) and corrects the market's habit of underrating heavy favorites. MMA is high-variance: even the most likely single result is usually well under 50%.

The fair odds are the American odds that match the win chance with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook only offers value on a fighter when its price beats the fair line.

The three edge columns value every side of each market at its posted price: expected value (EV) is the average profit per $1 staked, from the final prediction: the win chance blended with the moneyline (which corrects the market's habit of underrating heavy favorites), and method and round chances anchored to their own props, moved only by what the blend changes. A side is an edge when its EV is at least 3%; each cell names the best side if one clears that bar, with its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, at most 3 units on one bout; else "no edge". Moneylines and props are never priced near -110, so a missing price is never assumed: without one, the round-total cell shows the model's fair odds at the line closest to even and the method cell each fighter's fair KO/TKO, submission and decision odds. Over 1.5 rounds means the fight passes 2:30 of round 2 (a decision is always over); finishes are assumed spread evenly within a round.

See the backtest (backtest.md) for how these edges did against the dataset's closing prices, next to the model alone, which finds a 3% edge in most fights and lost money on them. Treat these columns as a live test, tracked below, not as betting advice.

## UFC Fight Night: Adesanya vs Magomedov

Saturday, December 05, 2026 · first bout locks Sat Dec 5, 10:00 AM ET

| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | Most likely result | Moneyline edge | Round total edge | Method edge |
|---|---|---|---|---|---|---|---|---|---|---|
| **Israel Adesanya** vs. **Shara Magomedov**<br>MW, 5 rds | Adesanya 59% – 41% Magomedov | -145 / +145 | Adesanya 60% (-166 / +140) | Adesanya 46% (+120) | Adesanya 32% / 5% / 22%<br>Magomedov 23% / 4% / 14% | 36% | Adesanya by KO/TKO (32%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Adesanya +215 / +1750 / +350<br>Magomedov +335 / +2350 / +635 |
| **Ian Machado Garry** vs. **Yaroslav Amosov**<br>WW, 3 rds | Garry 59% – 41% Amosov | -140 / +140 | Garry 60% (-170 / +142) | Garry 42% (+140) | Garry 17% / 6% / 36%<br>Amosov 4% / 20% / 17% | 53% | Garry by decision (36%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Garry +470 / +1690 / +180<br>Amosov +2215 / +405 / +485 |
| **Serghei Spivac** vs. **Mario Pinto**<br>HW, 3 rds | Spivac 21% – 79% Pinto | +365 / -365 | Spivac 27% (+250 / -310) | Spivac 23% (+335) | Spivac 7% / 3% / 11%<br>Pinto 35% / 14% / 30% | 41% | Pinto by KO/TKO (35%) | Pinto (-310): EV +3.9%, 79%, stake 3.0u | no edge | no prices yet; fair KO / Sub / Dec<br>Spivac +1255 / +3215 / +805<br>Pinto +190 / +630 / +230 |
| **Levan Chokheli** vs. **Islam Dulatov**<br>WW, 3 rds | Chokheli 37% – 63% Dulatov | +170 / -170 | Chokheli 38% (+154 / -185) | Chokheli 47% (+110) | Chokheli 19% / 3% / 15%<br>Dulatov 29% / 6% / 28% | 43% | Dulatov by KO/TKO (29%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Chokheli +435 / +3720 / +550<br>Dulatov +245 / +1470 / +255 |
| **Mairon Santos** vs. **Akbar Abdullaev**<br>LW, 3 rds, UFC debut: Abdullaev | Santos 32% – 68% Abdullaev | +215 / -215 | Santos 27% (+260 / -298) | Santos 73% (-275) | Santos 13% / 3% / 15%<br>Abdullaev 20% / 13% / 36% | 51% | Abdullaev by decision (36%) | Santos (+260): EV +14.0%, 32%, stake 1.4u | no edge | no prices yet; fair KO / Sub / Dec<br>Santos +660 / +3045 / +550<br>Abdullaev +405 / +685 / +180 |
| **Magomed Tuchalov** vs. **Ion Cutelaba**<br>LHW, 3 rds | Tuchalov 65% – 35% Cutelaba | -185 / +185 | Tuchalov 62% (-185 / +154) | Tuchalov 59% (-145) | Tuchalov 25% / 16% / 24%<br>Cutelaba 11% / 10% / 15% | 38% | Tuchalov by KO/TKO (25%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Tuchalov +300 / +530 / +320<br>Cutelaba +810 / +920 / +585 |
| **Bruno Silva** vs. **Jafel Filho**<br>FLW, 3 rds, UFC debut: Silva | Silva 45% – 55% Filho | +120 / -120 | no line yet | Silva 45% (+120) | Silva 9% / 11% / 25%<br>Filho 6% / 30% / 18% | 43% | Filho by submission (30%) | no line yet | no edge | no prices yet; fair KO / Sub / Dec<br>Silva +1000 / +775 / +305<br>Filho +1450 / +235 / +445 |
| **Uran Satybaldiev** vs. **Ivan Gnizditskiy**<br>LHW, 3 rds, UFC debut: Gnizditskiy | Satybaldiev 52% – 48% Gnizditskiy | -110 / +110 | Satybaldiev 53% (-125 / +102) | Satybaldiev 48% (+110) | Satybaldiev 25% / 15% / 13%<br>Gnizditskiy 23% / 8% / 17% | 30% | Satybaldiev by KO/TKO (25%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Satybaldiev +305 / +555 / +695<br>Gnizditskiy +345 / +1210 / +475 |
| **Marco Tulio** vs. **JunYong Park**<br>MW, 3 rds | Tulio 59% – 41% Park | -145 / +145 | no line yet | Tulio 59% (-145) | Tulio 28% / 6% / 25%<br>Park 18% / 7% / 16% | 40% | Tulio by KO/TKO (28%) | no line yet | no price yet; fair Over 2.5 +125, Under -125 | no prices yet; fair KO / Sub / Dec<br>Tulio +255 / +1490 / +310<br>Park +455 / +1275 / +540 |
| **Pavel Andrusca** vs. **Mehemmedeli Osmanli**<br>BW, 3 rds | Andrusca 66% – 34% Osmanli | -190 / +190 | Andrusca 56% (-142 / +120) | Andrusca 83% (-480) | Andrusca 12% / 13% / 41%<br>Osmanli 9% / 5% / 20% | 61% | Andrusca by decision (41%) | Andrusca (-142): EV +11.8%, 66%, stake 3.0u | no edge | no prices yet; fair KO / Sub / Dec<br>Andrusca +745 / +660 / +145<br>Osmanli +990 / +1775 / +405 |
| **Modestino Rodrigues** vs. **Matthieu Letho Duclos**<br>MW, 3 rds, UFC debut: Rodrigues | Rodrigues 43% – 57% Duclos | +135 / -135 | Rodrigues 46% (+110 / -130) | Rodrigues 38% (+165) | Rodrigues 16% / 8% / 18%<br>Duclos 31% / 7% / 19% | 37% | Duclos by KO/TKO (31%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Rodrigues +520 / +1115 / +450<br>Duclos +220 / +1360 / +420 |
| **Abdul Hussein** vs. **Hecher Sosa**<br>BW, 3 rds | Hussein 66% – 34% Sosa | -190 / +190 | Hussein 62% (-180 / +150) | Hussein 66% (-195) | Hussein 17% / 23% / 25%<br>Sosa 8% / 3% / 23% | 48% | Hussein by decision (25%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Hussein +475 / +335 / +295<br>Sosa +1110 / +2910 / +340 |
| **Luke Riley** vs. **Gabriel Santos**<br>FW, 3 rds | Riley 59% – 41% Santos | -140 / +140 | Riley 55% (-135 / +114) | Riley 64% (-180) | Riley 26% / 4% / 29%<br>Santos 10% / 8% / 23% | 53% | Riley by decision (29%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Riley +285 / +2745 / +240<br>Santos +900 / +1180 / +325 |
| **Mateusz Rębecki** vs. **Elves Brener**<br>LW, 3 rds | Rębecki 55% – 45% Brener | -120 / +120 | Rębecki 54% (-130 / +110) | Rębecki 53% (-110) | Rębecki 21% / 6% / 28%<br>Brener 19% / 6% / 20% | 48% | Rębecki by decision (28%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Rębecki +365 / +1580 / +260<br>Brener +420 / +1645 / +400 |

When it ends (either fighter):

| Bout | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Decision |
|---|---|---|---|---|---|---|
| Adesanya vs. Magomedov | 23% | 18% | 12% | 6% | 5% | 36% |
| Garry vs. Amosov | 24% | 15% | 8% |  |  | 53% |
| Spivac vs. Pinto | 31% | 19% | 9% |  |  | 41% |
| Chokheli vs. Dulatov | 30% | 18% | 9% |  |  | 43% |
| Santos vs. Abdullaev | 25% | 16% | 8% |  |  | 51% |
| Tuchalov vs. Cutelaba | 33% | 19% | 9% |  |  | 38% |
| Silva vs. Filho | 30% | 18% | 9% |  |  | 43% |
| Satybaldiev vs. Gnizditskiy | 40% | 21% | 9% |  |  | 30% |
| Tulio vs. Park | 32% | 19% | 9% |  |  | 40% |
| Andrusca vs. Osmanli | 19% | 13% | 7% |  |  | 61% |
| Rodrigues vs. Duclos | 34% | 19% | 9% |  |  | 37% |
| Hussein vs. Sosa | 27% | 17% | 8% |  |  | 48% |
| Riley vs. Santos | 24% | 15% | 8% |  |  | 53% |
| Rębecki vs. Brener | 27% | 17% | 8% |  |  | 48% |

## UFC 335: Oliveira vs. Lopes

Saturday, December 12, 2026 · first bout locks Sat Dec 12, 5:00 PM ET

| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | Most likely result | Moneyline edge | Round total edge | Method edge |
|---|---|---|---|---|---|---|---|---|---|---|
| **Charles Oliveira** vs. **Diego Lopes**<br>LW, 5 rds | Oliveira 56% – 44% Lopes | -125 / +125 | Oliveira 57% (-148 / +124) | Oliveira 42% (+135) | Oliveira 15% / 23% / 17%<br>Lopes 23% / 7% / 14% | 32% | Lopes by KO/TKO (23%) | no edge | no price yet; fair Over 2.5 +105, Under -105 | no prices yet; fair KO / Sub / Dec<br>Oliveira +560 / +335 / +475<br>Lopes +330 / +1300 / +610 |
| **Alex Pereira** vs. **Sergei Pavlovich**<br>HW, 5 rds | Pereira 33% – 67% Pavlovich | +205 / -205 | Pereira 36% (+164 / -198) | Pereira 35% (+185) | Pereira 23% / 2% / 8%<br>Pavlovich 48% / 3% / 16% | 24% | Pavlovich by KO/TKO (48%) | no edge | no price yet; fair Over 1.5 -140, Under +140 | no prices yet; fair KO / Sub / Dec<br>Pereira +330 / +6160 / +1210<br>Pavlovich +105 / +3315 / +515 |
| **Brandon Moreno** vs. **Charles Johnson**<br>FLW, 3 rds | Moreno 70% – 30% Johnson | -230 / +230 | no line yet | Moreno 70% (-230) | Moreno 17% / 11% / 41%<br>Johnson 8% / 4% / 19% | 60% | Moreno by decision (41%) | no line yet | no price yet; fair Over 2.5 -170, Under +170 | no prices yet; fair KO / Sub / Dec<br>Moreno +480 / +770 / +145<br>Johnson +1180 / +2475 / +440 |
| **Damian Pinas** vs. **Baisangur Susurkaev**<br>MW, 3 rds | Pinas 44% – 56% Susurkaev | +130 / -130 | no line yet | Pinas 44% (+130) | Pinas 33% / 1% / 10%<br>Susurkaev 18% / 15% / 23% | 34% | Pinas by KO/TKO (33%) | no line yet | no price yet; fair Over 1.5 -115, Under +115 | no prices yet; fair KO / Sub / Dec<br>Pinas +210 / +9900 / +860<br>Susurkaev +445 / +585 / +330 |
| **Kyler Phillips** vs. **Ethyn Ewing**<br>BW, 3 rds | Phillips 39% – 61% Ewing | +155 / -155 | no line yet | Phillips 39% (+155) | Phillips 8% / 4% / 26%<br>Ewing 16% / 4% / 41% | 67% | Ewing by decision (41%) | no line yet | no price yet; fair Over 2.5 -235, Under +235 | no prices yet; fair KO / Sub / Dec<br>Phillips +1100 / +2175 / +280<br>Ewing +510 / +2490 / +145 |
| **Quentin Pasley** vs. **Junior Tafa**<br>LHW, 3 rds, UFC debut: Pasley | Pasley 52% – 48% Tafa | -110 / +110 | no line yet | Pasley 52% (-110) | Pasley 26% / 14% / 13%<br>Tafa 28% / 6% / 14% | 26% | Tafa by KO/TKO (28%) | no line yet | no price yet; fair Over 1.5 +115, Under -115 | no prices yet; fair KO / Sub / Dec<br>Pasley +285 / +640 / +685<br>Tafa +255 / +1565 / +630 |
| **Roque Conceição** vs. **Nilson Rojas**<br>FLW, 3 rds, UFC debut: Conceição | Conceição 57% – 43% Rojas | -135 / +135 | no line yet | Conceição 57% (-135) | Conceição 20% / 14% / 23%<br>Rojas 10% / 9% / 23% | 46% | Rojas by decision (23%) | no line yet | no price yet; fair Over 2.5 -100, Under +100 | no prices yet; fair KO / Sub / Dec<br>Conceição +410 / +595 / +330<br>Rojas +860 / +995 / +330 |
| **Jacqueline Cavalcanti** vs. **Michelle Montague**<br>W-BW, 3 rds | Cavalcanti 56% – 44% Montague | -130 / +130 | no line yet | Cavalcanti 56% (-130) | Cavalcanti 8% / 4% / 44%<br>Montague 4% / 4% / 36% | 81% | Cavalcanti by decision (44%) | no line yet | no price yet; fair Over 2.5 -470, Under +470 | no prices yet; fair KO / Sub / Dec<br>Cavalcanti +1165 / +2440 / +125<br>Montague +2455 / +2645 / +175 |

When it ends (either fighter):

| Bout | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Decision |
|---|---|---|---|---|---|---|
| Oliveira vs. Lopes | 26% | 20% | 12% | 6% | 5% | 32% |
| Pereira vs. Pavlovich | 31% | 22% | 13% | 6% | 5% | 24% |
| Moreno vs. Johnson | 20% | 13% | 7% |  |  | 60% |
| Pinas vs. Susurkaev | 37% | 20% | 9% |  |  | 34% |
| Phillips vs. Ewing | 16% | 11% | 6% |  |  | 67% |
| Pasley vs. Tafa | 43% | 22% | 9% |  |  | 26% |
| Conceição vs. Rojas | 28% | 17% | 9% |  |  | 46% |
| Cavalcanti vs. Montague | 9% | 7% | 4% |  |  | 81% |

## How the 2026 predictions have done

| Predictor | Fights | Log loss | Brier | Winners |
|---|---|---|---|---|
| Final prediction | 513 | 0.6195 | 0.215 | 64.5% |
| Model alone (before the market) | 513 | 0.6360 | 0.222 | 62.8% |
| Glicko-2 rating alone | 513 | 0.6836 | 0.245 | 57.1% |
| Final, on fights with a price | 178 | 0.5454 | 0.183 | 73.6% |
| Market price when predicted | 178 | 0.5556 | 0.186 | 74.2% |
| Coin flip | 513 | 0.6931 | 0.250 | – |

Log loss scores the win chances (lower is better; a coin flip scores 0.693, and the betting market about 0.61). Brier is the squared error of the win chance. Picking every betting favorite already gets about two thirds of winners right, so the win rate says little on its own.

- Winner and method (six outcomes): log loss 1.571 on 512 fights, against 1.792 for guessing uniformly. The single most likely result happened 34% of the time.
- Went the distance: predicted 48% on average, actual 43%.

449 of these fights happened before the predictor went live. They are backfilled walk-forward (each fight predicted from earlier fights only, with models fitted on earlier years) using the odds dataset's approximate closing prices, which run only through March 2026, so later backfilled fights use the model alone. Every fight since is graded on the prediction logged before it started.

### Edge record

Every edge logged with a live prediction (the last one before the fight), at the stake and price logged with it; edges logged before edges were priced from the final prediction are left out. Pushes return the stake (a no contest voids every bet; a draw refunds the moneyline). Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised.

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Moneyline | 12 | 8-4-0 | 26.4 | +1.82 | +6.9% | +5.3% |
| Round total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Method of victory | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

### Latest results: UFC Fight Night: Procházka vs. Stirling

| Bout | Predicted | Result | Chance given to the winner | Chance given to the exact result |
|---|---|---|---|---|
| Jiří Procházka vs. Navajo Stirling | Stirling 66% | Navajo Stirling by KO/TKO, R2 | 66% | 49% |
| Aljamain Sterling vs. Kevin Vallejos | Vallejos 56% | Kevin Vallejos by decision | 56% | 29% |
| Dan Hooker vs. Brian Ortega | Hooker 62% | Dan Hooker by decision | 62% | 26% |
| Kyoji Horiguchi vs. Asu Almabayev | Horiguchi 62% | Kyoji Horiguchi by decision | 62% | 38% |
| Jared Cannonier vs. Ikram Aliskerov | Aliskerov 80% | Ikram Aliskerov by decision | 80% | 38% |
| Aleksandre Topuria vs. Santiago Luna | Topuria 69% | Santiago Luna by decision | 31% | 19% |
| Shamil Gaziev vs. Tallison Teixeira | Gaziev 58% | Tallison Teixeira by decision | 42% | 13% |
| Amir Albazi vs. Alessandro Costa | Costa 51% | Amir Albazi by submission, R3 | 49% | 9% |
| Jake Matthews vs. Tahir Abdullayev | Matthews 69% | Tahir Abdullayev by decision | 31% | 16% |
| Nikolas Motta vs. Dom Mar Fan | Fan 67% | Dom Mar Fan by decision | 67% | 30% |
| Diyar Nurgozhay vs. Alik Lorenz | Nurgozhay 73% | Diyar Nurgozhay by KO/TKO, R2 | 73% | 44% |
| Shoaib Yousaf vs. John Mitchell | Mitchell 57% | John Mitchell by KO/TKO, R1 | 57% | 19% |

## Top fighters by division

Glicko-2 rating from UFC results, with finishes counting as clearer wins than decisions. ± is two rating deviations (fighters with few or old fights are less certain), and the ranking uses the rating minus that margin so an unproven fighter does not top a division on one big win. Active fighters only (a fight in the last two years).

| Division | # | Fighter | Rating | ± | UFC record | Last fight |
|---|---|---|---|---|---|---|
| Flyweight | 1 | Manel Kape | 1978 | 284 | 8-3 | 2026-06-20 |
|  | 2 | Joshua Van | 1942 | 261 | 11-1 | 2026-09-19 |
|  | 3 | Brandon Moreno | 1895 | 238 | 12-7-2 | 2026-09-12 |
|  | 4 | Alexandre Pantoja | 1894 | 238 | 14-5 | 2026-09-19 |
|  | 5 | Tatsuro Taira | 1963 | 318 | 8-2 | 2026-05-09 |
| Bantamweight | 1 | Petr Yan | 2147 | 229 | 13-4 | 2026-10-24 |
|  | 2 | Merab Dvalishvili | 2128 | 225 | 14-4 | 2026-10-24 |
|  | 3 | Song Yadong | 2064 | 226 | 13-4-1 | 2026-08-29 |
|  | 4 | Cory Sandhagen | 2059 | 232 | 11-6 | 2026-07-11 |
|  | 5 | Sean O'Malley | 2059 | 245 | 12-3 | 2026-06-14 |
| Featherweight | 1 | Alexander Volkanovski | 2214 | 226 | 16-3 | 2026-10-24 |
|  | 2 | Diego Lopes | 2145 | 268 | 7-3 | 2026-06-14 |
|  | 3 | Aljamain Sterling | 2073 | 221 | 18-6 | 2026-11-21 |
|  | 4 | Jean Silva | 2075 | 302 | 7-1 | 2026-09-12 |
|  | 5 | Jose Aldo | 2015 | 247 | 14-9 | 2025-05-10 |
| Lightweight | 1 | Ilia Topuria | 2274 | 297 | 9-1 | 2026-06-14 |
|  | 2 | Justin Gaethje | 2193 | 241 | 11-5 | 2026-06-14 |
|  | 3 | Charles Oliveira | 2146 | 213 | 25-11 | 2026-03-07 |
|  | 4 | Arman Tsarukyan | 2148 | 268 | 11-2 | 2026-09-19 |
|  | 5 | Dustin Poirier | 2096 | 231 | 22-9 | 2025-07-19 |
| Welterweight | 1 | Islam Makhachev | 2278 | 234 | 18-1 | 2026-08-15 |
|  | 2 | Shavkat Rakhmonov | 2401 | 408 | 7-0 | 2024-12-07 |
|  | 3 | Max Holloway | 2190 | 212 | 24-9 | 2026-07-11 |
|  | 4 | Carlos Prates | 2236 | 283 | 7-1 | 2026-05-02 |
|  | 5 | Michael Morales | 2245 | 323 | 7-0 | 2025-11-15 |
| Middleweight | 1 | Dricus Du Plessis | 2231 | 254 | 10-1 | 2026-07-18 |
|  | 2 | Khamzat Chimaev | 2255 | 278 | 9-1 | 2026-05-09 |
|  | 3 | Kamaru Usman | 2181 | 241 | 16-4 | 2026-07-18 |
|  | 4 | Nassourdine Imavov | 2173 | 278 | 9-2 | 2025-09-06 |
|  | 5 | Brendan Allen | 2123 | 229 | 16-4 | 2026-10-10 |
| Light Heavyweight | 1 | Magomed Ankalaev | 2188 | 242 | 13-2-1 | 2026-07-25 |
|  | 2 | Robert Whittaker | 2156 | 231 | 18-7 | 2026-07-11 |
|  | 3 | Carlos Ulberg | 2126 | 274 | 10-1 | 2026-04-11 |
|  | 4 | Paulo Costa | 2107 | 269 | 8-4 | 2026-04-11 |
|  | 5 | Dominick Reyes | 2063 | 237 | 11-5 | 2026-10-24 |
| Heavyweight | 1 | Ciryl Gane | 2350 | 260 | 12-2 | 2026-11-14 |
|  | 2 | Alexander Volkov | 2247 | 231 | 15-5 | 2026-10-24 |
|  | 3 | Alex Pereira | 2268 | 255 | 10-3 | 2026-06-14 |
|  | 4 | Tom Aspinall | 2279 | 303 | 8-1 | 2025-10-25 |
|  | 5 | Curtis Blaydes | 2162 | 240 | 15-6 | 2026-09-12 |
| Women's Strawweight | 1 | Tatiana Suarez | 2021 | 295 | 10-1 | 2026-11-07 |
|  | 2 | Virna Jandiroba | 1834 | 243 | 9-5 | 2026-11-07 |
|  | 3 | Mackenzie Dern | 1797 | 231 | 12-5 | 2026-08-15 |
|  | 4 | Gillian Robertson | 1785 | 232 | 14-7 | 2026-08-15 |
|  | 5 | Jessica Andrade | 1753 | 221 | 17-13 | 2025-08-16 |
| Women's Flyweight | 1 | Valentina Shevchenko | 1998 | 256 | 15-3-1 | 2025-11-15 |
|  | 2 | Zhang Weili | 1981 | 258 | 10-3 | 2025-11-15 |
|  | 3 | Erin Blanchfield | 1984 | 286 | 8-2 | 2026-10-17 |
|  | 4 | Natalia Silva | 2007 | 311 | 9-0 | 2026-10-03 |
|  | 5 | Manon Fiorot | 1961 | 289 | 8-2 | 2026-09-12 |
| Women's Bantamweight | 1 | Kayla Harrison | 2165 | 401 | 4-0 | 2026-11-14 |
|  | 2 | Amanda Nunes | 1981 | 280 | 16-3 | 2026-11-14 |
|  | 3 | Luana Santos | 1846 | 323 | 7-1 | 2026-10-31 |
|  | 4 | Ketlen Vieira | 1773 | 251 | 10-5 | 2026-05-16 |
|  | 5 | Julianna Pena | 1821 | 307 | 8-4 | 2025-06-07 |

## Current model fit

- Fitted on 5394 fights from 2016–2026.
- Market blend: 80% weight on the de-vigged price, total slope 1.28 (above 1 stretches favorites, correcting the favorite-longshot bias). Without a price: slope 1.02 on the model alone.
- Strongest win-model inputs (log-odds per standard deviation, A minus B): age -0.28, glicko_logit +0.21, strike_matchup +0.18, debut -0.13, age_decline -0.11, sapm -0.09.
