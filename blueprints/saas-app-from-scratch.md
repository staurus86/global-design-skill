# SaaS App — From Scratch

> Build protocol for a product UI: authenticated app, data-driven screens, multi-state components. Covers shell, navigation, core screens, and empty/loading/error states.

**Load alongside:** `rules/13-saas-products.md` · `patterns/product-ui/` · `patterns/navigation/` · `checklists/ui-review.md`

---

## Before You Start — Resolve These First

```
Primary user: [role + technical literacy: low / medium / high]
Primary device: [mobile / desktop / both — with % split if known]
Core workflow: [the one thing users do most often]
Data density: [low — few items / medium / high — complex tables, charts]
Notification model: [real-time / polling / manual refresh]
Auth model: [single user / team / multi-tenant org]
```

**Blocked until answered:**
- What is the one screen users spend 70%+ of their time on? (Start there)
- What does an empty account look like? (Day 1 experience)
- What does a power user's account look like? (Day 90 experience)

---

## App Shell — Decide First

The shell is the structural decision that everything else inherits.

### Shell Option A: Sidebar + Content
```
┌──────────┬─────────────────────────────┐
│ Sidebar  │ Content area                │
│ (240px)  │ (fluid)                     │
│          │                             │
│          │                             │
└──────────┴─────────────────────────────┘
```
**Use when:** app has 5+ primary sections, complex navigation hierarchy, frequent context-switching.

### Shell Option B: Top Nav + Content
```
┌─────────────────────────────────────────┐
│ Top navigation                          │
├─────────────────────────────────────────┤
│ Content area (fluid)                    │
│                                         │
└─────────────────────────────────────────┘
```
**Use when:** app has ≤ 5 primary sections, marketing-adjacent (public + auth views), mobile-first.

### Shell Option C: Sidebar + Secondary Sidebar + Content
```
┌────────┬──────────┬──────────────────────┐
│ Nav    │ Secondary│ Content              │
│ (64px) │ (240px)  │ (fluid)              │
│ icons  │ context  │                      │
└────────┴──────────┴──────────────────────┘
```
**Use when:** app has nested navigation (teams → projects → files), IDE-like structure, desktop-primary.

**Mobile for all shells:** sidebar collapses to bottom tab bar (4-5 items max) or hamburger drawer.

---

## Navigation Architecture

