# SharpEdge MLB K Prop Postmortem — 2026-06-21

## Zack Wheeler — 7+ Strikeouts

**Game:** New York Mets at Philadelphia Phillies  
**Market:** Zack Wheeler 7+ pitching strikeouts  
**Book:** William Hill  
**Entry Odds:** -122  
**Cash Wagered:** $8.39  
**Paid:** $15.27  
**Profit:** +$6.88  
**Final Result:** 7 strikeouts  
**Outcome:** WIN

---

## Pregame Projection Snapshot

| Metric | Projection |
|---|---:|
| Mean | 7.3 K |
| Median | 7 K |
| Hit Probability | 62-65% |
| Market Implied Probability | 55.0% |
| Estimated Edge | +7.0 to +10.0 percentage points |
| Grade | A |

```yaml
position:
  date: 2026-06-21
  sport: MLB
  market_type: pitcher_strikeouts
  pitcher: Zack Wheeler
  team: Philadelphia Phillies
  opponent: New York Mets
  book: William Hill
  target: 7_plus_strikeouts
  entry_odds: -122
  stake_type: cash
  stake: 8.39
  paid: 15.27
  profit: 6.88
  result_strikeouts: 7
  outcome: WIN
```

---

## Final Pitching Line

| IP | H | R | ER | BB | K | HR | Pitches-Strikes | BF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5.2 | 4 | 2 | 2 | 3 | 7 | 1 | 104-60 | 23 |

---

## Core Metrics

| Metric | Result |
|---|---:|
| Total Pitches | 104 |
| Average Pitch Velocity | 89.6 mph |
| Top-Level Velo Marker | 97.7 mph |
| Exit Velocity Marker | 107.8 |
| Swings | 46 |
| Called Strikes | 14 |
| Whiffs | 17 |
| CStr+Whiff | 31 / 104 |
| CSW | 30% |
| Whiff / Swing | 37% |
| Strike Rate | 58% |
| Zone Rate | 39% |
| Chase Rate | 29% |
| First-Pitch Strike | 61% |
| Average EV Allowed | 83.3 mph |

---

## Pitch Mix

| Pitch | Usage | Avg Velo | K | Swings | CStr | Whiffs | CStr+Whiff |
|---|---:|---:|---:|---:|---:|---:|---:|
| 4-Seam Fastball | 29% / 30 | 95.9 | 2 | 12 | 5 | 6 | 37% |
| Sweeper | 26% / 27 | 81.7 | 3 | 13 | 5 | 7 | 44% |
| Splitter | 16% / 17 | 88.4 | 1 | 5 | 1 | 3 | 24% |
| Sinker | 14% / 15 | 95.8 | 1 | 9 | 3 | 0 | 20% |
| Cutter | 9% / 9 | 90.9 | 0 | 5 | 0 | 1 | 11% |
| Curveball | 6% / 6 | 80.3 | 0 | 2 | 0 | 0 | 0% |
| All | 100% / 104 | 89.6 | 7 | 46 | 14 | 17 | 30% |

---

## What Worked

1. **Median threshold projection was correct.** The model projected a 7 K median and Wheeler landed exactly on the 7+ threshold.
2. **Sweeper was the primary separator.** Wheeler's sweeper produced 3 strikeouts, 7 whiffs, and a 44% CStr+Whiff rate.
3. **Four-seam fastball supported the K floor.** The fastball produced 2 strikeouts and a strong 37% CStr+Whiff rate.
4. **Contact suppression protected the runway.** Wheeler allowed only 83.3 average EV on batted balls, helping him survive traffic and reach 104 pitches.
5. **Leash stability was validated.** Philadelphia extended Wheeler to 104 pitches despite three walks and a HR allowed.

---

## Risk Notes

- Wheeler needed 104 pitches to complete only 5.2 innings.
- Walk count reached 3, creating pitch-count drag.
- The ticket cashed exactly at 7 Ks, so 8+ would have failed.
- This reinforces the model's correct choice of 7+ over 8+.

---

## CLV Read

William Hill was not shown on the closing line comparison screen, so local William Hill CLV could not be directly measured.

Available broader-market close showed most books around **Over 6.5 between -108 and -125**, with Pinnacle at **-116** and Kalshi at **-121**.

```yaml
clv_tracking:
  local_william_hill_clv: unknown
  entry: "7+ at -122"
  broader_market_close: "Over 6.5 around -108 to -125"
  pinnacle_close: "Over 6.5 at -116"
  kalshi_close: "Over 6.5 at -121"
  market_clv: neutral_to_slight_negative
  sharp_clv_vs_pinnacle: slight_negative
  result_note: "Win does not erase the need to track CLV separately from outcome."
```

### CLV Protocol Note

SharpEdge should track CLV in three layers:

1. **Local book CLV** — entry vs closing number at the sportsbook where the bet was placed.
2. **Consensus market CLV** — entry vs broader market close.
3. **Sharp-source CLV** — entry vs a sharp reference such as Pinnacle.

When William Hill is missing from the closing screen, record local CLV as `unknown` and use consensus/Pinnacle as secondary benchmarks.

---

## Model Grade

| Category | Grade |
|---|---:|
| Result | A |
| Projection Quality | A |
| Entry Execution | A- |
| Market Timing | B |
| Leash Stability | A- |
| Pitch Efficiency | B- |
| CSW | A- |
| Whiff Sustainability | A |
| Contact Suppression | A |
| LRS Accuracy | A |
| Final Grade | A |

---

## Model Learning

```yaml
wheeler_2026_06_21_learning:
  confirmed:
    - primary_edge_rank_accuracy
    - median_threshold_targeting
    - leash_stability
    - sweeper_whiff_path
    - contact_suppression_runway_protection
    - exact_threshold_hit
  caution:
    - three_walks_created_pitch_count_drag
    - 8_plus_ladder_would_have_failed
    - track_clv_independently_from_result
```

---

## Tags

`WIN` `WILLIAM_HILL_EXECUTION_LAYER` `PRIMARY_EDGE_CONFIRMED` `MEDIAN_THRESHOLD_CONFIRMED` `EXACT_THRESHOLD_HIT` `LRS_CONFIRMED` `SWEEPER_WHIFF_PATH` `CONTACT_SUPPRESSION_CONFIRMED` `LEASH_STABILITY_CONFIRMED` `CLV_NEUTRAL_TO_SLIGHT_NEGATIVE` `DO_NOT_BLIND_LADDER`
