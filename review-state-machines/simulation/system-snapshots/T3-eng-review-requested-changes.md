# T3: Engineering Review — Changes Requested

**Transition:** Developer reviews PR, finds issues, requests changes  
**Trigger:** Developer submits PR review via GitHub with state `changes_requested`  
**Phase:** 4 (Reviewing) → Dev_decision = ISSUES_FOUND → BACK_TO_DRAFTING

## System State

### JIRA
```
DOC-201:
  status:    In Review         ← unchanged (still under review)
```

### GitHub  ← PRIMARY CHANGE
```
PR #42:
  state:              open
  reviews:
    - review #1001 (sarah-chen):
        state:        changes_requested     ← NEW
        comments:     3 inline comments     ← NEW
          line 82:    Python hmac.new() deprecation note needed
          line 31:    API response format wrong (v1 vs v2)
          line 198:   Body parsing middleware section missing
        submitted:    2026-02-11T10:30:00Z
  
  mergeable:          true (no conflicts, but review blocking)
  
  branch feature/DOC-201:
    └── docs/guides/webhooks/setup.md   ← unchanged (writer hasn't fixed yet)
```

### What the Writer Sees
```
Email notification:
  "sarah-chen requested changes on PR #42"
  
GitHub PR page:
  🔴 Changes requested (1 review)
  3 unresolved conversations
  
  Inline comments appear on specific lines of the diff:
  - Line 82: code sample issue
  - Line 31: response format issue  
  - Line 198: missing content
```

## What Data Moved
1. Developer opened PR #42 in GitHub
2. Developer ran checklist mentally (or used diff viewer):
   - Opened diff view → checked code samples (code-tested.md sub-machine)
   - Read through source → checked explanations (explanations-comprehensive.md)
   - Read troubleshooting → found gap (debugging-steps-clear.md)
3. Developer created PR review object with 3 inline comments
4. GitHub sent notification to writer (email + GitHub notification)
5. GitHub marked PR as "changes requested" (blocks merge in branch protection)

## Review → Checklist Mapping

| Comment | Checklist Sub-Machine | Step That Failed |
|---------|----------------------|------------------|
| Line 82: hmac.new() | code-tested.md → Check Syntax Validity | `SYNTAX_ERROR` (soft deprecation) |
| Line 31: API response | code-tested.md → Check Runtime Behavior | `DIVERGES` (v1 vs v2 format) |
| Line 198: body parsing | debugging-steps-clear.md → Check Resolution Paths | `DEAD_END` (missing most common fix) |

## State Machine Position
```
Developer Guide Checklist:
  Code Tested?               → FAIL (2 issues)
  Explanations Comprehensive → PASS
  Debugging Steps Clear?     → FAIL (1 issue)
  
  Dev_decision = ISSUES_FOUND
  → Developer: Request Changes
  → GITHUB_requestChanges (review #1001 submitted)
  → SUBMITTED
  → Writer returns to Phase 3 (Drafting) to fix
```

## Key Observation
The review comments are the system's mechanism for communicating WHAT failed.
The GitHub review state (`changes_requested`) is the mechanism for BLOCKING progress.
The writer must:
1. Read the comments (data flows GitHub → writer's brain)
2. Fix the issues (edit local files)
3. Push new commits (data flows local → GitHub)
4. Re-request review (GitHub notifies reviewer)
