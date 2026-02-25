#!/bin/bash
# === Phase 5: Publishing — actual commands run by writer ===

# 1. Merge PR via GitHub CLI
gh pr merge 42 --squash --delete-branch
# Output:
# ✓ Squashed and merged pull request #42 (docs: Webhook Setup Developer Guide)
# ✓ Deleted branch feature/DOC-201

# --- What happens automatically after merge: ---
# GitHub webhook fires → CI/CD pipeline triggered
# Pipeline: checkout main → build docs (mkdocs/docusaurus/sphinx) → deploy to preview
# Build output: https://docs-preview.company.com/guides/webhooks/setup/

# 2. Publish to Confluence (if docs also live there)
# This might be a script, a CI step, or manual copy
# Using Confluence REST API to create/update a page:

curl -X PUT \
  "https://company.atlassian.net/wiki/rest/api/content/345678" \
  -H "Authorization: Bearer $CONFLUENCE_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "version": { "number": 2 },
    "title": "Webhook Setup Guide",
    "type": "page",
    "space": { "key": "DOCS" },
    "ancestors": [{ "id": "345000" }],
    "body": {
      "storage": {
        "value": "<h1>Webhook Setup Guide</h1><p>Learn how to create and manage webhooks...</p>...",
        "representation": "storage"
      }
    }
  }'

# 3. Close JIRA ticket
curl -X POST \
  "https://company.atlassian.net/rest/api/3/issue/DOC-201/transitions" \
  -H "Authorization: Bearer $JIRA_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{ "transition": { "id": "31", "name": "Done" } }'

# 4. Docs PM checks remaining tickets
curl -s \
  "https://company.atlassian.net/rest/api/3/search?jql=epic=EPIC-100+AND+type=Task+AND+labels=docs+AND+status!=Done" \
  -H "Authorization: Bearer $JIRA_TOKEN" | jq '.issues[] | {key, summary: .fields.summary, status: .fields.status.name}'

# Output:
# { "key": "DOC-202", "summary": "UI Reference: Webhook Management Panel", "status": "In Progress" }
# { "key": "DOC-203", "summary": "User Workflow: Setting Up Event Notifications", "status": "To Do" }
#
# → MORE_TICKETS — loop back to Phase 2 for DOC-202 and DOC-203
