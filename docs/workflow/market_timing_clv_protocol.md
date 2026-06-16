# SharpEdge Workflow Protocol — Market Timing + CLV

**Effective Date:** 2026-06-16  
**System:** DBst-23 / MLB Betting Model  
**Module:** Strikeout Edge Hunting / Kalshi + Sportsbook Market Comparison

---

## Purpose

Market Timing and CLV are now formal SharpEdge workflow fields for every pitcher strikeout investment.

The goal is to separate:

- good process with bad variance
- bad process with lucky results
- real market edge from isolated win/loss noise

A wager can lose and still be graded as a strong process ticket if it beats the closing market. A wager can win and still receive a weak process grade if the entry was worse than market close.

---

## Required Fields For Every K Investment

```yaml
MarketTiming:
  Opening_Odds:
  Entry_Odds:
  Secondary_Market_Check:
  Closing_Odds:
  CLV_Cents:
  CLV_Implied_Probability_Delta:
  Beat_Close: true/false
  Market_Inflation_Detected: true/false
  Timing_Grade:
```

---

## CLV Calculation Rules

### American Odds Implied Probability

For negative odds:

```text
Implied Probability = abs(odds) / (abs(odds) + 100)
```

For positive odds:

```text
Implied Probability = 100 / (odds + 100)
```

### CLV Cents

For a YES / Over strikeout position:

```text
CLV_Cents = Closing_Odds - Entry_Odds, adjusted directionally for bettor value
```

Examples:

| Entry | Close | CLV Result |
|---:|---:|---|
| -117 | -129 | Positive CLV, beat close |
| -117 | -121 | Positive CLV, beat close |
| +123 | +105 | Positive CLV, beat close |
| +123 | +145 | Negative CLV, market improved after entry |

---

## Positive CLV Thresholds

| CLV Band | Meaning | Workflow Tag |
|---|---|---|
| +1 to +4 cents | Minor confirmation | `CLV_MINOR_POSITIVE` |
| +5 to +9 cents | Good timing | `CLV_CONFIRMED` |
| +10 to +19 cents | Strong timing | `CLV_STRONG` |
| +20+ cents | Major market beat | `CLV_STEAM_CAPTURED` |

---

## Negative CLV Thresholds

| CLV Band | Meaning | Workflow Tag |
|---|---|---|
| -1 to -4 cents | Minor drift | `CLV_MINOR_NEGATIVE` |
| -5 to -9 cents | Timing concern | `CLV_WARNING` |
| -10 to -19 cents | Market moved against us | `CLV_NEGATIVE_STRONG` |
| -20+ cents | Bad timing / stale price | `CLV_FAIL` |

---

## Workflow Rule Patch

```yaml
rule_patch_market_timing_clv:
  name: "Market Timing CLV Confirmation"
  applies_to:
    - pitcher_strikeout_props
    - Kalshi_yes_markets
    - sportsbook_comparison_markets
  pregame_required:
    - capture_entry_odds
    - capture_comparison_market_odds_when_available
    - record implied_probability_at_entry
  post_entry_required:
    - compare_entry_to_best_available_market
    - classify_clv_band
    - update ticket grade before final result
  postgame_required:
    - include CLV in postmortem
    - grade process separately from result
```

---

## Example: 2026-06-16 Active Tickets

```yaml
active_positions_2026_06_16:
  gerrit_cole_6_plus:
    market: "Gerrit Cole 6+ Strikeouts"
    entry_book: Kalshi
    entry_odds: -117
    comparison_book: WilliamHill
    comparison_odds: -129
    clv_cents: +12
    implied_probability_entry: 53.9%
    implied_probability_comparison: 56.3%
    implied_probability_delta: +2.4%
    beat_close: true
    clv_tag: CLV_STRONG
    timing_grade: A

  framber_valdez_5_plus:
    market: "Framber Valdez 5+ Strikeouts"
    entry_book: Kalshi
    entry_odds: -117
    comparison_book: WilliamHill
    comparison_odds: -121
    clv_cents: +4
    implied_probability_entry: 53.9%
    implied_probability_comparison: 54.8%
    implied_probability_delta: +0.9%
    beat_close: true
    clv_tag: CLV_MINOR_POSITIVE
    timing_grade: B+
```

---

## Updated Postmortem Grading Structure

Every postmortem should now grade two separate categories:

```yaml
PostmortemGrade:
  Result_Grade:
  Process_Grade:
  Market_Timing_Grade:
  Projection_Accuracy_Grade:
  Final_SharpEdge_Grade:
```

### Interpretation

| Scenario | Grade Logic |
|---|---|
| Win + positive CLV | Strongest confirmation |
| Loss + positive CLV | Good process, negative variance |
| Win + negative CLV | Lucky result, review timing/model |
| Loss + negative CLV | Full review required |

---

## Execution Notes

1. Price capture should happen immediately after target ranking.
2. If multiple books are shown, compare Kalshi to the sharpest available market.
3. If Kalshi is better than sportsbook price, log it as positive CLV / market advantage.
4. If sportsbooks are better after entry, flag market drift.
5. Never evaluate a ticket by result alone.

---

## SharpEdge Command

From this point forward:

```yaml
workflow_command:
  every_locked_ticket_must_include:
    - entry_odds
    - comparison_market_odds
    - implied_probability
    - CLV_cents
    - Beat_Close flag
    - Market_Timing_Grade
```

This protocol is now part of the standard DBst-23 MLB strikeout edge hunting workflow.
