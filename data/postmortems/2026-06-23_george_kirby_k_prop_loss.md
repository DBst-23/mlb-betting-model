# SharpEdge MLB K Prop Postmortem — 2026-06-23

## Position Summary

**Date:** 2026-06-23  
**Book:** William Hill  
**Game:** Seattle Mariners at Pittsburgh Pirates  
**Pitcher:** George Kirby  
**Market:** Total Pitching Strikeouts  
**Target:** Over 5.5 Ks / 6+  
**Entry Odds:** +116  
**Cash Wagered:** $10.00  
**To Win:** $11.60  
**Paid:** $0.00  
**Profit/Loss:** -$10.00  
**Final Strikeouts:** 5  
**Outcome:** LOSS

---

## Pregame Model Snapshot

| Metric | Projection |
|---|---:|
| Mean | 6.0 K |
| Median | 6 K |
| Hit Probability | 55-58% |
| Market Implied Probability | 46.3% |
| Estimated Edge | +8.7 to +11.7 percentage points |
| Grade | A |
| Position Type | Command-runway plus-price edge |

```yaml
position:
  date: 2026-06-23
  sport: MLB
  market_type: pitcher_strikeouts
  pitcher: George Kirby
  team: Seattle Mariners
  opponent: Pittsburgh Pirates
  book: William Hill
  target: over_5_5_strikeouts
  equivalent_ladder: 6_plus_strikeouts
  entry_odds: 116
  stake_type: cash
  stake: 10.00
  paid: 0.00
  profit: -10.00
  result_strikeouts: 5
  outcome: LOSS
```

---

## Final Pitching Line

| IP | H | R | ER | BB | K | HR | Pitches-Strikes | BF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6.0 | 8 | 2 | 1 | 2 | 5 | 0 | 91-65 | 27 |

---

## Core Performance Metrics

| Metric | Result |
|---|---:|
| Total Pitches | 91 |
| Strikes | 65 |
| Strike Rate | 71% |
| Batters Faced | 27 |
| Swings | 52 |
| Called Strikes | 13 |
| Whiffs | 8 |
| CStr+Whiff | 21 / 91 |
| CSW | 23% |
| Whiff / Swing | 15% |
| Zone Rate | 56% |
| Chase Rate | 33% |
| First-Pitch Strike | 74% |
| Average EV Allowed | 87.5 mph |
| Hard-Hit BBE | 9 |
| Top EV Marker | 106.3 |
| Velo Marker | 99.1 |

---

## Pitch Mix

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CStr+Whiff |
|---|---:|---:|---:|---:|---:|---:|---:|
| Sweeper | 46% / 42 | 87.9 | 5 | 19 | 9 | 6 | 36% |
| Sinker | 21% / 19 | 97.7 | 0 | 14 | 2 | 2 | 21% |
| 4-Seam Fastball | 14% / 13 | 97.6 | 0 | 10 | 1 | 0 | 8% |
| Knuckle Curve | 9% / 8 | 84.6 | 0 | 5 | 0 | 0 | 0% |
| Changeup | 5% / 5 | 89.2 | 0 | 2 | 1 | 0 | 20% |
| Cutter | 4% / 4 | 94.5 | 0 | 2 | 0 | 0 | 0% |
| All | 100% / 91 | 91.4 | 5 | 52 | 13 | 8 | 23% |

---

## What Happened

Kirby gave the model the expected runway: 6.0 innings, 91 pitches, 27 batters faced, 71% strike rate, and 74% first-pitch strikes. The loss did not come from leash failure. It came from insufficient whiff conversion outside the sweeper.

The sweeper carried the entire K profile with all 5 strikeouts and a 36% CStr+Whiff rate. Every other pitch combined for 0 strikeouts. The four-seam and sinker velocity was strong, but the fastball family did not generate enough swing-and-miss to push Kirby from 5 Ks to 6 Ks.

---

## Model Diagnosis

### Confirmed

1. **Runway projection was correct.** Kirby reached 6.0 IP, 91 pitches, and 27 batters faced.
2. **Command profile was correctly identified.** Strike rate and first-pitch strike rate were strong.
3. **Price discipline was logical.** +116 implied 46.3%, while the pregame model had the 6+ probability at 55-58%.

### Missed / Weakened

1. **Whiff sustainability was overestimated.** Overall whiff/swing was only 15%.
2. **Non-sweeper K support was absent.** Sinker, 4-seam, curve, changeup, and cutter produced 0 Ks.
3. **Pirates contact resistance was stronger than modeled.** Pittsburgh created enough balls in play and foul-ball resistance to hold Kirby to 5 Ks despite full runway.
4. **Hard-hit count was elevated.** 9 hard-hit BBE created inning stress even though average EV was manageable.

---

## LRS / Opponent Adjustment Review

```yaml
lineup_resistance_review:
  expected_lrs: 4.7
  actual_behavior: higher_resistance_than_expected
  drivers:
    - contact_rate_better_than_projection
    - low_whiff_response_to_fastball_family
    - enough balls_in_play_to_prevent_extra_k_conversion
    - elevated hard_hit_count
  adjustment:
    pirates_lrs_vs_command_righties: increase_by_0.3_to_0.5
```

The Pirates should receive a small upward LRS adjustment against command-first right-handed pitchers when the pitcher does not have multiple secondary weapons producing Ks. Kirby's sweeper was excellent, but the rest of the arsenal did not provide ladder support.

---

## Patch Recommendation

```yaml
patch_recommendation:
  name: non_primary_pitch_k_support_check
  action: add
  description: >
    Before attacking 6+ on command-first pitchers, require at least two pitch families
    with projected K conversion or a recent CSW profile above threshold. If only one
    pitch is carrying the K path, cap confidence unless opponent LRS is clearly weak.
  effect:
    - reduce false confidence on 6+ thresholds
    - improve pitcher K ladder selection
    - separate runway edges from whiff-conversion edges
```

---

## Threshold Lesson

This was a classic **right pitcher, wrong rung** outcome.

- Kirby 5+ would have cashed.
- Kirby O5.5 / 6+ lost by one strikeout.
- The model correctly identified innings runway but overstated the 6+ conversion rate.

```yaml
threshold_lesson:
  result_type: one_k_short
  correct_soft_threshold: 5_plus
  failed_threshold: 6_plus
  classification: threshold_miss_not_leash_miss
  future_rule: >
    If projected mean equals exactly 6.0 and median equals 6, require stronger
    multi-pitch whiff support before paying for O5.5 or 6+.
```

---

## Final Classification

```yaml
postmortem_classification:
  signal: weakened
  failure_type: whiff_conversion_shortfall
  leash_read: confirmed
  command_read: confirmed
  opponent_lrs: underestimated
  market_selection: acceptable_but_threshold_sensitive
  result: loss
  pnl: -10.00
  confidence_after_review: medium
  final_status: modify
```

---

## Tags

`LOSS` `GEORGE_KIRBY` `WILLIAM_HILL` `OVER_5_5_KS` `ONE_K_SHORT` `THRESHOLD_MISS` `LEASH_CONFIRMED` `COMMAND_CONFIRMED` `WHIFF_CONVERSION_SHORTFALL` `PIRATES_LRS_UPGRADE` `NON_PRIMARY_PITCH_K_SUPPORT_PATCH` `MODEL_MODIFY`
