---
applyTo: "industries/*.md"
---

# Industry Sector File Rules

Every `industries/*.md` file (except `_index.md`) must start with:

```yaml
---
version: 1.0.0
last_updated: YYYY-MM-DD
source: manual
stale_after_days: 90
---
```

Required sections (9):
1. Sector Profile
2. Mobile Rules
3. Required Elements
4. Banned Patterns
5. Trust Signals
6. Conversion Path
7. Page Structure
8. Quick Diagnosis
9. Disambiguation

After any change, run: `python scripts/validate-industries.py`
