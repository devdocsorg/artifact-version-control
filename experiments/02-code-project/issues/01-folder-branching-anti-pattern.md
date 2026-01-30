# Issue: Folder-Based Branching is an Anti-Pattern for Code

## Severity: High

## Description
The prompt's folder-based branching (copying entire artifact/ to Forked_From/ and artifact/) 
duplicates what git branches already provide. For code projects, this creates:

- **Massive commits**: 76 files changed for 3 branches on a 14-file project
- **Fragility**: Untracked files are wiped by `git checkout` to another branch
- **Wasted disk**: O(project_size × branch_count) duplication
- **Confusion**: Two branching systems (git + folders) with overlapping responsibilities

## Evidence
- Session 1 lost ALL experiment data due to branch-switching destroying untracked files
- Branch 3 (1-line fix) required copying 14 files twice (28 copies) to change 3 lines
- The 76-file commit contained ~90% duplicate content

## Recommendation
For code artifacts: use git branching exclusively. The prompt should only add:
1. `summary.md` (high-level overview, refactoring maps)
2. `PR.md` (intent, decisions, review focus)
3. `history.md` (human-readable changelog)

Eliminate: `Forked_From/`, duplicate `artifact/`, per-file `.diff` files
