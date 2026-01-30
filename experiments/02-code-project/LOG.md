# Experiment 02 — Code Project LOG

## 2025-01-31 — Session Start

### Setup
- Read SUB_AGENT_CONTEXT.md, v1-original.md, TASK.md, scoring-rubric.md
- Created git branch: `experiment/02-code-project`
- Working directory: `experiments/02-code-project/`

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

---

## Phase 2: Create Artifact — DONE
- Created csvjson Python project with: cli.py, converter.py, validators.py, formatters.py
- Created test suite: test_converter.py (12 tests), test_validators.py (8 tests) — 20 total
- All 20 tests passing
- Set up virtual env at /tmp/csvjson-venv
- Created history.md (v1.0.0) and test_checklist.md
- Initial git commit on experiment/02-code-project branch

### Observation: Test Checklist Generation
The prompt says to auto-generate a test checklist on first branch. I created one proactively.
This is already something code projects typically handle via CI/CD — the checklist feels 
like it duplicates what a CI pipeline + PR template would do. But for an AI agent 
without CI, it's a useful self-discipline tool.

---

## Phase 3: Feature Branches — Starting

### Branch 1: add-yaml-output
Starting now...
