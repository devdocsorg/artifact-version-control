# Checklist Sub-Machine: Comprehensive vs Other Features

**Parent:** [Engineering Review: User Workflow](../engineering/user-workflow-review.md)  
**Reviewer:** Developer  
**Global outcome on FAIL:** `Dev_decision → ISSUES_FOUND → BACK_TO_DRAFTING`  
**Global outcome on PASS:** Advances to next check (`Troubleshooting Correct?`)

---

## The Question

> Does this documentation accurately describe how this feature interacts with, depends on,
> and affects other features in the product?

## Sub-State Machine

```
[START: Comprehensive vs Other Features?]
    │
    ▼
┌──────────────────────────────┐
│ Map Feature Dependencies     │  What other features must be configured
│ (MAPPED | INCOMPLETE)        │  for this one to work?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Integration Points     │  Where does this feature send/receive
│ (DOCUMENTED | MISSING)       │  data to/from other features?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Conflict Scenarios     │  Can this feature conflict with or
│ (NOTED | HIDDEN)             │  override other features?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Feature Comparison     │  When would a user choose this feature
│ Guidance                     │  vs. a similar one?
│ (GUIDED | CONFUSING)         │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Cross-References       │  Are links to related feature docs
│ (LINKED | ISOLATED)          │  provided at the right points?
└────────┬─────────────────────┘
         │
         ▼
[AGGREGATE] ──→ PASS or FAIL
```

## What the Reviewer Looks For

### 1. Feature Dependencies
- Does the doc state which other features must be enabled/configured first?
- Are there implicit dependencies? (e.g., "audit logging" requires "SSO" to be configured)
- Are version or plan-tier requirements for dependent features mentioned?
- **Diff viewer:** **Source (read-through)** — look for prerequisites that reference other features.

### 2. Integration Points
- Where does data flow between this feature and others?
- If this feature generates events, where do those events surface?
- Does this feature consume data from another feature? Is that dependency documented?
- Example: "Billing alerts" depends on "Usage tracking" data — is that connection stated?
- **Diff viewer:** **Changes (diff)** — new integrations should document both sides of the connection.

### 3. Conflict Scenarios
- Can two features contradict each other? (e.g., "auto-scale" vs "fixed capacity")
- Does enabling this feature disable or limit another?
- Are there priority/precedence rules? ("Team settings override personal settings")
- **Diff viewer:** **Source (read-through)** — look for feature interactions that could surprise users.

### 4. Feature Comparison Guidance
- If similar features exist, does the doc help the user choose?
- "Webhooks vs. Polling vs. Server-Sent Events" — when to use which?
- Are tradeoffs documented? (performance, cost, complexity)
- **Diff viewer:** **Source (read-through)** — look for comparison tables, "when to use" sections.

### 5. Cross-References
- Are related feature docs linked at natural decision points?
- Not a generic "Related docs" footer — links where the reader actually needs them
- Do cross-references use the correct and current doc titles?
- **Diff viewer:** **Changes (diff)** — new content should include links where other features are mentioned.

## Pass / Fail Criteria

| Verdict | Condition |
|---------|-----------|
| **PASS** | Dependencies on other features are stated, integration points are documented, conflicts/overrides are noted, comparison guidance helps users choose, and cross-references link to related docs at relevant moments |
| **FAIL** | Feature is documented in isolation, doesn't mention interactions with other features, ignores conflicts, or leaves the user confused about which feature to use for their scenario |

## Failure Feedback Template

```
❌ Comprehensive vs Other Features: FAIL

[file.md, "Role-Based Access"] — Missing dependency:
  RBAC requires SSO to be configured first, but the doc
  doesn't mention this. Users will hit a wall at step 3.

[file.md] — Conflict not documented:
  "IP allowlist" and "VPN requirement" can conflict —
  users enabling both get locked out. This needs a warning.

[file.md] — Missing comparison:
  This doc describes "scheduled exports" but doesn't
  compare it to "real-time webhooks" which solve a similar
  problem. Users need guidance on when to use which.
```
