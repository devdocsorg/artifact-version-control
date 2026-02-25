# Checklist Sub-Machine: Explanations Comprehensive

**Parent:** [Engineering Review: Developer Guide](../engineering/developer-guide-review.md)  
**Reviewer:** Developer  
**Global outcome on FAIL:** `Dev_decision → ISSUES_FOUND → BACK_TO_DRAFTING`  
**Global outcome on PASS:** Advances to next check (`Debugging Steps Clear?`)

---

## The Question

> Are the technical concepts, design decisions, and architectural rationale explained
> thoroughly enough for someone unfamiliar with the codebase?

## Sub-State Machine

```
[START: Explanations Comprehensive?]
    │
    ▼
┌────────────────────────────┐
│ Check Concept Introduction │  Are technical terms defined before use?
│ (DEFINED | UNDEFINED_TERMS)│
└────────┬───────────────────┘
         │
         ▼
┌────────────────────────────┐
│ Check "Why" Coverage       │  Does the doc explain WHY, not just HOW?
│ (EXPLAINED | MISSING_WHY)  │
└────────┬───────────────────┘
         │
         ▼
┌────────────────────────────┐
│ Check Prerequisite Chain   │  Are assumptions about prior knowledge explicit?
│ (CLEAR | HIDDEN_PREREQS)   │
└────────┬───────────────────┘
         │
         ▼
┌────────────────────────────┐
│ Check Edge Case Mentions   │  Are limitations and special cases noted?
│ (COVERED | GAPS)           │
└────────┬───────────────────┘
         │
         ▼
┌────────────────────────────┐
│ Check Architecture Context │  Does the reader understand how this fits?
│ (SITUATED | FLOATING)      │
└────────┬───────────────────┘
         │
         ▼
[AGGREGATE] ──→ PASS or FAIL
```

## What the Reviewer Looks For

### 1. Concept Introduction
- Is every technical term, acronym, or library name defined on first use?
- Are links to external reference docs provided where appropriate?
- Is jargon used without explanation? (e.g., "shard the data" without defining sharding)
- **Diff viewer:** **Source (read-through)** — read as if you're a new team member.

### 2. "Why" Coverage
- For every design decision described, does the doc explain the rationale?
- "Use Redis for caching" → but WHY Redis? What alternatives were considered?
- Does the doc just list steps, or does it help the reader build a mental model?
- **Diff viewer:** **Changes (diff)** — new sections should include reasoning, not just instructions.

### 3. Prerequisite Chain
- Does the doc state required knowledge upfront? ("Assumes familiarity with Docker")
- Are there hidden dependencies? (Uses `kubectl` without mentioning Kubernetes setup)
- Is there a "Before you begin" section with versions, tools, and access requirements?
- **Diff viewer:** **Source (read-through)** — check the opening section.

### 4. Edge Cases and Limitations
- Are known limitations documented? ("This approach doesn't work with >1M rows")
- Are platform-specific differences noted? (macOS vs Linux vs Windows)
- Are rate limits, quotas, or resource constraints mentioned?
- **Diff viewer:** **Changes (diff)** — were edge cases added alongside the new feature?

### 5. Architecture Context
- Does the reader know where this component fits in the overall system?
- Is there a diagram or at least a paragraph explaining relationships?
- Can someone reading only this doc understand enough to be productive?
- **Diff viewer:** **Preview (rendered)** — look for architecture diagrams, relationship descriptions.

## Pass / Fail Criteria

| Verdict | Condition |
|---------|-----------|
| **PASS** | A developer unfamiliar with the codebase could read this doc and understand not just what to do, but why they're doing it, what assumptions are made, and where this fits in the bigger picture |
| **FAIL** | The doc assumes implicit knowledge, skips rationale, uses undefined terms, or leaves the reader wondering "but why?" |

## Failure Feedback Template

```
❌ Explanations Comprehensive: FAIL

[file.md, "Authentication" section] — Missing rationale:
  Doc says "Use OAuth2 PKCE flow" but doesn't explain why PKCE
  over standard OAuth2 or API keys. A developer new to this would
  not understand the security tradeoff.

[file.md, line 34] — Undefined term:
  "idempotency key" used without definition or link to docs.

[file.md] — Missing prerequisites:
  No mention that the user needs a running PostgreSQL instance.
  This is a hard blocker at step 3.
```
