# HTML Changes — redesign-nav

All 3 HTML files received identical changes to their `<nav>` section and a new `<script>` block.

## Navigation Markup (all pages)

[MODIFIED: Nav section]
Changes:
- Added hamburger button element before the nav links
- Added class `nav-menu` to the `<ul>` element
Reason: Enable mobile hamburger menu toggle

---
BEFORE:
```html
<nav>
  <div class="nav-container">
    <div class="logo">Alex<span>Chen</span></div>
    <ul>
      <li><a href="index.html" class="active">Home</a></li>
      <li><a href="about.html">About</a></li>
      <li><a href="projects.html">Projects</a></li>
    </ul>
  </div>
</nav>
```
---
AFTER:
```html
<nav>
  <div class="nav-container">
    <div class="logo">Alex<span>Chen</span></div>
    <button class="hamburger" aria-label="Toggle navigation" aria-expanded="false">
      <span class="hamburger-line"></span>
      <span class="hamburger-line"></span>
      <span class="hamburger-line"></span>
    </button>
    <ul class="nav-menu">
      <li><a href="index.html" class="active">Home</a></li>
      <li><a href="about.html">About</a></li>
      <li><a href="projects.html">Projects</a></li>
    </ul>
  </div>
</nav>
```

## JavaScript Toggle (all pages)

[ADDED: Before closing `</body>` tag]
Additions:
- Toggle script for hamburger menu
- Click handler to open/close nav
- Auto-close when clicking a nav link
- Accessibility: updates `aria-expanded` attribute
Reason: JavaScript is needed to toggle the mobile menu open/closed

---
```html
<script>
  const hamburger = document.querySelector('.hamburger');
  const navMenu = document.querySelector('.nav-menu');
  
  hamburger.addEventListener('click', () => {
    const isOpen = navMenu.classList.toggle('nav-open');
    hamburger.classList.toggle('is-active');
    hamburger.setAttribute('aria-expanded', isOpen);
  });

  document.querySelectorAll('.nav-menu a').forEach(link => {
    link.addEventListener('click', () => {
      navMenu.classList.remove('nav-open');
      hamburger.classList.remove('is-active');
      hamburger.setAttribute('aria-expanded', 'false');
    });
  });
</script>
```

## Unchanged Sections
[UNCHANGED: All non-nav content in all 3 files — hero, cards, about content, footer]
