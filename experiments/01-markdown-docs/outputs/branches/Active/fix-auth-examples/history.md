# Branch History: fix-auth-examples

## Branch Created
- **Date:** 2025-01-31
- **Forked from:** main @ v1.0 (Initial Commit)
- **Purpose:** Fix incorrect code examples in authentication docs and update endpoint auth references

## Commit 1: Fix auth header and examples
- **Date:** 2025-01-31
- **Changes:**
  - authentication.md: Changed API key header from `Authorization: Bearer` to `X-API-Key:` (Bearer is for OAuth only)
  - authentication.md: Added Content-Type headers to curl examples
  - authentication.md: Fixed OAuth scope format to resource-based (`users:read`, `projects:write`)
  - authentication.md: Added redirect_uri to token exchange (was missing, required param)
  - authentication.md: Added client_id to refresh token request (was missing)
  - authentication.md: Added security tip, migration notes, scope change notice, redirect_uri warning
  - authentication.md: Updated key rotation response to include `previous_key_valid_until` field
  - endpoints.md: Updated all 3 curl examples to use `X-API-Key` header instead of `Authorization: Bearer`
