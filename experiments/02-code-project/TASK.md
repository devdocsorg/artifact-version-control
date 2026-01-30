# Task: Run Experiment 02 — Code Project

## Your Mission

You are testing the "Artifact Branch Workflow" prompt (v1) with a multi-file Python project.

This is the most interesting comparison because code already has great git diff support. Your job is to figure out where this workflow ADDS value beyond native git.

## Steps

### Phase 1: Setup
1. Read `/Users/jacksonmills/clawd/artifact-version-control/SUB_AGENT_CONTEXT.md` for rules
2. Read `/Users/jacksonmills/clawd/artifact-version-control/prompt/v1-original.md` for the prompt
3. Work in `/Users/jacksonmills/clawd/artifact-version-control/experiments/02-code-project/`
4. Start a `LOG.md` — write to it constantly

### Phase 2: Create the Artifact
Create a small Python CLI tool (a CSV-to-JSON converter) with this structure:
```
outputs/main/artifact/
├── csvjson/
│   ├── __init__.py
│   ├── cli.py          # argparse CLI
│   ├── converter.py    # Core conversion logic
│   ├── validators.py   # Input validation
│   └── formatters.py   # Output formatting options
├── tests/
│   ├── test_converter.py
│   └── test_validators.py
├── setup.py
└── README.md
```
Make it actually runnable — this lets you test the integration testing part of the prompt.
Initialize `outputs/main/history.md` with a v1 commit.

### Phase 3: Test Feature Branches
Follow the prompt's workflow EXACTLY for each:

**Branch 1: `add-yaml-output`**
- Add YAML as an output format option
- Update cli.py to accept --format yaml
- Add tests for YAML output
- Update README

**Branch 2: `refactor-validators`**
- Split validators.py into schema_validators.py and type_validators.py
- Update imports across all files
- This is a "swipe across project" change — the kind git diffs handle poorly

**Branch 3: `fix-unicode-bug`**
- Fix a bug with unicode characters in CSV input
- Add a test case
- Small, surgical change — git handles this well

### Phase 4: Compare with Git
For each branch, ALSO create a real git branch and generate `git diff`:
```bash
git diff main..branch-name
```
Then compare the prompt's diff output to git's diff. Which is more useful? When?

### Phase 5: Evaluate
Score each branch on all 5 dimensions.
Pay special attention to dimension 5 (Git Integration).
Write results to `RESULTS.md`.

### Phase 6: Report
- Update `/Users/jacksonmills/clawd/artifact-version-control/LEARNINGS.md`
- Git commit and push
- Be specific: when does this workflow beat git? When does git win?

## Key Questions to Answer
1. Does `diff -u` give you everything, or does the summary.md add value?
2. For the refactor (branch 2), which diff is easier to understand: git or the prompt's?
3. Does the test checklist auto-generation produce useful tests for code?
4. Is the folder-based branching redundant with git branching for code?
5. What would you change about the prompt for code artifacts?

## Remember
- LOG AS YOU GO
- Commit frequently
- Update LEARNINGS.md when you discover something
- Actually run the Python code to test integration
