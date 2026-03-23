# TOR @ PHX Postmortem V1

Date: 2026-03-22
Final: Suns 120, Raptors 98
Project: SharpEdge NBA LiveFlow v.003

## Summary
- Environment tag: `ENVIRONMENT_FAILED_TOR_PHX`
- Key tags: `PHX_SHOOTING_SPIKE_CONFIRMED`, `POELTL_ROLE_FAILURE`, `BOOKER_HOOK_BURN`, `LIVE_BACKDOOR_FAILED`
- Final read: Phoenix sustained elite perimeter efficiency and won the rebound environment, invalidating Toronto’s expected size edge.

## Game Phase Analysis
### First Half
Phoenix took control early and led 66-48 at halftime. The Suns’ shotmaking held from the opening stretch, while Toronto’s interior edge never materialized. Jakob Poeltl was a nonfactor, and Devin Booker’s usage translated more into points and assists than rebounds.

### Second Half
Toronto never built a real comeback structure. Phoenix maintained control and the final margin expanded to 22. The halftime backdoor-cover thesis on Toronto failed because the Suns’ shooting held and Toronto never stabilized on the glass or in transition.

## Pivotal Moments
1. Phoenix perimeter shooting sustained: 18/40 from three (45.0%).
2. Toronto lost the rebound battle: 30 to 43 total rebounds, 7 to 14 offensive rebounds.
3. Jakob Poeltl finished with 0 rebounds in 17 minutes, collapsing the main frontcourt premise.

## Defensive / Psychological Variables
- Phoenix had clean role clarity around Booker plus strong support creation.
- Toronto failed to establish resistance once the game tilted.
- This was not a viable backdoor-cover environment after halftime; Toronto was outplayed in shooting, rebounding, second-chance points, and turnover conversion.

## Model Relevance Summary
### Pregame tickets tied to this matchup
- Card 1: Jakob Poeltl Higher 8.5 REB ❌
- Card 4: Devin Booker Higher 3.5 REB ❌ by hook
- Live prop card: Jakob Poeltl Higher 4.5 REB ❌, Devin Booker Higher 3.5 REB ❌ by hook
- Live game line: TOR +10.5 ❌

### Leg-by-leg notes
#### Jakob Poeltl Higher 8.5 — MISS
- Actual: 0 rebounds
- Failure tags: `ROLE_FAILURE`, `CENTER_DISPLACEMENT_RISK_ON_MISREAD`, `ENVIRONMENT_FAILED`
- Note: This was a full role collapse, not a variance miss.

#### Devin Booker Higher 3.5 — MISS
- Actual: 3 rebounds
- Failure tags: `HOOK_BURN`, `ROLE_SUCCESS_STAT_ALLOCATION_MISS`
- Note: Phoenix environment worked, but production skewed toward points and assists instead of rebounds.

#### TOR +10.5 live — MISS
- Failure tags: `LIVE_BACKDOOR_FAILED`, `PHX_SHOOTING_SPIKE_HELD`, `HALFTIME_STRUCTURE_MISREAD`
- Note: Halftime regression/backdoor assumptions failed because Phoenix kept scoring and Toronto never stabilized.

## Team Stats Snapshot
- TOR: 98 points, 30 rebounds (7 offensive), 28 assists, 19 turnovers, 9/27 from three.
- PHX: 120 points, 43 rebounds (14 offensive), 24 assists, 16 turnovers, 18/40 from three.

## Action Items
- Strengthen `CENTER_ROLE_STABILITY_FAILSAFE` for center rebound overs when the opponent can spread the floor and the team identity breaks early.
- Re-check rebound allocation on high-usage creator teams where efficient offense may reduce guard rebound variance.

## GitHub Tags
- `POSTMORTEM_TOR_PHX_03222026`
- `PHX_SHOOTING_SPIKE_CONFIRMED`
- `POELTL_ROLE_FAILURE`
- `BOOKER_HOOK_BURN`
- `TOR_SIZE_EDGE_FAILED`
- `LIVE_BACKDOOR_FAILED`
- `SECOND_CHANCE_ENVIRONMENT_LOST`
- `MODEL_PATCH_REQUIRED_CENTER_ROLE_STABILITY`
