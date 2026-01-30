# Issue 01: No Visual Diff Support

## Severity: Critical

## Description
The v1 prompt has no mechanism for visual before/after comparison. For HTML/CSS artifacts, text diffs of code are insufficient — you need to see the rendered output. The dark-mode-theme branch produces ~90 lines of CSS color changes that result in every pixel on every page changing, but the text diff tells a reviewer nothing about whether it looks good.

## Affected Branch Types
- CSS-only changes (colors, spacing, layout)
- Responsive design changes (mobile vs desktop)
- Animation/transition changes
- Any change where the visual output matters more than the code

## Proposed Fix
Add a `[VISUAL]` marker to the diff format:
```
[VISUAL: index.html — Desktop]
Before: diff/screenshots/before/index-desktop.png
After: diff/screenshots/after/index-desktop.png
```

Mandate screenshots in diff/ for any artifact with visual output.

## Evidence
See `samples/branch3-dark-mode/` — light vs dark mode screenshots tell the whole story that the CSS diff cannot.
