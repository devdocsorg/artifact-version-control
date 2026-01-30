# Issue 02: No Cascade Impact Tracking

## Severity: High

## Description
When a shared resource (CSS file) changes, all pages that reference it are visually affected. The diff only shows the CSS file as "Modified" but doesn't enumerate the visual impact across all consumers.

## Example
Branch `dark-mode-theme` modifies only `styles.css` and the 3 HTML files (for the toggle button). But the diff doesn't communicate:
- index.html: all colors change, hero gradient changes, cards invert
- about.html: photo placeholder inverts, skills pills adapt, all text color changes
- projects.html: all 6 project cards invert, tags adapt

## Proposed Fix
Add a "Cascade Impact" section to diff/summary.md:
```markdown
## Cascade Impact
| Shared Resource | Changed | Visually Affected Pages |
|-----------------|---------|------------------------|
| css/styles.css  | Yes     | index.html, about.html, projects.html |
```
