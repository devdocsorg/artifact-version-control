# Learnings — Artifact Version Control Experiments

> **Rule: Log as you go. Never wait until the end. If you don't write it down, you WILL forget.**

## Key Insights

### 1. The Two-Layer Problem (Git + Folder Branches)
When multiple sub-agents work in one repo, they fight over git branches while ALSO creating folder-based branches inside their experiments. For **code** artifacts, this is redundant — git already handles branches. For **non-code** (PowerPoint, images), the folder approach is necessary because git can't diff them. **The prompt should detect the artifact type and recommend: "Use git branches for text, folder branches for binary."**

### 2. Multi-Agent Git Collisions
Sub-agents sharing one git worktree causes constant `checkout` conflicts. Untracked files get overwritten, stashes collide, and branch switches lose uncommitted work. **If using sub-agents, each needs its own worktree or its own clone.** `git worktree add` would solve this.

### 3. DiffBundle as the Universal Interface
The most promising direction: a JSON format (DiffBundle) that any artifact type can produce. Contains typed "Renderables" — code blocks, images, tables, HTML. A single viewer renders all of them. This decouples "how to diff X" from "how to display a diff."

### 4. The Viewer Works
A GitHub-PR-style HTML viewer loaded from DiffBundle JSON works well:
- File sidebar with colored status dots
- Collapsible unchanged sections (critical for large artifacts)
- Side-by-side BEFORE/AFTER for modifications
- Inline commenting per change block
- Approve/Reject/Export actions
- Drag-and-drop loading

### 5. Test Checklist Auto-Generation is Useful
Both exp-01 (markdown) and exp-02 (code) auto-generated sensible test checklists for their artifact types. The prompt's approach of "infer tests from artifact type" works when the AI knows the format well.

### 6. Merge Metadata Gets Lost
When exp-02 merged a branch, the PR.md, diff/, and history.md weren't preserved in the Merged/ folder. **The prompt should explicitly say: "Preserve all branch metadata when moving to Merged/."**

### 7. Diff Quality: Text vs Custom Format
For exp-01 (markdown), the sub-agent generated BOTH `diff -u` output AND a custom format per the prompt spec (UNCHANGED/MODIFIED/ADDED markers). The custom format is more readable for non-developers but the `diff -u` is more precise. **Recommendation: generate both. Use `diff -u` as the canonical diff, custom format as the human-readable summary.**

### 8. The Prompt Is Too Long for Setup
At ~4500 words, the v1 prompt takes significant context. Sub-agents spend a lot of tokens just reading it. Consider splitting into: (a) core workflow rules (~500 words), (b) format-specific appendices loaded on demand.

---

## Experiment Status

### Experiment 01: Markdown Docs ✅ Complete
- Created 5-file API documentation artifact
- 3 feature branches completed (add-pagination, fix-auth, restructure-docs)
- All branches generated diffs (both `diff -u` and custom format)
- Merging worked. All 3 branches merged successfully.
  - Branch 1: clean merge
  - Branch 2: soft conflict (different lines in same file) — resolved via sed
  - Branch 3: TRUE conflict (restructured file + main had other changes) — manual 3-way merge
- Test checklist auto-generated sensibly for markdown
- **Overall score: 3.4/5** — Good for simple changes, breaks on restructuring
- **Key finding:** `diff -u` fails catastrophically on section reordering (242-line diff for a moved block). The prompt's custom format would be better here IF it supported MOVE semantics.
- **Key finding:** summary.md is the most valuable artifact the prompt creates — it's the only thing that saved Branch 3's diff from being useless.
- **Key finding:** Forked_From/ snapshot, despite seeming redundant for text, proved essential for three-way merge conflict resolution in Branch 3.

### Experiment 02: Code Project ✅ Complete
- Created runnable Python CLI tool (csvjson) — 9 source files, 20 initial tests
- 3 feature branches completed:
  - Branch 1: add-yaml-output (feature addition, 7 files, 28 tests)
  - Branch 2: refactor-validators (file split refactor, 7 files, 41 tests)
  - Branch 3: fix-unicode-bug (surgical 1-line fix, 2 files, 43 tests)
- All branches merged. All tests passing.
- **Overall score: 3.1/5** — Good completeness, terrible friction, mixed git integration
- **Key finding: Refactoring Map is the killer feature.** summary.md showing code movement
  (MOVED vs. NEW) provides insight git diff fundamentally cannot. This is the one thing
  that justifies the workflow for code projects.
- **Key finding: Folder-based branching is anti-value for code.** Copying 14 files to 
  Forked_From/ duplicates what `git diff main..branch` gives for free. Creates 76-file 
  commits. Fragile under git checkout (lost data in session 1).
- **Key finding: Workflow ceremony must scale with change size.** A 1-line bugfix should
  not require the same process as a 7-file refactor. Need lightweight mode.
- **Key finding: PR.md is universally useful.** The only artifact that adds value
  across all change types — captures intent, decisions, review focus.

### Experiment 03: HTML Site 🔄 In Progress
- Created 3-page portfolio site with CSS
- Branch 1 (redesign-nav) in progress
- Visual diff challenge: need browser screenshots for before/after

---

## Prompt Version History

| Version | Date | Key Changes | Results |
|---------|------|-------------|---------|
| v1 | 2026-01-30 | Original from Slack thread | Works for text. Multi-agent needs work. DiffBundle viewer is the key innovation. |

---

## Pain Points Discovered

1. **Multi-agent git conflicts** — sub-agents share one worktree, constant checkout collisions
2. **Merge metadata loss** — branch PR.md/diff/ not preserved after merge
3. **Prompt length** — 4500 words is a lot of context to read before starting
4. **Diff format inconsistency** — prompt describes a custom format but `diff -u` is cleaner for text
5. **History drift** — commit history in history.md sometimes not updated (AI forgets)
6. **Two-layer confusion** — git branches + folder branches overlap for text artifacts
7. **Catastrophic overhead for small changes** (exp02) — folder-copy workflow creates 30+ files for a 1-line fix
8. **Folder branching fragility** (exp02) — Forked_From/ and artifact/ copies are untracked files that `git checkout` can destroy. Session 1 lost all experiment data this way.
9. **No code movement detection** (exp02) — prompt says "generate diffs programmatically" but has no mechanism for detecting moved code. The Refactoring Map had to be hand-written.
7. **No MOVE semantics in diffs** — Content moving between files (errors.md → endpoints.md) or sections reordering within a file produce misleading diffs. Need `[MOVED_FROM]`/`[MOVED_TO]` markers.
8. **Manual merge is under-specified** — Prompt detects conflicts well but provides no tools/guidance for actually resolving them. "Flag for manual resolution" is where the hard work starts.
9. **Folder branching is ironically MORE ROBUST than git branching for AI agents** — Folder state survives regardless of which git branch you're on. Git branching requires maintaining stateful awareness of current branch, which AI agents are bad at across tool calls.

## What Works Well

1. **Directory structure** — main/, branches/Active|Merged|Canceled/ is clean
2. **Forked_From snapshot** — critical for merge conflict detection  
3. **PR.md descriptions** — consistently good with full context
4. **Test checklist auto-generation** — produces relevant checks per artifact type
5. **DiffBundle + Viewer** — the universal interface concept works beautifully
6. **Commentable changes** — per-change inline comments are more useful than whole-file comments
7. **summary.md for refactors** (exp02) — Refactoring Map showing code movement is the standout value-add for code projects
8. **Completeness enforcement** (exp02) — the prompt's requirement to account for ALL files (unchanged too) caught gaps that git diff ignores
