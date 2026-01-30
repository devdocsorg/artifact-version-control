# Experiment 01: Markdown Documents

## Goal
Test the Artifact Branch Workflow with markdown files — the simplest text-based format.

## Why This Matters
- Markdown is the easiest format to diff (text-native)
- If the workflow can't produce clean diffs for markdown, it won't work for anything harder
- Establishes a baseline for comparison with other formats

## Test Plan
1. Create a sample multi-page markdown document as the initial artifact
2. Create a feature branch that adds a new section
3. Create a feature branch that modifies existing content
4. Create a feature branch that restructures (reorders sections)
5. Test merge conflict detection (overlapping changes)
6. Evaluate diff quality at each step

## Artifact
A technical documentation site with 3-5 markdown files covering a fictional API.

## Success Criteria
- Diffs clearly show what changed and why
- All files accounted for in summary
- Workflow friction is low (score ≥ 4/5)
- Merge conflicts are detected and described
