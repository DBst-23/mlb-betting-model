# POSTMORTEM — 03/30 BOS @ ATL REBOUND SIGNAL AUDIT

## Summary
- Matchup: Celtics @ Hawks
- Final score: Hawks 112, Celtics 102
- Focus: rebound signal review, role-shift validation, and under-filter performance

## Primary signals audited
- Jalen Johnson Over 8.5 rebounds
- Derrick White Under 4.5 rebounds
- Jaylen Brown Under 7.5 rebounds
- Keon Ellis Over 6.5 points (separate card component linked to same workflow window)

## Final outcomes
- Jalen Johnson: 12 rebounds — Win
- Derrick White: 5 rebounds — Loss
- Jaylen Brown: 10 rebounds — Loss
- Keon Ellis: 13 points — Win

## Team environment outcome
- Boston rebounds: 48
- Atlanta rebounds: 45
- Boston offensive rebounds: 10
- Atlanta offensive rebounds: 9
- Boston shooting: 35-85 FG, 14-37 from three, 18-26 FT
- Atlanta shooting: 43-92 FG, 15-38 from three, 11-15 FT

## Signal review
### Jalen Johnson Over 8.5 rebounds
- Final: 12
- Cleared with room
- Boston frontcourt instability and Johnson’s role concentration held up
- Signal classification: Anchor hit

### Derrick White Under 4.5 rebounds
- Final: 5
- Lost by hook
- Boston’s improvised rotation and elevated minute load kept him live for long rebounds and spillover board volume
- Signal classification: Under-filter miss

### Jaylen Brown Under 7.5 rebounds
- Final: 10
- Clear miss
- Brown’s minutes, usage, and all-around burden expanded in the stripped-down Boston lineup and produced additional rebound opportunity
- Signal classification: Under-filter failure

### Keon Ellis Over 6.5 points
- Final: 13
- Clean win from alt-threshold capture
- Signal classification: Threshold win

## What the game told us
1. The over-side read on Jalen Johnson remained strong and validated the rebound-over workflow.
2. The under-side reads on Boston secondary rebounders were too fragile because the Celtics were operating in a heavily distorted lineup environment.
3. Role compression increased Boston rebound concentration instead of diffusing it.
4. Luka Garza’s 9 rebounds and Brown’s 10 rebounds both reinforced that emergency frontcourt and star-burden conditions can inflate board outcomes even when baseline defensive rebound assumptions suggest otherwise.

## Model lessons
### Validated
- Rebound-over engine remains the stronger side of the workflow
- Role-concentrated forwards in unstable opponent frontcourts remain strong targets

### Failed
- Under filters need stronger suppression rules when:
  - the lineup is missing stabilizing frontcourt pieces
  - star wings absorb expanded all-around load
  - replacement bigs and hybrid lineups create rebound volatility

## Patch recommendations
- Add an UNDER_SUPPRESSION_FAILSAFE when roster instability raises rebound redistribution uncertainty
- Apply a STAR_LOAD_REBOUND_BOOST when shot volume and on-ball responsibility both increase in thin lineups
- Downgrade unders when frontcourt absences force non-standard rebounding assignments

## Verdict
This was a split audit with one strong structural over hit and two meaningful under misses.
The key lesson is that the current workflow is much stronger at identifying rebound-over expansion spots than it is at safely attacking rebound unders inside distorted lineups.

## Tags
- EDGE_CALL_ACTIVE
- REB_OVER_ENGINE_ACTIVE
- UNDER_FILTER_WEAKNESS
- ROLE_DISTORTION_ACTIVE
- STAR_LOAD_REBOUND_BOOST_NEEDED
