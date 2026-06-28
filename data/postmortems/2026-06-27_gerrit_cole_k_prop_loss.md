# SharpEdge MLB K Prop Postmortem — 2026-06-27

## Position Summary

**Date:** 2026-06-27  
**Book:** William Hill  
**Game:** New York Yankees at Boston Red Sox  
**Pitcher:** Gerrit Cole  
**Market:** Pitching Strikeouts  

| Target | Entry Odds | Stake | To Win | Paid | Profit/Loss | Final Ks | Outcome |
|---|---:|---:|---:|---:|---:|---:|---|
| 6+ Strikeouts | +122 | $5.00 | $6.10 | $0.00 | -$5.00 | 5 | LOSS |

**Total Risk:** $5.00  
**Total Paid:** $0.00  
**Net Profit/Loss:** -$5.00  
**Final Strikeouts:** 5  
**Portfolio Outcome:** 0-1

---

## Pregame Model Snapshot

| Metric | Projection |
|---|---:|
| Mean | 6.0 Ks |
| Median | 6 Ks |
| Raw Hit Probability: 6+ | 55-59% |
| Adjusted Hit Probability: 6+ | 50-54% |
| Market Implied Probability | 45.0% |
| Estimated Edge | +5 to +9 pts adjusted |
| Grade | B / B+ |

```yaml
position:
  date: 2026-06-27
  sport: MLB
  market_type: pitcher_strikeouts
  pitcher: Gerrit Cole
  team: New York Yankees
  opponent: Boston Red Sox
  book: William Hill
  target: 6_plus_strikeouts
  odds: 122
  stake: 5.00
  to_win: 6.10
  paid: 0.00
  profit: -5.00
  result_strikeouts: 5
  outcome: LOSS
```

---

## Final Pitching Line

| IP | H | R | ER | BB | K | HR | ERA | Pitches-Strikes | BF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5.1 | 7 | 4 | 4 | 1 | 5 | 2 | 6.75 | 89-61 | 24 |

---

## Core Performance Metrics

| Metric | Result |
|---|---:|
| Total Pitches | 89 |
| Strikes | 61 |
| Strike Rate | 69% |
| Batters Faced | 24 |
| Swings | 46 |
| Called Strikes | 14 |
| Whiffs | 6 |
| CStr+Whiff | 20 / 89 |
| CSW | 22% |
| Whiff / Swing | 13% |
| Zone Rate | 54% |
| Chase Rate | 39% |
| First-Pitch Strike | 71% |
| Average EV Allowed | 92.3 mph |
| Hard-Hit BBE | 9 |
| Top EV Marker | 114.4 mph |
| Velo Marker | 99.6 mph |

---

## Pitch Mix

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CStr+Whiff |
|---|---:|---:|---:|---:|---:|---:|---:|
| 4-Seam Fastball | 29% / 26 | 97.2 | 1 | 15 | 3 | 2 | 19% |
| Knuckle Curve | 22% / 20 | 83.4 | 1 | 8 | 4 | 0 | 20% |
| Changeup | 18% / 16 | 86.7 | 2 | 11 | 0 | 3 | 19% |
| Slider | 17% / 15 | 89.2 | 0 | 7 | 4 | 1 | 33% |
| Sinker | 13% / 12 | 96.7 | 1 | 5 | 3 | 0 | 25% |
| All | 100% / 89 | 90.8 | 5 | 46 | 14 | 6 | 22% |

---

## What Happened

Cole finished with 5 strikeouts and missed the 6+ ticket by one strikeout. This was a threshold loss, but not the same shape as the Peralta one-K miss. Cole had command and zone presence, but the swing-and-miss profile was not strong enough to support the plus-money 6+ path.

The best signal was his control: 69% strike rate, 71% first-pitch strike rate, and only 1 walk. The damaging signal was that Boston produced 9 hard-hit batted balls, 7 hits, 2 homers, and only allowed 6 whiffs on 46 swings. Cole was around the zone, but Boston did enough damage and contact suppression was too weak for a clean 6+ conversion.

---

## Model Diagnosis

### Confirmed

1. **Command was stable.** Cole threw 61 strikes on 89 pitches and walked only 1 batter.
2. **Runway was partially present.** 5.1 IP and 24 batters faced gave the ticket a plausible path.
3. **Soft threshold was correct.** The safer 5+ market would have cashed. The 6+ market was the plus-money lane and carried threshold volatility.

### Missed / Weakened

