# WNBA LiveFlow Halftime Read — Las Vegas Aces at Dallas Wings

## Game Metadata
- **Date:** 2026-05-28
- **Venue:** College Park Center, Arlington, TX
- **Market Snapshot:** Halftime
- **Score:** Las Vegas 53, Dallas 45
- **Live Spread:** LV -9.5 (-112) / DAL +9.5 (-108)
- **Live Moneyline:** LV -610 / DAL +455
- **Live Total:** 189.5 — Over -117 / Under -104
- **Officials:** Clare Simmons, Charles Watson, Jason Alabanza

## Halftime Core Read
Las Vegas leads by 8 despite Dallas producing a clean offensive half. This is not a collapse profile. Dallas is shooting 45.5% FG, 33.3% from three, and 100% at the line. The Wings have 17 rebounds, 11 assists, and only 6 turnovers. Their offensive process is still alive.

Las Vegas is carrying elite efficiency: 52.5% FG, 50% from three, 13 assists, only 4 turnovers. The Aces are winning the paint 26-16 and have a cleaner assist-to-turnover profile.

## LiveFlow Model Projection
```yaml
projected_final_score:
  las_vegas_aces:
    mean: 97.8
    median: 98
  dallas_wings:
    mean: 88.6
    median: 88
  projected_total:
    mean: 186.4
    median: 186
  projected_margin:
    aces_by:
      mean: 9.2
      median: 10
```

## Market Probability Read
```yaml
market_probabilities:
  aces_ml_minus_610_implied: 85.9
  wings_ml_plus_455_implied: 18.0
  aces_minus_9_5_model_cover_probability: 50.8
  wings_plus_9_5_model_cover_probability: 49.2
  over_189_5_model_probability: 44.5
  under_189_5_model_probability: 55.5
```

## Edge Classification
```yaml
edge_board:
  spread:
    call: PASS
    reason: Market is tight. Model median sits near Aces -10, almost exactly on live spread.
  moneyline:
    call: PASS
    reason: Aces ML at -610 is beyond threshold with limited value.
  total:
    call: LEAN_UNDER_189_5
    confidence: moderate_low
    fair_line: 186.5
    edge: roughly 3 points to under
```

## LiveFlow Trigger Check
This does **not** qualify for `LIVE_TOTAL_COLLAPSE_MISPRICE`.

```yaml
LIVE_TOTAL_COLLAPSE_MISPRICE_CHECK:
  halftime_lead_gte_15: false
  trailing_team_q2_points_lte_12: false
  trailing_team_fg_pct_lte_40: false
  live_total_within_3_points_of_pregame_total: unknown
  leading_team_has_no_pace_incentive: partial_false
  status: NOT_TRIGGERED
```

Dallas scored 24 in Q2 and is still generating efficient possessions through Shepard, Bueckers, Fudd, and Siegrist. The live total is high, but this is not the same structural misprice as the Mystics-Storm total collapse.

## Recommended LiveFlow Action
```yaml
recommended_action:
  primary: PASS_FOR_NOW
  watch_trigger:
    - If 3Q starts below 9 points by 6:30, attack Under if total remains 187.5 or higher.
    - If Dallas opens 3Q with missed threes and Aces slow tempo, look for No Over plus money.
    - If live total drops below 184, do not chase under.
  avoid:
    - Aces ML at -610
    - Aces -9.5 without better price
    - Over 189.5 unless 3Q pace spikes immediately
```

## Tags
```yaml
tags:
  - WNBA_LIVEFLOW
  - HALFTIME_SCAN
  - LV_DAL_2026_05_28
  - TOTAL_LEAN_UNDER_BUT_NO_COLLAPSE
  - SPREAD_MARKET_EFFICIENT
  - NO_BET_PRIMARY
```
