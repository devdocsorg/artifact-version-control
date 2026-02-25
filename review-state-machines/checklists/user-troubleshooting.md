# Checklist Sub-Machine: User Troubleshooting

**Parent:** [PM Review](../pm/pm-review.md)  
**Reviewer:** PM (Product Manager)  
**Global outcome on FAIL:** `PM_decision → ISSUES_FOUND → BACK_TO_DRAFTING2`  
**Global outcome on PASS:** Advances to next check (`Outcome Guarantees?`)

---

## The Question

> Can users self-serve when something goes wrong? Will the documentation reduce
> support tickets, or will users be forced to contact support for basic issues?

## Sub-State Machine

```
[START: User Troubleshooting?]
    │
    ▼
┌──────────────────────────────┐
│ Check Known Issue Coverage   │  Are the top support-ticket issues
│ (COVERED | GAPS)             │  addressed in the doc?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check User-Friendly Language │  Can a non-technical user understand
│ (ACCESSIBLE | TOO_TECHNICAL) │  the troubleshooting steps?
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Self-Serve Resolution  │  Can users fix it themselves, or does
│ Rate                         │  every issue require contacting support?
│ (SELF_SERVE | SUPPORT_WALL)  │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check FAQ / Common Questions │  Are frequently asked questions answered?
│ (PRESENT | MISSING)          │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Check Support Channel        │  When self-serve fails, is there a clear
│ Guidance                     │  path to human help?
│ (CLEAR | MISSING)            │
└────────┬─────────────────────┘
         │
         ▼
[AGGREGATE] ──→ PASS or FAIL
```

## How This Differs from Engineering's "Troubleshooting Correct"

The engineering reviewer checks whether troubleshooting steps are **technically accurate**.
The PM checks whether they're **user-appropriate** and **strategically complete**:

| Engineering (Technical) | PM (Product) |
|------------------------|-------------|
| "Does this fix work?" | "Will a user understand this fix?" |
| "Is the error message right?" | "Are we covering the errors users actually hit?" |
| "Is the diagnostic correct?" | "Will this reduce our support ticket volume?" |

## What the Reviewer Looks For

### 1. Known Issue Coverage
- Do the documented troubleshooting topics match the top 10 support tickets?
- Has the PM cross-referenced with the support team's known issues list?
- Are recently-discovered issues from beta/early access included?
- **Source:** Support ticket data, customer feedback, internal bug tracker.

### 2. User-Friendly Language
- Are error messages explained in plain language, not just technical terms?
- "Error 502" needs to be translated: "The service is temporarily unavailable. This usually resolves in a few minutes."
- Are steps written for the target user's skill level?
- **Diff viewer:** **Preview (rendered)** — read as an end user, not an engineer.

### 3. Self-Serve Resolution Rate
- What percentage of documented issues can the user resolve without contacting support?
- Are there issues where the resolution is just "contact support"? Can any of those be made self-serve?
- Are workarounds documented for known bugs pending fixes?
- **Diff viewer:** **Source (read-through)** — for each issue, check whether the resolution is actionable by the user.

### 4. FAQ / Common Questions
- Are frequently asked questions answered proactively?
- Do FAQs address conceptual confusion, not just errors? ("What's the difference between X and Y?")
- Are FAQs based on actual user questions, not just what engineering thinks users ask?

### 5. Support Channel Guidance
- When self-serve fails, where does the user go?
- Are support channels clearly listed? (email, chat, community forum, GitHub issues)
- Is there guidance on what info to include in a support request?
- Are SLA expectations set? ("We respond within 24 hours")

## Pass / Fail Criteria

| Verdict | Condition |
|---------|-----------|
| **PASS** | Known issues are covered, language is appropriate for the target user, most issues are self-serve resolvable, FAQs exist, and support escalation is clearly documented |
| **FAIL** | Top user issues aren't covered, language is too technical for the audience, too many issues require support contact, no FAQ, or no support escalation path |

## Failure Feedback Template

```
❌ User Troubleshooting: FAIL

[file.md] — Top issue not covered:
  The #1 support ticket is "I can't reset my password via SSO."
  This isn't mentioned anywhere in the troubleshooting section.

[file.md, "Error Handling"] — Too technical:
  Error explanations reference HTTP status codes and JSON payloads.
  Our end users aren't developers — need plain-language translations.

[file.md] — Support wall:
  5 of 8 troubleshooting entries end with "Contact support."
  At least 3 of these could have user-actionable workarounds.
```
