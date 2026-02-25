# Research Notes: DOC-201 — Webhook Setup Developer Guide

**Writer:** Alex Rivera  
**Date started:** 2026-02-03  
**JIRA:** DOC-201 (status changed to In Progress)

---

## Sources Reviewed

### Confluence
- [x] PRD (page 123456) — read 2/3, clear scope
- [x] TRD (page 789012) — read 2/3, has API spec details
- [ ] Need to confirm: does HMAC use SHA256 or SHA512? TRD says 256, API spec says 512

### GitHub Code
- [x] `api/webhooks/openapi.yaml` — full API spec, 6 endpoints
- [x] `src/webhooks/delivery.go` — retry logic lives here
- [x] `src/webhooks/signature.go` — HMAC implementation (confirmed: SHA256)
- [x] `tests/webhooks/` — test cases show edge case behaviors

### Feature Testing (staging environment)
- [x] Created webhook via API — works, returns 201
- [x] Created webhook via UI — works, but "Event Types" dropdown is slow to load (>3s)
- [x] Triggered test event — received payload at my ngrok endpoint
- [x] Verified signature — my Python verification code works
- [x] Tested retry — killed my endpoint, saw 3 retries in delivery log
- [ ] BUG: Retry timing shows 1, 5, 25 min (not 1, 5, 30 as PRD says). Asked dev.

### Developer Conversations
- **Sarah Chen (2/4):** Confirmed retry intervals are 1, 5, 30 min. The 25-min I saw 
  was a timing measurement error on my end — the retry fires at 30 min but my log 
  timestamp was from when it was queued, not delivered.
- **Sarah Chen (2/4):** Signature header name is `X-Webhook-Signature-256` (not 
  `X-Signature` as TRD says — TRD is outdated on this).
- **Need follow-up:** What happens when max retries exhausted? Does the webhook get 
  disabled? Sarah said she'd check.

## Key Findings Affecting the Doc

1. **Signature header name discrepancy** — TRD says `X-Signature`, code says 
   `X-Webhook-Signature-256`. Using the code as source of truth.
2. **Event type list** — 15 types at launch. Got full list from openapi.yaml.
3. **Rate limit on webhook creation** — 25 webhooks per account. Not in PRD.
   Confirmed with PM this is intentional. Must document.
4. **Payload size limit** — 256KB max payload. Larger events are truncated.
   Not in PRD or TRD. Found in code comments.

## Outline Plan

1. Overview (what webhooks are, when to use them)
2. Prerequisites (API key, endpoint URL, HTTPS required)
3. Creating a Webhook (API + UI paths)
4. Event Types (table of all 15 with descriptions)
5. Payload Format (JSON structure, common fields, event-specific fields)
6. Signature Verification (HMAC-SHA256, code samples in Python/Node/Go)
7. Retry Behavior (timing, max retries, what happens after exhaustion)
8. Delivery Logs (how to check, what fields mean)
9. Troubleshooting (common errors, diagnostic steps)
10. Limits & Quotas (25 webhooks, 256KB payload, rate limits)

## Status

Research ~90% complete. Waiting on:
- [ ] Sarah's answer on what happens after max retries exhausted
- [ ] Final confirmation from PM on the 25 webhook limit messaging

Ready to start drafting sections 1-6 while waiting.
