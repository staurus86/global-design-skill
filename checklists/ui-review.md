# UI Review Checklist — Product & Admin

> Run before every UI feature ships. Covers product UI, admin panels, SaaS apps, and data-heavy interfaces. Distinct from landing-conversion-review.md (which is for marketing pages).

**Legend:** ✅ Pass · ❌ Fail (blocks ship) · ⚠️ Needs review · N/A Not applicable

---

## 1. Component States

*Every interactive element must have all applicable states designed and implemented.*

| # | Check | Priority | Status |
|---|---|---|---|
| 1.1 | Idle state defined with exact token values | CRITICAL | |
| 1.2 | Hover state present (`@media (hover: hover)` — not on touch) | CRITICAL | |
| 1.3 | Active/pressed state present (scale or darkening) | CRITICAL | |
| 1.4 | Focus-visible ring: 2px solid `var(--color-accent)`, correct offset | CRITICAL | |
| 1.5 | Disabled state: opacity 0.4, cursor not-allowed, pointer-events none | CRITICAL | |
| 1.6 | Loading state: spinner/skeleton + label changes + element disabled | CRITICAL | |
| 1.7 | Error state: border-color change + error message + aria-invalid | CRITICAL | |
| 1.8 | Empty state: illustration/icon + title + body + CTA (specific, not generic) | CRITICAL | |
| 1.9 | Success state: feedback message + duration defined | IMPORTANT | |

---

## 2. Forms

| # | Check | Priority | Status |
|---|---|---|---|
| 2.1 | Every input has a visible `<label>` (not placeholder as label) | CRITICAL | |
| 2.2 | Placeholder text is example data, not field label | CRITICAL | |
| 2.3 | Error messages: "[Field] — [Why] — [How to fix]" formula | CRITICAL | |
| 2.4 | Error appears inline below field, not only on submit | IMPORTANT | |
| 2.5 | `aria-invalid="true"` on errored input | CRITICAL | |
| 2.6 | `aria-describedby` links input to helper text and error message | IMPORTANT | |
| 2.7 | Required fields marked (not only with color — use asterisk + legend) | CRITICAL | |
| 2.8 | Submit button label describes action: "Save changes" not "Submit" | CRITICAL | |
| 2.9 | Form never resets fields on failed submit | CRITICAL | |
| 2.10 | Multi-step form: progress indicator + back navigation | IMPORTANT | |
| 2.11 | Password fields have show/hide toggle | IMPORTANT | |
| 2.12 | Date inputs use native `<input type="date">` or accessible date picker | IMPORTANT | |
| 2.13 | Autocomplete attributes set on appropriate fields | NICE | |

---

## 3. Data Tables (admin/product)

| # | Check | Priority | Status |
|---|---|---|---|
| 3.1 | Sticky table header when table scrolls vertically | CRITICAL | |
| 3.2 | Sort state visible with icon (unsorted / ascending / descending) | CRITICAL | |
| 3.3 | Sort button accessible (keyboard, aria-label with direction) | CRITICAL | |
| 3.4 | Empty state inside `<tbody>` with colspan spanning all columns | CRITICAL | |
| 3.5 | Loading skeleton rows with `aria-busy="true"` | CRITICAL | |
| 3.6 | Bulk action bar appears only when rows are selected | IMPORTANT | |
| 3.7 | Bulk delete confirmation shows count: "Delete 24 items?" not "Delete items?" | CRITICAL | |
| 3.8 | Row actions hidden until hover (desktop), always visible (mobile) | IMPORTANT | |
| 3.9 | Pagination: "Showing X–Y of Z results" + page controls | CRITICAL | |
| 3.10 | Table horizontally scrollable on small screens (not page scroll) | CRITICAL | |
| 3.11 | Row hover background change provides subtle selection feedback | IMPORTANT | |
| 3.12 | "Select all" checkbox has indeterminate state when partial selection | IMPORTANT | |

---

## 4. Filters & Search

