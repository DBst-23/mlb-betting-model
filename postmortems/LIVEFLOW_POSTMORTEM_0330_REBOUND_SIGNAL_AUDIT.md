# LIVE-FLOW POSTMORTEM — 03/30 REBOUND SIGNAL AUDIT

## Objective
Audit SharpEdge pregame + LiveFlow rebound workflow against actual game outcomes to measure alignment between:
- ON/OFF role signals
- projected minutes
- rebound environment reads
- market movement / line capture
- final stat outcomes

---

## CORE TAKEAWAY

The workflow showed strong alignment on **rebound overs** and **early line-capture identification**.

Best examples:
- Kyle Filipowski Over 7.5 REB ✅
- Evan Mobley Over 9.5 REB ✅
- Jalen Johnson Over 8.5 REB ✅
- James Harden Over 4.5 REB ✅

Weakness appeared on:
- Jaylen Brown Under 7.5 REB ❌
- Derrick White Under 4.5 REB ❌

Initial conclusion:
**SharpEdge is currently strongest at detecting true rebound expansion and soft over lines.**
Unders remain more fragile in volatile redistribution environments.

---

## MATCHUP 1 — CLE @ UTA

### SharpEdge pregame read
- Mobley rebound environment was strong
- Filipowski rebound role remained viable even into tougher matchup
- Market later validated the read:
  - Filipowski line moved from 7.5 to 8.5
  - Sharp books pushed Mobley toward 10.5

### Actual outcomes
- Evan Mobley Over 9.5 REB ✅ — finished 15
- Kyle Filipowski Over 7.5 REB ✅ — finished 10
- James Harden Over 4.5 REB ✅ — finished 5
- Keon Ellis Over 6.5 PTS ✅ — finished 10

### Audit verdict
**Excellent alignment**
- Minutes + role + environment + market confirmation all pointed in the correct direction
- This is the model’s cleanest win condition profile

### Tags
- EDGE_CALL_ACTIVE
- ANCHOR_OVER_VALIDATED
- MARKET_BEAT_CONFIRMED
- ROLE_EXPANSION_CONFIRMED

---

## MATCHUP 2 — BOS @ ATL

### SharpEdge pregame read
- Boston lineup instability created a thin frontcourt
- Unders were identified on rebound concentration assumptions:
  - Jaylen Brown Under 7.5 REB
  - Derrick White Under 4.5 REB
- Jalen Johnson Over 8.5 REB remained a strong board concentration signal

### Actual outcomes
- Jalen Johnson Over 8.5 REB ✅ — finished 12
- Jaylen Brown Under 7.5 REB ❌ — finished 10
- Derrick White Under 4.5 REB ❌ — finished 5

### Audit verdict
**Mixed**
- Johnson over was correctly identified
- Boston under logic failed because rebound vacuum consolidated more heavily than expected
- White miss was a hook / threshold issue
- Brown miss was a true structural miss

### Tags
- EDGE_CALL_ACTIVE
- UNDER_FRAGILITY_EXPOSED
- REBOUND_VACUUM_MISS
- HOOK_BURN
- ROLE_REDISTRIBUTION_FAILURE

---

## MARKET TIMING AUDIT

### Confirmed wins on number capture
- Filipowski O7.5 → later moved to 8.5
- Jalen Johnson O8.5 → later moved to 9.5
- Mobley sharp market drift → normal line pushed toward 10.5
- Keon Ellis alt-ladder to 6.5 captured well below market’s standard 8.5

### Conclusion
SharpEdge is not only finding direction well — it is increasingly finding **the right threshold before the market fully adjusts**.

### Tags
- CLV_WIN
- THRESHOLD_CAPTURE
- EARLY_SIGNAL_VALIDATED

---

## SYSTEM INSIGHTS

### What is working best
1. ON/OFF rebound role identification
2. Projected minutes integration
3. Early market scan before line inflation
4. Rebound-over environment mapping
5. Ladder-down alt construction when market standard line is higher

### What needs refinement
1. Rebound unders in unstable rotation contexts
2. Late frontcourt redistribution handling
3. Small-lineup rebound vacuum penalty
4. Hook protection on under calls

---

## SHARPEDGE REBOUND ENGINE STATUS

### Current best use-case
**Anchor / strong-secondary rebound overs**

### Current caution zone
**Rebound unders when lineup instability creates hidden consolidation**

### Provisional rule update
Only fire rebound unders when:
- board share is clearly capped
- no rebound vacuum exists
- late lineup changes do not force role concentration
- most likely exact result is at least 1 full rebound below line

---

## FINAL JUDGMENT

The 03/30 cycle strongly suggests the workflow is real.
The strongest version of SharpEdge currently functions as:

**A rebound-over and number-capture engine first.**

The process is producing:
- true role signals
- actionable thresholds
- early market wins
- repeatable edge patterns

Next development focus:
**tighten under filters without weakening the over engine.**
