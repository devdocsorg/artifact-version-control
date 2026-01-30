# Issue 03: No Cross-File Move Tracking

## Severity: Medium
## Affected: Branch 3 (restructure-docs)

## Description
When error codes were moved from `errors.md` into inline tables in `endpoints.md`, the diff showed:
- errors.md: DELETED (full file)
- endpoints.md: massive diff with many additions

There was no way to communicate: "This content moved from file A to file B."

## Impact
A reviewer looking at the diff would think:
1. A whole file was deleted (data loss?)
2. A bunch of new content was added to endpoints.md

They wouldn't know these are the SAME content unless they read the summary.md prose description.

## Proposed Fix
Add a `[MOVED_FROM]` / `[MOVED_TO]` marker pair:
```
In errors.md.diff:
[MOVED_TO: endpoints.md, inline error tables per endpoint]
Original content: 60 lines of error code documentation

In endpoints.md.diff:
[MOVED_FROM: errors.md, lines 1-60]
Content redistributed as inline error tables per endpoint
```
