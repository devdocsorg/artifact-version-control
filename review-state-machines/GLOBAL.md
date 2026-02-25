# Global State Machine — Phase 4: Reviewing

This is the top-level review state machine for the Release Documentation Cycle.
It orchestrates two sequential reviews (Engineering → PM) and routes to doc-type-specific
sub-machines. Each checklist item in those sub-machines has its own detailed sub-state
machine file in `./checklists/` describing exactly what the reviewer looks for and how
they verify it using the diff viewer.

## Context: Where Phase 4 Sits

```
Phase 1: Organizing → Phase 2: Researching → Phase 3: Drafting → ★ Phase 4: Reviewing ★ → Phase 5: Publishing
```

Phase 4 begins after the writer creates a PR (Phase 3) and ends when both engineering
and PM reviewers approve, or loops back to Phase 3 if changes are needed.

---

## Top-Level Flow

```
[PR_SUBMITTED from Phase 3]
    │
    ▼
┌──────────────────────────────────────────┐
│  Developer: Engineering Review            │
│  ┌────────────────────────────────────┐  │
│  │ GITHUB_openPR → LOADED             │  │
│  │         │                          │  │
│  │    Dev_selectDocType               │  │
│  │    ┌────┼────────────┐             │  │
│  │    ▼    ▼            ▼             │  │
│  │  [DevGuide] [UIRef] [UserWF]      │  │
│  │    └────┼────────────┘             │  │
│  │         ▼                          │  │
│  │    Dev_decision                    │  │
│  └────────────────────────────────────┘  │
│                  │                        │
│     ┌────────────┴───────────┐           │
│     ▼                        ▼           │
│  ISSUES_FOUND           ALL_PASSED       │
│     │                        │           │
│  Developer:              Developer:      │
│  Request Changes         Approve         │
│     │                        │           │
│  GITHUB_requestChanges   GITHUB_devApprove│
│     │                        │           │
│  SUBMITTED               APPROVED        │
│     │                                    │
│  BACK_TO_DRAFTING                        │
└──────────────────────────────────────────┘
         │ (if APPROVED)
         ▼
    ENG_APPROVED
         │
         ▼
┌──────────────────────────────────────────┐
│  PM: Product Review                       │
│  ┌────────────────────────────────────┐  │
│  │ GITHUB_openPR2 → LOADED            │  │
│  │         │                          │  │
│  │  PM Checklist (All Doc Types)      │  │
│  │  Basic Workflows?                  │  │
│  │  Advanced Workflows?               │  │
│  │  User Troubleshooting?             │  │
│  │  Outcome Guarantees?               │  │
│  │  UI Reference Accuracy?            │  │
│  │  Workflow Pages Accuracy?          │  │
│  │         │                          │  │
│  │    PM_decision                     │  │
│  └────────────────────────────────────┘  │
│                  │                        │
│     ┌────────────┴───────────┐           │
│     ▼                        ▼           │
│  ISSUES_FOUND           ALL_PASSED       │
│     │                        │           │
│  PM: Request             PM: Approve     │
│  Changes                     │           │
│     │                   GITHUB_pmApprove │
│  GITHUB_pmRequestChanges     │           │
│     │                   APPROVED         │
│  SUBMITTED                               │
│     │                                    │
│  BACK_TO_DRAFTING2                       │
└──────────────────────────────────────────┘
         │ (if APPROVED)
         ▼
    PM_APPROVED → Phase 5: Publishing
```

---

## Exit Conditions

| Outcome | Next State | Trigger |
|---------|-----------|---------|
| `BACK_TO_DRAFTING` | Phase 3 | Engineering reviewer found issues |
| `BACK_TO_DRAFTING2` | Phase 3 | PM reviewer found issues |
| `PM_APPROVED` | Phase 5 | Both reviews passed |

---

## Sub-State Machine Index

### Engineering Review Sub-Machines (by Doc Type)

| File | Doc Type | Checklist Items |
|------|----------|-----------------|
| [engineering/developer-guide-review.md](./engineering/developer-guide-review.md) | Developer Guide | Code Tested, Explanations Comprehensive, Debugging Steps Clear |
| [engineering/ui-reference-review.md](./engineering/ui-reference-review.md) | UI Reference | UX Components Accurate, Error States Documented, Data Sources Explained, Actions Documented |
| [engineering/user-workflow-review.md](./engineering/user-workflow-review.md) | User Workflow | Feature Contextualized, Comprehensive vs Other Features, Troubleshooting Correct |

### PM Review Sub-Machine

| File | Applies To | Checklist Items |
|------|-----------|-----------------|
| [pm/pm-review.md](./pm/pm-review.md) | All Doc Types | Basic Workflows, Advanced Workflows, User Troubleshooting, Outcome Guarantees, UI Reference Accuracy, Workflow Pages Accuracy |

### Detailed Checklist Item Sub-Machines

Each checklist item has its own file in `./checklists/` with:
- What the reviewer is actually evaluating (specific questions)
- What to look for in the diff viewer (which views, what signals)
- Pass/fail criteria with examples
- How failure feeds back into the global machine

#### Engineering Checklist Items
| File | Parent Review | Question |
|------|--------------|----------|
| [checklists/code-tested.md](./checklists/code-tested.md) | Developer Guide | Do code samples compile/run correctly? |
| [checklists/explanations-comprehensive.md](./checklists/explanations-comprehensive.md) | Developer Guide | Are technical concepts fully explained? |
| [checklists/debugging-steps-clear.md](./checklists/debugging-steps-clear.md) | Developer Guide | Can a user troubleshoot using these steps? |
| [checklists/ux-components-accurate.md](./checklists/ux-components-accurate.md) | UI Reference | Do UI descriptions match the actual interface? |
| [checklists/error-states-documented.md](./checklists/error-states-documented.md) | UI Reference | Are all error/edge-case states covered? |
| [checklists/data-sources-explained.md](./checklists/data-sources-explained.md) | UI Reference | Is it clear where displayed data comes from? |
| [checklists/actions-documented.md](./checklists/actions-documented.md) | UI Reference | Are all user actions and their effects described? |
| [checklists/feature-contextualized.md](./checklists/feature-contextualized.md) | User Workflow | Is the feature placed in the user's broader journey? |
| [checklists/comprehensive-vs-other-features.md](./checklists/comprehensive-vs-other-features.md) | User Workflow | Are interactions with other features covered? |
| [checklists/troubleshooting-correct.md](./checklists/troubleshooting-correct.md) | User Workflow | Are troubleshooting steps technically accurate? |

#### PM Checklist Items
| File | Question |
|------|----------|
| [checklists/basic-workflows.md](./checklists/basic-workflows.md) | Are standard user workflows documented? |
| [checklists/advanced-workflows.md](./checklists/advanced-workflows.md) | Are power-user/advanced scenarios covered? |
| [checklists/user-troubleshooting.md](./checklists/user-troubleshooting.md) | Can users self-serve when things go wrong? |
| [checklists/outcome-guarantees.md](./checklists/outcome-guarantees.md) | Does the doc promise clear, achievable outcomes? |
| [checklists/ui-reference-accuracy.md](./checklists/ui-reference-accuracy.md) | Do UI screenshots/descriptions match the product? |
| [checklists/workflow-pages-accuracy.md](./checklists/workflow-pages-accuracy.md) | Do workflow pages reflect the actual user flow? |
