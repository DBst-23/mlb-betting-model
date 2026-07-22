# Tyler Mahle Live K Prop Postmortem — 2026-07-21

## Position
- Book: William Hill
- Game: San Francisco Giants at Kansas City Royals
- Market: Tyler Mahle 6+ strikeouts live
- Entry: +103
- Stake: $15.00
- Paid: $0.00
- Profit/Loss: -$15.00
- Strikeouts at entry: 4 through 3.0 innings
- Final: 5.0 IP, 5 H, 3 ER, 1 BB, 4 K, 1 HR, 91 pitches

## Entry Read
Mahle had four strikeouts through three innings, but the live profile was less dominant than the strikeout count suggested:
- 22% CSW
- 23% whiff per swing
- 42% chase
- 68% strikes
- 60 pitches after three innings

The wager required two more strikeouts. That demanded both sustainable swing-and-miss and enough remaining batters faced.

## Final Metrics
- Strike rate: 65%
- CSW: 20%
- Whiff per swing: 18%
- Zone rate: 45%
- Chase rate: 36%
- First-pitch strike rate: 55%
- Average EV: 89.9 mph
- Hard-hit balls: 8
- Max EV: 106.7 mph

## Pitch Mix
- Four-seam: 42 pitches, 2 K, 19% CSW
- Cutter: 26 pitches, 1 K, 19% CSW
- Splitter: 23 pitches, 1 K, 22% CSW

## What Happened
Mahle recorded no strikeouts after the live entry. Over the final two innings, the early chase and whiff rates regressed, Kansas City made more contact, and Mahle reached 91 pitches after five innings.

The live model over-weighted the four strikeouts already banked and under-weighted:
- modest entry CSW
- modest entry whiff rate
- 60 pitches through three innings
- second-trip lineup resistance
- five-inning leash risk

## Model Diagnosis
Classification: Full live-process miss

Primary failure: Whiff sustainability and inning-runway overestimation.

Secondary failure: Standard stake on a marginal live profile.

## Patch
```yaml
post_entry_whiff_sustainability_gate:
  two_plus_additional_ks:
    preferred_csw_floor: 27%
    preferred_whiff_per_swing_floor: 26%
  runway_penalty:
    trigger: 55_plus_pitches_after_3_innings
  second_trip_penalty: true
  if_both_whiff_floors_fail:
    action: pass_or_micro_only
```

## Stake Review
```yaml
entry_grade_revised: C_plus
correct_stake: pass_or_micro
standard_stake_allowed: false
```

## Final Lesson
A strong live strikeout count is not enough. The model must project only future strikeouts using current whiff quality, expected remaining batters faced, pitch count, and leash.

## Tags
`liveflow` `pitcher-k` `tyler-mahle` `royals` `whiff-regression` `runway-failure` `stake-sizing` `loss`
