# Example — Settings Page (App)

> **Before:** A long single-column form with every setting on one page. No navigation, no section grouping, unrelated settings next to each other.  
> **After:** Vertical tab navigation with categorized sections, each section independently scrollable, all forms following the error/validation recipe.

---

## Before

```html
<!-- Flat settings dump — all in one form, no grouping -->
<div style="max-width: 600px; margin: 40px auto; padding: 0 20px;">
  <h1>Settings</h1>

  <input type="text" placeholder="Your name" style="display: block; width: 100%; margin: 10px 0; padding: 8px; border: 1px solid #ccc;" />
  <input type="email" placeholder="Email address" style="display: block; width: 100%; margin: 10px 0; padding: 8px; border: 1px solid #ccc;" />
  <input type="text" placeholder="Company name" style="display: block; width: 100%; margin: 10px 0; padding: 8px; border: 1px solid #ccc;" />
  <input type="tel" placeholder="Phone" style="display: block; width: 100%; margin: 10px 0; padding: 8px; border: 1px solid #ccc;" />

  <hr />

  <input type="checkbox" id="marketing" />
  <label for="marketing">Receive marketing emails</label>
  <br /><br />
  <input type="checkbox" id="weekly" />
  <label for="weekly">Weekly digest</label>

  <hr />

  <button>Save Changes</button>
  <button style="color: red; background: none; border: none;">Delete Account</button>
</div>
```

**Problems:**
- No navigation — user can't find specific settings
- Hardcoded inline styles — no tokens
- "Delete Account" next to "Save" — dangerous proximity
- No form labels properly associated
- No validation or error states

---

## After

```html
<div class="settings-layout">

  <!-- Vertical tab nav (see patterns/navigation/tabs-patterns.md Pattern 3) -->
  <nav class="settings-nav" role="tablist" aria-label="Settings" aria-orientation="vertical">
    <a href="#profile"       class="settings-nav__item settings-nav__item--active" role="tab" aria-selected="true"  aria-controls="panel-profile"   id="tab-profile">Profile</a>
    <a href="#notifications" class="settings-nav__item" role="tab" aria-selected="false" aria-controls="panel-notifications" id="tab-notifications" tabindex="-1">Notifications</a>
    <a href="#security"      class="settings-nav__item" role="tab" aria-selected="false" aria-controls="panel-security"      id="tab-security"  tabindex="-1">Security</a>
    <a href="#billing"       class="settings-nav__item" role="tab" aria-selected="false" aria-controls="panel-billing"       id="tab-billing"   tabindex="-1">Billing</a>
    <a href="#team"          class="settings-nav__item" role="tab" aria-selected="false" aria-controls="panel-team"          id="tab-team"      tabindex="-1">Team</a>
    <div class="settings-nav__separator" aria-hidden="true"></div>
    <a href="#danger"        class="settings-nav__item settings-nav__item--danger" role="tab" aria-selected="false" aria-controls="panel-danger" id="tab-danger" tabindex="-1">Danger zone</a>
  </nav>

  <!-- Content panels -->
  <div class="settings-panels">

    <!-- Profile -->
    <div class="settings-panel" role="tabpanel" id="panel-profile" aria-labelledby="tab-profile">
      <div class="settings-section">
        <div class="settings-section__header">
          <h2 class="settings-section__heading">Profile</h2>
          <p class="settings-section__desc">Your personal information and public identity.</p>
        </div>

        <form class="settings-form" novalidate>

          <!-- Avatar -->
          <div class="settings-row">
            <div class="settings-row__label">
              <label class="field-label">Profile photo</label>
            </div>
            <div class="settings-row__control">
              <div class="avatar-upload">
                <img src="/avatar.jpg" alt="Alex Kim" class="avatar-upload__img" width="64" height="64" />
                <button class="btn btn--ghost btn--sm" type="button">Change photo</button>
              </div>
            </div>
          </div>

          <div class="settings-divider" aria-hidden="true"></div>

          <!-- Name + email -->
          <div class="settings-row">
            <div class="settings-row__label">
              <label class="field-label" for="full-name">Full name</label>
            </div>
            <div class="settings-row__control">
              <input class="field-input field-input--md" type="text" id="full-name"
                name="full_name" autocomplete="name" value="Alex Kim" />
            </div>
          </div>

          <div class="settings-divider" aria-hidden="true"></div>

          <div class="settings-row">
            <div class="settings-row__label">
              <label class="field-label" for="email">Email address</label>
              <p class="field-hint">Used for login and notifications.</p>
            </div>
            <div class="settings-row__control">
              <input class="field-input field-input--md" type="email" id="email"
                name="email" autocomplete="email" value="alex@example.com" />
            </div>
          </div>

          <!-- Form footer -->
          <div class="settings-form__footer">
            <button class="btn btn--primary" type="submit">Save changes</button>
          </div>

        </form>
      </div>
    </div>

    <!-- Danger zone — separate panel, separate form -->
    <div class="settings-panel" role="tabpanel" id="panel-danger" aria-labelledby="tab-danger" hidden>
      <div class="settings-section settings-section--danger">
        <div class="settings-section__header">
          <h2 class="settings-section__heading settings-section__heading--danger">Danger zone</h2>
          <p class="settings-section__desc">Irreversible actions. Read carefully.</p>
        </div>

        <div class="danger-action">
          <div>
            <p class="danger-action__title">Delete account</p>
            <p class="danger-action__desc">
              Permanently deletes your account, all projects, and all associated data.
              This cannot be undone.
            </p>
          </div>
          <button class="btn btn--danger btn--sm" type="button"
            data-confirm="delete-account">
            Delete account
          </button>
        </div>
      </div>
    </div>

  </div>
</div>
```

