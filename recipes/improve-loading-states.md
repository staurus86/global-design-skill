# Recipe — Improve Loading States

> **Trigger:** The app goes blank, spins, or freezes when data is loading. Users can't tell if the request is in progress, failed, or stuck. The UI feels slow even when it isn't.

---

## Diagnosis Checklist

```
[ ] Page shows a full-screen spinner during data load
[ ] Layout shifts when content replaces the skeleton
[ ] Multiple skeleton items each have their own pulse animation
[ ] No error state when data fails to load
[ ] No empty state when the query returns zero results
[ ] Loading state reuses the spinner in contexts where a skeleton is better
[ ] "Loading..." text without a visual indicator
[ ] No optimistic UI — user waits for round trip on simple actions
[ ] Stale data shown briefly before new data arrives (no transition)
```

---

## Loading State Decision Tree

```
What is loading?
│
├── Initial page / route load
│     └── Full-page: use skeleton (never full-screen spinner)
│
├── A list / table of items
│     └── Use skeleton rows that match the real row structure
│
├── A card grid
│     └── Use skeleton cards at the same dimensions as real cards
│
├── A specific action (submit, delete)
│     └── Use inline spinner on the button; disable the button
│
├── Background refresh (polling, websocket update)
│     └── No visual if data arrives in < 1s
│     └── Subtle "Refreshing..." badge if > 1s
│
└── Progressive load (images, video, embeds)
      └── Use blur-up technique or aspect-ratio container
```

---

## Pattern 1 — Skeleton Loading (Preferred for Lists / Grids)

A structural preview that matches the real layout. No layout shift on data arrival.

```html
<!-- Use exact same container structure as the real content -->
<ul class="project-list" aria-label="Projects" aria-busy="true">

  <li class="skeleton-container project-card">
    <div class="skeleton project-card__icon"></div>
    <div class="project-card__body">
      <div class="skeleton skeleton--text skeleton--text-lg"></div>
      <div class="skeleton skeleton--text skeleton--text-sm"></div>
    </div>
    <div class="skeleton skeleton--badge"></div>
  </li>

  <li class="skeleton-container project-card">
    <!-- repeat 2–4 times matching expected item count -->
  </li>

</ul>
```

```css
.skeleton {
  background: var(--color-surface-3);
  border-radius: var(--radius-sm);
}

.skeleton--text    { height: 14px; width: 80%; }
.skeleton--text-lg { height: 16px; width: 60%; }
.skeleton--text-sm { height: 12px; width: 40%; margin-top: var(--space-2); }
.skeleton--badge   { height: 22px; width: 64px; border-radius: var(--radius-full); }

/* Single shimmer on container — not on each skeleton element */
.skeleton-container {
  position: relative;
  overflow: hidden;
}

@keyframes shimmer {
  from { background-position: 200% 0; }
  to   { background-position: -200% 0; }
}

.skeleton-container::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    90deg,
    transparent          0%,
    oklch(100% 0 0 / 0.05) 50%,
    transparent          100%
  );
  background-size: 200% 100%;
  animation: shimmer 1.8s linear infinite;
  pointer-events: none;
}

@media (prefers-reduced-motion: reduce) {
  .skeleton-container::after { animation: none; }
}
```

**Critical:** After real data loads, replace the skeleton list items — do NOT replace the outer container. This prevents layout shift.

```js
async function loadProjects () {
  const list = document.querySelector('.project-list')
  list.setAttribute('aria-busy', 'true')

  // Show skeleton
  list.innerHTML = generateSkeletons(3)

  try {
    const projects = await fetchProjects()
    // Replace skeleton items with real items — outer container stays
    list.innerHTML = projects.map(renderProject).join('')
    list.removeAttribute('aria-busy')
  } catch (err) {
    list.innerHTML = renderError(err)
    list.removeAttribute('aria-busy')
  }
}
```

---

## Pattern 2 — Button Loading State

When a form action or operation is in flight.

```html
<button class="btn btn--primary" type="submit" id="submit-btn">
  <svg class="btn__spinner" aria-hidden="true" width="16" height="16"
    viewBox="0 0 24 24" fill="none">
    <circle class="spinner-track" cx="12" cy="12" r="10"
      stroke="currentColor" stroke-width="2" stroke-opacity="0.25"/>
    <path class="spinner-head" d="M12 2a10 10 0 0 1 10 10"
      stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
  </svg>
  <span class="btn__label">Deploy</span>
</button>
```

```css
.btn__spinner {
  display: none;
  animation: spin 0.75s linear infinite;
  flex-shrink: 0;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}

.btn[aria-busy="true"] {
  pointer-events: none;
  cursor: not-allowed;
  opacity: 0.7;
}

.btn[aria-busy="true"] .btn__spinner { display: block; }
.btn[aria-busy="true"] .btn__label  { opacity: 0.7; }

@media (prefers-reduced-motion: reduce) {
  .btn__spinner { animation: none; opacity: 0.6; }
}
```

```js
async function handleSubmit (e) {
  e.preventDefault()
  const btn = e.submitter ?? document.getElementById('submit-btn')

  btn.setAttribute('aria-busy', 'true')
  btn.setAttribute('aria-label', 'Deploying...')

  try {
    await deploy()
    btn.removeAttribute('aria-busy')
    btn.setAttribute('aria-label', 'Deploy')
    showSuccess()
  } catch (err) {
    btn.removeAttribute('aria-busy')
    btn.setAttribute('aria-label', 'Deploy')
    showError(err)
  }
}
```

