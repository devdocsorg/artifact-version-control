#!/bin/bash
# === Actual commands the writer runs during Phase 3: Drafting ===

# 1. Create feature branch from main
git checkout main
git pull origin main
git checkout -b feature/DOC-201

# 2. Create the doc file
mkdir -p docs/guides/webhooks
# (writer edits docs/guides/webhooks/setup.md in their editor)

# 3. Stage and commit
git add docs/guides/webhooks/setup.md
git commit -m "docs: add webhook setup developer guide

Adds comprehensive developer guide covering:
- Webhook creation (API + UI)
- Event types reference table
- Payload format with examples
- HMAC-SHA256 signature verification (Python, Node.js)
- Retry behavior and delivery logs
- Troubleshooting common issues
- Limits and quotas

Closes DOC-201"

# 4. Push branch to GitHub
git push -u origin feature/DOC-201
# Output:
# remote: Create a pull request for 'feature/DOC-201' on GitHub by visiting:
# remote:   https://github.com/company/docs/pull/new/feature/DOC-201

# 5. Create PR via GitHub CLI
gh pr create \
  --title "docs: Webhook Setup Developer Guide" \
  --body "## Summary

Adds a new developer guide for webhook setup and management.

**JIRA:** [DOC-201](https://company.atlassian.net/browse/DOC-201)
**Epic:** [EPIC-100](https://company.atlassian.net/browse/EPIC-100) (Webhook Management)
**Doc Type:** Developer Guide

## What's Included
- Overview and prerequisites
- Creating webhooks (API + UI)
- Event types reference (15 types)
- Payload format with examples
- Signature verification (Python, Node.js, Go)
- Retry behavior
- Delivery log usage
- Troubleshooting section
- Limits and quotas

## Review Notes
- Signature header is \`X-Webhook-Signature-256\` (corrected from TRD which says \`X-Signature\`)
- Discovered 25-webhook-per-account limit not in PRD — confirmed with PM
- Payload truncation at 256KB found in code, not documented anywhere before this

## Checklist
- [x] Code samples tested against staging
- [x] Event type list matches openapi.yaml
- [x] Signature verification tested with real payloads
- [x] Retry timing confirmed with engineering
- [ ] Awaiting: engineering review
- [ ] Awaiting: PM review
" \
  --reviewer sarah-chen,marcus-webb \
  --label documentation,developer-guide \
  --assignee alex-rivera

# PR #42 created
# Output:
# https://github.com/company/docs/pull/42
