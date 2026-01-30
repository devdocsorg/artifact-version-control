# Architecture: Universal Artifact Diff Viewer

## The Big Picture

Two things:

### 1. DiffBundle — The Abstract Interface
A JSON format any artifact type produces diffs in. Format-agnostic. Contains:
- **metadata** (branch, type, author, status)
- **summary** (files changed/added/removed with stats)  
- **changes** (ordered list of Unchanged/Added/Removed/Modified)
- **comments** (review feedback attached to specific changes)

Each change contains **Renderables** — typed content blocks:
- `code` — syntax highlighted text
- `image` — base64 or URL image (for visual diffs)
- `html` — rendered HTML content
- `table` — tabular data with cell-level highlighting
- `diff` — unified diff text
- `slide` — PowerPoint slide rendering

### 2. Format-Specific Generators
Plugins that produce DiffBundles from two versions of an artifact:

| Format | Strategy |
|--------|----------|
| Code/Text | `diff -u` → semantic change blocks |
| PowerPoint | Slide extraction → screenshot before/after |
| HTML/CSS | Text diff + browser screenshot before/after |
| CSV/Data | Semantic data diff (row/column aware) |
| Images | Side-by-side + pixel overlay diff |

### 3. Universal Viewer
Single-page HTML that renders any DiffBundle:
- GitHub-PR-like UI (dark theme, file sidebar, change blocks)
- Collapsible unchanged sections
- Side-by-side BEFORE/AFTER for modifications
- Inline commenting per change
- Approve/Reject/Export actions

## Data Flow
```
Artifact v1 + Artifact v2 → Generator → DiffBundle.json → Viewer → Human Review → Comments.json
```
