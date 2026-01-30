# Diff Summary

## Files Changed
| File | Status | Description |
|------|--------|-------------|
| `endpoints.md` | Modified | Reordered sections (Projects before Users), added inline error tables per endpoint, added Common Errors section |
| `errors.md` | Removed | Content moved inline to endpoints.md |
| `README.md` | Modified | Removed errors.md links, updated endpoints description |
| `authentication.md` | Unchanged | — |
| `changelog.md` | Unchanged | — |

## Detailed Changes

### endpoints.md (major restructure)
**Warning:** The unified diff for this file is 242 lines and appears to show almost everything as changed. This is because sections were reordered (Projects moved before Users), which `diff -u` handles poorly — it can't detect moved blocks.

Actual changes:
1. **Section reorder:** Projects section moved from after Users to before Users
2. **Added error tables:** Each endpoint now has an inline "Errors:" table with relevant HTTP status codes
3. **Added Common Errors section:** Bottom section with 429 (rate limit) and 500 (server error)
4. **No content was deleted** from the original endpoints — all existing content is preserved

### errors.md
Deleted entirely. Error codes have been distributed:
- Endpoint-specific errors → inline tables in endpoints.md
- Generic errors (429, 500) → "Common Errors" section in endpoints.md
- Error response format documentation → NOT preserved (potential gap)

### README.md
- Removed "Handle errors gracefully" from Quick Start steps
- Removed errors.md from Table of Contents
- Updated endpoints.md description: "Full API reference" → "Full API reference with inline error codes"
