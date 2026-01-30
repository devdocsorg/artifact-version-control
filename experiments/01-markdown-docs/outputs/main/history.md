# Main Branch History

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
