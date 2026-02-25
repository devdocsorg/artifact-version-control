# Issue Log — Manual Testing as End User

Tested all 3 experiments with `sample_bundle.json`. Approached each as a reviewer who's never seen this tool before, trying to answer:
1. What changed in this PR?
2. Are the changes correct?
3. Does the document read well after changes?
4. How does it look rendered?
5. Was anything important lost when errors.md was deleted?

---

## Issues Across ALL Experiments

### 🔴 Critical: Truncated content renders as literal text in Preview
The bundle contains `... (2 more) ...`, `... (35 more) ...`, `... (13 more) ...` placeholders where content was truncated. In the markdown preview, these render as literal text — it looks like the document is broken. A reviewer would think the document has garbage in it.

**Example:** Under "Users" section, the preview shows:
```
... (35 more) ... }
**Errors:**
| Status | Code | Description |
```
This renders as a raw code block with pipe tables visible instead of being formatted, because the markdown parser sees the truncation as content.

**Fix needed:** Either the bundle generator needs to include full content, OR the viewer needs to detect and visually mark truncated sections (e.g. "⋯ 35 lines not shown in bundle").

### 🔴 Critical: No explanation of what this tool IS on first load
A new user lands and sees "Load a DiffBundle JSON to review changes." They don't know what a DiffBundle is, how to generate one, or why they should care. The tool assumes knowledge the user doesn't have.

### 🟡 Medium: "New Source" and "Preview" tabs are visible for DELETED files
In Experiments A and B, when viewing errors.md (deleted), the "New Source" and "Preview" tabs are still visible and clickable. Clicking Preview shows "File does not exist in this version" — but the user would expect to see the *old* version's preview. Experiment C handles this better by only showing "Changes" and "Old Source".

### 🟡 Medium: No connection between checking off "Content/Flow/Preview" and viewing modes
In Experiment C, the checkboxes (Content, Flow, Preview) are passive — they don't guide you to the right view. Clicking "Flow" should suggest switching to "New Source" view. Clicking "Preview" should switch to the Preview tab. Right now they're just manual checkboxes with no intelligence.

### 🟡 Medium: Unchanged files waste the reviewer's time
All three experiments include unchanged files (authentication.md, changelog.md). In Experiment B, clicking "Next" from README.md goes to authentication.md which shows "(77 lines, no changes)" — a dead-end screen. The reviewer has to click Next again. Experiment C skips them in the sidebar (good) but Experiment B counts them in "2/5" navigation.

---

## Experiment A — Tabbed File Cards

### First Impression (as new user)
"There's a LOT on this page. I see the header, a sidebar, a description, then a wall of cards. Each card has tabs at the top but they're small and I didn't notice them at first. The endpoints.md diff is enormous and dominates the page."

### Issues

1. **🔴 Tabs are easy to miss.** The tab labels ("📝 Changes", "📄 New Source", "👁 Preview") blend into the card chrome. On first view, I didn't realize they were clickable tabs — they look like passive labels. Need stronger visual differentiation (underline, background, bigger hit target).

