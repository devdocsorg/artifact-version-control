# Experiment 03: HTML Site — Log

## Session Start
- **Time**: 2025-01-31
- **Branch**: `experiment/03-html-site`
- **Goal**: Test the Artifact Branch Workflow prompt (v1) with a static HTML/CSS portfolio site
- **Key focus**: Visual diffs — text diffs of HTML/CSS miss visual changes

---

## Phase 1: Setup ✅
- Read all context files
- Created git branch `experiment/03-html-site`

## Phase 2: Artifact Created ✅
- 3-page portfolio site: index.html, about.html, projects.html + css/styles.css
- Dark navy nav/footer, white bg, red accent, serif headings
- Verified rendering in browser — all 3 pages look correct
- Baseline screenshots saved to samples/before/
- test_checklist.md created
- history.md initialized with v1.0

## Phase 3: Feature Branches

### Branch 1: redesign-nav ✅
- Changed horizontal nav to hamburger menu on mobile
- Modified all 3 HTML files (button + class + JS) + CSS
- Screenshotted: mobile before (cramped links), mobile after (hamburger closed), mobile after (open with X)
- Desktop: visually identical — hamburger hidden
- **Key observation**: Text diff cannot convey what the hamburger looks like or how the animation works

### Branch 2: add-blog-page ✅
- Created blog.html with 4 posts (date, tag, title, excerpt, read-more)
- Updated nav in all 3 existing pages
- Added ~70 lines blog CSS
- Screenshotted: blog page, index with 4-item nav
- **Key observation**: Additive changes (new page) work better in text diff than visual changes

### Branch 3: dark-mode-theme ✅
- Added @media (prefers-color-scheme: dark) with full color override
- Added body.dark-mode class for manual toggle
- Added toggle button + JS to all pages
- Screenshotted: light mode, dark mode index, dark mode about
- **KEY FINDING**: ~90 lines of CSS hex values → EVERY PIXEL on EVERY PAGE changes. Text diff is completely useless for judging this change. This is the worst case for text-based diffing.
- Note: sed bug inserted extra toggle button in about.html skills section — fixed manually

## Phase 4: Visual Diff Challenge ✅
- Browser tool successfully captures before/after screenshots
- Mobile viewport simulation (resize to 375px) works for responsive testing
- JS evaluation (click handlers) works for testing interactive states
- Screenshots stored in samples/ directory as evidence

## Phase 5: Scoring ✅
- Overall: 2.9/5.0
- Diff readability: 2.3 (devastating for CSS-only changes)
- Completeness: 4.3 (file tracking works)
- Workflow friction: 3.0 (functional but heavy)
- Format fit: 2.0 (prompt fundamentally misses visual dimension)
- Git integration: 3.0 (neutral)

## Phase 6: Report ✅
- RESULTS.md written with per-branch scores, key findings, recommendations
- LEARNINGS.md to be updated

## Git Issues During Experiment
- Other sub-agents kept switching branches (experiment/01, experiment/02)
- Several commits landed on wrong branch
- Had to cherry-pick, hard-reset, and restore files multiple times
- **Meta-learning**: Parallel sub-agents sharing one git repo is fragile. Need worktrees or separate repos.
