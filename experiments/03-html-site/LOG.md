# Experiment 03: HTML Site — Log

## Session Start
- **Time**: 2025-01-31
- **Branch**: `experiment/03-html-site`
- **Goal**: Test the Artifact Branch Workflow prompt (v1) with a static HTML/CSS portfolio site
- **Key focus**: Visual diffs — text diffs of HTML/CSS miss visual changes

---

## Phase 1: Setup
- [x] Read SUB_AGENT_CONTEXT.md
- [x] Read v1-original.md prompt
- [x] Read TASK.md
- [x] Read scoring-rubric.md
- [x] Created git branch `experiment/03-html-site`
- [x] Created directory structure

## Phase 2: Creating the Artifact
- [x] Created 3-page portfolio site (index.html, about.html, projects.html, css/styles.css)
- [x] Verified all 3 pages render correctly in browser
- [x] Saved baseline screenshots (before/)
- [x] Created test_checklist.md

## Phase 3 — Branch 1: redesign-nav
- [x] Created branch folder structure per prompt
- [x] Copied Forked_From snapshot
- [x] Modified all 3 HTML files: added hamburger button, class on ul, JS toggle
- [x] Modified CSS: added hamburger styles, animated X, mobile dropdown
- [x] Screenshot desktop: identical to before (hamburger hidden)
- [x] Screenshot mobile before: cramped horizontal links
- [x] Screenshot mobile after (closed): clean hamburger icon
- [x] Screenshot mobile after (open): X icon + vertical dropdown
- [x] Generated text diff (diff -ru)
- [x] Wrote diff/summary.md, diff/html-changes.md, diff/styles.css.diff
- [x] Created PR.md and history.md

### Key Observation — Branch 1
The text diff of CSS shows new selectors and properties but CANNOT convey:
1. What the hamburger looks like visually
2. The animated line-to-X transition
3. The feel of the dropdown appearing
4. Whether the shadow/border/spacing looks good

**Visual screenshots are ESSENTIAL** for this type of change. The diff framework from v1 has no built-in support for visual comparisons.
