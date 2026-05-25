# Partial Error States

Use when: main content loaded; a subset of data failed.

## Pattern: Inline Error Row

For tables or lists where some rows failed to load:

```html
<tr class="row--error" aria-label="Row failed to load">
  <td colspan="4">
    <span class="error-icon" aria-hidden="true">⚠</span>
    Failed to load data for this item.
    <button type="button" onclick="retryRow(id)">Retry</button>
  </td>
</tr>
```

```css
.row--error { background: var(--color-error-surface); }
```

## Pattern: Degraded-Mode Banner

For dashboard widgets or sections that loaded partially:

```html
<div role="alert" class="banner banner--warning">
  Some data could not be loaded. Showing cached results from
  <time datetime="2026-05-25T10:00:00Z">10:00 AM</time>.
  <button type="button">Retry</button>
</div>
```

## Rules
- Always show what DID load — do not blank the whole component.
- Provide a retry action per failed unit, not just a global page refresh.
- Show the timestamp of the last successful data if displaying cached content.
- Never use red for a partial error that does not require user action.
