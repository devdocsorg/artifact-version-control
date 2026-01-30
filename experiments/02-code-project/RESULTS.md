# Experiment 02 Results — Code Project (Python)

## Overview

**Artifact:** csvjson — a Python CLI tool for CSV-to-JSON conversion  
**Files:** 9 source files + 5 test files at v1.0.0, grew to 11+7 by v1.2.1  
**Branches tested:**
1. `add-yaml-output` — feature addition (new output format, touches 7 files)
2. `refactor-validators` — structural refactor (file split, touches 7 files)
3. `fix-unicode-bug` — surgical bugfix (2 files, 3 changed lines)

**All code is real and runnable.** Tests: 20 → 28 → 41 → 43 across branches.

---

## Scoring

### Branch 1: add-yaml-output (Feature Addition)

| Dimension | Score | Notes |
|-----------|-------|-------|
| Diff Readability | 3 | Per-file diffs readable but [UNCHANGED]/[MODIFIED] markers are clunkier than `diff -u` for code |
| Completeness | 5 | summary.md accounted for all 11 files (7 changed, 4 unchanged) |
| Workflow Friction | 2 | Copying artifact dir twice (Forked_From + working), hand-writing 7 diff files, heavy |
| Format Fit | 3 | Prompt works for code but diff format is inferior to unified diff for text files |
| Git Integration | 3 | summary.md + PR.md add narrative context git lacks. Folder branching is pure overhead. |
| **Average** | **3.2** | |

**Native git diff:** 123 lines, immediately shows all changes. Missing: no "why" context.  
**Prompt workflow:** summary.md adds overview value. PR.md captures decisions. But per-file diffs duplicate what `diff -u` does better.

---

### Branch 2: refactor-validators (Structural Refactor) ⭐

| Dimension | Score | Notes |
|-----------|-------|-------|
| Diff Readability | 4 | **The Refactoring Map in summary.md is excellent.** Shows moved vs. new code. |
| Completeness | 5 | All 15 files accounted for, movement annotations accurate |
| Workflow Friction | 2 | Same folder-copy overhead. But diff output was genuinely worth writing. |
| Format Fit | 4 | The structural narrative format fits refactors better than line-level diffs |
| Git Integration | 4 | **Genuinely complements git.** Git shows code deleted+added; summary shows it *moved*. |
| **Average** | **3.8** | |

**Native git diff:** 166 lines. Shows validators.py losing 32 lines and two new files gaining ~100 lines. Tells you NOTHING about what's moved vs. new. You'd have to read both new files carefully and mentally diff against the old one.  
**Prompt workflow:** The Refactoring Map is the killer feature:

```
BEFORE:                           AFTER:
validators.py                     schema_validators.py
  ├─ validate_file_path()     →     ├─ validate_file_path()      [MOVED, unchanged]
  └─ validate_output_format() →   type_validators.py
                                    ├─ validate_output_format() [MOVED, unchanged]
                                    └─ validate_delimiter()     [NEW]
```

**This is the clearest win for the prompt workflow.** Git fundamentally cannot express "this code moved to a new file with no changes."

---

### Branch 3: fix-unicode-bug (Surgical Bugfix)

| Dimension | Score | Notes |
|-----------|-------|-------|
| Diff Readability | 3 | Fine, but adds nothing over git diff |
| Completeness | 5 | Complete |
| Workflow Friction | 1 | **Absurd overhead.** Copied 14 files to Forked_From/ + 14 files to artifact/ to change 3 lines. |
| Format Fit | 2 | The prompt's full branch ceremony is wildly disproportionate to a bugfix |
| Git Integration | 1 | **Actively harmful.** Git diff: 51 lines, perfectly clear. Workflow: created 30+ files. |
| **Average** | **2.4** | |

**Native git diff:** 51 lines. You can read it in 10 seconds. The fix is obvious.  
**Prompt workflow:** Created 30+ files across Forked_From/ and artifact/ directories, wrote PR.md, history.md, summary.md — for a 1-line encoding change. The workflow-to-value ratio is catastrophic.

