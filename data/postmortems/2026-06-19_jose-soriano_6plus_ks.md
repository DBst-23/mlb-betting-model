# MLB K Prop Postmortem — 2026-06-19

## Jose Soriano — 6+ Strikeouts

**Game:** Los Angeles Angels at Athletics  
**Market:** Jose Soriano 6+ pitching strikeouts  
**Book:** William Hill  
**Entry Odds:** +123  
**Stake:** 10.00  
**Paid:** 22.30  
**Profit:** +12.30  
**Final Result:** 6 strikeouts  
**Outcome:** WIN

---

## Pregame Projection

| Metric | Projection |
|---|---:|
| Mean | 5.9 K |
| Median | 6 K |
| Hit Probability | 51-54% |
| Market Implied Probability | 44.8% |
| Estimated Edge | +6.2 to +9.2 percentage points |
| LRS | 4.6 |
| Grade | A- |

**Pregame thesis:** Soriano 6+ was a plus-money median-threshold position. The model preferred the 6+ rung over the 5+ because the 6+ price offered better payout efficiency without overextending into a 7+ ceiling ladder.

---

## Final Pitching Line

| IP | H | R | ER | BB | K | HR | Pitches-Strikes | BF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5.0 | 6 | 4 | 4 | 4 | 6 | 1 | 105-62 | 24 |

---

## Core Metrics

| Metric | Result |
|---|---:|
| Total Pitches | 105 |
| Swings | 44 |
| Called Strikes | 18 |
| Whiffs | 17 |
| CSW | 33% |
| Whiff / Swing | 39% |
| Strike Rate | 59% |
| Zone Rate | 41% |
| Chase Rate | 27% |
| First-Pitch Strike | 56% |
| Pitches / Inning | 21.0 |
| Pitches / Batter | 4.38 |

---

## Pitch Mix

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CStr+Whiff |
|---|---:|---:|---:|---:|---:|---:|---:|
| 4-Seam Fastball | 32% / 34 | 97.0 | 3 | 16 | 8 | 8 | 47% |
| Sinker | 23% / 24 | 96.5 | 2 | 9 | 5 | 1 | 25% |
| Knuckle Curve | 22% / 23 | 85.2 | 1 | 11 | 4 | 5 | 39% |
| Splitter | 16% / 17 | 92.3 | 0 | 7 | 1 | 2 | 18% |
| Slider | 7% / 7 | 91.1 | 0 | 1 | 0 | 1 | 14% |
| All | 100% / 105 | 93.1 | 6 | 44 | 18 | 17 | 33% |

---

## What Worked

1. **Four-seam fastball carried the strikeout profile.** Soriano generated 3 of his 6 strikeouts with the four-seamer, with 8 called strikes and 8 whiffs.
2. **Curveball supported the whiff floor.** The knuckle curve produced 5 whiffs and a 39% CStr+Whiff rate.
3. **LRS read was validated.** The Athletics lineup provided enough strikeout leakage for the 6+ median-threshold target to clear.

---

## What Almost Broke the Position

1. **Walk volatility:** 4 walks created runway risk.
2. **Pitch efficiency drag:** 105 pitches in only 5.0 innings created early-hook pressure.
3. **Run prevention instability:** 4 earned runs and 1 HR added volatility, even though the strikeout stuff held.

---

## Model Grade

| Category | Grade |
|---|---:|
| Result | A |
| Projection Quality | A- |
| Entry Execution | A |
| Market Timing | B+ |
| Leash Stability | B- |
| Pitch Efficiency | C- |
| CSW | A |
| Whiff Sustainability | A |
| Contact Suppression | B |
| LRS Accuracy | A- |
| Final Grade | A- |

---

## Model Lessons

- The model correctly identified a plus-money soft-threshold opportunity.
- The 6+ rung was the correct target; 7+ would have been too aggressive pregame.
- Walk-prone arms need a larger Pitch Efficiency Index penalty before ladder exposure.
- Soriano-type profiles are playable at median thresholds when CSW and opponent LRS align, but should not be blindly laddered without LiveFlow confirmation.

---

## Tags

`WIN` `WILLIAM_HILL_EXECUTION_LAYER` `PLUS_MONEY_SOFT_THRESHOLD` `EXACT_THRESHOLD_HIT` `CSW_CONFIRMED` `WHIFF_CONFIRMED` `PITCH_EFFICIENCY_DRAG` `WALK_VOLATILITY_WARNING` `DO_NOT_BLIND_LADDER`
