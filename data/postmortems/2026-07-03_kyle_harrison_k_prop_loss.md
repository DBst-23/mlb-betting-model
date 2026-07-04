# SharpEdge MLB K Prop Postmortem — 2026-07-03

## Position Summary

**Date:** 2026-07-03  
**Book:** William Hill  
**Game:** Milwaukee Brewers at Arizona Diamondbacks  
**Pitcher:** Kyle Harrison  
**Market:** Pitching Strikeouts  

| Target | Entry Odds | Stake | To Win | Paid | Profit/Loss | Final Ks | Outcome |
|---|---:|---:|---:|---:|---:|---:|---|
| 6+ Strikeouts | +126 | $10.00 | $12.60 | $0.00 | -$10.00 | 3 | LOSS |

```yaml
position:
  date: 2026-07-03
  sport: MLB
  market_type: pitcher_strikeouts
  pitcher: Kyle Harrison
  team: Milwaukee Brewers
  opponent: Arizona Diamondbacks
  book: William Hill
  target: 6_plus_strikeouts
  odds: 126
  stake: 10.00
  to_win: 12.60
  paid: 0.00
  profit: -10.00
  result_strikeouts: 3
  outcome: LOSS
```

---

## Pregame Model Snapshot

Harrison was selected as a controlled plus-money K shot after Arizona vs LHP data and Harrison split data were sharpened.

| Metric | Pregame Projection |
|---|---:|
| Market | 6+ Strikeouts |
| Odds | +126 |
| Implied Probability | 44.2% |
| Refined Mean | 5.9 Ks |
| Median | 6 Ks |
| 6+ Hit Probability | 50-54% |
| Arizona LRS | 5.6 |
| Grade | B+ |
| Stake Style | Small / controlled |

The model allowed an arsenal override because Harrison showed strong K rates against both LHH and RHH in recent form.

```yaml
pregame_read:
  opponent_team_k_rate_vs_lhp: 14.0_percent
  opponent_lrs: 5.6
  harrison_vs_lhh_k_rate: 31.3_percent
  harrison_vs_rhh_k_rate: 32.7_percent
  decision: PLAYABLE_SMALL
  market_selected: 6_plus_at_plus_126
  avoided_market: 5_plus_at_minus_176
```

---

## Final Pitching Line

| IP | H | R | ER | BB | K | HR | ERA | Pitches-Strikes | BF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2.2 | 5 | 3 | 3 | 1 | 3 | 0 | 10.13 | 72-43 | 15 |

---

## Core Performance Metrics

| Metric | Result |
|---|---:|
| Total Pitches | 72 |
| Strikes | 43 |
| Strike Rate | 60% |
| Batters Faced | 15 |
| Swings | 31 |
| Called Strikes | 12 |
| Whiffs | 8 |
| CStr+Whiff | 20 / 72 |
| CSW | 28% |
| Whiff / Swing | 26% |
| Zone Rate | 47% |
| Chase Rate | 26% |
| First-Pitch Strike | 33% |
| BBE | 11 |
| Hits Allowed | 5 |
| Hard-Hit BBE | 6 |
| Average EV Allowed | 92.9 mph |
| Top EV Marker | 107.2 mph |
| Velo Marker | 97.7 mph |

---

## Pitch Mix

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CStr+Whiff |
|---|---:|---:|---:|---:|---:|---:|---:|
| 4-Seam Fastball | 57% / 41 | 95.9 | 1 | 22 | 7 | 5 | 29% |
| Slurve | 31% / 22 | 83.0 | 2 | 9 | 3 | 3 | 27% |
| Changeup | 10% / 7 | 87.6 | 0 | 0 | 2 | 0 | 29% |
| Sinker | 3% / 2 | 95.8 | 0 | 0 | 0 | 0 | 0% |
| All | 100% / 72 | 91.1 | 3 | 31 | 12 | 8 | 28% |

---

## What Happened

Harrison did not fail because the raw whiff indicators were completely dead. He produced 8 whiffs on 31 swings, a 26% whiff/swing rate, and a 28% CSW. Those are not terrible K indicators.

The bet failed because the runway collapsed. He lasted only 2.2 innings, faced only 15 batters, allowed 5 hits, 3 earned runs, 6 hard-hit balls, and needed 72 pitches to record 8 outs. The early damage and poor first-pitch strike rate destroyed the 6+ path before the strikeout profile could accumulate.

This is a major distinction: the model did not simply miss the bat-missing ability. It missed the probability that Arizona's low-K, hard-contact profile would break leash/runway quickly enough to make 6+ unreachable.

---

## Model Diagnosis

### Confirmed

1. **Whiff floor was present.** 26% whiff/swing cleared the minimum zone.
2. **CSW was playable.** 28% CSW was acceptable.
3. **The 5+ market was correctly avoided.** -176 would have been a worse price shape.
4. **Arizona hard-contact risk was real.** 6 hard-hit balls and 92.9 mph average EV confirmed the warning.
5. **Low-K team profile mattered.** Arizona forced balls in play and punished mistakes.

### Missed / Weakened

1. **Runway risk was massively underweighted.** Harrison needed 6+ Ks but lasted only 2.2 IP.
2. **Opponent team K rate of 14.0% should have been a harder gate.** The arsenal override was applied too aggressively.
3. **First-pitch strike collapse was not modeled.** 33% first-pitch strike created count stress.
4. **Hard-contact pockets should have blocked standard-ish exposure.** Arizona's contact damage translated directly into short outing risk.
5. **6+ against a 14% K opponent requires elite outlier, not just strong split K rates.** Harrison was strong, but not Misiorowski-tier.
6. **Stake was too high for a conflict profile.** $10 was too much for a B+ K prop during a K-market drawdown.