2. **🟡 Page is extremely long.** With all files expanded at once (especially endpoints.md's 84-line addition), the page is easily 5000+ px tall. You lose context as you scroll. It's hard to go back and forth between README changes and endpoints changes.

3. **🟡 Preview tabs are per-file, not global.** If I want to check the preview for every file, I have to click the Preview tab on each card separately. There's no "switch all files to Preview mode" toggle.

4. **🟡 Sidebar doesn't indicate current scroll position.** The sidebar highlights the "active" file but doesn't auto-update as I scroll through the page. So after scrolling, the sidebar highlight is stale.

5. **🟡 Unchanged file cards add noise.** authentication.md and changelog.md show "No changes" cards that push the interesting content further down. Why show them at all?

6. **🟡 The diff for endpoints.md is confusing.** The chunked diffs with small context windows make it hard to understand the overall restructuring. You see a "+84 lines" block followed by scattered modifications, but it's hard to piece together *what the new file structure looks like*.

7. **🟢 Nice: All files visible at once.** Good for getting a quick overview of scope. Scrolling through lets you see everything without clicking.

8. **🟢 Nice: Tab state persists per file.** I can have README on Preview and endpoints on Changes simultaneously.

---

## Experiment B — Focused File Review

### First Impression (as new user)
"Clean! The overview is nice — I can see which files changed and click into them. When I click README.md, I get the full-width diff which is easy to read. The mode bar is clear. I understand what this tool does."

### Issues

1. **🔴 Unchanged files in navigation are a dead end.** Clicking "Next" from README.md goes to authentication.md which says "(77 lines, no changes)." All the view modes are still enabled but pointless. I have to click Next again. The counter says "2/5" including these dead files.

2. **🔴 For deleted files, "Preview" and "New Source" are misleading.** On errors.md (REMOVED), clicking Preview shows a trash can icon and "File does not exist in this version." The user naturally wants to see what was deleted — but the UI offers "Preview" (which shows nothing) instead of automatically showing the old rendered version.

3. **🟡 Keyboard shortcuts are hidden.** The keyboard hint is in the bottom-right corner and very subtle. `←` `→` navigation and `1-5` mode switching are powerful but invisible to first-time users. No tooltips on the mode buttons either.

4. **🟡 Mode bar resets when switching files.** If I'm on "Split Preview" for README.md and click Next to endpoints.md, it stays on Split Preview — but the content reloads at scroll position 0. Would be nice if it remembered scroll position per file.

5. **🟡 Overview only shows changed files.** Good — but no PR description visible when inside a file. You'd need to go back to Overview to re-read the description. Could be a hover/tooltip on the branch badge.

6. **🟡 "COMPARE:" section label in mode bar is confusing.** The distinction between "VIEW:" and "COMPARE:" isn't immediately obvious. "Split Source" and "Split Preview" could just be alongside the other modes.

7. **🟢 Nice: Full-width content is much more readable.** The diff for README.md is instantly clear — you can see the whole file at once without scrolling.

8. **🟢 Nice: Split Preview is the killer feature.** Side-by-side rendered before/after for README.md immediately shows the error link was removed and the TOC was updated. This is the single most useful view for manual review.

9. **🟢 Nice: Overview page is a great entry point.** Shows scope, description, and lets you click into specific files.

---

## Experiment C — Review Dashboard

### First Impression (as new user)
"I see a sidebar with files and checkboxes, a progress bar, and a diff. The checkboxes (Content, Flow, Preview) are interesting but I don't immediately understand what they mean or what I'm supposed to do with them. Is 'Content' checking the content? Or marking that I've checked the content?"

### Issues

1. **🔴 Checklist semantics are unclear.** "Content", "Flow", "Preview" — are these aspects I should check? Statuses? Review criteria? There's no tooltip or explanation. A new user would not know that checking "Preview" means "I've reviewed this file's rendered preview." The word "Preview" especially is confusing because there's also a "Preview" view tab.

2. **🔴 Clicking checkboxes doesn't change the view.** If I click "Flow" checkbox on README.md, nothing happens in the main panel — it just turns green. The natural expectation would be: clicking "Flow" checkbox switches to "New Source" view (so I can check the flow), or clicking "Preview" checkbox switches to Preview mode. Right now, the checkboxes are completely disconnected from the view.

3. **🟡 Progress bar is gamification without value.** "13% reviewed (1/8 checks)" — but there's no guarantee that checking a box means I actually reviewed anything. I could check all boxes without looking at anything. The progress bar creates a false sense of thoroughness.

4. **🟡 Sidebar takes up permanent space.** The review sidebar with file list + checkboxes is always visible, taking ~300px. This leaves less room for the actual content, especially in Split/Compare views. Experiment B uses the full width.

5. **🟡 Notes panel is always visible.** The "Review notes for this file" textarea at the bottom takes up vertical space even when empty. It should be collapsible or hidden until needed.

6. **🟡 Deleted file (errors.md) gets "Content" and "Impact" checks but no guidance.** What does "Impact" mean for a deleted file? The user has to guess that they should check whether the deleted content was properly moved elsewhere. No help text.

7. **🟡 File names truncated in sidebar.** "errors..." is truncated. The sidebar is 300px wide but the badges, stats, and checkboxes compete for space, pushing the filename into truncation.

8. **🟢 Nice: Per-file review checklist is a good concept.** For a thorough review process, having structured criteria per file is valuable. Just needs better UX.

9. **🟢 Nice: Different check types for different file statuses.** Modified files get (Content, Flow, Preview) while deleted files get (Content, Impact). Smart adaptation.

10. **🟢 Nice: Notes per file.** Being able to jot down concerns per file is useful for coming back to or sharing.

---

## Top Recommendations (prioritized)

### Must Fix
1. **Handle truncated content gracefully** — detect `... (N more) ...` and render as a styled "content not shown" placeholder
2. **Hide/disable irrelevant view modes** — no "Preview" for deleted files, no modes for unchanged files
3. **Skip unchanged files in navigation** (Experiment B) or don't show them at all (Experiment C approach)

### High Impact
4. **Make Experiment B's Split Preview the default comparison mode** — it's the single clearest way to review document changes
5. **Connect checkboxes to view modes** (Experiment C) — clicking "Preview ✓" should BOTH switch to preview view AND mark it checked
6. **Add a "What is this?" onboarding hint** for new users landing on the tool

### Nice to Have
7. **Global view mode toggle** (Experiment A) — "show all files as Preview" button
8. **Collapsible notes panel** (Experiment C)
9. **Tooltips on all buttons/modes** explaining what they do
10. **Auto-scroll sidebar to current file** as user navigates
