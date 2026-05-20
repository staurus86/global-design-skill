# Recipe — Improve Empty States

> An empty state is not a failure — it is an opportunity. The first time a user sees an empty list is the moment they have the most attention and the most motivation. A generic "No items found" wastes both. A great empty state moves the user toward value.

---

## When to use

- New users land on empty dashboards and leave without taking action
- Empty state says "No results" or "Nothing here yet"
- Users don't know what the feature is FOR from the empty state
- Error states and empty states look the same
- Cleared states show the same UI as "never had data"

---

## The Five Types of Empty States

Each type has a different purpose and requires a different design.

| Type | When it appears | Goal |
|---|---|---|
| **First-time** | User has never used this feature | Educate + convert to first action |
| **No results** | Search/filter returns nothing | Help user adjust their query |
| **Cleared** | User deleted all items | Acknowledge + offer to undo/start over |
| **Permission denied** | User lacks access | Explain + show path to getting access |
| **Error** | Data failed to load | Explain + offer retry |

---

## Type 1 — First-Time Empty State

This is the highest-value empty state. The user has zero data and is deciding whether to continue.

**The formula:**
```
Visual: preview of the populated state (not an abstract illustration)
Title:  What's missing — "[Feature name] will appear here"
Body:   Why it's valuable — one specific sentence
CTA:    Specific action — "[Verb] your first [noun]"
```

**Before (generic):**
```html
<div class="empty">
  <img src="/empty-icon.svg" alt="" />
  <p>No projects yet</p>
  <a href="/new">Create one</a>
</div>
```

**After (converts):**
```html
<div class="empty-state">
  <!-- Preview: shows what the populated state looks like -->
  <div class="empty-state__preview" aria-hidden="true">
    <!-- Blurred/dimmed preview of a real populated view -->
    <img
      src="/projects-preview.webp"
      alt=""
      class="empty-state__preview-img"
    />
    <div class="empty-state__preview-overlay"></div>
  </div>

  <div class="empty-state__content">
    <h2 class="empty-state__title">Your projects will appear here</h2>
    <p class="empty-state__body">
      Projects keep your work organized. Each project has its own
      team, deadlines, and activity feed.
    </p>
    <a href="/projects/new" class="btn-primary">
      Create your first project
    </a>
    <a href="/docs/projects" class="btn-text">Learn how projects work →</a>
  </div>
</div>
```

```css
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-8);
  padding: var(--space-16) var(--space-8);
  text-align: center;
  max-width: 480px;
  margin-inline: auto;
}

.empty-state__preview {
  position: relative;
  width: 100%;
  max-width: 420px;
  border-radius: var(--radius-xl);
  overflow: hidden;
  border: 1px solid var(--color-border);
  box-shadow: var(--shadow-md);
}

.empty-state__preview-img {
  width: 100%;
  height: 220px;
  object-fit: cover;
  object-position: top;
  /* Slightly blurred to indicate "not yet" */
  filter: blur(2px) brightness(0.9);
  transform: scale(1.02);  /* hide blur edges */
}

.empty-state__preview-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to bottom, transparent 30%, var(--color-surface) 90%);
}

.empty-state__title {
  font-size: var(--text-h3);
  font-weight: 600;
  color: var(--color-text-primary);
}

.empty-state__body {
  font-size: var(--text-body);
  color: var(--color-text-secondary);
  line-height: 1.65;
  max-width: 38ch;
}

/* Entry animation */
@starting-style {
  .empty-state {
    opacity: 0;
    transform: translateY(12px);
  }
}

.empty-state {
  transition: opacity 400ms cubic-bezier(0.16, 1, 0.3, 1),
              transform 400ms cubic-bezier(0.16, 1, 0.3, 1);
}

@media (prefers-reduced-motion: reduce) {
  .empty-state { transition: none; }
}
```

---

## Type 2 — No Results (Search / Filter)

The user is actively looking for something. Help them adjust, don't apologize.

**Before:**
```html
<p>No results found.</p>
```

**After:**
```html
<div class="empty-state empty-state--search">
  <div class="empty-state__icon" aria-hidden="true">
    <!-- Search icon with × — not a generic "empty" icon -->
    <svg>...</svg>
  </div>
  <h3 class="empty-state__title">No results for "[query]"</h3>
  <p class="empty-state__body">
    Try a different spelling, remove filters, or search by a different term.
  </p>
  <div class="empty-state__actions">
    <button class="btn-ghost" onclick="clearSearch()">Clear search</button>
    <button class="btn-ghost" onclick="clearFilters()">Remove all filters</button>
  </div>
</div>
```

**Rules for no-results state:**
- Show the actual query in the title: `No results for "priject"` (including typos)
- Suggest related terms if available
- Offer to clear the search/filters immediately
- Never show "0 results" — show a specific no-results message

---

## Type 3 — Cleared State

The user just deleted all items. This is different from never having data.

**The wrong approach:** Show the first-time empty state again. The user knows what the feature does — they just deleted their data.

