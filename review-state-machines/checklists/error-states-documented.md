# Checklist Sub-Machine: Error States Documented

**Parent:** [Engineering Review: UI Reference](../engineering/ui-reference-review.md)  
**Reviewer:** Developer  
**Global outcome on FAIL:** `Dev_decision → ISSUES_FOUND → BACK_TO_DRAFTING`  
**Global outcome on PASS:** Advances to next check (`Data Sources Explained?`)

---

## The Question

> Are all the ways the UI can go wrong — error messages, validation failures, empty states,
> loading states, permission denials — documented so the user isn't surprised?

## Sub-State Machine

```
[START: Error States Documented?]
    │
    ▼
┌─────────────────────────────┐
│ Identify UI Error Points    │  Where can errors surface in this UI?
│ (forms, API calls, auth,    │
│  data loading, permissions) │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│ Check Validation Errors     │  Are form/input validation errors documented?
│ (COVERED | MISSING)         │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│ Check Empty States          │  What does the user see when there's no data?
│ (DOCUMENTED | INVISIBLE)    │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│ Check Permission Errors     │  What if the user lacks access?
│ (DOCUMENTED | IGNORED)      │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│ Check Loading / Timeout     │  What happens during slow loads or failures?
│ States                      │
│ (DOCUMENTED | IGNORED)      │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│ Check Error Recovery        │  Does the doc tell the user what to do about it?
│ Guidance                    │
│ (PROVIDED | MISSING)        │
└────────┬────────────────────┘
         │
         ▼
[AGGREGATE] ──→ PASS or FAIL
```

## What the Reviewer Looks For

### 1. Identify UI Error Points
- Map every location where the UI can show an error state
- Form submissions, API-driven data loads, file uploads, authentication checks
- **Diff viewer:** **Source (read-through)** — identify all interactive elements, then ask "what if this fails?"

### 2. Validation Errors
- Are required field indicators documented?
- What happens when the user enters invalid data? (email format, character limits, type mismatches)
- Are specific validation rules stated? ("Password must be 8+ characters with one number")
- Are inline error message texts shown?
- **Diff viewer:** **Changes (diff)** — new form fields should come with validation documentation.

### 3. Empty States
- What does a dashboard/list/table look like before any data exists?
- Is there a first-time user experience described?
- What shows when a search returns zero results?
- **Diff viewer:** **Preview (rendered)** — look for "empty state" mentions or screenshots.

### 4. Permission Errors
- What does a non-admin see on an admin-only page?
- Are role-based feature restrictions documented?
- What message does the user get when denied access?
- Are instructions for requesting access provided?

### 5. Loading and Timeout States
- Does the doc mention what happens during long operations?
- Are timeout behaviors documented? (auto-retry? error banner? redirect?)
- What does the user see while data is loading?

### 6. Error Recovery Guidance
- For each documented error, is there a "what to do" instruction?
- Refresh the page? Contact admin? Check network? Wait and retry?
- Is there an escalation path (support link, error code to report)?

## Pass / Fail Criteria

| Verdict | Condition |
|---------|-----------|
| **PASS** | All error-producing UI paths are documented with the exact error messages, empty states are described, permission errors are covered, and each error includes recovery guidance |
| **FAIL** | The doc only shows the happy path. Errors, empty states, or permission issues are ignored or missing recovery guidance |

## Failure Feedback Template

```
❌ Error States Documented: FAIL

[file.md, "Create Project" form] — Missing validation errors:
  Form has 5 required fields but the doc doesn't describe
  what happens when they're left blank or filled incorrectly.

[file.md, "Dashboard"] — Missing empty state:
  No description of what a new user sees before creating
  their first project. This is the #1 first-time user experience.

[file.md, "API Keys" section] — Missing permission error:
  Only admins can see this tab. No mention of what regular
  users see or how they request access.
```
