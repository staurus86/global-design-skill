# UX Audit Report — [Product / Page Name]

> Template for a UX audit deliverable. Fill every bracketed field. Delete this blockquote and any `[N/A]` sections before delivering. Keep findings specific: name the location, quantify the impact, give a concrete fix.

**Audited:** [URL or screen name]  
**Date:** [YYYY-MM-DD]  
**Auditor:** [Name]  
**Scope:** [What was reviewed — pages, flows, viewports]

---

## Executive Summary

[2–3 sentences. Overall assessment of the experience, and the single top-priority issue to fix first. Lead with the conclusion, not the process.]

**Overall verdict:** [Ship-ready / Needs work / Significant rework required]

---

## Critical Issues — fix before launch

These block core tasks, cause data loss, or fail accessibility/legal requirements.

| # | Issue | Location | Impact | Fix |
|---|---|---|---|---|
| 1 | [What is wrong] | [Page / component] | [Who is affected and how — quantify if possible] | [Specific change to make] |
| 2 | | | | |

---

## Medium Issues — fix in the next sprint

These add friction or confusion but do not block the core task.

| # | Issue | Location | Impact | Fix |
|---|---|---|---|---|
| 1 | [What is wrong] | [Page / component] | [Friction caused] | [Specific change] |
| 2 | | | | |

---

## Improvements — nice to have

Lower-priority refinements that raise quality once critical and medium issues are resolved.

- [Improvement] — [why it helps]
- [Improvement] — [why it helps]

---

## Accessibility Findings

[Summarize WCAG 2.2 AA gaps. List each as: criterion — what fails — where. If none, state "No WCAG 2.2 AA violations found in the audited scope."]

| WCAG criterion | Status | Note |
|---|---|---|
| 1.4.3 Contrast (Minimum) | [Pass / Fail] | [detail] |
| 2.1.1 Keyboard | [Pass / Fail] | [detail] |
| 2.4.7 Focus Visible | [Pass / Fail] | [detail] |
| 2.5.8 Target Size (Minimum) | [Pass / Fail] | [detail] |

---

## Priorities

Ordered by business impact × implementation effort. The top of this list is what to do first.

1. [Issue] — [impact: high/med/low] × [effort: high/med/low]
2. [Issue] — [impact] × [effort]
3. [Issue] — [impact] × [effort]

---

## Estimates

Rough time to resolve each critical issue.

| Issue | Estimate |
|---|---|
| [Critical issue 1] | [e.g. 0.5 day] |
| [Critical issue 2] | [e.g. 2 days] |

---

## Not in Scope

[What was deliberately not reviewed, and why. Prevents the report from being read as a clean bill of health for areas never examined.]

- [Area] — [reason not reviewed]

---

*Template version: global-design-skill v1.0 — `templates/outputs/ux-audit-report.md`*  
*Updated: 2026-05-20*  
*Related: `output-formats.md`, `templates/specs/design-review-report.md`, `agents/ux-architect.md`*
