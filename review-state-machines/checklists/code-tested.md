# Checklist Sub-Machine: Code Tested

**Parent:** [Engineering Review: Developer Guide](../engineering/developer-guide-review.md)  
**Reviewer:** Developer  
**Global outcome on FAIL:** `Dev_decision → ISSUES_FOUND → BACK_TO_DRAFTING`  
**Global outcome on PASS:** Advances to next check (`Explanations Comprehensive?`)

---

## The Question

> Do the code samples, commands, and technical instructions in this document actually work?

## Sub-State Machine

```
[START: Code Tested?]
    │
    ▼
┌──────────────────────────┐
│ Identify All Code Blocks │  List every code sample, CLI command, config snippet
│ (inventory)              │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Check Syntax Validity    │  Do samples parse/compile without errors?
│ (VALID | SYNTAX_ERROR)   │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Check Runtime Behavior   │  Do samples produce the described output?
│ (MATCHES | DIVERGES)     │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Check Version Compat     │  Are version/dependency assumptions stated and current?
│ (CURRENT | STALE)        │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Check Copy-Paste Ready   │  Can a user copy the sample and run it as-is?
│ (READY | NEEDS_EDITS)    │
└────────┬─────────────────┘
         │
         ▼
[AGGREGATE] ──→ PASS (all good) or FAIL (any issue found)
```

## What the Reviewer Looks For

### 1. Identify All Code Blocks (Inventory)
- Count every fenced code block, inline command, and config example
- Note the language/runtime for each (Python, bash, JSON, YAML, etc.)
- Flag any blocks missing language annotations

### 2. Check Syntax Validity
- **For code:** Does it parse? Missing imports, typos, unmatched brackets?
- **For CLI commands:** Are flags correct? Do tools accept those arguments?
- **For config files:** Is the format valid JSON/YAML/TOML?
- **Diff viewer:** Use **Changes** view to see what was modified. Focus on new/changed code blocks.

### 3. Check Runtime Behavior
- Do the samples produce the output shown in the doc?
- Are environment variables, auth tokens, or placeholders marked clearly?
- Is the expected output section accurate, or does it show an idealized version?
- **Diff viewer:** Use **Source (read-through)** — mentally execute the steps in order.

### 4. Check Version Compatibility
- Are library/SDK version numbers stated?
- Does `pip install foo` get the right version, or does it need `foo==2.3.1`?
- Are deprecated methods used without noting deprecation?
- Has the API endpoint URL changed since the doc was written?

### 5. Check Copy-Paste Readiness
- Can someone literally copy the code block and run it?
- Or does it have `<YOUR_API_KEY>` placeholders that need explanation?
- Are placeholders clearly marked vs. looking like real values?
- Is there a clear indication of what to substitute?

## Pass / Fail Criteria

| Verdict | Condition |
|---------|-----------|
| **PASS** | All code blocks are syntactically valid, produce described output, use current APIs/versions, and are copy-paste ready (or clearly mark what needs substitution) |
| **FAIL** | Any code block has syntax errors, produces wrong output, uses deprecated APIs, or would confuse a user trying to run it |

## Failure Feedback Template

When this check fails, the reviewer should comment:

```
❌ Code Tested: FAIL

[file.md, line X] — Code block using `deprecated_method()`:
  This method was removed in v3.0. Replace with `new_method()`.

[file.md, line Y] — Expected output doesn't match:
  Doc shows: `{"status": "ok"}`
  Actual:    `{"status": "success", "code": 200}`
```
