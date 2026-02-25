# T4: Engineering Review — Approved

**Transition:** Writer fixes issues, dev re-reviews and approves  
**Trigger:** Developer submits PR review with state `approved`  
**Phase:** 4 (Reviewing) → Dev_decision = ALL_PASSED → ENG_APPROVED

## System State

### GitHub  ← PRIMARY CHANGE
```
PR #42:
  state:              open
  commits:            2 (original + fix commit)
  
  branch feature/DOC-201:
    └── docs/guides/webhooks/setup.md   ← UPDATED (fixes applied)
        Changes in fix commit:
        - API response: flat secret → credentials.secret
        - Python: added hmac.new() deprecation note
        - Added body-parsing middleware section (Express, Flask, Django)
  
  reviews:
    - review #1001 (sarah-chen):
        state:        changes_requested
        comments:     3 (all resolved)
    - review #1002 (sarah-chen):            ← NEW
        state:        approved ✅
        body:         "All issues addressed"
        submitted:    2026-02-11T16:15:00Z
    - review from marcus-webb:              pending (not yet submitted)
  
  checks:             passing (CI rebuilt after fix commit)
  
  Status:
    🟢 sarah-chen approved
    ⏳ marcus-webb review pending
```

## What Data Moved (Fix Cycle)
```
1. Writer reads GitHub comments          GitHub → writer's brain
2. Writer edits setup.md locally         brain → local file
3. Writer commits fix                    local file → git commit (b7c8d9e0...)
4. Writer pushes                         local git → GitHub branch
5. Writer resolves conversations         GitHub UI (marks conversations resolved)
6. Writer re-requests review             GitHub API → notification to sarah-chen
7. Developer re-reviews diff             GitHub diff → developer's brain
8. Developer submits approval            developer's brain → GitHub review #1002
9. GitHub sends notification to PM       GitHub → marcus-webb notification
```

## Review State After Engineering Approval
```
Engineering Checklist (Round 2):
  Code Tested?               → PASS ✅ (response format fixed, deprecation noted)
  Explanations Comprehensive → PASS ✅ (unchanged from round 1)
  Debugging Steps Clear?     → PASS ✅ (body parsing section added)
  
  Dev_decision = ALL_PASSED
  → Developer: Approve
  → GITHUB_devApprove (review #1002)
  → ENG_APPROVED
  → Now waiting for PM: Product Review
```

## Key Observation
Between T3 and T4, the data made a round trip:
```
GitHub review comments → writer's brain → local edits → GitHub push → GitHub review
```
This loop is the BACK_TO_DRAFTING cycle in the state machine.
The diff between commit 1 and commit 2 IS the evidence that the feedback was addressed.
The diff viewer can show this as "changes since last review" — the most useful view
for the re-reviewing developer.