---

## Pattern 3 — Optimistic UI

Update the UI immediately, sync in the background, rollback on failure.

```tsx
'use client'
import { useOptimistic, useTransition } from 'react'

interface Todo {
  id: string
  text: string
  done: boolean
}

function TodoList ({ initial }: { initial: Todo[] }) {
  const [isPending, startTransition] = useTransition()
  const [todos, addOptimistic] = useOptimistic(
    initial,
    (state, newTodo: Todo) => [...state, newTodo]
  )

  async function addTodo (formData: FormData) {
    const text = formData.get('text') as string
    const optimistic: Todo = { id: 'temp', text, done: false }

    startTransition(async () => {
      addOptimistic(optimistic)          // Immediate UI update
      await saveTodo(text)               // Network request
      // On error: React rolls back addOptimistic automatically
    })
  }

  return (
    <ul aria-busy={isPending}>
      {todos.map(todo => (
        <li key={todo.id} style={{ opacity: todo.id === 'temp' ? 0.6 : 1 }}>
          {todo.text}
        </li>
      ))}
    </ul>
  )
}
```

---

## Pattern 4 — Progressive Image Loading (Blur-Up)

Prevents layout shift and shows immediate feedback.

```html
<!-- Reserve exact dimensions with aspect-ratio -->
<div class="img-wrap" style="--img-aspect: 16/9">
  <img
    class="img-blur"
    src="/hero-thumb.jpg"     <!-- tiny 20px LQIP placeholder -->
    data-src="/hero-full.jpg" <!-- full resolution -->
    alt="Product dashboard"
    width="1200"
    height="675"
    loading="eager"
    fetchpriority="high"
  />
</div>
```

```css
.img-wrap {
  position: relative;
  width: 100%;
  aspect-ratio: var(--img-aspect, 16/9);
  overflow: hidden;
  background: var(--color-surface-3);
  border-radius: var(--radius-lg);
}

.img-blur {
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: blur(20px);
  scale: 1.05; /* Hide blur edges */
  transition: filter 400ms var(--ease-smooth), scale 400ms var(--ease-smooth);
}

.img-blur.is-loaded {
  filter: blur(0);
  scale: 1;
}

@media (prefers-reduced-motion: reduce) {
  .img-blur { transition: none; filter: none; scale: 1; }
}
```

```js
document.querySelectorAll('.img-blur[data-src]').forEach(img => {
  const full = new Image()
  full.src = img.dataset.src
  full.onload = () => {
    img.src = full.src
    img.classList.add('is-loaded')
    img.removeAttribute('data-src')
  }
})
```

---

## Pattern 5 — Empty State (Zero Results)

An empty state is not a bug — it's a feature. Guide the user to the next step.

```html
<div class="empty-state" role="status" aria-live="polite">
  <svg class="empty-state__icon" aria-hidden="true" width="48" height="48"
    viewBox="0 0 24 24" fill="none" stroke="currentColor"
    stroke-width="1" stroke-linecap="round" stroke-linejoin="round">
    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
  </svg>
  <h3 class="empty-state__title">No projects yet</h3>
  <p class="empty-state__desc">Create your first project to start deploying in under 5 minutes.</p>
  <a href="/projects/new" class="btn btn--primary">Create project</a>
</div>
```

```css
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: var(--space-16) var(--space-8);
  gap: var(--space-4);
}

.empty-state__icon { color: var(--color-text-muted); opacity: 0.5; }

.empty-state__title {
  font-size: var(--text-h3);
  font-weight: var(--font-weight-semibold);
  color: var(--color-text-primary);
  margin: 0;
}

.empty-state__desc {
  font-size: var(--text-body);
  color: var(--color-text-secondary);
  max-width: 36ch;
  margin: 0;
  line-height: 1.65;
}
```

---

## Before/After Summary

| Problem | Fix |
|---|---|
| Full-screen spinner on load | Layout-matched skeleton |
| Skeleton items each pulse | Single shimmer on skeleton container |
| Layout shift when data arrives | Skeleton uses same DOM structure as real content |
| No button loading state | `aria-busy="true"` + inline spinner |
| User waits for simple actions | Optimistic UI with rollback |
| Images cause layout shift | `aspect-ratio` container + explicit dimensions |
| Blurry placeholder → jarring swap | Blur-up technique |
| Empty list shows nothing | Empty state with next action |

---

## Verification

```
[ ] Skeleton structure matches real content structure exactly
[ ] Only 1 shimmer animation per skeleton group
[ ] No layout shift when real data replaces skeleton (check with DevTools CLS)
[ ] Buttons show spinner and disable during async action
[ ] aria-busy="true" on loading containers
[ ] Empty state present for all list/table views
[ ] Error state present for all data fetches
[ ] Images have explicit width + height (prevents CLS)
[ ] prefers-reduced-motion disables shimmer and spinner animation
```

---

*Recipe version: global-design-skill v1.0 — `recipes/improve-loading-states.md`*  
*Related: `rules/08-performance.md`, `patterns/product-ui/notifications.md`, `agents/performance-auditor.md`*
