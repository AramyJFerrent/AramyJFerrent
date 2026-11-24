# UFC fight predictions

Updated Mon Nov 23, 2026 08:11 PM ET. Refreshed automatically every day and several times on fight week; each bout's prediction is locked when its part of the card starts and graded once the result is in.

Each bout gets one consistent breakdown: each fighter's chance to win, split into KO/TKO, submission and decision, and the chance it ends in each round. The win chance blends the model with the betting market (about 80% market, the weight that has predicted best on past fights) and corrects the market's habit of underrating heavy favorites. MMA is high-variance: even the most likely single result is usually well under 50%.

The fair odds are the American odds that match the win chance with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook only offers value on a fighter when its price beats the fair line.

The three edge columns value every side of each market at its posted price: expected value (EV) is the average profit per $1 staked, from the final prediction: the win chance blended with the moneyline (which corrects the market's habit of underrating heavy favorites), and method and round chances anchored to their own props, moved only by what the blend changes. A side is an edge when its EV is at least 3%; each cell names the best side if one clears that bar, with its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, at most 3 units on one bout; else "no edge". Moneylines and props are never priced near -110, so a missing price is never assumed: without one, the round-total cell shows the model's fair odds at the line closest to even and the method cell each fighter's fair KO/TKO, submission and decision odds. Over 1.5 rounds means the fight passes 2:30 of round 2 (a decision is always over); finishes are assumed spread evenly within a round.

See the backtest (backtest.md) for how these edges did against the dataset's closing prices, next to the model alone, which finds a 3% edge in most fights and lost money on them. Treat these columns as a live test, tracked below, not as betting advice.

## UFC Fight Night: Adesanya vs Magomedov

Saturday, December 05, 2026 · first bout locks Sat Dec 5, 10:00 AM ET

| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | Most likely result | Moneyline edge | Round total edge | Method edge |
|---|---|---|---|---|---|---|---|---|---|---|
| **Israel Adesanya** vs. **Shara Magomedov**<br>MW, 5 rds | Adesanya 59% – 41% Magomedov | -140 / +140 | Adesanya 59% (-162 / +136) | Adesanya 46% (+120) | Adesanya 31% / 5% / 22%<br>Magomedov 23% / 4% / 14% | 36% | Adesanya by KO/TKO (31%) | no edge | no price yet; fair Over 2.5 -110, Under +110 | no prices yet; fair KO / Sub / Dec<br>Adesanya +220 / +1770 / +355<br>Magomedov +330 / +2305 / +625 |
| **Ian Machado Garry** vs. **Yaroslav Amosov**<br>WW, 3 rds | Garry 60% – 40% Amosov | -150 / +150 | Garry 62% (-180 / +150) | Garry 42% (+140) | Garry 18% / 6% / 36%<br>Amosov 4% / 19% / 17% | 53% | Garry by decision (36%) | no edge | no price yet; fair Over 2.5 -130, Under +130 | no prices yet; fair KO / Sub / Dec<br>Garry +460 / +1640 / +175<br>Amosov +2290 / +420 / +500 |
| **Serghei Spivac** vs. **Mario Pinto**<br>HW, 3 rds | Spivac 23% – 77% Pinto | +335 / -335 | no line yet | Spivac 23% (+335) | Spivac 8% / 3% / 12%<br>Pinto 34% / 13% / 30% | 41% | Pinto by KO/TKO (34%) | no line yet | no price yet; fair Over 2.5 +120, Under -120 | no prices yet; fair KO / Sub / Dec<br>Spivac +1165 / +2985 / +750<br>Pinto +195 / +645 / +235 |
| **Luke Riley** vs. **Gabriel Santos**<br>FW, 3 rds | Riley 64% – 36% Santos | -180 / +180 | no line yet | Riley 64% (-180) | Riley 28% / 4% / 32%<br>Santos 9% / 7% / 21% | 52% | Riley by decision (32%) | no line yet | no price yet; fair Over 2.5 -130, Under +130 | no prices yet; fair KO / Sub / Dec<br>Riley +250 / +2465 / +215<br>Santos +1050 / +1395 / +385 |
| **Levan Chokheli** vs. **Islam Dulatov**<br>WW, 3 rds | Chokheli 47% – 53% Dulatov | +110 / -110 | no line yet | Chokheli 47% (+110) | Chokheli 24% / 3% / 20%<br>Dulatov 24% / 5% / 24% | 43% | Chokheli by KO/TKO (24%) | no line yet | no price yet; fair Over 2.5 +110, Under -110 | no prices yet; fair KO / Sub / Dec<br>Chokheli +315 / +2790 / +410<br>Dulatov +315 / +1840 / +320 |
| **Mairon Santos** vs. **Akbar Abdullaev**<br>LW, 3 rds, UFC debut: Abdullaev | Santos 73% – 27% Abdullaev | -275 / +275 | no line yet | Santos 73% (-275) | Santos 31% / 8% / 34%<br>Abdullaev 8% / 4% / 15% | 49% | Santos by decision (34%) | no line yet | no price yet; fair Over 2.5 -110, Under +110 | no prices yet; fair KO / Sub / Dec<br>Santos +225 / +1085 / +195<br>Abdullaev +1205 / +2205 / +590 |
| **Magomed Tuchalov** vs. **Ion Cutelaba**<br>LHW, 3 rds | Tuchalov 59% – 41% Cutelaba | -145 / +145 | no line yet | Tuchalov 59% (-145) | Tuchalov 23% / 14% / 22%<br>Cutelaba 13% / 11% / 17% | 39% | Tuchalov by KO/TKO (23%) | no line yet | no price yet; fair Over 2.5 +130, Under -130 | no prices yet; fair KO / Sub / Dec<br>Tuchalov +335 / +595 / +355<br>Cutelaba +690 / +770 / +500 |
| **Bruno Silva** vs. **Jafel Filho**<br>FLW, 3 rds, UFC debut: Silva | Silva 45% – 55% Filho | +120 / -120 | no line yet | Silva 45% (+120) | Silva 9% / 11% / 25%<br>Filho 6% / 30% / 18% | 43% | Filho by submission (30%) | no line yet | no price yet; fair Over 2.5 +110, Under -110 | no prices yet; fair KO / Sub / Dec<br>Silva +1000 / +775 / +305<br>Filho +1450 / +235 / +445 |
| **Uran Satybaldiev** vs. **Ivan Gnizditskiy**<br>LHW, 3 rds, UFC debut: Gnizditskiy | Satybaldiev 48% – 52% Gnizditskiy | +110 / -110 | no line yet | Satybaldiev 48% (+110) | Satybaldiev 22% / 14% / 12%<br>Gnizditskiy 25% / 9% / 19% | 31% | Gnizditskiy by KO/TKO (25%) | no line yet | no price yet; fair Over 1.5 -100, Under +100 | no prices yet; fair KO / Sub / Dec<br>Satybaldiev +345 / +630 / +765<br>Gnizditskiy +305 / +1075 / +425 |
| **Marco Tulio** vs. **JunYong Park**<br>MW, 3 rds | Tulio 59% – 41% Park | -145 / +145 | no line yet | Tulio 59% (-145) | Tulio 28% / 6% / 25%<br>Park 18% / 7% / 16% | 40% | Tulio by KO/TKO (28%) | no line yet | no price yet; fair Over 2.5 +125, Under -125 | no prices yet; fair KO / Sub / Dec<br>Tulio +255 / +1490 / +310<br>Park +455 / +1275 / +540 |
| **Pavel Andrusca** vs. **Mehemmedeli Osmanli**<br>BW, 3 rds | Andrusca 83% – 17% Osmanli | -480 / +480 | no line yet | Andrusca 83% (-480) | Andrusca 15% / 18% / 50%<br>Osmanli 5% / 3% / 10% | 60% | Andrusca by decision (50%) | no line yet | no price yet; fair Over 2.5 -175, Under +175 | no prices yet; fair KO / Sub / Dec<br>Andrusca +570 / +465 / -100<br>Osmanli +2080 / +3895 / +880 |
| **Modestino Rodrigues** vs. **Matthieu Letho Duclos**<br>MW, 3 rds, UFC debut: Rodrigues | Rodrigues 38% – 62% Duclos | +165 / -165 | no line yet | Rodrigues 38% (+165) | Rodrigues 14% / 7% / 16%<br>Duclos 34% / 8% / 21% | 37% | Duclos by KO/TKO (34%) | no line yet | no price yet; fair Over 1.5 -125, Under +125 | no prices yet; fair KO / Sub / Dec<br>Rodrigues +595 / +1285 / +515<br>Duclos +195 / +1230 / +385 |
| **Abdul Hussein** vs. **Hecher Sosa**<br>BW, 3 rds | Hussein 66% – 34% Sosa | -195 / +195 | no line yet | Hussein 66% (-195) | Hussein 18% / 23% / 25%<br>Sosa 8% / 3% / 22% | 48% | Hussein by decision (25%) | no line yet | no price yet; fair Over 2.5 -110, Under +110 | no prices yet; fair KO / Sub / Dec<br>Hussein +470 / +330 / +295<br>Sosa +1125 / +2945 / +345 |

When it ends (either fighter):

| Bout | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Decision |
|---|---|---|---|---|---|---|
| Adesanya vs. Magomedov | 23% | 18% | 12% | 6% | 5% | 36% |
| Garry vs. Amosov | 24% | 15% | 8% |  |  | 53% |
| Spivac vs. Pinto | 31% | 18% | 9% |  |  | 41% |
| Riley vs. Santos | 24% | 16% | 8% |  |  | 52% |
| Chokheli vs. Dulatov | 30% | 18% | 9% |  |  | 43% |
| Santos vs. Abdullaev | 26% | 17% | 8% |  |  | 49% |
| Tuchalov vs. Cutelaba | 33% | 19% | 9% |  |  | 39% |
| Silva vs. Filho | 30% | 18% | 9% |  |  | 43% |
| Satybaldiev vs. Gnizditskiy | 39% | 21% | 9% |  |  | 31% |
| Tulio vs. Park | 32% | 19% | 9% |  |  | 40% |
| Andrusca vs. Osmanli | 20% | 13% | 7% |  |  | 60% |
| Rodrigues vs. Duclos | 34% | 20% | 9% |  |  | 37% |
| Hussein vs. Sosa | 27% | 17% | 8% |  |  | 48% |

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
|  | 3 | Song Yadong | 2064 | 225 | 13-4-1 | 2026-08-29 |
|  | 4 | Cory Sandhagen | 2059 | 232 | 11-6 | 2026-07-11 |
|  | 5 | Sean O'Malley | 2059 | 244 | 12-3 | 2026-06-14 |
| Featherweight | 1 | Alexander Volkanovski | 2214 | 226 | 16-3 | 2026-10-24 |
|  | 2 | Diego Lopes | 2145 | 268 | 7-3 | 2026-06-14 |
|  | 3 | Aljamain Sterling | 2073 | 221 | 18-6 | 2026-11-21 |
|  | 4 | Jean Silva | 2075 | 302 | 7-1 | 2026-09-12 |
|  | 5 | Jose Aldo | 2015 | 247 | 14-9 | 2025-05-10 |
| Lightweight | 1 | Ilia Topuria | 2274 | 297 | 9-1 | 2026-06-14 |
|  | 2 | Justin Gaethje | 2193 | 240 | 11-5 | 2026-06-14 |
|  | 3 | Charles Oliveira | 2146 | 212 | 25-11 | 2026-03-07 |
|  | 4 | Arman Tsarukyan | 2148 | 268 | 11-2 | 2026-09-19 |
|  | 5 | Dustin Poirier | 2096 | 230 | 22-9 | 2025-07-19 |
| Welterweight | 1 | Islam Makhachev | 2278 | 234 | 18-1 | 2026-08-15 |
|  | 2 | Shavkat Rakhmonov | 2401 | 408 | 7-0 | 2024-12-07 |
|  | 3 | Max Holloway | 2190 | 212 | 24-9 | 2026-07-11 |
|  | 4 | Carlos Prates | 2236 | 282 | 7-1 | 2026-05-02 |
|  | 5 | Michael Morales | 2245 | 323 | 7-0 | 2025-11-15 |
| Middleweight | 1 | Dricus Du Plessis | 2231 | 254 | 10-1 | 2026-07-18 |
|  | 2 | Khamzat Chimaev | 2255 | 278 | 9-1 | 2026-05-09 |
|  | 3 | Kamaru Usman | 2181 | 240 | 16-4 | 2026-07-18 |
|  | 4 | Nassourdine Imavov | 2173 | 277 | 9-2 | 2025-09-06 |
|  | 5 | Brendan Allen | 2123 | 229 | 16-4 | 2026-10-10 |
| Light Heavyweight | 1 | Magomed Ankalaev | 2188 | 242 | 13-2-1 | 2026-07-25 |
|  | 2 | Robert Whittaker | 2156 | 231 | 18-7 | 2026-07-11 |
|  | 3 | Carlos Ulberg | 2126 | 273 | 10-1 | 2026-04-11 |
|  | 4 | Paulo Costa | 2107 | 268 | 8-4 | 2026-04-11 |
|  | 5 | Dominick Reyes | 2063 | 237 | 11-5 | 2026-10-24 |
| Heavyweight | 1 | Ciryl Gane | 2350 | 260 | 12-2 | 2026-11-14 |
|  | 2 | Alexander Volkov | 2247 | 231 | 15-5 | 2026-10-24 |
|  | 3 | Alex Pereira | 2268 | 255 | 10-3 | 2026-06-14 |
|  | 4 | Tom Aspinall | 2279 | 303 | 8-1 | 2025-10-25 |
|  | 5 | Curtis Blaydes | 2162 | 239 | 15-6 | 2026-09-12 |
| Women's Strawweight | 1 | Tatiana Suarez | 2021 | 295 | 10-1 | 2026-11-07 |
|  | 2 | Virna Jandiroba | 1834 | 243 | 9-5 | 2026-11-07 |
|  | 3 | Mackenzie Dern | 1797 | 231 | 12-5 | 2026-08-15 |
|  | 4 | Gillian Robertson | 1785 | 232 | 14-7 | 2026-08-15 |
|  | 5 | Jessica Andrade | 1753 | 221 | 17-13 | 2025-08-16 |
| Women's Flyweight | 1 | Valentina Shevchenko | 1998 | 256 | 15-3-1 | 2025-11-15 |
|  | 2 | Zhang Weili | 1981 | 258 | 10-3 | 2025-11-15 |
|  | 3 | Erin Blanchfield | 1984 | 286 | 8-2 | 2026-10-17 |
|  | 4 | Natalia Silva | 2007 | 311 | 9-0 | 2026-10-03 |
|  | 5 | Manon Fiorot | 1961 | 288 | 8-2 | 2026-09-12 |
| Women's Bantamweight | 1 | Kayla Harrison | 2165 | 401 | 4-0 | 2026-11-14 |
|  | 2 | Amanda Nunes | 1981 | 280 | 16-3 | 2026-11-14 |
|  | 3 | Luana Santos | 1846 | 323 | 7-1 | 2026-10-31 |
|  | 4 | Ketlen Vieira | 1773 | 251 | 10-5 | 2026-05-16 |
|  | 5 | Julianna Pena | 1821 | 307 | 8-4 | 2025-06-07 |

## Current model fit

- Fitted on 5394 fights from 2016–2026.
- Market blend: 80% weight on the de-vigged price, total slope 1.28 (above 1 stretches favorites, correcting the favorite-longshot bias). Without a price: slope 1.02 on the model alone.
- Strongest win-model inputs (log-odds per standard deviation, A minus B): age -0.28, glicko_logit +0.21, strike_matchup +0.18, debut -0.13, age_decline -0.11, sapm -0.09.
