# Test Checklist for Markdown Documentation

## Unit Tests (per changed section)
- [ ] Markdown renders without syntax errors (no broken tables, unclosed code blocks)
- [ ] All internal links point to existing files/anchors
- [ ] Code examples use correct syntax highlighting language tags
- [ ] Tables have consistent column counts (no misaligned rows)
- [ ] No orphaned headings (heading with no content below before next heading)

## Integration Tests (whole artifact)
- [ ] README.md table of contents matches actual files in artifact/
- [ ] Cross-file references resolve (e.g., "see [Authentication](authentication.md)" links work)
- [ ] Documentation reads coherently from start to finish
- [ ] No duplicate content across files
- [ ] Changelog reflects all documented features

## Custom Checks
_(none yet — would normally ask user)_

---
Last updated: 2025-01-31
