# Bundle Size Limits

## Size Targets Per Component Type

| Component type | Max JS (gzipped) | Notes |
|---------------|-----------------|-------|
| Leaf component (Button, Input) | 2 KB | No external deps |
| Composite component (Form, Modal) | 8 KB | Shared chunks excluded |
| Page component | 30 KB | First load JS |
| Full application shell | 80 KB | Initial bundle |
| Third-party library (single) | 20 KB | Prefer tree-shakeable |

## Next.js Bundle Analysis

```bash
ANALYZE=true npm run build
```

`next.config.ts`:

```ts
import BundleAnalyzer from '@next/bundle-analyzer';

const withBundleAnalyzer = BundleAnalyzer({
  enabled: process.env.ANALYZE === 'true',
});

export default withBundleAnalyzer({ /* your config */ });
```

## Tree-Shaking Checklist

- [ ] Import named exports only: `import { Button } from './ui'` not `import * as UI`
- [ ] No `export default` on libraries — use named exports
- [ ] `sideEffects: false` in `package.json` for component libraries
- [ ] Check with: `npx webpack-bundle-analyzer stats.json`