**Top-level items:** ≤ 7 (Hick's Law)
**Naming:** task verbs, not nouns ("Create report" not "Reports" if that's the primary action)
**Current state:** visually clear — not just color (add weight, background, icon fill)
**Hierarchy:**
- Level 1: primary sections (sidebar or top nav)
- Level 2: subsections (secondary sidebar or tabs within content)
- Level 3: filters, views, sort controls within a section

---

## Core Screens — Build in This Order

### 1. Empty state — Dashboard or primary screen

The first experience for new users. If this screen is broken, users never see the product's value.

**Structure:**
```
[Illustration or icon — not generic]
Headline: [Why it's empty — specific]
Subtext: [What to do to fill it — one sentence]
CTA: [The first action — specific verb]
```

**Requirements:**
- Illustration is specific to this product, not generic "no data" imagery
- CTA goes directly to creation, not to a settings page
- Never show a skeleton loader for a genuinely empty state

---

### 2. Loading state — primary data screen

**Rules by duration:**
- < 100ms: no indicator (show immediately)
- 100ms–1s: skeleton loader (match layout of loaded state exactly)
- 1–10s: skeleton + progress indicator
- > 10s: progress + "continue in background" option

**Skeleton requirements:**
- Same layout as loaded content (not generic rows)
- Animated shimmer: CSS `animation-timeline` or `@keyframes` shimmer
- Never skeleton for navigation, headers, or persistent UI

---

### 3. Primary data screen (list or table)

The screen users return to most. Design for the 90th-percentile user (full data), not day 1.

**Required elements:**
- Page title + action ("Projects" + "New project" button — top right)
- Search / filter controls (if > 20 expected items)
- Sort control on each column header (tables) or sort dropdown (lists)
- Bulk action bar (appears when items selected)
- Pagination or infinite scroll (decide one — never both)
- Empty state for filtered results ("No results for 'query' — clear filters")

**Table-specific:**
- Column order: most-used first
- Fixed columns: identifier column always visible on horizontal scroll
- Row actions: visible on hover (desktop), always visible (mobile)
- Row height: comfortable (48px), compact (36px), spacious (64px) — decide once

---

### 4. Detail / edit screen

A single item in full detail: view, edit, related data.

**Structure:**
```
Page header: [item name] + [primary action] + [secondary actions]
Content area: [main fields / content / canvas]
Sidebar (if needed): [metadata, related items, activity log]
```

**State machine:**
- View mode → Edit mode → Saving → Saved / Error
- Unsaved changes: browser `beforeunload` warning + in-page indicator
- Autosave: visible indicator ("Saved 2 seconds ago")
- Conflict: two users editing simultaneously — merge or lock?

---

### 5. Settings screen

**Architecture:**
```
Settings
├── Account (name, email, password, avatar)
├── Notifications (granular per-event controls)
├── Integrations (connect external services)
├── Billing (plan, payment method, invoices)
└── Danger zone (delete account)
```

**Rules:**
- Changes save immediately (toggle) or require explicit save (form) — decide per section
- Destructive actions (delete account, cancel subscription) require confirmation: name the consequence, use a destructive-labeled button
- Danger zone section is visually separated and comes last

---

### 6. Onboarding flow

**Goal:** get user to first value moment (not just account setup).

**Structure:**
- Step 1: minimum required info (name + password, if social auth not used)
- Step 2: personalization (role, use case — max 2 questions)
- Step 3: create first item (guided, not a tutorial)
- Step 4: invite team (optional, skippable)

**Rules:**
- Progress indicator visible at all times
- "Skip" available for non-critical steps
- Each step has one primary action
- First value moment happens inside the app, not in an email

---

## Notification System

Decide the model before building:

| Type | When | Component | Duration |
|---|---|---|---|
| Toast | Non-critical success/info | Overlay, top-right | 4s auto-dismiss |
| Error toast | Action failed | Overlay, top-right | Persist until dismissed |
| Inline error | Form validation | Below field | Until corrected |
| Banner | System-wide alert | Below nav, full width | Until dismissed |
| Modal | Destructive confirmation | Blocking | Until decision |

**Rules:**
- Max 1 toast visible at a time (queue, don't stack)
- `aria-live="polite"` on toast container, `aria-live="assertive"` for errors
- All toasts keyboard-dismissable (Escape)

---

## Design System Decisions

```css
/* App-specific token additions beyond landing page base */

/* Surfaces — layered depth */
--color-base:      oklch(/* darkest */);
--color-surface:   oklch(/* +2% L */);
--color-surface-2: oklch(/* +4% L */);
--color-surface-3: oklch(/* +6% L */);

/* Data states */
--color-success:   oklch(65% 0.18 145);
--color-warning:   oklch(75% 0.18 80);
--color-error:     oklch(55% 0.22 25);
--color-info:      oklch(65% 0.18 250);

/* Sidebar */
--sidebar-width:      240px;
--sidebar-width-collapsed: 64px;
--sidebar-bg:         var(--color-surface);
--sidebar-border:     1px solid var(--color-border);

/* Content */
--content-max-width: 1280px;
--content-padding:   var(--space-6) var(--space-8);
```

---

## Component State Requirements

Every component in a SaaS app must have all states documented before development:

| Component | Required states |
|---|---|
| Data table | loading (skeleton) · empty (no data) · populated · row-selected · error |
| Form | idle · focused · filled · validating · invalid · submitting · success · server-error |
| Button | idle · hover · active · loading · disabled · success |
| Dropdown/Select | closed · open · option-hovered · option-selected · disabled |
| Modal | entering · open · confirming (destructive) · closing |
| Toast | entering · visible · exiting |
| Search | empty · typing · loading · results · no-results · error |
| Sidebar item | idle · hover · active (current) · collapsed |

---

## Technology Decisions

**Component library:** shadcn/ui + Tailwind v4 (default)
- `@import "tailwindcss"; @import "tw-animate-css"; @import "shadcn/tailwind.css"`
- Theming via `@theme inline` — OKLCH throughout

**Data fetching:** React 19 + Next.js 15
```tsx
// Server action pattern
'use server'
async function updateItem(formData: FormData) {
  const result = await db.items.update(/* ... */)
  revalidatePath('/items')
}

// Client component with useActionState
const [state, action, isPending] = useActionState(updateItem, null)
```

**Optimistic updates:**
```tsx
const [optimisticItems, addOptimistic] = useOptimistic(items)
// Update UI immediately, sync with server in background
```

**Caching (Next.js 15):**
```tsx
'use cache'
export async function getItems() {
  const data = await db.items.findMany()
  cacheLife('minutes') // profile: seconds | minutes | hours | days | weeks
  return data
}
```

---

## Quality Gates

- [ ] Gate 1: Problem Definition (user, workflow, success metric)
- [ ] Gate 2: Information Architecture (all screens listed, navigation ≤ 7)
- [ ] Gate 3: Design System (tokens, type scale, spacing)
- [ ] Gate 4: States (all states per component — see table above)
- [ ] Gate 5: Responsive (390px mobile, sidebar collapses)
- [ ] Gate 6: Accessibility (keyboard navigation through entire app, ARIA on all interactive)
- [ ] Gate 8: Frontend Readiness (every state documented, every token named)

Run `agents/ux-architect.md` for flow review.
Run `agents/frontend-handoff-reviewer.md` before development.
