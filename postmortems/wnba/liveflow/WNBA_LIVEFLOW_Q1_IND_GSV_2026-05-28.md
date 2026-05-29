# WNBA LiveFlow Q1 Strike Prep — Indiana Fever at Golden State Valkyries

## Game Metadata
- **Date:** 2026-05-28
- **Venue:** Chase Center, San Francisco, CA
- **Checkpoint:** End of 1st Quarter
- **Score:** Golden State Valkyries 21, Indiana Fever 14
- **Officials:** Roy Gulbeyan, Agon Abazi, Tyler Mirkovich
- **Inactive:** Fever — Hall, Pissott | Valkyries — Rupert, Sowah

## Q1 Snapshot
Indiana opened ice cold while Golden State controlled defensive pressure and rebounding quality.

```yaml
q1_score:
  indiana_fever: 14
  golden_state_valkyries: 21

team_efficiency:
  fever:
    fg: 5/20
    fg_pct: 25.0
    three_pt: 0/8
    three_pt_pct: 0.0
    ft: 4/5
    rebounds: 11
    assists: 2
    turnovers: 1
  valkyries:
    fg: 8/19
    fg_pct: 42.1
    three_pt: 2/6
    three_pt_pct: 33.3
    ft: 3/3
    rebounds: 12
    assists: 6
    turnovers: 1
```

## LiveFlow Model Read
This is a **Fever offensive suppression watch**, not yet a full collapse. The strongest signal is Indiana's 0-for-8 from three with only 2 assists. The low turnover count means the issue is not chaos; it is shot quality and blocked creation.

Golden State has 3 blocks already, including multiple early contests on Caitlin Clark and Lexie Hull. Veronica Burton's point-of-attack impact is a meaningful live modifier.

## Player / Role Notes
```yaml
key_signals:
  caitlin_clark:
    q1_points: 5
    fg: 1/4
    three_pt: 0/1
    fouls: 1
    note: Drawing contact but not creating efficient half-court offense yet.
  kelsey_mitchell:
    q1_points: 0
    fg: 0/2
    three_pt: 0/1
    fouls: 1
    note: Early offensive non-factor; watch for Q2 aggression correction.
  lexie_hull:
    q1_points: 0
    fg: 0/4
    three_pt: 0/2
    rebounds: 3
    note: Volume without conversion.
  veronica_burton:
    q1_points: 8
    blocks: 2
    note: Defensive pressure plus scoring burst.
  janelle_salaun:
    q1_points: 5
    rebounds: 2
    note: Bench spacing stabilized Valkyries close.
```

## Live Total / Strike Setup
```yaml
current_total_points: 35
q1_pace_quality: moderate
shooting_context:
  indiana_three_point_regression: likely_positive
  golden_state_efficiency_regression: mild_negative
  defensive_pressure: golden_state_plus

projected_final_total:
  mean: 153.5
  median: 153
  range: 148-160
```

## Edge Board
```yaml
market_targets:
  primary_watch:
    - Fever team total under if market remains anchored too high
    - Full game under if live total stays inflated above 160.5
    - Valkyries spread/ML only if plus price or soft number appears
  avoid:
    - Chasing Valkyries after full market adjustment
    - Fever overs unless Indiana creates paint touches early Q2
    - Over unless Indiana starts Q2 with quick 3PT correction
```

## Trigger Logic
```yaml
LIVE_TOTAL_COLLAPSE_MISPRICE_CHECK:
  q1_lead_gte_7: true
  trailing_team_q1_points_lte_14: true
  trailing_team_fg_pct_lte_30: true
  trailing_team_3pt_pct_lte_20: true
  trailing_team_turnovers_high: false
  status: WATCHLIST_NOT_FULL_TRIGGER
```

This is a **pre-halftime watchlist** version of the collapse-misprice logic. The full tag should not fire until Q2 confirms that Indiana cannot correct the shot profile.

## Strike Plan
```yaml
next_checkpoint:
  time: Q2 6:00
  strike_if:
    - Indiana total points <= 24
    - Indiana remains <= 2 made threes
    - live total remains >= 157.5
    - Golden State lead remains >= 7
  preferred_attack:
    - No Over live total
    - Fever team total under
    - Valkyries spread if not priced beyond threshold
  pass_if:
    - Indiana scores 10+ points in first 4 minutes of Q2
    - Clark/Mitchell hit back-to-back threes
    - live total corrects below 153.5
```

## Tags
```yaml
tags:
  - WNBA_LIVEFLOW
  - Q1_STRIKE_PREP
  - IND_GSV_2026_05_28
  - FEVER_OFFENSIVE_SUPPRESSION_WATCH
  - PRE_HALFTIME_COLLAPSE_WATCH
  - LIVE_TOTAL_COLLAPSE_MISPRICE_WATCHLIST
```
