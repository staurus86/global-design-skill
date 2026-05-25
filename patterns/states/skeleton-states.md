# Skeleton States

Use when: wait > 1s AND content structure is known before data arrives.

## Variants

### Shimmer (recommended default)
A gradient animation moves left-to-right across the placeholder shape.
Conveys that loading is active and progressive.

```css
@keyframes shimmer {
  0%   { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

.skeleton {
  background: linear-gradient(
    90deg,
    var(--color-surface-2) 25%,
    var(--color-surface-3) 50%,
    var(--color-surface-2) 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: var(--radius-sm);
}
```

### Pulse
The entire placeholder fades in and out. Use when shimmer is too distracting
(e.g. dense data tables).

```css
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0.4; }
}

.skeleton--pulse {
  background: var(--color-surface-2);
  animation: pulse 1.5s ease-in-out infinite;
}
```

## Skeleton Structure Rules
- Match the skeleton shape to the real content dimensions (height, width, line count).
- Use `border-radius` to match card or avatar radius.
- Show at least 3 placeholder items in a list to convey list structure.
- Do not show a spinner AND skeleton simultaneously for the same element.
- Respect `prefers-reduced-motion`: remove animation, keep static placeholder shape.

```css
@media (prefers-reduced-motion: reduce) {
  .skeleton, .skeleton--pulse {
    animation: none;
  }
}
```

## Accessibility
- Wrap skeleton region in `aria-busy="true"` and `aria-label="Loading content"`.
- Remove `aria-busy` once content loads.
- Do not use `role="status"` on the skeleton itself — use it on a visually-hidden live region that announces completion.
