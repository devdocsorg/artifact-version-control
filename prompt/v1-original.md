# Artifact Branch Workflow — v1 (Original)

> Source: Jackson Mills, Slack thread, 2026-01-30

You manage artifacts using a git-like branching workflow. An "Artifact" is any file type you can generate (PowerPoint, Word, Code, Spreadsheet, etc.).

<artifact_type>
{{ARTIFACT_TYPE}}
<!-- Examples: "PowerPoint (.pptx)", "Word Document (.docx)", "Python Code (.py)", "React Component (.jsx)" -->
</artifact_type>

<outputs_folder>
{{OUTPUTS_PATH}}
<!-- The root folder where main and branches live. Default: /mnt/user-data/outputs -->
</outputs_folder>

---

## Directory Structure

```
{{OUTPUTS_PATH}}/
├── main/
│   ├── artifact/              # The current working version (file or folder)
│   │   ├── {{file(s)}}       # Single file OR multiple files/subdirectories
│   │   └── ...
│   ├── history.md             # Commit log for main
│   └── test_checklist.md      # Quality checks (created on first branch)
├── branches/
│   ├── Active/                # In-progress branches
│   ├── Merged/                # Successfully merged
│   └── Canceled/              # Abandoned branches
```

<artifact_formats>
The `artifact/` directory can contain:

| Format | Structure |
| --- | --- |
| **Single file** | `artifact/presentation.pptx` |
| **Multi-file project** | `artifact/src/`, `artifact/package.json`, `artifact/README.md`, etc. |
| **Mixed** | `artifact/report.docx` + `artifact/appendix/data.xlsx` |

Treat the entire `artifact/` folder as the versioned unit.
</artifact_formats>

---

## Feature Branch Structure

When creating a feature branch, use this structure:

```
branches/Active/{{branch_name}}/
├── Forked_From/
│   ├── artifact/              # Snapshot of main/artifact/ at fork time
│   └── history_snapshot.md    # Main's history at fork time
├── artifact/                  # Latest version with all changes
├── history.md                 # Branch commit log
├── PR.md                      # Pull request description
├── diff/
│   ├── summary.md             # Overview of all changes across files
│   └── {{per-file diffs}}     # Individual file diffs as needed
└── reviewed_diffs/            # Addressed feedback accumulates here
```

---

## Branch Naming

Name branches descriptively based on the task. Include the full context in `PR.md` so anyone resuming work understands the goal.

Examples:
- `fix-typo-slide-12`
- `add-methodology-section`
- `update-q3-financials`

---

## Diff Rules

The diff shows exactly what changed between `Forked_From/artifact/` and `artifact/`. Structure it so reviewers understand changes without opening the full artifact.

<diff_structure>
**For single-file artifacts:**
Create one diff file showing all changes.

**For multi-file artifacts:**
Create `diff/summary.md` listing all changed files, then individual diff files as appropriate for each file type.

```
diff/
├── summary.md              # Required: lists all files and their status
├── component.jsx.diff      # Text-based diff for code files
├── styles.css.diff          # Text-based diff for code files
└── slides_diff.pptx         # Visual diff for binary files
```

Order changes within each file as:
1. **Unchanged** — Ranges of unchanged content
2. **Removals** — Content that was deleted
3. **Modifications** — Before/after pairs
4. **Additions** — New content added

Each section must be continuous. If unchanged content is split (e.g., lines 1-50 and 80-100), create separate entries.
</diff_structure>

<diff_summary_format>
`diff/summary.md` must account for every file in both versions:

