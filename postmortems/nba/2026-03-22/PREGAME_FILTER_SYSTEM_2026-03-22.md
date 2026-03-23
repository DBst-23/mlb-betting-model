# SharpEdge Pregame Filter System

Date: 2026-03-22
Project: SharpEdge NBA LiveFlow v.003

## Purpose
Codify the main environment lessons from the 2026-03-22 NBA slate into a pregame filter that determines whether a matchup should be attacked with pregame props, held for LiveFlow only, or avoided.

## Core Environment Types

### 1. Halfcourt Suppression
**Examples:** missing top usage scorer, slower pace, organized defenses, concentrated rebound tree.

**Pregame actions**
- Upgrade rebound overs on stable high-minute stars and primary wings.
- Downgrade broad game-side confidence unless favorite shooting efficiency is also secure.
- Prefer props over sides when suppression is clear but shotmaking variance remains open.

**Tags**
- `HALFCOURT_SUPPRESSION_ENVIRONMENT`
- `REBOUND_CONCENTRATION_ON`
- `PROP_OVER_SIDE`

### 2. Concentrated Chaos
**Examples:** undermanned frontcourt, volatile game flow, but one team still has clear glass advantage.

**Pregame actions**
- Avoid unders on starting big rebound props if the opponent is severely weak on the glass.
- Split chaos reads into distributed chaos vs concentrated chaos before firing unders.
- Keep live side capture ready if structural rebound dominance appears before the scoreboard reflects it.

**Tags**
- `CONCENTRATED_CHAOS_ENVIRONMENT`
- `FRONTCOURT_DOMINANCE_RISK`
- `LIVE_SIDE_CAPTURE_READY`

### 3. Controlled Elite Offense
**Examples:** Jokic-type hub, elite assist rates, sustained efficiency, opponent survives only via volume.

**Pregame actions**
- Downgrade sides and totals when the price already reflects control.
- Upgrade rebound overs that are driven by volume/possession count rather than team win equity.
- Avoid mistaking high volume for true competitiveness when the opponent's efficiency edge is overwhelming.

**Tags**
- `CONTROLLED_ELITE_OFFENSE_ENVIRONMENT`
- `EFFICIENCY_OVER_VOLUME`
- `REBOUND_OVERS_STABLE`

### 4. Blowout Volatility
**Examples:** giant spread, top-heavy favorite, weaker opponent with poor structural resistance.

**Pregame actions**
- Upgrade center-anchor overs and main-frontcourt rebound ceilings on the favorite.
- Downgrade wing rebound overs and secondary support overs.
- Treat role-linked unders more favorably when backup usage is uncertain and tied to game state.

**Tags**
- `BLOWOUT_VOLATILITY_FLAG`
- `CENTER_PRIORITY_ON`
- `WING_REBOUND_SUPPRESSION`

### 5. Collapse / Role Failure Risk
**Examples:** shaky center minutes, spread-floor opponent, team identity can break early.

**Pregame actions**
- Downgrade center rebound overs when the player's role stability is not truly locked.
- Trigger `CENTER_ROLE_STABILITY_FAILSAFE` if the matchup can erase the center from the intended game plan.
- Prefer waiting for LiveFlow confirmation before entering chase overs.

**Tags**
- `CENTER_ROLE_STABILITY_FAILSAFE`
- `CENTER_DISPLACEMENT_RISK_ON`
- `LIVE_CONFIRMATION_REQUIRED`

## Filter Ladder

### Tier 1 — Auto-Playable Pregame
Criteria:
- Clear environment classification
- Stable role minutes
- No major CLV tax
- Prop aligns with environment-specific allocation

Action:
- Fire pregame prop
- Can be used in core cards

### Tier 2 — Playable but Reduced
Criteria:
- Environment identified, but one fragility factor remains
- Small CLV loss or moderate rotation uncertainty

Action:
- Single card only
- Reduced stake

### Tier 3 — LiveFlow Only
Criteria:
- Environment unclear pregame or depends on first-half confirmation
- Game line or prop likely to improve after early variance

Action:
- No pregame entry
- Monitor halftime structure and role deployment

### Tier 4 — No Fire
Criteria:
- Role instability + unclear environment + poor number
- Side confidence and prop confidence are both weak

Action:
- Pass entirely

## Hard Rules Added From This Slate
1. Do not tie side confidence to environment confidence.
2. High volume with sub-45% shooting is a fake competitiveness signal.
3. Chaos must be labeled as either distributed or concentrated before playing rebound unders.
4. In blowouts, prioritize bigs over wings for rebounds.
5. A rebound over can still be valid in a losing script if possession volume is real.
6. If the line loses clear cushion and the book never confirms the move, downgrade immediately.

## Operational Workflow
1. Classify environment before opening the board.
2. Assign role-stability rating to each target.
3. Label matchup as Tier 1, 2, 3, or 4.
4. Only then compare line, mean, median, and hit probability.
5. If Tier 3, wait for LiveFlow instead of forcing pregame entry.

## Carry-Forward Patch Queue
- `MODEL_PATCH_SPLIT_CHAOS_TYPES`
- `MODEL_PATCH_KEEP_BLOWOUT_FILTERS`
- `MODEL_PATCH_REQUIRED_CENTER_ROLE_STABILITY`
- `JOKIC_CONTROL_FIELD`
- `EFFICIENCY_OVER_VOLUME_FILTER`
