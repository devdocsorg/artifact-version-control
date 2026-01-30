# Experiment 01 Results — Markdown Documents

## Per-Branch Scores

### Branch 1: add-pagination-docs
| Dimension | Score | Notes |
|-----------|-------|-------|
| Diff Readability | **5** | `diff -u` was perfect. New file, modified lines, added lines — all crystal clear. |
| Completeness | **5** | All 6 files accounted for in summary.md. Every change captured. |
| Workflow Friction | **3** | Copying all files to Forked_From/ and artifact/ took time. PR.md + history.md setup is boilerplate. For text files, this is all unnecessary — git does it natively. |
| Format Fit | **4** | Prompt adapted well to markdown. `diff -u` recommended for text files. Custom format was unnecessary overhead but summary.md added real value. |
| Git Integration | **2** | Folder-based branches redundant with git branches for text. Two parallel branching systems created confusion. Files on disk fought with git working tree constantly. |

**Branch 1 Average: 3.8 / 5**

---

### Branch 2: fix-auth-examples
| Dimension | Score | Notes |
|-----------|-------|-------|
| Diff Readability | **5** | 89-line auth diff + 29-line endpoints diff, both perfectly readable. Code blocks provide natural visual structure in diffs. |
| Completeness | **5** | All files accounted for. Detailed changes section in summary.md was helpful for the longer auth diff. |
| Workflow Friction | **3** | Same overhead as branch 1. The sed replacement for endpoints.md was efficient, but generating the diff still required the full copy workflow. |
| Format Fit | **4** | Good. Markdown with code blocks diffs beautifully — code fences are natural boundary markers. |
| Git Integration | **2** | Same git vs. folders tension. Merge conflict detection (compare history snapshots) worked but is a worse version of `git merge-base`. |

**Branch 2 Average: 3.8 / 5**

---

### Branch 3: restructure-docs
| Dimension | Score | Notes |
|-----------|-------|-------|
| Diff Readability | **2** | `diff -u` produced a 242-line mess for endpoints.md because sections were reordered. You cannot understand the change from the diff alone. summary.md was the only salvation. |
| Completeness | **4** | All changes captured technically, but the endpoints diff is misleading — it shows everything as changed when really sections were moved. The summary.md caught the deleted file correctly. |
| Workflow Friction | **3** | Same copy overhead. Merge was significantly harder — manual three-way merge of endpoints.md required understanding both change sets and composing a new file. |
| Format Fit | **3** | This is where the prompt's custom format would have been BETTER — you could annotate `[MOVED: section]` which `diff -u` can't do. But the prompt doesn't specify how to handle moves. |
| Git Integration | **2** | The Forked_From/ snapshot proved essential for merge conflict resolution — it's the common ancestor. But git provides `merge-base` for free. |

**Branch 3 Average: 2.8 / 5**

---

### Merge Conflict Resolution
| Dimension | Score | Notes |
|-----------|-------|-------|
| Diff Readability | N/A | Merge conflicts don't produce a diff — they require manual resolution |
| Completeness | **4** | The prompt's conflict detection process (history comparison → per-file analysis) caught all conflicts correctly. One file (errors.md deleted vs unchanged) was correctly identified as safe. |
| Workflow Friction | **2** | The three-way merge of endpoints.md was entirely manual. No tools, no automation. The prompt describes the PROCESS but doesn't help with the WORK. For a 190-line restructured file, this was painful. |
| Format Fit | **3** | The per-file conflict rules (unchanged in branch → take main, etc.) worked well for simple cases. For the true conflict (endpoints.md), the rules correctly flagged it but couldn't help resolve it. |
| Git Integration | **3** | Forked_From/ proved its worth here — it's the merge base. But `git merge` would have done this automatically for text files, including auto-resolving the non-overlapping changes. |

**Merge Average: 3.0 / 5**

---

## Overall Scores

| Dimension | Average | Notes |
|-----------|---------|-------|
| **Diff Readability** | **4.0** | Excellent for line-level changes, poor for structural changes |
| **Completeness** | **4.7** | summary.md ensures nothing is missed |
| **Workflow Friction** | **2.75** | Heavy overhead for text files. Copy-everything model doesn't fit. |
| **Format Fit** | **3.5** | Good for simple changes, needs "move" support for restructuring |
| **Git Integration** | **2.25** | Actively conflicts with git for text files |

### **Overall: 3.4 / 5**

---

## Key Findings

### What Works Well
1. **summary.md is the star.** Regardless of artifact type, a file-level overview of changes is invaluable. Even when individual diffs are unreadable (branch 3), the summary tells you what happened.
2. **PR.md is solid.** The structured template (original request, changes, status checklist) creates useful documentation. The status checklist is good progress tracking.
3. **Forked_From/ enables three-way merge.** For conflict resolution, the common ancestor is essential. This proved its value even for text files.
4. **History tracking works.** The commit log format is clear and the merge history preserved decision rationale.
5. **`diff -u` is the right tool for markdown line changes.** The prompt correctly recommends it.

### What Fails
1. **`diff -u` fails for structural changes.** Section reordering, content moves between files — these produce useless diffs. The prompt offers no alternative.
2. **The folder-based workflow is redundant with git for text.** Two branching systems = twice the confusion, twice the overhead.
3. **No move/rename detection.** When content moves between files (errors.md → endpoints.md), there's no way to show this in the diff.
4. **Manual merge is too hard.** The prompt describes conflict detection but provides no resolution tools.
5. **Custom diff format is worse than `diff -u`** for simple changes but **better for structural changes** — the prompt should recommend using BOTH based on change type.

### Recommendations for v2
1. **For text artifacts: skip Forked_From/ copies.** Use git diff or store only a hash/commit reference.
2. **Add a MOVE marker to the diff format:** `[MOVED: from errors.md lines 1-60 to endpoints.md lines 150-210]`
3. **Make summary.md the primary diff document** for complex changes, with individual diffs as supplementary.
4. **For text, recommend git branching over folder branching.** The folder system adds value for binary artifacts, not text.
5. **Add tooling recommendations.** For markdown: `diff -u`, `diff --color-words` (word-level), `wdiff`. For structural changes: human-written narrative.
