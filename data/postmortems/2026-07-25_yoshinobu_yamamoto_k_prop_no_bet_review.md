# SharpEdge MLB K Prop Review — 2026-07-25

## Position Summary
**Date:** 2026-07-25  
**Game:** Los Angeles Dodgers at New York Mets  
**Pitcher:** Yoshinobu Yamamoto  
**Pregame market reviewed:** 7+ strikeouts at +102  
**Investment:** None  
**Final strikeouts:** 5  
**Classification:** Correct no-bet / rejected candidate

```yaml
review:
  date: 2026-07-25
  sport: MLB
  pitcher: Yoshinobu Yamamoto
  team: Los Angeles Dodgers
  opponent: New York Mets
  market_reviewed: 7_plus_strikeouts
  price: +102
  stake: 0.00
  result_strikeouts: 5
  outcome: no_bet_correct
```

## Pregame Model Snapshot
The pregame board showed:
- 6+ at -205
- 7+ at +102
- 8+ at +183

The initial projection placed 7+ around 43–47%, while +102 required about 49.5% to break even. The market therefore offered no clean edge, and the official command was to sharpen the confirmed lineup rather than lock the wager.

## Final Pitching Line
| IP | H | R | ER | BB | K | HR | Pitches-Strikes | Batters Faced |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 6.0 | 5 | 1 | 1 | 3 | 5 | 0 | 100-65 | 26 |

## Core Performance Metrics
| Metric | Final |
|---|---:|
| Strike rate | 65% |
| CSW | 26% |
| Whiff/swing | 25% |
| Zone rate | 46% |
| Chase rate | 31% |
| First-pitch strike | 54% |
| Average EV allowed | 83.1 mph |
| Hard-hit balls | 4 |
| Maximum EV | 107.4 mph |

## Pitch Mix
| Pitch | Usage | Ks | Swings | Called Strikes | Whiffs | CSW by pitch |
|---|---:|---:|---:|---:|---:|---:|
| Splitter | 28% / 28 | 4 | 19 | 0 | 8 | 29% |
| Four-seam fastball | 26% / 26 | 0 | 10 | 3 | 4 | 27% |
| Cutter | 16% / 16 | 0 | 10 | 4 | 0 | 25% |
| Curveball | 13% / 13 | 1 | 5 | 6 | 1 | 54% |
| Sinker | 11% / 11 | 0 | 6 | 0 | 0 | 0% |
| Slider | 6% / 6 | 0 | 2 | 0 | 0 | 0% |

## What Happened
Yamamoto pitched well enough to suppress runs, but the strikeout conversion did not support the 7+ threshold.

Key points:
- He reached 100 pitches in six innings, limiting additional runway.
- The splitter generated four of his five strikeouts and carried most of the bat-missing burden.
- The fastball, cutter, sinker and slider combined for zero strikeouts.
- Overall whiff/swing finished at 25%, just below the preferred 26% floor for higher thresholds.
- CSW finished at 26%, also below the preferred 27% floor for 7+ approval.
- Three walks added pitch-count pressure and reduced the probability of a seventh inning.

## Model Diagnosis
### Confirmed
- The pregame price was not favorable enough for the projected hit rate.
- Yamamoto had stable command and contact suppression, but not enough strikeout conversion across the full arsenal.
- The 7+ threshold required more than strong run prevention; it required deeper inning runway and better multi-pitch K support.

### Important Distinction
This was not a failed investment. It was a correctly rejected candidate. The final result supports the decision not to chase 7+ at a near-even price.

## Model Patch Reinforcement
```yaml
yamamoto_review_patches:
  seven_plus_requires_dual_floor:
    preferred_csw: 27_percent_or_higher
    preferred_whiff_per_swing: 26_percent_or_higher
  multi_pitch_k_support_check:
    rule: Do not approve 7+ when one pitch carries most strikeout production.
  walk_pressure_runway_gate:
    rule: Elevated walks reduce seventh-inning probability even when run prevention is strong.
  price_discipline:
    rule: Near-even 7+ prices require a true probability edge above 52%, not a narrative lean.
```

## Threshold Lesson
A quality start does not automatically create a pitcher-K over. Yamamoto allowed only one run, but his strikeout total stopped at five because the profile was concentrated in one pitch and the pitch count reached 100 through six innings.

## Final Classification
**Classification:** Correct no-bet  
**Process grade:** A  
**Market lesson:** Passing a near-fair price is part of preserving edge  

## Tags
`no-bet` `pitcher-k` `yoshinobu-yamamoto` `mets` `price-discipline` `runway` `multi-pitch-support` `correct-pass`
