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
Starting artifact creation...
