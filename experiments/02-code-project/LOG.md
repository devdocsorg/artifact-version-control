# Experiment 02 — Code Project LOG

## Session 2 (2025-02-01): Rebuild & Complete

Previous session had git branch-switching issues — commits landed on wrong branches,
workflow artifacts were lost. This is itself a critical finding:

**META-FINDING: The folder-based workflow creates massive file duplication. When combined 
with git branch operations, it's extremely fragile. A single wrong `git checkout` can 
wipe out dozens of untracked files. The prompt's directory structure fights git.**

Rebuilt from committed v1.0.0 baseline. All 3 branches executed cleanly this time.

---

## Phase 2: Artifact Created
- csvjson Python CLI: cli.py, converter.py, validators.py, formatters.py
- Tests: 20 passing, virtual env at /tmp/csvjson-venv2
- history.md and test_checklist.md initialized

## Phase 3: Feature Branches

### Branch 1: add-yaml-output ✅
- Feature addition across 7 files
- Added YAML formatter, CLI choice, validator entry, dependency, docs, tests
- Tests: 20 → 28
- Workflow: summary.md + PR.md added context. Per-file .diff files were more work than value.
- **Observation:** The [UNCHANGED]/[MODIFIED] format is clunky for code. `diff -u` is better.

### Branch 2: refactor-validators ✅ ⭐ STAR RESULT
- Structural refactor: split validators.py into schema_validators.py + type_validators.py
- Tests: 28 → 41
- **KEY FINDING:** The Refactoring Map in summary.md is the single most valuable output 
  of this entire experiment. It shows MOVED vs. NEW code — something git fundamentally 
  cannot express for file-split operations.
- Git diff: 166 lines of code appearing/disappearing with no structural context.
- Prompt diff: Clear map of what moved where, what's unchanged, what's genuinely new.

### Branch 3: fix-unicode-bug ✅
- Surgical 1-line fix (encoding utf-8 → utf-8-sig) + 2 test cases
- Tests: 41 → 43
- **KEY FINDING:** The workflow is catastrophically disproportionate for small fixes.
  Copied 14 files twice to change 3 lines. Git diff: 51 lines, perfectly clear.

## Phase 4: Native Git Diff Comparison
- Branch 1: 123-line diff (clear, precise, no context on "why")
- Branch 2: 166-line diff (shows add/delete, CANNOT show code movement)
- Branch 3: 51-line diff (crystal clear, zero overhead needed)
- Saved all to samples/ directory

## Phase 5: Scoring Complete → RESULTS.md
- Overall: 3.1/5
- Best dimension: Completeness (5.0) — the prompt enforces accounting for all files
- Worst dimension: Workflow Friction (1.7) — folder-based branching is punishing for code

## Phase 6: Writing LEARNINGS.md and pushing
