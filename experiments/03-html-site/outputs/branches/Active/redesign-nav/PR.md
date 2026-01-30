# PR: redesign-nav

## Original Request
Replace horizontal navigation with a hamburger menu that activates on mobile (≤768px).

## Summary of Changes
- **All 3 HTML files**: Added `<button class="hamburger">` with 3 bars, changed `<ul>` to `<ul class="nav-links">`, added JS toggle script
- **styles.css**: Added hamburger button styles (hidden desktop), mobile dropdown, animated bars → X transition

## What to Review
1. Desktop: nav should look identical (hamburger hidden)
2. Mobile ≤768px: hamburger appears, tapping toggles vertical dropdown
3. Bars animate into X when active
4. Accessibility: aria-label, aria-expanded

## Status
- [x] Branch created
- [x] Changes implemented
- [x] Diff generated
- [ ] Ready for review
