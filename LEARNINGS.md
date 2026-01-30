# Learnings — Artifact Version Control Experiments

> **Rule: Log as you go. Never wait until the end. If you don't write it down, you WILL forget.**

## Key Insights (update this section first, always)

_Nothing yet — experiments starting._

---

## Experiment Log

### Experiment 01: Markdown Docs
- **Status:** Not started
- **Format:** Markdown files (single + multi-file)
- **Question:** Does the prompt produce clean, useful diffs for text-based artifacts?

### Experiment 02: Code Project
- **Status:** Not started
- **Format:** Multi-file code project (Python or JS)
- **Question:** Can the workflow match or exceed what git diff already provides? Where does it add value?

### Experiment 03: HTML Site
- **Status:** Not started
- **Format:** Static HTML/CSS site
- **Question:** How well do visual diffs work for rendered content?

### Experiment 04: Spreadsheet/CSV
- **Status:** Not started
- **Format:** CSV data files
- **Question:** Can formula/cell changes be represented in human-readable diffs?

### Experiment 05: Mixed Artifacts
- **Status:** Not started
- **Format:** A project with multiple artifact types
- **Question:** Does the workflow hold up when artifact/ contains heterogeneous file types?

---

## Prompt Version History

| Version | Date | Key Changes | Experiment Results |
|---------|------|-------------|-------------------|
| v1 | 2026-01-30 | Original from Slack thread | _pending_ |

---

## Pain Points Discovered

_None yet._

## What Works Well

_Nothing confirmed yet._

## Format-Specific Notes

### PowerPoint (.pptx)
- Already tested extensively in `powerpoint-editor` repo
- Binary format requires special diff handling (screenshot-based, slide extraction)
- pptx_tools.py + generate_diff.py are mature

### Markdown (.md)
_pending_

### Code (.py, .js, .jsx)
_pending_

### HTML/CSS
_pending_

### CSV/Spreadsheet
_pending_
