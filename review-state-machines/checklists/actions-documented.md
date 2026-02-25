# Checklist Sub-Machine: Actions Documented

**Parent:** [Engineering Review: UI Reference](../engineering/ui-reference-review.md)  
**Reviewer:** Developer  
**Global outcome on FAIL:** `Dev_decision → ISSUES_FOUND → BACK_TO_DRAFTING`  
**Global outcome on PASS:** All UI Reference checks complete → `Dev_decision`

---

## The Question

> For every interactive element in the UI (buttons, links, menus, toggles, form submissions),
> does the documentation describe what happens when the user interacts with it?

## Sub-State Machine

```
[START: Actions Documented?]
    │
    ▼
┌──────────────────────────────┐
│ Inventory Interactive        │  List every clickable, submittable, toggleable
│ Elements                     │  element on the documented screens
│ (buttons, links, menus,      │
│  toggles, forms, shortcuts)  │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Action Descriptions    │  Is the effect of each action described?
│ (DESCRIBED | UNDOCUMENTED)   │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Confirmation Behaviors │  Do destructive actions have confirmation
│ (DOCUMENTED | MISSING)       │  dialogs? Are they mentioned?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Side Effects           │  Does clicking X also affect Y?
│ (NOTED | HIDDEN)             │  Are cascading effects documented?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Reversibility          │  Can the user undo this action? Is that stated?
│ (STATED | AMBIGUOUS)         │
└────────┬─────────────────────┘
         │
         ▼
[AGGREGATE] ──→ PASS or FAIL
```

## What the Reviewer Looks For

### 1. Inventory Interactive Elements
- List every button, link, form submit, dropdown, toggle, drag-drop target, keyboard shortcut
- Include both primary actions (big CTA buttons) and secondary ones (context menus, gear icons)
- Note bulk actions, multi-select operations, and right-click menus
- **Diff viewer:** **Preview (rendered)** — scan for mentions of clickable elements.

### 2. Action Descriptions
- For each action: what happens when the user does it?
- "Click **Delete**" → what actually happens? Is the item soft-deleted or permanently removed?
- "Toggle **Enable notifications**" → enable for whom? What kind of notifications?
- Does the doc describe the UI response? (spinner, success toast, page redirect)
- **Diff viewer:** **Source (read-through)** — check that each mentioned action has a result.

### 3. Confirmation Behaviors
- Do destructive actions show a confirmation dialog? Is the dialog documented?
- What does the confirmation dialog say? What are the options?
- Are irreversible actions clearly labeled as such?
- **Diff viewer:** **Changes (diff)** — new features should document their confirmation flows.

### 4. Side Effects
- Does performing action A also affect state B? ("Deleting a project also deletes all its API keys")
- Are webhook triggers, email notifications, or audit log entries mentioned?
- Does the action affect other users? ("Revoking access removes the user immediately")
- **Diff viewer:** **Source (read-through)** — look for implicit cascading effects.

### 5. Reversibility
- Can the user undo the action? (Ctrl+Z, recycle bin, restore, revert)
- If irreversible, is that clearly stated?
- Is there a grace period? ("Deleted items are recoverable for 30 days")
- **Diff viewer:** **Source (read-through)** — check for undo/revert guidance.

## Pass / Fail Criteria

| Verdict | Condition |
|---------|-----------|
| **PASS** | Every interactive element has its effect described, destructive actions note their consequences and confirmation flows, side effects are documented, and reversibility is stated |
| **FAIL** | Buttons/actions exist in the UI without their behavior being documented, destructive actions lack warnings, or side effects are hidden |

## Failure Feedback Template

```
❌ Actions Documented: FAIL

[file.md, "Team Members" section] — Missing action description:
  "Remove" button next to each team member is shown in the
  screenshot but the doc never explains what happens when clicked.
  Does it revoke access immediately? Is there a confirmation?

[file.md, "Settings"] — Hidden side effect:
  "Disable SSO" toggle doesn't mention that it immediately
  logs out all SSO users. This is a critical side effect.

[file.md, "Archive Project"] — Missing reversibility info:
  Is archiving reversible? Can you unarchive? The doc doesn't say.
```
