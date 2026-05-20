# Pattern — Loading States

> Loading states are a promise: "your data is coming." The design must maintain user confidence during the wait and match the loaded layout exactly when it arrives.

---

## The Loading Decision Matrix

Choose a loading pattern based on expected wait duration:

| Duration | Pattern | Rationale |
|---|---|---|
| < 100ms | No indicator | Flash of loading is worse than no indicator |
| 100ms – 1s | Skeleton loader | Shows that content is coming, prevents layout shift |
| 1s – 10s | Skeleton + progress indicator | User needs to know work is in progress |
| > 10s | Progress bar + "Continue in background" option | User may want to do something else |
| Unknown | Skeleton with shimmer | Default when duration can't be estimated |

**Never show a skeleton for a genuinely empty state.** Skeleton means "data is loading." Empty means "no data exists." These are different states with different designs.

---

## Pattern A — Skeleton Loader

The primary loading pattern for content that has a known layout.

**Critical rule:** The skeleton must match the layout of the loaded content exactly. If the loaded card has a 48px avatar, a title, and two lines of text, the skeleton has a 48px circle, a title bar, and two text bars.

```html
<!-- Skeleton for a user card -->
<div class="skeleton-card" aria-busy="true" aria-label="Loading user information">
  <div class="skeleton-row">
    <div class="skeleton skeleton--circle" style="width: 48px; height: 48px;"></div>
    <div class="skeleton-col">
      <div class="skeleton skeleton--text" style="width: 60%;"></div>
      <div class="skeleton skeleton--text" style="width: 40%;"></div>
    </div>
  </div>
  <div class="skeleton skeleton--text" style="width: 80%;"></div>
  <div class="skeleton skeleton--text" style="width: 55%;"></div>
  <div class="skeleton skeleton--rect" style="height: 36px;"></div>
</div>
```

```css
/* Base skeleton element */
.skeleton {
  background: var(--color-surface-2);
  border-radius: var(--radius-sm);
  animation: shimmer 1.6s ease-in-out infinite;
  background-image: linear-gradient(
    90deg,
    var(--color-surface-2) 25%,
    oklch(from var(--color-surface-2) calc(l + 0.05) c h) 50%,
    var(--color-surface-2) 75%
  );
  background-size: 400% 100%;
}

@keyframes shimmer {
  0%   { background-position: 200% center; }
  100% { background-position: -200% center; }
}

@media (prefers-reduced-motion: reduce) {
  .skeleton {
    animation: none;
    background-image: none;
  }
}

/* Variants */
.skeleton--text {
  height: 1em;
  border-radius: var(--radius-sm);
  margin-block: 0.25em;
}

.skeleton--circle { border-radius: 50%; }

.skeleton--rect {
  width: 100%;
  border-radius: var(--radius-md);
}

/* Layout helpers */
.skeleton-row {
  display: flex;
  gap: var(--space-3);
  align-items: center;
}

.skeleton-col {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  flex: 1;
}
```

---

## Pattern B — Skeleton Table

For data tables loading their rows.

```html
<table aria-busy="true" aria-label="Loading project list">
  <thead>
    <tr>
      <th>Name</th>
      <th>Status</th>
      <th>Members</th>
      <th>Updated</th>
    </tr>
  </thead>
  <tbody>
    <!-- Repeat 8-10 skeleton rows -->
    <tr class="skeleton-row-tr" aria-hidden="true">
      <td><div class="skeleton skeleton--text" style="width: 70%;"></div></td>
      <td><div class="skeleton skeleton--text" style="width: 50%;"></div></td>
      <td><div class="skeleton skeleton--text" style="width: 40%;"></div></td>
      <td><div class="skeleton skeleton--text" style="width: 55%;"></div></td>
    </tr>
    <!-- … -->
  </tbody>
</table>
```

```css
.skeleton-row-tr td {
  padding-block: var(--space-3);
  border-bottom: 1px solid var(--color-border);
}

/* Stagger the shimmer for a wave effect */
.skeleton-row-tr:nth-child(1) .skeleton { animation-delay: 0ms; }
.skeleton-row-tr:nth-child(2) .skeleton { animation-delay: 60ms; }
.skeleton-row-tr:nth-child(3) .skeleton { animation-delay: 120ms; }
.skeleton-row-tr:nth-child(4) .skeleton { animation-delay: 180ms; }
```

---

## Pattern C — Button Loading State

Trigger: user clicks a button that triggers an async operation (form submit, delete, save).

```html
<button class="btn-primary btn-loading" disabled aria-disabled="true" aria-busy="true">
  <span class="btn-spinner" aria-hidden="true"></span>
  <span>Saving changes…</span>
</button>
```

