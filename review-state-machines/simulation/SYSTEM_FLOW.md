# System Flow: How Data Actually Moves

This traces the **concrete artifacts** through the documentation system — what file
exists, in what format, in which system, and what event causes the next system to
learn about it.

## Systems and Their Data Formats

| System | What It Stores | Format | How It's Updated |
|--------|---------------|--------|-----------------|
| **JIRA** | Tickets, epics, status, assignee, links | JSON via REST API | API calls, UI actions |
| **Confluence** | PRDs, TRDs, published docs | XHTML storage format (wiki markup) | API calls, editor saves |
| **GitHub** | Source files, branches, PRs, reviews | Files (markdown/RST/MDX), Git objects | `git push`, PR API, review API |
| **Local filesystem** | Writer's working copy | Markdown/RST/MDX files | Editor saves, `git pull/checkout` |
| **CI/CD** | Build artifacts, preview deploys | HTML (built docs site) | Triggered by GitHub webhooks |

---

## The Full Data Journey

```
                    CONFLUENCE                    JIRA                     GITHUB                    LOCAL FS
                    ──────────                    ────                     ──────                    ────────
Phase 1             PRD-1234.xhtml               EPIC-100 (status:Open)
(Organizing)        created by PM                 │
                         │                        ├─ FEAT-101 (dev ticket)
                         │                        ├─ FEAT-102 (dev ticket)
                         │                        │
                         │                        ├─ DOC-201 (doc ticket)    
                         │                        │  status: To Do           
                         │                        │  assignee: writer-1      
                         │                        │  linked to: EPIC-100     
                         │                        │  labels: [developer-guide]
                         │                        │                          
Phase 2             PRD-1234.xhtml ──read──────→ (writer reads)            repo/docs/ ──clone──→ ~/work/docs/
(Researching)       TRD-5678.xhtml ──read──────→ (writer reads)            repo/src/  ──read───→ (writer reads code)
                                                  DOC-201                                         writer's notes
                                                  status: In Progress                             (scratch.md, 
                                                                                                   not committed)
                                                                                                        │
Phase 3                                           DOC-201                  feature/DOC-201 branch       │
(Drafting)                                        status: In Review        │                             │
                                                                           ├─ docs/guides/              ▼
                                                                           │  new-feature.md ◄──── writer creates
                                                                           │  (committed)          this file locally
                                                                           │                       then pushes
                                                                           │
                                                                           └─ PR #42 created
                                                                              base: main
                                                                              head: feature/DOC-201
                                                                              body: "Closes DOC-201"
                                                                              status: open
                                                                              reviewers: [dev-1, pm-1]
                                                                              │
Phase 4                                           DOC-201                  PR #42                  
(Reviewing)                                       status: In Review        │
                                                                           ├─ Review 1 (dev-1)
                                                                           │  state: changes_requested
                                                                           │  comments: [...]
                                                                           │                       writer edits
                                                                           ├─ commit abc123 ◄───── locally, pushes
                                                                           │  (addressing feedback)  force-push
                                                                           │
                                                                           ├─ Review 2 (dev-1)
                                                                           │  state: approved ✓
                                                                           │
                                                                           ├─ Review 3 (pm-1)
                                                                           │  state: approved ✓
                                                                           │
                                                                           └─ status: approved
                                                                              checks: passing
                                                                              │
Phase 5             published-doc.xhtml           DOC-201                  PR #42
(Publishing)        created/updated               status: Done             │ merged → main
                    in docs space                 resolution: Complete     │ branch deleted
                                                                           │
                                                                           main branch now contains
                                                                           docs/guides/new-feature.md
                                                                              │
                                                                           CI/CD builds → preview site
```

---

## Phase-by-Phase: What Actually Happens to the Bits

### Phase 1 → Phase 2 Handoff
**Trigger:** Docs PM sets DOC-201 `assignee` and `status: To Do` via JIRA API  
**What the writer receives:** JIRA notification email + Slack bot message  
**What the writer needs to find:**
- Confluence page URL (linked in JIRA ticket `description` field)
- GitHub repo URL (in JIRA ticket `custom_field_repo` or team wiki)
- Feature branch name if dev work is in progress

### Phase 2 → Phase 3 Handoff
**Trigger:** Writer decides they have enough information to start drafting  
**What changes:**
- Writer runs `git checkout -b feature/DOC-201` locally
- Writer creates `docs/guides/new-feature.md` in their editor
- JIRA status stays "In Progress" (writer updated it when starting research)

### Phase 3 → Phase 4 Handoff
**Trigger:** Writer runs `git push origin feature/DOC-201` and creates PR via GitHub UI/CLI  
**What changes:**
- GitHub: new branch + new PR object created
- PR body contains `Closes DOC-201` (JIRA integration picks this up)
- Writer sets JIRA status to "In Review" via JIRA UI or automation
- GitHub: reviewers auto-assigned via CODEOWNERS or manual selection

### Phase 4 → Phase 5 Handoff
**Trigger:** Both reviews show "approved" state on the PR  
**What changes:**
- Writer clicks "Merge" on GitHub (or uses merge API)
- GitHub: PR status → merged, branch deleted
- CI/CD: webhook fires, docs site rebuilds
- Writer publishes to Confluence (manual or automated)
- Writer sets JIRA status to "Done"

### Phase 5 → Phase 2 Loop (if more tickets)
**Trigger:** Docs PM queries JIRA for remaining open DOC-* tickets in the epic  
**What changes:**
- If `JIRA_query` returns more open tickets → next writer assignment
- If all DOC-* tickets are Done → Docs PM validates release coverage

---

## See Also

- [phase1-organizing/](./phase1-organizing/) — sample JIRA + Confluence artifacts
- [phase2-researching/](./phase2-researching/) — sample writer research notes
- [phase3-drafting/](./phase3-drafting/) — sample draft content + git objects
- [phase4-reviewing/](./phase4-reviewing/) — sample PR, review comments, diff bundle
- [phase5-publishing/](./phase5-publishing/) — sample published artifacts
- [system-snapshots/](./system-snapshots/) — full system state at each transition
