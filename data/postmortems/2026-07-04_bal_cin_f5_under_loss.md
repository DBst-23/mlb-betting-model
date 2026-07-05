# SharpEdge MLB F5 Total Postmortem — 2026-07-04

## Position Summary

**Date:** 2026-07-04  
**Book:** William Hill  
**Game:** Baltimore Orioles at Cincinnati Reds  
**Market:** 1st 5 Innings Total Runs  
**Position:** Under 5  

| Market | Entry Odds | Stake | To Win | Paid | Profit/Loss | Result | Outcome |
|---|---:|---:|---:|---:|---:|---|---|
| F5 Under 5 | -130 | $18.00 | $13.85 | $0.00 | -$18.00 | BAL/CIN exceeded 5 before F5 completed | LOSS |

```yaml
position:
  date: 2026-07-04
  sport: MLB
  market_type: F5_total
  game: Baltimore Orioles at Cincinnati Reds
  book: William Hill
  target: Under_5
  odds: -130
  stake: 18.00
  to_win: 13.85
  paid: 0.00
  profit: -18.00
  outcome: LOSS
```

---

## Pregame Model Snapshot

The original F5 screen showed **F5 Total 5.0**, with Over +100 and Under -130 at William Hill. Broader market screens showed some shops in the -117 to -125 range, so William Hill was not the best number.

The model leaned Under because of push protection at 5, Hunter Greene's early-game strikeout/run-suppression profile, Baltimore's 25.0% recent K rate vs RHP, Cincinnati's poor recent offense vs RHP, and key Baltimore power bats missing.

| Input | Pregame Read |
|---|---|
| F5 Total | 5.0 |
| Model Projection | 3.9 to 4.1 |
| Fair Line | 4.0 to 4.5 |
| Edge Side | Under |
| Stake Guidance | Small only |
| Final Actual Stake | $18.00 |

```yaml
pregame_read:
  projected_f5_total: 3.9_to_4.1
  market_total: 5.0
  primary_reason:
    - push_protection_at_5
    - reds_recent_vs_rhp_weak
    - orioles_k_rate_vs_rhp_high
    - greene_best_early_game_arm
    - baltimore_missing_power_depth
  risk_flags:
    - great_american_ball_park_hr_environment
    - brandon_young_hard_contact_allowed
    - hunter_greene_fly_ball_and_command_volatility
    - early_walk_plus_damage_sequence
```

---

## Final F5 / Early Game Result

The ticket was effectively dead before the F5 window was complete. Live state showed the game reached **BAL 3 - CIN 4 in the bottom of the 2nd**, meaning 7 runs had already scored.

```yaml
early_game_state:
  live_score: BAL_3_CIN_4
  inning: bottom_2nd
  total_runs: 7
  under_5_status: lost
  failure_type: early_crooked_inning
```

---

## Batter Events Through First 5 Innings

### Key Baltimore Damage / Traffic

| Batter | Inning | Result | EV | LA | xBA | Notes |
|---|---:|---|---:|---:|---:|---|
| Gunnar Henderson | 1 | Single | 108.5 | — | .490 | Immediate hard contact |
| Pete Alonso | 1 | Walk | — | — | — | Early free baserunner |
| Samuel Basallo | 1 | Home Run | 105.7 | 27 | .930 | First-inning HR, 23/30 parks |
| Jackson Holliday | 2 | Walk | — | — | — | Free traffic |
| Adley Rutschman | 3 | Double | 97.3 | 25 | .270 | Extra-base damage |
| Pete Alonso | 3 | Single | 72.7 | 18 | .890 | Soft contact fell / high xBA |
| Adley Rutschman | 4 | Double | 96.6 | 10 | .730 | More extra-base pressure |
| Colton Cowser | 4 | Single | 75.7 | 24 | .860 | Contact conversion |
| Blaze Alexander | 4 | Single | 99.6 | 13 | .930 | Hard contact |

### Key Cincinnati Damage / Traffic

| Batter | Inning | Result | EV | LA | xBA | Notes |
|---|---:|---|---:|---:|---:|---|
| Sal Stewart | 1 | Double | 81.2 | 30 | .100 | Low xBA hit / variance |
| Spencer Steer | 2 | Single | 102.2 | 6 | .640 | Hard contact |
| Jose Trevino | 2 | Double | 94.7 | 17 | .570 | Extra-base damage |
| TJ Friedl | 2 | Triple | 102.9 | 5 | .590 | Crooked-inning accelerator |
| Elly De La Cruz | 2 | Single | 83.9 | 11 | .480 | Contact extension |
| Jose Trevino | 3 | Single | 101.3 | -2 | .310 | Continued pressure |
| Matt McLain | 4 | Walk | — | — | — | Free traffic |
| Elly De La Cruz | 4 | GIDP | 108.9 | — | .490 | Hard-hit grounder; damage avoided by DP |

