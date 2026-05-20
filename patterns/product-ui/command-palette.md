# Pattern — Command Palette

> The command palette is the power user's shortcut to every action in the product. Triggered by ⌘K / Ctrl+K, it replaces menu navigation for experienced users. Required in any product with more than 20 distinct actions.

---

## When to Implement

```
Add a command palette when:
  Product has 20+ distinct user actions
  Users are technical or power-user oriented
  Navigation has grown complex (more than 3 levels)
  Users report feeling "stuck" finding specific features
  Analytics show high use of search to navigate
```

---

## Pattern — Full Command Palette

```html
<!-- Trigger in header (shows keyboard shortcut as affordance) -->
<button class="cmd-trigger" type="button" aria-label="Open command palette (⌘K)">
  <svg class="cmd-trigger__icon" aria-hidden="true" width="16" height="16"
    viewBox="0 0 24 24" fill="none" stroke="currentColor"
    stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>
  </svg>
  <span class="cmd-trigger__label">Search or jump to...</span>
  <kbd class="cmd-trigger__kbd">⌘K</kbd>
</button>

<!-- Overlay + dialog -->
<div class="cmd-overlay" id="cmd-overlay" hidden aria-hidden="true"></div>

<div
  class="cmd-palette"
  id="cmd-palette"
  role="dialog"
  aria-label="Command palette"
  aria-modal="true"
  hidden
>
  <!-- Search input -->
  <div class="cmd-search">
    <svg class="cmd-search__icon" aria-hidden="true" width="18" height="18"
      viewBox="0 0 24 24" fill="none" stroke="currentColor"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>
    </svg>
    <input
      class="cmd-search__input"
      type="search"
      role="combobox"
      aria-expanded="true"
      aria-controls="cmd-listbox"
      aria-autocomplete="list"
      aria-activedescendant=""
      placeholder="Search commands, pages, or people..."
      autocomplete="off"
      spellcheck="false"
      id="cmd-input"
    />
    <kbd class="cmd-search__esc">Esc</kbd>
  </div>

  <!-- Results list -->
  <ul class="cmd-results" id="cmd-listbox" role="listbox" aria-label="Commands">
    <!-- Groups injected by JS -->
  </ul>

  <!-- Footer hint -->
  <div class="cmd-footer" aria-hidden="true">
    <span><kbd>↑↓</kbd> Navigate</span>
    <span><kbd>↵</kbd> Select</span>
    <span><kbd>Esc</kbd> Dismiss</span>
  </div>
</div>
```

