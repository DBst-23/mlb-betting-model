# BKN @ SAC Postmortem V1

Date: 2026-03-22
Final: Kings 126, Nets 122
Project: SharpEdge NBA LiveFlow v.003

## Summary
- Environment tag: `CHAOS_ENVIRONMENT_PARTIALLY_CONFIRMED`
- Key tags: `SAC_FRONTCOURT_CONCENTRATION_REAL`, `RAYNAUD_UNDER_FAILED`, `LIVE_SAC_CAPTURE_HIT`, `OFFENSE_OUTRAN_CONTROL`
- Final read: The game was chaotic and high-variance as expected, but Sacramento's frontcourt concentration was stronger than projected. Brooklyn's shotmaking kept the game live, while the Kings' rebound dominance and second-chance volume still carried the structural edge.

## Game Phase Analysis
### First Half
Brooklyn led at halftime despite Sacramento controlling the glass. This confirmed the split-variance shape flagged pregame: BKN held the shooting edge while SAC owned rebounding and second-chance leverage. That divergence created the halftime live entry on SAC -1.5.

### Second Half
The Kings converted their structural edge into the final result. Sacramento won the rebound battle 51-25 and offensive rebounds 17-7, which outweighed Brooklyn's strong shooting night. The live read on Sacramento side control was correct, even though the game remained close to the horn.

## Pivotal Moments
1. Sacramento rebound dominance: 51 rebounds to 25, including 17 offensive boards.
2. Second-chance scoring: SAC 28 second-chance points to BKN 10.
3. Brooklyn shot well enough to keep pressure on the game, scoring 122 on 63.0 TS%, but could not survive the possession gap.
4. Malik Monk's bench offense and the Kings' frontcourt duo of Achiuwa plus Raynaud stabilized the comeback and finish.

## Defensive / Psychological Variables
- Brooklyn never fully collapsed offensively, which is why this game stayed volatile and dangerous.
- Sacramento’s interior and second-chance persistence mattered more than initial shooting flow.
- This matchup showed that chaos can coexist with concentrated frontcourt outcomes when one team fully owns the glass.

## Model Relevance Summary
### Pregame tickets tied to this matchup
- Maxime Raynaud Lower 9.5 REB ❌
- Josh Minott Lower 4.5 REB ➖ refund/void
- Live SAC -1.5 ✅

### Leg-by-leg notes
#### Maxime Raynaud Lower 9.5 — MISS
- Actual: 10 rebounds
- Failure tags: `MISS_REGISTERED`, `NEGATIVE_CLV_PUNISHED`, `SAC_FRONTCOURT_CONCENTRATION_REAL`
- Note: The under lost both on price and on game shape. Sacramento's frontcourt concentrated more than our anti-concentration framework expected.

#### Josh Minott Lower 4.5 — REFUND
- Status: refund/void
- Tags: `REFUND_REGISTERED`
- Note: No reliable outcome signal from this leg.

#### SAC -1.5 live — HIT
- Result: Sacramento won 126-122
- Success tags: `LIVE_HIT_REGISTERED`, `HALFTIME_STRUCTURE_CONFIRMED`, `SECOND_CHANCE_EDGE_CONVERTED`
- Note: The live entry correctly prioritized structural control over halftime scoreboard variance.

## Team Stats Snapshot
- BKN: 122 points, 25 rebounds (7 offensive), 30 assists, 7 turnovers, 14/33 from three.
- SAC: 126 points, 51 rebounds (17 offensive), 30 assists, 16 turnovers, 14/27 from three.

## Action Items
- Keep chaos labeling active, but split it into two subtypes: distributed chaos vs concentrated chaos.
- Add a stronger frontcourt-concentration trigger when the opponent is severely undermanned on the glass.
- Preserve live side capture logic when structural rebound dominance is obvious despite halftime score deficit.

## GitHub Tags
- `POSTMORTEM_BKN_SAC_03222026`
- `CHAOS_ENVIRONMENT_PARTIALLY_CONFIRMED`
- `SAC_FRONTCOURT_CONCENTRATION_REAL`
- `RAYNAUD_UNDER_FAILED`
- `LIVE_SAC_CAPTURE_HIT`
- `SECOND_CHANCE_EDGE_CONVERTED`
- `MODEL_PATCH_SPLIT_CHAOS_TYPES`
