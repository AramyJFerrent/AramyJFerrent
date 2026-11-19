# UFC fight predictions

Updated Thu Nov 19, 2026 04:46 PM ET. Refreshed automatically every day and several times on fight week; each bout's prediction is locked when its part of the card starts and graded once the result is in.

Each bout gets one consistent breakdown: each fighter's chance to win, split into KO/TKO, submission and decision, and the chance it ends in each round. The win chance blends the model with the betting market (about 81% market, the weight that has predicted best on past fights) and corrects the market's habit of underrating heavy favorites. MMA is high-variance: even the most likely single result is usually well under 50%.

The fair odds are the American odds that match the win chance with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook only offers value on a fighter when its price beats the fair line.

The three edge columns value every side of each market at its posted price: expected value (EV) is the average profit per $1 staked, from the final prediction: the win chance blended with the moneyline (which corrects the market's habit of underrating heavy favorites), and method and round chances anchored to their own props, moved only by what the blend changes. A side is an edge when its EV is at least 3%; each cell names the best side if one clears that bar, with its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, at most 3 units on one bout; else "no edge". Moneylines and props are never priced near -110, so a missing price is never assumed: without one, the round-total cell shows the model's fair odds at the line closest to even and the method cell each fighter's fair KO/TKO, submission and decision odds. Over 1.5 rounds means the fight passes 2:30 of round 2 (a decision is always over); finishes are assumed spread evenly within a round.

See the backtest (backtest.md) for how these edges did against the dataset's closing prices, next to the model alone, which finds a 3% edge in most fights and lost money on them. Treat these columns as a live test, tracked below, not as betting advice.

## UFC Fight Night: Procházka vs. Stirling

Saturday, November 21, 2026 · first bout locks Sat Nov 21, 10:00 AM ET

| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | Most likely result | Moneyline edge | Round total edge | Method edge |
|---|---|---|---|---|---|---|---|---|---|---|
| **Jiří Procházka** vs. **Navajo Stirling**<br>LHW, 5 rds | Procházka 34% – 66% Stirling | +190 / -190 | Procházka 39% (+145 / -175) | Procházka 32% (+215) | Procházka 23% / 2% / 9%<br>Stirling 49% / 4% / 13% | 21% | Stirling by KO/TKO (49%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Procházka +330 / +3945 / +1055<br>Stirling +105 / +2285 / +695 |
| **Aljamain Sterling** vs. **Kevin Vallejos**<br>FW, 3 rds | Sterling 43% – 57% Vallejos | +130 / -130 | Sterling 45% (+114 / -135) | Sterling 43% (+130) | Sterling 7% / 5% / 32%<br>Vallejos 25% / 3% / 29% | 61% | Sterling by decision (32%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Sterling +1380 / +2055 / +215<br>Vallejos +305 / +3165 / +245 |
| **Dan Hooker** vs. **Brian Ortega**<br>LW, 3 rds | Hooker 63% – 37% Ortega | -170 / +170 | Hooker 63% (-192 / +160) | Hooker 46% (+115) | Hooker 27% / 9% / 27%<br>Ortega 14% / 9% / 14% | 41% | Hooker by decision (27%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Hooker +275 / +990 / +275<br>Ortega +615 / +970 / +615 |
| **Kyoji Horiguchi** vs. **Asu Almabayev**<br>FLW, 3 rds | Horiguchi 62% – 38% Almabayev | -165 / +165 | Horiguchi 64% (-198 / +164) | Horiguchi 43% (+135) | Horiguchi 13% / 12% / 38%<br>Almabayev 5% / 15% / 18% | 56% | Horiguchi by decision (38%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Horiguchi +695 / +735 / +165<br>Almabayev +2035 / +575 / +455 |
| **Jared Cannonier** vs. **Ikram Aliskerov**<br>MW, 3 rds | Cannonier 22% – 78% Aliskerov | +350 / -350 | Cannonier 29% (+235 / -290) | Cannonier 21% (+375) | Cannonier 9% / 2% / 11%<br>Aliskerov 32% / 8% / 38% | 49% | Aliskerov by decision (38%) | Aliskerov (-290): EV +4.7%, 78%, stake 3.0u | no edge | no prices yet; fair KO / Sub / Dec<br>Cannonier +985 / +4705 / +820<br>Aliskerov +215 / +1105 / +165 |
| **Aleksandre Topuria** vs. **Santiago Luna**<br>BW, 3 rds | Topuria 69% – 31% Luna | -225 / +225 | Topuria 71% (-285 / +230) | Topuria 40% (+155) | Topuria 14% / 13% / 42%<br>Luna 8% / 4% / 19% | 61% | Topuria by decision (42%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Topuria +600 / +685 / +135<br>Luna +1160 / +2580 / +430 |
| **Shamil Gaziev** vs. **Tallison Teixeira**<br>HW, 3 rds | Gaziev 59% – 41% Teixeira | -145 / +145 | Gaziev 64% (-198 / +164) | Gaziev 29% (+245) | Gaziev 39% / 5% / 15%<br>Teixeira 25% / 3% / 13% | 27% | Gaziev by KO/TKO (39%) | Teixeira (+164): EV +8.0%, 41%, stake 1.2u | no edge | no prices yet; fair KO / Sub / Dec<br>Gaziev +155 / +1900 / +570<br>Teixeira +300 / +2815 / +695 |
| **Amir Albazi** vs. **Alessandro Costa**<br>FLW, 3 rds | Albazi 49% – 51% Costa | +105 / -105 | Albazi 50% (-108 / -112) | Albazi 49% (+105) | Albazi 11% / 9% / 28%<br>Costa 15% / 11% / 25% | 53% | Albazi by decision (28%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Albazi +770 / +955 / +255<br>Costa +580 / +775 / +305 |
| **Jake Matthews** vs. **Tahir Abdullayev**<br>WW, 3 rds | Matthews 71% – 29% Abdullayev | -240 / +240 | Matthews 69% (-245 / +210) | Matthews 56% (-130) | Matthews 22% / 12% / 37%<br>Abdullayev 9% / 5% / 16% | 52% | Matthews by decision (37%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Matthews +365 / +710 / +175<br>Abdullayev +1065 / +1850 / +535 |
| **Nikolas Motta** vs. **Dom Mar Fan**<br>LW, 3 rds | Motta 35% – 65% Fan | +190 / -190 | Motta 40% (+136 / -170) | Motta 28% (+265) | Motta 16% / 5% / 14%<br>Fan 28% / 8% / 29% | 43% | Fan by decision (29%) | Fan (-170): EV +4.0%, 65%, stake 1.7u | no edge | no prices yet; fair KO / Sub / Dec<br>Motta +535 / +2020 / +610<br>Fan +260 / +1110 / +240 |
| **Diyar Nurgozhay** vs. **Alik Lorenz**<br>LHW, 3 rds, UFC debut: Lorenz | Nurgozhay 72% – 28% Lorenz | -250 / +250 | Nurgozhay 68% (-245 / +200) | Nurgozhay 65% (-180) | Nurgozhay 44% / 6% / 21%<br>Lorenz 14% / 7% / 8% | 30% | Nurgozhay by KO/TKO (44%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Nurgozhay +130 / +1445 / +365<br>Lorenz +625 / +1420 / +1135 |
| **Shoaib Yousaf** vs. **John Mitchell**<br>LW, 3 rds, UFC debut: Yousaf, UFC debut: Mitchell | Yousaf 50% – 50% Mitchell | +100 / +100 | no line yet | Yousaf 50% (+100) | Yousaf 17% / 11% / 22%<br>Mitchell 17% / 11% / 22% | 45% | Yousaf by decision (22%) | no line yet | no price yet; fair Over 2.5 +105, Under -105 | no prices yet; fair KO / Sub / Dec<br>Yousaf +485 / +850 / +345<br>Mitchell +485 / +850 / +345 |

When it ends (either fighter):

| Bout | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Decision |
|---|---|---|---|---|---|---|
| Procházka vs. Stirling | 33% | 22% | 13% | 6% | 5% | 21% |
| Sterling vs. Vallejos | 19% | 13% | 7% |  |  | 61% |
| Hooker vs. Ortega | 32% | 19% | 9% |  |  | 41% |
| Horiguchi vs. Almabayev | 22% | 15% | 8% |  |  | 56% |
| Cannonier vs. Aliskerov | 26% | 17% | 8% |  |  | 49% |
| Topuria vs. Luna | 19% | 13% | 7% |  |  | 61% |
| Gaziev vs. Teixeira | 42% | 21% | 9% |  |  | 27% |
| Albazi vs. Costa | 24% | 15% | 8% |  |  | 53% |
| Matthews vs. Abdullayev | 24% | 16% | 8% |  |  | 52% |
| Motta vs. Fan | 30% | 18% | 9% |  |  | 43% |
| Nurgozhay vs. Lorenz | 40% | 21% | 9% |  |  | 30% |
| Yousaf vs. Mitchell | 29% | 18% | 9% |  |  | 45% |

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

## Top fighters by division

Glicko-2 rating from UFC results, with finishes counting as clearer wins than decisions. ± is two rating deviations (fighters with few or old fights are less certain), and the ranking uses the rating minus that margin so an unproven fighter does not top a division on one big win. Active fighters only (a fight in the last two years).

| Division | # | Fighter | Rating | ± | UFC record | Last fight |
|---|---|---|---|---|---|---|
| Flyweight | 1 | Manel Kape | 1978 | 284 | 8-3 | 2026-06-20 |
|  | 2 | Joshua Van | 1942 | 261 | 11-1 | 2026-09-19 |
|  | 3 | Brandon Moreno | 1895 | 237 | 12-7-2 | 2026-09-12 |
|  | 4 | Alexandre Pantoja | 1894 | 238 | 14-5 | 2026-09-19 |
|  | 5 | Tatsuro Taira | 1963 | 318 | 8-2 | 2026-05-09 |
| Bantamweight | 1 | Petr Yan | 2147 | 228 | 13-4 | 2026-10-24 |
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
|  | 4 | Jiri Prochazka | 2174 | 329 | 6-3 | 2026-04-11 |
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
|  | 4 | Ketlen Vieira | 1773 | 250 | 10-5 | 2026-05-16 |
|  | 5 | Julianna Pena | 1821 | 307 | 8-4 | 2025-06-07 |

## Current model fit

- Fitted on 5382 fights from 2016–2026.
- Market blend: 81% weight on the de-vigged price, total slope 1.27 (above 1 stretches favorites, correcting the favorite-longshot bias). Without a price: slope 1.02 on the model alone.
- Strongest win-model inputs (log-odds per standard deviation, A minus B): age -0.28, glicko_logit +0.21, strike_matchup +0.18, debut -0.13, age_decline -0.12, sapm -0.09.
