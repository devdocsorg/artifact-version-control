# Checklist Sub-Machine: Basic Workflows

**Parent:** [PM Review](../pm/pm-review.md)  
**Reviewer:** PM (Product Manager)  
**Global outcome on FAIL:** `PM_decision → ISSUES_FOUND → BACK_TO_DRAFTING2`  
**Global outcome on PASS:** Advances to next check (`Advanced Workflows?`)

---

## The Question

> Does the documentation cover the standard, happy-path workflows that the majority
> of users will follow? Can a typical user accomplish the core tasks?

## Sub-State Machine

```
[START: Basic Workflows?]
    │
    ▼
┌──────────────────────────────┐
│ Identify Core User Tasks     │  What are the 3-5 things most users MUST
│ (from PRD / product vision)  │  be able to do?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Task Coverage          │  Is each core task documented start-to-finish?
│ (COVERED | GAPS)             │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Step Completeness      │  Can a user follow the steps without guessing?
│ (COMPLETE | MISSING_STEPS)   │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Outcome Clarity        │  Does the user know when they've succeeded?
│ (CLEAR | AMBIGUOUS)          │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Onboarding Flow        │  Is the first-time-user path documented?
│ (DOCUMENTED | MISSING)       │
└────────┬─────────────────────┘
         │
         ▼
[AGGREGATE] ──→ PASS or FAIL
```

## What the Reviewer Looks For

### 1. Identify Core User Tasks
- What are the primary jobs-to-be-done for this feature?
- Cross-reference with the PRD: what did we promise?
- Think from the user's perspective, not the feature list (task-oriented, not feature-oriented)
- **Source:** PRD, user stories, product vision document

### 2. Task Coverage
- Is each core task documented from "I want to do X" through "X is done"?
- Are there tasks the PM considers essential that the writer hasn't covered?
- Is the coverage proportional? (primary task gets detailed treatment, not buried in a footnote)
- **Diff viewer:** **Source (read-through)** — read the doc as a user looking to accomplish something.

### 3. Step Completeness
- For each documented workflow: are all steps present? No "then configure the settings" without showing HOW
- Are prerequisites listed before the steps begin?
- Are decision points in the workflow handled? ("If you selected option A, continue here")
- **Diff viewer:** **Preview (rendered)** — follow the workflow visually.

### 4. Outcome Clarity
- At the end of the workflow, does the user know they succeeded?
- Is there a verification step? ("You should see a green checkmark" / "Run this command to verify")
- What does success look like? What does the user have at the end that they didn't before?
- **Diff viewer:** **Source (read-through)** — check the conclusion of each workflow.

### 5. Onboarding Flow
- Is the first-time experience covered? (new user, empty account, initial setup)
- Is the happy path from signup/install to first meaningful action documented?
- Are "getting started" and "quickstart" scenarios present?

## Pass / Fail Criteria

| Verdict | Condition |
|---------|-----------|
| **PASS** | All core user tasks are documented end-to-end, steps are complete and followable, success is clearly defined, and the first-time user path exists |
| **FAIL** | Core tasks are missing, workflows have gaps, outcomes are unclear, or new users have no starting path |

## Failure Feedback Template

```
❌ Basic Workflows: FAIL

[file.md] — Missing core task:
  The #1 user task is "Create and send an invoice" but the doc
  only covers creating — not sending. The workflow is incomplete.

[file.md, "Setup"] — Missing onboarding:
  No first-time-user flow. A new user who just signed up has
  no idea where to start. Need a "Getting Started" section.

[file.md, "Import Data"] — Unclear outcome:
  Workflow ends at "Click Import" but doesn't describe what
  success looks like. How does the user know the import worked?
```
