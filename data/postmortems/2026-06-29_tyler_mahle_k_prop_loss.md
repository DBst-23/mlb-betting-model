# SharpEdge MLB K Prop Postmortem — 2026-06-29

## Position Summary

**Date:** 2026-06-29  
**Book:** William Hill  
**Game:** San Francisco Giants at Arizona Diamondbacks  
**Pitcher:** Tyler Mahle  
**Market:** Pitching Strikeouts Live  

| Target | Entry Odds | Stake | To Win | Paid | Profit/Loss | Final Ks | Outcome |
|---|---:|---:|---:|---:|---:|---:|---|
| 5+ Strikeouts | +126 | $10.00 | $12.60 | $0.00 | -$10.00 | 3 | LOSS |

```yaml
position:
  date: 2026-06-29
  sport: MLB
  market_type: pitcher_strikeouts_live
  pitcher: Tyler Mahle
  team: San Francisco Giants
  opponent: Arizona Diamondbacks
  book: William Hill
  target: 5_plus_strikeouts
  odds: 126
  stake: 10.00
  to_win: 12.60
  paid: 0.00
  profit: -10.00
  result_strikeouts: 3
  outcome: LOSS
```

---

## Pregame / Live Market Snapshot

Mahle was classified as a small plus-money value position, not a core projection smash.

| Metric | Projection |
|---|---:|
| Refined Mean | 4.7 Ks |
| Median | 5 Ks |
| 5+ Hit Probability | 45-49% |
| Market Implied Probability | 44.2% |
| Estimated Edge | Slight positive |
| Lineup Resistance Score | 5.6 |
| Grade | B / small playable |

---

## Final Pitching Line

| IP | H | R | ER | BB | K | HR | ERA | Pitches-Strikes | BF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.1 | 4 | 4 | 4 | 3 | 3 | 1 | 8.31 | 85-51 | 19 |

---

## Core Performance Metrics

| Metric | Result |
|---|---:|
| Total Pitches | 85 |
| Strikes | 51 |
| Strike Rate | 60% |
| Batters Faced | 19 |
| Swings | 37 |
| Called Strikes | 13 |
| Whiffs | 10 |
| CStr+Whiff | 23 / 85 |
| CSW | 27% |
| Whiff / Swing | 27% |
| Zone Rate | 42% |
| Chase Rate | 27% |
| First-Pitch Strike | 58% |
| BBE | 13 |
| Hits Allowed | 4 |
| Hard-Hit BBE | 2 |
| Average EV Allowed | 87.7 mph |
| Top EV Marker | 103.9 mph |
| Velo Marker | 95.5 mph |

---

## Pitch Mix

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CStr+Whiff |
|---|---:|---:|---:|---:|---:|---:|---:|
| 4-Seam Fastball | 45% / 38 | 93.5 | 0 | 15 | 9 | 1 | 26% |
| Splitter | 33% / 28 | 87.7 | 2 | 15 | 0 | 6 | 21% |
| Slider | 13% / 11 | 84.6 | 0 | 4 | 1 | 2 | 27% |
| Cutter | 9% / 8 | 87.4 | 1 | 3 | 3 | 1 | 50% |
| All | 100% / 85 | 89.9 | 3 | 37 | 13 | 10 | 27% |

---

## What Happened

Mahle showed playable bat-missing indicators: 27% CSW, 27% whiff/swing, and 10 whiffs on 37 swings. The problem was runway and conversion. He lasted only 4.1 innings, allowed 4 earned runs, walked 3 hitters, and finished with 3 strikeouts.

This differs from the Lodolo loss. Lodolo had strong run prevention but weak whiff conversion. Mahle had acceptable whiff indicators but did not get enough innings runway for the 5+ target to mature.

---

## Model Diagnosis

### Confirmed

1. Whiff indicators were playable: 27% CSW and 27% whiff/swing.
2. Splitter was the best K pitch, producing 6 whiffs and 2 strikeouts.
3. Cutter was efficient in small usage with 1 strikeout and 50% CStr+Whiff.
4. The +126 price was not bad in isolation.

### Missed / Weakened

