# SharpEdge MLB K Prop Postmortem — 2026-06-20

## Slate Result

Two William Hill strikeout investments were logged from the 2026-06-20 MLB slate. Both positions won.

| Pitcher | Market | Book | Stake Type | Entry Odds | Stake | Paid / Profit | Result | Outcome |
|---|---:|---|---|---:|---:|---:|---:|---|
| Walker Buehler | 5+ Ks | William Hill | Cash | +121 | $5.00 | $11.05 paid / +$6.05 profit | 7 Ks | WIN |
| Paul Skenes | 7+ Ks | William Hill | Bonus Bet | -130 | $10.00 bonus | $7.69 profit | 8 Ks | WIN |

```yaml
slate_summary:
  date: 2026-06-20
  sport: MLB
  market_type: pitcher_strikeouts
  book: William Hill
  positions: 2
  wins: 2
  losses: 0
  cash_staked: 5.00
  bonus_bet_staked: 10.00
  cash_paid: 11.05
  cash_profit: 6.05
  bonus_bet_profit: 7.69
  total_profit: 13.74
```

---

# Walker Buehler — 5+ Strikeouts

## Position Summary

**Game:** San Diego Padres at Texas Rangers  
**Book:** William Hill  
**Market:** Walker Buehler 5+ pitching strikeouts  
**Entry Odds:** +121  
**Cash Wagered:** $5.00  
**Paid:** $11.05  
**Profit:** +$6.05  
**Final Result:** 7 strikeouts  
**Outcome:** WIN

## Final Pitching Line

| IP | H | R | ER | BB | K | HR | ERA |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 5.1 | 5 | 1 | 1 | 1 | 7 | 0 | 1.69 |

## Core Metrics

| Metric | Result |
|---|---:|
| Total Pitches | 87 |
| Average Pitch Velocity | 89.4 mph |
| Top-Level Velo Marker | 94.8 mph |
| Exit Velocity Marker | 108.0 |
| Swings | 45 |
| Called Strikes | 15 |
| Whiffs | 13 |
| CSW | 32% |
| Whiff / Swing | 29% |
| Strike Rate | 69% |
| Zone Rate | 51% |
| Chase Rate | 33% |
| First-Pitch Strike | 86% |

## Pitch Mix

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CStr+Whiff |
|---|---:|---:|---:|---:|---:|---:|---:|
| Slider | 22% / 19 | 87.5 | 3 | 11 | 1 | 5 | 32% |
| 4-Seam Fastball | 22% / 19 | 93.2 | 2 | 7 | 7 | 3 | 53% |
| Sinker | 18% / 16 | 93.8 | 1 | 8 | 5 | 1 | 38% |
| Cutter | 16% / 14 | 89.7 | 1 | 6 | 2 | 0 | 14% |
| Sweeper | 9% / 8 | 81.5 | 0 | 5 | 0 | 1 | 13% |
| Changeup | 8% / 7 | 87.9 | 0 | 5 | 0 | 2 | 29% |
| Knuckle Curve | 5% / 4 | 79.4 | 0 | 3 | 0 | 1 | 25% |
| All | 100% / 87 | 89.4 | 7 | 45 | 15 | 13 | 32% |

## What Worked

1. Soft-threshold plus-money attack was correct. Buehler 5+ at +121 gave the model a favorable payout profile without needing a full ceiling outcome.
2. First-pitch strike rate was elite. 86% first-pitch strike gave Buehler immediate count leverage and reduced pitch-count drag.
3. Slider carried the K production. The slider produced 3 strikeouts and 5 whiffs.
4. Four-seam fastball was a called-strike weapon. The four-seamer produced 7 called strikes and 3 whiffs on only 19 pitches.

## Risk Notes

- Texas was a tougher LRS opponent than the prior Buehler/Baltimore win.
- Contact quality allowed stayed elevated: 93.4 average EV on batted balls and 6 hard-hit balls.
- This win was made safer by command and first-pitch dominance, not by elite contact suppression.

## Model Grade

| Category | Grade |
|---|---:|
| Result | A |
| Projection Quality | A- |
| Entry Execution | A |
| Market Timing | A |
| Leash Stability | B+ |
| Pitch Efficiency | A- |
| CSW | A- |
| Whiff Sustainability | B+ |
| Contact Suppression | B- |
| LRS Accuracy | A- |
| Final Grade | A- |

```yaml
buehler_model_learning:
  confirmed:
    - plus_money_soft_threshold_attack
    - 5_plus_threshold_value
    - first_pitch_strike_as_runway_stabilizer
    - slider_whiff_path
  caution:
    - contact_quality_allowed_remained_elevated
    - do_not_auto_upgrade_buehler_to_6_plus_against_high_lrs_lineups
```

---

# Paul Skenes — 7+ Strikeouts

## Position Summary

