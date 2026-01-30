# Experiment 03 Results — HTML/CSS Site

## Overview
Tested the Artifact Branch Workflow (v1) with a 3-page static portfolio site. Created 3 feature branches testing different types of changes: structural/behavioral (hamburger nav), additive (new blog page), and purely visual (dark mode theme).

## Branch Scores

### Branch 1: redesign-nav (Hamburger Menu)
| Dimension | Score | Notes |
|-----------|-------|-------|
| Diff Readability | 2 | Text diff shows CSS selectors and HTML markup changes but CANNOT convey the visual result — you can't see the hamburger icon, the animated X transition, or the mobile dropdown from code alone |
| Completeness | 4 | All file changes accounted for. Missing: no way to show the "desktop unchanged" fact |
| Workflow Friction | 3 | Branch setup worked fine. Generating diffs was mechanical. But the diff format has no concept of "visual before/after" |
| Format Fit | 2 | The prompt assumes text diffs are sufficient. For HTML/CSS, they are not — especially for responsive/interactive changes |
| Git Integration | 3 | Folder branches work fine alongside git. No conflict, no synergy either |
| **Average** | **2.8** | |

### Branch 2: add-blog-page (New Page + Nav Update)
| Dimension | Score | Notes |
|-----------|-------|-------|
| Diff Readability | 4 | New page = entire file is "Added" which is clear. Nav changes in existing pages are small insertions — easy to read |
| Completeness | 5 | All changes captured: new file, nav updates in 3 files, CSS additions |
| Workflow Friction | 3 | Same as branch 1 — workflow works but feels heavy for "add a page" |
| Format Fit | 3 | Works better for additive changes. Text diff of "new file" is natural. Still can't tell if the blog page *looks* good |
| Git Integration | 3 | Neutral |
| **Average** | **3.6** | |

### Branch 3: dark-mode-theme (CSS-Only, Huge Visual Change)
| Dimension | Score | Notes |
|-----------|-------|-------|
| Diff Readability | 1 | **THE WORST CASE.** The diff shows ~90 lines of hex color changes. A reviewer cannot determine: Does it look good? Is contrast sufficient? Were any elements missed? This is completely unreviewable from text alone |
| Completeness | 4 | All changes accounted for. But "completeness" of a visual change means showing ALL affected pages, not just the CSS diff |
| Workflow Friction | 3 | Same as others |
| Format Fit | 1 | The prompt completely fails here. CSS-only changes with massive visual impact need a fundamentally different diff approach |
| Git Integration | 3 | Neutral |
| **Average** | **2.4** | |

## Overall Experiment Score

| Dimension | Average Across Branches |
|-----------|------------------------|
| Diff Readability | 2.3 |
| Completeness | 4.3 |
| Workflow Friction | 3.0 |
| Format Fit | 2.0 |
| Git Integration | 3.0 |
| **Overall** | **2.9** |

## Key Findings

### 1. The Visual Diff Gap (Critical)
The v1 prompt has NO mechanism for visual diffs. For HTML/CSS artifacts:
- Text diffs of CSS are almost useless for understanding visual changes
- The diff format specification covers `[MODIFIED]`, `[ADDED]`, etc. but only for code text
- There's no `[VISUAL: before.jpg → after.jpg]` marker type
- The prompt says "render visual comparison if possible" for binary files, but HTML/CSS isn't binary — it's text that produces visual output. The prompt doesn't handle this intermediate case.

### 2. Code/Visual Mismatch Severity Scale
Different types of HTML/CSS changes have different code-to-visual ratios:

| Change Type | Code Size | Visual Impact | Text Diff Usefulness |
|-------------|-----------|---------------|---------------------|
| Add new page | Large | Large | ✅ Good — new content is readable |
| Change nav markup | Medium | Medium | ⚠️ Partial — structure clear, appearance not |
| CSS color scheme | Small | **Enormous** | ❌ Useless — hex codes tell you nothing |
| CSS layout change | Small | Large | ❌ Bad — `flex-direction: column` doesn't convey layout |
| Responsive changes | Medium | **Context-dependent** | ❌ Terrible — diff doesn't show different viewports |

### 3. Browser Screenshots Are the Missing Tool
In this experiment, I used the browser tool to:
- Verify initial rendering
- Capture mobile before/after for hamburger menu (resize viewport)
- Capture dark mode before/after (click toggle, re-screenshot)
- Verify blog page styling matches existing design language

**The prompt should mandate screenshots for visual artifacts.** Possible addition to the diff format:
```markdown
[VISUAL: index.html]
- Before: screenshots/before/index-desktop.jpg
- After: screenshots/after/index-desktop.jpg
- After (mobile): screenshots/after/index-mobile.jpg
```

### 4. Cascading Changes Are Invisible
CSS changes affect ALL pages. The diff only shows `styles.css` as modified, but every page renders differently. The prompt needs a concept of "cascade impact" — when a shared resource changes, list all affected artifacts.

### 5. Interactive/Behavioral Changes Can't Be Diffed
The hamburger menu has behavior (click → toggle). There is no way to represent this in a static diff. Animation, hover states, transitions — all invisible.

### 6. What Worked
- Branch structure and naming: clear and organized
- PR.md: good for capturing intent and review guidance
- history.md: adequate for tracking changes
- The diff summary format (table of files) works well for completeness tracking
- The Forked_From snapshot concept is solid for comparison baseline

### 7. The Test Checklist Needs Visual Checks
The prompt's test checklist template includes "Slide positioning correct" for PowerPoint and "Component renders without error" for React. For HTML/CSS, it should include:
- [ ] All pages render correctly at desktop and mobile breakpoints
- [ ] Visual before/after comparison shows intended changes
- [ ] No unintended visual regressions on unchanged pages

## Recommendations for v2

1. **Add a `[VISUAL]` diff marker** for artifacts with visual output
2. **Mandate screenshots** in the diff/ folder for HTML, CSS, PowerPoint, and any visual artifact
3. **Add "cascade impact" tracking** — when a shared file changes, enumerate all affected outputs
4. **Add viewport/state matrix** for responsive artifacts: test at multiple widths
5. **Distinguish "code diff" from "output diff"** — CSS changes are code changes but the output is pixels
6. **Add visual regression detection** — compare screenshots pixel-by-pixel
