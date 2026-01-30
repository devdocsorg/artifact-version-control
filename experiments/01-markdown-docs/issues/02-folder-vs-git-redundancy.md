# Issue 02: Folder-Based Branching Redundant with Git for Text

## Severity: Medium
## Affected: All branches

## Description
The prompt's folder-based branching system (branches/Active/, Forked_From/ snapshots, etc.) duplicates what git already does natively for text files. Running both systems simultaneously creates:
- Double the storage (full artifact copies in Forked_From/ AND git history)
- Confusion about which system is "authoritative"
- Working tree conflicts when git branch switches wipe folder state
- Agent context loss when git state doesn't match folder state

## Quantification
Each branch required copying 5 files (~6.5KB total) twice:
- Once to Forked_From/artifact/ (baseline)
- Once to artifact/ (working copy)

For 3 branches: ~39KB of redundant copies. In a real project with larger docs, this scales badly.

## Nuance
The Forked_From/ snapshot IS valuable for merge conflict resolution — it serves as the "merge base." But for text files, `git merge-base` provides this for free.

## Proposed Fix
For text-based artifacts:
1. Skip Forked_From/ file copies — store only a git commit hash reference
2. Use `git diff <merge-base>..<branch-tip>` instead of folder comparison
3. Keep folder branching ONLY for binary artifacts where git can't diff
4. OR: make the folder system opt-in per artifact type