**Game:** Pittsburgh Pirates at Colorado Rockies  
**Book:** William Hill  
**Market:** Paul Skenes 7+ pitching strikeouts  
**Entry Odds:** -130  
**Stake Type:** Bonus Bet  
**Bonus Bet Amount:** $10.00  
**Paid / Profit:** $7.69  
**Final Result:** 8 strikeouts  
**Outcome:** WIN

## Pregame Projection Snapshot

| Metric | Projection |
|---|---:|
| Mean | 7.4 K |
| Median | 7 K |
| 7+ Hit Probability | 62-65% |
| Market Implied Probability at -130 | 56.5% |
| Estimated Edge | +5.5 to +8.5 percentage points |
| Grade | A |

## Final Pitching Line

| IP | H | R | ER | BB | K | HR | ERA |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 6.0 | 4 | 2 | 2 | 2 | 8 | 1 | 3.00 |

## Core Metrics

| Metric | Result |
|---|---:|
| Total Pitches | 104 |
| Average Pitch Velocity | 92.2 mph |
| Top-Level Velo Marker | 98.6 mph |
| Exit Velocity Marker | 105.9 |
| Swings | 53 |
| Called Strikes | 10 |
| Whiffs | 19 |
| CSW | 28% |
| Whiff / Swing | 36% |
| Strike Rate | 61% |
| Zone Rate | 40% |
| Chase Rate | 34% |
| First-Pitch Strike | 46% |

## Pitch Mix

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CStr+Whiff |
|---|---:|---:|---:|---:|---:|---:|---:|
| 4-Seam Fastball | 51% / 53 | 96.5 | 2 | 29 | 7 | 6 | 25% |
| Changeup | 28% / 29 | 88.7 | 3 | 14 | 1 | 7 | 28% |
| Slider | 12% / 12 | 86.8 | 0 | 4 | 1 | 0 | 8% |
| Sweeper | 9% / 9 | 85.1 | 3 | 5 | 1 | 5 | 67% |
| Sinker | 1% / 1 | 96.5 | 0 | 1 | 0 | 1 | 100% |
| All | 100% / 104 | 92.2 | 8 | 53 | 10 | 19 | 28% |

## What Worked

1. Correct rung selection. The 7+ at -130 was the correct target. The 6+ was too expensive at -280, while 8+ was higher variance.
2. Colorado LRS was attackable. The Rockies matchup gave enough strikeout runway for the premium arm to clear 7+.
3. Whiff volume carried the ticket. Skenes generated 19 whiffs and a 36% whiff-per-swing rate.
4. Sweeper was the separator. The sweeper produced 3 strikeouts and 5 whiffs on only 9 pitches.
5. Changeup gave him a second K lane. The changeup produced 3 strikeouts and 7 whiffs.

## Risk Notes

- First-pitch strike rate was only 46%, which created some efficiency pressure.
- CSW was solid but not elite at 28%.
- 104 pitches through 6.0 innings means 8+ cashed, but the line still required a full workload.

## Model Grade

| Category | Grade |
|---|---:|
| Result | A |
| Projection Quality | A |
| Entry Execution | A |
| Market Timing | A- |
| Leash Stability | A- |
| Pitch Efficiency | B |
| CSW | B+ |
| Whiff Sustainability | A |
| Contact Suppression | B+ |
| LRS Accuracy | A |
| Final Grade | A |

```yaml
skenes_model_learning:
  confirmed:
    - primary_edge_rank_accuracy
    - 7_plus_rung_selection
    - colorado_lrs_attack
    - whiff_sustainability
    - bonus_bet_conversion_layer
  caution:
    - first_pitch_strike_rate_can_create_pitch_count_drag
    - avoid_paying_extreme_juice_on_6_plus_even_when_projection_is_strong
```

---

# Combined System Learning

```yaml
sharpedge_2026_06_20_learning:
  confirmed:
    - william_hill_execution_layer_remains_useful
    - bonus_bets_can_be_deployed_on_high_probability_minus_price_edges
    - cash_positions_should_prioritize_plus_money_soft_thresholds
    - lrs_adjustment_improved_target_selection
    - correct_rung_selection_outperformed_blind_laddering
  rules_reinforced:
    - do_not_take_name_brand_ceiling_rungs_when_market_forces_wrong_threshold
    - attack_median_thresholds_when_price_is_misaligned
    - use_first_pitch_strike_rate_as_live_runway_stabilizer
    - use_whiff_per_swing_plus_csw_to_separate_real_k_paths_from_name_value
```

## Tags

`WIN` `WILLIAM_HILL_EXECUTION_LAYER` `BONUS_BET_CONVERSION` `PLUS_MONEY_SOFT_THRESHOLD` `PRIMARY_EDGE_CONFIRMED` `LRS_CONFIRMED` `CORRECT_RUNG_SELECTION` `WHIFF_SUSTAINABILITY_CONFIRMED` `FIRST_PITCH_STRIKE_RUNWAY` `DO_NOT_BLIND_LADDER`
