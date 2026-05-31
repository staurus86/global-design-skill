# Design Iteration Log

Track how many rounds of revision each design output required before acceptance.
Low iteration count = skill is producing correct output. High count = a rule or
pattern needs updating.

## Log Entry Template

```
Date: YYYY-MM-DD
Task type: [ ] Landing page  [ ] Component  [ ] Admin panel  [ ] Other: ___
Iterations to acceptance: [number]
Round 1 rejection reason: [what was wrong]
Round 2+ rejection reasons: [what was still wrong]
Pattern implicated: [which file should be updated to prevent this]
```

## Aggregate Metrics (update weekly)

| Metric | Value |
|--------|-------|
| Average iterations this sprint | |
| Median iterations | |
| Tasks accepted in 1 iteration | |
| Target: accepted in ≤ 2 iterations | 80% |

---

## Entries

```
Date: 2026-05-31
Task type: [x] Other: live multi-page redesign (sk-seo.ru) — bento language + branded icons + portraits + blog CTAs, shipped to prod
Iterations to acceptance: 1 per page (each page verified before tiling; no rework)
Round 1 rejection reason: none on the work itself. One process miss caught: a hand-off summary CLAIMED an axe pass + before/after screenshots that did not exist on disk → had to actually run the verification, not trust the claim.
Round 2+ rejection reasons: none
Pattern implicated (updated this round):
  - patterns/marketing-blocks/bento-grid.md — added Proof-Bento Variants (proof-cell hero / spotlight price-anchor / statement band) + Editorial Meta-Spec + the "new fact, not an echo" content rule
  - rules/15-iconography.md — added R11 (a domain-specific branded icon set can BE the system; 1 topic→1 icon, no repeats on a plane, bare, lazy)
  - blueprints/redesign-existing-page.md — added Verify-before-tile (Phase 6) + two anti-patterns (tile-before-verify, shipping deploy junk on no-build sites)
Net: low iteration count = the existing bento/redesign rules held; gaps were (a) branded-icon-as-system, (b) verify-before-tile discipline, (c) deploy hygiene — now encoded.
Evidence: examples/before-after/sk-seo-2026-05-31/ (before/ + after/ + components/ + DESIGN-DECISIONS.md), live at https://sk-seo.ru
```
