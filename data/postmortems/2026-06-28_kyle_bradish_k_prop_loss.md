# SharpEdge MLB K Prop Postmortem — 2026-06-28

## Position Summary

**Date:** 2026-06-28  
**Book:** William Hill  
**Game:** Washington Nationals at Baltimore Orioles  
**Pitcher:** Kyle Bradish  
**Market:** Pitching Strikeouts  

| Target | Entry Odds | Stake | To Win | Paid | Profit/Loss | Final Ks | Outcome |
|---|---:|---:|---:|---:|---:|---:|---|
| 7+ Strikeouts | +118 | $5.00 | $5.90 | $0.00 | -$5.00 | 2 | LOSS |

**Total Risk:** $5.00  
**Total Paid:** $0.00  
**Net Profit/Loss:** -$5.00  
**Final Strikeouts:** 2  
**Portfolio Outcome:** 0-1

---

## Pregame Model Snapshot

| Metric | Projection |
|---|---:|
| Mean | 6.5 Ks |
| Median | 6 Ks |
| Hit Probability: 7+ | 45-49% |
| Market Implied Probability | 45.9% |
| Estimated Edge | Fair to slight positive |
| Grade | B+ |

```yaml
position:
  date: 2026-06-28
  sport: MLB
  market_type: pitcher_strikeouts
  pitcher: Kyle Bradish
  team: Baltimore Orioles
  opponent: Washington Nationals
  book: William Hill
  target: 7_plus_strikeouts
  odds: 118
  stake: 5.00
  to_win: 5.90
  paid: 0.00
  profit: -5.00
  result_strikeouts: 2
  outcome: LOSS
```

---

## Final Pitching Line

| IP | H | R | ER | BB | K | HR | ERA | Pitches-Strikes | BF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.0 | 1 | 4 | 3 | 5 | 2 | 0 | 6.75 | 85-40 | 19 |

---

## Core Performance Metrics

| Metric | Result |
|---|---:|
| Total Pitches | 85 |
| Strikes | 40 |
| Strike Rate | 47% |
| Batters Faced | 19 |
| Swings | 29 |
| Called Strikes | 11 |
| Whiffs | 5 |
| CStr+Whiff | 16 / 85 |
| CSW | 19% |
| Whiff / Swing | 17% |
| Zone Rate | 36% |
| Chase Rate | 17% |
| First-Pitch Strike | 47% |
| Average EV Allowed | 84.9 mph |
| Hard-Hit BBE | 2 |
| Top EV Marker | 99.6 mph |
| Velo Marker | 97.3 mph |

---

## Pitch Mix

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CStr+Whiff |
|---|---:|---:|---:|---:|---:|---:|---:|
| Sinker | 42% / 36 | 94.7 | 0 | 13 | 6 | 0 | 17% |
| Slider | 24% / 20 | 88.5 | 0 | 9 | 2 | 2 | 20% |
| 4-Seam Fastball | 18% / 15 | 94.5 | 0 | 4 | 1 | 0 | 7% |
| Curveball | 16% / 14 | 86.4 | 2 | 3 | 2 | 3 | 36% |
| All | 100% / 85 | 91.8 | 2 | 29 | 11 | 5 | 19% |

---

## What Happened

Bradish finished with only 2 strikeouts over 4.0 innings, making this a full projection miss rather than a threshold miss. The position was placed on the plus-money 7+ lane at +118 after the market offered a fair to slight positive number. The actual outing never developed the required strikeout runway.

The strongest positive signal was contact suppression: Bradish allowed only 1 hit, 2 hard-hit batted balls, and an 84.9 mph average EV. The problem was everything tied to strikeout generation. He threw only 47% strikes, walked 5 hitters, posted a 36% zone rate, generated only a 17% chase rate, and finished with a 19% CSW. The Nationals did not damage him through hits, but they forced inefficient counts and let the walks collapse his leash.

This is the second recent full miss after Sasaki with the same broad failure shape: command volatility plus low chase suppressed the K path and shortened the outing.

---

## Model Diagnosis

### Confirmed

1. **Contact suppression was real.** Bradish allowed only 1 hit and an 84.9 mph average EV.
2. **Home run damage was avoided.** Zero HR allowed.
3. **Curveball was the only true bat-missing pitch.** It produced all 2 strikeouts and 36% CStr+Whiff.

### Missed / Weakened

