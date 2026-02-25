# Checklist Sub-Machine: Workflow Pages Accuracy

**Parent:** [PM Review](../pm/pm-review.md)  
**Reviewer:** PM (Product Manager)  
**Global outcome on FAIL:** `PM_decision → ISSUES_FOUND → BACK_TO_DRAFTING2`  
**Global outcome on PASS:** All PM checks complete → `PM_decision`

---

## The Question

> Do the documented workflows accurately reflect how users actually move through
> the product? Do the pages match real user journeys, not idealized internal diagrams?

## Sub-State Machine

```
[START: Workflow Pages Accuracy?]
    │
    ▼
┌──────────────────────────────┐
│ Check Journey Map Match      │  Does the documented workflow match the
│ (MATCHES | DIVERGED)         │  actual user journey through the product?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Page Transitions       │  Are page-to-page transitions described
│ (ACCURATE | BROKEN)          │  correctly? Do they match the real flow?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Decision Points        │  Are user decision points (branching paths)
│ (DOCUMENTED | MISSING)       │  captured with appropriate guidance?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Edge Paths             │  Are non-happy-path routes (back, cancel,
│ (COVERED | HAPPY_PATH_ONLY)  │  error, timeout) accounted for?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Cross-Page Consistency │  Do descriptions of the same screen
│ (CONSISTENT | CONTRADICTS)   │  agree across different workflow pages?
└────────┬─────────────────────┘
         │
         ▼
[AGGREGATE] ──→ PASS or FAIL
```

## What the Reviewer Looks For

### 1. Journey Map Match
- Does the documented flow reflect how real users actually use the product?
- Is the workflow based on analytics/user research, or on how engineering built it?
- Are common shortcuts and alternate paths that real users take documented?
- Does the PM recognize this as the intended user experience?
- **Diff viewer:** **Source (read-through)** — walk through the workflow as a user would.

### 2. Page Transitions
- When the doc says "you'll be taken to the Dashboard," does the product actually go there?
- Are redirect behaviors after form submission correct?
- Are modal/drawer behaviors described accurately? (does it open a new page or a modal?)
- Are transition triggers correct? ("After saving" vs "After clicking Continue")
- **Diff viewer:** **Changes (diff)** — were transitions updated when the UI flow changed?

### 3. Decision Points
- Does the workflow branch where users actually have choices?
- Are conditional paths documented? ("If you selected Free plan, see X. If Pro, see Y.")
- Is guidance given at each decision point? (not just "choose an option" but why you'd pick each)
- Are role-based forks handled? (admin vs user sees different next steps)
- **Diff viewer:** **Source (read-through)** — identify every "if/then" in the workflow.

### 4. Edge Paths
- What happens when the user clicks "Back"? "Cancel"? Closes the browser?
- What if the user navigates away mid-workflow — is the state saved?
- Are timeout behaviors documented? (session expires during a multi-step process)
- What happens if the user skips an optional step?
- **Diff viewer:** **Source (read-through)** — check for non-happy-path documentation.

### 5. Cross-Page Consistency
- If the same screen is described in two different workflow pages, do they agree?
- Are field names, button labels, and behaviors consistent across all pages that reference them?
- Does navigating between docs create contradictions?
- **Diff viewer:** **Before/After (compare)** — check that changes are consistent across files.

## Pass / Fail Criteria

| Verdict | Condition |
|---------|-----------|
| **PASS** | Documented workflows match real user journeys, transitions are correct, decision points have guidance, edge paths are covered, and cross-page references are consistent |
| **FAIL** | Workflows reflect internal architecture instead of user experience, transitions are wrong, decision points lack guidance, only the happy path is covered, or pages contradict each other |

## Failure Feedback Template

```
❌ Workflow Pages Accuracy: FAIL

[file.md, "Onboarding"] — Journey mismatch:
  Doc shows: Signup → Profile → Dashboard
  Actual:    Signup → Verification Email → Profile → Team Setup → Dashboard
  Two steps are completely missing from the workflow.

[file.md, "Checkout"] — Wrong transition:
  Doc says "After payment, you'll see the confirmation page."
  Actually, the user is redirected to Stripe and then back.
  The redirect creates confusion the doc doesn't address.

[file.md + settings.md] — Cross-page contradiction:
  "Settings" workflow says the Save button is at the bottom.
  "Quick Setup" workflow says it's in the top-right toolbar.
  One of these is wrong (it's bottom-right).
```
