# Issue 03: Interactive/Behavioral Changes Cannot Be Diffed

## Severity: Medium

## Description
The hamburger menu has behavior: click → toggle → animation. CSS transitions, hover states, and JavaScript interactions are invisible in any static diff format. A screenshot shows one state; you'd need a video or animated GIF to show the transition.

## Affected Changes
- CSS transitions and animations
- JavaScript-driven UI state changes
- Hover/focus/active states
- Responsive layout changes across breakpoints

## Proposed Fix
For interactive changes, the diff should include:
1. Multiple screenshots showing key states (before click, during animation, after click)
2. A text description of the interaction flow
3. Optionally: a screen recording or animated GIF

The PR.md already supports "What to Review" descriptions — this should be formalized for interactive artifacts.
