# UFC fight predictions

Updated Sat Nov 21, 2026 03:13 PM ET. Refreshed automatically every day and several times on fight week; each bout's prediction is locked when its part of the card starts and graded once the result is in.

Each bout gets one consistent breakdown: each fighter's chance to win, split into KO/TKO, submission and decision, and the chance it ends in each round. The win chance blends the model with the betting market (about 81% market, the weight that has predicted best on past fights) and corrects the market's habit of underrating heavy favorites. MMA is high-variance: even the most likely single result is usually well under 50%.

The fair odds are the American odds that match the win chance with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook only offers value on a fighter when its price beats the fair line.

The three edge columns value every side of each market at its posted price: expected value (EV) is the average profit per $1 staked, from the final prediction: the win chance blended with the moneyline (which corrects the market's habit of underrating heavy favorites), and method and round chances anchored to their own props, moved only by what the blend changes. A side is an edge when its EV is at least 3%; each cell names the best side if one clears that bar, with its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, at most 3 units on one bout; else "no edge". Moneylines and props are never priced near -110, so a missing price is never assumed: without one, the round-total cell shows the model's fair odds at the line closest to even and the method cell each fighter's fair KO/TKO, submission and decision odds. Over 1.5 rounds means the fight passes 2:30 of round 2 (a decision is always over); finishes are assumed spread evenly within a round.

See the backtest (backtest.md) for how these edges did against the dataset's closing prices, next to the model alone, which finds a 3% edge in most fights and lost money on them. Treat these columns as a live test, tracked below, not as betting advice.

## UFC Fight Night: Adesanya vs Magomedov

Saturday, December 05, 2026 · first bout locks Sat Dec 5, 10:00 AM ET

| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | Most likely result | Moneyline edge | Round total edge | Method edge |
|---|---|---|---|---|---|---|---|---|---|---|
| **Israel Adesanya** vs. **Shara Magomedov**<br>MW, 5 rds | Adesanya 60% – 40% Magomedov | -150 / +150 | Adesanya 60% (-170 / +142) | Adesanya 46% (+120) | Adesanya 32% / 5% / 22%<br>Magomedov 23% / 4% / 13% | 36% | Adesanya by KO/TKO (32%) | no edge | no price yet; fair Over 2.5 -110, Under +110 | no prices yet; fair KO / Sub / Dec<br>Adesanya +215 / +1730 / +345<br>Magomedov +340 / +2385 / +640 |
| **Ian Machado Garry** vs. **Yaroslav Amosov**<br>WW, 3 rds | Garry 59% – 41% Amosov | -145 / +145 | Garry 61% (-175 / +145) | Garry 41% (+140) | Garry 18% / 6% / 36%<br>Amosov 4% / 20% / 17% | 53% | Garry by decision (36%) | no edge | no price yet; fair Over 2.5 -130, Under +130 | no prices yet; fair KO / Sub / Dec<br>Garry +465 / +1660 / +180<br>Amosov +2235 / +410 / +490 |
| **Serghei Spivac** vs. **Mario Pinto**<br>HW, 3 rds | Spivac 23% – 77% Pinto | +335 / -335 | no line yet | Spivac 23% (+335) | Spivac 8% / 3% / 12%<br>Pinto 34% / 13% / 29% | 41% | Pinto by KO/TKO (34%) | no line yet | no price yet; fair Over 2.5 +120, Under -120 | no prices yet; fair KO / Sub / Dec<br>Spivac +1150 / +2960 / +745<br>Pinto +195 / +645 / +240 |
| **Luke Riley** vs. **Gabriel Santos**<br>FW, 3 rds | Riley 64% – 36% Santos | -175 / +175 | no line yet | Riley 64% (-175) | Riley 28% / 4% / 31%<br>Santos 9% / 7% / 21% | 52% | Riley by decision (31%) | no line yet | no price yet; fair Over 2.5 -130, Under +130 | no prices yet; fair KO / Sub / Dec<br>Riley +250 / +2470 / +220<br>Santos +1040 / +1380 / +385 |
| **Mairon Santos** vs. **Akbar Abdullaev**<br>LW, 3 rds, UFC debut: Abdullaev | Santos 74% – 26% Abdullaev | -280 / +280 | no line yet | Santos 74% (-280) | Santos 31% / 8% / 34%<br>Abdullaev 8% / 4% / 14% | 49% | Santos by decision (34%) | no line yet | no price yet; fair Over 2.5 -110, Under +110 | no prices yet; fair KO / Sub / Dec<br>Santos +225 / +1080 / +195<br>Abdullaev +1205 / +2200 / +590 |
| **Magomed Tuchalov** vs. **Ion Cutelaba**<br>LHW, 3 rds | Tuchalov 59% – 41% Cutelaba | -145 / +145 | no line yet | Tuchalov 59% (-145) | Tuchalov 23% / 14% / 22%<br>Cutelaba 13% / 12% / 17% | 39% | Tuchalov by KO/TKO (23%) | no line yet | no price yet; fair Over 2.5 +130, Under -130 | no prices yet; fair KO / Sub / Dec<br>Tuchalov +340 / +595 / +355<br>Cutelaba +690 / +770 / +500 |
| **Bruno Silva** vs. **Jafel Filho**<br>FLW, 3 rds, UFC debut: Silva | Silva 45% – 55% Filho | +120 / -120 | no line yet | Silva 45% (+120) | Silva 9% / 11% / 25%<br>Filho 7% / 30% / 19% | 43% | Filho by submission (30%) | no line yet | no price yet; fair Over 2.5 +110, Under -110 | no prices yet; fair KO / Sub / Dec<br>Silva +990 / +785 / +305<br>Filho +1425 / +235 / +435 |
| **Uran Satybaldiev** vs. **Ivan Gnizditskiy**<br>LHW, 3 rds, UFC debut: Gnizditskiy | Satybaldiev 48% – 52% Gnizditskiy | +110 / -110 | no line yet | Satybaldiev 48% (+110) | Satybaldiev 22% / 14% / 12%<br>Gnizditskiy 25% / 9% / 19% | 31% | Gnizditskiy by KO/TKO (25%) | no line yet | no price yet; fair Over 1.5 -100, Under +100 | no prices yet; fair KO / Sub / Dec<br>Satybaldiev +350 / +630 / +760<br>Gnizditskiy +305 / +1070 / +425 |
| **Marco Tulio** vs. **JunYong Park**<br>MW, 3 rds | Tulio 59% – 41% Park | -145 / +145 | no line yet | Tulio 59% (-145) | Tulio 28% / 6% / 24%<br>Park 18% / 7% / 16% | 40% | Tulio by KO/TKO (28%) | no line yet | no price yet; fair Over 2.5 +125, Under -125 | no prices yet; fair KO / Sub / Dec<br>Tulio +255 / +1490 / +310<br>Park +450 / +1265 / +540 |
| **Pavel Andrusca** vs. **Mehemmedeli Osmanli**<br>BW, 3 rds | Andrusca 83% – 17% Osmanli | -480 / +480 | no line yet | Andrusca 83% (-480) | Andrusca 15% / 18% / 50%<br>Osmanli 5% / 3% / 10% | 60% | Andrusca by decision (50%) | no line yet | no price yet; fair Over 2.5 -175, Under +175 | no prices yet; fair KO / Sub / Dec<br>Andrusca +570 / +460 / +100<br>Osmanli +2080 / +3895 / +885 |
| **Modestino Rodrigues** vs. **Matthieu Letho Duclos**<br>MW, 3 rds, UFC debut: Rodrigues | Rodrigues 38% – 62% Duclos | +165 / -165 | no line yet | Rodrigues 38% (+165) | Rodrigues 14% / 7% / 16%<br>Duclos 34% / 8% / 21% | 37% | Duclos by KO/TKO (34%) | no line yet | no price yet; fair Over 1.5 -125, Under +125 | no prices yet; fair KO / Sub / Dec<br>Rodrigues +595 / +1285 / +515<br>Duclos +195 / +1230 / +385 |
| **Abdul Hussein** vs. **Hecher Sosa**<br>BW, 3 rds | Hussein 66% – 34% Sosa | -195 / +195 | no line yet | Hussein 66% (-195) | Hussein 18% / 23% / 25%<br>Sosa 8% / 3% / 22% | 48% | Hussein by decision (25%) | no line yet | no price yet; fair Over 2.5 -110, Under +110 | no prices yet; fair KO / Sub / Dec<br>Hussein +470 / +330 / +295<br>Sosa +1120 / +2935 / +345 |
| **Levan Chokheli** vs. **Islam Dulatov**<br>WW, 3 rds | Chokheli 47% – 53% Dulatov | +115 / -115 | no line yet | Chokheli 47% (+115) | Chokheli 24% / 3% / 19%<br>Dulatov 24% / 5% / 24% | 43% | Chokheli by KO/TKO (24%) | no line yet | no price yet; fair Over 2.5 +110, Under -110 | no prices yet; fair KO / Sub / Dec<br>Chokheli +315 / +2790 / +415<br>Dulatov +315 / +1835 / +325 |

When it ends (either fighter):

| Bout | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Decision |
|---|---|---|---|---|---|---|
| Adesanya vs. Magomedov | 23% | 18% | 12% | 6% | 5% | 36% |
| Garry vs. Amosov | 24% | 15% | 8% |  |  | 53% |
| Spivac vs. Pinto | 31% | 19% | 9% |  |  | 41% |
| Riley vs. Santos | 24% | 16% | 8% |  |  | 52% |
| Santos vs. Abdullaev | 26% | 17% | 8% |  |  | 49% |
| Tuchalov vs. Cutelaba | 33% | 19% | 9% |  |  | 39% |
| Silva vs. Filho | 30% | 18% | 9% |  |  | 43% |
| Satybaldiev vs. Gnizditskiy | 39% | 21% | 9% |  |  | 31% |
| Tulio vs. Park | 32% | 19% | 9% |  |  | 40% |
| Andrusca vs. Osmanli | 20% | 13% | 7% |  |  | 60% |
| Rodrigues vs. Duclos | 34% | 20% | 9% |  |  | 37% |
| Hussein vs. Sosa | 27% | 17% | 8% |  |  | 48% |
| Chokheli vs. Dulatov | 30% | 18% | 9% |  |  | 43% |

## How the 2026 predictions have done

| Predictor | Fights | Log loss | Brier | Winners |
|---|---|---|---|---|
| Final prediction | 501 | 0.6195 | 0.215 | 64.5% |
| Model alone (before the market) | 501 | 0.6379 | 0.223 | 62.7% |
| Glicko-2 rating alone | 501 | 0.6815 | 0.244 | 57.7% |
| Final, on fights with a price | 166 | 0.5402 | 0.181 | 74.1% |
| Market price when predicted | 166 | 0.5487 | 0.183 | 74.7% |
| Coin flip | 501 | 0.6931 | 0.250 | – |

Log loss scores the win chances (lower is better; a coin flip scores 0.693, and the betting market about 0.61). Brier is the squared error of the win chance. Picking every betting favorite already gets about two thirds of winners right, so the win rate says little on its own.

- Winner and method (six outcomes): log loss 1.575 on 500 fights, against 1.792 for guessing uniformly. The single most likely result happened 34% of the time.
- Went the distance: predicted 48% on average, actual 42%.

449 of these fights happened before the predictor went live. They are backfilled walk-forward (each fight predicted from earlier fights only, with models fitted on earlier years) using the odds dataset's approximate closing prices, which run only through March 2026, so later backfilled fights use the model alone. Every fight since is graded on the prediction logged before it started.

### Edge record

Every edge logged with a live prediction (the last one before the fight), at the stake and price logged with it; edges logged before edges were priced from the final prediction are left out. Pushes return the stake (a no contest voids every bet; a draw refunds the moneyline). Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised.

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Moneyline | 8 | 4-4-0 | 18.7 | -3.02 | -16.1% | +5.5% |
| Round total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Method of victory | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

### Latest results: UFC 334: Gane vs. Hokit

| Bout | Predicted | Result | Chance given to the winner | Chance given to the exact result |
|---|---|---|---|---|
| Ciryl Gane vs. Josh Hokit | Gane 69% | Ciryl Gane by decision | 69% | 17% |
| Kayla Harrison vs. Amanda Nunes | Harrison 64% | Kayla Harrison by submission, R4 | 64% | 22% |
| Caio Borralho vs. Yousri Belgaroui | Borralho 57% | Caio Borralho by decision | 57% | 31% |
| Uroš Medić vs. Kevin Holland | Medić 58% | draw | – | – |
| Bilal Hasan vs. Luis Gurule | Hasan 91% | Luis Gurule by decision | 9% | 5% |
| Stephen Thompson vs. Charles Radtke | Thompson 51% | Stephen Thompson by KO/TKO, R3 | 51% | 20% |
| Drew Dober vs. Chris Duncan | Duncan 67% | Chris Duncan by decision | 67% | 30% |
| Jim Miller vs. Terrance McKinney | McKinney 73% | Terrance McKinney by KO/TKO, R1 | 73% | 30% |
| Donte Johnson vs. Cesar Almeida | Johnson 72% | Cesar Almeida by KO/TKO, R1 | 28% | 8% |
| Jared Gordon vs. Melquizael Costa | Costa 81% | Melquizael Costa by decision | 81% | 30% |
| Macy Chiasson vs. Bia Mesquita | Mesquita 74% | Bia Mesquita by submission, R1 | 74% | 43% |
| Alatengheili vs. Juan Diaz | Diaz 84% | Juan Diaz by decision | 84% | 43% |
| Evan Elder vs. Samuel Sanches | Sanches 53% | Evan Elder by decision | 47% | 22% |

12 locked predictions are waiting for official results.

## Top fighters by division

Glicko-2 rating from UFC results, with finishes counting as clearer wins than decisions. ± is two rating deviations (fighters with few or old fights are less certain), and the ranking uses the rating minus that margin so an unproven fighter does not top a division on one big win. Active fighters only (a fight in the last two years).

| Division | # | Fighter | Rating | ± | UFC record | Last fight |
|---|---|---|---|---|---|---|
| Flyweight | 1 | Manel Kape | 1978 | 284 | 8-3 | 2026-06-20 |
|  | 2 | Joshua Van | 1942 | 261 | 11-1 | 2026-09-19 |
|  | 3 | Brandon Moreno | 1895 | 237 | 12-7-2 | 2026-09-12 |
|  | 4 | Alexandre Pantoja | 1894 | 238 | 14-5 | 2026-09-19 |
|  | 5 | Tatsuro Taira | 1963 | 318 | 8-2 | 2026-05-09 |
| Bantamweight | 1 | Petr Yan | 2147 | 229 | 13-4 | 2026-10-24 |
|  | 2 | Merab Dvalishvili | 2128 | 225 | 14-4 | 2026-10-24 |
|  | 3 | Song Yadong | 2064 | 225 | 13-4-1 | 2026-08-29 |
|  | 4 | Cory Sandhagen | 2059 | 232 | 11-6 | 2026-07-11 |
|  | 5 | Sean O'Malley | 2059 | 244 | 12-3 | 2026-06-14 |
| Featherweight | 1 | Alexander Volkanovski | 2214 | 226 | 16-3 | 2026-10-24 |
|  | 2 | Diego Lopes | 2145 | 268 | 7-3 | 2026-06-14 |
|  | 3 | Aljamain Sterling | 2097 | 229 | 18-5 | 2026-04-25 |
|  | 4 | Brian Ortega | 2062 | 272 | 8-5 | 2025-08-23 |
|  | 5 | Jean Silva | 2075 | 302 | 7-1 | 2026-09-12 |
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
|  | 4 | Jiri Prochazka | 2174 | 330 | 6-3 | 2026-04-11 |
|  | 5 | Paulo Costa | 2107 | 268 | 8-4 | 2026-04-11 |
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
|  | 2 | Amanda Nunes | 1981 | 279 | 16-3 | 2026-11-14 |
|  | 3 | Luana Santos | 1846 | 323 | 7-1 | 2026-10-31 |
|  | 4 | Ketlen Vieira | 1773 | 251 | 10-5 | 2026-05-16 |
|  | 5 | Julianna Pena | 1821 | 307 | 8-4 | 2025-06-07 |

## Current model fit

- Fitted on 5382 fights from 2016–2026.
- Market blend: 81% weight on the de-vigged price, total slope 1.27 (above 1 stretches favorites, correcting the favorite-longshot bias). Without a price: slope 1.02 on the model alone.
- Strongest win-model inputs (log-odds per standard deviation, A minus B): age -0.28, glicko_logit +0.21, strike_matchup +0.18, debut -0.13, age_decline -0.12, sapm -0.09.
