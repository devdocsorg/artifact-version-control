# PM Review: Product Review (All Doc Types)

**Reviewer:** PM (Product Manager)  
**Doc Type:** All — this checklist applies universally after engineering approval  
**Entry:** `ENG_APPROVED` → `GITHUB_openPR2` → `LOADED`  
**Exit:** Returns verdict to `PM_decision` in [GLOBAL.md](../GLOBAL.md)

## State Machine

```
[ENG_APPROVED]
    │
    ▼
GITHUB_openPR2 ──→ LOADED
    │
    ▼
┌────────────────────────────┐
│ PM Checklist (All Doc Types)│
│                             │
│ ┌────────────────────────┐ │
│ │ Basic Workflows?       │ │──→ see ../checklists/basic-workflows.md
│ └───────┬────────────────┘ │
│         ▼                   │
│ ┌────────────────────────┐ │
│ │ Advanced Workflows?    │ │──→ see ../checklists/advanced-workflows.md
│ └───────┬────────────────┘ │
│         ▼                   │
│ ┌────────────────────────┐ │
│ │ User Troubleshooting?  │ │──→ see ../checklists/user-troubleshooting.md
│ └───────┬────────────────┘ │
│         ▼                   │
│ ┌────────────────────────┐ │
│ │ Outcome Guarantees?    │ │──→ see ../checklists/outcome-guarantees.md
│ └───────┬────────────────┘ │
│         ▼                   │
│ ┌────────────────────────┐ │
│ │ UI Reference Accuracy? │ │──→ see ../checklists/ui-reference-accuracy.md
│ └───────┬────────────────┘ │
│         ▼                   │
│ ┌────────────────────────┐ │
│ │ Workflow Pages         │ │──→ see ../checklists/workflow-pages-accuracy.md
│ │ Accuracy?              │ │
│ └───────┬────────────────┘ │
│         ▼                   │
│    [ALL_CHECKS_DONE]       │
└────────────────────────────┘
    │
    ▼
PM_decision
    │
    ├── ISSUES_FOUND ──→ PM: Request Changes → GITHUB_pmRequestChanges → SUBMITTED → BACK_TO_DRAFTING2
    └── ALL_PASSED   ──→ PM: Approve → GITHUB_pmApprove → APPROVED → PM_APPROVED
```

## How PM Review Differs from Engineering Review

The engineering review asks: **"Is this technically correct?"**  
The PM review asks: **"Does this serve the user and align with the product vision?"**

The PM is not re-checking code accuracy (engineering already passed). Instead they're
evaluating whether the documentation:
- Covers the workflows users actually need
- Promises outcomes the product can deliver
- Matches the product as it ships (not as it was specced)
- Tells a complete story from the user's perspective

## Aggregation → PM_decision

```
IF any check returned FAIL:
    PM_decision = ISSUES_FOUND
    → Collect all FAIL notes into PM review comments
    → PM: Request Changes → GITHUB_pmRequestChanges → BACK_TO_DRAFTING2
ELSE:
    PM_decision = ALL_PASSED
    → PM: Approve → GITHUB_pmApprove → PM_APPROVED
```

## Diff Viewer Strategy

The PM uses the diff viewer differently from the engineer:

| PM Focus | Primary View | Why |
|----------|-------------|-----|
| "Does it cover the right workflows?" | **Source (read-through)** | Reading for completeness, not correctness |
| "Does it match the product?" | **Preview (rendered)** | Seeing the doc as a user would |
| "Did the writer address my previous feedback?" | **Changes (diff)** | Checking specific modifications |
| "Is the visual presentation right?" | **Before/After (compare)** | Comparing evolved structure |

## Common PM Rejection Patterns

1. **Scope gap** — doc covers basic usage but not the advanced scenario leadership cares about
2. **Vision drift** — doc describes v1 behavior but the PM has already changed direction for v2
3. **User disconnect** — doc is technically accurate but doesn't speak to the user's actual problem
4. **Missing safety net** — no troubleshooting section, users will flood support
5. **Screenshot mismatch** — UI screenshots are from staging, not production
6. **Inconsistent terminology** — doc uses internal names instead of customer-facing names
