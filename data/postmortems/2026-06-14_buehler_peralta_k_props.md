# MLB K Prop Postmortem — 2026-06-14

## Card Summary

| Pitcher | Market | Stake | Odds | Result | Payout | Profit/Loss |
|---|---:|---:|---:|---|---:|---:|
| Walker Buehler | 5+ strikeouts | $3.50 | +158 | WIN | $9.05 | +$5.55 |
| Freddy Peralta | 6+ strikeouts | $5.94 | +105 | LOSS | $0.00 | -$5.94 |

**Net card result:** -$0.39  
**Card read:** Correct value structure on Buehler soft threshold; Peralta projection overestimated strikeout conversion despite acceptable run prevention and leash.

---

## Walker Buehler — WIN

**Game:** San Diego vs Baltimore  
**Ticket:** Yes — Walker Buehler 5+ strikeouts  
**Entry:** $3.50 at +158  
**Payout:** $9.05  
**Result:** Hit, 5 strikeouts

### Final Line

| IP | H | R | ER | BB | K | HR | ERA |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 5.0 | 6 | 1 | 1 | 0 | 5 | 1 | 1.80 |

**Pitches-strikes:** 86-60  
**Groundouts-flyouts:** 5-3  
**Batters faced:** 21

### Pitch Metrics

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CSW |
|---|---:|---:|---:|---:|---:|---:|---:|
| 4-Seam Fastball | 24% (21) | 94.6 | 1 | 10 | 3 | 1 | 19% |
| Cutter | 22% (19) | 91.0 | 2 | 9 | 6 | 2 | 42% |
| Slider | 17% (15) | 87.9 | 1 | 10 | 1 | 4 | 33% |
| Sinker | 12% (10) | 95.1 | 0 | 7 | 1 | 0 | 10% |
| Sweeper | 9% (8) | 82.6 | 0 | 4 | 2 | 1 | 38% |
| Knuckle Curve | 9% (8) | 81.4 | 1 | 5 | 0 | 1 | 13% |
| Changeup | 6% (5) | 90.0 | 0 | 1 | 1 | 1 | 40% |
| **ALL** | **86 pitches** | **90.1** | **5** | **46** | **14** | **10** | **28%** |

### Contact / Discipline

| Metric | Value |
|---|---:|
| BBE | 16 |
| Hits | 6 |
| Hard-hit | 9 |
| Avg EV allowed | 92.0 mph |
| Zone% | 57% |
| zSwing% | 71% |
| Chase% | 30% |
| Strike% | 70% |
| 1PStr% | 81% |

### Postmortem Read

Buehler won because the soft **5+ threshold** gave him enough runway despite imperfect contact suppression. The pregame refinement correctly identified Baltimore as a lineup with hard-contact and lefty OBP pressure, which capped ceiling but did not kill the 5+ path.

Key positives:

- 0 walks protected leash.
- 81% first-pitch strike rate created count leverage.
- Cutter and slider carried the K conversion: 13 combined CSW on 34 pitches.
- He reached exactly 5.0 IP and exactly 5 K, validating the median projection.

Key risk that showed up:

- 9 hard-hit balls and 92.0 mph average EV confirmed Baltimore contact danger.
- The ticket was threshold-sensitive, not ceiling-rich.

### Model Lesson

This was a strong example of **soft-threshold value beating raw ceiling uncertainty**. Even with a difficult contact environment, +158 on 5+ gave enough margin because the market priced Buehler closer to a low-leash 4-K arm than a median 5-K arm.

```yaml
walker_buehler_2026_06_14:
  market: "5+ strikeouts"
  entry_odds: +158
  stake: 3.50
  result: WIN
  final_ks: 5
  final_ip: 5.0
  pitch_count: 86
  strikes: 60
  batters_faced: 21
  csw_rate: 0.28
  whiffs: 10
  chase_rate: 0.30
  first_pitch_strike_rate: 0.81
  avg_ev_allowed: 92.0
  hard_hit_allowed: 9
  model_tag:
    - SOFT_THRESHOLD_VALUE
    - MEDIAN_HIT
    - CONTACT_RISK_PRESENT
    - ZERO_WALK_LEASH_SUPPORT
    - CUTTER_SLIDER_CONVERSION
```

---

## Freddy Peralta — LOSS

**Game:** Atlanta vs New York Mets  
**Ticket:** Yes — Freddy Peralta 6+ strikeouts  
**Entry:** $5.94 at +105  
**Payout:** $0.00  
**Result:** Missed, 2 strikeouts

### Final Line

