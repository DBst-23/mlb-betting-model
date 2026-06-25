# SharpEdge MLB K Prop Postmortem — 2026-06-24

## Position Summary

**Date:** 2026-06-24  
**Book:** William Hill  
**Game:** Seattle Mariners at Pittsburgh Pirates  
**Pitcher:** Bryan Woo  
**Markets:** Total Pitching Strikeouts  

| Leg | Target | Entry Odds | Stake | To Win | Paid | Profit/Loss | Final Ks | Outcome |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Primary | Over 5.5 Ks / 6+ | -102 | $10.00 | $9.80 | $0.00 | -$10.00 | 4 | LOSS |
| Ladder | 7+ Ks | +187 | $5.00 | $9.35 | $0.00 | -$5.00 | 4 | LOSS |

**Total Risk:** $15.00  
**Total Paid:** $0.00  
**Net Profit/Loss:** -$15.00  
**Final Strikeouts:** 4  
**Portfolio Outcome:** 0-2

---

## Pregame Model Snapshot

| Market | Model Probability | Market Implied | Estimated Edge | Grade |
|---|---:|---:|---:|---|
| 6+ / O5.5 | 55-58% | 50.5% | +4.5 to +7.5 pts | B+ / A- |
| 7+ | 38-42% | 34.8% | +3.2 to +7.2 pts | B micro-ladder |

```yaml
position:
  date: 2026-06-24
  sport: MLB
  market_type: pitcher_strikeouts
  pitcher: Bryan Woo
  team: Seattle Mariners
  opponent: Pittsburgh Pirates
  book: William Hill
  entries:
    - target: over_5_5_strikeouts
      equivalent_ladder: 6_plus_strikeouts
      odds: -102
      stake: 10.00
      paid: 0.00
      profit: -10.00
      outcome: LOSS
    - target: 7_plus_strikeouts
      odds: 187
      stake: 5.00
      paid: 0.00
      profit: -5.00
      outcome: LOSS
  result_strikeouts: 4
  total_pnl: -15.00
```

---

## Final Pitching Line

| IP | H | R | ER | BB | K | HR | ERA | Pitches-Strikes | BF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.0 | 6 | 5 | 5 | 2 | 4 | 0 | 11.25 | 86-57 | 20 |

---

## Core Performance Metrics

| Metric | Result |
|---|---:|
| Total Pitches | 86 |
| Strikes | 57 |
| Strike Rate | 66% |
| Batters Faced | 20 |
| Swings | 46 |
| Called Strikes | 11 |
| Whiffs | 13 |
| CStr+Whiff | 24 / 86 |
| CSW | 28% |
| Whiff / Swing | 28% |
| Zone Rate | 55% |
| Chase Rate | 31% |
| First-Pitch Strike | 60% |
| Average EV Allowed | 93.3 mph |
| Hard-Hit BBE | 8 |
| Top EV Marker | 106.8 |
| Velo Marker | 98.0 |

---

## Pitch Mix

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CStr+Whiff |
|---|---:|---:|---:|---:|---:|---:|---:|
| 4-Seam Fastball | 64% / 55 | 96.6 | 2 | 31 | 8 | 10 | 33% |
| Slider | 16% / 14 | 87.2 | 1 | 8 | 0 | 2 | 14% |
| Sinker | 12% / 10 | 95.9 | 1 | 4 | 3 | 0 | 30% |
| Sweeper | 6% / 5 | 84.4 | 0 | 1 | 0 | 0 | 0% |
| Changeup | 2% / 2 | 88.3 | 0 | 2 | 0 | 1 | 50% |
| All | 100% / 86 | 94.1 | 4 | 46 | 11 | 13 | 28% |

---

## What Happened

Woo produced enough bat-missing indicators to keep the pregame K thesis partially alive: 28% CSW and 28% whiff/swing are not poor. The bet lost because the runway collapsed. He lasted only 4.0 innings, faced 20 batters, allowed 6 hits, 5 earned runs, 2 walks, and 8 hard-hit balls.

The primary 6+ ticket needed at least one more clean inning, while the 7+ ladder needed both clean efficiency and strikeout density. Neither condition held. Woo had K stuff, but the contact damage and run prevention failure shortened the outing.

---

## Model Diagnosis

### Confirmed

