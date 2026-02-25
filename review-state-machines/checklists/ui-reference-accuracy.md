# Checklist Sub-Machine: UI Reference Accuracy

**Parent:** [PM Review](../pm/pm-review.md)  
**Reviewer:** PM (Product Manager)  
**Global outcome on FAIL:** `PM_decision → ISSUES_FOUND → BACK_TO_DRAFTING2`  
**Global outcome on PASS:** Advances to next check (`Workflow Pages Accuracy?`)

---

## The Question

> Do the UI descriptions and screenshots in the documentation match the product
> as it will ship to users — not staging, not mockups, not an old version?

## Sub-State Machine

```
[START: UI Reference Accuracy?]
    │
    ▼
┌──────────────────────────────┐
│ Check Screenshot Currency    │  Are screenshots from the current/shipping
│ (CURRENT | OUTDATED)         │  version of the product?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Screenshot Environment │  Are screenshots from production, not
│ (PRODUCTION | STAGING/DEV)   │  staging or dev with test data?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Terminology Match      │  Does the doc use the same labels and
│ (CONSISTENT | MISMATCHED)    │  terminology as the product UI?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Navigation Accuracy    │  Do described menu paths and navigation
│ (CORRECT | WRONG)            │  instructions match the product?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Feature Flag State     │  Are described features enabled for all
│ (GENERAL_AVAILABILITY |      │  users, or still behind a feature flag?
│  BEHIND_FLAG)                │
└────────┬─────────────────────┘
         │
         ▼
[AGGREGATE] ──→ PASS or FAIL
```

## How This Differs from Engineering's "UX Components Accurate"

The engineering reviewer checks component-level accuracy: does each button, field, and
label match the code? The PM checks **product-level accuracy**: does the documented
experience match what a paying customer will see?

| Engineering (Components) | PM (Product Experience) |
|------------------------|------------------------|
| "Does the button label match the code?" | "Are these screenshots from production?" |
| "Is the field order correct?" | "Is the terminology customer-facing?" |
| "Does this component exist?" | "Is this feature GA or behind a flag?" |

## What the Reviewer Looks For

### 1. Screenshot Currency
- Are screenshots from the version that will ship (not a mockup or older version)?
- Do screenshots show the final visual design (not a prototype)?
- Are screenshots at appropriate resolution and readable?
- Do annotations match the current layout?
- **Diff viewer:** **Before/After (compare)** — compare old and new screenshots.

### 2. Screenshot Environment
- Are screenshots from production (or a production-like environment)?
- Is test data realistic? (not "test@test.com" or "John Doe" everywhere)
- Are staging-only features or debug UI elements visible?
- Is the environment indicator (staging banner, debug toolbar) cropped out?
- **Diff viewer:** **Preview (rendered)** — examine screenshots closely.

### 3. Terminology Match
- Does the doc use internal codenames or customer-facing names?
- Are product/feature names capitalized consistently with marketing?
- Does the doc call it what the UI calls it? ("Workspaces" not "Projects" if the UI says "Workspaces")
- Are industry terms used correctly per the company's style guide?
- **Diff viewer:** **Source (read-through)** — check terminology against the live product.

### 4. Navigation Accuracy
- Do menu paths match the current IA? ("Settings > Security > SSO" — is that the real path?)
- Have any menu items been renamed or reorganized since the doc was written?
- Are breadcrumbs, sidebar items, and tab names correct?
- **Diff viewer:** **Changes (diff)** — were navigation paths updated alongside the feature change?

### 5. Feature Flag State
- Is every described feature available to all users?
- Are beta or early-access features clearly labeled as such?
- Is there a risk of documenting a feature that gets pulled before GA?
- Does the PM sign off that this feature will ship in this release?

## Pass / Fail Criteria

| Verdict | Condition |
|---------|-----------|
| **PASS** | Screenshots are current and from production, terminology matches the product, navigation paths are correct, and all described features are GA or clearly labeled as beta |
| **FAIL** | Screenshots are outdated or from staging, terminology doesn't match the product, navigation is wrong, or doc describes features that aren't available to users |

## Failure Feedback Template

```
❌ UI Reference Accuracy: FAIL

[file.md, screenshot line 23] — Staging screenshot:
  Screenshot shows "STAGING" banner in the header and test
  data ("Test Company, test@example.com"). Need production
  screenshot with realistic data.

[file.md, "Analytics" section] — Wrong terminology:
  Doc calls it "Reports" throughout, but the product UI was
  renamed to "Insights" in v4.1. Needs global find/replace.

[file.md] — Feature flag issue:
  "Custom Roles" is documented but still behind a feature flag.
  Not available to users until Q2. Either remove or label as
  "Coming Soon."
```
