# Diff Summary — add-blog-page

## Files Changed
| File | Status | Description |
|------|--------|-------------|
| `blog.html` | Added | New blog listing page with 4 post previews |
| `index.html` | Modified | Added Blog link to navigation |
| `about.html` | Modified | Added Blog link to navigation |
| `projects.html` | Modified | Added Blog link to navigation |
| `css/styles.css` | Modified | Added ~70 lines of blog-specific CSS |
| `images/` | Unchanged | — |

## Visual Impact
- **Nav bar**: 4th link "Blog" appears in all pages
- **New page**: Clean blog listing with date, category tags, post titles, excerpts
- **Existing pages**: Nav slightly wider due to 4th link; otherwise identical

## Visual Evidence
See `samples/branch2-add-blog/`:
- `blog-page.jpg` — The new blog page
- `index-with-blog-nav.jpg` — Home page showing 4-item nav

## Observation on Diffing
For the "add new page" case, text diff works reasonably well — the entire blog.html is "Added" and the nav changes in existing files are small, predictable insertions. The CSS additions are also clearly new blocks.

**However**: You still can't tell from the text diff whether the blog looks good. Does the spacing work? Do the category tags match the existing visual language? A screenshot answers instantly.
