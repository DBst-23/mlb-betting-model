# SharpEdge Postmortem — Zack Wheeler 7+ Ks Win

**Date:** 2026-06-15  
**Game:** Miami vs Philadelphia  
**Market:** Zack Wheeler 7+ strikeouts  
**Book:** Kalshi  
**Stake:** $9.00  
**Entry Odds:** +123  
**Result:** Win  
**Payout:** $20.12  
**Profit:** +$11.12  
**ROI:** +123.64%

---

## Final Line

| Pitcher | IP | H | R | ER | BB | K | HR | ERA |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Zack Wheeler | 6.0 | 2 | 0 | 0 | 3 | 9 | 0 | 0.00 |

**Pitches-Strikes:** 97-59  
**Groundouts-Flyouts:** 5-3  
**Batters Faced:** 23

---

## Ticket Outcome

| Market | Stake | Odds | Needed | Actual | Outcome | Profit |
|---|---:|---:|---:|---:|---|---:|
| Wheeler 7+ Ks | $9.00 | +123 | 7 | 9 | Win | +$11.12 |

---

## Pregame Thesis

This was tagged as the cleanest late-wave strikeout edge on the board because Wheeler combined:

- stable leash profile
- strong opponent K path versus Miami
- command floor
- plus-money price at a median-friendly threshold
- clean runway to 95+ pitches if efficient enough

Pregame model read:

```yaml
zack_wheeler_7_plus_pregame:
  projected_mean_ks: 7.2
  projected_median_ks: 7
  implied_probability_at_plus_123: 44.8%
  model_probability: 58-62%
  projected_edge: +13_to_17_percentage_points
  grade: A-
  status: PRIMARY_INVESTMENT
```

---

## Pitch Mix / Results

| Pitch | Usage | Avg Velo | K | Swings | Called Strikes | Whiffs | CSW |
|---|---:|---:|---:|---:|---:|---:|---:|
| 4-Seam | 32% (31) | 96.0 | 3 | 11 | 9 | 2 | 35% |
| Splitter | 19% (18) | 87.7 | 2 | 10 | 0 | 6 | 33% |
| Sinker | 15% (15) | 95.2 | 2 | 6 | 5 | 1 | 40% |
| Cutter | 15% (15) | 91.0 | 2 | 7 | 4 | 3 | 47% |
| Curveball | 9% (9) | 79.7 | 0 | 1 | 2 | 0 | 22% |
| Sweeper | 9% (9) | 81.4 | 0 | 2 | 2 | 0 | 22% |
| **All** | **97 pitches** | **90.7** | **9** | **37** | **22** | **12** | **35%** |

---

## Contact / Discipline Notes

| Metric | Result |
|---|---:|
| Batted Balls | 11 |
| Hits Allowed | 2 |
| Hard-Hit BBE | 3 |
| Avg EV Allowed | 87.8 mph |
| Zone% | 49% |
| Chase% | 20% |
| Strike% | 61% |
| First-Pitch Strike% | 65% |
| CSW | 35% |
| Whiffs | 12 |

---

## Why It Won

The ticket won because Wheeler did not need extreme chase dependency. He won through layered strike generation:

1. **Fastball called-strike foundation** — 9 called strikes on the 4-seam, 35% CSW.
2. **Splitter conversion weapon** — 6 whiffs on 10 swings, 60% whiff per swing.
3. **Cutter/sinker support** — 4 combined strikeouts from secondary hard stuff.
4. **Low contact damage** — only 2 hits and 87.8 mph average EV allowed.
5. **Leash held** — 97 pitches, 6.0 IP, enough runway for 9 Ks.

This validated the pregame model’s core edge: strong pitcher quality plus opponent K path plus an underpriced 7+ threshold.

---

## SharpEdge Model Lessons

### Validated

```yaml
validated_rules:
  - premium_arm_plus_money_7_plus_is_actionable_when_mean_ge_7
  - stable_leash_can_outweigh_moderate_walk_drag
  - high_csw_profile_supports_ceiling_without_needing_extreme_chase
  - multi_pitch_k_distribution_reduces single_pitch_failure_risk
```

### Add to DBst-23

```yaml
rule_patch_2026_06_15:
  name: "Multi-Pitch Conversion Confirmation"
  trigger:
    pregame:
      - pitcher_mean_ks >= 7.0
      - median_ks >= 7
      - market_7_plus_price >= +100
      - opponent_lrs <= 4.5
    live:
      - csw >= 30%
      - whiffs >= 8 by 5 IP
      - pitch_count_runway >= 90
  action:
    - classify_as_PRIMARY_INVESTMENT
    - allow_standard_to_strong_stake
    - do_not_require_ladder_unless_8_plus_price_remains_plus_150_or_better
```

---

## Final Grade

| Category | Grade |
|---|---|
| Pregame Read | A |
| Price Capture | A |
| Leash Projection | A |
| Matchup Read | A- |
| Execution | A |
| Result Quality | A |

**Final SharpEdge Grade:** A

---

## Summary

Wheeler 7+ at +123 was a clean edge and cashed comfortably with 9 strikeouts. The position matched the model profile almost perfectly: median threshold, plus-money, stable leash, strong CSW, and multi-pitch strikeout distribution. This is a template win for DBst-23 strikeout edge hunting.
