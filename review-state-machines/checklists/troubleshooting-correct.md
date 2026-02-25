# Checklist Sub-Machine: Troubleshooting Correct

**Parent:** [Engineering Review: User Workflow](../engineering/user-workflow-review.md)  
**Reviewer:** Developer  
**Global outcome on FAIL:** `Dev_decision → ISSUES_FOUND → BACK_TO_DRAFTING`  
**Global outcome on PASS:** All User Workflow checks complete → `Dev_decision`

---

## The Question

> Are the troubleshooting steps in this workflow document technically accurate — will they
> actually diagnose and resolve the problems described?

## Sub-State Machine

```
[START: Troubleshooting Correct?]
    │
    ▼
┌──────────────────────────────┐
│ Check Symptom Descriptions   │  Do described symptoms match real behavior?
│ (ACCURATE | WRONG)           │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Diagnostic Validity    │  Do the suggested diagnostic steps actually
│ (VALID | INEFFECTIVE)        │  reveal the problem?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Fix Correctness        │  Do the suggested fixes actually solve
│ (CORRECT | WRONG_FIX)        │  the diagnosed problem?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Fix Safety             │  Could the fix cause new problems?
│ (SAFE | RISKY)               │  Are risks/rollback documented?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Workflow-Specific       │  Are troubleshooting steps specific to
│ Context                      │  this workflow, not generic?
│ (SPECIFIC | GENERIC)         │
└────────┬─────────────────────┘
         │
         ▼
[AGGREGATE] ──→ PASS or FAIL
```

## What the Reviewer Looks For

### 1. Symptom Descriptions
- Does the documented symptom match what the user actually sees?
- "You may see a blank screen" — is it actually blank, or is there a spinner?
- Are error messages quoted exactly?
- Are symptoms specific enough to distinguish between different root causes?
- **Diff viewer:** **Changes (diff)** — verify symptom descriptions match known bug reports.

### 2. Diagnostic Validity
- Do the diagnostic commands actually work? (correct syntax, correct tool, exists in the system)
- Will the diagnostic step actually reveal the root cause, or is it a red herring?
- Are diagnostic steps ordered correctly? (cheapest/fastest checks first)
- Example: "Check the logs at `/var/log/app.log`" — is that the right path?
- **Diff viewer:** **Source (read-through)** — mentally execute each diagnostic step.

### 3. Fix Correctness
- Will the documented fix actually resolve the problem?
- Is the fix complete? (not just "restart the service" when you also need to clear the cache)
- Does the fix match the diagnostic? (not prescribing fix A when diagnosis B was found)
- Has the fix been tested with the current software version?
- **Diff viewer:** **Changes (diff)** — new fixes should reference known solutions from engineering.

### 4. Fix Safety
- Could the fix cause data loss, downtime, or cascading failures?
- Are warnings included for destructive fixes? ("This will reset all user sessions")
- Is a rollback procedure documented?
- Are there "try this first" (safe) vs "try this last" (risky) tiers?
- **Diff viewer:** **Source (read-through)** — check for destructive operations without warnings.

### 5. Workflow-Specific Context
- Are troubleshooting steps specific to this workflow, not generic "restart everything" advice?
- Do they account for the state the user is in during this particular workflow?
- Example: "If the export fails at step 3" is better than "If something goes wrong"
- **Diff viewer:** **Source (read-through)** — check that troubleshooting references specific workflow steps.

## Pass / Fail Criteria

| Verdict | Condition |
|---------|-----------|
| **PASS** | Symptoms are accurately described, diagnostic steps work and reveal root causes, fixes are correct and safe, risks are noted, and troubleshooting is specific to the workflow |
| **FAIL** | Symptoms don't match reality, diagnostics are wrong/outdated, fixes don't actually work, destructive fixes lack warnings, or troubleshooting is generic boilerplate |

## Failure Feedback Template

```
❌ Troubleshooting Correct: FAIL

[file.md, "Export fails"] — Wrong diagnostic:
  Doc says to check `/var/log/export.log` but this service
  logs to `/var/log/app/export-worker.log` since v3.1.

[file.md, "Connection timeout"] — Fix doesn't work:
  Doc says "increase the timeout to 60s in config.yml" but
  the timeout is now set via environment variable TIMEOUT_MS,
  not the config file. Config file setting is ignored.

[file.md, "Reset data"] — Missing safety warning:
  "Run `reset-pipeline --force`" will delete ALL pipeline data,
  not just the current run. This needs a giant warning and a
  "backup first" step.
```
