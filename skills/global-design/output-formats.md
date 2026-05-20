# Output Formats

> Match the output format to the audience. Same design decision, different framing.

---

## For the client / product owner

Focus on outcomes, not implementation. No jargon.

```markdown
## What's wrong
[Plain language description of the problem and its business impact]

## What to change
[List of changes, ordered by impact]

## Why
[Business rationale — conversion, trust, clarity, retention]

## What to expect
[Concrete outcome: "users will understand X in the first 5 seconds" / "form completion rate should improve"]
```

---

## For the developer (frontend ТЗ)

Unambiguous. Every value is exact. Every state is described. No interpretation required.

Full template → `templates/specs/frontend-tz.md`

```markdown
## Task: [Component or page name]

**Problem:** [What exists now and why it's wrong]

**What to implement:** [Exact description]

### Desktop behavior
[Exact layout, dimensions, states, interactions]

### Mobile behavior (≤ 768px)
[How it changes — not "make it responsive", exact behavior]

### States
- **Idle:** [exact appearance]
- **Hover:** [exact appearance — desktop only]
- **Loading:** [skeleton? spinner? duration threshold?]
- **Empty:** [what to show, what copy]
- **Error:** [copy formula, recovery action]
- **Success:** [what to show, duration]

### Tokens
- Background: `var(--color-surface)`
- Text: `var(--color-text)`
- Border: `1px solid var(--color-border)`
- Spacing: `var(--space-6)` padding

### Animation
- Duration: 200ms
- Easing: `cubic-bezier(0.16, 1, 0.3, 1)`
- Trigger: on mount / on hover / on scroll entry

### ARIA
- Role: `[role]`
- Label: `aria-label="[exact string]"`
- State: `aria-expanded`, `aria-selected`, etc.

### Acceptance criteria
- [ ] [Specific, testable criterion]
- [ ] Keyboard navigable (Tab + Enter)
- [ ] Touch target ≥ 44×44px
- [ ] Works at 200% zoom
- [ ] `prefers-reduced-motion` collapses animation

### Do not
- [Explicit prohibition 1]
- [Explicit prohibition 2]
```

---

## For vibe coding

Structured as a self-contained prompt. Paste directly into Claude Code / Cursor.

```markdown
## Goal
[One sentence: what the finished result does]

## Context
[Tech stack, existing constraints, related components]

## Create these files
[List of files to create, with purpose]

## Components
[List of React components with props interface]

## Styles
[Token values to use — no raw colors/sizes]
[Tailwind classes if applicable]

## Logic
[State, effects, data fetching — what the code must do]

## Verification
[How to know it's working correctly]
[Edge cases to test]

## Do not
- Use hardcoded hex colors — use CSS custom properties
- Add features not listed above
- Use framer-motion — use motion/react
- Use 100vh — use 100dvh
```

---

## For the designer (design brief)

Full template → `templates/briefs/project-brief.md`

```markdown
## Project
[Name, type, URL if existing]

## User
- Primary persona: [role + context]
- Primary device: [mobile / desktop / both]
- Technical literacy: [low / medium / high]

## Business goal
[Primary conversion or outcome this design must serve]

## Screen/page structure
[List of required screens in user flow order]

## Grid
[12-column / bento / sidebar / fluid — with max-width]

## Typography
[Display font + body font + mono — from approved list only]

## Color strategy
[Restrained / Committed / Full palette / Drenched]
[Primary accent hue + rationale]

## Design archetype
[From SKILL.md Section 3 — named, with rationale]

## Key components
[List components that must be designed]

## States required per component
[Idle, hover, loading, empty, error, success]

## Responsive breakpoints
[390px / 768px / 1280px behaviors]

## Accessibility requirements
[WCAG level — minimum AA]

## What to avoid
[Specific patterns, colors, copy styles to exclude]
```

---

## For an audit report

Full template → `templates/outputs/ux-audit-report.md`

```markdown
## Executive summary
[2-3 sentences: overall assessment + top priority]

## Critical issues (fix before launch)
| Issue | Location | Impact | Fix |
|---|---|---|---|

## Medium issues (fix in next sprint)
| Issue | Location | Impact | Fix |
|---|---|---|---|

## Improvements (nice to have)
[List with rationale]

## Priorities
[Ordered by: business impact × implementation effort]

## Estimates
[Time to fix each critical issue]

## Not in scope
[What was not reviewed and why]
```
