# Pattern — Search

> Search is the fastest path from intent to result. It must respond within 300ms, filter results as-you-type after 300ms debounce, and never abandon the user without a helpful empty state.

---

## Search Types

| Type | Use when | Response time |
|---|---|---|
| **Inline filter** | Filtering visible list on the same page | Immediate (0ms debounce) |
| **Live search** | Querying API, showing suggestions | 300ms debounce |
| **Global search** | Searching across the entire product | 300ms debounce + command palette |
| **Full-page search** | SEO search results, document search | On submit, paginated |

---

## Pattern 1 — Inline Filter Search

For filtering an already-loaded list or table. No network call.

```html
<div class="search-field search-field--inline">
  <svg class="search-field__icon" aria-hidden="true" width="16" height="16"
    viewBox="0 0 24 24" fill="none" stroke="currentColor"
    stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>
  </svg>
  <input
    class="search-field__input"
    type="search"
    placeholder="Filter by name..."
    aria-label="Filter projects by name"
    autocomplete="off"
    spellcheck="false"
  />
  <button class="search-field__clear" type="button" aria-label="Clear search" hidden>
    <svg aria-hidden="true" width="14" height="14" viewBox="0 0 16 16" fill="none"
      stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
      <path d="M4 4l8 8M12 4l-8 8"/>
    </svg>
  </button>
</div>
```

```css
.search-field {
  position: relative;
  display: flex;
  align-items: center;
}

.search-field__icon {
  position: absolute;
  left: var(--space-3);
  color: var(--color-text-muted);
  pointer-events: none;
  flex-shrink: 0;
}

.search-field__input {
  width: 100%;
  padding: var(--space-2) var(--space-3) var(--space-2) calc(var(--space-3) + 16px + var(--space-2));
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  background: var(--color-surface);
  color: var(--color-text-primary);
  font-size: var(--text-body);
  font-family: var(--font-body);
  transition: border-color var(--duration-fast) var(--ease-smooth);
}

.search-field__input:focus {
  outline: none;
  border-color: var(--color-border-focus);
  box-shadow: 0 0 0 3px oklch(from var(--color-border-focus) l c h / 0.12);
}

.search-field__input::-webkit-search-cancel-button { display: none; }

.search-field__clear {
  position: absolute;
  right: var(--space-2);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 24px; height: 24px;
  border-radius: var(--radius-sm);
  background: transparent;
  border: none;
  color: var(--color-text-muted);
  cursor: pointer;
  transition: background var(--duration-fast) var(--ease-smooth);
}

.search-field__clear:hover { background: var(--color-surface-2); }
.search-field__clear[hidden] { display: none; }

/* When user has text — add right padding for clear button */
.search-field__input:not(:placeholder-shown) {
  padding-right: calc(var(--space-2) + 24px + var(--space-2));
}
```

```js
const input   = document.querySelector('.search-field__input')
const clear   = document.querySelector('.search-field__clear')
const items   = document.querySelectorAll('[data-searchable]')

input.addEventListener('input', () => {
  const q = input.value.toLowerCase().trim()
  clear.hidden = q === ''

  items.forEach(item => {
    const text = item.textContent.toLowerCase()
    item.hidden = q !== '' && !text.includes(q)
  })
})

clear.addEventListener('click', () => {
  input.value = ''
  input.dispatchEvent(new Event('input'))
  input.focus()
})
```

---

## Pattern 2 — Live Search with Suggestions

API-powered typeahead with a suggestions dropdown.

```html
<div class="search-combobox" role="combobox" aria-expanded="false" aria-haspopup="listbox">
  <div class="search-field">
    <svg class="search-field__icon" aria-hidden="true" width="16" height="16"
      viewBox="0 0 24 24" fill="none" stroke="currentColor"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>
    </svg>
    <input
      class="search-field__input"
      type="search"
      role="searchbox"
      aria-autocomplete="list"
      aria-controls="search-listbox"
      aria-activedescendant=""
      placeholder="Search..."
      aria-label="Search"
      autocomplete="off"
      spellcheck="false"
    />
    <span class="search-field__kbd" aria-hidden="true">⌘K</span>
  </div>

  <ul
    class="search-results"
    id="search-listbox"
    role="listbox"
    aria-label="Search suggestions"
    hidden
  >
    <!-- Injected by JS -->
  </ul>
</div>
```

```css
.search-combobox { position: relative; }

.search-field__kbd {
  position: absolute;
  right: var(--space-3);
  padding: 2px var(--space-2);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  font-size: 11px;
  font-family: var(--font-mono);
  color: var(--color-text-muted);
  background: var(--color-surface-2);
}

.search-results {
  position: absolute;
  top: calc(100% + var(--space-2));
  left: 0; right: 0;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
  padding: var(--space-1);
  list-style: none;
  max-height: 320px;
  overflow-y: auto;
  z-index: var(--z-dropdown);

  /* Smooth open */
  @starting-style { opacity: 0; transform: translateY(-4px); }
  opacity: 1;
  transform: translateY(0);
  transition:
    opacity   var(--duration-fast) var(--ease-spring),
    transform var(--duration-fast) var(--ease-spring);
}

.search-results[hidden] { display: none; }

.search-result-item {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: background var(--duration-fast) var(--ease-smooth);
}

.search-result-item:hover,
.search-result-item[aria-selected="true"] {
  background: var(--color-surface-2);
}

.search-result-item__icon {
  width: 32px; height: 32px;
  border-radius: var(--radius-sm);
  background: var(--color-surface-3);
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
  color: var(--color-text-secondary);
}

.search-result-item__main { flex: 1; min-width: 0; }
.search-result-item__title {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-primary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.search-result-item__sub {
  font-size: 12px;
  color: var(--color-text-muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* Highlight matched characters */
.search-result-item__title mark {
  background: transparent;
  color: var(--color-accent);
  font-weight: var(--font-weight-semibold);
}

.search-results__section-label {
  padding: var(--space-2) var(--space-3) var(--space-1);
  font-size: 11px;
  font-weight: var(--font-weight-semibold);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-text-muted);
}

.search-results__empty {
  padding: var(--space-6) var(--space-4);
  text-align: center;
  color: var(--color-text-secondary);
  font-size: var(--text-sm);
}
```

