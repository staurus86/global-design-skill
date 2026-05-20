# Pattern — Empty States

> An empty state is the first product experience for new users. It is not a blank screen. It is a conversion moment: from new user to activated user.

---

## Three Types of Empty States

| Type | Trigger | Goal |
|---|---|---|
| **First-time** | User has never created any content | Drive to first creation action |
| **Cleared** | User deleted all content, or filters removed all results | Restore or reframe |
| **No results** | Search or filter returns nothing | Adjust or clear filter |

Each type has different copy and different design. Never use the same empty state for all three.

---

## Pattern A — First-Time Empty State

The most important empty state. Sets expectations and drives activation.

```html
<div class="empty-state" role="region" aria-label="No projects yet">
  <!-- Visual: show what the populated state looks like -->
  <div class="empty-state__visual">
    <img
      src="/empty-projects-preview.webp"
      alt="Preview of what your project dashboard looks like with data"
      width="480"
      height="300"
      class="empty-state__preview"
    />
  </div>

  <div class="empty-state__content">
    <h2 class="empty-state__title">No projects yet</h2>
    <p class="empty-state__desc">
      Projects organize your designs, specs, and team feedback in one place.
      Create your first one to get started.
    </p>
    <a href="/projects/new" class="btn-primary">
      Create your first project
    </a>
    <a href="/docs/projects" class="empty-state__learn">
      Learn how projects work →
    </a>
  </div>
</div>
```

```css
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: clamp(3rem, 8vw, 6rem) var(--space-6);
  max-width: 560px;
  margin-inline: auto;
}

.empty-state__preview {
  width: 100%;
  max-width: 480px;
  height: auto;
  border-radius: var(--radius-xl);
  border: 1px solid var(--color-border);
  box-shadow: 0 8px 32px oklch(0% 0 0 / 0.15);
  margin-bottom: var(--space-8);
}

.empty-state__title {
  font-size: clamp(1.25rem, 2vw, 1.5rem);
  margin-bottom: var(--space-3);
}

.empty-state__desc {
  color: var(--color-text-secondary);
  line-height: 1.65;
  max-width: 44ch;
  margin-bottom: var(--space-6);
}

.empty-state__learn {
  display: block;
  margin-top: var(--space-4);
  font-size: 0.875rem;
  color: var(--color-text-muted);
  text-decoration: none;
}

.empty-state__learn:hover { color: var(--color-accent); }
```

---

## Pattern B — Illustration Empty State

For products where a screenshot preview isn't available (complex tools, early stage).

```html
<div class="empty-state empty-state--illustrated">
  <div class="empty-state__icon" aria-hidden="true">
    <!-- Product-specific SVG — not a generic "empty box" -->
    <svg width="80" height="80" viewBox="0 0 80 80" fill="none">
      <!-- Icon that represents THIS specific type of empty content -->
      <!-- e.g., for "no reports": a document with a chart -->
      <!-- e.g., for "no members": silhouettes of people -->
      <!-- e.g., for "no events": a calendar -->
    </svg>
  </div>
  <h2>No reports yet</h2>
  <p>Reports give you a bird's eye view of your team's velocity and blockers. Create your first one.</p>
  <button class="btn-primary" type="button">Create report</button>
</div>
```

```css
.empty-state--illustrated .empty-state__icon {
  color: var(--color-text-muted);
  margin-bottom: var(--space-6);
  opacity: 0.6;
}

/* Subtle pulse animation to draw attention */
.empty-state--illustrated .empty-state__icon svg {
  animation: idle-float 4s ease-in-out infinite;
}

@keyframes idle-float {
  0%, 100% { transform: translateY(0); }
  50%       { transform: translateY(-6px); }
}

@media (prefers-reduced-motion: reduce) {
  .empty-state--illustrated .empty-state__icon svg { animation: none; }
}
```

---

## Pattern C — No Results (filtered/search empty)

