# PR: dark-mode-theme

## Original Request
Add dark mode CSS variant with a toggle button.

## Summary of Changes
- **styles.css**: Added ~90 lines — `@media (prefers-color-scheme: dark)` block, `body.dark-mode` class, `.theme-toggle` button style. Changed: bg, text, heading, accent, card, footer, hero gradient colors.
- **All 3 HTML files**: Added `<button class="theme-toggle">🌙 Dark</button>` in nav + JS toggle script

## What to Review
1. Auto dark mode via `prefers-color-scheme` (OS-level)
2. Manual toggle button in nav → `body.dark-mode` class
3. ALL colors invert properly: backgrounds, text, cards, image placeholders, skills pills, footer
4. Accent color shifts from #e94560 → #ff6b81 (slightly brighter pink for dark bg contrast)
5. Hero gradient darkens appropriately

## ⚠️ This is the KEY test case for visual diffing
The CSS diff is ~90 lines of color value changes. It tells you NOTHING about whether the dark mode looks good, whether contrast is sufficient, or whether any element was missed.

**Without screenshots, this change is unreviewable from a diff alone.**

## Status
- [x] Branch created
- [x] Changes implemented
- [x] Diff generated
- [ ] Ready for review
