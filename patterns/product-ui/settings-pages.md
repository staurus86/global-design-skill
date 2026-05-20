# Pattern — Settings Pages

> Settings must be findable, understandable, and safe. Findable: users should not need to search for settings. Understandable: the effect of each control is obvious before changing it. Safe: destructive actions require explicit confirmation.

---

## Settings IA

Organize by user mental model, not by product architecture. Users think "I want to change my name" — not "I want to access the user_profile database record."

### Standard structure (SaaS)

```
Settings
├── Profile            Name, email, avatar, timezone, language
├── Account            Plan, billing, usage, invoices
├── Notifications      Per-event + per-channel controls
├── Security           Password, 2FA, sessions, connected devices
├── Workspace          (if multi-user) Name, branding, slug
├── Members            Invite, roles, remove members
├── Integrations       OAuth apps, API keys, webhooks
└── Danger zone        Delete account, export data, cancel subscription
```

**Rules:**
- Danger zone always last — visually separated
- Group by what the user wants to accomplish, not by data model
- Labels use plain English: "Email me when someone mentions me" not "Notification trigger: mention"

---

## Pattern A — Sidebar + Content (standard)

Best for: settings with 5+ sections.

```html
<div class="settings-layout">
  <!-- Sidebar navigation -->
  <nav class="settings-nav" aria-label="Settings navigation">
    <ul>
      <li>
        <a href="/settings/profile"
           class="settings-nav__item settings-nav__item--active"
           aria-current="page">
          Profile
        </a>
      </li>
      <li>
        <a href="/settings/account" class="settings-nav__item">Account</a>
      </li>
      <li>
        <a href="/settings/notifications" class="settings-nav__item">Notifications</a>
      </li>
      <li>
        <a href="/settings/security" class="settings-nav__item">Security</a>
      </li>
      <li class="settings-nav__divider" role="separator"></li>
      <li>
        <a href="/settings/integrations" class="settings-nav__item">Integrations</a>
      </li>
      <li>
        <a href="/settings/danger" class="settings-nav__item settings-nav__item--danger">
          Danger zone
        </a>
      </li>
    </ul>
  </nav>

  <!-- Settings content area -->
  <main class="settings-content">
    <div class="settings-section">
      <header class="settings-section__header">
        <h1>Profile</h1>
        <p>Manage your personal information and preferences.</p>
      </header>
      <!-- Section content -->
    </div>
  </main>
</div>
```

```css
.settings-layout {
  display: grid;
  grid-template-columns: 1fr;
  min-height: calc(100dvh - var(--nav-height));
}

@media (min-width: 768px) {
  .settings-layout {
    grid-template-columns: 200px 1fr;
    gap: 0;
  }
}

/* Settings sidebar */
.settings-nav {
  padding: var(--space-6) var(--space-4);
  border-right: 1px solid var(--color-border);
}

.settings-nav ul {
  list-style: none;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
}

.settings-nav__item {
  display: block;
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-md);
  font-size: 0.9375rem;
  color: var(--color-text-secondary);
  text-decoration: none;
  transition: background 120ms, color 120ms;
}

.settings-nav__item:hover {
  background: var(--color-surface-2);
  color: var(--color-text-primary);
}

.settings-nav__item--active {
  background: var(--color-surface-2);
  color: var(--color-text-primary);
  font-weight: 500;
}

.settings-nav__item--danger { color: var(--color-error); }
.settings-nav__item--danger:hover { background: oklch(from var(--color-error) l c h / 0.08); }

.settings-nav__divider {
  height: 1px;
  background: var(--color-border);
  margin-block: var(--space-3);
}

/* Content area */
.settings-content {
  padding: var(--space-8) clamp(var(--space-6), 5vw, var(--space-16));
  max-width: 720px;
}

.settings-section__header {
  margin-bottom: var(--space-8);
  padding-bottom: var(--space-6);
  border-bottom: 1px solid var(--color-border);
}

.settings-section__header h1 {
  font-size: 1.5rem;
  margin-bottom: var(--space-2);
}

.settings-section__header p {
  color: var(--color-text-muted);
  font-size: 0.9375rem;
}
```

