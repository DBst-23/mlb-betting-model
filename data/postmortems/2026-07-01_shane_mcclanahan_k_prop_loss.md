# SharpEdge MLB K Prop Postmortem — 2026-07-01

## Position Summary

**Date:** 2026-07-01  
**Book:** William Hill  
**Game:** Tampa Bay Rays at Kansas City Royals  
**Pitcher:** Shane McClanahan  
**Market:** Pitching Strikeouts  

| Target | Entry Odds | Stake | To Win | Paid | Profit/Loss | Final Ks | Outcome |
|---|---:|---:|---:|---:|---:|---:|---|
| 5+ Strikeouts | -102 | $7.50 | $7.35 | $0.00 | -$7.50 | 4 | LOSS |

```yaml
position:
  date: 2026-07-01
  sport: MLB
  market_type: pitcher_strikeouts
  pitcher: Shane McClanahan
  team: Tampa Bay Rays
  opponent: Kansas City Royals
  book: William Hill
  target: 5_plus_strikeouts
  odds: -102
  stake: 7.50
  to_win: 7.35
  paid: 0.00
  profit: -7.50
  result_strikeouts: 4
  outcome: LOSS
```

---

## Pregame Model Snapshot

McClanahan was selected as the cleanest K investment from the 07-01 slate after Skenes and Wheeler were priced into inflated ceiling markets.

| Metric | Projection |
|---|---:|
| Refined Mean | 5.4 Ks |
| Median | 5 Ks |
| 5+ Hit Probability | 61-65% |
| Market Implied Probability at -102 | 50.5% |
| Estimated Edge | +10.5 to +14.5 pts |
| Kansas City LRS | 5.4 |
| Grade | B+ / A- price-adjusted |

---

## Final Pitching Line

| IP | H | R | ER | BB | K | HR | ERA | Pitches-Strikes | BF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6.0 | 3 | 0 | 0 | 0 | 4 | 0 | 0.00 | 69-49 | 20 |

---

## Core Performance Metrics

| Metric | Result |
|---|---:|
| Total Pitches | 69 |
| Strikes | 49 |
| Strike Rate | 71% |
| Batters Faced | 20 |
| Swings | 33 |
| Called Strikes | 15 |
| Whiffs | 7 |
| CStr+Whiff | 22 / 69 |
| CSW | 32% |
| Whiff / Swing | 21% |
| Zone Rate | 55% |
| Chase Rate | 32% |
| First-Pitch Strike | 80% |
| BBE | 16 |
| Hits Allowed | 3 |
| Hard-Hit BBE | 7 |
| Average EV Allowed | 87.1 mph |
| Top EV Marker | 108.3 mph |
| Velo Marker | 98.2 mph |

---

## Pitch Mix

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CStr+Whiff |
|---|---:|---:|---:|---:|---:|---:|---:|
| Changeup | 41% / 28 | 87.2 | 1 | 16 | 2 | 4 | 21% |
| 4-Seam Fastball | 28% / 19 | 95.9 | 2 | 7 | 7 | 0 | 37% |
| Slider | 19% / 13 | 88.4 | 1 | 8 | 1 | 3 | 31% |
| Curveball | 13% / 9 | 82.8 | 0 | 2 | 5 | 0 | 56% |
| All | 100% / 69 | 89.3 | 4 | 33 | 15 | 7 | 32% |

---

## What Happened

McClanahan pitched extremely well in real baseball terms: 6.0 scoreless innings, 3 hits, 0 walks, 71% strikes, 80% first-pitch strikes, and a strong 32% CSW. The ticket still lost by one strikeout because Kansas City's low-K contact profile converted too many plate appearances into balls in play instead of strikeouts.

This was not a command failure. It was not a leash failure. It was not a run-prevention failure. This was a strikeout-conversion miss against a lineup whose low-K pockets were correctly identified but still not penalized enough.

The most important clue is the final pitch count: only 69 pitches through 6 innings. McClanahan was efficient, but that efficiency came partly from KC putting balls in play early. Efficiency helped real pitching value but reduced extra strikeout chances.

---

## Model Diagnosis

### Confirmed

1. **Command was elite.** 71% strikes, 80% first-pitch strike, 0 walks.
2. **Leash was fine.** He reached 6.0 innings.
3. **Run prevention was excellent.** 0 ER, 3 hits, 0 HR.
4. **CSW cleared.** 32% CSW was well above the preferred floor.
5. **Market selection was better than the ceiling ladders.** We avoided Skenes/Wheeler inflated markets and avoided McClanahan 6+.

### Missed / Weakened

1. **Whiff/swing was only 21%.** This was below the preferred 23-25% threshold for a standard K investment.
2. **Kansas City low-K contact pockets were underweighted.** Bobby Witt Jr., Vinnie Pasquantino, Nick Loftin, Michael Massey, Maikel Garcia, and Isaac Collins created a contact floor.
3. **5+ probability was overstated.** The refined 61-65% was too aggressive given KC's 19.7% recent K rate vs LHP.
4. **Efficiency reduced K runway.** Only 69 pitches through 6 innings left fewer total conversion opportunities.
5. **Hard contact was present despite run prevention.** 7 hard-hit BBE and a 108.3 top EV showed KC was not helpless.
6. **Stake size remained too high for an LRS 5.4 opponent.** A $7.50 stake was controlled, but not small enough during the K-prop drawdown.