1. **Whiff conversion failed.** Cole generated only 6 whiffs on 46 swings.
2. **CSW floor failed.** Actual CSW was 22%, below the preferred 6+ floor.
3. **Contact damage was underestimated.** 9 hard-hit BBE and 2 HR created pressure on leash and efficiency.
4. **Fastball K conversion was weak.** The 4-seam produced only 1 K and 19% CStr+Whiff.
5. **Boston contact resistance was underestimated.** Boston did not chase poorly; they chased enough, but made too much contact when they swung.

---

## Boston LRS Update

```yaml
lineup_resistance_update:
  opponent: Boston Red Sox
  archetype: veteran_rhp_power_fastball_mix
  current_signal:
    - Gerrit Cole 2026-06-27: 5.1 IP, 5 K, 22% CSW, 13% whiff/swing, 9 hard-hit BBE, 2 HR
  adjustment:
    red_sox_lrs_vs_power_rhp: increase_by_0.3_to_0.5
    red_sox_contact_damage_modifier: increase
    red_sox_whiff_resistance_modifier: slight_increase
  reason: >
    Boston allowed strike-zone command but converted swings into contact and damage,
    suppressing Cole's whiff efficiency and creating a one-K threshold miss.
```

---

## Patch Recommendation

```yaml
patch_recommendation:
  name: plus_money_threshold_vs_soft_threshold_split
  action: strengthen
  description: >
    When a pitcher projects with mean and median exactly on the betting threshold,
    separate safer soft-threshold probability from plus-money threshold volatility.
    If the soft threshold is juiced but high probability and the plus threshold is plus-money,
    classify the plus threshold as small-stake only unless CSW and whiff floors are clearly above target.
  example:
    cole_2026_06_27:
      safer_market: 5_plus
      result: would_have_won
      plus_market: 6_plus
      result: lost_by_one
```

```yaml
patch_recommendation_2:
  name: whiff_per_swing_gate_for_6plus
  action: add
  description: >
    For 6+ K positions, require either projected whiff/swing strength or multiple bat-missing pitch families.
    Strike rate alone is not enough. If the pitcher projects as command-stable but contact-damage vulnerable,
    reduce the 6+ probability and prefer 5+ or live confirmation.
  thresholds:
    preferred_whiff_per_swing: 26_percent_or_higher
    caution_zone: 21_to_25_percent
    downgrade_zone: below_21_percent
```

```yaml
patch_recommendation_3:
  name: contact_damage_runway_gate_confirmed
  action: strengthen
  description: >
    High strike rate and first-pitch strike rate do not guarantee K conversion when hard-hit damage is elevated.
    If opponent has power/contact resistance, require stronger whiff support before approving 6+ or higher.
```

---

## Threshold Lesson

This was a **one-K miss** caused by weak whiff conversion and contact damage, not command collapse.

- 5+ would have won.
- 6+ lost by one.
- 7+ would have lost.
- The model correctly identified a path but overrated the ceiling probability.

```yaml
threshold_lesson:
  result_type: one_k_miss
  failed_target: 6_plus
  classification: whiff_conversion_contact_damage_failure
  command_read: confirmed
  runway_read: partial_confirmed
  csw_read: failed
  contact_suppression_read: failed
  market_selection: acceptable_but_high_variance
  future_rule: >
    When mean and median sit exactly at 6, do not upgrade 6+ solely because of plus money.
    Require CSW and whiff/swing confirmation, or choose the softer 5+ market if price is not prohibitive.
```

---

## Final Classification

```yaml
postmortem_classification:
  signal: mixed
  failure_type: whiff_conversion_contact_damage_failure
  command_read: confirmed
  leash_read: partial_confirmed
  contact_suppression_read: failed
  csw_read: failed
  opponent_lrs: slightly_underestimated
  market_selection: acceptable_but_threshold_sensitive
  ladder_exposure: none
  result: loss
  record: 0-1
  pnl: -5.00
  confidence_after_review: medium
  final_status: modify_threshold_selection
```

---

## Tags

`LOSS` `GERRIT_COLE` `WILLIAM_HILL` `6_PLUS_KS` `ONE_K_MISS` `WHIFF_CONVERSION_FAILURE` `CONTACT_DAMAGE` `BOSTON_LRS_UPGRADE` `CSW_FLOOR_GATE` `WHIFF_PER_SWING_GATE` `THRESHOLD_SELECTION_PATCH` `MODEL_MODIFY`
