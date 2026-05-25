# Rate Limit States

Use when: server returns 429 or the app enforces a client-side quota.

## Pattern: Cooldown Timer

```html
<div role="alert" aria-live="assertive" class="rate-limit-notice">
  <p>Too many requests. Try again in
    <strong><time id="cooldown-timer">0:45</time></strong>.
  </p>
</div>
```

```js
function startCooldown(seconds) {
  const el = document.getElementById('cooldown-timer');
  const end = Date.now() + seconds * 1000;

  const tick = () => {
    const remaining = Math.ceil((end - Date.now()) / 1000);
    if (remaining <= 0) {
      el.closest('[role="alert"]').hidden = true;
      return;
    }
    const m = Math.floor(remaining / 60);
    const s = remaining % 60;
    el.textContent = `${m}:${s.toString().padStart(2, '0')}`;
    setTimeout(tick, 1000);
  };
  tick();
}
```

## Pattern: Quota Progress Bar

For API plans with monthly limits:

```html
<div class="quota-meter" role="meter" aria-valuenow="850"
     aria-valuemin="0" aria-valuemax="1000"
     aria-label="API calls this month: 850 of 1000">
  <div class="quota-meter__fill" style="width: 85%"></div>
  <span>850 / 1000 API calls used</span>
</div>
```

## Rules
- Always show the exact remaining wait time, not "please wait".
- Disable the triggering action for the duration of the cooldown.
- Provide an upgrade path when rate limit is a plan constraint.
- Never silently drop requests — always inform the user.