---

## Kansas City LRS Update

```yaml
lineup_resistance_update:
  opponent: Kansas City Royals
  archetype: low_k_contact_vs_lhp
  current_signal:
    - Shane McClanahan 2026-07-01: 6.0 IP, 4 K, 0 BB, 32% CSW, 21% whiff_swing, 69 pitches
  adjustment:
    royals_lrs_vs_lhp: increase_by_0.4_to_0.7
    royals_contact_conversion_modifier: increase
    royals_low_k_pocket_weight: increase
    royals_walk_pressure_modifier: neutral
    royals_contact_damage_modifier: slight_increase
  reason: >
    Kansas City did not beat the K prop through walks or run damage. They beat it through
    contact conversion and efficient balls in play. McClanahan was sharp, but the lineup
    suppressed strikeout volume enough to hold him at 4 Ks over 6 scoreless innings.
```

---

## Patch Recommendations

```yaml
patches_added:
  - efficient_contact_k_suppression_gate
  - lrs_5_3_standard_stake_ban
  - whiff_swing_minimum_for_standard_k

 efficient_contact_k_suppression_gate:
  action: add
  rule: >
    Penalize K props when opponent has multiple low-K contact hitters and the pitcher's likely
    run-prevention path includes efficient early-count outs. Efficient innings can reduce K runway.

lrs_5_3_standard_stake_ban:
  action: strengthen
  rule: >
    When opponent LRS is 5.3 or higher, no standard stake is allowed unless projected whiff/swing,
    CSW, leash, and opponent chase weakness all clear. Price edge alone is not enough.

whiff_swing_minimum_for_standard_k:
  action: add
  rule: >
    For any 5+ K investment above micro stake, projected whiff/swing should clear 23-25%.
    CSW can be inflated by called strikes and should not substitute for true swing-and-miss.
```

---

## Threshold Lesson

This was a one-K miss, but it was more serious than a random one-K miss because the pitcher pitched well and still failed. When a starter throws 6 scoreless innings with 0 walks and 32% CSW but lands under the K line, the model must respect the opponent's contact profile more aggressively.

```yaml
threshold_lesson:
  result_type: one_k_miss
  failed_target: 5_plus
  classification: low_k_contact_conversion_failure
  command_read: confirmed
  leash_read: confirmed
  contact_suppression_read: confirmed_in_runs_but_not_k_conversion
  csw_read: passed
  whiff_read: borderline_failed
  opponent_lrs: underestimated
  market_selection: correct_market_wrong_stake
  future_rule: >
    Do not make 5+ K a controlled-standard stake against LRS 5.3+ opponents unless whiff/swing
    projection clears independently. Called strikes and leash are not enough against low-K contact lineups.
```

---

## Edge Review: Have We Lost Our Edge?

```yaml
edge_review:
  answer: not_lost_but_degraded_in_pitcher_k_markets
  diagnosis: >
    The edge has not disappeared entirely, but the pitcher K pregame model has become too optimistic
    in the current market environment. Books are pricing elite K arms aggressively, and our model has
    been overvaluing soft thresholds when opponent LRS is elevated.
  evidence:
    - multiple recent K losses despite reasonable price shopping
    - several losses came with good real pitching outcomes but failed K conversion
    - opponent low-chase and low-K pockets repeatedly suppressed props
    - market inflation has pushed elite pitchers into ceiling thresholds
  operational_response: >
    Reduce pregame K volume immediately. Shift more capital to F5 structures, NRFI/F5 under frameworks,
    and LiveFlow K entries where actual CSW, whiff/swing, and pitch count are confirmed.
```

---

## Final Classification

```yaml
postmortem_classification:
  signal: weakened
  failure_type: one_k_threshold_miss
  sub_type: low_k_contact_conversion_failure
  command_read: confirmed
  leash_read: confirmed
  contact_suppression_read: confirmed_but_non_decisive
  csw_read: passed
  whiff_read: borderline_failed
  opponent_lrs: underestimated
  market_selection: correct_threshold_but_overstaked
  ladder_exposure: none
  result: loss
  record: 0-1
  pnl: -7.50
  confidence_after_review: reduced
  final_status: reduce_pregame_k_exposure
```

---

## Model State After Loss

```yaml
active_new_patches:
  - efficient_contact_k_suppression_gate
  - lrs_5_3_standard_stake_ban
  - whiff_swing_minimum_for_standard_k

risk_review:
  recent_pattern: >
    The K portfolio is experiencing a negative cluster. The model is identifying pitchers who pitch well,
    but it is overestimating strikeout conversion against lineups with low-K contact pockets, OBP depth,
    or efficient ball-in-play profiles.
  immediate_operational_change: >
    Pregame K props move to micro/small only unless A-grade after full LRS sharpen. Any LRS 5.3+ opponent
    requires independent whiff/swing clearance before any stake above micro. F5 and LiveFlow frameworks
    receive priority until the K edge stabilizes.
```

---

## Tags

`LOSS` `SHANE_MCCLANAHAN` `WILLIAM_HILL` `5_PLUS_KS` `ONE_K_MISS` `LOW_K_CONTACT` `ROYALS_LRS_UPGRADE` `CSW_PASSED` `WHIFF_SWING_BORDERLINE` `EDGE_REVIEW` `MODEL_MODIFY`
