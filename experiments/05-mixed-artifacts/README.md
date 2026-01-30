# Experiment 05: Mixed Artifacts

## Goal
Test the Artifact Branch Workflow with a project containing multiple file types in one artifact.

## Why This Matters
- Real projects are rarely one format
- A "project" might be: a report (.md) + data (.csv) + visualization (.html) + presentation (.pptx summary)
- The diff system needs to handle heterogeneous content in a single branch
- Most challenging test of the prompt's format-adaptive diff generation

## Test Plan
1. Create a mixed artifact: analysis report (3 markdown files + 1 CSV dataset + 1 HTML dashboard)
2. Feature branch: update the data AND the report that references it
3. Feature branch: add a new visualization page
4. Feature branch: restructure the entire project (move files, rename)
5. Evaluate: does a single diff summary make sense for cross-format changes?

## Artifact
A data analysis project:
```
artifact/
├── README.md
├── data/
│   └── sales_2025.csv
├── analysis/
│   ├── methodology.md
│   └── findings.md
└── dashboard/
    ├── index.html
    └── styles.css
```

## Success Criteria
- Diff summary covers ALL file types coherently
- Cross-file dependencies noted (e.g., "data changed, report references updated")
- Per-file diffs use appropriate format (text diff for .md, data diff for .csv, visual for .html)
- The whole thing reads as one coherent change, not separate diffs stitched together
