# Project Brief — Template

> A brief defines what to build and why, before any design work begins. It is the contract between business and design. A brief with vague goals produces vague design. Fill every section with specific, verifiable answers.

**Usage:** Complete this before opening Figma or writing any code. If you cannot fill a section, that gap must be resolved before design begins — not during.

---

## Project: [Name]

**Type:** `[ ] New product` `[ ] New feature` `[ ] Redesign` `[ ] Marketing site` `[ ] Campaign` `[ ] Admin tool`

**Date:** [YYYY-MM-DD]

**Owner:** [Name, role]

**Stakeholders:** [Name — role, Name — role]

**Design lead:** [Name]

**Dev lead:** [Name]

**Ticket / link:** [Linear / Jira / GitHub URL]

---

## Problem

### What exists now

[Describe current state factually. What does the user do today? What product/page/flow are we replacing or extending?]

### Why it's wrong

[Specific, data-backed problems. Not "outdated" — numbers, user quotes, metrics.]

```
Conversion rate:     [current] → [target]
Drop-off point:      [where users leave]
Support tickets:     [volume and category]
User feedback:       [verbatim quotes from research]
Business cost:       [what this problem costs in $, time, or reputation]
```

### Who has this problem

[Specific user description. Not "our users" — persona with context.]

```
Primary user:        [job title / context / expertise level]
Secondary user:      [if any]
User frequency:      [daily / weekly / occasional]
User environment:    [device / location / ambient conditions]
```

---

## Goal

### North Star Metric

[One number that defines success. If you improve this, the project succeeded.]

```
Metric:  [conversion rate / activation rate / NPS / revenue / error rate]
Current: [value]
Target:  [value]
By:      [date]
```

### Secondary metrics (max 3)

```
1. [metric]: [current] → [target]
2. [metric]: [current] → [target]
3. [metric]: [current] → [target]
```

### What success is NOT

[Explicit anti-goals. Prevents misaligned effort.]

- Not: [activity metric — "more users" without retention]
- Not: [vanity metric — "looks more modern"]
- Not: [scope creep — feature not in this project]

---

## Users

### Primary User

**Who:** [Specific description — "B2B SaaS procurement manager, 35-50, makes $500K+ software decisions"]

**Job to be done:** `When [situation], I want to [motivation], so I can [expected outcome].`

**Current pain:** [Exact friction in current flow]

**Success looks like:** [Specific outcome for this user when the product works]

### Secondary Users (if any)

**Who:** [Description]

**Their distinct need:** [What's different from primary user]

---

## Scope

### In scope

- [Explicit list of what must be designed and built]
- [Each item is specific enough to be checked off]

### Out of scope

- [Explicit list — prevents scope creep during execution]
- [Include things that might seem related but aren't in this project]

### Dependencies

| Dependency | Owner | Status | Needed by |
|---|---|---|---|
| [API / design system / data / auth] | [team/person] | [ready/in progress/not started] | [date] |

---

## Constraints

**Technical:**
- [Framework / platform / browser support requirements]
- [Performance budget: LCP < [ms], CLS < [value], INP < [ms]]
- [Bundle size constraints]
- [Third-party service limitations]

**Business:**
- [Legal / compliance requirements]
- [Brand guidelines version — link]
- [Copy/content approval process]

**Timeline:**
```
Design kickoff:   [YYYY-MM-DD]
Design review:    [YYYY-MM-DD]
Dev handoff:      [YYYY-MM-DD]
QA:               [YYYY-MM-DD]
Launch:           [YYYY-MM-DD]
```

---

## Design direction

### Aesthetic

**Archetype:** [Ethereal Black / Editorial Luxury / Cyberbrutalism / Organic Softness / Volumetric Glass / Neo-Maximalism / Post-Digital Terminal / Spatial Luxury]

**The One Memorable Thing:** [One sentence: what will a visitor remember 3 days after seeing this design?]

**Tone:** [3-5 adjectives — e.g., "confident, direct, human" or "calm, data-driven, trustworthy"]

**Reference:** [URLs or descriptions of designs this should feel like — not copy]

**Anti-references:** [Designs this must NOT feel like]

### Content

**Primary copy owner:** [who writes and approves]

**Localization:** `[ ] English only` `[ ] Multiple languages — [list]`

**Images / media:** `[ ] Photography` `[ ] Illustrations` `[ ] Product screenshots` `[ ] Icons only`

**Copy tone:** [Formal / Conversational / Technical / Marketing — with example sentence]

---

## User flows

### Happy path

[Step-by-step: what the user does from entry to success. Every step explicit.]

```
1. User arrives at [entry point] via [source]
2. User sees [first screen / element]
3. User [action]
4. System [response]
5. User [action]
6. User reaches [success state]
```

### Edge cases (must be designed)

| Scenario | Frequency | Design needed |
|---|---|---|
| [Empty state — no data] | [all new users] | [empty state screen] |
| [Error — API fails] | [est. X% of sessions] | [error state] |
| [Slow connection] | [est. X% of sessions] | [skeleton / timeout] |
| [Mobile, small screen] | [est. X% of traffic] | [mobile layout] |
| [Returning user] | [X% of sessions] | [returning state — skip onboarding] |

---

## Competitive analysis

| Competitor | URL | What they do well | What we'll do differently |
|---|---|---|---|
| [Name] | [url] | [specific element] | [specific differentiation] |
| [Name] | [url] | [specific element] | [specific differentiation] |

---

## Open questions

[Questions that must be answered before design begins. Owner + deadline for each.]

| Question | Who decides | Due |
|---|---|---|
| [Specific question] | [Name] | [YYYY-MM-DD] |
| [Specific question] | [Name] | [YYYY-MM-DD] |

---

## Sign-off

| Role | Name | Signature | Date |
|---|---|---|---|
| Product owner | | | |
| Design lead | | | |
| Tech lead | | | |
| Stakeholder | | | |

---

*Sign-off means: you have read this brief, agree with the scope and goals, and commit to flagging scope changes before design is complete — not after.*

---

*Template version: global-design-skill v1.0 — `templates/briefs/project-brief.md`*
