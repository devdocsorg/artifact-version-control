# Experiment 02: Code Project

## Goal
Test the Artifact Branch Workflow with a multi-file Python project, and compare its diffs to native git diffs.

## Why This Matters
- Code already has great git diff support
- This experiment tests whether the workflow ADDS value beyond git (e.g., better summaries, context-aware diffs)
- Tests the multi-file diff summary format
- Tests integration testing (does the code still run?)

## Test Plan
1. Create a small Python CLI tool (3-5 files) as the initial artifact
2. Feature branch: add a new command
3. Feature branch: refactor shared utilities
4. Feature branch: fix a bug + add tests
5. Compare prompt-generated diffs to `git diff` output
6. Test the test checklist auto-generation

## Artifact
A Python CLI tool for data transformation (e.g., CSV → JSON converter).

## Success Criteria
- Diff summary adds value beyond raw git diff
- Test checklist is appropriate for the artifact type
- Multi-file changes are easy to follow
- Integration tests actually catch real issues
