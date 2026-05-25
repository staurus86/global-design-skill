# axe-core Accessibility Testing

## Thresholds

| Violation severity | Threshold | Action |
|-------------------|-----------|--------|
| critical | 0 | Block merge |
| serious  | 0 | Block merge |
| moderate | ≤ 3 | Warning, review required |
| minor    | any | Info only |

## Playwright Integration

```ts
// tests/a11y.spec.ts
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('homepage passes axe accessibility check', async ({ page }) => {
  await page.goto('/');
  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21aa'])
    .analyze();

  const critical = results.violations.filter(v => v.impact === 'critical');
  const serious  = results.violations.filter(v => v.impact === 'serious');

  expect(critical, `Critical violations: ${JSON.stringify(critical, null, 2)}`).toHaveLength(0);
  expect(serious,  `Serious violations: ${JSON.stringify(serious, null, 2)}`).toHaveLength(0);
});
```

## Jest Integration

```ts
// jest.setup.ts
import 'jest-axe/extend-expect';

// component.test.tsx
import { render } from '@testing-library/react';
import { axe } from 'jest-axe';
import { MyComponent } from './MyComponent';

it('has no accessibility violations', async () => {
  const { container } = render(<MyComponent />);
  expect(await axe(container)).toHaveNoViolations();
});
```
