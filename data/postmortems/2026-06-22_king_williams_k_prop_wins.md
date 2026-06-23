# SharpEdge MLB K Prop Postmortem — 2026-06-22

## Portfolio Summary

**Slate:** 2026-06-22 MLB K Props  
**Book:** William Hill  
**Result:** 2-0  
**Total Cash Wagered:** $15.27  
**Total Paid:** $29.40  
**Total Profit:** +$14.13

| Pitcher | Market | Odds | Stake | Paid | Profit | Result |
|---|---:|---:|---:|---:|---:|---|
| Michael King | Over 4.5 Ks / 5+ | -128 | $10.00 | $17.81 | +$7.81 | WIN |
| Gavin Williams | 7+ Ks | +120 | $5.27 | $11.59 | +$6.32 | WIN |

---

# Michael King — Over 4.5 Strikeouts

**Game:** Atlanta Braves at San Diego Padres  
**Market:** Michael King Over 4.5 total pitching strikeouts  
**Equivalent Ladder:** 5+ strikeouts  
**Book:** William Hill  
**Entry Odds:** -128  
**Cash Wagered:** $10.00  
**Paid:** $17.81  
**Profit:** +$7.81  
**Final Result:** 5 strikeouts  
**Outcome:** WIN

## Pregame Projection Snapshot

| Metric | Projection |
|---|---:|
| Mean | 5.7 K |
| Median | 5 K |
| Hit Probability | 63-66% |
| Market Implied Probability | 56.1% |
| Estimated Edge | +6.9 to +9.9 percentage points |
| Grade | A- |

```yaml
position:
  date: 2026-06-22
  sport: MLB
  market_type: pitcher_strikeouts
  pitcher: Michael King
  team: San Diego Padres
  opponent: Atlanta Braves
  book: William Hill
  target: over_4_5_strikeouts
  equivalent_ladder: 5_plus_strikeouts
  entry_odds: -128
  stake_type: cash
  stake: 10.00
  paid: 17.81
  profit: 7.81
  result_strikeouts: 5
  outcome: WIN
```

## Final Pitching Line

| IP | H | R | ER | BB | K | HR | Pitches-Strikes | BF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 7.0 | 6 | 0 | 0 | 0 | 5 | 0 | 93-62 | 27 |

## Core Metrics

| Metric | Result |
|---|---:|
| Total Pitches | 93 |
| Average Pitch Velocity | 88.2 mph |
| Top-Level Velo Marker | 95.4 mph |
| Exit Velocity Marker | 110.3 |
| Swings | 45 |
| Called Strikes | 17 |
| Whiffs | 11 |
| CStr+Whiff | 28 / 93 |
| CSW | 30% |
| Whiff / Swing | 24% |
| Strike Rate | 67% |
| Zone Rate | 42% |
| Chase Rate | 43% |
| First-Pitch Strike | 63% |
| Average EV Allowed | 91.0 mph |

## Pitch Mix

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CStr+Whiff |
|---|---:|---:|---:|---:|---:|---:|---:|
| Sinker | 34% / 32 | 92.6 | 2 | 16 | 9 | 3 | 38% |
| Changeup | 24% / 22 | 86.1 | 3 | 11 | 2 | 5 | 32% |
| Sweeper | 18% / 17 | 80.8 | 0 | 4 | 5 | 1 | 35% |
| 4-Seam Fastball | 13% / 12 | 94.0 | 0 | 9 | 0 | 1 | 8% |
| Slider | 11% / 10 | 84.7 | 0 | 5 | 1 | 1 | 20% |
| All | 100% / 93 | 88.2 | 5 | 45 | 17 | 11 | 30% |

## What Worked

1. **Threshold selection was correct.** The model attacked 5+ / Over 4.5 and avoided 6+ ladder exposure.
2. **Runway stability carried the position.** King worked 7.0 full innings and faced 27 batters.
3. **Command profile was elite.** Zero walks against Atlanta preserved pitch efficiency and inning depth.
4. **Sinker/changeup pairing created the K path.** All five strikeouts came from the sinker and changeup.
5. **Chase profile validated.** King produced a 43% chase rate, which was crucial against a strong lineup.

## Risk Notes

- The ticket cashed exactly at 5 Ks.
- 6+ would have lost.
- Average EV allowed was elevated at 91.0 mph, so contact quality risk was real.
- Atlanta LRS was respected correctly by avoiding a ceiling ladder.

---

# Gavin Williams — 7+ Strikeouts

**Game:** Cleveland Guardians at Chicago White Sox  
**Market:** Gavin Williams 7+ pitching strikeouts  
**Book:** William Hill  
**Entry Odds:** +120  
**Cash Wagered:** $5.27  
**Paid:** $11.59  
**Profit:** +$6.32  
**Final Result:** 8 strikeouts  
**Outcome:** WIN