---

## Overall Scores

| Dimension | B1 (Feature) | B2 (Refactor) | B3 (Bugfix) | Average |
|-----------|:---:|:---:|:---:|:---:|
| Diff Readability | 3 | 4 | 3 | **3.3** |
| Completeness | 5 | 5 | 5 | **5.0** |
| Workflow Friction | 2 | 2 | 1 | **1.7** |
| Format Fit | 3 | 4 | 2 | **3.0** |
| Git Integration | 3 | 4 | 1 | **2.7** |
| **Branch Total** | **3.2** | **3.8** | **2.4** | **3.1** |

---

## Key Findings

### 1. The workflow has ONE killer feature for code: structural narrative

The summary.md's ability to express **code movement** and **refactoring structure** is genuinely valuable and has no git equivalent. `git diff -M` detects renamed files but cannot detect split files. The Refactoring Map pattern is worth extracting and standardizing.

### 2. For everything else, git diff wins

For feature additions and bugfixes, `diff -u` is faster to generate, more precise, and easier to read than the prompt's [UNCHANGED]/[MODIFIED]/[ADDED] format. The prompt's diff format was designed for non-text artifacts (PowerPoint, etc.) and it shows.

### 3. Folder-based branching is ANTI-VALUE for code

This is the harshest finding. For code projects:
- Git already tracks branches perfectly
- Copying 14 files to `Forked_From/` duplicates what `git diff main..branch` gives you for free
- The duplication creates **76-file commits** for simple changes
- It's fragile under `git checkout` (the previous session lost data this way)
- It wastes disk space proportional to project size × number of branches

### 4. PR.md is the most universally useful artifact

PR.md adds genuine value across all branch types — it captures intent, decisions, and review focus. This maps directly to GitHub/GitLab PR descriptions. For an AI agent workflow, this is valuable self-discipline.

### 5. Workflow friction is the biggest problem

The workflow demands ~40% overhead for bookkeeping (directory copies, manual diff generation, multiple metadata files) with proportional value only for complex structural changes. For the other 80% of code changes (features + bugfixes), most of that overhead is waste.

### 6. Test checklist is useful but redundant with CI

The prompt's test checklist generation produces reasonable tests. But code projects already have pytest, CI pipelines, and PR checks. The checklist adds value mainly for AI agents working without CI — a real but narrow use case.

---

## Comparison: When Does the Workflow Beat Git?

| Change Type | Git Diff | Prompt Workflow | Winner |
|-------------|----------|-----------------|--------|
| **Small bugfix** | Perfect clarity, zero overhead | Massive overhead, no added insight | **Git** |
| **Feature addition** | Shows what changed, not why | summary.md + PR.md add context | **Tie** |
| **File rename** | `git diff -M` handles it | Redundant | **Git** |
| **File split/refactor** | Shows add+delete, no structure | Refactoring Map is excellent | **Prompt** |
| **Cross-project sweep** | Each file change is isolated | summary.md links related changes | **Prompt** |
| **Binary artifacts** | Useless | Essential | **Prompt** |

---

## Recommendations for v2

1. **For code: use git branching, not folder branching.** Eliminate Forked_From/ entirely. Use `git diff` for line-level diffs. Only add summary.md and PR.md as supplementary artifacts.

2. **Make summary.md the primary value-add.** Standardize the Refactoring Map pattern. For code, the summary should link to git diff rather than replacing it.

3. **Scale ceremony to change size.** A 1-line bugfix should not require the same workflow as a 7-file refactor. Add a "lightweight" branch mode.

4. **Use `diff -u` for code diffs.** The [UNCHANGED]/[MODIFIED] format is designed for non-text artifacts. For code, embed or link to standard unified diffs.

5. **Keep PR.md.** It works everywhere.

6. **Detect artifact type and adapt.** Code vs. PowerPoint vs. CSV need fundamentally different diff strategies. The prompt should branch on type.
