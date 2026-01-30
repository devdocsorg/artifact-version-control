# Prompt Changelog

## v1 — 2026-01-30 (Original)
- Source: Jackson Mills, Slack thread
- Full abstract workflow: directory structure, feature branches, diffs, testing, merging
- Tested extensively with PowerPoint in `powerpoint-editor` repo
- Known issues from real use:
  - Diff presentation inconsistent (tags on slides vs in-between slides, random colors)
  - History tracking drifts (AI forgets to update commit log)
  - Merge conflict detection is described but undertested
  - Test checklist first-time setup is useful but rarely exercised
  - Works great for single-artifact single-format repos
  - Multi-format, multi-file projects untested with this prompt
