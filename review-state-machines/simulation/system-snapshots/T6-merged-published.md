# T6: Merged and Published

**Transition:** Writer merges PR, publishes to Confluence, closes JIRA ticket  
**Trigger:** Writer clicks "Merge" on GitHub (or `gh pr merge`)  
**Phase:** 5 (Publishing) → complete for DOC-201

## System State — FINAL

### JIRA ← CHANGED
```
DOC-201:
  status:      Done ✅
  resolution:  Complete
  assignee:    Alex Rivera
  
  Timeline:
    To Do:       Feb 1  (2 days)
    In Progress: Feb 3  (7 days — research + draft)
    In Review:   Feb 10 (2 days — 2 eng rounds + PM review)
    Done:        Feb 12
    Total:       11 days

Remaining docs in EPIC-100:
  DOC-202: In Progress  (UI Reference — different writer)
  DOC-203: To Do        (User Workflow — not yet assigned)
```

### Confluence ← CHANGED
```
PRD (page 123456):   unchanged (source of truth for requirements)
TRD (page 789012):   unchanged (source of truth for technical design)
Published doc (345678): EXISTS NOW ← NEW
  Space:  DOCS
  Title:  "Webhook Setup Guide"
  Parent: "Developer Guides"
  Status: Current
  Version: 1
```

### GitHub ← CHANGED
```
PR #42:
  state:    merged (closed)
  merged_by: alex-rivera
  merged_at: 2026-02-12T10:00:00Z
  merge_commit: d4e5f6a7...

branch feature/DOC-201:  DELETED

main branch:
  └── docs/guides/webhooks/setup.md   ← NOW IN MAIN
      (identical to the reviewed, approved version)
```

### CI/CD ← CHANGED
```
Build #795:
  trigger:   merge to main
  status:    passed
  output:    production docs site updated
  URL:       https://docs.company.com/guides/webhooks/setup/
             ← LIVE, accessible to customers
```

### Local Filesystem (Writer's machine)
```
~/work/docs/                          ← back on main branch
├── docs/guides/webhooks/
│   └── setup.md                      ← same as GitHub main
└── ...

~/work/notes/
└── DOC-201-research.md               ← still here, still untracked
    (writer may delete or keep for reference)
```

## Complete Data Flow Summary

```
                    Phase 1                Phase 2              Phase 3                Phase 4                 Phase 5
                    ─────────              ─────────            ─────────              ─────────               ─────────
PM's brain ──────→  Confluence PRD
                    │
Docs PM's brain ──→ JIRA ticket
                    │ (DOC-201)
                    │                      │
                    ▼                      ▼
                                     Confluence PRD ──read──→ Writer's brain
                                     GitHub code    ──read──→ Writer's brain
                                     Staging env    ──test──→ Writer's brain
                                     Dev's brain    ──talk──→ Writer's brain
                                           │                      │
                                           │                      ▼
                                           │               Writer's notes (local, untracked)
                                           │                      │
                                           │                      ▼
                                           │               Markdown file (local)
                                           │                      │
                                           │                      ▼ git commit
                                           │               Git blob (local)
                                           │                      │
                                           │                      ▼ git push
                                           │               GitHub branch + PR
                                           │                      │
                                           │                      ▼ CI webhook
                                           │               Preview HTML site
                                           │                      │
                                           │                      ▼ reviewer reads
                                           │               Review comments (GitHub)
                                           │                      │
                                           │                      ▼ writer reads comments
                                           │               Writer's brain (feedback loop)
                                           │                      │
                                           │                      ▼ edits + push
                                           │               Updated branch
                                           │                      │
                                           │                      ▼ re-review
                                           │               Approval (GitHub review objects)
                                           │                      │
                                           │                      ▼ merge
                                           │               Main branch (GitHub)
                                           │                      │
                                           │                      ├──→ Production HTML site (CI/CD)
                                           │                      │
                                           └──────────────────────├──→ Confluence published page
                                                                  │
                                                                  └──→ JIRA ticket → Done
```

## Docs PM Coverage Check (Phase 5 Loop)
```
JIRA query: epic=EPIC-100 AND labels=docs AND status!=Done

Results:
  DOC-202 (UI Reference)      → In Progress   → continue cycle
  DOC-203 (User Workflow)     → To Do         → assign + continue cycle

Decision: MORE_TICKETS → loop back to Phase 2 for remaining tickets
```

## Where Content Actually Lives When "Done"

| Location | Format | Purpose | Who Reads It |
|----------|--------|---------|-------------|
| GitHub `main` branch | Markdown source | Source of truth for content | Writers, reviewers, CI |
| Docs site (CI-built) | HTML | Customer-facing documentation | External developers |
| Confluence | XHTML wiki markup | Internal reference, searchable | Internal teams, PM |
| JIRA | Ticket metadata | Tracking, reporting, audit trail | Docs PM, leadership |