---

## Pattern B — Settings Form Row

The standard unit for settings: label + control + save.

```html
<!-- Save-on-change (toggle, select) -->
<div class="settings-row">
  <div class="settings-row__info">
    <label for="email-notifs" class="settings-row__label">
      Email notifications
    </label>
    <p class="settings-row__desc">
      Receive email summaries for activity in your projects.
    </p>
  </div>
  <div class="settings-row__control">
    <button
      id="email-notifs"
      class="toggle"
      role="switch"
      aria-checked="true"
      onclick="this.setAttribute('aria-checked', this.getAttribute('aria-checked') === 'true' ? 'false' : 'true')"
    >
      <span class="toggle__thumb" aria-hidden="true"></span>
      <span class="sr-only">Email notifications: on</span>
    </button>
  </div>
</div>

<!-- Save-on-submit (text input) -->
<div class="settings-row settings-row--form">
  <div class="settings-row__info">
    <label for="display-name" class="settings-row__label">Display name</label>
    <p class="settings-row__desc">This is how you appear to teammates.</p>
  </div>
  <div class="settings-row__control">
    <form action="/settings/profile" method="POST" class="settings-inline-form">
      <input id="display-name" name="display_name" type="text" value="Sarah Chen" />
      <button type="submit" class="btn-primary btn-sm">Save</button>
    </form>
  </div>
</div>
```

```css
.settings-row {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: var(--space-6);
  align-items: center;
  padding-block: var(--space-5);
  border-bottom: 1px solid var(--color-border);
}

.settings-row--form {
  grid-template-columns: 1fr;
  align-items: start;
}

@media (min-width: 640px) {
  .settings-row--form {
    grid-template-columns: 1fr 1fr;
  }
}

.settings-row__label {
  font-weight: 500;
  font-size: 0.9375rem;
  display: block;
  margin-bottom: var(--space-1);
}

.settings-row__desc {
  font-size: 0.875rem;
  color: var(--color-text-muted);
  line-height: 1.5;
}

.settings-inline-form {
  display: flex;
  gap: var(--space-3);
  align-items: center;
}

.settings-inline-form input {
  flex: 1;
  min-width: 0;
}
```

---

## Pattern C — Toggle Switch

Used for binary settings (on/off). Saves immediately.

```css
.toggle {
  position: relative;
  width: 44px;
  height: 24px;
  border-radius: 9999px;
  background: var(--color-surface-2);
  border: none;
  cursor: pointer;
  transition: background 200ms;
  flex-shrink: 0;
}

.toggle[aria-checked="true"] {
  background: var(--color-accent);
}

.toggle__thumb {
  position: absolute;
  top: 3px;
  left: 3px;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: white;
  box-shadow: 0 1px 3px oklch(0% 0 0 / 0.2);
  transition: transform 200ms cubic-bezier(0.16, 1, 0.3, 1);
}

.toggle[aria-checked="true"] .toggle__thumb {
  transform: translateX(20px);
}

.toggle:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 3px;
}
```

**Immediate save + confirmation:**
```tsx
async function handleToggle(setting: string, value: boolean) {
  // Optimistic update
  setSettings(prev => ({ ...prev, [setting]: value }))

  try {
    await updateSetting(setting, value)
    toast.success('Settings saved')
  } catch {
    // Revert on failure
    setSettings(prev => ({ ...prev, [setting]: !value }))
    toast.error('Failed to save. Try again.')
  }
}
```

---

## Pattern D — Danger Zone Section

Always last. Visually distinct. Every action here is irreversible or high-impact.

```html
<section class="settings-danger" aria-labelledby="danger-zone-heading">
  <header class="settings-danger__header">
    <h2 id="danger-zone-heading">Danger zone</h2>
  </header>

  <div class="danger-action">
    <div class="danger-action__info">
      <strong>Export your data</strong>
      <p>Download a complete copy of your account data, projects, and files.</p>
    </div>
    <button class="btn-ghost btn-sm" onclick="requestExport()">
      Export data
    </button>
  </div>

  <div class="danger-action">
    <div class="danger-action__info">
      <strong>Delete account</strong>
      <p>
        Permanently delete your account and all associated data.
        This cannot be undone.
      </p>
    </div>
    <button class="btn-destructive btn-sm" onclick="openDeleteDialog()">
      Delete account
    </button>
  </div>
</section>
```

