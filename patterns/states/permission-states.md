# Permission States

Use when: user is authenticated but cannot access a feature due to plan or role.

## Pattern: Locked Feature (upgrade path)

```html
<div class="feature--locked" aria-label="Feature requires Pro plan">
  <div class="feature__preview" aria-hidden="true">
    <!-- blurred or greyed preview of the feature -->
  </div>
  <div class="feature__gate">
    <h3>Available on Pro</h3>
    <p>Unlock advanced analytics and custom exports.</p>
    <a href="/upgrade" class="btn btn--primary">Upgrade to Pro</a>
    <a href="/compare-plans">Compare plans</a>
  </div>
</div>
```

## Pattern: Role-Restricted Section

```html
<div role="alert" class="permission-notice">
  <p>You don't have permission to view this section.</p>
  <p>Contact your workspace admin to request access.</p>
</div>
```

## Rules
- Never hide locked features — always show them with a clear unlock path.
- Distinguish between "upgrade required" (commercial) and "admin approval required" (role).
- Do not use `disabled` attribute on entire sections — use `aria-disabled` and the permission pattern.
- Show a preview (blurred or reduced) to communicate the value before the gate.
