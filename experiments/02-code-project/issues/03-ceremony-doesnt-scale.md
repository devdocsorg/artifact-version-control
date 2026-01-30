# Issue: Workflow Ceremony Doesn't Scale with Change Size

## Severity: Medium

## Description
The prompt requires identical ceremony for all changes:
- Create branch folder structure
- Copy Forked_From/
- Copy working artifact/
- Create PR.md, history.md
- Generate diff/summary.md + per-file diffs
- Run unit + integration tests
- Fill out status checklist

For a 7-file refactor, this is appropriate. For a 1-line bugfix, it's absurd.

## Evidence
- Branch 3 (fix-unicode-bug): 3 lines changed, 30+ files created
- Time on workflow bookkeeping exceeded time on actual fix
- Workflow friction score: 1/5

## Recommendation
Add tiered branch modes:
- **Quick fix**: PR.md only (intent + 1-line diff). No Forked_From/, no separate diff files.
- **Standard**: Current workflow minus Forked_From/ (rely on git)
- **Full**: Current workflow (for non-git artifacts where folder branching is necessary)

Let the agent choose based on change scope.
