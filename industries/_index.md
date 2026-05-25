# Industries Index

This directory maps 13 business sectors to design rules. AI tools read this
index first, then load the relevant sector file for the current request.

## Routing Logic

When a user request mentions a business context, determine the sector:

1. B2B product or service (equipment, SaaS, consulting, logistics) → `b2b-products.md`
2. Physical consumer product (bicycles, electronics, furniture) → `b2c-products.md`
3. Consumer service (therapy, cleaning, fitness, tarot) → `services.md`
4. Content or media publication → `content-media.md`
5. Course, training, or school → `education.md`
6. Medical, clinic, or wellness → `health.md`
7. Banking, insurance, fintech → `finance.md`
8. Property, rental, construction → `real-estate.md`
9. Hotel, tour, restaurant, travel → `travel.md`
10. Software product, SaaS, AI tool, developer tool → `tech-saas.md`
11. NGO, charity, foundation → `non-profit.md`
12. Government portal, civic service → `government.md`
13. Game, streaming, event, sports → `entertainment.md`

## Disambiguation

- SaaS sold to businesses → `b2b-products.md` if buyer is procurement/engineering;
  `tech-saas.md` if buyer is developer or power user
- Medical service → `health.md` not `services.md`
- No match → use generic rules from `rules/` and `blueprints/`

## Integration

This file is referenced from `integrations/claude-code/CLAUDE.md`.
Load the matching sector file before generating any design output.
