# AI-Guided Review Plan — Design Document

## The Core Problem

Today: Reviewer opens a diff viewer and has to figure out what to look for themselves.
Tomorrow: AI analyzes the changes, generates a **guided review tour**, and maps each check to the exact view that answers it.

The key insight: **Different changes require different types of scrutiny**, and the viewer already has the right views — we just need an AI to connect "what to check" to "how to check it."

---

## What This Looks Like

### Before (current)
1. Reviewer opens PR
2. Scrolls through diffs
3. Hopes they catch everything
4. ??? 
5. Approves or requests changes

### After (AI-guided)
1. Reviewer opens PR → sees **personalized review plan**
2. Each check item: specific question + linked to the exact view that answers it
3. "Tour mode": checks presented in optimal order, reviewer steps through them
4. Each check: Pass / Fail / Discuss
5. Review summary auto-generated with structured feedback

---

## Architecture

### Data Flow

```
Project Context (.reviewrc)   PR Metadata (description, branch)
         ↓                              ↓
    ┌─────────────────────────────────────┐
    │       AI Review Plan Generator       │
    │  (analyzes changes + project rules)  │
    └──────────────┬──────────────────────┘
                   ↓
           Review Plan JSON
           (embedded in bundle or separate file)
                   ↓
    ┌─────────────────────────────────────┐
    │         Artifact Diff Viewer         │
    │   (presents guided review + views)   │
    └──────────────┬──────────────────────┘
                   ↓
        Reviewer selects role (optional)
                   ↓
        Filtered, ordered checklist
        Each item → specific file + view
                   ↓
        Review complete → export feedback
```

### Review Plan Schema

```json
{
  "review_plan": {
    "summary": "One-paragraph AI summary of what this PR does",
    "risk_level": "low|medium|high",
    "estimated_review_time": "5 min",
    
    "roles": [
      { "id": "content", "name": "Content Reviewer", "icon": "📝", "desc": "Checks accuracy, flow, completeness" },
      { "id": "technical", "name": "Technical Reviewer", "icon": "⚙️", "desc": "Checks API accuracy, specs" },
      { "id": "docs-infra", "name": "Docs Infrastructure", "icon": "🔧", "desc": "Checks rendering, links, build" }
    ],
    
    "checks": [
      {
        "id": "check-1",
        "question": "Were all error codes from errors.md moved into their correct endpoint sections?",
        "why": "The PR deletes errors.md and claims to inline error codes — we need to verify nothing was lost",
        "category": "content-accuracy",
        "severity": "critical",
        "roles": ["content", "technical"],
        "file": "endpoints.md",
        "view": "compare",
        "also_check": [{ "file": "errors.md", "view": "old-preview" }],
        "look_for": "Compare the error tables in the new endpoints.md against the full errors.md that was deleted. Every error code should appear."
      }
    ],
    
    "categories": [
      { "id": "content-accuracy", "name": "Content Accuracy", "icon": "✅" },
      { "id": "structure", "name": "Document Structure", "icon": "🏗️" },
      { "id": "appearance", "name": "Visual Appearance", "icon": "👁" },
      { "id": "consistency", "name": "Consistency", "icon": "🔗" }
    ]
  }
}
```

### Project Config (.reviewrc.json)

Projects can define persistent rules that get incorporated into every review plan:

```json
{
  "always_check": [
    "All markdown files render without broken links",
    "Table of Contents matches actual file list",
    "Every API endpoint has an Errors section"
  ],
  "roles": [
    { "id": "tech-writer", "name": "Technical Writer", "focus": ["grammar", "flow", "formatting"] },
    { "id": "api-owner", "name": "API Owner", "focus": ["accuracy", "completeness", "breaking-changes"] }
  ],
  "severity_rules": {
    "deleted_files": "always flag as critical",
    "new_files": "check for consistency with existing docs",
    "modified_toc": "verify all links still work"
  }
}
```

---

## Workflows to Support

