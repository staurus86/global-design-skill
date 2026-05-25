# Demo Gallery

Eight self-contained Before/After redesign demos using global-design-skill.

## Token Update Protocol

`demo/tokens.css` is the single source of truth for design tokens. Tokens are
duplicated into each demo file for self-containment (no build step, GitHub Pages ready).

To update a token value across all demo files, run from the repo root:

```bash
# Portable — works on macOS and Linux
sed -i'' 's/--color-accent: oklch(52% 0.20 258)/--color-accent: oklch(NEW_VALUE)/g' demo/*.html
```

Use the same pattern for any other token — replace the property name and old value accordingly.

Never edit token values in individual demo files directly.

## Files

| File | Wave | Component |
|------|------|-----------|
| `index.html` | — | Gallery page |
| `hacker-news.html` | 1 | HN Story List Item |
| `stack-overflow.html` | 1 | SO Question Card |
| `github-pr.html` | 1 | GitHub PR Card |
| `npm-package.html` | 2 | npm Package Card |
| `mdn-api.html` | 2 | MDN API Method Block |
| `product-hunt.html` | 2 | Product Hunt Listing |
| `caniuse-table.html` | 3 | Can I Use Browser Table |
| `devto-card.html` | 3 | Dev.to Article Card |
