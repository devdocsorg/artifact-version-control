# Artifact Version Control — Experiment Repo

**Goal:** Build a git-like workflow with human-understandable diffs that works for ANY artifact format — not just code.

## The Problem

Git is great for code. But many artifacts we work with aren't code:
- PowerPoint decks
- Word documents
- Spreadsheets
- Mixed-format projects (docs + code + data)
- HTML sites

Git's diff UI is designed for line-by-line text changes. When you're doing "swipe across a project" changes (search-and-replace, restructuring, adding sections), git diffs are a bad view. And for binary formats (pptx, xlsx), git can't diff them at all.

## The Approach

We have a prompt that creates a folder-based branching workflow:
- `main/artifact/` — the working version
- `branches/Active/` — in-progress changes
- Each branch includes: forked snapshot, changes, PR description, human-readable diff
- Diffs are format-aware: text gets unified diffs, PowerPoint gets before/after slides, etc.

## What We're Experimenting With

This repo tests the prompt across different artifact types to find:
1. Where the workflow shines
2. Where it breaks
3. How to make diffs truly human-readable regardless of format
4. Whether actual git branching (on the repo) can complement the folder-based branching (in the workflow)

## Structure

```
├── LEARNINGS.md              # Top-level findings (read this first)
├── SUB_AGENT_CONTEXT.md      # Shared context for AI sub-agents
├── prompt/
│   ├── v1-original.md        # The full prompt
│   └── CHANGELOG.md          # Iterations
├── experiments/
│   ├── 01-markdown-docs/     # Test with markdown files
│   ├── 02-code-project/      # Test with multi-file Python project
│   ├── 03-html-site/         # Test with HTML/CSS
│   ├── 04-spreadsheet-csv/   # Test with data files
│   └── 05-mixed-artifacts/   # Test with heterogeneous formats
├── analysis/                 # Cross-experiment comparisons
└── tools/                    # Shared diff tooling
```

## Origin

This started with a PowerPoint editing workflow in [powerpoint-editor](https://github.com/devdocsorg/powerpoint-editor) that used AI to manage slide decks through feature branches with visual diffs. It worked so well for presentations that we wanted to generalize it to work with any artifact type.

See the [Slack discussion](prompt/v1-original.md) for the full context.
