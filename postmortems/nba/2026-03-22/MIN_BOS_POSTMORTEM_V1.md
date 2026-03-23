# MIN @ BOS Postmortem V1

Date: 2026-03-22
Final: Timberwolves 102, Celtics 92
Project: SharpEdge NBA LiveFlow v.003

## Summary
- Environment tag: `HALFCOURT_SUPPRESSION_ENVIRONMENT_CONFIRMED`
- Key tags: `MODEL_EDGE_REALIZED`, `REBOUND_CONCENTRATION_CONFIRMED`, `BOS_OFFENSE_COLLAPSE`, `UNDER_SCRIPT_CONFIRMED_BUT_SIDE_MISREAD`
- Final read: The structural suppression read held, rebound concentration among the core targets held, but Boston lost the game outright as Minnesota controlled the glass and won the shot-volume battle.

## Game Phase Analysis
### First Half
The game opened as the type of slower, structured environment expected without Anthony Edwards. Possessions were more deliberate and rebound opportunities concentrated around the frontcourt and primary wings. However, Minnesota’s energy and shot volume began to pressure Boston’s offensive flow.

### Second Half
Minnesota finished the game stronger and Boston’s offense never recovered. The Celtics shot just 34/95 from the field and 9/33 from three, while Minnesota generated enough second-chance opportunities and defensive resistance to turn a suppression game into a Wolves win rather than a Boston control game.

## Pivotal Moments
1. Boston offensive collapse: 35.8% FG and 27.3% from three.
2. Minnesota rebounding and volume edge: 56 rebounds to 53, despite both teams living in a lower-efficiency environment.
3. Minnesota bench lift, especially Bones Hyland plus Naz Reid, changed the game’s momentum and scoring balance.

## Defensive / Psychological Variables
- Minnesota stayed intact defensively and did not crack under Boston’s home-court pressure.
- Boston failed to convert the expected halfcourt control into scoring leverage.
- This matchup confirmed the rebound concentration logic, even though the side result flipped away from the favorite.

## Model Relevance Summary
### Pregame tickets tied to this matchup
- Card 2: Jayson Tatum Higher 7.5 REB ✅
- Card 2: Ayo Dosunmu Higher 4.5 REB ✅

### Leg-by-leg notes
#### Jayson Tatum Higher 7.5 — HIT
- Actual: 11 rebounds
- Success tags: `HIT_REGISTERED`, `REBOUND_CONCENTRATION_CONFIRMED`, `MODEL_EDGE_REALIZED`
- Note: Tatum benefited from the exact slower, more concentrated rebound environment the model expected.

#### Ayo Dosunmu Higher 4.5 — HIT
- Actual: 8 rebounds
- Success tags: `HIT_REGISTERED`, `WING_REBOUND_SHARE_CONFIRMED`, `MODEL_EDGE_REALIZED`
- Note: Ayo’s quiet rebound profile translated cleanly in the suppressed environment and beat the line comfortably.

## Team Stats Snapshot
- MIN: 102 points, 56 rebounds (12 offensive), 24 assists, 14 turnovers, 12/33 from three.
- BOS: 92 points, 53 rebounds (13 offensive), 17 assists, 11 turnovers, 9/33 from three.

## Action Items
- Keep the suppression + rebound concentration framework active for similar missing-star environments.
- Separate game-side confidence from prop confidence more aggressively when the environment is right but the favorite’s offensive efficiency is less secure than assumed.

## GitHub Tags
- `POSTMORTEM_MIN_BOS_03222026`
- `HALFCOURT_SUPPRESSION_ENVIRONMENT_CONFIRMED`
- `MODEL_EDGE_REALIZED`
- `REBOUND_CONCENTRATION_CONFIRMED`
- `BOS_OFFENSE_COLLAPSE`
- `UNDER_SCRIPT_CONFIRMED_BUT_SIDE_MISREAD`
