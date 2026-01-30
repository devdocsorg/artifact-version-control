# Issue: No Code Movement Detection

## Severity: Medium

## Description
The prompt says "generate diffs programmatically when possible" and suggests `diff -u` 
for code files. But `diff -u` cannot detect code that MOVED between files without changes.

For the refactor-validators branch, `validate_file_path()` moved from `validators.py` to 
`schema_validators.py` with zero logic changes. Git shows this as 30 lines deleted + 30 
lines added — indistinguishable from completely new code.

The Refactoring Map I created in summary.md was the ONLY way to express this, and I had 
to write it manually.

## Evidence
- Branch 2 native diff: 166 lines showing add/delete with no structural context
- summary.md Refactoring Map: immediately clear what moved vs. what's new

## Recommendation
Add explicit guidance for refactoring diffs:
1. Identify moved functions/classes by content hash comparison
2. Use a "MOVED" marker in the diff format alongside UNCHANGED/MODIFIED/ADDED
3. For code specifically, consider integrating with `git diff -M -C` (copy detection)
4. Make the Refactoring Map a first-class template in the prompt
