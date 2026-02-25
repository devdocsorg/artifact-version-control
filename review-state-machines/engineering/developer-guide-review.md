# Engineering Review: Developer Guide

**Reviewer:** Developer (Engineer who built or owns the feature)  
**Doc Type:** Developer Guide — tutorials, getting-started, integration guides, SDK docs  
**Entry:** `DOC_TYPE_DEVELOPER_GUIDE` from `Dev_selectDocType`  
**Exit:** Returns verdict to `Dev_decision` in [GLOBAL.md](../GLOBAL.md)

## State Machine

```
[DOC_TYPE_DEVELOPER_GUIDE]
    │
    ▼
┌─────────────────────────┐
│ Code Tested?            │──→ see ../checklists/code-tested.md
│ (PASS | FAIL + notes)   │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│ Explanations            │──→ see ../checklists/explanations-comprehensive.md
│ Comprehensive?          │
│ (PASS | FAIL + notes)   │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│ Debugging Steps Clear?  │──→ see ../checklists/debugging-steps-clear.md
│ (PASS | FAIL + notes)   │
└────────┬────────────────┘
         │
         ▼
[CHECKLIST_COMPLETE] ──→ Dev_decision
```

## Aggregation → Dev_decision

```
IF any check returned FAIL:
    Dev_decision = ISSUES_FOUND
    → Collect all FAIL notes into a single PR review
    → Developer: Request Changes → GITHUB_requestChanges → BACK_TO_DRAFTING
ELSE:
    Dev_decision = ALL_PASSED
    → Developer: Approve → GITHUB_devApprove → ENG_APPROVED
```

**Best practice:** Complete ALL checks even after the first failure. The writer gets
one comprehensive round of feedback rather than piecemeal rejections.

## What Makes Developer Guides Special

Developer guides are **instructional** — they walk someone through doing something.
The engineering reviewer verifies the instructions *actually work* and are *technically
correct*. This is fundamentally different from UI Reference (describing what exists)
or User Workflow (describing how features connect).

**Core question:** "Could a developer follow these instructions and succeed on the first try?"

## Diff Viewer Strategy

| Check | Primary View | What to Look For |
|-------|-------------|------------------|
| Code Tested | **Changes (diff)** | Modified code samples, new imports, changed API calls |
| Code Tested | **Source (read-through)** | Follow the tutorial steps end-to-end mentally |
| Explanations Comprehensive | **Source (read-through)** | Read for gaps in reasoning, undefined terms |
| Explanations Comprehensive | **Preview (rendered)** | Check that context flows visually |
| Debugging Steps Clear | **Source (read-through)** | Can you follow the troubleshooting path? |
| Debugging Steps Clear | **Changes (diff)** | Verify error messages/codes match reality |

## Common Failure Patterns

1. **Stale code samples** — API changed but example wasn't updated
2. **Missing prerequisites** — assumes packages/tools are installed
3. **Wrong output shown** — expected output doesn't match what actually happens
4. **Skipped error handling** — happy path only, no mention of what can go wrong
5. **Version mismatch** — code works on v2 but doc says v1
