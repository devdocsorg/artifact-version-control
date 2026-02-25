# Checklist Sub-Machine: Feature Contextualized

**Parent:** [Engineering Review: User Workflow](../engineering/user-workflow-review.md)  
**Reviewer:** Developer  
**Global outcome on FAIL:** `Dev_decision → ISSUES_FOUND → BACK_TO_DRAFTING`  
**Global outcome on PASS:** Advances to next check (`Comprehensive vs Other Features?`)

---

## The Question

> Is this feature placed within the broader context of the user's journey? Does the
> reader understand when, why, and where they would encounter this feature?

## Sub-State Machine

```
[START: Feature Contextualized?]
    │
    ▼
┌──────────────────────────────┐
│ Check "When" Context         │  At what point in the user journey does
│ (CLEAR | UNCLEAR)            │  this feature become relevant?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check "Why" Motivation       │  What user problem does this feature solve?
│ (STATED | ASSUMED)           │  Is the motivation explicit?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Entry Points           │  How does the user get to this feature?
│ (MAPPED | VAGUE)             │  Are all navigation paths described?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Exit Points            │  Where does the user go after this feature?
│ (MAPPED | DEAD_END)          │  What's the next logical step?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check User Persona Fit       │  Is it clear which user this workflow is for?
│ (TARGETED | GENERIC)         │
└────────┬─────────────────────┘
         │
         ▼
[AGGREGATE] ──→ PASS or FAIL
```

## What the Reviewer Looks For

### 1. "When" Context
- Does the doc explain when in the user journey this feature matters?
- Is there a "before you start" that situates the reader in time? ("After deploying your app..." or "During the initial setup...")
- Is the trigger clear? What event causes the user to need this feature?
- **Diff viewer:** **Source (read-through)** — check the introduction paragraph.

### 2. "Why" Motivation
- Is the user problem stated explicitly?
- Not just "how to use feature X" but "when you need to Y, use feature X"
- Does the doc connect the feature to a business or technical outcome?
- **Diff viewer:** **Source (read-through)** — look for problem-statement or use-case language.

### 3. Entry Points
- How does the user navigate to this feature? (menu path, URL, CLI command, API call)
- Are all entry points documented? (e.g., feature accessible from sidebar AND from a deep link)
- Are context-dependent entry points noted? ("This option only appears after enabling X")
- **Diff viewer:** **Changes (diff)** — new entry points should be documented with the feature.

### 4. Exit Points
- Where does the user go next after completing this workflow?
- Are "next steps" or "related" links provided?
- Does the doc avoid dead-ending the reader on a page with no forward navigation?
- **Diff viewer:** **Source (read-through)** — check the end of the doc for continuation guidance.

### 5. User Persona Fit
- Is the target user identified? (admin, developer, end-user, new user, power user)
- Are role-specific variations noted?
- Would the wrong user be confused reading this? (e.g., a developer reading an end-user workflow)

## Pass / Fail Criteria

| Verdict | Condition |
|---------|-----------|
| **PASS** | The feature's place in the user journey is clear: when they need it, why they need it, how to get to it, and where to go next. Target persona is identifiable |
| **FAIL** | The doc jumps straight into feature mechanics without explaining context, motivation, navigation, or who this is for |

## Failure Feedback Template

```
❌ Feature Contextualized: FAIL

[file.md] — Missing motivation:
  Doc opens with "To configure webhooks, go to Settings > Webhooks."
  But never explains WHEN a user would need webhooks or WHAT
  problem they solve. A new user has no idea if they need this.

[file.md] — No entry points documented:
  How does the user navigate to this feature? There are 3 ways
  (sidebar, settings, API) but the doc mentions none.

[file.md] — Dead-end:
  After completing the webhook setup, there's no "next steps."
  User should be directed to testing the webhook or monitoring logs.
```
