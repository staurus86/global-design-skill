# Rule 12 — Admin Panels

> Admin panels are operator tools. Efficiency, clarity, and correctness take priority over aesthetics. Every design decision must be justified by operator workflow, not visual preference.

---

## The Admin Design Shift

Admin UI operates under different constraints than consumer product:

| Consumer product | Admin panel |
|---|---|
| Delight is a feature | Efficiency is the feature |
| Aesthetic = trust signal | Clarity = trust signal |
| Whitespace creates breathing room | Density reduces time-on-task |
| User is a visitor | User is a professional with repetitive workflows |
| Error is rare | Error handling is the main design challenge |

**Implication:** Every consumer design pattern (generous whitespace, minimal text, visual hierarchy through large imagery) must be re-evaluated for admin context. Most will fail.

---

## Rules

### R1 — Information density is intentional

Admin operators work in these tools all day. Showing less information per screen means more time per task. More information per screen means faster workflows — up to the cognitive limit.

**Target density:** Medium-high. Show 3-5 data points per row. Show 20-25 rows per page.

**Banned:** Landing-page-style sections in admin UI. `10rem` padding blocks. One stat per card with large whitespace. Full-page illustrations for empty states.

**Admin-appropriate:** `2-4rem` section padding. Compact table rows (36-40px). Dense sidebar navigation. Multiple data points per row.

---

### R2 — Labels on everything

Admin operators encounter edge cases daily. Missing labels create ambiguity that causes errors.

**Rules:**
- Every icon-only button requires a tooltip with the action name
- Every table column has a visible header
- Every status badge has a text label (not color alone)
- Every numeric value has a unit (%, $, ms, px, items)
- Every timestamp has a timezone (or "your local time" if localized)

**Exception:** Globally unambiguous icons (trash, pencil, ×) in a sequence of identical rows may be icon-only if: touch target is ≥ 44px, tooltip appears on hover with 300ms delay, and screen reader gets the accessible label.

---

### R3 — Data table is the primary component

Most admin panels are 70% data tables. The table must be the most refined component.

**Anatomy:**
```
[ Column header (sortable) ]
  [ Row: checkbox | ID | primary field | secondary fields | status | actions ]
  [ Row (selected): highlighted + bulk action bar appears ]
  [ Row (hover): actions visible ]
  [ Row (error): red left border + error icon ]
[ Pagination: prev | 1 2 3 ... 47 | next ]  [Rows per page: 25 ▼]
```

**Sorting:** Click header to sort ascending. Click again: descending. Click again: unsorted. Show arrow indicator (↑ / ↓) only on active sort column.

**Column resize:** Optional but high-value for operators. `grid-template-columns` with draggable handle.

**Column visibility:** Let operators hide columns they don't need. Preferences persist to localStorage or user settings.

**Pagination:** Use page-number pagination (not infinite scroll). Operators navigate to specific page numbers. Show total count: "Showing 201–225 of 4,832 results".

---

### R4 — Filter and search are mandatory at scale

For any table with > 20 expected rows, filter and search must exist on first release.

**Filter bar:**
```
[Search ....................] [Status ▼] [Created ▼] [Assigned ▼] [Export] [+ Add filter]
                             [Active chip ×] [Last 30 days ×] [Clear all filters]
```

**Requirements:**
- Search: debounced 300ms, not on-every-keystroke, not on-submit-only
- Active filters: shown as removable chips
- Clear all: always visible when any filter is active
- Filter state: URL params (shareable, refreshable) or session storage (persists nav)
- Export: always filters the current filtered set, not all data

---

### R5 — Bulk operations reduce repetition

If an operator needs to perform the same action on 5+ items, bulk operation is required.

**Pattern:**
```
When ≥ 1 row selected: bulk action bar slides down from table header
[N items selected]  [Archive ▼]  [Export]  [Delete]  [Deselect all]
```

**Rules:**
- Destructive bulk operations require confirmation with the count: "Delete 24 items? This cannot be undone."
- Non-destructive bulk operations execute immediately with undo toast (5s window)
- "Select all on this page" + "Select all [total count]" are separate actions for large datasets

---

### R6 — Destructive operations require explicit friction

Operations that are irreversible must have friction proportional to their impact.

**Friction levels:**