### Workflow 1: Solo Reviewer (default)
- Open bundle → see all checks
- Work through them in suggested order
- Mark each pass/fail
- Export summary

### Workflow 2: Role-Based Review
- Open bundle → select "I'm the Content Reviewer"
- See only checks relevant to content
- Other checks grayed out: "Assigned to: Technical Reviewer"

### Workflow 3: Team Review
- Multiple reviewers each open the same bundle
- Each selects their role
- Each sees their portion of the review
- Review states could be synced (future: shared state)

### Workflow 4: Re-Review After Changes
- Author makes changes based on feedback
- New bundle generated with updated review plan
- Previously-passed checks that weren't affected: auto-marked
- Changed areas: re-flagged for review
- New check: "Verify requested changes were addressed"

---

## Problems to Solve

### 1. How does the AI know what to check?
**Input signals:**
- PR description (intent)
- File-level changes (scope)
- Change types (added/modified/removed)
- Content analysis (what kind of content changed — headers? code? tables?)
- Project config (persistent rules)
- Reviewer role (focus area)

**The AI should ask:**
- What could go wrong with these specific changes?
- What assumptions does the author make that should be verified?
- What human judgment is needed that a linter can't provide?

### 2. What if the AI plan is wrong?
- Reviewer can dismiss/skip checks
- Reviewer can add custom checks
- "This check is not relevant" feedback improves future plans
- Plan is a suggestion, not a gate

### 3. Mapping checks to views
The AI needs to understand what each view is good for:
- **Changes (diff)** → "Was the syntax of the change correct?"
- **Read Through (source)** → "Does the document flow well?"
- **How It Looks (preview)** → "Does the rendered output look right?"
- **Before/After (compare)** → "How did the overall document change?"
- **Custom views** → AI can suggest new views not yet built

### 4. What about non-markdown artifacts?
- CSV data: "Do the new rows follow the same format?" → table diff view
- PowerPoint: "Are the new slides consistent with the deck's style?" → slide comparison
- Code: "Does the new function handle edge cases?" → code diff with annotations
- The schema is format-agnostic; views are format-specific

### 5. Review plan generation timing
**Option A: At bundle creation time** (recommended for v1)
- AI generates plan when the diff bundle is created
- Plan is embedded in the bundle JSON
- No AI needed at review time
- Pro: Works offline, fast
- Con: Can't personalize per reviewer at load time

**Option B: At review time**
- Viewer sends bundle to AI API for plan generation
- Pro: Always fresh, can personalize
- Con: Requires API, costs money, adds latency

**Option C: Hybrid** (recommended for v2)
- Base plan in bundle (pre-generated)
- Viewer can call AI to refine based on reviewer role
- Best of both worlds

---

## New Views the AI Might Request

The review plan might identify needs that current views don't serve:

1. **Cross-file comparison** — "Compare the errors table in endpoints.md to the old errors.md"
   - Need: side-by-side view of two DIFFERENT files
   
2. **Outline diff** — "Compare the heading structure before/after"
   - Need: TOC/outline extraction + comparison

3. **Annotation overlay** — "Look at line 45 of endpoints.md"
   - Need: preview with highlighted regions

4. **Content coverage map** — "All error codes from errors.md accounted for?"
   - Need: checklist showing which items from file A appear in file B

These could be built as new view modes triggered by the review plan.

---

## Implementation Plan

### Phase 1: Static Review Plan in Viewer (NOW)
- Define review_plan schema
- Create sample plans for existing bundles
- Build guided review UI in viewer
- Role selector, categorized checks, linked views

### Phase 2: AI Plan Generator
- Build script that takes bundle + project config → review plan
- Use LLM to analyze changes and generate checks
- Template system for common patterns

### Phase 3: Reviewer Personalization
- Role selection persists per reviewer
- Custom checks can be added
- Review state can be exported/imported

### Phase 4: New View Types
- Cross-file comparison
- Annotation overlays
- Content coverage maps
- Outline diff
