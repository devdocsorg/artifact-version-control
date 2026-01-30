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
- Merging worked. Restructure branch tested file deletion + content moves
- Test checklist auto-generated sensibly for markdown
- **Generated DiffBundles and verified in viewer**

### Experiment 02: Code Project 🔄 In Progress
- Created runnable Python CLI tool (csvjson) with 20+ passing tests
- Branch 1 (add-yaml-output) merged successfully
- Branch 2 (refactor-validators) in progress — the "swipe across project" test
- Test checklist auto-generated with appropriate Python checks
- `git diff` comparison saved for branch 1

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

## What Works Well

1. **Directory structure** — main/, branches/Active|Merged|Canceled/ is clean
2. **Forked_From snapshot** — critical for merge conflict detection  
3. **PR.md descriptions** — consistently good with full context
4. **Test checklist auto-generation** — produces relevant checks per artifact type
5. **DiffBundle + Viewer** — the universal interface concept works beautifully
6. **Commentable changes** — per-change inline comments are more useful than whole-file comments
