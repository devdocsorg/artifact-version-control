# Issue 04: Merge Conflict Resolution Has No Tooling

## Severity: High
## Affected: Branch 3 merge

## Description
The prompt describes a clear process for DETECTING conflicts:
1. Compare history snapshots
2. Identify per-file changes
3. Apply rules (unchanged in branch → take main, etc.)

But for TRUE conflicts (both sides modified the same file), the prompt just says "flag for manual resolution" and moves on. The actual WORK of merging — understanding both change sets, composing a new version, verifying correctness — is entirely manual.

## Impact
For the endpoints.md merge in Branch 3, I had to:
1. Read the full 151-line main version
2. Read the full 190-line branch version
3. Understand what main changed (pagination meta + auth headers)
4. Understand what branch changed (reorder + inline errors + new sections)
5. Compose a new 200+ line file that incorporates all changes
6. Verify nothing was lost

This took more time than ALL other merge work combined.

## Proposed Fix
1. For text files: recommend `git merge` or three-way merge tools
2. Provide a merge conflict documentation template (which changes from each side, where they overlap, resolution strategy)
3. Consider a "rebase" workflow where branches update their Forked_From to current main before merging
4. Add word-level diff tools (`diff --color-words`, `wdiff`) for identifying fine-grained changes within conflicting sections