## Pregame Projection Snapshot

| Metric | Projection |
|---|---:|
| Mean | 6.6 K |
| Median | 6 K |
| Hit Probability | 47-51% for 7+ |
| Market Implied Probability | 45.5% |
| Estimated Edge | +1.5 to +5.5 percentage points |
| Grade | B+ ceiling |

```yaml
position:
  date: 2026-06-22
  sport: MLB
  market_type: pitcher_strikeouts
  pitcher: Gavin Williams
  team: Cleveland Guardians
  opponent: Chicago White Sox
  book: William Hill
  target: 7_plus_strikeouts
  entry_odds: 120
  stake_type: cash
  stake: 5.27
  paid: 11.59
  profit: 6.32
  result_strikeouts: 8
  outcome: WIN
```

## Final Pitching Line

| IP | H | R | ER | BB | K | HR | Pitches-Strikes | BF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5.0 | 5 | 2 | 2 | 1 | 8 | 0 | 95-60 | 20 |

## Core Metrics

| Metric | Result |
|---|---:|
| Total Pitches | 95 |
| Average Pitch Velocity | 92.6 mph |
| Top-Level Velo Marker | 99.6 mph |
| Exit Velocity Marker | 104.6 |
| Swings | 44 |
| Called Strikes | 16 |
| Whiffs | 14 |
| CStr+Whiff | 30 / 95 |
| CSW | 32% |
| Whiff / Swing | 32% |
| Strike Rate | 63% |
| Zone Rate | 58% |
| Chase Rate | 23% |
| First-Pitch Strike | 70% |
| Average EV Allowed | 93.4 mph |

## Pitch Mix

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CStr+Whiff |
|---|---:|---:|---:|---:|---:|---:|---:|
| Sinker | 35% / 33 | 97.8 | 0 | 12 | 10 | 2 | 36% |
| Sweeper | 25% / 24 | 87.9 | 3 | 13 | 3 | 6 | 38% |
| 4-Seam Fastball | 16% / 15 | 97.9 | 3 | 10 | 1 | 4 | 33% |
| Curveball | 16% / 15 | 83.7 | 1 | 3 | 1 | 1 | 13% |
| Cutter | 8% / 8 | 92.3 | 1 | 6 | 1 | 1 | 25% |
| All | 100% / 95 | 92.6 | 8 | 44 | 16 | 14 | 32% |

## What Worked

1. **Plus-money ceiling selection was correct.** The safer 6+ was overpriced, while 7+ at +120 produced playable ceiling value.
2. **Stuff was live.** Williams carried a 99.6 velo marker, with sinker and four-seam both running near 98 mph.
3. **CSW supported the ladder.** Overall 32% CSW was strong enough to validate the ceiling target.
4. **First-pitch strike rate helped early count control.** 70% first-pitch strikes created more strikeout counts.
5. **White Sox LRS was correctly exploitable.** The matchup allowed ceiling access despite only 5.0 innings.

## Risk Notes

- Williams needed 8 Ks in only 5.0 innings; this was a ceiling outcome, not a soft-floor cash.
- Average EV allowed was high at 93.4 mph, with 5 hard-hit batted balls.
- Chase rate was only 23%, meaning this was more stuff/zone dominance than chase dominance.
- The model should continue treating Williams as high-ceiling but volatility-sensitive.

---

# Portfolio Learning

```yaml
portfolio_learning_2026_06_22:
  record: 2-0
  profit: 14.13
  confirmed:
    - price_shopping_between_ladder_and_over_under_screen
    - michael_king_soft_threshold_attack
    - gavin_williams_plus_money_ceiling_attack
    - lineup_resistance_score_improved_target_filtering
    - avoiding_overpriced_ceiling_ladders
  caution:
    - both tickets were threshold-sensitive
    - michael_king_6_plus_would_have_lost
    - gavin_williams_required_ceiling_pace
    - contact_quality_allowed_was_not_fully_clean
```

---

# CLV Tracking Placeholder

Closing-line comparison should be added if post-close odds are captured.

```yaml
clv_tracking:
  michael_king:
    local_william_hill_clv: pending
    consensus_market_clv: pending
    sharp_source_clv: pending
  gavin_williams:
    local_william_hill_clv: pending
    consensus_market_clv: pending
    sharp_source_clv: pending
```

---

# Tags

`WIN` `WILLIAM_HILL_EXECUTION_LAYER` `TWO_AND_ZERO_PORTFOLIO` `MICHAEL_KING_5PLUS_CONFIRMED` `GAVIN_WILLIAMS_7PLUS_CONFIRMED` `SOFT_THRESHOLD_HIT` `PLUS_MONEY_CEILING_HIT` `LRS_CONFIRMED` `PRICE_SHOPPING_CONFIRMED` `DO_NOT_BLIND_LADDER` `CLV_PENDING`
