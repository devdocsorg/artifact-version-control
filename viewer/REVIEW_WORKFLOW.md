# Manual Review Workflow Analysis

## What a Reviewer Looks For (by concern)

### 1. Content Accuracy — "What actually changed?"
- **What they check:** Every addition, removal, modification
- **How they check by hand:** Read each diff chunk, verify it makes sense
- **Tool needed:** Clean unified diff with clear +/- markers, good context lines
- **Current state:** ⚠️ Diff is split into many small chunks that are hard to follow

### 2. Document Flow — "Does it read well now?"
- **What they check:** Does the document flow logically after changes? Do sections connect? Is there redundancy?
- **How they check by hand:** Open the new version and read it top-to-bottom
- **Tool needed:** Full "new version" view — complete reconstructed file, no diff noise
- **Current state:** ❌ Not available — reviewer can only see fragmented chunks

### 3. Rendered Appearance — "How does it actually look?"
- **What they check:** Does formatting work? Do tables render? Do links make sense? Headers hierarchy?
- **How they check by hand:** Open in a markdown previewer or browser
- **Tool needed:** Live rendered markdown/HTML preview
- **Current state:** ❌ Not available — only raw source shown

### 4. Structural Changes — "Did the organization change?"
- **What they check:** Were sections moved, renamed, reordered? Does the hierarchy make sense?
- **How they check by hand:** Compare before/after table of contents
- **Tool needed:** Outline/TOC comparison, or side-by-side rendered view
- **Current state:** ❌ Not available

### 5. Before/After Comparison — "How does old vs new compare visually?"
- **What they check:** Side-by-side comparison of rendered output
- **How they check by hand:** Open both versions in two browser tabs and flip between them
- **Tool needed:** Side-by-side rendered preview, or toggle between old/new
- **Current state:** ⚠️ Source-level split exists but no rendered comparison

### 6. Deleted Content — "Did we lose anything important?"
- **What they check:** Was removed content truly redundant, or was important info lost?
- **How they check by hand:** Read removed sections carefully, cross-reference with new content
- **Tool needed:** Clear deleted content view, ideally with "was this content moved?" indicators
- **Current state:** ⚠️ Shown in diff but buried among other changes

---

## Reviewer Workflow Per File Type

### Markdown Docs (README, guides, API docs)
1. Skim change summary → understand scope
2. Read diff for content accuracy
3. Read new version for flow/coherence
4. Preview rendered markdown for appearance
5. Compare before/after structure

### CSV/Data Files
1. Check what rows/columns changed
2. Verify data values are correct
3. Look for patterns (all Q4? specific region?)
4. Compare summary statistics

### Code Files
1. Read diff for logic changes
2. Check if tests cover new code
3. Verify style consistency

---

## Experiments

### A: Tabbed File Cards
Each file card has tabs: **Changes | Source | Preview**
- Minimal change to current layout — adds capabilities inline
- Good for: scanning across many files quickly

### B: Focused Single-File Review
One file at a time, full width. Toolbar with mode switcher.
- Modes: **Diff | Source | Preview | Split Compare**
- Good for: deep review of individual files, less visual noise

### C: Guided Review Dashboard
Review checklist per file. Side-by-side comparisons as default.
- Tracks what you've reviewed, surfaces concerns
- Good for: thorough, structured review process
