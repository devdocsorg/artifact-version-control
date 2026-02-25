# System Snapshots

Each file captures the **complete state of all four systems** at a transition boundary.
Read these in order to see exactly how data propagates.

| Snapshot | Transition | What Changed |
|----------|-----------|-------------|
| [T0](./T0-ticket-created.md) | Docs PM creates DOC-201 | JIRA: ticket exists |
| [T1](./T1-research-started.md) | Writer starts research | JIRA: status change. Local: clone + notes |
| [T2](./T2-pr-created.md) | Writer pushes branch + creates PR | GitHub: branch + PR. JIRA: status change |
| [T3](./T3-eng-review-requested-changes.md) | Dev requests changes | GitHub: review w/ comments |
| [T4](./T4-eng-review-approved.md) | Dev approves (round 2) | GitHub: approved review |
| [T5](./T5-pm-approved.md) | PM approves | GitHub: second approval |
| [T6](./T6-merged-published.md) | Writer merges + publishes | GitHub: merged. Confluence: published. JIRA: done |