Trigger: user searched or filtered and nothing matched. Goal: help them adjust.

```html
<div class="empty-state empty-state--no-results">
  <div class="empty-state__icon" aria-hidden="true">
    <!-- Search icon or magnifying glass -->
  </div>
  <h2>No results for "<strong>project alpha</strong>"</h2>
  <p>Try adjusting your search or filters, or check your spelling.</p>
  <div class="empty-state__actions">
    <button class="btn-primary" onclick="clearFilters()">
      Clear all filters
    </button>
    <button class="btn-ghost" onclick="clearSearch()">
      Clear search
    </button>
  </div>
</div>
```

```css
.empty-state--no-results { padding: var(--space-12) var(--space-6); }

.empty-state--no-results h2 strong {
  color: var(--color-text-primary);
  font-weight: 600;
}

.empty-state__actions {
  display: flex;
  gap: var(--space-3);
  flex-wrap: wrap;
  justify-content: center;
  margin-top: var(--space-5);
}
```

---

## Pattern D — Cleared State

Trigger: user deliberately deleted everything. Acknowledge the action; offer restart.

```html
<div class="empty-state empty-state--cleared">
  <h2>All projects archived</h2>
  <p>
    You've archived all your projects. They're safely stored in
    <a href="/archive">your archive</a> — restore any time.
  </p>
  <a href="/projects/new" class="btn-ghost">Start a new project</a>
</div>
```

This state is **not** the same as the first-time state. The user knows the product; don't explain it again.

---

## Pattern E — Permission Denied Empty State

Trigger: user has access to the container but not to the content within it.

```html
<div class="empty-state empty-state--locked">
  <div class="empty-state__icon" aria-hidden="true">🔒</div>
  <h2>Access restricted</h2>
  <p>
    You don't have permission to view projects in this workspace.
    Contact your workspace admin to request access.
  </p>
  <button class="btn-ghost" onclick="requestAccess()">
    Request access
  </button>
</div>
```

Never show a generic "no items" state for a permission issue. Users will assume the feature doesn't exist.

---

## Contextual Empty States (within cards/panels)

For smaller areas — table panels, sidebars, widget areas:

```html
<!-- Compact: no illustration, no title, direct action -->
<div class="empty-state-compact">
  <p>No comments yet. <a href="#comment-input">Add the first one.</a></p>
</div>
```

```css
.empty-state-compact {
  padding: var(--space-6);
  text-align: center;
  font-size: 0.875rem;
  color: var(--color-text-muted);
  border: 1px dashed var(--color-border);
  border-radius: var(--radius-lg);
}
```

---

## Copy Rules

```
Title:   [What's missing] — specific to this content type
         ✅ "No projects yet"    ❌ "Nothing here" ❌ "Empty" ❌ "No data"

Body:    [Why it's valuable] + [What to do]
         ✅ "Projects organize your designs and specs. Create your first one."
         ❌ "You haven't created any projects."

CTA:     Specific verb + content type
         ✅ "Create your first project"    ❌ "Get started" ❌ "Add item"

Tone:    Neutral + encouraging — never apologetic
         ❌ "Sorry, there's nothing here yet."
         ✅ "Your dashboard will appear here once you add your first data source."
```

---

## Anti-Patterns

- Generic "No data" or "Nothing to show" without context
- Showing a skeleton loader for a genuinely empty state (skeleton = content loading, not absent)
- Generic illustration (person shrugging, empty inbox icon for non-inbox content)
- Empty state that does not explain why it's empty
- CTA that goes to settings instead of directly to creation
- "No items found" for a search result without offering to clear the search

## Related Files

- `rules/13-saas-products.md` — R2: Empty states as product moments
- `blueprints/saas-app-from-scratch.md` — Core screen 1: Empty state
- `patterns/product-ui/loading-states.md` — skeleton vs. empty distinction
- `patterns/product-ui/error-states.md` — when empty is due to an error
