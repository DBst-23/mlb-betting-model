# SharpEdge MLB K Prop Postmortem — 2026-06-25

## Position Summary

**Date:** 2026-06-25  
**Book:** William Hill  
**Game:** Chicago Cubs at New York Mets  
**Pitcher:** Freddy Peralta  
**Market:** Total Pitching Strikeouts  

| Target | Entry Odds | Stake | To Win | Paid | Profit/Loss | Final Ks | Outcome |
|---|---:|---:|---:|---:|---:|---:|---|
| Over 5.5 Ks / 6+ | +106 | $10.00 | $10.60 | $0.00 | -$10.00 | 5 | LOSS |

**Total Risk:** $10.00  
**Total Paid:** $0.00  
**Net Profit/Loss:** -$10.00  
**Final Strikeouts:** 5  
**Portfolio Outcome:** 0-1

---

## Pregame Model Snapshot

| Metric | Projection |
|---|---:|
| Mean | 5.7 Ks |
| Median | 6 Ks |
| Hit Probability: 6+ | 48-52% |
| Market Implied Probability | 48.5% |
| Edge | Thin positive / fair-plus |
| Grade | B |

```yaml
position:
  date: 2026-06-25
  sport: MLB
  market_type: pitcher_strikeouts
  pitcher: Freddy Peralta
  team: New York Mets
  opponent: Chicago Cubs
  book: William Hill
  target: over_5_5_strikeouts
  equivalent_ladder: 6_plus_strikeouts
  odds: 106
  stake: 10.00
  to_win: 10.60
  paid: 0.00
  profit: -10.00
  result_strikeouts: 5
  outcome: LOSS
```

---

## Final Pitching Line

| IP | H | R | ER | BB | K | HR | ERA | Pitches-Strikes | BF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5.2 | 5 | 3 | 0 | 1 | 5 | 0 | 0.00 | 98-54 | 24 |

**Wild Pitch:** Freddy Peralta

---

## Core Performance Metrics

| Metric | Result |
|---|---:|
| Total Pitches | 98 |
| Strikes | 54 |
| Strike Rate | 55% |
| Batters Faced | 24 |
| Swings | 43 |
| Called Strikes | 11 |
| Whiffs | 8 |
| CStr+Whiff | 19 / 98 |
| CSW | 19% |
| Whiff / Swing | 19% |
| Zone Rate | 37% |
| Chase Rate | 26% |
| First-Pitch Strike | 54% |
| Average EV Allowed | 87.0 mph |
| Hard-Hit BBE | 4 |
| Top EV Marker | 102.3 |
| Velo Marker | 97.8 |

---

## Pitch Mix

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CStr+Whiff |
|---|---:|---:|---:|---:|---:|---:|---:|
| 4-Seam Fastball | 49% / 48 | 95.2 | 2 | 22 | 5 | 3 | 17% |
| Changeup | 21% / 21 | 87.9 | 2 | 11 | 2 | 1 | 14% |
| Curveball | 12% / 12 | 79.7 | 0 | 6 | 2 | 3 | 42% |
| Sweeper | 10% / 10 | 82.3 | 0 | 3 | 2 | 0 | 20% |
| Slider | 5% / 5 | 83.5 | 0 | 0 | 0 | 0 | 0% |
| Slow Curve | 2% / 2 | 74.5 | 1 | 1 | 0 | 1 | 50% |
| All | 100% / 98 | 89.4 | 5 | 43 | 11 | 8 | 19% |

---

## What Happened

Peralta finished with 5 strikeouts and lost the Over 5.5 / 6+ ticket by one strikeout. Unlike the Bryan Woo loss, the runway was mostly present: 5.2 innings, 98 pitches, and 24 batters faced gave the position enough volume to threaten the cash. The miss came from weak strikeout efficiency and poor swing-and-miss conversion.

The run prevention was actually strong on the surface: 3 runs allowed but 0 earned runs, only 1 walk, no homers, and 4 hard-hit batted balls. The issue was that the Cubs did not chase enough, Peralta did not generate enough whiffs, and the strike rate sat at only 55%.

