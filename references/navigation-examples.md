# Reference — Navigation Pattern Examples

> Real-world navigation implementations worth studying. Each entry explains the decision logic, not just the visual appearance. Use before designing any navigation system.

---

## Sidebar Navigation

The sidebar is the dominant navigation pattern for SaaS applications. Study these before building any app shell.

### Linear — linear.app

**Pattern:** Full sidebar + collapsed sidebar + command palette fallback  
**What to study:**

- **Sidebar as workspace map.** The sidebar in Linear isn't just navigation — it's the workspace state (active cycle, project health indicators, unread count). Navigation and information are fused.
- **Collapse to icons gracefully.** At narrow viewports or when user collapses, icons replace labels. Each icon is distinct enough to work without a label — they chose icons before labels, not after.
- **Keyboard shortcut layer.** Every sidebar item has a keyboard shortcut. The sidebar isn't the primary navigation tool — `⌘K` is. The sidebar is for orientation.
- **Active state precision.** The active item has: background highlight + accent color text + font-weight bump. Three signals simultaneously. Never ambiguous which item is active.
- **No icon-only by default.** The sidebar starts expanded. Collapsing is a user choice, not a design decision to save space.

**CSS pattern used:**
```css
.sidebar-item--active {
  background: var(--color-accent-subtle);
  color: var(--color-accent-text);
  font-weight: var(--font-weight-semibold);
}
```

---

### Vercel — vercel.com/dashboard

**Pattern:** Top navigation (marketing) → Left sidebar (dashboard) + breadcrumb  
**What to study:**

- **Navigation mode switch.** Marketing site uses top nav. Dashboard uses left sidebar. The transition is handled by re-routing to `/dashboard` — the navigation system itself signals "you're now in the product."
- **Breadcrumb = second navigation layer.** `/[team]/[project]/[deployment]` — the breadcrumb isn't just a URL path, it's the navigation depth indicator. Each segment is clickable back.
- **Project switcher in sidebar.** Workspace/team context switcher at the top of the sidebar, separate from the main navigation. Context → navigation, in that order.
- **Settings as bottom-pinned item.** Settings, help, and account items are pinned to the bottom of the sidebar. Content navigation at top, utility navigation at bottom.

---

### Stripe Dashboard — stripe.com/dashboard

**Pattern:** Left sidebar with groups, no collapse on desktop  
**What to study:**

- **Navigation groups by product area, not by user role.** "Payments" / "Billing" / "Connect" / "Radar" / "Atlas" — each group is a Stripe product. Users who don't use a product ignore those sections.
- **Badge counts for actionable items.** Unresolved disputes show a count badge. Pending payouts show a count. Badges only for items requiring action — not for informational counts.
- **Settings isolated from main nav.** A gear icon at the bottom — separate from the main navigation. Never mixed with navigation to feature areas.
- **Sub-navigation within sections.** Click "Payments" → the main area shows "Overview / Transactions / Payouts" as tabs within the content area, not as sub-items in the sidebar. This keeps the sidebar shallow.

---

### Notion — notion.so

**Pattern:** Collapsible tree sidebar with infinite nesting  
**What to study:**

- **Pages as navigation items.** In Notion, navigation IS content. The sidebar lists pages, and pages can contain other pages. The navigation is the IA, not a map to the IA.
- **Collapse/expand state persists.** Which sections are expanded is stored per-user. Notion remembers that you always have "Work" expanded and "Archive" collapsed.
- **Drag to reorder.** Sidebar items are drag-and-drop reorderable. The navigation is user-configurable, not developer-defined. Study this for: collaborative tools where users own their IA.
- **Emoji as visual anchor.** Each page has an optional emoji that appears in the sidebar. This visual anchoring makes navigation faster — users scan for the emoji, not the text.
- **"Add a page" at bottom.** Creating new content via the sidebar itself. Navigation is also a creation point.

---

## Top Navigation

### Webflow — webflow.com

**Pattern:** Sticky top nav, mega-menu on hover, transparent over hero  
**What to study:**

- **Mega-menu with categories, not lists.** "Product" hover shows: Build / CMS / Interactions / SEO — each with 3–4 sub-items + a featured customer story. Dense but organized.
- **Transparent to solid scroll transition.** The nav starts transparent over the hero image (CSS `backdrop-filter` on scroll), transitions to solid `var(--color-surface)` once hero scrolls out. Smooth, not jarring.
- **CTA isolated from navigation items.** "Get started" is a filled button in the top right. It's clearly a CTA, not a navigation item. The distinction between navigation (where to go) and conversion (what to do) is visually explicit.
- **Mobile hamburger → full-screen drawer.** On mobile, the hamburger opens a full-screen navigation overlay. All items visible, with the same mega-menu structure but vertically laid out.

---

### Stripe — stripe.com

**Pattern:** Clean 5-item horizontal nav, no mega-menu  
**What to study:**

- **IA simplicity as trust signal.** 5 items: Products / Solutions / Developers / Resources / Pricing. The simplicity communicates organizational clarity. A company that can organize its entire product in 5 nav items understands its own IA.
- **Dropdown on hover, immediate close on mouse-leave.** Stripe's dropdowns appear with a subtle fade (100ms). They close immediately when the mouse leaves — no sticky dropdown that covers content while you try to scroll.
- **"Sign in" vs "Contact sales" as separate CTAs.** Two clearly different user intentions: existing customer (sign in) vs. new prospect (contact sales). Both are in the nav but visually distinct.

