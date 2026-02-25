# Engineering Review: UI Reference

**Reviewer:** Developer (Engineer who built or owns the feature)  
**Doc Type:** UI Reference — screen-by-screen docs, component libraries, admin panels  
**Entry:** `DOC_TYPE_UI_REFERENCE` from `Dev_selectDocType`  
**Exit:** Returns verdict to `Dev_decision` in [GLOBAL.md](../GLOBAL.md)

## State Machine

```
[DOC_TYPE_UI_REFERENCE]
    │
    ▼
┌──────────────────────────┐
│ UX Components Accurate?  │──→ see ../checklists/ux-components-accurate.md
│ (PASS | FAIL + notes)    │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Error States Documented? │──→ see ../checklists/error-states-documented.md
│ (PASS | FAIL + notes)    │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Data Sources Explained?  │──→ see ../checklists/data-sources-explained.md
│ (PASS | FAIL + notes)    │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Actions Documented?      │──→ see ../checklists/actions-documented.md
│ (PASS | FAIL + notes)    │
└────────┬─────────────────┘
         │
         ▼
[CHECKLIST_COMPLETE] ──→ Dev_decision
```

## Aggregation → Dev_decision

```
IF any check returned FAIL:
    Dev_decision = ISSUES_FOUND
ELSE:
    Dev_decision = ALL_PASSED
```

## What Makes UI Reference Docs Special

UI Reference docs are **descriptive** — they describe what the user sees and can do on
each screen. The engineering reviewer verifies that the descriptions match the actual
product UI. This is the most screenshot-heavy doc type and the one most likely to go
stale when the UI changes.

**Core question:** "If a user is staring at this screen, does the doc accurately describe
everything they see and everything they can do?"

## Diff Viewer Strategy

| Check | Primary View | What to Look For |
|-------|-------------|------------------|
| UX Components Accurate | **Before/After (compare)** | Do described components still exist in the UI? |
| UX Components Accurate | **Preview (rendered)** | Do screenshots match current product? |
| Error States Documented | **Source (read-through)** | Are validation errors, empty states, permission errors covered? |
| Error States Documented | **Changes (diff)** | Were new error states added with the feature change? |
| Data Sources Explained | **Source (read-through)** | For each data field shown, is the source identified? |
| Actions Documented | **Source (read-through)** | For each button/link/control, is behavior documented? |
| Actions Documented | **Changes (diff)** | Were new actions added that match the feature change? |

## Common Failure Patterns

1. **Stale screenshots** — UI redesign happened but screenshots are old
2. **Missing fields** — new field added to form but not documented
3. **Wrong labels** — doc says "Submit" but button actually says "Save"
4. **Undocumented states** — describes the happy state, not loading/empty/error
5. **Permission blindness** — describes admin view but user sees different UI
6. **Orphaned references** — mentions a button/tab that was removed
