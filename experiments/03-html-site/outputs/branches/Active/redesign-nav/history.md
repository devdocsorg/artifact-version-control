# Branch History: redesign-nav

## 2025-01-31 — Branch created
Forked from main v1.0.

## 2025-01-31 — Hamburger menu implemented
- Replaced `<ul>` with `<button class="hamburger">` + `<ul class="nav-links">` in all 3 HTML files
- Added JS toggle script to each page
- CSS: Added `.hamburger` (hidden desktop, flex on mobile), `.bar` styles, `.active` animated X
- CSS: Renamed `nav ul` → `.nav-links`, added mobile dropdown with `position: absolute`
- CSS: Added `.nav-links.open` to show dropdown on toggle
