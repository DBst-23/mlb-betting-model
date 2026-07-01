# SharpEdge MLB F5 Postmortem — 2026-06-30

## Position Summary

**Date:** 2026-06-30  
**Book:** William Hill  
**Game:** Texas Rangers at Cleveland Guardians  
**Market:** 1st 5 Innings Total Runs  
**Position:** Under 4  

| Market | Entry Odds | Stake | Paid | Profit/Loss | F5 Runs | Outcome |
|---|---:|---:|---:|---:|---:|---|
| F5 Under 4 | -115 | $2.50 | $2.50 | $0.00 | 4 | PUSH |

```yaml
position:
  date: 2026-06-30
  sport: MLB
  market_type: f5_total
  matchup: Texas Rangers at Cleveland Guardians
  book: William Hill
  target: under_4_first_5_innings
  odds: -115
  stake: 2.50
  paid: 2.50
  profit: 0.00
  result_f5_total_runs: 4
  outcome: PUSH
```

---

## F5 Scoring Path

| Inning | Event | Runs |
|---|---|---:|
| Bottom 1st | Chase DeLauter double, Kyle Manzardo HR | CLE 2 |
| Top 3rd | Nicky Lopez single, Joc Pederson HR | TEX 2 |
| Remaining F5 | No further scoring | 0 |
| **F5 Total** | — | **4** |

**Result:** Under 4 pushed exactly. Under 3.5 would have lost. Push protection was the correct market structure.

---

## Starter Summary

### Jacob deGrom

| IP | H | R | ER | BB | K | HR | Pitches-Strikes | BF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 7.0 | 4 | 2 | 2 | 0 | 9 | 1 | 96-69 | 25 |

| Metric | Result |
|---|---:|
| Strike Rate | 72% |
| CSW | 39% |
| Whiff/Swing | 36% |
| Chase Rate | 40% |
| Zone Rate | 51% |
| First-Pitch Strike | 76% |
| Avg EV Allowed | 91.7 mph |
| Hard-Hit BBE | 8 |
| Top EV Marker | 105.1 mph |
| Velo Marker | 100.5 mph |

### Tanner Bibee

| IP | H | R | ER | BB | K | HR | Pitches-Strikes | BF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 7.0 | 5 | 3 | 2 | 0 | 2 | 1 | 91-63 | 26 |

| Metric | Result |
|---|---:|
| Strike Rate | 69% |
| CSW | 26% |
| Whiff/Swing | 11% |
| Chase Rate | 33% |
| Zone Rate | 49% |
| First-Pitch Strike | 73% |
| Avg EV Allowed | 83.3 mph |
| Hard-Hit BBE | 6 |
| Top EV Marker | 108.1 mph |
| Velo Marker | 94.2 mph |

---

## Batter Event Notes — First Five Innings

Primary run events:

| Batter | Inning | Result | EV | LA | xBA | HR/Park |
|---|---:|---|---:|---:|---:|---:|
| Kyle Manzardo | 1 | Home Run | 101.7 | 26 | .690 | 16/30 |
| Chase DeLauter | 1 | Double | 102.7 | 13 | .910 | — |
| Nicky Lopez | 3 | Single | 96.8 | 9 | .590 | — |
| Joc Pederson | 3 | Home Run | 102.7 | 33 | .590 | 22/30 |

Notable hard-contact outs:

| Batter | Inning | Result | EV | xBA |
|---|---:|---|---:|---:|
| Jake Burger | 3 | Groundout | 108.1 | .180 |
| Evan Carter | 4 | Lineout | 104.0 | .510 |
| Travis Bazzana | 3 | Groundout | 100.0 | .280 |
| Patrick Bailey | 2 | Forceout | 98.3 | .110 |

---

## What Happened

The F5 Under 4 did not lose, but it also did not cash. The ticket pushed because the first five innings landed exactly on 4 runs. The scoring came from two isolated two-run swings rather than sustained offensive pressure.

The game script was largely correct: both starters worked deep, both avoided walks, and both limited extended rallies. deGrom was dominant after the early Manzardo HR and finished with 9 strikeouts, 0 walks, and a 39% CSW. Bibee also validated the decision to avoid his K prop: he threw 7 innings with only 2 strikeouts, but still kept Texas controlled enough for the F5 under framework to survive.

---

## Model Diagnosis

### Confirmed

1. **F5 structure was better than the inflated pitcher K market.**
2. **Push protection mattered.** Under 4 returned stake; Under 3.5 would have lost.
3. **Bibee K pass was correct.** He finished with only 2 strikeouts despite 7.0 IP.
4. **deGrom suppression was real.** 7.0 IP, 2 ER, 0 BB, 9 K, 39% CSW.
5. **Both starters had enough leash and run-prevention profile for an under look.**

### Missed / Weakened

1. **Early HR variance was underestimated.** Manzardo and Pederson both produced two-run homers.
2. **Hard-hit pockets were real.** deGrom allowed 8 hard-hit BBE and Bibee allowed 6.
3. **The total projection was directionally correct but slightly low.** Projected F5 total was around 3.1; actual landed 4.

---

## Patch Recommendation

```yaml
patch_recommendation:
  name: f5_isolated_hr_risk_overlay
  action: add
  description: >
    For F5 unders, add a first-three-innings power pocket overlay that flags lineups with
    2+ hitters capable of multi-run HR damage even when starter run-prevention profiles are strong.
  trigger:
    caution_if:
      - f5_total <= 4
      - both_starting_pitchers_projected_good
      - lineup_has_multiple_30_plus_hr_or_high_hard_hit_bats
      - park_hr_factor_or_batter_park_hr_fit_is_notable
```

```yaml
patch_recommendation_2:
  name: f5_push_number_priority
  action: keep_active
  description: >
    Prioritize push numbers such as F5 Under 4 over Under 3.5 when the projection edge is moderate.
    This ticket confirms that push protection can prevent a good-process under from becoming a loss.
```

---

## Threshold Lesson

```yaml
threshold_lesson:
  market_type: f5_total
  result_type: push
  final_total: 4
  key_lesson: >
    F5 Under 4 was structurally correct because it protected against exactly this type of outcome:
    two isolated HR events with no sustained scoring afterward.
  avoid_future_if:
    - only_available_total_is_3_5
    - both_lineups_have_multiple_early_power_pockets
    - wind_or_park_conditions_boost_home_runs
```

---

## Final Classification

```yaml
postmortem_classification:
  signal: stable
  market_type: f5_total
  result_type: push
  model_read: mostly_correct
  failure_type: isolated_home_run_variance
  deGrom_read: confirmed
  Bibee_run_prevention_read: confirmed
  Bibee_k_prop_pass: confirmed
  market_selection: correct
  push_protection: confirmed
  stake_sizing: correct
  result: push
  pnl: 0.00
  final_status: keep_f5_under_framework_active
```

---

## Tags

`PUSH` `F5_TOTAL` `TEX_CLE` `UNDER_4` `WILLIAM_HILL` `PUSH_PROTECTION` `DEGROM` `BIBEE` `ISOLATED_HR_VARIANCE` `GOOD_PROCESS` `F5_FRAMEWORK_ACTIVE`