---

## Brandon Young Final Line

| IP | H | R | ER | BB | K | HR | Pitches-Strikes | BF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5.0 | 8 | 4 | 4 | 3 | 5 | 0 | 102-65 | 25 |

### Brandon Young Core Metrics

| Metric | Result |
|---|---:|
| Total Pitches | 102 |
| Strike Rate | 64% |
| CSW | 27% |
| Whiff/Swing | 22% |
| Zone Rate | 50% |
| Chase Rate | 29% |
| First-Pitch Strike | 76% |
| BBE | 17 |
| Hits Allowed | 8 |
| Hard-Hit BBE | 8 |
| Avg EV Allowed | 94.1 mph |
| Max EV Marker | 108.9 mph |

### Brandon Young Pitch Mix

| Pitch | Usage | K | Swings | CStr | Whiffs | CStr+Whiff |
|---|---:|---:|---:|---:|---:|---:|
| 4-Seam | 47% / 48 | 3 | 26 | 8 | 6 | 29% |
| Slider | 17% / 17 | 0 | 7 | 1 | 2 | 18% |
| Sinker | 17% / 17 | 1 | 8 | 5 | 0 | 29% |
| Curveball | 12% / 12 | 1 | 2 | 4 | 1 | 42% |
| Splitter | 8% / 8 | 0 | 3 | 0 | 1 | 13% |
| All | 100% / 102 | 5 | 46 | 18 | 10 | 27% |

---

## Hunter Greene Final Line

| IP | H | R | ER | BB | K | HR | Pitches-Strikes | BF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3.1 | 7 | 8 | 8 | 4 | 7 | 1 | 89-53 | 20 |

### Hunter Greene Core Metrics

| Metric | Result |
|---|---:|
| Total Pitches | 89 |
| Strike Rate | 60% |
| CSW | 25% |
| Whiff/Swing | 33% |
| Zone Rate | 44% |
| Chase Rate | 26% |
| First-Pitch Strike | 50% |
| BBE | 9 |
| Hits Allowed | 7 |
| Hard-Hit BBE | 6 |
| Avg EV Allowed | 93.9 mph |
| Max EV Marker | 108.5 mph |

### Hunter Greene Pitch Mix

| Pitch | Usage | K | Swings | CStr | Whiffs | CStr+Whiff |
|---|---:|---:|---:|---:|---:|---:|
| 4-Seam | 53% / 47 | 2 | 17 | 6 | 1 | 15% |
| Slider | 40% / 36 | 5 | 24 | 1 | 14 | 42% |
| Sinker | 4% / 4 | 0 | 4 | 0 | 0 | 0% |
| Splitter | 2% / 2 | 0 | 0 | 0 | 0 | 0% |
| All | 100% / 89 | 7 | 45 | 7 | 15 | 25% |

---

## What Happened

The F5 Under did not lose because both offenses gradually outperformed the projection. It lost immediately through an early-game scoring avalanche. Baltimore generated first-inning power via Basallo's 105.7 mph home run after early traffic. Cincinnati answered with a second-inning hard-contact cluster: Steer single, Trevino double, Friedl triple, and De La Cruz single. By the bottom of the second, the game was already past the Under 5 threshold.

The pregame model's central error was treating the push at 5 as enough protection while underweighting Great American Ball Park volatility plus both starters' hard-contact paths. The play required avoiding exactly the type of early crooked inning that both pitcher profiles were capable of allowing.

---

## Model Diagnosis

### Confirmed

1. **Hunter Greene had strikeout stuff.** He produced 7 Ks and a 33% whiff/swing rate.
2. **Greene's slider was elite.** 14 whiffs on 24 swings, 42% CStr+Whiff, 5 Ks.
3. **Baltimore left-handed pressure was real.** Henderson, Basallo, Rutschman, Cowser, and Holliday all generated traffic or damage.
4. **Brandon Young's hard-contact risk was real.** He allowed 8 hard-hit balls and a 94.1 mph average EV.
5. **Great American Ball Park variance was material.** Early extra-base and HR damage overwhelmed the push-protected number.

### Missed / Weakened

