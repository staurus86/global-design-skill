# Golden output — o02: CRM admin panel architecture

**Prompt:** "Use global-design-skill and architect an admin panel for a CRM. Include customer list, filters, bulk actions, and empty states."

---

## What a correct response must include

### 1. Problem framing before layout

Must resolve Gate 1 first: who operates this panel (role, daily volume, primary task), on what device, and the success metric (e.g., time-to-resolve a record). No layout before this.

### 2. Data table as the core surface

Must specify a `data table`, not generic cards:
- Column set with explicit priority (which columns survive at 768px)
- Row density control — `compact` / `comfortable` toggle is the expected term
- Sticky header + first column on horizontal scroll
- Reference: `patterns/admin-ui/data-tables.md` + `rules/11-data-tables.md`

### 3. Filters

Must specify a `filter` system: filter bar with applied-filter chips, clear-all, and persistence (URL params or saved views). Not a single search box.

### 4. Bulk actions

Must specify `bulk action` behavior:
- Selection model (checkbox column, shift-range select, select-all-across-pages vs current page)
- A sticky bulk action bar that appears only when rows are selected
- Destructive bulk actions (delete) spatially separated and confirmed

### 5. All states — not just the happy path

Must address every state, the `empty state` explicitly:
- **Loading:** skeleton rows (100ms–1s), not a full-page spinner
- **Empty:** reason + primary action ("No customers yet — Import or Add customer")
- **Error:** neutral tone + retry, table frame preserved
- **Bulk-selected:** count + available actions

### 6. Keyboard operability

Must specify `keyboard` support: arrow-key row navigation, `Space`/`x` to select, `/` to focus search, `Esc` to clear selection. Density and keyboard are what separate an admin panel from a marketing table.

### 7. Gate compliance

Must address Gates 1–8, with Gate 4 (states) and Gate 6 (keyboard/contrast) called out for an admin context.

---

## What a correct response must NOT include

- `background-clip: text` (gradient text — banned)
- `decorative gradient` used as a section accent (admin = density and legibility over decoration)
- Marketing-style hero or oversized whitespace in a data-dense tool
- "States TBD" or a happy-path-only table
