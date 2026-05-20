# Contributing

## What to contribute

High-value contributions:
- New patterns in `patterns/` with real-world variants
- Additional blueprints in `blueprints/` for project types not covered
- Improvement recipes in `recipes/` based on common problems
- Worked examples in `examples/` with clear rationale
- Agent refinements based on actual usage

Low-value contributions (please don't):
- Aesthetic opinions without rationale
- Patterns that duplicate existing ones
- Generic advice that doesn't add to existing rules
- Anything that contradicts the technology standards in `manifest.yaml`

---

## File standards

### All files follow this header:

```markdown
# Title

> One-sentence summary of what this file is for and when to use it.

---
```

### Rules files (`rules/`)

Structure:
```
# Rule: [Topic]
## Core principle (1-2 sentences)
## When this applies
## The rule with rationale
## Code examples (correct + incorrect)
## Common mistakes
## Checklist
```

### Pattern files (`patterns/`)

Structure:
```
# [Block] Patterns
## When to use this block
## Variants (named, with description)
## Required elements
## Anti-patterns
## Responsive behavior
## Accessibility requirements
## Code example (preferred variant)
```

### Blueprint files (`blueprints/`)

Structure:
```
# [Type] From Scratch
## When to use
## Questions to ask before starting
## Required sections/screens (ordered)
## UX rules for this type
## UI rules for this type
## Anti-patterns
## Related agents
## Related checklists
## Output format
```

---

## Code examples

- CSS: OKLCH for all colors — no hex unless brand-specified
- TypeScript: use `satisfies` for token objects
- React: React 19 patterns (`useActionState`, ref as prop)
- Next.js: 15 patterns (`await cookies()`, `"use cache"`)
- Motion: `motion/react` imports — not `framer-motion`
- GSAP: `useGSAP` hook pattern with `contextSafe()`
- Tailwind: v4 `@theme {}` pattern — no `tailwind.config.js`

---

## Pull request process

1. One PR per logical addition (one new pattern, one new rule, one recipe)
2. Test your addition by actually using it with Claude Code or Cursor
3. Include a brief description of what real problem this solved
4. Update `CHANGELOG.md`

---

## Philosophy

This is not a style guide. It is a decision framework. Every addition should answer: **"What decision does this help make, and how?"**

If your contribution only describes what something looks like — not why, when, and how to verify — it belongs elsewhere.