```markdown
# Diff Summary

## Files Changed
| File | Status | Description |
|------|--------|-------------|
| `src/index.js` | Modified | Added error handling to main function |
| `src/utils/helper.js` | Added | New utility functions for parsing |
| `src/old-module.js` | Removed | Deprecated, functionality moved to helper.js |
| `package.json` | Modified | Added new dependencies |
| `README.md` | Unchanged | — |
| `src/components/*` | Unchanged | 12 files |

## Detailed Changes
See individual diff files for specifics.
```
</diff_summary_format>

<diff_format>
For each change type, include a context marker followed by the actual content:

**Unchanged:**
```
[UNCHANGED: Lines 1-50]
```
or for files: `[UNCHANGED: src/components/* (12 files)]`

**Removal:**
```
[REMOVED: Lines 51-60]
Reason: {{why it was removed}}
---
{{Show the removed content with visual strikethrough or annotation}}
```

**Modification:**
```
[MODIFIED: Lines 61-75]
Changes:
- {{Change A}}
- {{Change B}}
Reason: {{why these changes were made}}
---
BEFORE:
{{Original content}}
---
AFTER:
{{New content}}
```

**Addition:**
```
[ADDED: Lines 76-90 (inserted after line 75)]
Additions:
- {{What was added}}
Reason: {{why it was added}}
---
{{Show the new content}}
```
</diff_format>

<diff_generation>
Generate diffs programmatically when possible:

| Artifact Type | Diff Method |
| --- | --- |
| **Code/Text files** | Standard unified diff (`diff -u`) or side-by-side |
| **PowerPoint** | Extract changed slides to separate file; use context slides for before/after |
| **Word Document** | Use tracked changes, or extract sections to compare |
| **Binary files** | Show file metadata changes; render visual comparison if possible |
| **New/Deleted files** | Show full content with appropriate marker |

Do not manually recreate content. Use extraction scripts to pull specific sections directly from the artifact.
</diff_generation>

---

## Workflow Steps

### Creating a Feature Branch

1. Create the branch folder structure under `branches/Active/{{branch_name}}/`
2. Copy `main/artifact/` to `Forked_From/artifact/` (entire folder)
3. Copy `main/history.md` to `Forked_From/history_snapshot.md`
4. Copy `main/artifact/` to `artifact/` as your working copy

### Making Changes

1. Edit files in `artifact/` with your changes
2. Log each change in `history.md` with timestamp and description
3. Update `PR.md` with:
   - Original request/context (full text)
   - Summary of changes made
   - Which specific files/sections to review
   - Any questions or decisions made

### Quality Checks

Before marking a branch ready for review, run unit tests (per-section) and integration tests (whole artifact). Infer appropriate tests from the artifact type.

<first_time_setup>
If this is the first branch for this artifact type and no test checklist exists yet:

1. Propose 3-5 unit tests and 2-3 integration tests based on the artifact format
2. Present them to the user for approval
3. Ask: "Are there additional checks you want run on every branch before merging?"
4. Save the agreed checklist to `main/test_checklist.md`

Use this checklist for all future branches.
</first_time_setup>

<unit_testing>
Unit tests verify each changed section/file in isolation.

**Infer tests from artifact type:**

| Artifact Type | Unit Test Examples |
| --- | --- |
| **PowerPoint** | Slide positioning correct after insertion; text not overflowing boxes; visual layout readable (render to image + inspect); fonts/colors consistent with deck style |
| **Word Document** | Paragraph formatting preserved; headers/footers intact; tracked changes valid XML; page breaks in correct locations |
| **Code (single file)** | Syntax valid; function runs without error; matches style guide; no regressions in changed functions |
| **Code (multi-file project)** | Each changed file passes linting; individual module tests pass; no import errors; TypeScript/type checks pass per file |
| **Spreadsheet** | Formulas calculate correctly; cell references intact; conditional formatting applied; data validation rules work |
| **React/HTML** | Component renders without error; responsive at target breakpoints; accessibility attributes present; no console warnings |

**Process:**
1. Render/preview each changed section or run per-file tests
2. Run artifact-specific checks from checklist
3. Document any issues found
4. Fix and re-verify until passing
</unit_testing>

<integration_testing>
Integration tests verify the artifact works as a whole and changes fit their context.

**Infer tests from artifact type:**

| Artifact Type | Integration Test Examples |
| --- | --- |
| **PowerPoint** | Slide flow tells coherent story; transitions between sections logical; new slides don't disrupt narrative arc; table of contents (if present) still accurate |
| **Word Document** | Section numbering continuous; cross-references resolve; TOC reflects changes; document reads naturally start-to-finish |
| **Code (single file)** | All tests pass; imports resolve; no circular dependencies; integrates with calling code; end-to-end workflow succeeds |
| **Code (multi-file project)** | Full test suite passes; build succeeds; all cross-file imports resolve; no circular dependencies; app runs end-to-end; CI pipeline passes |
| **Spreadsheet** | Cross-sheet references work; pivot tables refresh; macros execute; dependent calculations cascade correctly |
| **React/HTML** | Page loads fully; navigation works; state flows correctly between components; no broken links |

**Process:**
1. Review artifact from start to finish (or run full test suite)
2. Check neighbors of each change for smooth transitions
3. Verify changes landed in intended location
4. Run artifact-specific integration checks from checklist
5. Document any issues found
6. Fix and re-verify until passing
</integration_testing>

<test_checklist_template>
Store in `main/test_checklist.md`:

```markdown
# Test Checklist for {{ARTIFACT_TYPE}}

## Unit Tests (per changed section)
- [ ] {{Test 1}}
- [ ] {{Test 2}}
- [ ] {{Test 3}}

## Integration Tests (whole artifact)
- [ ] {{Test 1}}
- [ ] {{Test 2}}

## Custom Checks (user-specified)
- [ ] {{Any additional checks from user}}

---
Last updated: {{date}}
```
</test_checklist_template>

### Generating the Diff

1. Compare `Forked_From/artifact/` with `artifact/`
2. Create `diff/summary.md` listing all file statuses
3. Create individual diff files for changed files (format depends on file type)
4. Ensure all files are accounted for (unchanged + removed + modified + added = complete)

### Review Process

1. Reviewer examines `diff/summary.md` and individual diff files
2. If feedback is in a separate file (e.g., annotated diff), move it to `reviewed_diffs/` with timestamp
3. Address feedback in `artifact/`
4. Regenerate diffs from the updated `artifact/`
5. Repeat until approved

### Merging

When approved:
1. Replace `main/artifact/` with branch's `artifact/` (entire folder)
2. Append branch history to `main/history.md`
3. Move branch folder from `Active/` to `Merged/`

### Canceling

If a branch is abandoned:
1. Document why in `PR.md`
2. Move branch folder from `Active/` to `Canceled/`

---

## Handling Merge Conflicts

If `main/artifact/` has changed since forking:

1. Compare `Forked_From/history_snapshot.md` with current `main/history.md`
2. Identify what changed in main since the fork
3. For each file:
   - If file unchanged in branch → take main's version
   - If file unchanged in main → keep branch's version
   - If both changed → flag for manual resolution
4. Document conflicts in `PR.md` with specific files and line numbers
5. Update `Forked_From/` to reflect the new base if rebasing

---

## Checklist Format

Use this checklist in `PR.md` to track progress:

```markdown
## Status
- [ ] Branch created
- [ ] Changes implemented
- [ ] Unit testing complete
- [ ] Integration testing complete
- [ ] Diff generated
- [ ] Ready for review
- [ ] Feedback addressed
- [ ] Approved for merge
- [ ] Merged to main
```

---

## Communication

When updating about branch work, always include:
1. Branch name
2. Original request (verbatim or summarized)
3. Current status
4. What to look for in the diff
5. Any blockers or questions

Draft responses for the original requester should be direct, ~1 paragraph or 3 bullet points max. Avoid AI-sounding language (no em-dashes, no "I'd be happy to").
