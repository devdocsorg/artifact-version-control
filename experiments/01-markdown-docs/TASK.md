# Task: Run Experiment 01 — Markdown Documents

## Your Mission

You are testing the "Artifact Branch Workflow" prompt (v1) with markdown documents as the artifact type.

## Steps

### Phase 1: Setup
1. Read `/Users/jacksonmills/clawd/artifact-version-control/SUB_AGENT_CONTEXT.md` for rules
2. Read `/Users/jacksonmills/clawd/artifact-version-control/prompt/v1-original.md` for the prompt
3. Work in `/Users/jacksonmills/clawd/artifact-version-control/experiments/01-markdown-docs/`
4. Start a `LOG.md` — write to it constantly

### Phase 2: Create the Artifact
Create a sample API documentation project with 3-5 markdown files:
```
outputs/main/artifact/
├── README.md          # API overview
├── authentication.md  # Auth docs  
├── endpoints.md       # API endpoints reference
├── errors.md          # Error codes
└── changelog.md       # Version history
```
Initialize `outputs/main/history.md` with a v1 commit.

### Phase 3: Test Feature Branches
Follow the prompt's workflow EXACTLY for each of these changes:

**Branch 1: `add-pagination-docs`**
- Add a new section to endpoints.md about pagination
- Add a new file: `pagination.md` with detailed pagination guide
- Update README.md to link to the new file

**Branch 2: `fix-auth-examples`**  
- Modify authentication.md to fix incorrect code examples
- Update the endpoint examples that reference auth

**Branch 3: `restructure-docs`**
- Reorder sections in endpoints.md
- Move error codes from errors.md inline into endpoints.md
- Delete errors.md
- Update README.md links

### Phase 4: Test Merge + Conflict
- Merge branch 1 first
- Then try to merge branch 2 (may have conflicts with the pagination content)
- Then try branch 3 (WILL have conflicts since structure changed)

### Phase 5: Evaluate
For each branch, score the diff on all 5 dimensions from the scoring rubric.
Write results to `RESULTS.md` in your experiment folder.

### Phase 6: Report
- Update `/Users/jacksonmills/clawd/artifact-version-control/LEARNINGS.md` with findings
- Git commit and push all work
- Be specific about what the prompt got right and wrong

## Key Questions to Answer
1. Did you use `diff -u` or write custom diffs? Which was better?
2. Was the diff/summary.md useful for markdown, or overkill?
3. Did the test checklist auto-generation make sense for docs?
4. How did merge conflict detection work?
5. What would you change about the prompt for text-based artifacts?

## Remember
- LOG AS YOU GO
- Commit frequently  
- Update LEARNINGS.md when you discover something