```css
.settings-layout {
  display: grid;
  grid-template-columns: 220px 1fr;
  gap: var(--space-10);
  max-width: 900px;
  margin-inline: auto;
  padding: var(--space-8) var(--space-6);
  min-height: 100dvh;
  align-items: start;
}

/* Nav */
.settings-nav {
  position: sticky;
  top: var(--space-8);
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
}

.settings-nav__item {
  display: flex;
  align-items: center;
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-md);
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-secondary);
  text-decoration: none;
  transition: background var(--duration-fast) var(--ease-smooth), color var(--duration-fast) var(--ease-smooth);
}

.settings-nav__item:hover { background: var(--color-surface-2); color: var(--color-text-primary); }
.settings-nav__item--active {
  background: var(--color-accent-subtle);
  color: var(--color-accent-text);
  font-weight: var(--font-weight-semibold);
}

.settings-nav__item--danger { color: var(--color-danger); }
.settings-nav__item--danger:hover { background: var(--color-danger-subtle); }

.settings-nav__separator {
  height: 1px;
  background: var(--color-border);
  margin-block: var(--space-2);
}

/* Panels */
.settings-panel[hidden] { display: none; }

.settings-section {
  display: flex;
  flex-direction: column;
  gap: var(--space-8);
}

.settings-section__header { display: flex; flex-direction: column; gap: var(--space-2); }

.settings-section__heading {
  font-size: var(--text-h3);
  font-weight: var(--font-weight-semibold);
  color: var(--color-text-primary);
}

.settings-section__heading--danger { color: var(--color-danger); }
.settings-section__desc { font-size: var(--text-sm); color: var(--color-text-secondary); }

/* Two-column row layout */
.settings-form { display: flex; flex-direction: column; }

.settings-row {
  display: grid;
  grid-template-columns: 1fr 1.5fr;
  gap: var(--space-8);
  align-items: start;
  padding-block: var(--space-5);
}

.settings-row__label { display: flex; flex-direction: column; gap: var(--space-1); }
.settings-divider { height: 1px; background: var(--color-border); }

.settings-form__footer {
  padding-top: var(--space-6);
  border-top: 1px solid var(--color-border);
  display: flex;
  justify-content: flex-end;
}

/* Danger section */
.settings-section--danger {
  border: 1px solid var(--color-danger-subtle);
  border-radius: var(--radius-xl);
  padding: var(--space-6);
  background: oklch(from var(--color-danger) l c h / 0.03);
}

.danger-action {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-6);
  padding: var(--space-5);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
}

.danger-action__title {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-semibold);
  color: var(--color-text-primary);
}

.danger-action__desc {
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  line-height: 1.5;
  max-width: 40ch;
}

/* Avatar upload */
.avatar-upload {
  display: flex;
  align-items: center;
  gap: var(--space-4);
}

.avatar-upload__img {
  width: 56px; height: 56px;
  border-radius: var(--radius-full);
  object-fit: cover;
}

@media (max-width: 768px) {
  .settings-layout { grid-template-columns: 1fr; }
  .settings-nav { position: static; flex-direction: row; overflow-x: auto; scrollbar-width: none; }
  .settings-row { grid-template-columns: 1fr; }
}
```

---

## Before/After Comparison

| Element | Before | After |
|---|---|---|
| Navigation | None — everything on one page | Vertical tabs by category |
| Layout | Single column | Two-column row (label + control) |
| Dangerous actions | Next to Save button | Separate panel, bottom of nav |
| Styles | Inline, hardcoded | Token-based |
| Labels | Placeholder-only | Associated `<label>` elements |
| Mobile | Broken single column | Horizontal nav + stacked rows |

---

*Example version: global-design-skill v1.0 — `examples/apps/01-settings-page.md`*  
*Related: `patterns/navigation/tabs-patterns.md`, `patterns/product-ui/forms.md`, `rules/10-forms.md`*
