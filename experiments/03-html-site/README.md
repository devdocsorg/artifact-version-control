# Experiment 03: HTML Site

## Goal
Test the Artifact Branch Workflow with a static HTML/CSS site — a format where visual rendering matters.

## Why This Matters
- HTML changes are text-diffable but the *visual impact* isn't obvious from text diffs
- Similar to PowerPoint in needing "before/after" visual comparisons
- Tests whether the prompt can generate visual diffs (screenshots)
- CSS changes can have cascading visual effects across multiple pages

## Test Plan
1. Create a simple 3-page static site as the initial artifact
2. Feature branch: redesign the navigation
3. Feature branch: add a new page
4. Feature branch: change the color scheme (CSS-only)
5. Evaluate: can a reviewer understand visual changes from the diff alone?

## Artifact
A personal portfolio site (index.html, about.html, projects.html + styles.css).

## Success Criteria
- Text diffs are generated for HTML/CSS files
- Visual before/after is available (screenshots or browser preview)
- CSS-only changes describe their visual impact
- Cross-page effects are noted in the diff summary
