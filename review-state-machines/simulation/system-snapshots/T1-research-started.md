# T1: Research Started

**Transition:** Writer begins researching the feature  
**Trigger:** Writer reads JIRA ticket, transitions status to "In Progress"  
**Phase:** 2 (Researching) → start

## System State

### JIRA
```
DOC-201:
  status:    In Progress       ← CHANGED from To Do
  assignee:  Alex Rivera
```

### Confluence
```
PRD (page 123456):  being read by writer (no changes)
TRD (page 789012):  being read by writer (no changes)
```

### GitHub
```
Repo: company/docs
  main branch:          no webhook docs
  feature/FEAT-101:     exists (dev's feature branch — writer reads code here)
  feature/DOC-201:      does not exist yet
```

### Local Filesystem (Writer's machine)
```
~/work/docs/                          ← git clone of company/docs
├── docs/guides/                      ← existing docs (no webhook content)
└── ...

~/work/notes/
└── DOC-201-research.md               ← writer's scratch notes (NOT committed)
    - PRD summary
    - TRD summary  
    - API endpoint list from openapi.yaml
    - Questions for engineering
    - Test results from staging
```

## What Data Moved
1. Writer read JIRA ticket → extracted Confluence URLs, repo URL
2. Writer opened Confluence pages → read PRD and TRD (Confluence read, no write)
3. Writer cloned/pulled docs repo → read code in feature/FEAT-101
4. Writer tested feature on staging → captured test results in local notes
5. Writer talked to Sarah Chen → captured answers in local notes

## Key Observation
At this point, the writer's research notes exist ONLY on their local machine.
No system knows what the writer has learned. The knowledge lives in:
- Writer's brain
- `~/work/notes/DOC-201-research.md` (untracked, uncommitted)

This is the most fragile point in the cycle — if the writer disappears, all
research is lost. The JIRA ticket would need to be reassigned and research restarted.
