# Branch History: redesign-nav

## 2025-01-31 — Branch created
Forked from main v1.0 to redesign navigation.

## 2025-01-31 — Hamburger menu implemented
- Added `<button class="hamburger">` with 3 `<span class="hamburger-line">` elements to all 3 HTML files
- Changed `<ul>` to `<ul class="nav-menu">` in all files
- Added JavaScript toggle at bottom of each HTML file
- Added CSS: `.hamburger` styles (hidden on desktop, visible on mobile)
- Added CSS: `.nav-menu` responsive styles (vertical dropdown on mobile)
- Added CSS: `.hamburger.is-active` animation (lines → X)
- Added `aria-label` and `aria-expanded` for accessibility
