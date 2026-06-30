# SharpEdge MLB K Prop Postmortem — 2026-06-29

## Position Summary

**Date:** 2026-06-29  
**Book:** William Hill  
**Game:** Cincinnati Reds at Milwaukee Brewers  
**Pitcher:** Nick Lodolo  
**Market:** Total Pitching Strikeouts  

| Target | Entry Odds | Stake | To Win | Paid | Profit/Loss | Final Ks | Outcome |
|---|---:|---:|---:|---:|---:|---:|---|
| Over 4.5 Strikeouts | -115 | $10.00 | $8.70 | $0.00 | -$10.00 | 4 | LOSS |

**Total Risk:** $10.00  
**Total Paid:** $0.00  
**Net Profit/Loss:** -$10.00  
**Final Strikeouts:** 4  
**Portfolio Outcome:** 0-1

---

## Pregame Model Snapshot

The position was originally identified after rejecting the 5+ ladder price at -135 and finding the same 5-strikeout cash condition at a better price through the Over 4.5 market at -115.

| Metric | Projection |
|---|---:|
| Refined Mean | 5.4 Ks |
| Median | 5 Ks |
| O4.5 / 5+ Hit Probability | 60-64% |
| Market Implied Probability | 53.5% |
| Estimated Edge | +6.5 to +10.5 pts |
| Lineup Resistance Score | 5.5 |
| Grade | B+ |

```yaml
position:
  date: 2026-06-29
  sport: MLB
  market_type: pitcher_strikeouts
  pitcher: Nick Lodolo
  team: Cincinnati Reds
  opponent: Milwaukee Brewers
  book: William Hill
  target: over_4_5_strikeouts
  odds: -115
  stake: 10.00
  to_win: 8.70
  paid: 0.00
  profit: -10.00
  result_strikeouts: 4
  outcome: LOSS
```

---

## Final Pitching Line

| IP | H | R | ER | BB | K | HR | ERA | Pitches-Strikes | BF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5.0 | 1 | 0 | 0 | 4 | 4 | 0 | 0.00 | 96-52 | 20 |

---

## Core Performance Metrics

| Metric | Result |
|---|---:|
| Total Pitches | 96 |
| Strikes | 52 |
| Strike Rate | 54% |
| Batters Faced | 20 |
| Swings | 34 |
| Called Strikes | 18 |
| Whiffs | 5 |
| CStr+Whiff | 23 / 96 |
| CSW | 24% |
| Whiff / Swing | 15% |
| Zone Rate | 46% |
| Chase Rate | 15% |
| First-Pitch Strike | 60% |
| BBE | 11 |
| Hits Allowed | 1 |
| Hard-Hit BBE | 3 |
| Average EV Allowed | 92.0 mph |
| Top EV Marker | 104.5 mph |
| Velo Marker | 96.0 mph |

---

## Pitch Mix

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CStr+Whiff |
|---|---:|---:|---:|---:|---:|---:|---:|
| Sinker | 40% / 38 | 93.9 | 0 | 15 | 9 | 0 | 24% |
| Changeup | 27% / 26 | 87.9 | 1 | 13 | 4 | 1 | 19% |
| Curveball | 20% / 19 | 81.5 | 1 | 3 | 4 | 2 | 32% |
| 4-Seam Fastball | 14% / 13 | 94.6 | 2 | 3 | 1 | 2 | 23% |
| All | 100% / 96 | 89.9 | 4 | 34 | 18 | 5 | 24% |

---

## What Happened

Lodolo threw five scoreless innings and allowed only one hit, but the strikeout ticket still lost by one strikeout. This was a classic one-K threshold miss: strong run prevention, enough leash to reach five innings, but not enough whiff conversion to clear the Over 4.5 strikeout market.

The Brewers confirmed the primary pregame concern. They resisted chase, forced long counts, produced four walks, and pushed Lodolo to 96 pitches through only five innings. Lodolo's CSW landed at 24%, below the preferred 27%+ threshold for pregame strikeout overs, while whiff/swing was only 15%. The pitch mix also leaned heavily on the sinker, which produced zero whiffs on 15 swings and zero strikeouts.

The ticket was correctly priced better than the 5+ ladder market, but the projection still underestimated Milwaukee's ability to suppress whiff conversion and create pitch-count drag.

---

## Model Diagnosis

### Confirmed

1. **Run prevention was strong.** Lodolo allowed 0 runs and only 1 hit over 5.0 innings.
2. **Leash was sufficient for a soft threshold.** He reached 96 pitches and completed 5 innings.
3. **Contact suppression was acceptable in run terms.** Milwaukee did not beat him through scoring or volume of hits.
4. **Over 4.5 was better than 5+ at -135.** The price shopping was correct.

### Missed / Weakened

1. **Whiff conversion was over-projected.** Only 5 whiffs on 34 swings, 15% whiff/swing.
2. **CSW floor failed.** Actual CSW was 24%, below the target floor for confidence.
3. **Brewers chase resistance was underestimated.** Chase rate finished at only 15%.
4. **Walk pressure was underestimated.** Four walks created pitch-count drag and reduced strikeout opportunities.
5. **Sinker-heavy usage was a K suppressor.** The sinker was 40% of the pitch mix, generated zero whiffs, and produced zero strikeouts.
6. **The refined LRS was still too low.** Milwaukee's LRS should have been closer to a true red-zone profile for Lodolo's arsenal shape.

---

## Milwaukee LRS Update

