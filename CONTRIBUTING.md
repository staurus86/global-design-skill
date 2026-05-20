# Contributing

This is a decision framework, not a style guide. Every contribution must answer: **"What decision does this help make, and how?"**

---

## What to contribute

**High value:**
- New patterns in `patterns/` — real-world variants with working code
- Additional blueprints in `blueprints/` for project types not covered
- New recipes in `recipes/` based on problems you actually solved
- Rule files filling gaps in `rules/` (03-typography, 04-color, 05-animation, 07-accessibility, 08-performance)
- Agent refinements based on real usage

**Low value (don't submit):**
- Aesthetic opinions without rationale or code
- Patterns that duplicate existing ones
- Generic advice without "when to use" and "what not to do"
- Anything using banned tech: `framer-motion`, `ease-in-out`, `100vh`, raw hex, `rgba()`

---

## File Standards

### Every file opens with:

```markdown
# [Title] — [Pattern | Rule | Recipe | Blueprint]

> One sentence: what this is for and when to use it.

---
```

### Rules (`rules/`)

```
# Rule: [Topic]
## R1 — [Rule name]
[Rationale in 1-2 sentences]
[Correct code example]
[Wrong code example — labeled "Before (wrong)"]
## Anti-patterns
## Acceptance criteria
```

### Patterns (`patterns/`)

```
# Pattern — [Block name]
> [One-sentence principle]
## Pattern A — [Name]
Best for: [specific scenario]
[HTML]
[CSS]
## Anti-Patterns
## Related Files
```

### Recipes (`recipes/`)

```
# Recipe — [Goal]
> [What this fixes]
## When to use
## Diagnosis: [Problem] Checklist
## Step 1 — [First action]
[Before / After code comparison]
## Acceptance Criteria
```

### Blueprints (`blueprints/`)

```
# [Type] From Scratch
> [One-line purpose]
## When to use
## Before you start: questions to answer
## Section/Screen [N]: [Name]
[HTML structure]
[CSS]
[Rationale]
## Anti-Patterns
## Related Files
```

---

## Code Standards

All code examples must follow the 2026 baseline:

| Area | Requirement |
|---|---|
| Colors | OKLCH only — `oklch(65% 0.22 258)` — no hex, no rgb() |
| Spacing | CSS custom properties — `var(--space-4)` — no raw px |
| Animation | Named cubic-bezier — `var(--ease-spring)` — no `ease-in-out` |
| Viewport height | `100dvh` — never `100vh` |
| Motion library | `motion/react` import — never `framer-motion` |
| Hover states | Wrapped in `@media (hover: hover)` |
| React | React 19 patterns — `useActionState`, `useOptimistic` |
| Next.js | v15 patterns — `await cookies()`, `"use cache"` |
| Tailwind | v4 `@theme {}` pattern |

**Verification:** Run your code example through `checklists/global-design-review.md` before submitting. It must pass all CRITICAL items.

---

## Naming Conventions

| Location | Format | Example |
|---|---|---|
| `rules/` | `NN-topic.md` (two-digit number) | `03-typography.md` |
| `patterns/[category]/` | `topic-patterns.md` | `form-patterns.md` |
| `recipes/` | `verb-object.md` | `improve-typography.md` |
| `blueprints/` | `type-from-scratch.md` | `ecommerce-from-scratch.md` |
| `agents/` | `role-name.md` | `seo-auditor.md` |
| `templates/[type]/` | `purpose.md` | `audit-report.md` |
| `checklists/` | `scope-review.md` | `ecommerce-review.md` |

---

## Pull Request Process

1. One PR per logical addition
2. Test by actually using it with Claude Code, Cursor, or another AI assistant
3. Include in description: what real problem this solved, what you tried first
4. Update `CHANGELOG.md` under `## Upcoming`
5. The PR title format: `[category] Add [name]` or `[category] Improve [name]`

**PR checklist:**
```
[ ] Code examples use OKLCH, CSS tokens, cubic-bezier
[ ] File has opening > quote describing when to use
[ ] Anti-patterns section present
[ ] No duplicate of existing content
[ ] Passes global-design-review.md CRITICAL checks
[ ] CHANGELOG.md updated
```

---

## Philosophy

If your contribution only describes what something looks like — not **why**, **when**, and **how to verify** — it belongs elsewhere.

The test: could a developer implement your pattern correctly after reading it, without asking a single question? If yes, it's ready.
