# Template — Redesign Brief

> Use when redesigning an existing page or interface — not building from scratch. The brief must capture what exists, what fails, what must be preserved, and what success looks like. Fill every section before starting design work.

---

## Project Identification

| Field | Value |
|---|---|
| **Project name** | |
| **Current URL(s)** | |
| **Date created** | |
| **Brief owner** | |
| **Design lead** | |
| **Engineering lead** | |
| **Target launch** | |

---

## 1. What We're Redesigning

**Page or flow being redesigned:**
[Name the specific page(s) or user flow. Be precise: "The onboarding wizard, steps 1–3" not "the onboarding."]

**Current version screenshot or URL:**
[Attach or link — never brief a redesign without seeing the current state.]

**Scope boundary:**
[What is explicitly OUT OF SCOPE. Redesign scope always wants to expand — define the fence.]

---

## 2. Why We're Redesigning

**The problem with the current design:**
[Specific, data-backed. "Conversion rate is 12% vs. industry average 28%" is a problem. "It looks old" is not.]

**Data or evidence:**
[Quantitative: analytics, heatmaps, session recordings, A/B test results.
Qualitative: user research findings, support ticket themes, NPS verbatims.]

**Why the current design can't fix this with incremental changes:**
[Redesigns are expensive. Explain why a redesign is the right solution rather than targeted improvements. If you can't answer this, consider whether a redesign is warranted.]

---

## 3. Users

**Primary user:**
[Role, context, goal. Not a demographic — a situation: "A developer evaluating API integrations at 10pm before a demo tomorrow."]

**Secondary users:**
[If applicable. Same specificity.]

**What the user is trying to accomplish:**
[The job-to-be-done. "Find out if this tool solves my problem before my manager asks tomorrow."]

**What currently frustrates them:**
[Specific friction points from user research or support data.]

---

## 4. Business Goal

**Primary metric we're moving:**
[One metric. Conversion rate, activation rate, task completion, NPS, support volume — pick one.]

**Current value:**
**Target value:**
**Measurement method:**
**Timeline for measurement:**

**Secondary metrics (monitored, not primary):**
[These should not improve at the expense of the primary metric.]

---

## 5. What Must Be Preserved

> This section prevents accidental regression. Every item here must be verified in design review before handoff.

**Content that cannot change:**
[Legal copy, compliance requirements, pricing information, specific claims.]

**Patterns that work (do not redesign):**
[From user research or data: interactions, flows, or elements with above-average engagement.]

**Technical constraints:**
[APIs that drive content, CMS structure, iframe embeds, third-party integrations that cannot change.]

**Brand constraints:**
[Logo usage, trademark requirements, colors that must stay, approved typography if specified.]

---

## 6. Design Constraints

**Token system:**
[Which token file? `tokens/tokens.css`. Are custom tokens allowed or must we stay in the existing system?]

**Component library:**
[Which component library is this built on? Shadcn/UI, custom, Radix? This affects what we can design.]

**Responsive targets:**
[390px (iPhone SE), 768px (iPad), 1280px (laptop), 1920px (desktop). Which are required?]

**Browser/platform targets:**
[Baseline 2024? IE11 (if legacy)? Specific OS versions for native apps?]

**Performance budget:**
[LCP ≤2.5s, CLS ≤0.1, INP ≤200ms. Are there tighter requirements?]

**Timeline:**
[Design completion, review completion, handoff date, ship date.]

---

## 7. Aesthetic Direction

**Archetype (from `references/aesthetic-archetypes.md`):**
[Which archetype? A–H. Or "same as current" with specific exceptions.]

**Reference sites:**
[3–5 sites from `references/inspiration-sites.md` that this redesign should look toward. Not "similar" to your product — sites that solve the specific problem this redesign addresses.]

**Tone:**
[From `SKILL.md` — quiet / excited / calm / authoritative / warm / tense?]

**What the design should NOT look like:**
[Specific examples of aesthetics to avoid — and why. "Not like [Site X] because their pricing section is manipulative" is actionable.]

---

## 8. Acceptance Criteria

> The redesign is complete when ALL of the following are true.

**Functional:**
- [ ] All 8 quality gates pass (see `quality-gates.md`)
- [ ] All 5 scoring dimensions ≥15/20
- [ ] No banned patterns present
- [ ] [Specific user flow test]: user can complete [task] in under [time]

**Metric:**
- [ ] [Primary metric] reaches [target] within [timeframe of measurement]

**Process:**
- [ ] Design Director agent: PASS or CONDITIONAL
- [ ] Accessibility Auditor: zero critical, zero major issues
- [ ] Frontend Handoff Reviewer: Gate 8 pass
- [ ] Engineering lead sign-off: implementation questions answered
- [ ] Product owner sign-off: scope matches brief

---

## 9. What Success Looks Like

**In 2 weeks:**
[Measurable indicator that design is on track]

**In 2 months:**
[Measurable indicator that the redesign achieved its goal]

**Failure definition:**
[What would indicate the redesign did not work. If you don't define failure, you can't learn from it.]

---

## Sign-Off

> The brief is complete when all owners sign off. Do not begin design work until this table is filled.

| Role | Name | Status | Date |
|---|---|---|---|
| Product owner | | Approved | |
| Design lead | | Approved | |
| Engineering lead | | Approved | |
| Stakeholder (if external) | | Approved | |

---

*Template version: global-design-skill v1.0 — `templates/briefs/redesign-brief.md`*  
*Related: `blueprints/redesign-existing-page.md`, `templates/specs/design-review-report.md`, `quality-gates.md`*