---

## Arizona LRS Update

```yaml
lineup_resistance_update:
  opponent: Arizona Diamondbacks
  split: vs_lhp
  previous_lrs: 5.6
  adjusted_lrs_range: 5.9_to_6.2
  current_signal:
    - Kyle Harrison 2026-07-03: 2.2 IP, 5 H, 3 ER, 1 BB, 3 K, 28% CSW, 26% whiff_swing, 6 hard_hit_BBE
  interpretation: >
    Arizona vs LHP should be treated as a red-zone K opponent when the expected nine has low team K rate,
    multiple low-K contact hitters, and hard-contact depth. Whiff indicators alone are not enough if
    contact quality can collapse innings and leash.
```

---

## Patch Recommendations

```yaml
patches_added:
  - low_team_k_rate_hard_gate
  - runway_collapse_gate
  - conflict_profile_stake_cap
  - first_pitch_strike_risk_gate
  - arsenal_override_tier_separation

low_team_k_rate_hard_gate:
  action: add
  rule: >
    If opponent expected-nine K rate is below 16%, no pregame 6+ K investment is allowed unless the pitcher
    qualifies as an elite outlier with 35%+ projected CSW, 30%+ projected whiff/swing, clean command, and
    multiple elite whiff pitch families.

runway_collapse_gate:
  action: add
  rule: >
    K props of 6+ require not only whiff ability but inning runway stability. If opponent hard-contact profile
    and low-K contact depth can force early pitch stress or damage, downgrade by at least one full K tier.

conflict_profile_stake_cap:
  action: add
  rule: >
    Any play with a negative opponent team K rate signal but positive pitcher K-split signal is a conflict profile.
    Conflict-profile K props are capped at micro stake during drawdowns.

first_pitch_strike_risk_gate:
  action: add
  rule: >
    If the pitcher has command/runway volatility and the opponent punishes contact, require stronger first-pitch
    strike stability before approving pregame K overs.

arsenal_override_tier_separation:
  action: strengthen
  rule: >
    Do not treat all arsenal overrides equally. Misiorowski-type elite outliers may override high LRS. Ordinary
    strong K arms like Harrison cannot override an opponent team K rate near 14% without elite current whiff context.
```

---

## Threshold Lesson

```yaml
threshold_lesson:
  market: 6_plus_strikeouts
  result_type: full_threshold_miss
  failed_by: 3_strikeouts
  failure_type: runway_collapse_contact_damage
  pitcher_whiff_read: partially_confirmed
  pitcher_command_read: failed
  leash_read: failed
  opponent_lrs: underestimated
  market_selection: right_price_shape_wrong_clearance
  future_rule: >
    A plus-money 6+ is not playable simply because the pitcher has strong K splits. Against a sub-16% K opponent,
    the pitcher must be an elite outlier or the play must be moved to LiveFlow only.
```

---

## Edge Review

```yaml
edge_review:
  current_pitcher_k_status: degraded
  psychological_note: >
    The discouragement is justified. The recent K-market results show repeated overconfidence in pregame projections.
    This does not mean the entire betting project has failed, but it does mean the pregame pitcher K module is not
    currently trustworthy enough for standard exposure.
  technical_diagnosis: >
    The model has been too willing to approve B+/A- K positions when one part of the profile clears while another
    major component fails. Recent losses are not random. They are clustered around opponent contact resistance,
    runway collapse, and over-aggressive arsenal overrides.
  operational_response: >
    Freeze standard pregame pitcher K bets immediately. Move pitcher K to paper-trade, micro-only, or LiveFlow-only
    until a new backtest proves the repaired gates. Capital should shift toward F5 structures and live totals where
    the recent reads have been cleaner.
```

---

## Final Classification

```yaml
postmortem_classification:
  signal: negative
  official_bet: true
  failure_type: runway_collapse_contact_damage
  sub_type: low_team_k_rate_override_failure
  command_read: failed
  leash_read: failed
  whiff_read: partial_pass
  csw_read: marginal_pass
  opponent_lrs: underestimated
  market_selection: right_market_shape_wrong_play
  stake_assessment: too_high_for_drawdown_conflict_profile
  bankroll_result: loss
  pnl: -10.00
  final_status: freeze_standard_pregame_k
```

---

## Model State After Loss

```yaml
active_model_changes:
  freeze:
    standard_pregame_pitcher_k: true
  restrict:
    pregame_pitcher_k:
      allowed_only_if:
        - elite_outlier_k_threshold_exception
        - opponent_expected_nine_k_rate_above_21_percent
        - lrs_below_5_2
        - projected_whiff_swing_above_28_percent
        - projected_csw_above_30_percent
        - leash_stability_confirmed
      otherwise: LiveFlow_only_or_no_bet
  add_patches:
    - low_team_k_rate_hard_gate
    - runway_collapse_gate
    - conflict_profile_stake_cap
    - first_pitch_strike_risk_gate
    - arsenal_override_tier_separation
```

---

## Tags

`LOSS` `KYLE_HARRISON` `WILLIAM_HILL` `6_PLUS_KS` `RUNWAY_COLLAPSE` `LOW_K_OPPONENT` `ARIZONA_LRS_UPGRADE` `CONTACT_DAMAGE` `ARSENAL_OVERRIDE_FAILURE` `FREEZE_PREGAME_K` `MODEL_MODIFY`
