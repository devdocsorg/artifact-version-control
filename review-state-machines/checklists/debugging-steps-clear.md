# Checklist Sub-Machine: Debugging Steps Clear

**Parent:** [Engineering Review: Developer Guide](../engineering/developer-guide-review.md)  
**Reviewer:** Developer  
**Global outcome on FAIL:** `Dev_decision → ISSUES_FOUND → BACK_TO_DRAFTING`  
**Global outcome on PASS:** All Developer Guide checks complete → `Dev_decision`

---

## The Question

> When something goes wrong, can a developer follow the debugging steps in this doc
> to diagnose and fix the issue without external help?

## Sub-State Machine

```
[START: Debugging Steps Clear?]
    │
    ▼
┌──────────────────────────────┐
│ Check Error Catalog          │  Are common errors listed with messages?
│ (CATALOGED | INCOMPLETE)     │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Diagnostic Commands    │  Are there concrete steps to investigate?
│ (ACTIONABLE | VAGUE)         │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Resolution Paths       │  Does each error lead to a fix?
│ (RESOLVED | DEAD_END)        │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Error Message Accuracy │  Do documented messages match actual output?
│ (ACCURATE | OUTDATED)        │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Escalation Path        │  If self-serve fails, where does the user go?
│ (DEFINED | MISSING)          │
└────────┬─────────────────────┘
         │
         ▼
[AGGREGATE] ──→ PASS or FAIL
```

## What the Reviewer Looks For

### 1. Error Catalog
- Are the most common errors listed? (Top 5-10 at minimum)
- Does each error show the **exact error message** the user would see?
- Are errors organized in a findable way? (by symptom, by error code, by stage)
- **Diff viewer:** **Source (read-through)** — look for a troubleshooting section or FAQ.

### 2. Diagnostic Commands
- For each error, is there a concrete diagnostic step? (not "check your config" but "run `foo --validate`")
- Are log file locations specified?
- Are environment-check commands provided? (`node --version`, `docker ps`, etc.)
- **Diff viewer:** **Changes (diff)** — were diagnostic steps added for new failure modes?

### 3. Resolution Paths
- Does each diagnosed problem lead to a clear fix?
- Are fixes actionable? ("Delete the cache directory at `~/.foo/cache`" vs "clear the cache")
- Do resolutions account for the user's environment? (different for Docker vs bare-metal)
- **Diff viewer:** **Source (read-through)** — follow each error → diagnosis → resolution chain.

### 4. Error Message Accuracy
- Do the error messages shown in the doc match what the software actually produces?
- Have error codes or message formats changed since the doc was written?
- Are stack traces or log excerpts realistic?
- **Diff viewer:** **Changes (diff)** — check modified error examples against known output.

### 5. Escalation Path
- If the troubleshooting steps don't resolve the issue, where does the user go?
- Is there a support channel, GitHub issue template, or contact mentioned?
- Is there a "collect diagnostic info" section for filing good bug reports?

## Pass / Fail Criteria

| Verdict | Condition |
|---------|-----------|
| **PASS** | Common errors are cataloged with exact messages, each has diagnostic steps and a resolution, error messages match reality, and there's an escalation path when self-serve debugging fails |
| **FAIL** | Debugging section is missing/thin, error messages are wrong, resolutions are vague ("check your configuration"), or there's no way out when the listed fixes don't work |

## Failure Feedback Template

```
❌ Debugging Steps Clear: FAIL

[file.md, "Troubleshooting"] — Dead-end error:
  Error "CONNECTION_REFUSED" is listed but resolution says
  "check your network settings." Need specific steps:
  which port, which host, how to test connectivity.

[file.md, line 89] — Outdated error message:
  Doc shows: "Error: Invalid token format"
  Current:   "AuthError: Token validation failed (code: AUTH_003)"

[file.md] — Missing escalation:
  No guidance on what to do if none of the listed fixes work.
  Add a "Still stuck?" section with support channel link.
```
