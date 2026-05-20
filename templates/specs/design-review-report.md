# Template — Design Review Report

> Use this template to document the output of any design review session. Fill in every section. Leave no placeholders. A review report with empty sections means the review wasn't done.

---

## Review Metadata

| Field | Value |
|---|---|
| **Product / Page** | [name + URL if applicable] |
| **Review date** | [YYYY-MM-DD] |
| **Reviewer** | [name / role] |
| **Review type** | [Initial audit / Pre-ship / Post-launch / Competitive] |
| **Scope** | [Landing page / Dashboard / Feature / Full product] |
| **Overall score** | [X]/100 |

---

## Verdict

<!-- Choose one: -->
- [ ] **PASS** — All 8 quality gates clear. Ship when implementation is complete.
- [ ] **CONDITIONAL** — Gates 1–7 clear. Issues below must be resolved before Gate 8.
- [ ] **REVISE** — Multiple gates fail. Return to design before implementation begins.
- [ ] **BLOCKED** — Critical issues require re-scoping. Schedule design sprint.

---

## Quality Gate Status

| Gate | Status | Notes |
|---|---|---|
| Gate 1 — Problem defined | ✅ / ❌ | |
| Gate 2 — User identified | ✅ / ❌ | |
| Gate 3 — Metric set | ✅ / ❌ | |
| Gate 4 — All states designed | ✅ / ❌ | |
| Gate 5 — Responsive behavior specified | ✅ / ❌ | |
| Gate 6 — ARIA specified | ✅ / ❌ | |
| Gate 7 — Tokens used | ✅ / ❌ | |
| Gate 8 — Developer can implement | ✅ / ❌ | |

---

## Dimension Scores

| Dimension | Score | Finding |
|---|---|---|
| Visual hierarchy | /20 | |
| Typography | /20 | |
| Color | /20 | |
| Motion | /20 | |
| Accessibility | /20 | |
| **Total** | **/100** | |

---

## Banned Patterns Found

> List every banned pattern detected. Each item is a blocker until resolved.

| Pattern | Location | Severity | Fix |
|---|---|---|---|
| [Pattern name] | [Component / Section / Line] | Critical / Major | [Specific fix] |

*If none found: "No banned patterns detected."*

---

## Critical Issues (block shipping)

> Items that must be fixed before any implementation begins.

1. **[Issue title]**
   - Location: [specific component or section]
   - Problem: [what is wrong and why it matters]
   - Fix: [specific, actionable instruction]
   - Reference: [rules file / pattern file]

2. **[Issue title]**
   - ...

---

## Major Issues (fix before handoff)

> Items that must be resolved before Gate 8 (developer handoff).

1. **[Issue title]**
   - Location:
   - Problem:
   - Fix:
   - Reference:

---

## Minor Issues (fix in implementation)

> Items that can be addressed during implementation but must be resolved before ship.

1. **[Issue title]**
   - Location:
   - Fix:

---

## Strengths

> Document what the design does well. These inform what NOT to change.

1. [Strength — specific, not generic]
2. [Strength]
3. [Strength]

---

## Recommendations

> Prioritized list of concrete next actions.

### Priority 1 — Required before implementation
- [ ] [Action item with owner]
- [ ] [Action item]

### Priority 2 — Required before handoff (Gate 8)
- [ ] [Action item]
- [ ] [Action item]

### Priority 3 — Required before ship
- [ ] [Action item]

### Priority 4 — Nice to have (post-ship iteration)
- [ ] [Action item]

---

## Agent Review Outputs

> Attach outputs from specialized agents when they were run.

### Design Director
- Verdict: [PASS / CONDITIONAL / REVISE]
- Top finding: [one sentence]

### UX Architect
- Verdict:
- Top finding:

### Conversion Designer *(if marketing page)*
- Verdict:
- Top finding:

### Design Critic
- Verdict: [REJECTED / CONDITIONAL / APPROVED]
- Top finding:

### Accessibility Auditor
- Critical: [count]
- Major: [count]
- Minor: [count]

### Performance Auditor *(if implemented)*
- LCP: [measured value vs. target ≤2.5s]
- CLS: [measured value vs. target ≤0.1]
- INP: [measured value vs. target ≤200ms]

### Copy Editor *(if text-heavy page)*
- Headline score: [/10]
- Banned words found: [list]

---

## Sign-Off

| Role | Name | Status | Date |
|---|---|---|---|
| Design lead | | Approved / Needs revision | |
| Engineering lead | | Approved / Needs revision | |
| Product owner | | Approved / Needs revision | |

---

*Template version: global-design-skill v1.0 — `templates/specs/design-review-report.md`*  
*Related: `checklists/global-design-review.md`, `skills/global-design/quality-gates.md`, `agents/`*
