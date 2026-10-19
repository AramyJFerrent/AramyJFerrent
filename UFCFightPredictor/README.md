# UFC Fight Predictor

Predicts every UFC bout on the next cards: each fighter's chance to win,
split into KO/TKO, submission and decision, and the chance it ends in each
round. It keeps itself current all year. A scheduled GitHub Action pulls new
results, cards and prices every day (and several times on fight week),
refits the model, re-predicts bouts that have not started, drops bouts that
fall off a card, and grades each prediction once the result is in.

**Latest predictions: [`predictions/README.md`](predictions/README.md)**
· Backtest: [`predictions/backtest.md`](predictions/backtest.md)

The design follows the *UFC Fight Prediction: Techniques Report*: an
uncertainty-aware rating plus opponent-adjusted, shrunk style statistics in a
calibrated win model, blended with the de-vigged betting market, then split
into method and round so every bout gets one consistent breakdown.

## How it stays up to date

`.github/workflows/ufc-fight-predictor.yml` runs `python -m ufcpredictor update`:

| When (ET) | Why |
|---|---|
| Every morning, about 9:40 AM | New results in the UFCStats scrape, new cards, updated prices |
| Friday about 3:40 PM | After weigh-ins: late replacements and cancellations |
| Saturday about noon | Before afternoon cards abroad |
| Saturday about 3 PM | Final prices before US prelims |

Each run:

1. Downloads the UFCStats scrape (every UFC fight since 1994, round by round)
   and the odds dataset, and rebuilds the tables in `data/`.
2. Rebuilds every fighter's rating and style profile from the full history
   and refits the win, calibration, market-blend, method and round models on
   the last ten years, including every fight so far this year.
3. Reads the cards for the next 15 days: bouts and fighter ids from UFCStats,
   start times and moneylines from ESPN, plus anything in
   `data/manual_card.csv`.
4. Predicts every bout that has not started and writes it to
   `predictions/log.csv`, replacing the earlier prediction for that bout. A
   bout's prediction locks when its part of the card starts, so the logged
   one is always the last made before the fight. A bout that drops off its
   card is removed, and a replacement opponent gets a new prediction.
5. Appends any new prices to `data/odds_log.csv` with a timestamp, fills in
   results, and grades the year so far against the market.
6. Commits the results back to the repo (only when something besides a
   timestamp changed).

UFC has no offseason, so nothing needs doing between years: predictions are
graded by calendar year and the history keeps growing. It went live in
October 2026 and backfilled that year's earlier fights with walk-forward
predictions, labeled as such, so the year's grading starts populated.

**To turn the schedule on**, merge this folder and the workflow into the
repository's default branch (GitHub only runs scheduled workflows from there),
make sure Actions are enabled, and optionally start a first run from the
Actions tab with **Run workflow**.

## How it works

| Stage | What it does | Code |
|---|---|---|
| Data | The UFCStats scrape reduced to one row per bout and one per fighter per bout. Renamed events are deduplicated, and the nine names shared by two different fighters are told apart by weight class and age. | `data.py` |
| Ratings | Glicko-2 with one update per fight. The rating deviation grows with inactivity, so a long layoff makes a fighter less certain. A finish counts as a full win, a decision as 0.8 and a split decision as 0.5. A plain UFC-only Elo is kept as the baseline. | `ratings.py` |
| Style profiles | Striking and grappling rates (strikes landed and absorbed per minute, accuracy, defense, takedowns, submission attempts, control time, knockdowns) and finishing and durability rates. They are shrunk toward the division average, older fights fade with a 3-year half-life, and the main rates are opponent-adjusted: landing on someone who rarely gets hit counts for more. | `profiles.py` |
| Features | Built strictly from earlier fights, as A-minus-B differences: the Glicko log-odds, rating uncertainty, age and age past 33, reach, height, experience, UFC debut, layoff, striking and takedown matchups, defense, durability, streak, southpaw against orthodox, and weight-class moves. | `features.py` |
| Win model | Ridge logistic regression with no intercept, so swapping the corners exactly swaps the answer and it cannot learn which corner the favorite usually gets. | `model.py` |
| Market blend | Out-of-fold model log-odds blended with the de-vigged moneyline on the log-odds scale. The fitted weight is about 80% market, with a total slope of about 1.2–1.3 that stretches favorites, correcting the favorite-longshot bias. Bouts without a price use the model alone. | `model.py` |
| Method | For each fighter as the winner, a multinomial model over KO/TKO, submission and decision. It starts from the division's base rates (heavyweights get knocked out, strawweights go the distance) and adjusts for the winner's finishing record, the loser's durability, how big a favorite the winner is, and five-round and title fights. | `model.py` |
| Round | Per-round finish hazards for three- and five-round fights, shifted so the chance of a finish matches the method model. Big finishers finish earlier as well as more often. | `model.py` |
| Cards | UFCStats upcoming events (exact fighter ids), ESPN start times and prices (name-matched), and a hand-edited card for anything the sites miss | `cards.py`, `names.py` |
| Backtest | Walk-forward by year, scored next to the market on the same fights | `backtest.py` |