```js
class LiveSearch {
  constructor (container) {
    this.input    = container.querySelector('[role="searchbox"]')
    this.listbox  = container.querySelector('[role="listbox"]')
    this.combobox = container
    this.timer    = null
    this.activeIndex = -1

    this.input.addEventListener('input',   () => this.onInput())
    this.input.addEventListener('keydown', e  => this.onKey(e))
    document.addEventListener('click', e => {
      if (!container.contains(e.target)) this.close()
    })
  }

  onInput () {
    clearTimeout(this.timer)
    const q = this.input.value.trim()
    if (!q) { this.close(); return }
    this.timer = setTimeout(() => this.fetch(q), 300)
  }

  async fetch (q) {
    const res = await fetch(`/api/search?q=${encodeURIComponent(q)}`)
    const { results } = await res.json()
    this.render(results, q)
  }

  render (results, q) {
    if (!results.length) {
      this.listbox.innerHTML = `<li class="search-results__empty">No results for "${q}"</li>`
      this.open()
      return
    }
    this.listbox.innerHTML = results.map((r, i) => `
      <li
        class="search-result-item"
        role="option"
        id="result-${i}"
        data-href="${r.url}"
      >
        <div class="search-result-item__main">
          <div class="search-result-item__title">${this.highlight(r.title, q)}</div>
          <div class="search-result-item__sub">${r.category}</div>
        </div>
      </li>
    `).join('')

    this.listbox.querySelectorAll('[role="option"]').forEach(el => {
      el.addEventListener('click', () => window.location.href = el.dataset.href)
    })

    this.activeIndex = -1
    this.open()
  }

  highlight (text, q) {
    const re = new RegExp(`(${q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi')
    return text.replace(re, '<mark>$1</mark>')
  }

  open () {
    this.listbox.hidden = false
    this.combobox.setAttribute('aria-expanded', 'true')
  }

  close () {
    this.listbox.hidden = true
    this.combobox.setAttribute('aria-expanded', 'false')
    this.activeIndex = -1
  }

  onKey (e) {
    const items = [...this.listbox.querySelectorAll('[role="option"]')]
    if (!items.length) return

    if (e.key === 'ArrowDown') {
      e.preventDefault()
      this.activeIndex = Math.min(this.activeIndex + 1, items.length - 1)
      this.setActive(items)
    } else if (e.key === 'ArrowUp') {
      e.preventDefault()
      this.activeIndex = Math.max(this.activeIndex - 1, -1)
      this.setActive(items)
    } else if (e.key === 'Enter' && this.activeIndex >= 0) {
      window.location.href = items[this.activeIndex].dataset.href
    } else if (e.key === 'Escape') {
      this.close()
      this.input.focus()
    }
  }

  setActive (items) {
    items.forEach((item, i) => {
      const active = i === this.activeIndex
      item.setAttribute('aria-selected', String(active))
    })
    this.input.setAttribute(
      'aria-activedescendant',
      this.activeIndex >= 0 ? `result-${this.activeIndex}` : ''
    )
    if (this.activeIndex >= 0) items[this.activeIndex].scrollIntoView({ block: 'nearest' })
  }
}

document.querySelectorAll('.search-combobox').forEach(el => new LiveSearch(el))
```

---

## Pattern 3 — Empty State

Never leave the user staring at a blank results area.

```html
<!-- No results -->
<div class="search-empty" role="status" aria-live="polite">
  <svg class="search-empty__icon" aria-hidden="true" width="48" height="48"
    viewBox="0 0 24 24" fill="none" stroke="currentColor"
    stroke-width="1" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>
    <path d="M8 11h6M11 8v6"/>
  </svg>
  <p class="search-empty__title">No results for "deplooy"</p>
  <p class="search-empty__hint">Check the spelling, or try a shorter keyword.</p>
</div>
```

```css
.search-empty {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: var(--space-12) var(--space-6);
  gap: var(--space-3);
}

.search-empty__icon { color: var(--color-text-muted); opacity: 0.5; }
.search-empty__title {
  font-size: var(--text-body);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-primary);
}
.search-empty__hint {
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  max-width: 28ch;
}
```

---

## Anti-Patterns

```
× Search without debounce — fires API call on every keystroke
× No loading state — user doesn't know request is in progress
× No empty state — blank area looks broken
× Search results without keyboard navigation
× Clearing results list on blur — user can't click a result
× Showing partial results without a "View all results" link for long lists
× Search that doesn't preserve query in URL (breaks browser back)
```

---

*Pattern version: global-design-skill v1.0 — `patterns/product-ui/search.md`*  
*Related: `patterns/product-ui/command-palette.md`, `patterns/product-ui/forms.md`, `rules/07-accessibility.md`*
