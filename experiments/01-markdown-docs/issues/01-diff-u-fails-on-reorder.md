# Issue 01: `diff -u` Fails on Section Reordering

## Severity: High
## Affected: Branch 3 (restructure-docs)

## Description
When sections of a markdown file are reordered (e.g., moving "Projects" section before "Users"), `diff -u` produces a diff where nearly every line appears as removed and re-added. The 139-line file produced a 242-line diff that was essentially useless for understanding the change.

## Expected Behavior
The diff should communicate: "The Projects section was moved from lines 70-140 to lines 5-75. The Users section was moved from lines 5-69 to lines 76-140."

## Actual Behavior
242 lines of `-` and `+` markers showing the entire file as changed, making it impossible to identify what actually changed vs. what merely moved.

## Root Cause
`diff -u` operates on lines and has no concept of "moved blocks." This is a fundamental limitation of line-based diffing.

## Proposed Fix
1. Add a `[MOVED]` marker to the prompt's custom diff format
2. Recommend using the custom format (not `diff -u`) when changes are structural
3. Consider tools like `git diff --color-moved` or specialized markdown diff tools
4. Make summary.md the authoritative diff document for structural changes
