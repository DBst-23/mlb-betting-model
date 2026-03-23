# WAS @ NYK Postmortem V1

Date: 2026-03-22
Final: Knicks 145, Wizards 113
Project: SharpEdge NBA LiveFlow v.003

## Summary
- Environment tag: `BLOWOUT_VOLATILITY_FLAG_CONFIRMED`
- Key tags: `KNICKS_OFFENSIVE_AVALANCHE`, `KAT_REBOUND_CEILING_CONFIRMED`, `HART_SOLID_NOT_NUCLEAR`, `ALVARADO_UNDER_HIT`, `WIZARDS_COMPETENCE_NOT_COMPETITIVENESS`
- Final read: The game fully confirmed the blowout environment. New York’s offensive efficiency and rebounding edge were overwhelming, while the Wizards still produced enough scattered offense to create misleading surface stats without ever threatening control.

## Game Phase Analysis
### First Half
The Knicks established immediate control and never trailed meaningfully. Their size, efficiency, and cleaner offensive organization created the exact type of blowout trajectory the model warned about. Washington generated some isolated scoring pockets, but they could not hold the glass or contain New York’s primary creators.

### Second Half
The blowout remained intact. New York finished with 145 points on elite efficiency and continued to dominate interior scoring and rebounding. Washington’s offensive output reached 113, but much of it came after the game state was already broken, reinforcing that raw final scoring can hide a structurally non-competitive game.

## Pivotal Moments
1. Knicks offensive explosion: 145 points, 58.5% FG, 53.1% from three.
2. Rebounding domination: NYK 48 rebounds to WAS 28.
3. Karl-Anthony Towns produced the highest-value frontcourt line with 26 points and 16 rebounds.
4. Mitchell Robinson delivered strong bench board support with 10 rebounds in 17 minutes.

## Defensive / Psychological Variables
- The blowout risk was real and remained live throughout.
- Washington did not fully collapse offensively, but they never showed real game-control leverage.
- New York’s role clarity stayed intact enough for the main rebound hierarchy to matter before deeper bench rotations arrived.

## Model Relevance Summary
### Tickets tied to this matchup
- Jose Alvarado Lower 2.5 REB ✅

### Notes on core board reads
- Karl-Anthony Towns at 12.5 rebounds would have hit comfortably with 16.
- Josh Hart at 7.5 rebounds did not clear, finishing with 6.
- Mikal Bridges at 4.5 rebounds failed hard, finishing with 0.
- OG Anunoby at 5.5 rebounds failed with 2.
- Mitchell Robinson remained highly live in this environment and finished with 10 off the bench.

### Leg-by-leg notes
#### Jose Alvarado Lower 2.5 — HIT
- Actual: 2 rebounds
- Success tags: `HIT_REGISTERED`, `ROTATION_DEPENDENT_UNDER_HIT`, `BLOWOUT_CONTEXT_HANDLED`
- Note: The later-context entry worked. Even in a Knicks blowout win, Alvarado stayed below the line and never became a rebound-accumulation problem.

## Team Stats Snapshot
- WAS: 113 points, 28 rebounds (8 offensive), 25 assists, 14 turnovers, 18/47 from three.
- NYK: 145 points, 48 rebounds (13 offensive), 32 assists, 14 turnovers, 17/32 from three.

## Action Items
- Keep blowout filters active for Knicks-style heavy favorite environments.
- Separate score inflation from competitiveness when evaluating team totals and support-player prop viability.
- Upgrade center-anchor overs and downgrade wing rebound overs when the favorite’s frontcourt size edge is overwhelming.

## GitHub Tags
- `POSTMORTEM_WAS_NYK_03222026`
- `BLOWOUT_VOLATILITY_FLAG_CONFIRMED`
- `KNICKS_OFFENSIVE_AVALANCHE`
- `KAT_REBOUND_CEILING_CONFIRMED`
- `ALVARADO_UNDER_HIT`
- `WING_REBOUND_FAIL_IN_BLOWOUT`
- `MODEL_PATCH_KEEP_BLOWOUT_FILTERS`
