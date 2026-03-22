# LIVEFLOW DEFENSE SYSTEM V1

Date deployed: 2026-03-21
Sport: NBA

## Objective
Block fragile LiveFlow bets and protect bankroll from inflation traps, noisy rebound props, and weak single-signal reads.

## Modules

### 1. Efficiency Trap Detector
Do not play a live under only because the live total is far above the closing total.

Require at least two of these confirmations:
- 3PT regression signal
- shot quality decline
- fatigue or minutes strain
- turnover spike
- halfcourt slowdown

Block the bet when:
- both teams are still creating clean offense
- both teams remain highly efficient
- bench units are sustaining tempo

Source: LAC @ DAL on 2026-03-21.

### 2. Guard Rebound Volatility Filter
Avoid guard rebound props at 3.5 or below unless role and minutes are clearly stable.

Block when:
- the guard is a low-board role player
- the prop sits on a hook line
- the edge depends only on first-half pace

Source: LAL @ ORL on 2026-03-21.

### 3. Mid-Range Rebound Dead Zone Blocker
Avoid live rebound props in the 5.5 to 7.5 range unless there is a strong minutes cap, foul pressure, or role collapse signal.

Source: CLE @ NOP on 2026-03-21.

### 4. Blowout Dampener Rule
Approve live unders when a stronger team is likely to slow the game late through scoreboard control and rebounding dominance.

Source: OKC @ WAS on 2026-03-21.

### 5. Pace Suppression Confirmation
Upgrade live unders when first-half scoring appears inflated by hot shooting, transition bursts, or unstable foul rate.

Source: LAL @ ORL and CLE @ NOP on 2026-03-21.

### 6. Stake Governor
Maximum sizing:
- A edge with multiple confirmations: 0.75u
- B edge with two confirmations: 0.50u
- C edge with one confirmation: 0.25u
- Blocked market: 0u

Special limits:
- guard rebound props: 0.20u max
- inflation-only totals: 0.25u max
- no more than 2 correlated live unders in one segment

## Hard Blocks
- no live under on inflation alone
- no live guard rebound prop at 3.5 or lower without role confirmation
- no rebound dead-zone play without a structural trigger

## Preferred Targets
- blowout-adjusted live totals
- pace suppression totals
- frontcourt rebound props with secure minutes
- live numbers drifting far beyond close with visible efficiency decay