```css
.btn-loading {
  position: relative;
  pointer-events: none;
  opacity: 0.75;
}

.btn-spinner {
  width: 16px;
  height: 16px;
  border: 2px solid currentColor;
  border-top-color: transparent;
  border-radius: 50%;
  animation: spin 600ms linear infinite;
  flex-shrink: 0;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

@media (prefers-reduced-motion: reduce) {
  .btn-spinner { animation: none; opacity: 0.5; }
}
```

**Label change rule:** Change the button label during loading: "Save" → "Saving…". This confirms to the user that the action was received.

---

## Pattern D — Page / Section Loading

Trigger: navigating to a new page, loading a complex dashboard, or switching between heavy tabs.

```tsx
// Next.js 15: loading.tsx
export default function DashboardLoading() {
  return (
    <div className="dashboard-skeleton">
      {/* Match the exact layout of the dashboard */}
      <div className="skeleton-header">
        <div className="skeleton skeleton--text" style={{ width: '200px', height: '32px' }} />
        <div className="skeleton skeleton--rect" style={{ width: '120px', height: '40px' }} />
      </div>

      <div className="skeleton-metrics">
        {[...Array(4)].map((_, i) => (
          <div key={i} className="skeleton-metric-card">
            <div className="skeleton skeleton--text" style={{ width: '50%' }} />
            <div className="skeleton skeleton--text" style={{ width: '70%', height: '2em' }} />
          </div>
        ))}
      </div>

      <div className="skeleton skeleton--rect" style={{ height: '300px' }} />
    </div>
  )
}
```

---

## Pattern E — Progress Bar (long operations)

Trigger: operations that take 1-10 seconds, where the system can estimate progress.

```html
<div class="progress-container" role="status" aria-label="Uploading file: 64% complete">
  <div class="progress-header">
    <span class="progress-label">Uploading design assets</span>
    <span class="progress-percentage">64%</span>
  </div>
  <div class="progress-track" role="progressbar" aria-valuenow="64" aria-valuemin="0" aria-valuemax="100">
    <div class="progress-fill" style="width: 64%"></div>
  </div>
  <p class="progress-detail">12 of 19 files · 2 minutes remaining</p>
</div>
```

```css
.progress-container {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  padding: var(--space-4);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
}

.progress-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.9375rem;
  font-weight: 500;
}

.progress-track {
  height: 6px;
  background: var(--color-surface-2);
  border-radius: 9999px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: var(--color-accent);
  border-radius: 9999px;
  transition: width 400ms cubic-bezier(0.16, 1, 0.3, 1);
}

.progress-detail {
  font-size: 0.8125rem;
  color: var(--color-text-muted);
}
```

---

## Pattern F — Indeterminate Progress (unknown duration)

When progress can't be estimated, use an indeterminate indicator.

```css
/* Indeterminate progress bar */
.progress-fill--indeterminate {
  width: 40%;
  animation: indeterminate 1.5s ease-in-out infinite;
}

@keyframes indeterminate {
  0%   { transform: translateX(-100%); }
  100% { transform: translateX(350%); }
}

@media (prefers-reduced-motion: reduce) {
  .progress-fill--indeterminate {
    animation: none;
    width: 100%;
    opacity: 0.4;
  }
}
```

---

## Optimistic Loading (instant perceived response)

The best loading state is no loading state. Use optimistic updates for operations likely to succeed.

```tsx
// React 19 useOptimistic
const [optimisticItems, addOptimistic] = useOptimistic(
  items,
  (state, newItem) => [...state, { ...newItem, saving: true }]
)

async function handleAdd(formData: FormData) {
  const newItem = { id: 'temp', name: formData.get('name'), saving: true }

  // Update UI immediately — no loading state shown
  addOptimistic(newItem)

  // Sync with server in background
  await createItem(formData)
}
```

Show a subtle "saving" indicator on the optimistic item, not a blocking loading state:

```css
.item--saving {
  opacity: 0.7;
  pointer-events: none;
}

.item--saving::after {
  content: 'Saving…';
  font-size: 0.75rem;
  color: var(--color-text-muted);
  margin-left: var(--space-2);
}
```

---

## Anti-Patterns

- Showing a spinner with no context ("Loading…" for 10 seconds with no progress info)
- Skeleton that doesn't match the actual loaded layout (causes layout shift)
- Skeleton for empty states (skeleton = loading, empty state = no data)
- Progress bar that jumps from 0% to 100% instantly (fake progress is worse than no progress)
- Button spinner without disabling the button (user can click multiple times)
- Hiding the skeleton with `display: none` instead of removing it from DOM (still announced by screen readers)
- Not resetting button label after loading completes ("Saving…" that stays after save is done)

## Related Files

- `rules/13-saas-products.md` — R5: Real-time feedback, Doherty Threshold
- `skills/global-design/operating-principles.md` — Principle 4: Loading decision matrix
- `skills/global-design/quality-gates.md` — Gate 4: Loading state required
- `patterns/product-ui/error-states.md` — when loading fails
- `patterns/product-ui/empty-states.md` — when loaded content is genuinely empty
