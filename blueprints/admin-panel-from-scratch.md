# Admin Panel — From Scratch

> Build protocol for internal tooling: data tables, bulk operations, system management, operator workflows. Optimized for efficiency, not delight.

**Load alongside:** `rules/12-admin-panels.md` · `patterns/admin-ui/` · `checklists/admin-panel-review.md`

---

## Before You Start — Resolve These First

```
Primary operator: [role + technical literacy — assume medium/high for internal tools]
Data volume: [rows per table, expected growth rate]
Access control: [single role / multi-role / permission matrix]
Critical operations: [which actions are irreversible — define before building]
Audit requirements: [does every action need a log entry?]
Integration surface: [external APIs, webhooks, export formats]
```

**Blocked until answered:**
- What is the most time-critical operation? (This gets the most direct path)
- What are the top 3 destructive operations? (These need confirmation flows)
- What does "access denied" look like for this role system?

---

## Admin-Specific Design Principles

Admin panels are internal tools. The rules are different from consumer product:

1. **Density over whitespace** — operators work in these tools all day. Information density is a feature, not a bug. Section padding can be `4rem`, not `10rem`.
2. **Efficiency over delight** — keyboard shortcuts, bulk operations, and quick filters matter more than animations and typography.
3. **Clarity over aesthetics** — labels on everything. No "icon-only" patterns in admin UI (exception: globally understood actions with always-visible tooltips).
4. **Destructive actions need friction** — not too much (one confirmation dialog) but always some.
5. **Errors must be specific** — "Failed to delete user" is not acceptable. "Failed to delete user: user has active subscriptions. Resolve billing before deletion."

---

## App Shell — Admin Variant

```
┌──────────────────────────────────────────────────┐
│ Top bar: logo · search · notifications · profile │
├──────────┬───────────────────────────────────────┤
│ Sidebar  │ Page header: title · breadcrumb · CTA │
│ (240px)  ├───────────────────────────────────────┤
│          │ Content: filters · table · pagination  │
│          │                                        │
│ fixed    │                                        │
└──────────┴────────────────────────────────────────┘
```

**Sidebar rules:**
- Section grouping: group navigation by operator workflow, not by data model
- Active state: background highlight + left border (1px solid accent)
- Collapsible to icons for more horizontal space (desktop only)
- Badge counters for pending items, alerts

**Top bar rules:**
- Global search: command-K opens full-screen search palette
- Notification bell: badge count, dropdown preview of last 5
- Profile: avatar + name + role badge

---

## Core Screens — Build in This Order

### 1. Data table (primary screen)

The dominant pattern in admin UI. Every decision here propagates everywhere.

**Column structure:**
```
[ ] checkbox | ID | Primary identifier | Secondary fields | Status | Actions
```

**Column rules:**
- Primary identifier always visible on horizontal scroll (sticky first column)
- Status column uses badge: `color + label` — never color alone
- Actions column: icon buttons visible on row hover (desktop), always visible (mobile)
- Column widths: fixed where content is predictable (ID, status, date), fluid for names/titles

**Filter and search bar:**
```
[Search input ........................] [Filter by Status ▼] [Filter by Date ▼] [Clear all] [Export]
```

**Required filter behaviors:**
- Active filters shown as removable chips
- "Clear all filters" always visible when any filter is active
- Filter state persists on page reload (URL params or localStorage)
- Search debounced at 300ms — no search-on-every-keystroke

**Bulk operations:**
```
[x] 24 selected    [Move to ▼]    [Export]    [Delete]
```
- Appears on first selection, disappears on deselect-all
- Destructive bulk operations (delete) require confirmation with count: "Delete 24 items?"
- Non-destructive operations execute immediately with undo toast

**Pagination vs. infinite scroll:**
- Admin tables: pagination (operators navigate to specific pages by number)
- Infinite scroll is for consumer feeds — never for operator tooling

**Row states:**
- Default: standard density
- Hover: subtle background shift
- Selected: checkbox checked + row tinted
- Disabled/locked: reduced opacity + cursor:not-allowed + tooltip explaining why
- Error: red left border + error icon in row

---

### 2. Detail / edit screen

**Header:**
```
← Back to [list]    [Item name / ID]    [Status badge]    [Edit]  [More ▼]
```

**Sections:**
- Primary info (top, full width): most critical fields for the operator's workflow
- Secondary info (below or in sidebar): metadata, system fields, timestamps
- Related records: tabs or sections for associated data (orders → line items, users → sessions)
- Activity log: bottom or sidebar — chronological, actor + action + timestamp

**Edit mode:**
- Inline editing preferred for single fields (click to edit)
- Form edit for multiple fields (click "Edit" → full form appears)
- Autosave for non-critical fields; explicit save for critical changes
- Dirty state: "Unsaved changes" indicator + confirm-before-leave

---

### 3. Create / form screen

