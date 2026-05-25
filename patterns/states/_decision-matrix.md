# State Decision Matrix

This file extends the existing 9-state system (idle / hover / active / focus /
disabled / loading / empty / error / success) with 5 additional states.

No existing states are replaced. The matrix below determines which state to use
when multiple options are applicable.

## When to Use Each State

| State | Trigger condition | Typical duration | Example |
|-------|------------------|-----------------|---------|
| `loading` (spinner) | Wait < 1s, data volume unknown, no structure predictable | Short | Form submit, auth check |
| `skeleton` | Wait > 1s AND content structure is known before data arrives | Medium (1–10s) | Product list, article feed, user profile |
| `partial-error` | Main content loaded successfully; a subset of data failed | Persistent until retry | Table with 2/10 rows errored, dashboard widget unavailable |
| `offline` | Network connection lost, PWA or offline-capable app | Until reconnect | Dashboard with stale cached data |
| `permission` | User authenticated but lacks access to this resource | Persistent | Locked plan feature, role-restricted section |
| `rate-limit` | Too many requests sent; server returned 429 | Timed (until cooldown expires) | API quota exhausted, search throttled |

## Decision Rules

**loading vs skeleton:**
- Use `skeleton` when you know the layout before the data (e.g. a list of cards will have a title, subtitle, and image).
- Use `loading` when the result shape is unknown (e.g. an AI-generated response, a form validation result).
- Never show both for the same element simultaneously.

**error vs partial-error:**
- Use `error` when the entire component or page failed to load.
- Use `partial-error` when some data loaded and some did not — the user can still use part of the UI.

**offline vs error:**
- Use `offline` when `navigator.onLine === false` or the app detects a network-level failure.
- Use `error` for server errors (5xx) or application errors when the network is available.

**permission vs disabled:**
- Use `disabled` for UI controls that are not available in the current context or state (e.g. submit button before form is valid).
- Use `permission` for entire features or pages the user cannot access due to role or plan.
