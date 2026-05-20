# Reference — SaaS UI Examples

> Annotated examples of SaaS product UI patterns worth studying. Each entry explains what specifically to learn, not just who to look at. Used by `agents/reference-hunter.md` for Capability 1 (block category search) and Capability 3 (competitive analysis).

---

## Command Palette

The command palette is the highest-ROI UX pattern in modern SaaS. Study these before building one.

| Product | URL | What to learn |
|---|---|---|
| **Linear** | linear.app — press `⌘K` | The canonical implementation. Note: fuzzy search that tolerates typos; grouping by category (Recent / Actions / Pages); keyboard-first sub-menus; smooth 120ms entry animation with `@starting-style` |
| **Raycast** | raycast.com — product demo | Extension system inside command palette; how to surface third-party commands without visual chaos; the "AI mode" entry that doesn't break the keyboard pattern |
| **GitHub** | github.com — press `/` or `⌘K` | How to integrate command palette into an existing complex product; deep-link support (navigate to PR, file, repo from anywhere) |
| **Vercel** | vercel.com/dashboard — press `⌘K` | Deployment-context awareness — the palette shows different options based on current project; how context changes command scope |
| **Figma** | figma.com — press `⌘/` | Plugin commands + design commands in one palette; how to handle 1000+ commands without overwhelming the list |

**What the best implementations share:**
- Maximum 8–10 visible items before scrolling
- Sub-50ms response to keystroke input
- Recent/frequent items at top without user configuration
- Keyboard navigation with visual focus indicator
- `Escape` closes and returns focus to previous element (never loses context)

---

## Empty States

Empty states are the most-ignored pattern in SaaS. The best products treat them as onboarding moments.

| Product | Empty state location | What to learn |
|---|---|---|
| **Linear** | New workspace, no issues | Preview illustration → value statement → "Create your first issue" CTA. The illustration is a soft wireframe of what the populated state looks like — teaches the user what to expect. |
| **Notion** | New page, no content | Minimal — just a blinking cursor and "Press Enter to continue, or `/` for commands". The absence of illustration communicates editor-first. |
| **GitHub** | Empty repository | Code snippet showing first commit commands. Empty state AS onboarding instruction — the most contextually useful approach. |
| **Loom** | No recordings | Video product's empty state uses a video (of course). Short looping product demo. The empty state demonstrates the product. |
| **PostHog** | No events yet | Step-by-step instrumentation guide with code snippets. Empty state as technical documentation. |
| **Figma** | New team, no files | Vertical centered layout: illustration + "Your team's files will appear here" + "Create new file" + subtle import hint. |

