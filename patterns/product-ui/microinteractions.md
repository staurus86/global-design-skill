# Pattern — Microinteractions

> A microinteraction is a single, contained moment built around one task: toggle a setting, like a post, validate a field, copy a value. `rules/05-animation.md` governs the *mechanics* (timing, easing, GPU); this file governs the *anatomy* — what a microinteraction is made of and how to design one that communicates rather than decorates.

---

## The Anatomy — Trigger · Rules · Feedback · Loops & Modes

Every microinteraction decomposes into four parts (Dan Saffer's model). Name all four before writing code; if you can't, the interaction is under-specified.

| Part | Question it answers | Example (toggle a setting) |
|---|---|---|
| **Trigger** | What starts it? (user action or system event) | User clicks the switch |
| **Rules** | What happens, and what's allowed? | State flips on → off; disabled while a save is in flight |
| **Feedback** | How does the user know it worked? | Thumb slides, track recolors, optimistic save |
| **Loops & Modes** | What happens over time / in edge states? | Reverts + inline error if the save fails |

**Rule:** Feedback is mandatory and immediate — a state change with no perceptible feedback inside 100ms reads as a broken control (Doherty Threshold). Loops & Modes are where most interactions fail: the happy path animates, the error path snaps.

---

## When a moment deserves a microinteraction

| Signal | Add one? |
|---|---|
| State changes the user caused (toggle, like, select, copy) | Yes — confirm the change happened |
| Validation, success, or failure of a discrete action | Yes — feedback is the whole point |
| Status that changes without user action (sync, presence) | Yes — a quiet ambient signal |
| Decorative motion with no state behind it | No — that's effects, not a microinteraction |
| Inside a dense data table / high-density admin view | Minimal — confirmation only, no flourish |

Tie loudness to `MOTION_INTENSITY` (`rules/00-escalation-protocol.md`): a productivity app keeps these near-invisible; a marketing surface can make them signature moments.

---

## Pattern A — Action confirmation (toggle, like, copy)

The state change *is* the feedback. Animate the element that changed, not a separate indicator.

```css
.toggle {
  cursor: pointer;
  transition: background-color 150ms var(--ease-out);
}
.toggle__thumb {
  transition: translate 150ms var(--ease-spring);
}
.toggle[aria-checked="true"] {
  background-color: var(--color-accent);
}
.toggle[aria-checked="true"] .toggle__thumb { translate: 100% 0; }

/* Copy button: the label confirms, the icon doesn't need to spin */
.copy-btn[data-copied="true"]::after { content: "Copied"; }
```

**Optimistic UI rule:** reflect the change instantly, reconcile with the server in the background. On failure, run the Loop — revert the visual and surface the reason (`patterns/product-ui/notifications.md`).

---

## Pattern B — Inline validation feedback

Trigger on `blur`, not on every keystroke. Feedback states map to color *and* an icon/text (never color alone — `rules/07-accessibility.md`).

```css
.field[data-state="valid"]   { border-color: var(--color-success); }
.field[data-state="invalid"] { border-color: var(--color-error); }
.field__msg {
  opacity: 0;
  transition: opacity 200ms var(--ease-out);
}
.field[data-state="invalid"] .field__msg { opacity: 1; }
```

Loops & Modes: clear the error the instant the user starts correcting it — don't make them re-submit to discover they fixed it.

---

## Pattern C — Ambient status (sync, presence, progress)

System-triggered, no user action. Keep it quiet and continuous; it informs, it doesn't demand.

```css
.sync-dot[data-state="syncing"] {
  animation: pulse 1.2s var(--ease-in-out) infinite;
}
@media (prefers-reduced-motion: reduce) {
  .sync-dot[data-state="syncing"] { animation: none; }
  .sync-dot[data-state="syncing"]::after { content: " syncing…"; }  /* text fallback */
}
```

---

## Timing & easing (defaults)

| Interaction | Duration | Easing |
|---|---|---|
| Toggle / button press / hover | 120–150ms | `var(--ease-out)` or spring |
| Validation / inline reveal | 200ms | `var(--ease-out)` |
| Ambient loop (pulse, breathe) | 1–1.4s | `var(--ease-in-out)` |

Aligns with `checklists/global-design-review.md` 8.6 (micro < 150ms). Never `transition: all` and never `ease-in-out` as a default on user-triggered motion (`rules/05-animation.md` R2).

---

## Anti-Patterns

- State change with no feedback inside 100ms (control feels dead)
- The success path animates but the error path snaps with no explanation (missing Loop)
- Validation fires on every keystroke instead of on `blur`
- Color-only feedback with no icon/text (fails colorblind users)
- A spinner or confetti where a 150ms state change would do (decoration, not communication)
- Ambient loops with no `prefers-reduced-motion` fallback

---

## Acceptance Criteria

```
[ ] Trigger, Rules, Feedback, and Loops & Modes all named before build
[ ] Feedback perceptible within 100ms of the trigger
[ ] Error / failure path designed, not just the happy path
[ ] Feedback uses more than color (icon or text)
[ ] prefers-reduced-motion path provided for any looping animation
[ ] Loudness matches MOTION_INTENSITY for the surface
```

## Related Files

- `rules/05-animation.md` — timing, easing, GPU-safe properties
- `rules/17-motion-react.md` — `motion/react` implementation for React surfaces
- `rules/00-escalation-protocol.md` — `MOTION_INTENSITY` dial
- `patterns/effects/hover-effects.md` — hover-specific microinteractions
- `patterns/product-ui/notifications.md` — surfacing the failure Loop
- `patterns/product-ui/forms.md` — validation feedback in context
