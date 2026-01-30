# Experiment 02 — Code Project LOG

## 2025-02-01 — Session 2: Rebuild

Previous session had severe git branch-switching issues — commits landed on wrong branches,
workflow artifacts (diffs, PR.md, history.md) were created then lost. The code and merges 
happened but metadata is gone. This is itself an important finding:

**META-OBSERVATION: The folder-based workflow creates massive file duplication. When combined 
with git branch operations, it's extremely fragile. A single wrong `git checkout` can wipe 
out dozens of files. The prompt's directory structure fights git rather than complementing it.**

Rebuilding experiment cleanly from committed v1.0.0 baseline.

---

## 2025-01-31 — Session Start (original)

### Setup
- Read SUB_AGENT_CONTEXT.md, v1-original.md, TASK.md, scoring-rubric.md
- Created git branch: `experiment/02-code-project`
- Working directory: `/Users/jacksonmills/clawd/artifact-version-control/experiments/02-code-project/`

### Plan
1. Create the Python CSV-to-JSON converter project in `outputs/main/artifact/`
2. Initialize history.md, test_checklist.md
3. Run 3 feature branches through the Artifact Branch Workflow
4. Also create real git branches for comparison
5. Score and report

### Key hypothesis
Git already handles code diffs extremely well. This workflow should add value primarily through:
- High-level summary.md (narrative context git lacks)
- PR.md with human context
- Test checklist enforcement
- But folder-based branching will feel redundant

Starting Phase 2: Create the artifact...
