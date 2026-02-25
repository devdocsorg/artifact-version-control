# Checklist Sub-Machine: Data Sources Explained

**Parent:** [Engineering Review: UI Reference](../engineering/ui-reference-review.md)  
**Reviewer:** Developer  
**Global outcome on FAIL:** `Dev_decision → ISSUES_FOUND → BACK_TO_DRAFTING`  
**Global outcome on PASS:** Advances to next check (`Actions Documented?`)

---

## The Question

> For every piece of data displayed in the UI, does the documentation explain where it
> comes from, how it's calculated, and how often it updates?

## Sub-State Machine

```
[START: Data Sources Explained?]
    │
    ▼
┌──────────────────────────────┐
│ Inventory Displayed Data     │  List every data field, metric, count, chart
│ (fields, metrics, charts,    │  shown in the documented UI
│  tables, status indicators)  │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Source Attribution     │  Is the origin of each data point explained?
│ (ATTRIBUTED | UNEXPLAINED)   │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Calculation Logic      │  For computed values, is the formula or logic
│ (EXPLAINED | OPAQUE)         │  described?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Refresh / Staleness    │  How often does the data update?
│ (STATED | AMBIGUOUS)         │  Is there a lag? Can the user force refresh?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Data Accuracy Caveats  │  Are known approximations, sampling, or
│ (DISCLOSED | HIDDEN)         │  limitations noted?
└────────┬─────────────────────┘
         │
         ▼
[AGGREGATE] ──→ PASS or FAIL
```

## What the Reviewer Looks For

### 1. Inventory Displayed Data
- List every number, date, status, chart, table, count, and metric on the documented screens
- Include both primary data (explicit fields) and derived indicators (badges, color coding, progress bars)
- **Diff viewer:** **Preview (rendered)** — identify all data display elements.

### 2. Source Attribution
- For each data point: where does it come from? (user input, API, calculated, third-party)
- Is it clear which system of record owns this data?
- Example: "Total Revenue" — is this from Stripe? Calculated internally? From a report?
- **Diff viewer:** **Source (read-through)** — check descriptions near data fields.

### 3. Calculation Logic
- For aggregated/computed values: how is it calculated?
- "Active Users" — active in the last 7 days? 30 days? Currently logged in?
- "Conversion Rate" — what's the numerator and denominator?
- Are rounding rules mentioned?
- **Diff viewer:** **Changes (diff)** — new metrics should include calculation definitions.

### 4. Refresh and Staleness
- How often does displayed data update? (real-time, every 5 min, daily batch)
- Is there a "last updated" indicator documented?
- Can the user manually refresh?
- What does the user see during a refresh cycle?
- **Diff viewer:** **Source (read-through)** — look for temporal language about data.

### 5. Data Accuracy Caveats
- Are there known approximations? ("Estimated count, may differ by ±5%")
- Is data sampled rather than exhaustive?
- Are timezone effects mentioned? (UTC vs. local)
- Are there delays between action and data reflection?

## Pass / Fail Criteria

| Verdict | Condition |
|---------|-----------|
| **PASS** | Every displayed data element has its source identified, computed values have their logic explained, refresh frequency is stated, and known limitations are disclosed |
| **FAIL** | Data appears on screen with no explanation of where it comes from, metrics lack definitions, update frequency is unstated, or known inaccuracies are hidden |

## Failure Feedback Template

```
❌ Data Sources Explained: FAIL

[file.md, "Analytics Dashboard"] — Unexplained metric:
  "Monthly Active Users" is displayed but never defined.
  What counts as "active"? What's the time window?

[file.md, "Billing" section] — Missing refresh info:
  Usage data shown in the billing panel — is this real-time
  or delayed? Users will be confused if it doesn't match
  their recent activity.

[file.md, "Reports"] — Hidden limitation:
  Report data is sampled at 10% for accounts with >1M events.
  This is not mentioned — users will wonder why numbers
  don't match their raw data exports.
```
