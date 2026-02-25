# Engineering Review: User Workflow

**Reviewer:** Developer (Engineer who built or owns the feature)  
**Doc Type:** User Workflow — end-to-end task docs, process guides, multi-feature flows  
**Entry:** `DOC_TYPE_USER_WORKFLOW` from `Dev_selectDocType`  
**Exit:** Returns verdict to `Dev_decision` in [GLOBAL.md](../GLOBAL.md)

## State Machine

```
[DOC_TYPE_USER_WORKFLOW]
    │
    ▼
┌──────────────────────────────┐
│ Feature Contextualized?      │──→ see ../checklists/feature-contextualized.md
│ (PASS | FAIL + notes)        │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Comprehensive vs Other       │──→ see ../checklists/comprehensive-vs-other-features.md
│ Features?                    │
│ (PASS | FAIL + notes)        │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Troubleshooting Correct?     │──→ see ../checklists/troubleshooting-correct.md
│ (PASS | FAIL + notes)        │
└────────┬─────────────────────┘
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

## What Makes User Workflow Docs Special

User Workflow docs are **narrative** — they describe how a user accomplishes a goal
that may span multiple features, screens, or even products. The engineering reviewer
verifies that the described journey is technically possible and that the feature
interactions are accurate.

**Core question:** "Does this workflow actually work end-to-end, and does it correctly
describe how features interact with each other?"

## Diff Viewer Strategy

| Check | Primary View | What to Look For |
|-------|-------------|------------------|
| Feature Contextualized | **Source (read-through)** | Does the intro explain where this fits? |
| Feature Contextualized | **Before/After (compare)** | Was context added/changed appropriately? |
| Comprehensive vs Other Features | **Source (read-through)** | Are cross-feature interactions described? |
| Comprehensive vs Other Features | **Changes (diff)** | Do changes reference the right related features? |
| Troubleshooting Correct | **Source (read-through)** | Are the suggested fixes technically valid? |
| Troubleshooting Correct | **Changes (diff)** | Do error descriptions match actual error codes? |

## Common Failure Patterns

1. **Tunnel vision** — describes one feature in isolation, ignoring how it connects to others
2. **Missing prerequisites** — workflow starts at step 3, assumes steps 1-2 are obvious
3. **Dead-end paths** — "if X fails" with no guidance on what to do next
4. **Outdated integrations** — feature A no longer talks to feature B that way
5. **Role confusion** — describes an admin workflow but labels it as a user workflow
6. **Circular references** — "see the workflow doc" links back to itself