---

### Arc Browser — arc.net

**Pattern:** Minimal 3-item nav + scroll-reactive behavior  
**What to study:**

- **Navigation as story chapter markers.** The 3 nav items correspond to the 3 sections of the page (Download / What's Arc / Community). Clicking navigates to that section. The nav IS a table of contents.
- **Sticky nav appears on scroll.** Not visible on page load — only appears after the hero scrolls out. This gives the hero full real estate, then provides navigation once the user has decided to explore.
- **Personality in the nav.** The active item gets a slight emoji or visual signal. Even the navigation has the brand's personality.

---

## Mobile Navigation

### Bottom Tab Bar — most common for mobile apps

The best examples to study:

| App | What to study |
|---|---|
| **Linear (mobile)** | 4 tabs: Inbox / Issues / Projects / You. Icons with labels. Active tab has filled icon + accent color. Badge count on Inbox for unread. |
| **GitHub Mobile** | 5 tabs: Home / Notifications / Explore / Profile + compose FAB. Notification badge on the Notifications tab. Study for: balancing primary navigation (tabs) with primary action (FAB). |
| **Superhuman** | Bottom navigation blends with keyboard. When keyboard is open, the bottom nav slides up with it — no overlap. Study for: email/text entry products where the keyboard is always fighting with navigation. |
| **Notion Mobile** | Bottom sheet navigation pattern. Tab bar at bottom reveals a bottom sheet for nested navigation. More complexity accessible without drilling into deep navigation. |

**Bottom tab bar rules:**
- 3–5 items only. 6+ means something is wrong with the IA.
- Always label tabs — icon-only tabs fail usability testing consistently.
- Active state: filled icon + accent color on icon + accent color on label.
- Notification badges on the badge layer, not within the tab label.

---

### Hamburger → Drawer Pattern

The best mobile header + drawer implementations:

| Site | What to study |
|---|---|
| **Webflow** | Hamburger transitions to X (CSS transform: rotate). Drawer fills 100dvh (not 100vh). Background has slight blur overlay. All items accessible, no secondary nav needed. |
| **Vercel** | On mobile, the full sidebar navigation becomes a slide-in drawer. The desktop sidebar IA is preserved — mobile users get the same navigation depth, just different presentation. |
| **Tailwind CSS** | Minimalist: hamburger → full-width overlay. Single column, large touch targets (min 44px). No nested navigation on mobile — if it's complex enough to nest, reconsider the IA. |

**Drawer animation pattern:**
```css
/* Desktop sidebar → mobile drawer with @starting-style */
@media (max-width: 768px) {
  .nav-drawer {
    position: fixed;
    inset: 0;
    transform: translateX(-100%);
    transition: transform 300ms var(--ease-smooth);
    display: block; /* Always block — control with transform */
  }

  .nav-drawer[data-open="true"] {
    transform: translateX(0);
  }
}
```

---

## Breadcrumbs

### GitHub — github.com

**Pattern:** `owner / repo / tree / branch / path/to/file`  
**What to study:**

- **Breadcrumb encodes full path.** Every segment is clickable and represents a real navigation destination. Users can jump to any level.
- **Truncation for long paths.** When the path is too deep, middle segments collapse with `...` which expands on click. Study for: deep directory navigation in file-system-style UIs.
- **Repository name is visually stronger.** The repo name has slightly heavier weight — it's the most important context anchor.

---

### Vercel — vercel.com/[team]/[project]/...

**Pattern:** Team / Project / [Section]  
**What to study:**

- **Context breadcrumbs, not content breadcrumbs.** Vercel's breadcrumb shows your current workspace context (which team, which project), not navigation history. It answers "where am I" not "how did I get here."
- **Separator as visual weight.** The `/` separator is `text-muted` — lighter than the breadcrumb labels. The separator should never compete visually with the navigation items it separates.

---

## Navigation Anti-Patterns

Avoid these in production:

| Anti-pattern | Why it fails | Fix |
|---|---|---|
| More than 7 top-level nav items | Hick's Law — decision time increases with options | Group into 5–7 categories, use mega-menus for depth |
| Navigation item labels that match page H1 verbatim | Users want to know where they're GOING, not where they ARE | Use destination-oriented labels ("Analytics" not "Analytics Dashboard") |
| Active state with color alone | Colorblind users miss it | Always combine: color + weight + background |
| Deep dropdown nesting (3+ levels) | Mouse target gets too small, mobile breaks | Max 2 levels. If 3 are needed, the IA is wrong. |
| Navigation as breadcrumb (showing current page only) | Users lose orientation when depth > 2 | Show full path for content deeper than 2 levels |
| Hamburger without a label | "Menu" or "Navigation" label increases tap rate 20% | Label the hamburger on desktop |
| Fixed nav that covers content | Navigation obscures content user is trying to read | Use `scroll-padding-top` or reduce nav height |

---

*Reference version: global-design-skill v1.0 — `references/navigation-examples.md`*  
*Updated: 2026-05-20*  
*Related: `agents/reference-hunter.md`, `references/inspiration-sites.md`, `patterns/navigation/`*