```yaml
lineup_resistance_update:
  opponent: Milwaukee Brewers
  archetype: low_chase_obp_pressure_vs_lhp
  current_signal:
    - Nick Lodolo 2026-06-29: 5.0 IP, 4 K, 4 BB, 24% CSW, 15% whiff_swing, 15% chase
  adjustment:
    brewers_lrs_vs_lhp: increase_by_0.4_to_0.7
    brewers_chase_suppression_modifier: increase
    brewers_walk_pressure_modifier: increase
    brewers_contact_damage_modifier: neutral_to_slight_positive
  reason: >
    Milwaukee did not need to score to beat the K over. They extended counts,
    refused chase, drew walks, and reduced Lodolo's strikeout conversion enough
    to keep him at 4 Ks despite five scoreless innings.
```

---

## Patch Recommendation

```yaml
patch_recommendation:
  name: soft_threshold_requires_whiff_floor
  action: add
  description: >
    Even for soft 4.5/5+ strikeout markets, require a minimum whiff/swing floor
    when opponent LRS is 5.3 or higher. Price improvement alone should not
    override weak whiff conversion risk.
  triggers:
    downgrade_if:
      - target_cash_condition >= 5
      - opponent_lrs >= 5.3
      - projected_whiff_swing < 23_percent
      - pitcher_primary_pitch_is_contact_or_sinker_heavy
```

```yaml
patch_recommendation_2:
  name: low_chase_walk_pressure_combo_gate
  action: strengthen
  description: >
    Treat low chase plus elevated opponent walk depth as a direct strikeout-prop downgrade,
    even when the pitcher's run prevention and leash are stable.
  hard_warning_if:
    - opponent_chase_profile == low
    - opponent_obp_depth == moderate_to_high
    - pitcher_projected_zone_rate < 50_percent
    - target_cash_condition >= 5
```

```yaml
patch_recommendation_3:
  name: sinker_heavy_lefty_k_penalty
  action: add
  description: >
    LHPs using sinker-heavy structures should receive a K-conversion penalty
    unless breaking ball/changeup whiff support is clearly above threshold.
  trigger:
    downgrade_if:
      - pitcher_handedness == LHP
      - sinker_usage >= 35_percent
      - sinker_whiffs == low_or_zero_projection
      - opponent_has_low_chase_profile
```

---

## Threshold Lesson

This was a disciplined price-shop but still a losing threshold selection. The model correctly rejected 5+ at -135 and chose Over 4.5 at -115. The mistake was allowing price correction to elevate a profile where Milwaukee's LRS already carried warning signs.

```yaml
threshold_lesson:
  result_type: one_k_miss
  failed_target: over_4_5
  classification: chase_suppression_whiff_conversion_failure
  command_read: unstable
  leash_read: confirmed
  contact_suppression_read: confirmed_in_run_prevention_but_not_k_conversion
  csw_read: failed
  whiff_read: failed
  opponent_lrs: underestimated
  market_selection: price_shopped_correctly_but_profile_overrated
  future_rule: >
    When a lineup has low chase plus OBP depth, do not upgrade a 5-K cash condition
    solely because price improves from -135 to -115. Require projected CSW and
    whiff/swing floors to clear before making the bet standard size.
```

---

## Pitch-Level Lessons

```yaml
pitch_level_lessons:
  sinker:
    usage: 40_percent
    strikeouts: 0
    whiffs: 0
    lesson: >
      Sinker volume created weak contact/run prevention but did not support K conversion.
  changeup:
    usage: 27_percent
    strikeouts: 1
    whiffs: 1
    lesson: >
      Changeup was not a strong enough bat-missing weapon to offset sinker-heavy structure.
  curveball:
    usage: 20_percent
    strikeouts: 1
    cstr_whiff: 32_percent
    lesson: >
      Curveball was useful but too low-volume to carry the prop.
  four_seam:
    usage: 14_percent
    strikeouts: 2
    lesson: >
      Fastball produced two strikeouts but was not used enough to build the K path.
```

---

## Final Classification

```yaml
postmortem_classification:
  signal: weakened
  failure_type: one_k_threshold_miss
  sub_type: chase_suppression_whiff_conversion_failure
  command_read: unstable
  leash_read: confirmed
  contact_suppression_read: confirmed_but_non_decisive
  csw_read: failed
  whiff_read: failed
  opponent_lrs: underestimated
  market_selection: improved_price_but_overrated_profile
  ladder_exposure: none
  result: loss
  record: 0-1
  pnl: -10.00
  confidence_after_review: reduced
  final_status: modify_soft_threshold_rules
```

---

## Model State After Loss

```yaml
active_new_patches:
  - soft_threshold_requires_whiff_floor
  - low_chase_walk_pressure_combo_gate
  - sinker_heavy_lefty_k_penalty

risk_review:
  recent_pattern: >
    Multiple pitcher K investments have failed through similar paths: command volatility,
    low chase, whiff conversion failure, and opponent OBP depth. The model should reduce
    pregame K volume and require stronger dual-floor confirmation before committing stake.
  immediate_operational_change: >
    No standard-size K props when opponent LRS is 5.3+ unless CSW projection, whiff/swing
    projection, leash, and price all independently clear. Otherwise classify as LiveFlow only
    or micro stake.
```

---

## Tags

`LOSS` `NICK_LODOLO` `WILLIAM_HILL` `OVER_4_5_KS` `ONE_K_MISS` `BREWERS_LRS_UPGRADE` `LOW_CHASE` `WALK_PRESSURE` `WHIFF_CONVERSION_FAILURE` `SINKER_HEAVY_PENALTY` `SOFT_THRESHOLD_PATCH` `MODEL_MODIFY`
