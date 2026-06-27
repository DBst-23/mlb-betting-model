# SharpEdge MLB K Prop Postmortem — 2026-06-26

## Position Summary

**Date:** 2026-06-26  
**Book:** William Hill  
**Game:** Los Angeles Dodgers at San Diego Padres  
**Pitcher:** Roki Sasaki  
**Market:** Pitching Strikeouts  

| Target | Entry Odds | Stake | To Win | Paid | Profit/Loss | Final Ks | Outcome |
|---|---:|---:|---:|---:|---:|---:|---|
| 6+ Strikeouts | +104 | $5.43 | $5.65 | $0.00 | -$5.43 | 2 | LOSS |

**Total Risk:** $5.43  
**Total Paid:** $0.00  
**Net Profit/Loss:** -$5.43  
**Final Strikeouts:** 2  
**Portfolio Outcome:** 0-1

---

## Pregame Model Snapshot

| Metric | Projection |
|---|---:|
| Mean | 6.3 Ks |
| Median | 6 Ks |
| Hit Probability: 6+ | 60-64% |
| Market Implied Probability | 49.0% |
| Estimated Edge | +11 to +15 pts |
| Grade | A |

```yaml
position:
  date: 2026-06-26
  sport: MLB
  market_type: pitcher_strikeouts
  pitcher: Roki Sasaki
  team: Los Angeles Dodgers
  opponent: San Diego Padres
  book: William Hill
  target: 6_plus_strikeouts
  odds: 104
  stake: 5.43
  to_win: 5.65
  paid: 0.00
  profit: -5.43
  result_strikeouts: 2
  outcome: LOSS
```

---

## Final Pitching Line

| IP | H | R | ER | BB | K | HR | ERA | Pitches-Strikes | BF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.0 | 3 | 3 | 3 | 5 | 2 | 1 | 6.75 | 81-45 | 20 |

**Wild Pitch:** Roki Sasaki

---

## Core Performance Metrics

| Metric | Result |
|---|---:|
| Total Pitches | 81 |
| Strikes | 45 |
| Strike Rate | 56% |
| Batters Faced | 20 |
| Swings | 34 |
| Called Strikes | 11 |
| Whiffs | 7 |
| CStr+Whiff | 18 / 81 |
| CSW | 22% |
| Whiff / Swing | 21% |
| Zone Rate | 44% |
| Chase Rate | 20% |
| First-Pitch Strike | 65% |
| Average EV Allowed | 85.8 mph |
| Hard-Hit BBE | 6 |
| Top EV Marker | 111.1 |
| Velo Marker | 100.1 |

---

## Pitch Mix

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CStr+Whiff |
|---|---:|---:|---:|---:|---:|---:|---:|
| 4-Seam Fastball | 47% / 38 | 97.7 | 1 | 19 | 7 | 2 | 24% |
| Slider | 27% / 22 | 86.7 | 0 | 8 | 4 | 1 | 23% |
| Splitter | 26% / 21 | 90.3 | 1 | 7 | 0 | 4 | 19% |
| All | 100% / 81 | 92.8 | 2 | 34 | 11 | 7 | 22% |

---

## What Happened

Sasaki lost the 6+ position badly, finishing with only 2 strikeouts over 4.0 innings. The pregame edge came from price: +104 carried a 49.0% implied probability while the model projected 60-64%. The price was attractive, but the live result exposed a projection miss on command, chase, and runway.

The pitch quality was not dead: velocity was strong, with a 100.1 velo marker and a 97.7 mph four-seam average. The problem was conversion. Sasaki threw only 56% strikes, walked 5 hitters, generated only a 20% chase rate, and finished with a 22% CSW. The Padres did not chase enough, forced him into inefficient counts, and the walk cluster killed the inning runway.

This is not a one-K threshold loss. It is a full miss caused by control volatility and opponent discipline.

---

## Model Diagnosis

### Confirmed

1. **Velocity was live.** The stuff baseline was not broken; top velo reached 100.1.
2. **Pitch mix support existed in theory.** Sasaki used a real three-pitch mix: four-seam, slider, splitter.
3. **Contact suppression was partially acceptable.** Average EV allowed was 85.8 mph, and only 3 hits were allowed.

### Missed / Weakened