**The right approach:** Acknowledge the action, offer to undo.

```html
<div class="empty-state empty-state--cleared">
  <div class="empty-state__icon" aria-hidden="true">
    <!-- Checkmark or trash icon — confirms the action -->
  </div>
  <h3 class="empty-state__title">All projects deleted</h3>
  <p class="empty-state__body">
    Your projects have been moved to the trash and will be permanently deleted in 30 days.
  </p>
  <div class="empty-state__actions">
    <a href="/trash" class="btn-ghost">View trash</a>
    <a href="/projects/new" class="btn-primary">Start a new project</a>
  </div>
</div>
```

---

## Type 4 — Permission Denied

The user doesn't have access. Never show "No items" when the real reason is access control.

```html
<div class="empty-state empty-state--locked">
  <div class="empty-state__icon" aria-hidden="true">
    <!-- Lock icon — clearly communicates the reason -->
  </div>
  <h3 class="empty-state__title">You need access to view Analytics</h3>
  <p class="empty-state__body">
    Analytics is available on the Pro plan and above. Ask your workspace
    admin to upgrade, or upgrade your plan directly.
  </p>
  <div class="empty-state__actions">
    <a href="/settings/billing" class="btn-primary">View upgrade options</a>
    <button class="btn-ghost" onclick="requestAccess()">Request access from admin</button>
  </div>
</div>
```

---

## Type 5 — Error / Failed to Load

Not an empty state — a failure state. Treat it differently.

```html
<div class="empty-state empty-state--error">
  <div class="empty-state__icon empty-state__icon--error" aria-hidden="true">
    <!-- Warning triangle or broken connection icon -->
  </div>
  <h3 class="empty-state__title">Couldn't load your projects</h3>
  <p class="empty-state__body">
    We had trouble connecting to our servers. Your data is safe —
    this is a temporary issue.
  </p>
  <div class="empty-state__actions">
    <button class="btn-primary" onclick="retryLoad()">Try again</button>
    <a href="/status" class="btn-ghost">Check system status ↗</a>
  </div>
</div>
```

---

## Compact Empty State (inline, within a card)

For panels and sections where a full-page empty state would be too large.

```html
<div class="empty-compact">
  <p class="empty-compact__text">No activity yet</p>
  <a href="/invite" class="btn-text btn-sm">Invite teammates →</a>
</div>
```

```css
.empty-compact {
  padding: var(--space-10) var(--space-6);
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-3);
}

.empty-compact__text {
  font-size: 0.9375rem;
  color: var(--color-text-muted);
}
```

---

## Copy Tone Rules

| Tone | Example | Use when |
|---|---|---|
| **Neutral, factual** | "No projects yet. Create one to get started." | Standard first-time state |
| **Helpful, directive** | "No results for 'priject'. Try checking your spelling." | No-results state |
| **Acknowledging** | "All notifications cleared. You're up to date." | Cleared state |
| **Never apologetic** | ~~"Sorry, nothing to show here."~~ | Never |
| **Never cute** | ~~"Wow, so empty! Much nothing here!"~~ | Never |
| **Never accusatory** | ~~"You haven't done anything yet."~~ | Never |

---

## Animation for Empty States

Empty states benefit from a subtle float or entrance animation — they signal that the UI is "alive" even without data.

```css
/* Subtle float on the illustration */
@keyframes idle-float {
  0%, 100% { transform: translateY(0); }
  50%       { transform: translateY(-8px); }
}

.empty-state__icon {
  animation: idle-float 4s ease-in-out infinite;
}

@media (prefers-reduced-motion: reduce) {
  .empty-state__icon { animation: none; }
}
```

---

## Before / After Summary

| Before | After |
|---|---|
| "No items found" | "No results for '[query]' — clear search" |
| Generic empty icon (same for all states) | Type-specific visual (preview / search / lock / error) |
| No CTA, or "Create" with no context | Specific: "Create your first project" |
| Same state for first-time and cleared | Different designs for different contexts |
| Permission denied shows "No items" | Explicit: "You need access to [Feature]" |
| Apologetic copy | Direct, helpful, neutral |

---

## Acceptance Criteria

```
[ ] First-time state: preview image + specific title + outcome body + specific CTA
[ ] No-results state: shows actual query in title + offers clear/adjust actions
[ ] Cleared state: acknowledges action + offers recovery path
[ ] Permission state: names the feature + explains requirement + path to access
[ ] Error state: "safe data" reassurance + retry action + status page link
[ ] No apologetic copy ("sorry", "unfortunately", "oops")
[ ] No generic icons (all icons reflect the specific state type)
[ ] CTA label follows: Verb + specific noun (not "Get Started", "Create", "Add")
[ ] Animation present + prefers-reduced-motion respected
[ ] Screen reader: title and body announced correctly
```

---

*Recipe version: global-design-skill v1.0 — `recipes/improve-empty-states.md`*
*Related: `patterns/product-ui/empty-states.md`, `patterns/product-ui/error-states.md`, `rules/13-saas-products.md`*
