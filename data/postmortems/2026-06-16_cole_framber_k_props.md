# SharpEdge MLB K Prop Postmortem — 2026-06-16

## Slate Result Summary

| Pitcher | Market | Entry Odds | Stake | Result | Outcome | Payout | Profit |
|---|---:|---:|---:|---:|---|---:|---:|
| Gerrit Cole | 6+ Ks | -117 | $6.00 | 6 Ks | Win | $11.16 | +$5.16 |
| Framber Valdez | 5+ Ks | -117 | $4.18 | 6 Ks | Win | $7.77 | +$3.59 |

**Total Stake:** $10.18  
**Total Return:** $18.93  
**Net Profit:** +$8.75  
**Slate ROI:** +85.95%

---

## Market Timing / CLV

```yaml
market_timing:
  gerrit_cole_6_plus:
    entry_odds: -117
    current_observed_odds: -108
    official_closing_odds: null
    current_clv_status: NEGATIVE_CANDIDATE
    note: "Later market showed cheaper YES price than entry. Final CLV requires official close."

  framber_valdez_5_plus:
    entry_odds: -117
    current_observed_odds: -104
    official_closing_odds: null
    current_clv_status: NEGATIVE_CANDIDATE
    note: "Later market showed cheaper YES price than entry. Final CLV requires official close."
```

**Interpretation:** Both tickets cashed despite observed market drift against the original entries. This separates **projection edge** from **market timing edge**.

---

# Gerrit Cole — 6+ Strikeouts

## Final Line

```yaml
gerrit_cole_final:
  team: New York Yankees
  opponent: Chicago White Sox
  decision: W
  innings_pitched: 6.0
  hits: 3
  runs: 2
  earned_runs: 2
  walks: 2
  strikeouts: 6
  home_runs: 1
  pitches: 90
  strikes: 59
  batters_faced: 23
  groundouts: 5
  flyouts: 5
```

## Pitch Profile

```yaml
gerrit_cole_pitch_profile:
  average_exit_velocity_allowed: 90.4
  average_pitch_velocity: 91.2
  top_level_velocity_marker: 97.7
  total_pitches: 90
  total_swings: 43
  total_called_strikes: 16
  total_whiffs: 6
  called_strikes_plus_whiffs: 22
  csw_rate: 24.4
  whiff_rate_per_swing: 14.0
  strike_rate: 66.0
  first_pitch_strike_rate: 65.0
  chase_rate: 40.0
```

## Pitch Mix

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CSW |
|---|---:|---:|---:|---:|---:|---:|---:|
| Unknown | 31% / 28 | -- | 1 | 16 | 2 | 1 | 11% |
| 4-Seam Fastball | 28% / 25 | 95.9 | 4 | 12 | 5 | 4 | 36% |
| Slider | 16% / 14 | 89.0 | 0 | 7 | 1 | 1 | 14% |
| Sinker | 9% / 8 | 95.0 | 0 | 2 | 4 | 0 | 50% |
| Knuckle Curve | 9% / 8 | 82.1 | 0 | 3 | 1 | 0 | 13% |
| Changeup | 8% / 7 | 85.2 | 1 | 3 | 3 | 0 | 43% |

## SharpEdge Read

Cole did not win this ticket through a dominant whiff ceiling. The win came from stable leash, six full innings, strike efficiency, and enough matchup resistance leakage from Chicago to reach the exact threshold.

The fastball was the carrying pitch for strikeouts: 4 of his 6 Ks came through the four-seam. Even with overall whiff rate modest, 65% first-pitch strike rate and 66% strike rate gave him the runway needed to finish six innings.

## Grades

```yaml
gerrit_cole_grades:
  result_grade: A
  projection_quality_grade: A-
  market_timing_grade: C
  execution_grade: B+
  leash_stability_grade: A
  csw_grade: B-
  whiff_sustainability_grade: C+
  contact_suppression_grade: A-
  final_sharpedge_grade: A-
```

## Tags

```yaml
gerrit_cole_tags:
  - WIN
  - EXACT_THRESHOLD_HIT
  - MODERATE_LADDER_EFFICIENCY_OVERRIDE
  - LEASH_CONFIRMED
  - CONTACT_SUPPRESSION_CONFIRMED
  - WHIFFS_BELOW_ELITE
  - MARKET_DRIFT_AGAINST_ENTRY
```

