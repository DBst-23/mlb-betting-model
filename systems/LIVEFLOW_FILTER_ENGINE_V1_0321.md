# LIVEFLOW FILTER ENGINE V1

Date activated: 2026-03-21
Sport: NBA

## Objective
Convert LiveFlow reads into a clear three-state engine:
- FIRE
- CAUTION
- BLOCK

This engine sits on top of the LiveFlow Defense System and standardizes real-time decision grading before execution.

## Decision States

### FIRE
A market is approved only when:
- at least 2 structural signals agree
- no hard block is active
- stake governor allows exposure

Examples:
- live total inflated well above close plus visible efficiency decay
- blowout drag setup with rebounding dominance
- frontcourt rebound prop with stable minutes and clean share edge

### CAUTION
A market is monitor-only when:
- only 1 useful signal is present
- role or minute stability is not fully confirmed
- hook risk is meaningful
- correlation exposure is already elevated

Examples:
- live total with inflation but no visible shot-quality drop
- rebound prop with fair edge but uncertain 2H minutes
- low-threshold guard prop with decent angle but noisy path

### BLOCK
A market is rejected when any hard block is active.

Hard blocks include:
- inflation-only under with no decay signal
- guard rebound props at 3.5 or lower without elite role confirmation
- rebound dead-zone plays with no foul, minutes, or role trigger
- oversized correlated exposure

## Core Filters

### 1. Total Market Filter
FIRE when:
- live total is at least 10 points above close
- and either shooting regression, pace suppression, or blowout drag is visible

CAUTION when:
- total is inflated but both teams are still creating efficient offense

BLOCK when:
- inflation is the only reason for the bet

### 2. Rebound Prop Filter
FIRE when:
- player is frontcourt
- projected remaining minutes are stable
- rebound share is clearly above market line needs
- no dead-zone trap is active

CAUTION when:
- player is a wing or hybrid role
- rebound chances are present but distributed

BLOCK when:
- player is a guard on a low threshold line
- the edge depends only on current box score count

### 3. Correlation Filter
FIRE when:
- total exposure is isolated
- player prop is independent enough from other live positions

CAUTION when:
- same-game correlation is present but stake remains small

BLOCK when:
- multiple live totals or same-game rebound props stack on the same script

### 4. Stake Filter
Stake limits:
- FIRE: up to 0.75u if multi-signal
- CAUTION: up to 0.25u to 0.50u depending on signal quality
- BLOCK: 0u

Additional limits:
- guard rebound props max 0.20u when allowed
- inflation-only totals max 0.25u
- no more than 2 correlated live unders in the same segment

## Operator Output Format
Every LiveFlow read should end in this structure:
- Decision: FIRE / CAUTION / BLOCK
- Market type: total / rebound / spread
- Edge class: A / B / C
- Why: short trigger summary
- Stake cap: allowed max

## Calibration Sources
- NBA_POSTMORTEM_0321_BATCH1
- NBA_POSTMORTEM_0321_BATCH2
- LIVEFLOW_DEFENSE_SYSTEM_V1_0321

## Summary
This engine turns loose live reads into a consistent execution gate. It is designed to remove emotional firing, hook chasing, and inflation-only mistakes while preserving strong multi-signal edges.
