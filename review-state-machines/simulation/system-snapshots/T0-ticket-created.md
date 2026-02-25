# T0: Ticket Created

**Transition:** Docs PM creates DOC-201, assigns writer  
**Trigger:** Docs PM evaluates EPIC-100 documentation needs, creates doc tickets  
**Phase:** 1 (Organizing) → end

## System State

### JIRA
```
DOC-201:
  status:    To Do
  assignee:  Alex Rivera
  linked to: EPIC-100
  labels:    [docs, developer-guide, release-4.3]
  doc_type:  developer-guide
```

### Confluence
```
PRD (page 123456):  exists, status=Approved  ← created earlier by PM
TRD (page 789012):  exists, status=Approved  ← created earlier by engineering
Published doc:      does not exist yet
```

### GitHub
```
Repo: company/docs
  main branch: no webhook docs
  No feature branch for DOC-201
  No PR
```

### Local Filesystem (Writer's machine)
```
Nothing yet — writer hasn't started
```

## What Triggered This State
1. PM created PRD in Confluence
2. PM reviewed with leadership → approved
3. PM broke into JIRA epics (EPIC-100)
4. Docs PM reviewed epics → identified 3 doc needs
5. Docs PM created DOC-201, DOC-202, DOC-203 in JIRA
6. Docs PM assigned DOC-201 to Alex Rivera
7. JIRA sent assignment notification to Alex

## Next Trigger
Writer opens JIRA notification → clicks DOC-201 → reads description → starts research
