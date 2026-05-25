# Lighthouse CI Integration

## Performance Budgets

| Metric | Target | Fail threshold |
|--------|--------|---------------|
| LCP (Largest Contentful Paint) | < 2.5s | > 4s |
| CLS (Cumulative Layout Shift) | < 0.1 | > 0.25 |
| FID / INP | < 100ms | > 300ms |
| Performance score | ≥ 90 | < 75 |
| Accessibility score | ≥ 90 | < 80 |
| Best Practices score | ≥ 90 | < 80 |

## CI Configuration (GitHub Actions)

```yaml
# .github/workflows/lighthouse.yml
name: Lighthouse CI
on: [push, pull_request]
jobs:
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - run: npm ci
      - run: npm run build
      - uses: treosh/lighthouse-ci-action@v11
        with:
          urls: |
            http://localhost:3000
            http://localhost:3000/pricing
          budgetPath: ./lighthouse-budget.json
          uploadArtifacts: true
```

`lighthouse-budget.json`:

```json
[
  {
    "path": "/*",
    "timings": [
      { "metric": "largest-contentful-paint", "budget": 2500 },
      { "metric": "cumulative-layout-shift",  "budget": 0.1 },
      { "metric": "interactive",              "budget": 5000 }
    ],
    "audits": [
      { "id": "uses-optimized-images",     "warn": 0 },
      { "id": "render-blocking-resources", "warn": 0 }
    ]
  }
]
```

## Running Locally

```bash
npm install -g @lhci/cli
lhci autorun --collect.url=http://localhost:3000
```