---

# Framber Valdez — 5+ Strikeouts

## Final Line

```yaml
framber_valdez_final:
  team: Houston Astros
  opponent: Detroit Tigers
  innings_pitched: 6.0
  hits: 6
  runs: 1
  earned_runs: 0
  walks: 3
  strikeouts: 6
  home_runs: 0
  pitches: 92
  strikes: 57
  batters_faced: 27
  groundouts: 9
  flyouts: 3
```

## Pitch Profile

```yaml
framber_valdez_pitch_profile:
  average_exit_velocity_allowed: 89.0
  average_pitch_velocity: 88.6
  top_level_velocity_marker: 96.0
  total_pitches: 92
  total_swings: 41
  total_called_strikes: 15
  total_whiffs: 10
  called_strikes_plus_whiffs: 25
  csw_rate: 27.2
  whiff_rate_per_swing: 24.4
  strike_rate: 62.0
  first_pitch_strike_rate: 52.0
  chase_rate: 29.0
```

## Pitch Mix

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CSW |
|---|---:|---:|---:|---:|---:|---:|---:|
| Sinker | 36% / 33 | 94.3 | 0 | 18 | 7 | 2 | 27% |
| Changeup | 35% / 32 | 89.7 | 4 | 13 | 7 | 4 | 34% |
| Curveball | 27% / 25 | 79.4 | 2 | 10 | 1 | 4 | 20% |
| Slider | 1% / 1 | 84.8 | 0 | 0 | 0 | 0 | 0% |
| 4-Seam Fastball | 1% / 1 | 96.0 | 0 | 0 | 0 | 0 | 0% |

## SharpEdge Read

Framber validated the soft-threshold entry. The 5+ ticket was the correct way to express the edge because his profile can produce strikeouts through depth and sequencing rather than pure strikeout aggression.

The changeup was the separator: 4 strikeouts, 34% CSW, and 31% whiff rate on swings. The sinker kept the inning runway alive with ground-ball pressure, and the curveball added two strikeouts as a secondary finisher.

The core SharpEdge thesis was correct: moderate threshold + stable leash + contact management + enough whiff support.

## Grades

```yaml
framber_valdez_grades:
  result_grade: A
  projection_quality_grade: A
  market_timing_grade: C-
  execution_grade: A-
  leash_stability_grade: A
  csw_grade: B+
  whiff_sustainability_grade: B+
  contact_suppression_grade: A
  final_sharpedge_grade: A
```

## Tags

```yaml
framber_valdez_tags:
  - WIN
  - SOFT_THRESHOLD_VALUE_TICKET
  - MODERATE_LADDER_EFFICIENCY_OVERRIDE
  - LEASH_CONFIRMED
  - GROUNDBALL_RUNWAY_CONFIRMED
  - CHANGEUP_FINISHER_CONFIRMED
  - MARKET_DRIFT_AGAINST_ENTRY
```

---

# System Learning

## Confirmed Rule

```yaml
moderate_ladder_efficiency_override:
  applies_to:
    - 5_plus_strikeout_markets
    - 6_plus_strikeout_markets
  confirmed_by:
    - gerrit_cole_6_plus_2026_06_16
    - framber_valdez_5_plus_2026_06_16
  core_finding: >
    Moderate K ladders can cash without elite CSW or elite whiff rates when leash stability,
    pitch count runway, opponent lineup resistance, and contact suppression are favorable.
```

## Workflow Reinforcement

```yaml
workflow_reinforcement:
  separate_grades_required:
    - result_grade
    - projection_quality_grade
    - market_timing_grade
    - execution_grade
  note: >
    These tickets won despite negative observed market drift, meaning the model projection
    outperformed market timing. Future logs must keep CLV and projection validation separate.
```

---

# Final Slate Grade

```yaml
sharpedge_slate_grade_2026_06_16:
  record: 2-0
  total_stake: 10.18
  total_return: 18.93
  net_profit: 8.75
  roi_percent: 85.95
  projection_quality: A
  market_timing: C
  bankroll_execution: A-
  final_grade: A
```
