# Diff Summary

## Files Changed
| File | Status | Description |
|------|--------|-------------|
| `authentication.md` | Modified | Fixed API key header format, added Content-Type headers, updated OAuth scope format, added security notes |
| `endpoints.md` | Modified | Updated auth header in 3 curl examples from `Authorization: Bearer` to `X-API-Key:` |
| `README.md` | Unchanged | — |
| `changelog.md` | Unchanged | — |
| `errors.md` | Unchanged | — |

## Detailed Changes

### authentication.md (major changes)
- **API Key header:** `Authorization: Bearer` → `X-API-Key:` (Bearer is for OAuth only)
- **Added notes:** Security tip, scope format change notice, redirect_uri requirement
- **Fixed missing params:** Content-Type headers on POST requests, redirect_uri in token exchange, client_id in refresh
- **Updated response:** Key rotation now returns `api_key` (not `new_key`) + `previous_key_valid_until` field
- **Added context:** Old key grace period explanation, refresh token expiry behavior

### endpoints.md (minor changes)
- 3 curl examples updated: `Authorization: Bearer YOUR_API_KEY` → `X-API-Key: YOUR_API_KEY`