```css
.cmd-overlay {
  position: fixed;
  inset: 0;
  background: oklch(0% 0 0 / 0.5);
  backdrop-filter: blur(2px);
  z-index: var(--z-modal);
  @starting-style { opacity: 0; }
  opacity: 1;
  transition: opacity var(--duration-fast) var(--ease-smooth);
}

.cmd-overlay[hidden] { display: none; }

.cmd-palette {
  position: fixed;
  top: 12vh;
  left: 50%;
  transform: translateX(-50%);
  width: min(640px, calc(100vw - var(--space-8)));
  max-height: 60vh;
  display: flex;
  flex-direction: column;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-lg), 0 0 0 1px oklch(0% 0 0 / 0.05);
  overflow: hidden;
  z-index: calc(var(--z-modal) + 1);

  @starting-style {
    opacity: 0;
    transform: translateX(-50%) translateY(-8px) scale(0.97);
  }
  opacity: 1;
  transform: translateX(-50%) translateY(0) scale(1);
  transition:
    opacity   150ms var(--ease-spring),
    transform 150ms var(--ease-spring);
}

.cmd-palette[hidden] { display: none; }

/* Search bar */
.cmd-search {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-4);
  border-bottom: 1px solid var(--color-border);
  flex-shrink: 0;
}

.cmd-search__icon { color: var(--color-text-muted); flex-shrink: 0; }

.cmd-search__input {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  font-size: var(--text-body);
  font-family: var(--font-body);
  color: var(--color-text-primary);
  min-width: 0;
}

.cmd-search__input::placeholder { color: var(--color-text-muted); }

.cmd-search__esc {
  padding: 2px var(--space-2);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  font-size: 11px;
  font-family: var(--font-mono);
  color: var(--color-text-muted);
  flex-shrink: 0;
}

/* Results */
.cmd-results {
  flex: 1;
  overflow-y: auto;
  padding: var(--space-2);
  list-style: none;
  scrollbar-width: thin;
  scrollbar-color: var(--color-border) transparent;
}

.cmd-group-label {
  padding: var(--space-2) var(--space-3) var(--space-1);
  font-size: 11px;
  font-weight: var(--font-weight-semibold);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-text-muted);
}

.cmd-item {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-md);
  cursor: pointer;
  min-height: 44px;
  transition: background var(--duration-fast) var(--ease-smooth);
}

.cmd-item[aria-selected="true"] {
  background: var(--color-accent-subtle);
}

.cmd-item__icon {
  width: 28px; height: 28px;
  border-radius: var(--radius-sm);
  background: var(--color-surface-3);
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
  color: var(--color-text-secondary);
}

.cmd-item[aria-selected="true"] .cmd-item__icon {
  background: oklch(from var(--color-accent) l c h / 0.15);
  color: var(--color-accent);
}

.cmd-item__main { flex: 1; min-width: 0; }

.cmd-item__title {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-primary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.cmd-item__title mark {
  background: transparent;
  color: var(--color-accent);
  font-weight: var(--font-weight-semibold);
}

.cmd-item__sub {
  font-size: 12px;
  color: var(--color-text-muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.cmd-item__kbd {
  padding: 2px var(--space-2);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  font-size: 11px;
  font-family: var(--font-mono);
  color: var(--color-text-muted);
  flex-shrink: 0;
  white-space: nowrap;
}

.cmd-results__empty {
  padding: var(--space-10) var(--space-6);
  text-align: center;
  color: var(--color-text-secondary);
  font-size: var(--text-sm);
}

/* Footer */
.cmd-footer {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  padding: var(--space-2) var(--space-4);
  border-top: 1px solid var(--color-border);
  flex-shrink: 0;
}

.cmd-footer span {
  display: flex;
  align-items: center;
  gap: var(--space-1);
  font-size: 11px;
  color: var(--color-text-muted);
}

.cmd-footer kbd {
  padding: 1px var(--space-1);
  border: 1px solid var(--color-border);
  border-radius: 3px;
  font-size: 10px;
  font-family: var(--font-mono);
}

@media (prefers-reduced-motion: reduce) {
  .cmd-overlay { transition: none; }
  .cmd-palette { transition: none; }
}

@media (max-width: 640px) {
  .cmd-palette {
    top: 0;
    left: 0;
    right: 0;
    transform: none;
    width: 100%;
    max-height: 80vh;
    border-radius: 0 0 var(--radius-xl) var(--radius-xl);
  }

  @starting-style {
    .cmd-palette { transform: translateY(-100%); opacity: 0; }
  }
  .cmd-palette { transform: translateY(0); }
}
```

