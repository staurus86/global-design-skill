# Checklist — Admin Panel Review

> Admin panels are judged by efficiency, not beauty. The user is a professional doing the same task hundreds of times. This checklist audits an admin panel for density, speed, safety, and clarity. Run it before shipping any back-office interface.

---

## How to Use

Mark each item **[P]** Pass, **[F]** Fail, **[N/A]** Not applicable.

- Score = (passed / relevant) × 100
- **≥ 90%** — ship
- **75–89%** — fix critical items first
- **< 75%** — not ready

Critical sections: 2 (data tables), 5 (destructive actions), 7 (states). A fail there blocks ship regardless of total score.

---

## 1. Layout & Density

- [ ] Density-first: information is not padded out with marketing-style whitespace
- [ ] Sidebar or top nav gives access to all primary sections within one click
- [ ] Active navigation item is visually marked
- [ ] Content max-width does not waste horizontal space on wide screens
- [ ] Page-level actions (Create, Export) are in a consistent, predictable location
- [ ] No decorative hero sections — admin panels open straight into work

---

## 2. Data Tables

- [ ] Column headers are labeled clearly — no ambiguous abbreviations
- [ ] Numeric columns are right-aligned; text columns left-aligned
- [ ] Sortable columns show sort state with `aria-sort`
- [ ] Sticky header keeps column labels visible while scrolling
- [ ] Row density mode available (comfortable / compact) if rows exceed ~20
- [ ] Tables with > 200 rows are virtualized
- [ ] Pagination or infinite scroll decision matches the data volume
- [ ] Each row's primary action is reachable without a hover-only menu
- [ ] Empty table shows a useful empty state, not a blank grid

---

## 3. Filters & Search

- [ ] Filters are visible or one click away — not buried
- [ ] Active filters are shown as removable chips
- [ ] Filter state is reflected in the URL (shareable, survives refresh)
- [ ] Search has a visible loading indicator and a no-results state
- [ ] Clearing all filters is a single action

---

## 4. Forms & Editing

- [ ] Every input has a persistent visible label
- [ ] Required vs. optional fields are clearly distinguished
- [ ] Validation errors appear inline, next to the field, with a fix instruction
- [ ] Save behavior is explicit: save-on-change vs. explicit submit — not ambiguous
- [ ] Unsaved-changes warning when navigating away from a dirty form
- [ ] Long forms are grouped into labeled sections
- [ ] Form never silently discards data on error

---

## 5. Destructive Actions

- [ ] Delete / archive / bulk-destroy actions have friction proportional to impact
- [ ] Irreversible actions require confirmation naming the specific item(s)
- [ ] Destructive buttons are visually distinct (not the same as primary)
- [ ] Bulk destructive actions state the exact count being affected
- [ ] An undo path exists where technically feasible
- [ ] Destructive actions are not the default focus target in a dialog

---

## 6. Bulk Actions

- [ ] Row selection is clear (checkbox, select-all, indeterminate state)
- [ ] A bulk-action bar appears on selection, showing the selected count
- [ ] Bulk actions confirm before executing
- [ ] Selection state survives pagination, or the limitation is made explicit

---

## 7. States

- [ ] Loading: skeleton matches the real layout dimensions (no CLS)
- [ ] Empty: first-use empty state explains what to do, not just "no data"
- [ ] Error: failed loads show what failed, why, and a retry action
- [ ] Partial failure (some rows failed an action) is communicated per-row
- [ ] Permission-denied state is distinct from empty and from error

---

## 8. Efficiency & Keyboard

- [ ] Common actions have keyboard shortcuts, documented in-app
- [ ] Tab order is logical through tables, filters, and forms
- [ ] Focus is visible on every interactive element
- [ ] No action requires a hover that a keyboard user cannot trigger
- [ ] Frequent workflows do not require excessive clicks or page loads

---

## 9. Feedback & Trust

- [ ] Every action gets feedback within 400ms (Doherty Threshold)
- [ ] Success and failure of background jobs are surfaced (toast, banner, status)
- [ ] Timestamps and audit info are shown where accountability matters
- [ ] Optimistic UI updates roll back visibly on failure

---

## Final Gate

| Question | Answer |
|---|---|
| Can a power user complete the core task faster than in a spreadsheet? | Yes / No |
| Is every destructive action protected proportionally to its damage? | Yes / No |
| Does every data view have loading, empty, and error states? | Yes / No |
| Is the panel fully operable by keyboard? | Yes / No |

---

*Checklist version: global-design-skill v1.0 — `checklists/admin-panel-review.md`*  
*Updated: 2026-05-20*  
*Related: `rules/12-admin-panels.md`, `rules/11-data-tables.md`, `blueprints/admin-panel-from-scratch.md`, `patterns/admin-ui/`*
