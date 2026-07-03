# SharpEdge MLB K Model Sharpening Note — 2026-07-02

## Context

**Date:** 2026-07-02  
**Game:** Cincinnati Reds at Milwaukee Brewers  
**Pitchers Reviewed:** Chase Burns and Jacob Misiorowski  
**Official Investment:** No  
**Purpose:** Pregame look-hunt postmortem and K model sharpening  

This file reviews two pitchers from the 07-02 pregame K slate hunt. Neither was an official SharpEdge investment. The goal is to sharpen the model around market inflation, opponent LRS, arsenal concentration, and threshold selection.

```yaml
model_review:
  date: 2026-07-02
  sport: MLB
  market_type: pitcher_strikeouts
  official_investment: false
  reviewed_pitchers:
    - Chase Burns
    - Jacob Misiorowski
  purpose: model_sharpening
```

---

# Chase Burns Review

## Pregame Read

Burns was flagged as a risky K target because Milwaukee had already confirmed a strong LRS profile against left-handed and high-upside K arms: low chase, walk pressure, and K-conversion resistance. The model preferred no standard pregame exposure unless the price was extremely favorable.

```yaml
chase_burns_pregame:
  opponent: Milwaukee Brewers
  reviewed_market_shape: 7_plus_or_8_plus_thresholds
  pregame_concern:
    - brewers_lrs_red_flag
    - low_chase_profile
    - walk_pressure
    - contact_damage_depth
    - price_required_too_much_ceiling
  decision: PASS_PREGAME
```

## Final Pitching Line

| IP | H | R | ER | BB | K | HR | ERA | Pitches-Strikes | BF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6.0 | 4 | 2 | 2 | 2 | 4 | 1 | 3.00 | 89-55 | 23 |

## Core Metrics

| Metric | Result |
|---|---:|
| Total Pitches | 89 |
| Strikes | 55 |
| Strike Rate | 62% |
| Swings | 35 |
| Called Strikes | 20 |
| Whiffs | 8 |
| CStr+Whiff | 28 / 89 |
| CSW | 31% |
| Whiff / Swing | 23% |
| Zone Rate | 48% |
| Chase Rate | 24% |
| First-Pitch Strike | 57% |
| BBE | 17 |
| Hits Allowed | 4 |
| Hard-Hit BBE | 9 |
| Avg EV Allowed | 93.9 mph |
| Top EV Marker | 103.8 mph |
| Velo Marker | 99.4 mph |

## Pitch Mix

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CStr+Whiff |
|---|---:|---:|---:|---:|---:|---:|---:|
| 4-Seam Fastball | 69% / 61 | 97.1 | 1 | 26 | 16 | 1 | 28% |
| Slider | 31% / 28 | 89.1 | 3 | 9 | 4 | 7 | 39% |
| All | 100% / 89 | 94.6 | 4 | 35 | 20 | 8 | 31% |

## Burns Diagnosis

Burns pitched well enough from a run-prevention standpoint but did not come close to the market's aggressive K thresholds. The pass was correct.

### Confirmed

1. **Brewers LRS remained dangerous.** Burns reached 6.0 innings but finished with only 4 strikeouts.
2. **Fastball-heavy usage suppressed K conversion.** His 4-seam was 69% of the mix and generated only 1 whiff on 26 swings.
3. **Slider was the true K pitch but too low in volume.** The slider generated 7 whiffs on 9 swings and 3 of 4 strikeouts.
4. **Contact damage was elevated.** Milwaukee produced 17 BBE, 9 hard-hit balls, and a 93.9 mph average EV.
5. **Chase was not strong enough.** 24% chase did not support a high K ladder.

### Missed / Weakened

The model did not need major correction on Burns. The pregame caution was validated. If anything, this strengthens the no-standard-exposure rule against Milwaukee K overs unless the pitcher has elite multi-pitch whiff support and a soft threshold.