1. **Command risk was badly underestimated.** Five walks and a 47% strike rate destroyed runway.
2. **CSW floor failed.** Actual CSW was 19%, well below the 6+/7+ pregame requirement.
3. **Whiff/swing floor failed.** 17% whiff/swing did not support a 7+ target.
4. **Washington LRS was too low.** The Nationals showed chase resistance and OBP pressure without needing hard contact.
5. **Sinker-heavy profile created weak K conversion.** The sinker was 42% of the mix and produced zero whiffs on 13 swings.
6. **Target selection was too aggressive.** 7+ required strong whiff conversion and leash; neither showed up.

---

## Washington LRS Update

```yaml
lineup_resistance_update:
  opponent: Washington Nationals
  archetype: chase_resistant_contact_patient_lineup
  current_signal:
    - Kyle Bradish 2026-06-28: 4.0 IP, 2 K, 5 BB, 19% CSW, 17% chase, 47% strikes
  adjustment:
    nationals_lrs_vs_sinker_slider_rhp: increase_by_0.5_to_0.8
    nationals_chase_suppression_modifier: increase
    nationals_walk_pressure_modifier: increase
    nationals_contact_damage_modifier: neutral
  reason: >
    Washington did not need loud contact to beat the K prop. They suppressed chase,
    forced walks, and collapsed Bradish's inning runway.
```

---

## Patch Recommendation

```yaml
patch_recommendation:
  name: walk_pressure_lrs_gate
  action: add
  description: >
    Add a lineup-resistance subcomponent that penalizes patient opponents even when their
    raw strikeout rate appears attackable. If the expected nine can create walks and resist chase,
    downgrade 6+ and 7+ K markets, especially for pitchers with recent command volatility.
  triggers:
    downgrade_if:
      - opponent_chase_profile == low_or_declining
      - opponent_obp_depth == moderate_to_high
      - pitcher_zone_rate_projection == unstable
      - target >= 6
    hard_avoid_if:
      - pitcher_recent_walk_risk == elevated
      - target >= 7
      - market_edge <= slight_positive
```

```yaml
patch_recommendation_2:
  name: sinker_heavy_k_conversion_penalty
  action: add
  description: >
    Sinker-heavy profiles need stronger secondary pitch whiff evidence before approving 6+ or 7+ K ladders.
    Weak-contact groundball suppression is not the same as strikeout conversion.
  trigger:
    downgrade_if:
      - primary_pitch == sinker
      - sinker_usage >= 35_percent
      - secondary_whiff_support_not_elite
      - market_target >= 6
```

```yaml
patch_recommendation_3:
  name: seven_plus_requires_dual_floor
  action: strengthen
  description: >
    For 7+ pregame positions, require both a CSW floor and whiff/swing floor, not just a fair price.
    A fair market edge is not sufficient when mean and median sit below or at the threshold.
  thresholds:
    seven_plus_csw_floor: 28_percent_or_higher
    seven_plus_whiff_swing_floor: 25_percent_or_higher
    avoid_if_projected_median_below_target: true
```

---

## Threshold Lesson

This was not a one-K loss. The 7+ ticket missed by five strikeouts, and even the softer 6+ would have lost. The model overrated the ceiling because it treated Washington as a cleaner K opponent and did not penalize the combination of Bradish command volatility plus sinker-heavy conversion risk.

```yaml
threshold_lesson:
  result_type: full_miss
  failed_target: 7_plus
  classification: command_chase_runway_failure
  command_read: failed
  runway_read: failed
  csw_read: failed
  whiff_read: failed
  contact_suppression_read: confirmed_but_not_k_relevant
  market_selection: too_aggressive_for_projection_floor
  future_rule: >
    Do not approve 7+ positions when the model mean is below 7 and the edge is only fair/slight
    unless CSW, whiff/swing, command, and opponent chase weakness all confirm pregame.
```

---

## Final Classification

```yaml
postmortem_classification:
  signal: weakened
  failure_type: command_chase_runway_failure
  command_read: failed
  leash_read: failed
  contact_suppression_read: confirmed_but_non_decisive
  csw_read: failed
  whiff_read: failed
  opponent_lrs: underestimated
  market_selection: too_aggressive_threshold
  ladder_exposure: none
  result: loss
  record: 0-1
  pnl: -5.00
  confidence_after_review: low
  final_status: modify_threshold_and_lrs
```

---

## Tags

`LOSS` `KYLE_BRADISH` `WILLIAM_HILL` `7_PLUS_KS` `FULL_MISS` `COMMAND_VOLATILITY` `CHASE_RESISTANCE` `RUNWAY_COLLAPSE` `NATIONALS_LRS_UPGRADE` `SINKER_HEAVY_PENALTY` `SEVEN_PLUS_DUAL_FLOOR` `MODEL_MODIFY`