---

## Model Diagnosis

### Confirmed

1. **Runway was acceptable.** 98 pitches and 24 batters faced gave the ticket enough opportunity.
2. **Contact suppression was acceptable.** 87.0 mph average EV and 4 hard-hit BBE did not collapse the outing.
3. **Plus-money entry was disciplined.** At +106, the model did not overpay. This was a thin-edge position sized as a single primary, not a ladder stack.

### Missed / Weakened

1. **CSW projection was too high.** Actual CSW was only 19%.
2. **Whiff sustainability failed.** 8 whiffs on 43 swings equals 19% whiff/swing, below what a 6+ ticket needed.
3. **Cubs LRS should remain elevated.** The Cubs extended enough plate appearances and suppressed the K conversion despite not doing major earned damage.
4. **Fastball-heavy path was not enough.** 49% four-seam usage produced only 2 Ks and a 17% CStr+Whiff rate.
5. **Secondary K pitch support was inconsistent.** The curveball showed strong CSW, but it was only used 12 times and produced no Ks.

---

## Cubs LRS Update

```yaml
lineup_resistance_update:
  opponent: Chicago Cubs
  archetype: power_rhp_k_arms
  current_signal:
    - Freddy Peralta 2026-06-25: 5.2 IP, 5 K, O5.5 loss
  adjustment:
    cubs_lrs_vs_rhp_k_arms: maintain_elevated
    cubs_contact_resistance_modifier: increase_slightly
    cubs_chase_suppression_modifier: increase
  reason: >
    Cubs kept Peralta to 19% CSW and 19% whiff/swing while allowing enough runway.
    This profile signals strikeout conversion resistance rather than pure damage risk.
```

---

## Patch Recommendation

```yaml
patch_recommendation:
  name: thin_edge_plus_money_single_only
  action: keep
  description: >
    When model probability is near market implied and edge is classified as thin positive,
    use only one primary position and do not ladder. This execution was correct even though
    the result lost.
  status: confirmed
```

```yaml
patch_recommendation_2:
  name: csw_floor_gate_for_6plus
  action: add
  description: >
    Before approving a 6+ strikeout position, require recent and matchup-adjusted CSW
    support above threshold. If opponent has chase suppression/contact resistance, reduce
    6+ hit probability unless the pitcher has multiple active whiff pitch families.
  threshold:
    preferred_csw_floor: 27_percent
    caution_zone: 23_to_26_percent
    downgrade_zone: below_23_percent
```

---

## Threshold Lesson

This was a classic **one-K threshold loss**. The bet was not structurally reckless because the entry was plus-money and the ladder was avoided. The issue was that a median-6 projection does not have much margin when the actual CSW collapses below 20%.

```yaml
threshold_lesson:
  result_type: one_k_miss
  failed_target: over_5_5
  classification: whiff_conversion_failure
  runway_read: mostly_confirmed
  contact_suppression_read: confirmed
  csw_read: failed
  market_selection: acceptable
  future_rule: >
    For thin-edge 6+ positions, require a stronger CSW floor or reduce stake sizing when
    opponent LRS is elevated by chase suppression and contact resistance.
```

---

## Final Classification

```yaml
postmortem_classification:
  signal: mixed
  failure_type: whiff_conversion_failure
  leash_read: confirmed
  contact_suppression_read: confirmed
  csw_read: failed
  opponent_lrs: slightly_underestimated
  market_selection: acceptable
  ladder_exposure: none
  result: loss
  record: 0-1
  pnl: -10.00
  confidence_after_review: medium
  final_status: modify_projection_thresholds_not_execution
```

---

## Tags

`LOSS` `FREDDY_PERALTA` `WILLIAM_HILL` `OVER_5_5_KS` `6_PLUS_KS` `ONE_K_MISS` `WHIFF_CONVERSION_FAILURE` `CSW_FLOOR_GATE` `CUBS_LRS_ELEVATED` `THIN_EDGE_SINGLE_ONLY` `MODEL_MODIFY`
