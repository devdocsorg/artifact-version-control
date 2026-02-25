# Checklist Sub-Machine: UX Components Accurate

**Parent:** [Engineering Review: UI Reference](../engineering/ui-reference-review.md)  
**Reviewer:** Developer  
**Global outcome on FAIL:** `Dev_decision → ISSUES_FOUND → BACK_TO_DRAFTING`  
**Global outcome on PASS:** Advances to next check (`Error States Documented?`)

---

## The Question

> Do the UI components described in the documentation match what actually exists
> in the product right now?

## Sub-State Machine

```
[START: UX Components Accurate?]
    │
    ▼
┌─────────────────────────────┐
│ Inventory Described          │  List every UI element the doc references
│ Components                   │
│ (buttons, fields, tabs, etc) │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│ Cross-Reference with        │  Does each described component exist in the UI?
│ Actual UI                   │
│ (ALL_EXIST | ORPHANED_REFS) │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│ Check Labels & Copy         │  Do button labels, field names, menu items
│ (MATCH | MISMATCH)          │  match the actual UI text?
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│ Check Layout Description    │  Is the spatial relationship described correctly?
│ (ACCURATE | MISLEADING)     │  ("below the header", "in the sidebar")
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│ Check Screenshots Current   │  Do screenshots match the live product?
│ (CURRENT | STALE)           │
└────────┬────────────────────┘
         │
         ▼
[AGGREGATE] ──→ PASS or FAIL
```

## What the Reviewer Looks For

### 1. Inventory Described Components
- List every button, field, tab, menu, toggle, dropdown, link, icon the doc references
- Note which are new (added in this PR) vs. existing
- **Diff viewer:** **Changes (diff)** — identify which UI components are newly documented.

### 2. Cross-Reference with Actual UI
- Open the product screen alongside the doc
- Does every component the doc describes actually exist?
- Are there components on the screen that the doc doesn't mention?
- Has anything been renamed, moved, or removed since the doc was written?
- **Diff viewer:** **Preview (rendered)** alongside the actual product.

### 3. Labels and Copy
- Does the doc say "Click **Save**" when the button actually says "**Submit**"?
- Are field labels exactly right? ("Email Address" vs "Email" matters)
- Do menu paths match? ("Settings > Advanced > API Keys" — does that path exist?)
- **Diff viewer:** **Source (read-through)** — bold/quoted text should match the UI literally.

### 4. Layout Description
- If the doc says "in the top-right corner," is it actually there?
- If the doc describes a tab order (General, Advanced, Security), is that the real order?
- Are navigation instructions accurate? ("Click the gear icon in the sidebar")
- **Diff viewer:** **Before/After (compare)** — did layout descriptions change correctly with the UI change?

### 5. Screenshot Currency
- Do screenshots show the current UI, not a mockup or old version?
- Are screenshots from the right environment (production, not staging)?
- Do screenshots show the right user role (admin vs. regular user)?
- Are annotations/callouts pointing to the right elements?

## Pass / Fail Criteria

| Verdict | Condition |
|---------|-----------|
| **PASS** | Every described UI component exists in the product, labels match exactly, layout descriptions are accurate, and screenshots are current |
| **FAIL** | Doc references components that don't exist, uses wrong labels, describes a different layout, or shows outdated screenshots |

## Failure Feedback Template

```
❌ UX Components Accurate: FAIL

[file.md, "Dashboard" section] — Wrong label:
  Doc says: Click the "Generate Report" button
  Actual:   Button is labeled "Export Report"

[file.md, screenshot on line 45] — Stale screenshot:
  Screenshot shows old sidebar design. The sidebar was
  redesigned in v4.2 — new screenshot needed.

[file.md, "Settings" section] — Orphaned reference:
  Doc describes a "Notifications" tab that was removed in v4.0.
  This tab no longer exists.
```
