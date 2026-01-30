# PR: Fix Authentication Examples

## Original Request
Fix incorrect code examples in authentication.md and update endpoint examples that reference auth.

## Summary of Changes
1. **Fixed API key auth header:** Changed from `Authorization: Bearer` to `X-API-Key:` across all docs. Bearer scheme is reserved for OAuth access tokens.
2. **Added missing parameters:** Content-Type headers on POST requests, redirect_uri in token exchange, client_id in refresh token flow.
3. **Updated OAuth scopes:** Old format `read write` → new resource-based format `users:read+projects:write`.
4. **Added developer notes:** Security tips, scope migration notice, redirect_uri matching requirement, key rotation grace period, refresh token expiry.
5. **Fixed response format:** Key rotation response field renamed `new_key` → `api_key`, added `previous_key_valid_until`.

## Files to Review
- `authentication.md` — Heavy changes, review all code blocks carefully
- `endpoints.md` — Simple find/replace of auth header (3 occurrences)

## Questions / Decisions Made
- Decided API keys should use `X-API-Key` header (common pattern) rather than Bearer scheme
- Added 7-day grace period for old keys after rotation — this is a product decision that should be verified
- Resource-based scopes assumed to be v2.1 change — verify with changelog

## Status
- [x] Branch created
- [x] Changes implemented
- [x] Unit testing complete
- [x] Integration testing complete
- [x] Diff generated
- [x] Ready for review
- [ ] Feedback addressed
- [ ] Approved for merge
- [ ] Merged to main
