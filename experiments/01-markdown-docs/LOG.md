# Experiment 01 — Markdown Documents — LOG

## Session Start
- **Date:** 2025-01-31
- **Prompt version:** v1-original.md
- **Artifact type:** Markdown documents (API documentation set)
- **Goal:** Test whether the Artifact Branch Workflow produces useful, human-readable diffs for markdown documents

---

## Phase 1: Setup
- [x] Read SUB_AGENT_CONTEXT.md
- [x] Read v1-original.md (the prompt)
- [x] Read TASK.md
- [x] Read scoring-rubric.md
- [x] Created git branch `experiment/01-markdown-docs`
- [x] Started LOG.md

### Initial Observations on the Prompt
- The prompt is artifact-type-agnostic, but many examples lean toward PowerPoint/code
- For markdown, `diff -u` is explicitly mentioned as a diff method for "Code/Text files"
- The directory structure (main/, branches/Active/, etc.) is straightforward
- The test checklist auto-generation is interesting — not sure how useful it is for docs
- The diff format spec (UNCHANGED/REMOVED/MODIFIED/ADDED markers) is detailed but might be overkill when `diff -u` already works great for text

**Friction point #1:** The prompt says `{{OUTPUTS_PATH}}` and `{{ARTIFACT_TYPE}}` are template variables. As an AI following this prompt, I need to decide what to substitute. The prompt doesn't make this automatic — it requires setup. For markdown, I'll use `outputs/` as the path.

---

## Phase 2: Create the Artifact
- Created 5 markdown files in outputs/main/artifact/:
  - README.md (857 bytes) — API overview, TOC, base URL, rate limits
  - authentication.md (1573 bytes) — API key auth + OAuth 2.0 flow
  - endpoints.md (1980 bytes) — Users & Projects endpoints
  - errors.md (1634 bytes) — Error codes and troubleshooting
  - changelog.md (508 bytes) — Version history
- Created outputs/main/history.md with initial commit entry
- Created outputs/branches/{Active,Merged,Canceled}/ dirs
- Git committed: `exp01: initial artifact - API documentation (5 markdown files)`

**Friction point #2:** Had to manually create the branches/ subdirectory structure. The prompt describes it but doesn't specify when to create it. Did it during setup which makes sense.

---

## Phase 3: Feature Branches

### Branch 1: add-pagination-docs

**Setup:**
- Created full branch structure (Forked_From/, artifact/, diff/, reviewed_diffs/)
- Copied main/artifact → Forked_From/artifact + artifact/
- Copied main/history.md → Forked_From/history_snapshot.md
- Created history.md and PR.md
- Created test_checklist.md (first branch trigger)

**Changes made:**
- Added pagination.md (new file, 85 lines, full pagination guide)
- Modified endpoints.md (3 changes: note at top, 2 response format updates)
- Modified README.md (1 line added to TOC)

**Diff generation:**
- Used `diff -u` for standard unified diffs — worked perfectly
- Also created custom format diff per prompt spec (UNCHANGED/MODIFIED/ADDED markers)
- Used `diff -u /dev/null` for new file — clean output

**Observations:**
1. **`diff -u` is clearly superior for markdown.** The unified diff gives line-level context, is universally understood, and took seconds to generate. The custom format took 5+ minutes to write manually and adds very little over `diff -u`.
2. **The custom format has some value for EXPLAINING changes** — the "Reason:" field and human-readable descriptions are nice. But the BEFORE/AFTER blocks are just a worse version of unified diff.
3. **summary.md is genuinely useful.** Even for markdown, having a file-level overview of what changed/added/removed saves time. This is the prompt's strongest diff contribution.
4. **The Forked_From/ snapshot is heavy.** Copying ALL files just to have a diff baseline creates massive duplication. For text files, git already tracks this. But I see why it's needed for binary artifacts.
5. **Friction point #3:** The prompt says to create `reviewed_diffs/` but there's no review happening in this experiment. The structure is fine but the folder sits empty.
6. **Friction point #4:** The prompt's test checklist workflow says to "present to user for approval" — as a sub-agent, I can't do that. Had to skip the approval step.
7. **The PR.md is useful.** Having a structured PR template with original request, summary, and status checklist is solid.

**Time estimate:** Following the full workflow for one branch took ~15 minutes. About 5 min for setup/copies, 3 min for changes, 7 min for diffs + PR. The setup/copy overhead is the main friction.

---

### Branch 2: fix-auth-examples
Starting now...