| IP | H | R | ER | BB | K | HR | ERA |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 5.0 | 4 | 1 | 1 | 1 | 2 | 0 | 1.80 |

**Pitches-strikes:** 90-55  
**Groundouts-flyouts:** 7-1  
**Batters faced:** 20

### Pitch Metrics

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CSW |
|---|---:|---:|---:|---:|---:|---:|---:|
| 4-Seam Fastball | 40% (36) | 95.0 | 1 | 18 | 7 | 2 | 25% |
| Curveball | 23% (21) | 80.4 | 1 | 8 | 2 | 2 | 19% |
| Changeup | 17% (15) | 87.5 | 0 | 8 | 0 | 1 | 7% |
| Slider | 10% (9) | 82.3 | 0 | 3 | 1 | 1 | 22% |
| Sweeper | 9% (8) | 81.8 | 0 | 7 | 1 | 0 | 13% |
| Slow Curve | 1% (1) | 76.3 | 0 | 0 | 0 | 0 | 0% |
| **ALL** | **90 pitches** | **87.7** | **2** | **44** | **11** | **6** | **19%** |

### Contact / Discipline

| Metric | Value |
|---|---:|
| BBE | 17 |
| Hits | 4 |
| Hard-hit | 4 |
| Avg EV allowed | 80.4 mph |
| Zone% | 49% |
| zSwing% | 73% |
| Chase% | 26% |
| Strike% | 61% |
| 1PStr% | 50% |

### Postmortem Read

Peralta prevented runs, but the K profile never activated. The loss was not from damage; it was from **whiff failure and conversion failure**.

Main failure points:

- Only 6 whiffs on 44 swings.
- Overall CSW only 19%.
- Changeup was a major miss: 15 pitches, 1 whiff, 7% CSW.
- Sweeper generated zero whiffs despite 7 swings.
- 50% first-pitch strike rate limited count leverage.
- He created weak contact, but weak contact is bad for K overs when the threshold is 6+.

The pitch count was not terrible, but at 90 pitches through 5 IP with only 2 K, the ticket was dead by conversion, not leash.

### Model Lesson

This is a clean warning flag for future Peralta overs: do not upgrade him solely from velocity or run-prevention context. He needs actual early whiff confirmation, especially from changeup/slider/sweeper. When offspeed CSW is below 20%, his K ceiling can collapse even in a quality start.

```yaml
freddy_peralta_2026_06_14:
  market: "6+ strikeouts"
  entry_odds: +105
  stake: 5.94
  result: LOSS
  final_ks: 2
  final_ip: 5.0
  pitch_count: 90
  strikes: 55
  batters_faced: 20
  csw_rate: 0.19
  whiffs: 6
  chase_rate: 0.26
  first_pitch_strike_rate: 0.50
  avg_ev_allowed: 80.4
  hard_hit_allowed: 4
  model_tag:
    - WHIFF_FAILURE
    - CONVERSION_FAILURE
    - WEAK_CONTACT_NOT_K_FRIENDLY
    - CHANGEUP_CSW_COLLAPSE
    - PRE_GAME_OVERCONFIDENCE
    - LIVEFLOW_RED_CONFIRMED
```

---

## Card-Level Takeaways

1. **Buehler was the better structure:** lower threshold, plus-money payout, median hit condition.
2. **Peralta was the higher-friction structure:** needed 6+ while showing early pitch-count and CSW drag.
3. **Weak contact can hurt K overs:** Peralta generated soft contact, but that reduced K opportunity.
4. **First-pitch strike rate remains critical:** Buehler 81% vs Peralta 50% was the clearest control/leverage separator.
5. **New rule:** do not anchor a 6+ K ticket without either strong projected CSW or confirmed early whiff support.

## DBst-23 Rule Patch

```yaml
rule_patch_2026_06_14:
  name: "Soft Threshold vs Conversion Risk"
  applies_to: "MLB pitcher strikeout props"
  rule:
    - Prefer 5+ plus-money soft thresholds over 6+ thresholds when opponent has contact resistance.
    - Downgrade pitchers with projected weak-contact paths if whiff profile is unstable.
    - Require 28%+ live CSW or 4+ whiffs by end of 2 IP to maintain confidence on 6+ tickets.
    - If early CSW is under 22% and whiffs are under 3 through 3 IP, mark ticket as LIVEFLOW_RED.
  observed_examples:
    - "Buehler 5+ at +158 hit despite contact risk because threshold was soft."
    - "Peralta 6+ at +105 failed because whiff conversion collapsed despite run prevention."
```
