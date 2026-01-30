# PR: add-blog-page

## Original Request
Add a blog page to the portfolio site and update navigation across all pages.

## Summary of Changes
- **NEW `blog.html`**: Blog listing with 4 posts — each has date, category tag, title, excerpt, and "Read more" link
- **index.html, about.html, projects.html**: Added `<li><a href="blog.html">Blog</a></li>` to nav
- **styles.css**: Added ~70 lines of blog-specific styles (`.blog-list`, `.blog-post`, `.blog-meta`, `.blog-tag`, `.read-more`)

## What to Review
1. Blog page layout and typography
2. Nav updated in ALL existing pages (4th link)
3. Blog tag styling matches existing `.tag` accent color
4. Responsive behavior of blog list

## Status
- [x] Branch created
- [x] Changes implemented
- [x] Diff generated
- [ ] Ready for review
