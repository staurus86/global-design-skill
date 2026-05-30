# Golden output — o03: form accessibility audit

**Prompt:** "Use global-design-skill accessibility-auditor on this form: name field, email field, submit button. No labels visible."

---

## What a correct response must include

### 1. Severity matrix

Must structure findings as a severity matrix — `critical` / `major` / `minor` — not a flat list. Missing labels is **critical** (blocks screen-reader users).

### 2. Labels

Must flag the missing `label` as the top issue and prescribe the fix:
> Each input needs a visible `<label>` linked via `for`/`id`. Placeholder text is not a label — it disappears on input and fails WCAG 2.2.

### 3. ARIA and programmatic state

Must specify `aria` usage where native semantics are insufficient:
- `aria-invalid="true"` on fields in error
- `aria-describedby` linking the field to its error message
- `aria-live="polite"` region for validation feedback

### 4. Focus

Must require a visible `focus`-visible ring on every field and the submit button — never `outline: none` without a custom replacement.

### 5. Error states

Must specify `error` handling: error text below the field, neutral tone, specific recovery, color never the sole signal (icon + text).

### 6. Contrast and target size

Must check `contrast` (4.5:1 text, 3:1 UI/borders) and tap target ≥ `44px` for the submit button and any clear/clickable affordances.

### 7. WCAG citation

Must cite specific WCAG 2.2 success criteria (e.g., 1.3.1 Info and Relationships, 3.3.2 Labels or Instructions, 2.4.7 Focus Visible, 1.4.3 Contrast).

### 8. Gate compliance

Must satisfy Gate 4 (states) and Gate 6 (accessibility).

---

## What a correct response must NOT include

- A vague "improve accessibility" with no criteria or severities
- Color-only error signalling
- Removing the focus outline without a visible replacement