| # | Check | Priority | Status |
|---|---|---|---|
| 4.1 | Active filters shown as dismissible chips | CRITICAL | |
| 4.2 | "Clear all filters" button when multiple filters active | CRITICAL | |
| 4.3 | Filter state preserved in URL params | IMPORTANT | |
| 4.4 | Search debounced (300ms — not firing on every keystroke) | CRITICAL | |
| 4.5 | Filter dropdown: count of matching records per option | IMPORTANT | |
| 4.6 | Filter panel closes on Escape or outside click | IMPORTANT | |
| 4.7 | Active filter button visually distinct from inactive | CRITICAL | |
| 4.8 | Filter clear button removes chip and reloads data | CRITICAL | |

---

## 5. Navigation

| # | Check | Priority | Status |
|---|---|---|---|
| 5.1 | Active nav item visually distinct (color + weight or background) | CRITICAL | |
| 5.2 | Nav items ≤ 7 (Hick's Law) | IMPORTANT | |
| 5.3 | Skip navigation link at page top | CRITICAL | |
| 5.4 | Mobile navigation: bottom tabs or drawer (not desktop nav on mobile) | CRITICAL | |
| 5.5 | Mobile nav items ≥ 44px touch target | CRITICAL | |
| 5.6 | Hamburger button: `aria-expanded` + label changes on open/close | CRITICAL | |
| 5.7 | Drawer: focus trap + Escape closes + focus returns to trigger | CRITICAL | |
| 5.8 | Dropdown menus: `aria-haspopup` + `aria-expanded` + keyboard nav | CRITICAL | |
| 5.9 | Breadcrumbs use `<nav aria-label="Breadcrumb">` + `aria-current="page"` | IMPORTANT | |

---

## 6. Modals & Dialogs

| # | Check | Priority | Status |
|---|---|---|---|
| 6.1 | Uses native `<dialog>` element | IMPORTANT | |
| 6.2 | `aria-modal="true"` + `aria-labelledby` pointing to title | CRITICAL | |
| 6.3 | Focus moves to modal on open (first focusable element or heading) | CRITICAL | |
| 6.4 | Focus trap: Tab stays within modal | CRITICAL | |
| 6.5 | Escape closes modal | CRITICAL | |
| 6.6 | Focus returns to trigger element on close | CRITICAL | |
| 6.7 | Backdrop click closes modal (except destructive confirmations) | IMPORTANT | |
| 6.8 | Destructive action modal: action button is red/destructive variant | CRITICAL | |
| 6.9 | Type-to-confirm for catastrophic actions (delete account, drop database) | CRITICAL | |
| 6.10 | Modal animates in with `@starting-style` | IMPORTANT | |

---

## 7. Loading & Skeleton States

| # | Check | Priority | Status |
|---|---|---|---|
| 7.1 | Loading indicator matches timing: <100ms none, 100ms–1s skeleton, 1–10s progress | CRITICAL | |
| 7.2 | Skeleton matches exact layout of loaded content | CRITICAL | |
| 7.3 | Skeleton has shimmer animation | IMPORTANT | |
| 7.4 | `aria-busy="true"` on loading container | CRITICAL | |
| 7.5 | Button shows spinner + "Saving…" label during async actions | CRITICAL | |
| 7.6 | Optimistic updates implemented for instant feedback (React `useOptimistic`) | IMPORTANT | |
| 7.7 | Progress bar for operations > 1s | IMPORTANT | |
| 7.8 | Staggered skeleton animation for lists/tables (wave effect) | NICE | |

---

## 8. Error States

| # | Check | Priority | Status |
|---|---|---|---|
| 8.1 | Every error message follows: [What failed] — [Why] — [How to fix] | CRITICAL | |
| 8.2 | Network error has retry action | CRITICAL | |
| 8.3 | 404 page has navigation back + search + home link | CRITICAL | |
| 8.4 | 500 page has: what happened + retry + support contact | CRITICAL | |
| 8.5 | Form errors maintain field values (never reset on error) | CRITICAL | |
| 8.6 | Toast errors: persist until dismissed (not auto-dismiss) | CRITICAL | |
| 8.7 | `aria-live="assertive"` on blocking errors, `"polite"` on non-blocking | CRITICAL | |
| 8.8 | Session timeout: warning before expiry, not surprise logout | IMPORTANT | |

---

## 9. Notifications & Feedback

| # | Check | Priority | Status |
|---|---|---|---|
| 9.1 | Toast position: top-right desktop, bottom mobile | IMPORTANT | |
| 9.2 | Toast types: success (green), error (red), warning (yellow), info (blue/neutral) | IMPORTANT | |
| 9.3 | Toast has dismiss button (× or swipe) | CRITICAL | |
| 9.4 | Success toasts auto-dismiss after 4–6s | IMPORTANT | |
| 9.5 | Error toasts persist until dismissed | CRITICAL | |
| 9.6 | Notification badges show count (max "99+") | IMPORTANT | |
| 9.7 | Critical alerts use banner (not toast) — appear above main content | IMPORTANT | |

---

## 10. Accessibility (Product-Specific)

| # | Check | Priority | Status |
|---|---|---|---|
| 10.1 | All interactive elements reachable via Tab | CRITICAL | |
| 10.2 | Tab order matches visual reading order | CRITICAL | |
| 10.3 | Custom dropdowns/selects keyboard-navigable (Arrow keys, Enter, Escape) | CRITICAL | |
| 10.4 | Data visualizations have text alternatives | CRITICAL | |
| 10.5 | Status colors supplemented by label/icon (color is not the only indicator) | CRITICAL | |
| 10.6 | Screen reader announcement for dynamic content changes (`aria-live`) | CRITICAL | |
| 10.7 | Drag-and-drop: keyboard alternative provided | IMPORTANT | |
| 10.8 | Time-based content: user can pause/stop/extend | IMPORTANT | |
| 10.9 | No keyboard traps (except intentional focus traps in modals) | CRITICAL | |

---

## 11. Admin Panel Specifics

*Skip this section for consumer product UIs.*

| # | Check | Priority | Status |
|---|---|---|---|
| 11.1 | Every data field has a label — no unlabeled numbers or icons | CRITICAL | |
| 11.2 | Density appropriate: at least 3 data points visible per KPI card | CRITICAL | |
| 11.3 | Status indicators: color + label + icon (never color alone) | CRITICAL | |
| 11.4 | Destructive actions have 3-level friction system | CRITICAL | |
| 11.5 | Audit log exists for irreversible actions | IMPORTANT | |
| 11.6 | Access control state visible (locked/restricted elements are marked) | IMPORTANT | |
| 11.7 | Real-time dashboard: "Last updated" timestamp visible | CRITICAL | |
| 11.8 | Keyboard shortcuts documented and discoverable | NICE | |
| 11.9 | Export functionality available on all data tables | IMPORTANT | |

---

## 12. Performance

| # | Check | Priority | Status |
|---|---|---|---|
| 12.1 | INP ≤ 200ms: interactions feel immediate | CRITICAL | |
| 12.2 | Doherty Threshold: any action taking > 400ms shows loading feedback | CRITICAL | |
| 12.3 | Infinite scroll not used in admin tables (use pagination) | CRITICAL | |
| 12.4 | Large lists virtualized (> 200 rows) | IMPORTANT | |
| 12.5 | Image lazy loading on below-fold content | IMPORTANT | |

---

## Pre-Ship Checklist

```
[ ] All CRITICAL checks pass
[ ] Tested at 390px, 768px, 1280px
[ ] Tested with keyboard only (no mouse)
[ ] Tested with screen reader (VoiceOver Mac or NVDA Windows)
[ ] Tested at 200% browser zoom
[ ] Error states verified: trigger each error, confirm message and recovery
[ ] Loading states verified: throttle network to Slow 3G
[ ] Empty states verified: delete all data and confirm empty state shows
[ ] All forms: submit with invalid data, confirm error states
[ ] All forms: submit with valid data, confirm success state
[ ] Dark mode (if applicable): all states verified
[ ] Console: no errors or warnings in production build
```

---

## Review Summary

**Date:** [YYYY-MM-DD]

**Reviewer:** [Name]

**Feature / page:** [Name]

**Critical fails:** [N]

**Important fails:** [N]

**Verdict:**
```
[ ] SHIP — all critical pass
[ ] CONDITIONAL — fix before ship: [list items]
[ ] BLOCK — critical failures: [list failures]
```

---

*Checklist version: global-design-skill v1.0 — `checklists/ui-review.md`*
*Related: `checklists/global-design-review.md`, `rules/12-admin-panels.md`, `rules/13-saas-products.md`, `agents/frontend-handoff-reviewer.md`*