```js
class CommandPalette {
  constructor () {
    this.overlay   = document.getElementById('cmd-overlay')
    this.dialog    = document.getElementById('cmd-palette')
    this.input     = document.getElementById('cmd-input')
    this.listbox   = document.getElementById('cmd-listbox')
    this.trigger   = document.querySelector('.cmd-trigger')
    this.activeIdx = -1
    this.commands  = []   // loaded from your data source

    this.trigger?.addEventListener('click', () => this.open())
    this.overlay.addEventListener('click',  () => this.close())
    this.input.addEventListener('input',    () => this.filter())
    this.input.addEventListener('keydown',  e  => this.onKey(e))

    document.addEventListener('keydown', e => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault()
        this.dialog.hidden ? this.open() : this.close()
      }
      if (e.key === 'Escape' && !this.dialog.hidden) this.close()
    })
  }

  open () {
    this.dialog.hidden  = false
    this.overlay.hidden = false
    this.overlay.removeAttribute('aria-hidden')
    this.input.value = ''
    this.render(this.commands)
    requestAnimationFrame(() => this.input.focus())
  }

  close () {
    this.dialog.hidden  = true
    this.overlay.hidden = true
    this.overlay.setAttribute('aria-hidden', 'true')
    this.trigger?.focus()
  }

  filter () {
    const q = this.input.value.toLowerCase().trim()
    if (!q) { this.render(this.commands); return }
    const filtered = this.commands.filter(cmd =>
      cmd.title.toLowerCase().includes(q) ||
      cmd.group?.toLowerCase().includes(q) ||
      cmd.keywords?.some(k => k.includes(q))
    )
    this.render(filtered, q)
  }

  render (commands, query = '') {
    this.activeIdx = -1
    this.input.setAttribute('aria-activedescendant', '')

    if (!commands.length) {
      this.listbox.innerHTML = `<li class="cmd-results__empty">No commands found</li>`
      return
    }

    // Group by category
    const groups = commands.reduce((acc, cmd) => {
      const g = cmd.group || 'Other'
      if (!acc[g]) acc[g] = []
      acc[g].push(cmd)
      return acc
    }, {})

    let idx = 0
    this.listbox.innerHTML = Object.entries(groups).map(([group, items]) => `
      <li>
        <p class="cmd-group-label" role="presentation">${group}</p>
        <ul role="presentation">
          ${items.map(cmd => {
            const id   = `cmd-item-${idx}`
            const html = `
              <li
                class="cmd-item"
                role="option"
                id="${id}"
                data-action="${cmd.action}"
                data-href="${cmd.href || ''}"
              >
                <div class="cmd-item__icon" aria-hidden="true">${cmd.icon || ''}</div>
                <div class="cmd-item__main">
                  <div class="cmd-item__title">${query ? this.highlight(cmd.title, query) : cmd.title}</div>
                  ${cmd.sub ? `<div class="cmd-item__sub">${cmd.sub}</div>` : ''}
                </div>
                ${cmd.kbd ? `<kbd class="cmd-item__kbd">${cmd.kbd}</kbd>` : ''}
              </li>
            `
            idx++
            return html
          }).join('')}
        </ul>
      </li>
    `).join('')

    this.listbox.querySelectorAll('[role="option"]').forEach(el => {
      el.addEventListener('click', () => this.execute(el))
    })
  }

  highlight (text, q) {
    const re = new RegExp(`(${q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi')
    return text.replace(re, '<mark>$1</mark>')
  }

  execute (el) {
    if (el.dataset.href) window.location.href = el.dataset.href
    else if (el.dataset.action) document.dispatchEvent(new CustomEvent(el.dataset.action))
    this.close()
  }

  onKey (e) {
    const items = [...this.listbox.querySelectorAll('[role="option"]')]
    if (!items.length) return

    if (e.key === 'ArrowDown') {
      e.preventDefault()
      this.activeIdx = Math.min(this.activeIdx + 1, items.length - 1)
      this.setActive(items)
    } else if (e.key === 'ArrowUp') {
      e.preventDefault()
      this.activeIdx = Math.max(this.activeIdx - 1, -1)
      this.setActive(items)
    } else if (e.key === 'Enter' && this.activeIdx >= 0) {
      this.execute(items[this.activeIdx])
    }
  }

  setActive (items) {
    items.forEach((item, i) => {
      item.setAttribute('aria-selected', String(i === this.activeIdx))
    })
    this.input.setAttribute(
      'aria-activedescendant',
      this.activeIdx >= 0 ? items[this.activeIdx].id : ''
    )
    if (this.activeIdx >= 0) {
      items[this.activeIdx].scrollIntoView({ block: 'nearest' })
    }
  }
}

const palette = new CommandPalette()

// Example: Load commands from JSON
fetch('/api/commands')
  .then(r => r.json())
  .then(data => { palette.commands = data })
```

---

## Command Data Structure

```json
[
  {
    "title": "New Deployment",
    "group": "Actions",
    "sub": "Create a new deployment",
    "href": "/deployments/new",
    "kbd": "⌘N",
    "icon": "<svg .../>",
    "keywords": ["deploy", "release", "ship"]
  },
  {
    "title": "Go to Overview",
    "group": "Navigation",
    "href": "/overview",
    "icon": "<svg .../>",
    "keywords": ["home", "dashboard"]
  },
  {
    "title": "Toggle Dark Mode",
    "group": "Appearance",
    "action": "toggle-theme",
    "icon": "<svg .../>",
    "keywords": ["theme", "dark", "light"]
  }
]
```

---

## Anti-Patterns

```
× Command palette without ⌘K shortcut — undiscoverable
× No keyboard shortcut shown in trigger — users won't know it exists
× Results list without grouping — unstructured, hard to scan
× No empty state — blank area when no match looks broken
× No Escape to close
× Focus not trapped inside dialog
× Commands that require confirmation (destructive) executed immediately
× More than 5-6 groups — too many categories defeats the purpose
```

---

*Pattern version: global-design-skill v1.0 — `patterns/product-ui/command-palette.md`*  
*Related: `patterns/product-ui/search.md`, `patterns/product-ui/modals.md`, `rules/07-accessibility.md`*