1. **Whiff ability was present.** Woo produced 13 whiffs on 46 swings.
2. **Fastball velocity was healthy.** 4-seam averaged 96.6 mph with a 98.0 velo marker.
3. **Fastball K path existed.** 4-seam produced 2 Ks and 33% CStr+Whiff.

### Missed / Weakened

1. **Runway projection failed.** Woo reached only 4.0 innings and 20 batters faced.
2. **Contact suppression was overestimated.** 93.3 mph average EV and 8 hard-hit BBE created heavy damage.
3. **Opponent LRS was underestimated again.** Pittsburgh showed stronger contact resistance and damage capacity than expected against a command-first Seattle righty.
4. **Pitch mix concentration risk was too high.** Woo threw 64% four-seam fastballs. The K path existed but became too dependent on one pitch family.
5. **7+ ladder was too aggressive for the post-Kirby patch.** The added ladder exposure should have been even smaller or skipped given the same opponent and similar command/righty profile.

---

## Pittsburgh LRS Update

This is the second straight Seattle command/righty K miss against Pittsburgh after George Kirby on 2026-06-23. The opponent adjustment should not treat Pittsburgh as a soft K matchup for this archetype.

```yaml
lineup_resistance_update:
  opponent: Pittsburgh Pirates
  archetype: command_first_right_handed_pitchers
  previous_signal:
    - George Kirby 2026-06-23: 6.0 IP, 5 K, O5.5 loss
  current_signal:
    - Bryan Woo 2026-06-24: 4.0 IP, 4 K, O5.5 and 7+ losses
  adjustment:
    pirates_lrs_vs_command_rhp: increase_by_0.5_to_0.8
    pirates_contact_damage_modifier: increase
    pirates_foul_ball_contact_resistance: increase
  status: immediate_patch_required
```

---

## Patch Recommendation

```yaml
patch_recommendation:
  name: same_opponent_archetype_penalty
  action: add
  description: >
    If the model misses a pitcher K over against an opponent because of contact
    resistance or whiff conversion, apply a temporary resistance penalty to the same
    opponent against similar pitcher archetypes for the next 3-5 games. Require a
    deeper discount or avoid ladder exposure until the opponent confirms softness again.
  applies_to:
    - Pittsburgh vs Seattle command/righty profiles
    - command-first arms with concentrated fastball usage
    - pitchers whose K path depends on one dominant pitch family
```

```yaml
patch_recommendation_2:
  name: contact_damage_runway_gate
  action: add
  description: >
    Before approving a 6+ or 7+ K position, require contact suppression support.
    If opponent has recent hard-hit/contact resistance signal, reduce projected innings
    runway even when the pitcher's baseline leash is stable.
  thresholds:
    avoid_ladder_if:
      - opponent_recent_contact_damage_signal == high
      - pitcher_primary_pitch_usage_above_60_percent
      - projected_mean_between_5_8_and_6_2
```

---

## Threshold Lesson

This was not simply a one-K threshold miss like Kirby. Woo missed both the 6+ primary and 7+ ladder because the outing never stabilized.

- 5+ would also have lost.
- 6+ lost by 2 Ks.
- 7+ lost by 3 Ks.
- The miss was a **runway + contact suppression failure**, not a pure whiff failure.

```yaml
threshold_lesson:
  result_type: full_miss
  failed_targets:
    - over_5_5
    - 7_plus
  classification: runway_contact_damage_miss
  future_rule: >
    Do not stack primary plus ladder exposure on command-first righties against an
    opponent that already produced a same-archetype K-under signal within the prior
    24-48 hours.
```

---

## Final Classification

```yaml
postmortem_classification:
  signal: weakened
  failure_type: runway_contact_damage_failure
  leash_read: missed
  whiff_read: partially_confirmed
  opponent_lrs: underestimated
  market_selection: too_aggressive_with_ladder
  result: loss
  record: 0-2
  pnl: -15.00
  confidence_after_review: low_to_medium
  final_status: modify
```

---

## Tags

`LOSS` `BRYAN_WOO` `WILLIAM_HILL` `OVER_5_5_KS` `7_PLUS_KS` `PITTSBURGH_LRS_UPGRADE` `RUNWAY_MISS` `CONTACT_DAMAGE_FAILURE` `COMMAND_RHP_ARCHETYPE` `SAME_OPPONENT_ARCHETYPE_PENALTY` `MODEL_MODIFY`