```yaml
chase_burns_classification:
  official_bet: false
  result_type: correct_pass
  failure_if_bet: full_threshold_miss
  command_read: mixed
  leash_read: confirmed
  csw_read: passed
  whiff_read: borderline
  opponent_lrs: confirmed_high
  pitch_mix_issue: fastball_heavy_k_conversion_failure
  final_status: keep_brewers_lrs_red_flag_active
```

---

# Jacob Misiorowski Review

## Pregame Read

Misiorowski was the best raw K arm on the slate but was flagged for market inflation. William Hill pushed the market into high ceiling territory: 9+, 10+, and O9.5. The model did not want to pay full tax for a ceiling outcome.

```yaml
jacob_misiorowski_pregame:
  opponent: Cincinnati Reds
  raw_k_profile: elite
  reviewed_market_shape:
    - 9_plus_heavily_priced
    - 10_plus_near_even_money
    - over_9_5_plus_100
  pregame_concern:
    - market_inflation
    - extremely_high_threshold
    - no_push_protection
  decision: PASS_PREGAME
```

## Final Pitching Line

| IP | H | R | ER | BB | K | HR | ERA | Pitches-Strikes | BF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5.0 | 5 | 5 | 1 | 0 | 10 | 2 | 1.80 | 82-57 | 21 |

## Core Metrics

| Metric | Result |
|---|---:|
| Total Pitches | 82 |
| Strikes | 57 |
| Strike Rate | 70% |
| Swings | 43 |
| Called Strikes | 14 |
| Whiffs | 20 |
| CStr+Whiff | 34 / 82 |
| CSW | 41% |
| Whiff / Swing | 47% |
| Zone Rate | 52% |
| Chase Rate | 36% |
| First-Pitch Strike | 71% |
| BBE | 11 |
| Hits Allowed | 5 |
| Hard-Hit BBE | 4 |
| Avg EV Allowed | 80.0 mph |
| Top EV Marker | 109.5 mph |
| Velo Marker | 103.8 mph |

## Pitch Mix

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CStr+Whiff |
|---|---:|---:|---:|---:|---:|---:|---:|
| 4-Seam Fastball | 62% / 51 | 101.4 | 7 | 26 | 10 | 10 | 39% |
| Curveball | 20% / 16 | 88.6 | 3 | 9 | 3 | 7 | 63% |
| Cutter | 13% / 11 | 95.3 | 0 | 6 | 1 | 2 | 27% |
| Slider | 5% / 4 | 89.2 | 0 | 2 | 0 | 1 | 25% |
| All | 100% / 82 | 97.5 | 10 | 43 | 14 | 20 | 41% |

## Misiorowski Diagnosis

Misiorowski validated the elite K profile completely. He reached 10 strikeouts in only 5.0 innings with a 41% CSW and 47% whiff/swing. The model pass was defensible from a market discipline standpoint, but this becomes a critical sharpening note: true elite whiff profiles can beat high thresholds when the arsenal clears the multi-pitch whiff gate.

### Confirmed

1. **Elite whiff profile was real.** 20 whiffs on 43 swings and 47% whiff/swing.
2. **Multi-pitch whiff family cleared.** 4-seam and curveball both generated elite K conversion.
3. **Velocity was overwhelming.** Top velocity marker reached 103.8 mph, and fastball averaged 101.4 mph.
4. **Command was clean.** Zero walks and 70% strike rate.
5. **The raw K ceiling was correctly identified.** Misiorowski was the top raw K pitcher on the board.

### Missed / Weakened

1. **The market-inflation pass may have been too strict.** While thresholds were high, the pitcher had enough active whiff architecture to clear them.
2. **Elite arsenal override should apply earlier.** A 47% whiff/swing ceiling profile belongs in a separate class from ordinary plus-money ladders.
3. **High threshold does not equal bad bet if the pitcher is a true outlier.** Misiorowski was a true outlier.

