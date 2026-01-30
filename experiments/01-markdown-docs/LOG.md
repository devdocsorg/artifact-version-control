# Experiment 01 — Markdown Documents — LOG

## Session Info
- **Date:** 2025-01-31 (two sessions)
- **Prompt version:** v1-original.md
- **Artifact type:** Markdown documents (5-file API documentation set)
- **Goal:** Test whether the Artifact Branch Workflow produces useful, human-readable diffs for markdown documents

---

## Phase 1: Setup
- [x] Read SUB_AGENT_CONTEXT.md, v1-original.md, TASK.md, scoring-rubric.md
- [x] Created git branch `experiment/01-markdown-docs`
- [x] Started LOG.md

### Initial Prompt Observations
- Artifact-type-agnostic prompt, examples lean PowerPoint/code
- `diff -u` explicitly mentioned for "Code/Text files" — appropriate
- Directory structure (main/, branches/Active|Merged|Canceled/) is clear
- Test checklist auto-generation — unclear value for docs
- Custom diff format (UNCHANGED/REMOVED/MODIFIED/ADDED) feels overkill for text

**Friction point #1:** Template variables `{{OUTPUTS_PATH}}` and `{{ARTIFACT_TYPE}}` require manual substitution before use.

---

## Phase 2: Create the Artifact
Created 5 markdown files for a fictional API:
- `README.md` — API overview, TOC, base URL, rate limits
- `authentication.md` — API key auth + OAuth 2.0 flow
- `endpoints.md` — Users & Projects endpoint reference
- `errors.md` — Error codes and troubleshooting
- `changelog.md` — Version history

Also created `outputs/main/history.md` with initial commit.

**Friction point #2:** Had to manually create branches/{Active,Merged,Canceled} dirs. Prompt doesn't specify when.

---

## Phase 3: Feature Branches

### Branch 1: add-pagination-docs
**Task:** Add pagination section to endpoints.md, new pagination.md, update README.md TOC.

**Workflow execution:**
1. Created branch folder structure (Forked_From/, artifact/, diff/, reviewed_diffs/)
2. Copied main/artifact → Forked_From/artifact/ and artifact/ (working copy)
3. Copied main/history.md → Forked_From/history_snapshot.md
4. Created branch history.md and PR.md
5. Since first branch → created test_checklist.md per prompt
6. Made changes: new file (pagination.md), modified endpoints.md (3 spots), modified README.md (1 line)
7. Generated diffs using `diff -u` — worked perfectly
8. Also created prompt-format custom diff for comparison
9. Created diff/summary.md
10. Updated PR.md with summary and status

**Observations:**
- `diff -u` took seconds and was perfectly readable
- Custom format (UNCHANGED/MODIFIED/ADDED markers) took 5+ minutes to write manually
- Custom format's "Reason:" field was the only valuable addition over `diff -u`
- `summary.md` was genuinely useful — file-level overview saves time
- `Forked_From/` snapshot duplicates all files (~6.5KB × 2 copies) just for diffing
- `reviewed_diffs/` dir sat empty — no review process happening
- Test checklist says "present to user for approval" — impossible for autonomous agent

**Friction point #3:** Copying the full artifact for Forked_From/ is heavy for text files (git already tracks this).
**Friction point #4:** Test checklist requires user interaction that may not be available.

### Branch 2: fix-auth-examples
**Task:** Fix incorrect auth code examples, update endpoint auth references.

**Changes made:**
- authentication.md: Major rewrite — API key header (Bearer → X-API-Key), Content-Type headers, OAuth scope format, missing params, security notes
- endpoints.md: sed replacement of auth header in 3 curl examples

**Diff generation:**
- `diff -u` for authentication.md: 89 lines, very readable
- `diff -u` for endpoints.md: 29 lines, trivial
- summary.md: properly categorized all 6 files

**Observations:**
- For a file with many scattered changes (authentication.md), unified diff was still clear
- The 89-line diff was readable because changes were contextual (code blocks are clear boundaries)
- summary.md "Detailed Changes" section (human prose) added real value for auth.md where the diff was long

### Branch 3: restructure-docs
**Task:** Reorder endpoints.md sections, move error codes inline, delete errors.md, update README.md.

**Changes made:**
- endpoints.md: Completely restructured — Projects before Users, inline error tables per endpoint, Common Errors section
- errors.md: Deleted (content moved to endpoints.md)
- README.md: Removed errors.md links, updated endpoints description

**Diff generation:**
- `diff -u` for endpoints.md: **242 lines** — nearly every line shows as changed
- This is the KEY FAILURE of `diff -u` for restructuring: it can't detect moved blocks
- README.md diff: 17 lines, clean
- errors.md diff: noted as deleted

