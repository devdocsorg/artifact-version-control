# T2: PR Created

**Transition:** Writer finishes draft, creates branch, pushes, opens PR  
**Trigger:** `git push` + `gh pr create` (or GitHub UI)  
**Phase:** 3 (Drafting) → end / Phase 4 (Reviewing) → start

## System State

### JIRA
```
DOC-201:
  status:    In Review         ← CHANGED from In Progress
  assignee:  Alex Rivera
```

### Confluence
```
PRD (page 123456):  unchanged
TRD (page 789012):  unchanged
Published doc:      does not exist yet
```

### GitHub  ← PRIMARY CHANGE
```
Repo: company/docs
  main branch:          no webhook docs
  feature/DOC-201:      EXISTS (new)
    └── docs/guides/webhooks/setup.md   ← THE DRAFT (245 lines, markdown)
  
  PR #42:               EXISTS (new)
    state:              open
    author:             alex-rivera
    reviewers:          [sarah-chen, marcus-webb]
    labels:             [documentation, developer-guide]
    checks:             pending (CI building preview)
    reviews:            0
    body:               references DOC-201
```

### Local Filesystem (Writer's machine)
```
~/work/docs/                          ← on branch feature/DOC-201
├── docs/guides/webhooks/
│   └── setup.md                      ← committed, pushed
└── ...

~/work/notes/
└── DOC-201-research.md               ← still local only
```

### CI/CD (triggered by push)
```
Build #789:
  trigger:   push to feature/DOC-201
  status:    running → passed
  output:    preview deployed to https://docs-preview.company.com/pr-42/
```

## What Data Moved
1. Writer created branch locally: `git checkout -b feature/DOC-201`
2. Writer created `docs/guides/webhooks/setup.md` in editor
3. Writer committed: markdown file → git object (blob → tree → commit)
4. Writer pushed: local git objects → GitHub remote
5. Writer created PR: GitHub API creates PR object linking branch to main
6. Writer updated JIRA: status → "In Review" (manual or via automation)
7. GitHub sent notifications to reviewers (sarah-chen, marcus-webb)
8. CI/CD triggered by webhook → built preview site

## Format Transitions
```
Writer's knowledge → Markdown file (local)
                     → Git blob (compressed, SHA-addressed)
                     → GitHub branch (remote ref)
                     → PR object (metadata: title, body, reviewers, labels)
                     → CI build → HTML preview site
                     → JIRA status update (API call)
```

## Key Observation
This is the first moment where the draft content is visible to others.
Before `git push`, the work existed only on the writer's machine.
After PR creation, the content is:
- Readable by reviewers (GitHub PR view)
- Previewable as rendered docs (CI preview)
- Diffable against main (GitHub diff view, diff bundle)
- Trackable in JIRA (status = In Review)