**Pattern analysis:**
- Software that replaces a workflow: show the empty state of that workflow (GitHub's git commands)
- Productivity tools: show the first action (Notion's slash command)
- Visual/media tools: show a demo of the output (Loom's looping demo)
- Analytics tools: show the setup instructions (PostHog's SDK guide)

---

## Settings Pages

Settings pages reveal product architecture. Study them to understand information hierarchy in complex SaaS.

| Product | URL | What to learn |
|---|---|---|
| **Linear** | app.linear.app/settings | Vertical tab nav, two-column layout (label left / control right), toggle rows for preferences, danger zone isolated at bottom of sidebar |
| **Vercel** | vercel.com/[team]/settings | Nested settings (team → project → domain), breadcrumb navigation for context, environment variable UI (reveal/copy/delete pattern), danger zone with confirmation input |
| **GitHub** | github.com/settings | The most complex settings in the industry — how to organize 40+ categories. Sub-navigation grouping (Access / Code and automation / Integrations). Note how they handle settings that require re-authentication. |
| **Stripe** | dashboard.stripe.com/settings | Financial product settings — two-level sidebar (Payments / Billing / Team / Developers). How to handle settings that have immediate business consequences (webhook deletion, etc.) |
| **Notion** | notion.so/settings | Workspace + account split, team management, billing — all in one modal. How to make a complex settings tree navigable in a modal context. |
| **Raycast** | Raycast app settings | Desktop app settings — different constraints than web. Keyboard shortcuts manager, extension permissions, preferences per extension. |

**Settings IA patterns:**
1. **Flat list** (GitHub style): alphabetical/thematic, searchable — works at 20+ categories
2. **Grouped sidebar** (Linear style): 4–8 top-level groups, each with 3–6 items — works at 10–30 settings
3. **Modal tabs** (Notion style): 3–7 tabs, single scrollable panel — works at <20 settings

---

## Onboarding Flows

The best onboarding flows treat first-run as a product moment, not a form to complete.

| Product | Flow type | What to learn |
|---|---|---|
| **Linear** | Setup wizard → sample workspace | Creates a sample workspace populated with real data so users see value before entering any data. "Aha moment first" philosophy. |
| **Loom** | Extension install → record immediately | Reduces time-to-first-recording to under 2 minutes. Onboarding IS the first use case. No separate wizard. |
| **Notion** | Template selection → populated workspace | Template selector as onboarding — user picks their use case, workspace populates accordingly. Personalized empty state. |
| **Superhuman** | 1:1 onboarding call | Concierge model for premium products — 30-minute call to set up. Inverts the usual self-serve assumption. |
| **Figma** | Tutorial file → parallel real work | Puts users in a real file immediately. Tutorial overlays on the actual product. Learning while doing. |
| **Stripe** | Guided checklist → test payment | Developer onboarding that ends with a test charge. Proof the integration works = aha moment. |

**Onboarding patterns by product type:**
- **Productivity/workspace tools** (Linear, Notion): Create a populated sample state
- **Communication/recording** (Loom, Slack): Make the first use happen immediately
- **Developer/API tools** (Stripe, Supabase): First successful API call/integration IS the aha moment
- **Premium consumer** (Superhuman): Concierge for products where setup complexity = churned users

---

## Loading States

Loading states are the easiest way to make a product feel faster than it is.

| Product | Loading pattern | What to learn |
|---|---|---|
| **Linear** | Instant optimistic UI | Most actions complete instantly on the client before the server responds. `useOptimistic` (React 19). Error recovery is handled silently via background sync. |
| **GitHub** | Skeleton for code content | Skeleton shapes that match the content being loaded — file tree skeleton mirrors file tree structure. Not a generic spinner. |
| **Vercel** | Deployment progress bar | Linear progress with estimated time remaining. Status transitions: Queued → Building → Deploying → Live. Each state has a specific color. |
| **Stripe Dashboard** | Instant table with stale data | Shows previous data while fetching new — no blank state during reload. Subtle refresh indicator in the corner. |
| **Notion** | Progressive document load | Text renders immediately, images load progressively with aspect-ratio placeholders. No CLS as images load. |
| **PostHog** | Chart skeleton that matches shape | Bar chart skeleton mirrors bar chart dimensions — same number of bars, correct proportions. Transition to real data feels like a fill-in rather than a swap. |

**Loading state decision matrix:**

| Duration | Best pattern | Never do |
|---|---|---|
| < 100ms | No loading state at all | Spinner (perceived as slower) |
| 100ms–1s | Skeleton (shape-matched) | Spinner on full page |
| 1–3s | Progress indicator + cancel option | Blocking spinner |
| > 3s | Progress indicator + background + notification on complete | Forcing user to wait |

---

## Error States

Error messages are user-research data. The best products write errors that explain exactly what happened and exactly what to do.

| Product | Error type | What to learn |
|---|---|---|
| **Stripe** | Form validation | Error message includes: what field failed + why + example of correct format. "Card number is invalid — make sure it's 16 digits with no spaces" not "Invalid card number". |
| **GitHub** | Permission errors | Explains why access is denied AND who to contact for access. Error = situation + reason + next step. |
| **Linear** | Sync conflicts | Optimistic update that failed is rolled back with a toast: "Couldn't update [issue title] — tap to retry". User never loses their intent. |
| **Vercel** | Build failures | Shows exact build log, highlights the failing line, links to documentation for common errors. Error = full context. |
| **Supabase** | SQL errors | Shows PostgreSQL error code + human-readable explanation + link to Postgres docs. Doesn't hide the technical detail — developers need it. |
| **Clerk** | Auth errors | Different messages per auth state: "No account found" vs "Wrong password" vs "Account locked" vs "Unverified email" — each error is specific, each has a specific fix. |

**Error message formula (from `patterns/product-ui/error-states.md`):**
```
[What failed] — [Why it failed] — [How to fix it]
```
- Never: "Error" or "Something went wrong"
- Never: "Invalid" with no context
- Always: Specific, actionable, non-blaming

---

## Modals and Dialogs

Over 90% of modals in production SaaS are unnecessary. Study the ones that are necessary.

| Product | Modal use case | What to learn |
|---|---|---|
| **Linear** | Delete issue confirmation | Two-step: first click shows modal; modal requires typing "DELETE" for destructive operations. The friction is the feature. |
| **GitHub** | Repository deletion | Types the repository name. Extreme friction for extreme consequence. Modal communicates the severity through its own design. |
| **Stripe** | Webhook creation | Long form in a modal. Study how they handle form validation inside a modal — errors stay within the modal; modal doesn't close on error. |
| **Vercel** | Environment variable | Inline modal in the table row — not a full-page navigation. The context stays visible. |
| **Figma** | Share dialog | Complex modal (permissions, link settings, copy link) that doesn't use a multi-step wizard — all options visible at once because they're related decisions. |
| **Notion** | Page move | Tree navigation inside modal — how to make a nested picker usable in a constrained space. Search within the picker. |

**When to use a modal (strict criteria):**
1. Action requires immediate attention and shouldn't navigate away
2. Action is reversible OR requires explicit confirmation before being irreversible
3. Context behind the modal is needed to complete the action

**Never use a modal for:** information only (use a tooltip), complex forms with many steps (use a page), primary navigation.

---

## Notification Systems

The difference between helpful notifications and notification spam is specificity.

| Product | Notification approach | What to learn |
|---|---|---|
| **Linear** | Toast + persistent inbox | Toasts for immediate feedback (issue updated, comment added); persistent notification center for things that happened while you were away. Two channels, two purposes. |
| **Slack** | Notification threading | Notifications grouped by workspace → channel → thread. Badge counts are meaningful (unread) not decorative. |
| **GitHub** | Email + web + API | Granular notification subscriptions — per-repository, per-thread. User controls the volume. |
| **Vercel** | Deployment webhooks | Notifications as an API — push to Slack, Discord, or any endpoint. The notification system is the integration system. |
| **Stripe** | Webhook events | Event-driven notifications — every state change is a webhook. The dashboard notification is secondary to the API. |

**Toast message formula:**
- Success: "[Action] completed" — 3 seconds, auto-dismiss
- Error: "[Action] failed — [reason]" — persistent until dismissed, with Retry action
- Warning: "[Action] may affect [consequence]" — 8 seconds, with action to learn more
- Info: "[Event] happened" — 5 seconds, dismissible

---

## Table and Data Displays

Data-heavy SaaS products live or die by their table design.

| Product | Table approach | What to learn |
|---|---|---|
| **Linear** | Compact rows, groupable | 32px row height (compact mode), 40px (comfortable). Groupable by status, assignee, project. Keyboard shortcuts for bulk operations. No visible row borders — hover background only. |
| **PlanetScale** | Schema browser | Tables that display relational data (columns, indexes, foreign keys) with expandable detail rows. How to show database structure in a web table. |
| **Retool** | Configurable density | Table columns are drag-reorderable, resizable, hideable. Density switcher (compact / default / comfortable). Filter builder. This is the "table as a product" approach. |
| **Stripe Dashboard** | Filterable transaction table | Full-width table with live filter bar. Each row is clickable to detail view. Pagination with explicit "per page" control. Revenue numbers right-aligned. |
| **GitHub** | Issues/PR list | Tags, assignees, milestones as inline chips within the row. Status indicator as colored dot. Bulk select via checkbox column. |
| **Airtable** | Spreadsheet-style | The most feature-complete table on the web. Column types, formula cells, linked records. Reference for: what's possible if you treat the table as a primary interface. |

**Table design checklist:**
- Numbers: right-aligned
- Text: left-aligned
- Status: icon + label (never icon alone)
- Dates: relative for recent (3 days ago), absolute for older (Mar 12, 2025)
- Currency: consistent decimal places within a column
- Row actions: appear on hover in final column (not a separate action column)

---

*Reference version: global-design-skill v1.0 — `references/saas-ui-examples.md`*  
*Updated: 2026-05-20*  
*Related: `agents/reference-hunter.md`, `references/inspiration-sites.md`, `patterns/product-ui/`*
