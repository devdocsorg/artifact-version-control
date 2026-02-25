# Checklist Sub-Machine: Advanced Workflows

**Parent:** [PM Review](../pm/pm-review.md)  
**Reviewer:** PM (Product Manager)  
**Global outcome on FAIL:** `PM_decision → ISSUES_FOUND → BACK_TO_DRAFTING2`  
**Global outcome on PASS:** Advances to next check (`User Troubleshooting?`)

---

## The Question

> Does the documentation cover advanced, power-user, and edge-case workflows beyond
> the basics? Are sophisticated users served, not just beginners?

## Sub-State Machine

```
[START: Advanced Workflows?]
    │
    ▼
┌──────────────────────────────┐
│ Identify Power-User Tasks    │  What do experienced users need that
│ (from PM knowledge, support  │  goes beyond basic usage?
│  tickets, feature requests)  │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Automation /           │  Are batch operations, scripting, and
│ Bulk Operations              │  API-driven workflows documented?
│ (COVERED | MISSING)          │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Configuration Depth    │  Are advanced settings and customization
│ (DOCUMENTED | SURFACE_ONLY)  │  options explained?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Integration Scenarios  │  Are third-party integration and
│ (COVERED | MISSING)          │  interoperability workflows included?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Scale Considerations   │  Does the doc address large-scale usage?
│ (ADDRESSED | IGNORED)        │  Performance, limits, optimization?
└────────┬─────────────────────┘
         │
         ▼
[AGGREGATE] ──→ PASS or FAIL
```

## What the Reviewer Looks For

### 1. Power-User Tasks
- What would a 6-month user want to do that a day-1 user wouldn't?
- Are workflows for team leads, admins, and heavy users documented?
- Cross-reference with top support tickets: what do users ask about after mastering basics?
- **Source:** Support ticket trends, feature request backlog, PM intuition.

### 2. Automation and Bulk Operations
- Can users automate repetitive tasks? Is the method documented?
- Are bulk import/export workflows covered?
- Is the API documented as an automation tool, not just a reference?
- Are CLI tools or SDK workflows included for scripting?
- **Diff viewer:** **Source (read-through)** — look for automation and batch processing sections.

### 3. Configuration Depth
- Are advanced configuration options documented beyond the defaults?
- Environment variables, feature flags, advanced settings panels?
- Are configuration tradeoffs explained? ("Increasing X improves Y but costs Z")
- **Diff viewer:** **Changes (diff)** — new features should document their advanced configuration.

### 4. Integration Scenarios
- Are workflows with third-party tools documented? (Slack, Jira, CI/CD, SSO providers)
- Are webhook, API, and data export integration patterns described?
- Are common integration architectures shown? (not just "here's the API" but "here's how to connect to Salesforce")
- **Diff viewer:** **Source (read-through)** — look for integration or interoperability sections.

### 5. Scale Considerations
- Does the doc address what happens at scale? (1000+ users, millions of records)
- Are performance optimization tips included?
- Are known limits documented? (rate limits, storage caps, concurrent user limits)
- Is there guidance for enterprise/large-team usage patterns?

## Pass / Fail Criteria

| Verdict | Condition |
|---------|-----------|
| **PASS** | Advanced workflows are documented: automation, bulk operations, deep configuration, integrations, and scale considerations. Power users can find guidance beyond the basics |
| **FAIL** | Doc only covers beginner-level usage. Advanced users, automators, and enterprise customers will be left to figure things out on their own |

## Failure Feedback Template

```
❌ Advanced Workflows: FAIL

[file.md] — Missing bulk operations:
  Basic workflow covers creating items one-at-a-time, but there's
  no mention of the CSV bulk import or the API batch endpoint.
  Power users need this on day one.

[file.md] — No integration guidance:
  Feature has a webhook system but the doc doesn't include a
  single integration example. Need at least Slack + CI/CD patterns.

[file.md] — Scale not addressed:
  No mention of rate limits or what happens with >10K items.
  Enterprise customers will hit this immediately.
```
