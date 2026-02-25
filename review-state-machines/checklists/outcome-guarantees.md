# Checklist Sub-Machine: Outcome Guarantees

**Parent:** [PM Review](../pm/pm-review.md)  
**Reviewer:** PM (Product Manager)  
**Global outcome on FAIL:** `PM_decision → ISSUES_FOUND → BACK_TO_DRAFTING2`  
**Global outcome on PASS:** Advances to next check (`UI Reference Accuracy?`)

---

## The Question

> Does the documentation promise clear, achievable outcomes that the product can
> actually deliver? Are user expectations set correctly?

## Sub-State Machine

```
[START: Outcome Guarantees?]
    │
    ▼
┌──────────────────────────────┐
│ Check Outcome Statements     │  Does each workflow end with a clear
│ (STATED | VAGUE)             │  "you will have achieved X"?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Achievability          │  Can the product actually deliver what
│ (ACHIEVABLE | OVERPROMISED)  │  the doc promises?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Scope Accuracy         │  Is the doc clear about what the feature
│ (ACCURATE | INFLATED)        │  does AND doesn't do?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Success Verification   │  Can the user verify they achieved the
│ (VERIFIABLE | TRUST_ME)      │  promised outcome?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Expectation Alignment  │  Does the doc match the product's actual
│ with Product Vision          │  positioning and messaging?
│ (ALIGNED | DRIFTED)          │
└────────┬─────────────────────┘
         │
         ▼
[AGGREGATE] ──→ PASS or FAIL
```

## What the Reviewer Looks For

### 1. Outcome Statements
- Does each workflow clearly state what the user will have achieved?
- Not just "how to configure X" but "after this, you will have a working X that does Y"
- Are outcomes concrete and measurable? ("Your API will respond in <200ms" vs. "Your API will be fast")
- **Diff viewer:** **Source (read-through)** — check workflow endings and introduction promises.

### 2. Achievability
- Can the product actually deliver what the doc promises?
- Is the doc promising features that are roadmapped but not shipped?
- Are there known limitations that contradict the doc's claims?
- Cross-reference with current product capability: does it match?
- **Source:** Current product state, known bugs, release notes.

### 3. Scope Accuracy
- Does the doc accurately represent what the feature does and doesn't do?
- Are limitations stated upfront? ("This feature supports up to 100 concurrent users")
- Is the doc careful not to imply capabilities that don't exist?
- "Generate reports" — does it actually generate, or does it export data for you to analyze?
- **Diff viewer:** **Source (read-through)** — look for claims and compare to actual capability.

### 4. Success Verification
- Can the user confirm they achieved the outcome?
- Is there a "verify your setup" step? ("Run this command to confirm everything works")
- Are expected results shown? (screenshot of success state, expected output)
- What does "done" look like? Can the user distinguish success from failure?
- **Diff viewer:** **Preview (rendered)** — check for verification steps, success screenshots.

### 5. Expectation Alignment with Vision
- Does the documentation match how the PM wants the product positioned?
- Does the language match marketing and sales messaging?
- Is the feature described in terms of user value, not technical capability?
- Does the doc inadvertently set expectations for features that aren't planned?
- **Source:** Product positioning docs, sales materials, PM vision.

## Pass / Fail Criteria

| Verdict | Condition |
|---------|-----------|
| **PASS** | Each workflow promises a clear, achievable outcome, the product can deliver on every promise, limitations are stated, success is verifiable, and the doc aligns with product positioning |
| **FAIL** | Outcomes are vague or overpromised, the product can't deliver what's described, limitations are hidden, success is unverifiable, or the doc contradicts product positioning |

## Failure Feedback Template

```
❌ Outcome Guarantees: FAIL

[file.md, "Real-time Analytics"] — Overpromise:
  Doc says "real-time analytics dashboard" but data actually
  updates every 15 minutes. Need to say "near-real-time"
  and state the refresh interval.

[file.md, "Auto-Scaling"] — Feature not shipped:
  Doc describes auto-scaling behavior that's on the roadmap
  for Q3 but not yet implemented. Can't document it as if
  it works today.

[file.md, "Export Report"] — No verification:
  Workflow ends at "Click Export" but doesn't describe what
  a successful export looks like. Where does the file go?
  How do you know it completed? What if it's empty?
```