**Form layout:**
- Single-column for < 6 fields
- Two-column for 6-12 fields (related fields in same row)
- Multi-step wizard for > 12 fields (group into logical phases)

**Field requirements:**
- Label always visible (never placeholder-only)
- Required fields marked with `*` + footnote "* Required"
- Field-level validation on blur (not on submit only)
- Error message: specific + actionable ("Email already in use — sign in instead")
- Disabled fields: explain why ("Auto-generated from name" as helper text)

**Save / submit:**
- Button: "Create [noun]" not "Submit" or "Save"
- Loading state: spinner + "Creating…" label + button disabled
- Success: redirect to detail page + success toast
- Error: stay on form + scroll to first error + server error above submit button

---

### 4. User / role management

**User list:** standard data table + role badge column + status (active / suspended / invited)

**Role display:**
```
Role badge: [Admin] [Editor] [Viewer] [Custom]
```
- Color-coded by permission level: red (admin) → orange (editor) → gray (viewer)
- Permission matrix (for custom roles): grid of resource × action with toggle per cell

**Invite flow:**
1. Enter email(s)
2. Select role
3. Send invite → pending badge appears in user list
4. Invitee receives email → accepts → appears as active

**Danger operations:**
- Suspend user: confirm dialog, reversible
- Delete user: confirm dialog + type username to confirm, show consequences ("User has 14 active projects")
- Transfer ownership: explicit confirmation from both parties

---

### 5. Audit log

**Columns:** timestamp · actor (name + role) · action · target (resource + ID) · IP / location · result (success / failed)

**Required:**
- Immutable: no edit or delete operations on log entries
- Searchable by actor, action, target, date range
- Exportable to CSV
- Retention period visible: "Logs retained for 90 days"

**Detail view:** click a log entry → see full payload (before/after values for edits)

---

### 6. System settings / configuration

**Architecture:**
```
Settings
├── General (site name, timezone, locale)
├── Security (password policy, 2FA requirements, session timeout)
├── Integrations (API keys, webhooks, OAuth connections)
├── Email (SMTP config, notification templates)
├── Billing (for SaaS admin of own system)
└── Danger zone (reset system, delete organization)
```

**API keys section:**
```
[Key name]  [Prefix shown: sk-***...abc]  [Created by]  [Last used]  [Scopes]  [Revoke]
                                          [+ Create new key]
```
- Full key shown only once on creation, in a copyable code block
- Revoke requires confirmation: "Revoke key ending in ...abc? This cannot be undone."

---

## Status Badge System

Define once, use everywhere. Never use color alone — always color + label.

```css
.badge-active    { background: oklch(90% 0.12 145); color: oklch(30% 0.15 145); }
.badge-pending   { background: oklch(93% 0.12 80);  color: oklch(35% 0.15 80); }
.badge-error     { background: oklch(92% 0.12 25);  color: oklch(35% 0.15 25); }
.badge-inactive  { background: oklch(92% 0 0);      color: oklch(45% 0 0); }
.badge-admin     { background: oklch(90% 0.12 25);  color: oklch(30% 0.15 25); }
```

---

## Keyboard Shortcuts (define before building)

| Shortcut | Action |
|---|---|
| `Cmd/Ctrl + K` | Global search |
| `N` | New item (on list screens) |
| `E` | Edit selected item |
| `Backspace` or `Del` | Delete selected (with confirmation) |
| `Escape` | Close modal / cancel edit |
| `/` | Focus search field |
| `?` | Open keyboard shortcut help |

Display via `?` shortcut: modal with all shortcuts organized by section.

---

## Technology Checklist

**Tables:**
- [ ] TanStack Table v8 (headless, fully typed)
- [ ] Column virtualization for > 500 rows
- [ ] Row selection via `useRowSelection`
- [ ] Column visibility toggle (operators customize their view)

**Forms:**
- [ ] React Hook Form + Zod schema validation
- [ ] Server actions for submit (React 19 / Next.js 16)
- [ ] `useFormStatus` for loading state

**Filters:**
- [ ] URL params sync (nuqs or native URLSearchParams)
- [ ] Persist filter state across navigation

**Performance:**
- [ ] Debounce search input (300ms)
- [ ] Paginate queries — never load all rows
- [ ] Optimistic updates for status toggles and quick edits

---

## Quality Gates

- [ ] Gate 1: Problem Definition (operators, workflows, critical operations)
- [ ] Gate 2: Information Architecture (all screens, navigation, access levels)
- [ ] Gate 3: Design System (tokens, consistent badge system, status colors)
- [ ] Gate 4: States (all table states, all form states, all modal states)
- [ ] Gate 5: Responsive (collapses to mobile, touch targets ≥ 44px)
- [ ] Gate 6: Accessibility (full keyboard navigation, ARIA on data grid)
- [ ] Gate 8: Frontend Readiness

Run `agents/ux-architect.md` — especially for role-based access flows.
Run `agents/frontend-handoff-reviewer.md` before development starts.
