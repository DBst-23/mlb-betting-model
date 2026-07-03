# SharpEdge MLB K Model Sharpening Note — 2026-07-02

## Context

**Date:** 2026-07-02  
**Game:** Tampa Bay Rays at Kansas City Royals  
**Pitcher:** Ian Seymour  
**Opponent:** Kansas City Royals  
**Market Reviewed:** 5+ Pitching Strikeouts at +110  
**Official Investment:** No  
**Purpose:** Model sharpening / opponent LRS calibration  

This was not an official SharpEdge betting position. Seymour was reviewed as a candidate after the 07-02 William Hill board showed 5+ strikeouts at +110. The pregame model ultimately passed because Kansas City projected as a low-K contact opponent, especially after the Shane McClanahan loss on 07-01.

```yaml
model_review:
  date: 2026-07-02
  sport: MLB
  market_type: pitcher_strikeouts
  pitcher: Ian Seymour
  team: Tampa Bay Rays
  opponent: Kansas City Royals
  reviewed_market: 5_plus_strikeouts
  reviewed_odds: 110
  official_investment: false
  pregame_decision: PASS
  result_strikeouts: 8
  result_note: "Model pass would have missed a winning K outcome, but preserved process discipline."
```

---

## Pregame Model Read

### KC vs LHP Recent Form Input

| Metric | Value |
|---|---:|
| Date Range | 2026-06-01 to 2026-07-02 |
| Total PA | 409 |
| Total SO | 81 |
| Lineup K Rate | 19.8% |
| Total BB | 28 |
| Lineup BB Rate | 6.8% |
| Pre-Sharpen LRS | 5.9 |

### Pregame Seymour Projection

| Metric | Projection |
|---|---:|
| Mean | 4.2 Ks |
| Median | 4 Ks |
| 4+ Probability | 62-66% |
| 5+ Probability | 39-43% |
| 6+ Probability | 21-25% |
| LRS | 5.9 |
| Grade | C |
| Decision | PASS_PREGAME |

The pass was driven by Kansas City's low-K contact profile, not by a belief that Seymour lacked any strikeout ability.

---

## Final Pitching Line

| IP | H | R | ER | BB | K | HR | ERA | Pitches-Strikes | BF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6.0 | 3 | 1 | 1 | 1 | 8 | 1 | 1.50 | 83-55 | 23 |

---

## Core Performance Metrics

| Metric | Result |
|---|---:|
| Total Pitches | 83 |
| Strikes | 55 |
| Strike Rate | 66% |
| Batters Faced | 23 |
| Swings | 42 |
| Called Strikes | 13 |
| Whiffs | 15 |
| CStr+Whiff | 28 / 83 |
| CSW | 34% |
| Whiff / Swing | 36% |
| Zone Rate | 52% |
| Chase Rate | 33% |
| First-Pitch Strike | 65% |
| BBE | 14 |
| Hits Allowed | 3 |
| Hard-Hit BBE | 5 |
| Average EV Allowed | 92.8 mph |
| Top EV Marker | 106.7 mph |
| Velo Marker | 94.0 mph |

---

## Pitch Mix

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CStr+Whiff |
|---|---:|---:|---:|---:|---:|---:|---:|
| Sweeper | 31% / 26 | 81.1 | 2 | 18 | 2 | 7 | 35% |
| 4-Seam Fastball | 30% / 25 | 91.6 | 3 | 14 | 6 | 4 | 40% |
| Changeup | 20% / 17 | 83.9 | 3 | 7 | 1 | 3 | 24% |
| Sinker | 13% / 11 | 90.6 | 0 | 3 | 4 | 1 | 45% |
| Curveball | 4% / 3 | 72.8 | 0 | 0 | 0 | 0 | 0% |
| Slider | 1% / 1 | 82.7 | 0 | 0 | 0 | 0 | 0% |
| All | 100% / 83 | 85.8 | 8 | 42 | 13 | 15 | 34% |

---

## What Happened

Seymour cleared the reviewed 5+ threshold easily, finishing with 8 strikeouts over 6.0 innings. The main miss was that the model over-penalized Kansas City's team-level low-K profile and underweighted Seymour's active arsenal shape.

The Royals still created some of the danger we expected: 5 hard-hit balls, a 106.7 top EV marker, and a 92.8 mph average EV allowed. But Seymour's swing-and-miss profile was strong enough to overcome the contact risk. His 34% CSW and 36% whiff/swing were well above the thresholds we now require for K investment clearance.

This was a useful non-bet model note because it showed that the Kansas City LRS red-zone rule should not be applied blindly. The rule worked for McClanahan because his whiff/swing was only 21%. It did not apply to Seymour once his in-game whiff/swing reached 36%.

---

## Model Diagnosis

### Confirmed