```css
.settings-danger {
  margin-top: var(--space-16);
  border: 1px solid oklch(from var(--color-error) l c h / 0.35);
  border-radius: var(--radius-xl);
  overflow: hidden;
}

.settings-danger__header {
  background: oklch(from var(--color-error) l c h / 0.06);
  padding: var(--space-4) var(--space-6);
  border-bottom: 1px solid oklch(from var(--color-error) l c h / 0.2);
}

.settings-danger__header h2 {
  font-size: 1rem;
  color: var(--color-error);
}

.danger-action {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: var(--space-6);
  padding: var(--space-5) var(--space-6);
  border-bottom: 1px solid var(--color-border);
}

.danger-action:last-child { border-bottom: none; }

.danger-action__info strong { display: block; margin-bottom: var(--space-1); }
.danger-action__info p { font-size: 0.875rem; color: var(--color-text-muted); }

.btn-destructive {
  background: var(--color-error);
  color: white;
  /* All other button styles from btn-primary */
}

.btn-destructive:hover { filter: brightness(0.9); }
```

**Delete confirmation dialog (type-to-confirm pattern):**
```html
<dialog class="confirm-dialog" aria-labelledby="confirm-title">
  <h2 id="confirm-title">Delete your account?</h2>
  <p>
    This will permanently delete your account, 14 projects, and 3.2GB of files.
    <strong>This cannot be undone.</strong>
  </p>
  <label for="confirm-input">
    Type <strong>delete my account</strong> to confirm:
  </label>
  <input
    id="confirm-input"
    type="text"
    placeholder="delete my account"
    autocomplete="off"
  />
  <div class="confirm-dialog__actions">
    <button class="btn-ghost" onclick="this.closest('dialog').close()">Cancel</button>
    <button class="btn-destructive" id="confirm-delete-btn" disabled>
      Delete my account permanently
    </button>
  </div>
</dialog>
```

---

## API Keys Pattern

```html
<div class="api-keys-list">
  <div class="api-key-row">
    <div class="api-key-row__info">
      <strong class="api-key-row__name">Production</strong>
      <code class="api-key-row__value">sk-live-***...a2f8</code>
      <span class="api-key-row__meta">
        Created by Sarah Chen · Last used 2 hours ago
      </span>
    </div>
    <div class="api-key-row__actions">
      <button class="btn-ghost btn-sm">Copy key</button>
      <button class="btn-destructive btn-sm" onclick="revokeKey('production')">Revoke</button>
    </div>
  </div>
</div>

<button class="btn-primary btn-sm" onclick="createKey()">+ Create new key</button>
```

```css
.api-key-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: var(--space-4);
  padding-block: var(--space-4);
  border-bottom: 1px solid var(--color-border);
}

code.api-key-row__value {
  font-family: var(--font-mono);
  font-size: 0.875rem;
  background: var(--color-surface-2);
  padding: 0.2em 0.5em;
  border-radius: var(--radius-sm);
}

.api-key-row__meta {
  display: block;
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  margin-top: var(--space-1);
}

.api-key-row__actions {
  display: flex;
  gap: var(--space-2);
  flex-shrink: 0;
}
```

---

## Anti-Patterns

- Settings saved silently with no confirmation (user doesn't know if it worked)
- "Saved!" toast that fires every time a toggle is clicked (noisy)
- Destructive actions without confirmation dialogs
- Danger zone mixed in with other settings (not isolated at the bottom)
- Type-to-confirm with an unclear phrase (make it specific and predictable)
- API keys shown in full on the list page (show prefix+suffix only after creation)
- Password change requiring a page reload

## Related Files

- `rules/13-saas-products.md` — R8: Settings architecture
- `rules/12-admin-panels.md` — R6: Destructive operations friction levels
- `blueprints/saas-app-from-scratch.md` — Section 5: Settings screen
- `references/accessibility.md` — toggle switch ARIA, dialog focus management
