# Diff: endpoints.md (Custom Format per Prompt Spec)

[UNCHANGED: Lines 1-3]

[ADDED: Lines 4-5 (inserted after line 3)]
Additions:
- Pagination note callout linking to pagination.md
Reason: Alert readers that all list endpoints support pagination
---
> **Note:** All list endpoints support pagination. See the [Pagination Guide](pagination.md) for details.

[UNCHANGED: Lines 4-40 → now Lines 6-42]
_(Users section through response data array)_

[MODIFIED: Lines 41-42 → Lines 43-48]
Changes:
- Replaced bare `"total": 42` with full `meta` pagination object
Reason: Response format updated to include pagination metadata
---
BEFORE:
```json
  "total": 42
```
---
AFTER:
```json
  "meta": {
    "total": 42,
    "limit": 10,
    "offset": 0,
    "has_more": true
  }
```

[UNCHANGED: Lines 43-113 → Lines 49-119]
_(Get User, Create User, Projects section through response data array)_

[MODIFIED: Lines 114-115 → Lines 120-126]
Changes:
- Replaced bare `"total": 5` with full `meta` pagination object
Reason: Consistent pagination metadata across all list endpoint responses
---
BEFORE:
```json
  "total": 5
```
---
AFTER:
```json
  "meta": {
    "total": 5,
    "limit": 20,
    "offset": 0,
    "has_more": false
  }
```

[UNCHANGED: Lines 116-end → Lines 127-end]
_(Create Project, Delete Project sections)_