**Observations:**
- **`diff -u` fundamentally fails for section reordering.** It sees moves as delete+add, making the diff incomprehensible.
- The prompt's custom format would have been BETTER here — you could write `[MOVED: ## Projects section from lines 70-140 to lines 5-75]`
- summary.md was CRITICAL for this branch — without it, the 242-line diff is useless
- For restructuring changes, human-written narrative diffs > programmatic diffs

---

## Phase 4: Merge Testing

### Merge 1: add-pagination-docs → main
- **Conflict:** None. Clean merge.
- **Process:** Replace main/artifact/ with branch artifact/, append history, move to Merged/.
- **Observation:** Straightforward. The prompt's merge workflow is clear for clean merges.

### Merge 2: fix-auth-examples → main (after Branch 1 merged)
- **Conflict detection:** Compared Forked_From/history_snapshot.md with current main/history.md → main had new v1.1 entry.
- **File analysis:**
  - endpoints.md: Changed in both main (pagination meta) and branch (auth headers). Different lines → soft conflict.
  - README.md: Changed only in main (pagination link) → take main.
  - authentication.md: Changed only in branch → take branch.
- **Resolution:** Applied branch's sed fix to main's current endpoints.md. Clean.
- **Observation:** The prompt's conflict detection process (compare history snapshots → per-file analysis) worked well. The "if file unchanged in branch → take main's version" rule was correct and easy to apply.

### Merge 3: restructure-docs → main (after Branches 1+2 merged)
- **Conflict detection:** Main had gone through v1.1 (pagination) and v1.2 (auth fixes) since fork.
- **File analysis:**
  - endpoints.md: **TRUE CONFLICT** — branch restructured entire file while main had pagination meta + auth headers. Cannot auto-merge.
  - README.md: **CONFLICT** — main added pagination link, branch removed errors link. Different changes but overlapping area.
  - errors.md: Branch deleted, main unchanged → safe delete.
  - authentication.md: Main changed (auth fixes), branch unchanged → take main.
  - pagination.md: New in main since fork → keep.
- **Resolution:** Manual merge of endpoints.md — took branch's restructured layout, applied main's 3 additions (pagination note, meta objects, X-API-Key headers). Manual merge of README.md — combined both changes.
- **Observation:** The prompt's conflict resolution process is well-described but the actual WORK of manual merging is entirely on the agent. For endpoints.md, this was hard — I had to understand both sets of changes and compose a new version. The Forked_From/ snapshot was essential for this — without it, I couldn't have determined what each side changed.

**Key learning:** The Forked_From/ snapshot, which felt like unnecessary duplication for text files, proved CRITICAL for three-way merge conflict resolution. It's the common ancestor that makes merge analysis possible.

---

## Phase 5: Meta-Observations

### Git vs. Folder-Based Branching
Running this experiment exposed a brutal irony: I was using folder-based branching (the prompt's system) INSIDE git branches, and the two systems constantly fought each other. Files committed on wrong git branches, working trees wiped by git checkouts, stash conflicts — the overhead was enormous.

For text/markdown artifacts, the folder-based system is redundant with git. Git already does branching, diffing, and merging — better than folders. The folder system adds value only when:
1. The artifact is binary (git can't diff it)
2. You need to see multiple versions simultaneously (folders let you)
3. The AI needs explicit state tracking (can't rely on git log)

### What the Prompt Gets Right
1. **summary.md** — Invaluable regardless of artifact type
2. **PR.md** — Structured context for changes
3. **Forked_From/ for merge conflicts** — Essential for three-way merge
4. **History tracking** — Useful audit trail
5. **Test checklist** — Good idea, needs adaptation per type

### What the Prompt Gets Wrong for Markdown
1. **Custom diff format is worse than `diff -u`** for line-level changes
2. **Custom diff format is BETTER than `diff -u`** for structural changes (moves, reorders)
3. **Full artifact copy to Forked_From/** is wasteful for text (git tracks this)
4. **reviewed_diffs/** never gets used in practice
5. **Merge conflict process** needs tools, not just instructions

---

## Session Issues (Meta)
This experiment was severely impacted by git branch management issues:
- Commits repeatedly landed on wrong git branches due to agent context loss between tool calls
- Working tree files were wiped by branch switches
- Cherry-picking created inconsistent states
- Had to restore files from git history multiple times
- Total experiment time roughly doubled by these issues

This is itself a finding: **the folder-based workflow, while redundant with git for text, is MORE ROBUST against context loss.** The folder state survives regardless of which git branch you're on. Git branching requires maintaining stateful awareness of the current branch, which AI agents are bad at.