| Operation | Friction level | Pattern |
|---|---|---|
| Archive (reversible) | None | Execute + undo toast |
| Bulk delete (< 10) | Low | Confirmation dialog with count |
| Delete single item | Low | Confirmation dialog: "Delete [name]?" |
| Delete with consequences | Medium | Dialog shows consequences: "User has 14 active orders" |
| Delete account/organization | High | Type the name to confirm |
| Revoke access / API key | Medium | Confirmation + show who/what loses access |

**Confirmation dialog structure:**
```
Title:  Delete [item name]?
Body:   [Specific consequence — not "are you sure?"]
        "This will permanently delete the workspace and remove
         access for 12 members. Orders in progress will be cancelled."
Buttons: [Cancel]  [Delete workspace]  ← destructive verb, not "OK" or "Confirm"
```

---

### R7 — Access control must be visible

Operators need to understand why they can or cannot do something.

**Visibility rules:**
- Restricted actions: visible but disabled, with tooltip explaining the permission required
- Hidden actions: only when the existence of the feature itself is sensitive (rare)
- Role indicator: user's role visible in the navigation or top bar
- Permission denied page: show what permission is needed and who to contact

**Never:** Silently do nothing when a permission check fails. Always show a clear message.

---

### R8 — Error messages are specific

Admin errors are not consumer errors. Operators need to act on errors, not just understand them.

**Formula:** `[What failed] + [Why it failed] + [How to fix it]`

| Bad | Good |
|---|---|
| "Error" | "Failed to delete user: User has 3 active subscriptions. Cancel subscriptions first." |
| "Action failed" | "Export failed: The selected date range exceeds 90 days. Select a shorter range." |
| "Invalid input" | "API key name must be unique. 'Production' already exists — choose a different name." |
| "Something went wrong" | "Server error (500). Our team has been notified. Try again in a few minutes." |

---

### R9 — Audit trail for critical operations

Any operation that changes data should be logged. The log is a feature, not an afterthought.

**Minimum log entry:**
```
[Timestamp]  [Actor: name + role]  [Action]  [Target: resource type + ID/name]  [Result]
2026-05-20 14:32 UTC  Sarah K. (Admin)  Deleted  User: john@example.com (ID: 8821)  Success
```

**Log screen requirements:**
- Sortable by timestamp (default: newest first)
- Filterable by actor, action type, date range
- Exportable (CSV minimum)
- Immutable (no edit or delete of log entries)
- Click-through to the affected resource (if it still exists)

---

### R10 — Keyboard-first for power operators

Admin operators are power users. Keyboard shortcuts reduce friction for repetitive workflows.

**Minimum keyboard support:**
- `Cmd/Ctrl + K`: global command palette / search
- `N`: new item (on list screens)
- `E`: edit selected item (on detail screens)
- `/`: focus search input
- `Escape`: close modal / cancel edit / clear selection
- `?`: open keyboard shortcut help

**Command palette pattern:**
```
[Cmd+K] → opens full-screen overlay
[Search: ........................]
Recent: [recent actions]
Commands: [contextual actions for current screen]
Navigation: [go to page X]
```

---

### R11 — Status system is non-negotiable

A consistent status vocabulary across the entire admin panel.

**Define once:**
```
Active    → green
Pending   → amber
Inactive  → gray
Error     → red
Draft     → blue or gray
Suspended → red (distinct from Error: intentional, not failure)
```

**Application:** Every status badge, every table row coloring, every notification color — all map to this vocabulary. No one-off colors for one-off statuses.

---

## Admin Panel Checklist

```
[ ] Information density: medium-high (2-4rem section padding, not 10rem)
[ ] All icon-only buttons have tooltips with action name
[ ] Status badges: color + text label (never color alone)
[ ] Data table: sorting, filtering, column visibility, pagination
[ ] Filters: active filter chips, clear all, URL state
[ ] Bulk operations: for any repetitive multi-item action
[ ] Destructive operations: friction level matches consequence
[ ] Error messages: [what] + [why] + [how to fix]
[ ] Audit log: timestamp + actor + action + target + result
[ ] Keyboard shortcuts defined and documented
[ ] Status vocabulary: consistent colors across all screens
```

## Related Files

- `blueprints/admin-panel-from-scratch.md` — full build protocol
- `rules/11-tables-and-data-ui.md` — data table deep rules
- `patterns/admin-ui/data-tables.md` — table implementation patterns
- `patterns/admin-ui/filters.md` — filter UI patterns
- `checklists/admin-panel-review.md` — admin review checklist
