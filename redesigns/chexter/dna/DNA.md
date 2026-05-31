# Design DNA — chexter.ru (seed)

> Зафиксировано после гейта S2 (2026-05-31). Дорабатывается в S3 (референсы) и подтверждается Junior Pass до полной сборки S4.

## Выбранное направление
**C. Living Diagnostics** — школа **Motion Poetics** (анкор: Field.io / generative systems).
Применяемый блюпринт: `blueprints/interactive-landing-page.md` + `rules/17-motion-react.md`.

## Визуальная метафора (Memorability Gate #1)
**Рентген / живой сканер сайта.** Сайт «просвечивается» на глазах: hero показывает, как chexter
смотрит на URL «глазами AI и Google». Метафора ведёт навигацию, форму карточек, моушн и копирайтинг.

## One Memorable Thing (Memorability Gate #2)
Hero, который **живьём «сканирует» введённый URL** scan-line'ом и достраивает метрики (SEO/GEO/Speed)
последовательно по скроллу. Это то, что вспомнят через 3 дня — не «ещё один каталог SEO-инструментов».

## Макроструктура (Macrostructure-First)
**Narrative-scroll** — одна идея на вьюпорт, scroll-driven последовательность:
1. Hero-сканер (URL → живой просвет)
2. «Что видит AI» (GEO-слой, отличие от классики)
3. Метрики достраиваются по скроллу (data-viz builds)
4. 16 инструментов как «приборы» сканера
5. Доверие/методология → CTA

НЕ дефолтный centered-hero → 3-feature-grid → pricing → footer (это и есть slop-скелет).

## Дилы (rules/00)
| Дил | Значение |
|---|---|
| DESIGN_VARIANCE | 7 (передовой, неожиданный) |
| MOTION_INTENSITY | 7 (scroll-driven, scan-line, stagger) |
| VISUAL_DENSITY | 4 (баланс: моушн важнее плотности) |

## Токены (база — развить в S3, OKLCH-only)
Опора на брендбук Data Teal, переведённый в OKLCH + тёмная атмосфера:
- accent (electric blue #1E63FF) → `oklch(~58% 0.20 264)`
- teal (#18D4D0) → `oklch(~80% 0.13 195)` — сигнальный/scan-акцент
- navy bg (#0B1633) → `oklch(~18% 0.04 264)` — тёмная база
- glow/scan — teal на navy, `@property` + radial-gradient, scan-line через clip-path/keyframes

## Обязательные предохранители моушна (Effects Decision Block, Step 4)
- `prefers-reduced-motion`: вся анимация выключается (статичный fallback hero обязателен)
- Анимировать только `transform`/`opacity`; никаких `top/left`; `will-change` точечно
- CLS = 0 от поздних эффектов; mobile 390px без горизонтального скролла
- Lighthouse mobile ≥ 88; motion budget: CSS + IntersectionObserver, GSAP ScrollTrigger только если нужен pin
- No-JS / краулер-слой: scan — декоративный, контент и форма работают без JS

## Открытый блокер
PHP локально нет → «после» = статический HTML-прототип (`redesign/after/home.html`), рендер Playwright.
Порт в PHP-вьюхи — отдельный этап S6.