1. **Kansas City still showed contact damage risk.** Seymour allowed 5 hard-hit BBE and a 106.7 EV marker.
2. **The pregame caution was reasonable after McClanahan.** KC had just suppressed a strong left-handed starter's K prop despite excellent run prevention.
3. **LiveFlow would have caught the opportunity.** Seymour's early whiff indicators would have activated a live K entry if price remained available.
4. **No official loss occurred.** This was a model-sharpening miss, not a bankroll drawdown.

### Missed / Weakened

1. **Seymour's pitch-level K profile was underweighted.** Sweeper, fastball, and changeup all generated strikeout conversion.
2. **Team-level K rate was weighted too heavily.** KC's 19.8% K rate vs LHP suppressed the projection too aggressively.
3. **Arsenal diversity mattered.** Seymour had three K-producing pitches rather than a one-pitch or contact-heavy profile.
4. **KC LRS was too high against this specific arsenal.** The Royals' contact profile should not fully override a pitcher showing multiple bat-missing lanes.
5. **Whiff/swing upside was not captured pregame.** Actual whiff/swing reached 36%, far above the 23-25% minimum standard.

---

## Kansas City LRS Adjustment

```yaml
lineup_resistance_update:
  opponent: Kansas City Royals
  split: vs_lhp
  previous_lrs: 5.9
  adjusted_lrs_range: 5.4_to_5.7
  context: arsenal_dependent
  current_signal:
    - Shane McClanahan 2026-07-01: 6.0 IP, 4 K, 21% whiff_swing, 32% CSW
    - Ian Seymour 2026-07-02: 6.0 IP, 8 K, 36% whiff_swing, 34% CSW
  interpretation: >
    Kansas City remains a low-K contact opponent, but the LRS cannot be treated as an automatic
    hard-pass when the pitcher has multiple active whiff pitch families. KC suppresses mediocre or
    borderline whiff profiles, but they can still be beaten by arsenal diversity and strong swing-and-miss.
```

---

## Patch Recommendations

```yaml
patches_added:
  - arsenal_override_for_high_lrs
  - multi_pitch_whiff_family_gate
  - liveflow_reentry_after_pregame_pass

arsenal_override_for_high_lrs:
  action: add
  rule: >
    High opponent LRS can be partially overridden when the pitcher owns multiple projected whiff lanes
    and is not reliant on a single contact-oriented pitch. Do not auto-pass solely because team K rate
    is below 20%.

multi_pitch_whiff_family_gate:
  action: add
  rule: >
    Upgrade K projection when at least two pitch families project to generate whiffs and one additional
    pitch has called-strike support. Seymour showed sweeper, fastball, and changeup strikeout conversion.

liveflow_reentry_after_pregame_pass:
  action: strengthen
  rule: >
    If a pregame K prop is passed because of LRS but the pitcher opens with 30%+ CSW and 28%+ whiff/swing
    through two innings, the pitcher becomes eligible for LiveFlow reentry even against a red-zone opponent.
```

---

## Threshold Lesson

```yaml
threshold_lesson:
  market_reviewed: 5_plus
  official_investment: false
  result_type: missed_winning_pass
  classification: over_penalized_opponent_lrs
  pitcher_command_read: passed
  leash_read: passed
  csw_read: passed
  whiff_read: strongly_passed
  opponent_lrs: too_aggressive_without_arsenal_context
  future_rule: >
    LRS must be paired with pitcher-specific whiff architecture. A low-K lineup can still become playable
    if the pitcher has multi-pitch bat-missing support and clears whiff/swing floors.
```

---

## Final Classification

```yaml
postmortem_classification:
  signal: model_sharpening_positive
  official_bet: false
  result_type: missed_winning_pass
  failure_type: over_penalized_lrs
  command_read: confirmed
  leash_read: confirmed
  contact_suppression_read: mixed
  csw_read: passed
  whiff_read: strongly_passed
  opponent_lrs: too_high_without_arsenal_override
  market_selection: pass_was_defensible_but_too_conservative
  bankroll_result: no_loss
  pnl: 0.00
  final_status: add_arsenal_context_to_LRS
```

---

## Model State After Note

```yaml
model_state_update:
  keep_active:
    - lrs_5_3_standard_stake_ban
    - whiff_swing_minimum_for_standard_k
    - efficient_contact_k_suppression_gate
  modify:
    - kansas_city_vs_lhp_red_zone_rule
  add:
    - arsenal_override_for_high_lrs
    - multi_pitch_whiff_family_gate
    - liveflow_reentry_after_pregame_pass
  operational_change: >
    Continue reducing pregame K volume, but do not let high LRS alone eliminate pitchers with confirmed
    multi-pitch whiff architecture. Use LiveFlow reentry aggressively when early CSW and whiff/swing clear.
```

---

## Tags

`MODEL_SHARPENING` `IAN_SEYMOUR` `NO_BET` `MISSED_WINNING_PASS` `ROYALS_LRS_ADJUSTMENT` `ARSENAL_OVERRIDE` `MULTI_PITCH_WHIFF_GATE` `LIVEFLOW_REENTRY` `K_MODEL_REPAIR`
