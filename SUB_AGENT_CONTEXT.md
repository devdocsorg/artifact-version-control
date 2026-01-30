# Sub-Agent Context — READ THIS FIRST

> **You are a sub-agent working on the Artifact Version Control experiment.**
> **Your job: test a prompt that creates a git-like branching/diff workflow for ANY artifact type.**

## Critical Rules

1. **LOG EVERYTHING AS YOU GO.** Do not wait until the end. Your memory is not stable.
2. **Write to files.** Notes, observations, issues — all go in files in your experiment folder.
3. **Update LEARNINGS.md** at the repo root when you discover something important.
4. **Commit frequently.** Small, meaningful commits with clear messages.
5. **Use real git.** Create actual git branches for feature work. Push them. Make PRs if appropriate.

## What You're Testing

We have a prompt (in `/prompt/`) that defines a branching workflow for artifacts. The prompt creates:
- A `main/` folder with the current working version
- `branches/Active/`, `branches/Merged/`, `branches/Canceled/` for feature work
- Each branch has: `Forked_From/`, `artifact/`, `history.md`, `PR.md`, `diff/`
- Diffs must be human-readable regardless of format

## Your Experiment Process

1. **Read the prompt version** you've been assigned (default: latest in `/prompt/`)
2. **Create a sample artifact** appropriate to your experiment type
3. **Follow the prompt's workflow** to make changes via feature branches
4. **Generate diffs** and evaluate: Are they useful? Human-readable? Complete?
5. **Log observations** in your experiment folder's `LOG.md`
6. **Try to break it.** Edge cases, merge conflicts, multi-file changes, etc.
7. **Score the results** on:
   - Diff readability (1-5): Can a human understand what changed?
   - Completeness (1-5): Are all changes accounted for?
   - Workflow friction (1-5): How smooth is the process? (5 = seamless)
   - Format fit (1-5): Does the prompt adapt well to this artifact type?

## What We Already Know (from PowerPoint experiments)

- The workflow WORKS well for PowerPoint with custom tooling (pptx_tools.py, generate_diff.py)
- Diff presentation is inconsistent — sometimes tags on slides, sometimes in-between slides, sometimes yellow for no reason
- Branch naming and PR descriptions are solid
- The commit history tracking sometimes drifts (AI forgets to update)
- Merge conflict detection needs work
- The "test checklist" creation on first branch is useful but undertested

## Repo Structure

```
artifact-version-control/
├── LEARNINGS.md              ← UPDATE THIS when you learn something
├── SUB_AGENT_CONTEXT.md      ← YOU ARE READING THIS
├── prompt/
│   ├── v1-original.md        ← The full prompt
│   └── CHANGELOG.md
├── experiments/
│   ├── 01-markdown-docs/
│   ├── 02-code-project/
│   ├── 03-html-site/
│   ├── 04-spreadsheet-csv/
│   └── 05-mixed-artifacts/
├── analysis/
│   └── (comparative analysis goes here)
└── tools/
    └── (shared tooling)
```

## Git Workflow for Experiments

Each experiment should use ACTUAL git branches:
- `experiment/01-markdown-docs` — branch for that experiment
- Within the experiment, the ARTIFACT also uses the prompt's branching structure
- So you'll have git branches + the prompt's folder-based branches — that's fine, they're different layers

## How to Report Results

In your experiment folder, create:
- `LOG.md` — Running log of everything you do
- `RESULTS.md` — Final scores and observations
- `issues/` — Individual files for each problem discovered
- `samples/` — Example diffs you generated (good and bad)
