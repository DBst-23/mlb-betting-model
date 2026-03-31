# POSTMORTEM — 03/30 CLE @ UTA REBOUND SIGNAL AUDIT

## Summary
- Matchup: Cavaliers @ Jazz
- Final score: Cavaliers 122, Jazz 113
- Focus: rebound signal alignment and pregame threshold validation

## Pre-workflow signals audited
- Evan Mobley Over 9.5 rebounds
- Kyle Filipowski Over 7.5 rebounds
- James Harden Over 4.5 rebounds
- Keon Ellis Over 6.5 points

## Final outcomes
- Evan Mobley: 17 rebounds — Win
- Kyle Filipowski: 10 rebounds — Win
- James Harden: 6 rebounds — Win
- Keon Ellis: 13 points — Win

## Team environment outcome
- Cleveland rebounds: 49
- Utah rebounds: 40
- Offensive rebounds: tied 11 to 11
- Cleveland paint points: 82
- Utah made threes: 15 of 29

## Signal review
### Evan Mobley Over 9.5 rebounds
- Final: 17
- Clear smash
- Rebound role, minutes, and frontcourt environment all aligned correctly
- Signal classification: Anchor

### Kyle Filipowski Over 7.5 rebounds
- Final: 10
- Cleared with room despite difficult matchup
- Signal classification: Strong secondary

### James Harden Over 4.5 rebounds
- Final: 6
- Cleared above line without needing extreme variance
- Signal classification: Strong secondary

### Keon Ellis Over 6.5 points
- Final: 13
- Laddered down from normal 8.5 line and captured strong value band
- Signal classification: Smart threshold capture

## Model alignment notes
- The workflow correctly identified rebound expansion spots better than the market's early numbers
- Mobley and Filipowski both validated the rebound-over engine
- Harden confirmed the supporting rebound role read
- Keon Ellis validated the alt-threshold approach when the standard line was higher

## Market timing notes
- Filipowski line later moved from 7.5 to 8.5
- Sharp books pushed Mobley toward 10.5
- Keon Ellis standard line was 8.5 while ladder entry was 6.5
- This cycle showed strong threshold capture and favorable market timing

## Verdict
This was one of the strongest pregame validation cycles so far.
The rebound-over engine aligned closely with actual outcomes, and the threshold selection process added clear value.

## Tags
- EDGE_CALL_ACTIVE
- REB_OVER_ENGINE_ACTIVE
- THRESHOLD_CAPTURE
- MARKET_BEAT_CONFIRMED
- MODEL_ALIGNMENT_STRONG
