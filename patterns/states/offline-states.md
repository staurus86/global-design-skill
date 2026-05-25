# Offline States

Use when: `navigator.onLine === false` or network-level failure detected.

## Pattern: Offline Banner

Persistent, dismissible banner at top of page:

```html
<div role="status" aria-live="polite" class="banner banner--offline">
  <span aria-hidden="true">📶</span>
  You are offline. Some features may not be available.
  Last synced: <time datetime="2026-05-25T09:45:00Z">9:45 AM</time>
</div>
```

## Pattern: Sync Queue Indicator

Show pending actions queued for when connection returns:

```html
<div class="sync-queue" aria-label="3 changes pending sync">
  <span class="sync-queue__count">3</span> unsaved changes
  will sync when you're back online.
</div>
```

## Rules
- Show offline state within 2 seconds of connection loss.
- Always show the last sync time so users know how stale cached data is.
- Disable (not hide) actions that require network — show tooltip explaining why.
- Automatically dismiss banner and trigger sync on reconnect.
- Announce reconnection to screen readers via `aria-live="polite"`.