1. Runway was overestimated; Mahle lasted only 4.1 innings.
2. Run-prevention risk was underestimated: 4 ER and 1 HR.
3. Arizona's LRS was too lenient for a live 5+ position.
4. Fastball-heavy usage did not create K conversion: 45% four-seam, 0 strikeouts.
5. Three walks increased pitch-count stress.
6. The position was too large for a slight-positive B-grade profile.

---

## Arizona LRS Update

```yaml
lineup_resistance_update:
  opponent: Arizona Diamondbacks
  archetype: low_k_obp_resistance_vs_rhp
  current_signal:
    - Tyler Mahle 2026-06-29: 4.1 IP, 3 K, 3 BB, 4 ER, 27% CSW, 27% whiff_swing
  adjustment:
    diamondbacks_lrs_vs_rhp: increase_by_0.3_to_0.5
    diamondbacks_low_k_obp_modifier: increase
    diamondbacks_runway_pressure_modifier: increase
    diamondbacks_contact_damage_modifier: slight_increase
  reason: >
    Arizona did not fully suppress whiffs, but the lineup created enough baserunners,
    contact pressure, and run damage to shorten the starter's runway before a 5+ K target
    could mature.
```

---

## Patch Recommendations

```yaml
patches_added:
  - b_grade_plus_money_stake_cap
  - fastball_heavy_k_conversion_check
  - live_market_runway_confirmation_gate

b_grade_plus_money_stake_cap:
  action: add
  rule: >
    B-grade plus-money K props are capped at micro/small stake unless the edge is clear
    and runway, CSW, whiff, and LRS gates all independently pass.

fastball_heavy_k_conversion_check:
  action: add
  rule: >
    If four-seam usage is 40%+ and four-seam K conversion is weak, downgrade 5+ and 6+
    unless secondary pitch volume is strong enough to carry the prop.

live_market_runway_confirmation_gate:
  action: strengthen
  rule: >
    Live K positions need explicit innings runway confirmation. Good whiff rate alone is not enough.
```

---

## Threshold Lesson

This was a full miss relative to target. Mahle needed 5 Ks and finished with 3. The whiff metrics were acceptable, but the innings runway failed.

```yaml
threshold_lesson:
  result_type: full_miss
  failed_target: 5_plus
  classification: runway_contact_damage_failure
  command_read: mixed
  leash_read: failed
  contact_suppression_read: partially_failed
  csw_read: passed
  whiff_read: passed
  opponent_lrs: underestimated
  market_selection: slight_edge_overstaked
  future_rule: >
    Do not assign standard stake to slight-positive plus-money pitcher K props when LRS is 5.3+
    and projected mean is below the target. Require stronger edge or live runway confirmation.
```

---

## Final Classification

```yaml
postmortem_classification:
  signal: weakened
  failure_type: full_projection_miss
  sub_type: runway_contact_damage_failure
  command_read: mixed
  leash_read: failed
  contact_suppression_read: partially_failed
  csw_read: passed
  whiff_read: passed
  opponent_lrs: underestimated
  market_selection: slight_edge_overstaked
  ladder_exposure: none
  result: loss
  record: 0-1
  pnl: -10.00
  confidence_after_review: reduced
  final_status: reduce_pregame_and_live_k_volume
```

---

## Model State After Loss

```yaml
risk_review:
  recent_pattern: >
    The pitcher K portfolio is in a negative cluster. Recent losses have come through
    command volatility, low chase, walk pressure, whiff conversion failure, contact damage,
    and runway collapse.
  immediate_operational_change: >
    Reduce pitcher K volume. No standard $10 exposure on B-grade K props. Only A-grade or better
    with clear CSW, whiff/swing, leash, LRS, and price confirmation can receive standard stake.
```

---

## Tags

`LOSS` `TYLER_MAHLE` `WILLIAM_HILL` `5_PLUS_KS` `FULL_MISS` `RUNWAY_FAILURE` `CONTACT_DAMAGE` `B_GRADE_OVERSTAKED` `FASTBALL_HEAVY_CHECK` `LIVE_MARKET_RUNWAY_GATE` `DIAMONDBACKS_LRS_UPGRADE` `MODEL_MODIFY`
