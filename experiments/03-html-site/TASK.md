# Task: Run Experiment 03 — HTML Site

## Your Mission

You are testing the "Artifact Branch Workflow" prompt (v1) with a static HTML/CSS site — a format where visual rendering matters and text diffs alone miss the point.

## Steps

### Phase 1: Setup
1. Read `/Users/jacksonmills/clawd/artifact-version-control/SUB_AGENT_CONTEXT.md` for rules
2. Read `/Users/jacksonmills/clawd/artifact-version-control/prompt/v1-original.md` for the prompt
3. Work in `/Users/jacksonmills/clawd/artifact-version-control/experiments/03-html-site/`
4. Start a `LOG.md` — write to it constantly

### Phase 2: Create the Artifact
Create a simple 3-page portfolio site:
```
outputs/main/artifact/
├── index.html         # Home page
├── about.html         # About page
├── projects.html      # Projects showcase
├── css/
│   └── styles.css     # All styles
└── images/            # (empty, placeholder refs)
```
Make the HTML valid and styled nicely. Use a browser to verify rendering.
Initialize `outputs/main/history.md` with a v1 commit.

### Phase 3: Test Feature Branches

**Branch 1: `redesign-nav`**
- Change the navigation from horizontal to a hamburger menu
- Affects all 3 HTML files + CSS
- This is a visual change — text diff alone won't show the impact

**Branch 2: `add-blog-page`**
- Add a new blog.html page
- Update navigation in all pages to include it
- Add blog-specific CSS

**Branch 3: `dark-mode-theme`**
- Add a dark mode CSS variant
- Only changes styles.css (mostly)
- Huge visual impact, minimal code change

### Phase 4: Visual Diff Challenge
For each branch, try to generate a diff that conveys the VISUAL change:
- Can you screenshot before/after using the browser tool?
- Can you embed visual comparisons in the diff?
- Is a text diff of HTML/CSS sufficient to understand the visual change?

### Phase 5: Evaluate
Score each branch on all 5 dimensions.
Pay special attention to: how well does the diff convey visual changes?
Write results to `RESULTS.md`.

### Phase 6: Report
- Update `/Users/jacksonmills/clawd/artifact-version-control/LEARNINGS.md`
- Git commit and push
- Focus on: how should the prompt handle visual artifacts? What's missing?

## Key Questions
1. Is a text diff of HTML sufficient, or do you need visual before/after?
2. How should CSS-only changes be diffed? The file diff is tiny but the visual impact is huge.
3. Can you use the browser tool to generate visual diffs? How?
4. What testing makes sense for HTML? Does the test checklist capture it?
5. How should the prompt handle "cascading" changes (CSS change affects all pages)?

## Remember
- LOG AS YOU GO
- Commit frequently
- Use the browser to actually render the pages and compare
- Update LEARNINGS.md when you discover something