1. **Command risk was badly underestimated.** Five walks across 20 batters destroyed strikeout runway.
2. **Padres LRS was too low.** San Diego produced chase resistance and forced inefficient counts.
3. **CSW floor failed.** Actual 22% CSW landed in the model downgrade zone.
4. **Whiff conversion was weak.** Seven whiffs on 34 swings was not enough for a 6+ attack.
5. **Runway collapsed.** Sasaki lasted only 4.0 innings and faced 20 batters.
6. **Hard-hit risk remained present despite low hit total.** Six hard-hit BBE and a 111.1 EV marker created enough damage pressure to shorten leash.

---

## Padres LRS Update

```yaml
lineup_resistance_update:
  opponent: San Diego Padres
  archetype: high_velocity_rhp_with_command_volatility
  current_signal:
    - Roki Sasaki 2026-06-26: 4.0 IP, 2 K, 5 BB, 22% CSW, 20% chase
  adjustment:
    padres_lrs_vs_high_velo_rhp: increase_by_0.6_to_0.9
    padres_chase_suppression_modifier: increase
    padres_walk_pressure_modifier: increase
    padres_contact_damage_modifier: slight_increase
  reason: >
    Padres punished Sasaki's command volatility by refusing chase, creating walks,
    limiting strikeout conversion, and collapsing his inning runway.
```

---

## Patch Recommendation

```yaml
patch_recommendation:
  name: command_volatility_gate_for_plus_price_6plus
  action: add
  description: >
    Even when the price creates a large apparent edge, downgrade 6+ K projections for
    pitchers with command volatility when the opponent has above-average chase suppression
    or OBP depth. Price alone cannot override walk-pressure risk.
  thresholds:
    downgrade_if:
      - projected_walk_risk == elevated
      - opponent_chase_profile == disciplined
      - required_target >= 6
    avoid_if:
      - pitcher_walk_rate_recent_form == high
      - opponent_lrs >= 5.2
      - market_requires_6plus_or_higher
```

```yaml
patch_recommendation_2:
  name: csw_floor_gate_confirmed
  action: strengthen
  description: >
    The Peralta and Sasaki losses both confirm the need for a CSW floor gate.
    For a pregame 6+ strikeout position, require either strong recent CSW support or
    a clear opponent chase weakness. If the expected-nine LRS includes chase resistance,
    reduce 6+ probability by 4-8 percentage points.
  thresholds:
    preferred_csw_floor: 27_percent
    caution_zone: 23_to_26_percent
    downgrade_zone: below_23_percent
```

```yaml
patch_recommendation_3:
  name: big_edge_sanity_check
  action: add
  description: >
    When model edge exceeds +10 percentage points on a plus-money K prop, run a sanity
    check against leash, walk rate, and opponent chase profile before approving the bet.
    Large edges are often created by the model underpricing volatility or lineup resistance.
```

---

## Threshold Lesson

This was a full projection miss, not a bad beat. Sasaki missed 6+ by four strikeouts and never created a live path to the target.

- 5+ would have lost.
- 6+ lost by 4 Ks.
- 7+ would have been completely dead.
- The miss was command + chase resistance + runway collapse.

```yaml
threshold_lesson:
  result_type: full_miss
  failed_target: 6_plus
  classification: command_chase_runway_failure
  runway_read: failed
  contact_suppression_read: mixed
  csw_read: failed
  market_selection: price_looked_good_but_volatility_underpriced
  future_rule: >
    Do not let a plus-money number override command volatility when the opponent's
    chase suppression and OBP depth can force walks and shorten the outing.
```

---

## Final Classification

```yaml
postmortem_classification:
  signal: weakened
  failure_type: command_chase_runway_failure
  leash_read: failed
  command_read: failed
  contact_suppression_read: mixed
  csw_read: failed
  opponent_lrs: underestimated
  market_selection: overvalued_by_model_due_to_price
  ladder_exposure: none
  result: loss
  record: 0-1
  pnl: -5.43
  confidence_after_review: low
  final_status: modify
```

---

## Tags

`LOSS` `ROKI_SASAKI` `WILLIAM_HILL` `6_PLUS_KS` `COMMAND_VOLATILITY` `CHASE_RESISTANCE` `RUNWAY_COLLAPSE` `PADRES_LRS_UPGRADE` `CSW_FLOOR_GATE` `BIG_EDGE_SANITY_CHECK` `MODEL_MODIFY`
