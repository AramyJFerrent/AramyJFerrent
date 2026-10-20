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
3. Reads the cards for the next 15 days from ESPN: every announced bout, when
   its part of the card starts, and DraftKings moneylines from ESPN's odds
   API, plus round-total and method-of-victory prices when ESPN posts them.
   Fighters are matched to the UFCStats history by name; anyone with no UFC
   bouts is a debutant. UFCStats' own upcoming pages are used when they
   can be read (they answer GitHub's runners with a browser check), and
   `data/manual_card.csv` adds or overrides bouts by hand.
4. Predicts every bout that has not started, values the betting edge on
   each market (see below) and writes it to `predictions/log.csv`, replacing
   the earlier prediction for that bout. A
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
| Cards | ESPN's scoreboard (bouts, start times, divisions, scheduled rounds, belts) and odds API (moneylines tied to each fighter by id, round totals, and method props from its `propBets` link), names matched to the history; UFCStats upcoming pages when reachable; a hand-edited card for anything the sites miss | `cards.py`, `names.py` |
| Edges | Expected value of every side of the moneyline, round total and method markets at the posted price, from the model alone; an edge needs EV of at least 3% | `edges.py` |
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

## Betting edges

The predictions page has three edge columns per bout: moneyline, round total
(over/under x.5 rounds) and method of victory (each fighter by KO/TKO,
submission or decision). Each side of each market is valued at its posted
price by expected value, the average profit per $1 staked:
`EV = p × (decimal odds − 1) − (1 − p − push)`. The probabilities come from
the model alone, before the blend with the betting market: the "model alone"
win chance, with the method and round models rerun on it (the method model
takes the win chance as an input, so this is not a rescaling of the blended
split). The best side is an edge when its EV is at least 3%.

- Round totals: over 1.5 rounds means the fight passes 2:30 of round 2, and a
  decision is always over. The model gives the chance of a finish in each
  round but not when within it, so finishes are assumed spread evenly over
  the five minutes (since 2015 about 45% came in the first half of their
  round, so this slightly understates overs).
- Prices are never assumed: without one, the moneyline cell says "no line
  yet", the round-total cell gives the model's fair odds at the x.5 line
  closest to even, and the method cell each fighter's fair KO/TKO,
  submission and decision odds.
- Edges are logged with the prediction, frozen when the bout starts, graded
  after the result (a no contest voids every bet; a draw refunds the
  moneyline and loses method bets) and tracked per market on the page.

In the walk-forward backtest, at the dataset's moneylines and method props
(round totals have no historical prices):

| Market | Edges | ROI | 95% range | Model's average EV |
|---|---|---|---|---|
| Moneyline | 3,972 of 4,986 fights | −7.4% | −11.7% to −3.3% | +37.8% |
| Method of victory | 4,244 of 4,488 fights | −15.7% | −23.3% to −7.9% | +61.6% |

The model alone is well behind the market (log loss 0.643 against 0.609), so
it disagrees with the price on nearly every fight and those disagreements
lose: what it knows that the market does not is outweighed by what the market
knows that it does not. The edges are tracked live as a test of the model,
not as betting advice. (The blended final prediction, about 80% market, does
beat the closing price slightly on log loss, but it is not what the edges use.)

## Running it yourself

Python 3.11 or newer.

```bash
cd UFCFightPredictor
pip install -r requirements.txt

python -m ufcpredictor update             # refresh, predict the next 15 days of cards, grade results
python -m ufcpredictor card               # show the upcoming cards as read from UFCStats and ESPN
python -m ufcpredictor card --raw         # ...plus the raw pages, odds items and prop bets ESPN returned
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
| `predictions/log.csv` | Every prediction (the last one before the fight): the blended and model-alone probabilities, the prices, each market's edge (`moneyline_edge_*`, `rounds_edge_*`, `method_edge_*`), and the result once known |
| `predictions/ratings.csv` | Glicko-2 ratings of every active fighter |
| `predictions/model.json` | Fitted coefficients, blend weights, method base rates and round hazards |
| `data/bouts.csv`, `data/fight_stats.csv`, `data/fighters.csv` | The reduced UFCStats history |
| `data/odds_log.csv` | Every price the predictor has seen (moneylines, method props, round totals), with when it saw it |

## Not modeled yet

- Full professional records. Debutants start from an average rating with a
  wide deviation and a debut term, and the market blend brings in what the
  price knows about their regional careers. Sherdog and Tapology records would
  help, but those sites' terms rule out scraping them here.
- Method and round props as an input to the prediction. They are read for
  the edge columns when ESPN posts them, but props are where the model trails
  the market most.
- Fight-week news beyond the card itself: missed weight, short-notice
  replacements as a feature, and injuries reach the prediction only through
  the price.
- The report's gradient-boosting and fight-simulation variants. With about
  500 fights a year, the ridge logistic model was the safer start.

## Data

Fight results and statistics from [UFCStats](http://ufcstats.com), via the
[Scrape UFC Stats](https://github.com/Greco1899/scrape_ufc_stats) repository.
Historical odds from the [Ultimate UFC Dataset](https://github.com/shortlikeafox/ultimate_ufc_dataset).
Upcoming cards, start times and prices from ESPN's public scoreboard and odds
API (prices from its sportsbook partner, DraftKings).