1. **Greene run-prevention was overtrusted because of strikeout ability.** Strikeouts did not prevent hits, walks, or damage.
2. **Fastball quality failed.** Greene's 4-seam produced only 1 whiff on 17 swings and a 15% CStr+Whiff.
3. **Young's contact profile was too dangerous for an Under 5 at -130.** The 41.2% hard-hit profile entered the game as a known risk and became the game script.
4. **Price/stake mismatch.** Under 5 at -130 was not the best market price, and $18 was too large for a high-variance F5 under in a dangerous run park.
5. **Full-game total 9 was not respected enough.** A 9-run full-game environment means F5 Under 5 needs stronger suppression than this profile gave.
6. **Context favored Reds early but also exposed Young.** Superfan correctly highlighted Cincinnati's early path vs Young; the model weighted that as side pressure rather than total danger.

---

## Patch Recommendations

```yaml
patches_added:
  - f5_under_park_volatility_gate
  - f5_under_hard_contact_dual_starter_gate
  - f5_total_price_discipline_gate
  - f5_under_full_game_total_context_gate
  - strikeout_stuff_not_run_prevention_gate

f5_under_park_volatility_gate:
  action: add
  rule: >
    Avoid F5 unders in high-HR or high-run parks unless both starters have low hard-contact, low-walk,
    and low-HR profiles. Push protection alone is not enough.

f5_under_hard_contact_dual_starter_gate:
  action: add
  rule: >
    If either starter has 40%+ recent hard-hit allowed or unstable command, F5 under requires a better number
    than 5.0 or a heavily suppressed offensive environment.

f5_total_price_discipline_gate:
  action: add
  rule: >
    When the best market is available at -117 to -120, do not take -130 unless stake is reduced sharply.
    Price discipline is mandatory during drawdowns.

f5_under_full_game_total_context_gate:
  action: add
  rule: >
    F5 Under 5 in a full-game total of 9+ requires both starters to clear suppression gates. If the market
    expects a run environment, the F5 under must have cleaner pitcher/contact support.

strikeout_stuff_not_run_prevention_gate:
  action: add
  rule: >
    Do not equate strikeout upside with run prevention. Greene-type arms can produce strikeouts while still
    allowing walks, elevated contact, and crooked innings.
```

---

## Threshold Lesson

```yaml
threshold_lesson:
  market: F5_Under_5
  result_type: early_loss
  failed_by: bottom_2nd
  failure_type: early_crooked_inning_high_variance_park
  starter_command_read: failed_for_greene
  hard_contact_read: underestimated
  market_selection: right_number_shape_wrong_environment
  stake_assessment: too_high_for_high_variance_under
  future_rule: >
    F5 Under 5 should not be treated as safe merely because it has push protection. In volatile parks,
    hard-contact and walk risk must be low for both starters, or the play is pass/live-only.
```

---

## Edge Review

```yaml
edge_review:
  model_signal: negative
  official_bet: true
  bankroll_result: loss
  pnl: -18.00
  emotional_context: >
    User was already frustrated after recent pitcher K losses. This loss amplified the need to pause official
    pregame MLB exposure and rebuild the F5 model with stricter gates.
  technical_context: >
    The F5 model correctly identified some under-supporting inputs but overweighted push protection and
    underweighted environment plus dual starter hard-contact volatility.
  operational_response: >
    Pause official MLB pregame bets. Continue logging and paper-trading F5 totals until the new gates are tested.
```

---

## Final Classification

```yaml
postmortem_classification:
  signal: negative
  official_bet: true
  market_type: F5_total
  position: Under_5
  failure_type: early_crooked_inning
  sub_type: high_variance_park_contact_damage
  pitcher_read:
    hunter_greene: strikeout_stuff_confirmed_run_prevention_failed
    brandon_young: hard_contact_risk_confirmed
  market_selection: right_number_shape_wrong_environment
  price_assessment: suboptimal_at_minus_130
  stake_assessment: too_high_for_drawdown_context
  pnl: -18.00
  final_status: pause_pregame_MLB_exposure_and_rebuild_F5_gates
```

---

## Model State After Loss

```yaml
model_state_update:
  pause:
    official_pregame_MLB_bets: true
  continue:
    liveflow_monitoring: true
    paper_trade_F5_totals: true
    postmortem_logging: true
  add_patches:
    - f5_under_park_volatility_gate
    - f5_under_hard_contact_dual_starter_gate
    - f5_total_price_discipline_gate
    - f5_under_full_game_total_context_gate
    - strikeout_stuff_not_run_prevention_gate
```

---

## Tags

`LOSS` `BAL_CIN` `F5_TOTAL` `UNDER_5` `WILLIAM_HILL` `EARLY_CROOKED_INNING` `GREAT_AMERICAN_BALL_PARK` `HARD_CONTACT_DAMAGE` `HUNTER_GREENE` `BRANDON_YOUNG` `F5_MODEL_REPAIR` `PRICE_DISCIPLINE` `PAUSE_PREGAME_MLB`
