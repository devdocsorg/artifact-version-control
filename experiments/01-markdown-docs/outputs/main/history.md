# Main Branch History

## v1.3 — Merged: restructure-docs
- **Date:** 2025-01-31
- **Branch:** restructure-docs
- **Conflict resolution:** 
  - endpoints.md: TRUE CONFLICT — branch restructured entire file (reordered sections, added inline errors) while main had pagination meta + auth header changes. Manual merge required: took branch's structure, applied main's pagination note/meta objects/X-API-Key headers.
  - README.md: CONFLICT — both modified TOC area. Main added pagination link, branch removed errors.md links. Merged both changes.
  - errors.md: branch deleted, main unchanged → deleted.
  - authentication.md: main changed (auth fixes), branch unchanged → kept main's version.
  - pagination.md: new in main, not in fork/branch → kept.
- **Changes:**
  - Reordered endpoints.md: Projects now before Users
  - Added inline error tables per endpoint in endpoints.md
  - Added "Common Errors" section in endpoints.md
  - Deleted errors.md (content distributed to endpoints.md)
  - Updated README.md: removed errors.md references

## v1.2 — Merged: fix-auth-examples
- **Date:** 2025-01-31
- **Branch:** fix-auth-examples
- **Conflict resolution:** endpoints.md changed in both main (pagination meta) and branch (auth headers). Changes were on different lines — merged cleanly by applying branch's sed fix to main's version.
- **Changes:**
  - Modified authentication.md: Fixed API key header format, OAuth scopes, added Content-Type headers, security notes
  - Modified endpoints.md: Updated auth header in 3 curl examples (X-API-Key instead of Bearer)

## v1.1 — Merged: add-pagination-docs
- **Date:** 2025-01-31
- **Branch:** add-pagination-docs
- **Changes:**
  - Created pagination.md with full pagination guide (parameters, response metadata, examples, best practices)
  - Modified endpoints.md: added pagination note at top, updated response examples to include `meta` object
  - Modified README.md: added pagination.md link to table of contents

## v1.0 — Initial Commit
- **Date:** 2025-01-31
- **Author:** Experiment 01 Setup
- **Changes:**
  - Created README.md with API overview and table of contents
  - Created authentication.md with API key and OAuth 2.0 docs
  - Created endpoints.md with Users and Projects API reference
  - Created errors.md with error codes and troubleshooting
  - Created changelog.md with version history