```yaml
jacob_misiorowski_classification:
  official_bet: false
  result_type: missed_winning_pass
  market_reviewed: high_threshold_k_ladder
  command_read: confirmed
  leash_read: sufficient
  csw_read: elite
  whiff_read: elite
  opponent_lrs: beaten_by_elite_arsenal
  market_selection: pass_was_disciplined_but_too_conservative
  final_status: add_elite_outlier_exception
```

---

## Combined Model Lessons

Burns and Misiorowski show the difference between **fastball-heavy K promise** and **true elite whiff architecture**.

```yaml
combined_lessons:
  chase_burns:
    lesson: >
      High velocity and CSW are not enough when the primary fastball does not generate whiffs
      and the opponent has elevated LRS. Burns needed slider volume to drive Ks, but the fastball
      carried the pitch mix and suppressed ceiling.
  jacob_misiorowski:
    lesson: >
      True elite whiff architecture can override high thresholds. Misiorowski had fastball plus
      curveball dominance, elite velocity, 47% whiff/swing, 41% CSW, and zero walks.
```

---

## Patch Recommendations

```yaml
patches_added:
  - elite_outlier_k_threshold_exception
  - primary_fastball_whiff_quality_gate
  - two_pitch_elite_whiff_override

elite_outlier_k_threshold_exception:
  action: add
  rule: >
    Do not auto-pass high K thresholds when a pitcher projects as a true elite outlier with
    35%+ projected CSW, 30%+ projected whiff/swing, strong command, and at least two active
    K pitch families. High threshold still requires price discipline, but elite outliers need
    their own tier.

primary_fastball_whiff_quality_gate:
  action: strengthen
  rule: >
    Fastball-heavy pitchers require the fastball itself to generate whiffs. If fastball usage is
    above 55% and fastball whiff/swing projects weak, downgrade K ceiling even if called-strike
    volume is strong.

two_pitch_elite_whiff_override:
  action: add
  rule: >
    Upgrade K ceiling when two pitch families both clear elite CStr+Whiff or whiff indicators.
    Misiorowski's 4-seam and curveball combination should override ordinary market-inflation caution.
```

---

## Updated Opponent / Pitcher Tags

```yaml
opponent_updates:
  milwaukee_brewers:
    lrs_status: remains_high
    reason: >
      Burns reached 6 innings and had a 31% CSW but finished with only 4 Ks. Milwaukee continues
      to suppress non-elite K conversion.
  cincinnati_reds:
    lrs_status: vulnerable_to_elite_velocity
    reason: >
      Misiorowski produced 10 Ks in 5 innings with a 47% whiff/swing rate and zero walks.

pitcher_archetype_updates:
  chase_burns:
    archetype: fastball_heavy_power_arm
    caution: fastball_whiff_quality_required
  jacob_misiorowski:
    archetype: elite_outlier_two_pitch_whiff_monster
    status: qualifies_for_elite_threshold_exception
```

---

## Final Classification

```yaml
postmortem_classification:
  signal: model_sharpening_mixed
  official_bet: false
  bankroll_result: no_loss
  pitchers:
    chase_burns:
      result_type: correct_pass
      model_read: confirmed
      key_lesson: fastball_heavy_profiles_need_fastball_whiffs
    jacob_misiorowski:
      result_type: missed_winning_pass
      model_read: too_conservative_due_market_inflation_filter
      key_lesson: elite_outlier_profiles_need_exception_tier
  final_status: add_outlier_k_tier_and_fastball_quality_gate
```

---

## Tags

`MODEL_SHARPENING` `CHASE_BURNS` `JACOB_MISIOROWSKI` `NO_BET` `CORRECT_PASS` `MISSED_WINNING_PASS` `BREWERS_LRS_CONFIRMED` `ELITE_OUTLIER_EXCEPTION` `TWO_PITCH_WHIFF_OVERRIDE` `FASTBALL_WHIFF_GATE` `K_MODEL_REPAIR`
