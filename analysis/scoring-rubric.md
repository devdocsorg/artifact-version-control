# Scoring Rubric for Experiment Evaluation

## Dimensions

### 1. Diff Readability (1-5)
Can a human who didn't make the changes understand what changed just from the diff?

| Score | Description |
|-------|-------------|
| 1 | Incomprehensible — might as well open both versions yourself |
| 2 | Partial — you get the gist but miss important details |
| 3 | Adequate — main changes are clear, some context missing |
| 4 | Good — clear changes with context, minor gaps |
| 5 | Excellent — full understanding without opening the artifact |

### 2. Completeness (1-5)
Are ALL changes accounted for? No surprises when you open the actual artifact?

| Score | Description |
|-------|-------------|
| 1 | Major changes missing from diff |
| 2 | Several changes missing or misrepresented |
| 3 | Most changes captured, some omissions |
| 4 | All changes captured, minor formatting gaps |
| 5 | Perfect accounting — diff is the source of truth |

### 3. Workflow Friction (1-5)
How smooth is the process of creating branches, making changes, generating diffs?

| Score | Description |
|-------|-------------|
| 1 | Painful — constant manual intervention needed |
| 2 | Clunky — several workarounds required |
| 3 | Acceptable — works but feels heavy |
| 4 | Smooth — minor friction points |
| 5 | Seamless — the workflow disappears into the background |

### 4. Format Fit (1-5)
Does the prompt adapt well to this specific artifact type?

| Score | Description |
|-------|-------------|
| 1 | Completely wrong approach for this format |
| 2 | Awkward fit — prompt assumptions don't match format |
| 3 | Workable — prompt handles it but not optimally |
| 4 | Good fit — prompt adapts well with minor format gaps |
| 5 | Perfect fit — feels like it was designed for this format |

### 5. Git Integration (1-5)
How well does the folder-based workflow complement actual git?

| Score | Description |
|-------|-------------|
| 1 | Conflicts with git — confusing, redundant |
| 2 | Awkward coexistence — unclear what git vs folders handle |
| 3 | Neutral — doesn't help or hurt git usage |
| 4 | Complementary — folder workflow adds value git lacks |
| 5 | Synergistic — git + folder workflow together > either alone |

## Overall Score
Average of all 5 dimensions, weighted equally.