The win probability is settled first, and each fighter's three method
chances add up to it, so the six outcomes always sum to one. Rating and
profile settings were tuned on 2010–2014 fights (`python -m ufcpredictor tune`,
saved in `params.json`); everything else is refitted on every run.

## Backtest, 2015–2026

Every fight is predicted from earlier fights only, with all models fitted on
the ten years before its year. These are the 4,941 fights with a moneyline in
the Ultimate UFC Dataset (through March 2026).

| Predictor | Log loss | Brier | Winners |
|---|---|---|---|
| Final (model + market) | **0.6065** | **0.210** | 66.5% |
| Betting market (de-vigged) | 0.6089 | 0.211 | 65.8% |
| Model alone | 0.6432 | 0.226 | 63.0% |
| Glicko-2 rating alone | 0.6788 | 0.243 | 56.5% |
| Elo, UFC results only | 0.6825 | 0.245 | 55.2% |
| Coin flip | 0.6931 | 0.250 | – |

- The final prediction beats the market's own price: by 0.0024 log loss
  per fight, 95% interval 0.0005 to 0.0043, in a paired bootstrap. It is a
  small edge, but on a benchmark the report calls hard to beat.
- On its own, the model is far ahead of results-only ratings (Elo barely beats
  a coin flip, as the report found) but well behind the market, which knows
  debutants' regional records, injuries and camp news.
- Win chances are well calibrated: favorites given 75–80% won 77.4%.
- Method: six-way log loss 1.571, against 1.613 for division base rates and
  1.546 for de-vigged method props. It predicts the distance well (49.4%
  predicted, 49.6% actual, where props say 45.0%), but props know more about
  how a fight will end.
- Round: it beats division base rates for both three- and five-round fights.

## Can it beat the price?

One-unit moneyline bets whenever the final win chance beats the price's
implied chance, bookmaker margin included, by 2 points or more:

| Bets | Return per bet | 95% range | Share on favorites |
|---|---|---|---|
| 734 | +7.5% | +0.7% to +14.2% | 73% |

What this means:

- The edge comes from the favorite-longshot bias: heavy favorites win more
  often than their prices imply, and the blend's calibration stretches them.
  It held at every edge threshold tried (see backtest.md).
- Bets on the model's own view against the market lose about 7% a bet. The
  market knows more than the model about everything except that bias.
- It is not a proven money-maker. The thresholds were compared after the
  fact, the dataset does not say when its prices were captured or whether
  they are one book's or the best available, and the range above is wide.
  The predictions page flags these sides live and tracks their record on the
  prices it logged before each fight, which is the test that counts.

## Running it yourself

Python 3.11 or newer.

```bash
cd UFCFightPredictor
pip install -r requirements.txt

python -m ufcpredictor update             # refresh, predict the next 15 days of cards, grade results
python -m ufcpredictor card               # show the upcoming cards as read from UFCStats and ESPN
python -m ufcpredictor ratings --division Lightweight
python -m ufcpredictor backtest           # walk-forward 2015-2026, writes predictions/backtest.md
python -m ufcpredictor tune --save        # re-tune ratings and profiles on 2010-2014
python -m pytest -q tests
```

Downloads are cached in `.cache/` (ignored by git). To add or fix a bout by
hand, create `data/manual_card.csv`:

```csv
event,date,fighter_a,fighter_b,division,rounds,title,odds_a,odds_b,location
UFC Fight Night: One vs. Two,2026-10-24,Fighter One,Fighter Two,Lightweight,5,False,-150,130,"Las Vegas, Nevada, USA"
```

Manual rows replace the same bout from the other sources. Only `event`,
`date`, `fighter_a` and `fighter_b` are required.

## Outputs

| File | Contents |
|---|---|
| `predictions/README.md` | Upcoming cards, the year's grading, latest results, top fighters by division |
| `predictions/latest.json` | The same upcoming predictions as JSON |
| `predictions/log.csv` | Every prediction (the last one before the fight) with the result once known |
| `predictions/ratings.csv` | Glicko-2 ratings of every active fighter |
| `predictions/model.json` | Fitted coefficients, blend weights, method base rates and round hazards |
| `data/bouts.csv`, `data/fight_stats.csv`, `data/fighters.csv` | The reduced UFCStats history |
| `data/odds_log.csv` | Every price the predictor has seen, with when it saw it |

## Not modeled yet

- Full professional records. Debutants start from an average rating with a
  wide deviation and a debut term, and the market blend brings in what the
  price knows about their regional careers. Sherdog and Tapology records would
  help, but those sites' terms rule out scraping them here.
- Method and round props as an input. The ESPN feed carries moneylines only,
  and props are where the model trails the market most.
- Fight-week news beyond the card itself: missed weight, short-notice
  replacements as a feature, and injuries reach the prediction only through
  the price.
- The report's gradient-boosting and fight-simulation variants. With about
  500 fights a year, the ridge logistic model was the safer start.

## Data

Fight results and statistics from [UFCStats](http://ufcstats.com), via the
[Scrape UFC Stats](https://github.com/Greco1899/scrape_ufc_stats) repository.
Historical odds from the [Ultimate UFC Dataset](https://github.com/shortlikeafox/ultimate_ufc_dataset).
Upcoming start times and prices from ESPN's public scoreboard.
