# Журнал дизайн-решений — sk-seo.ru (2026-05-30)

> Что меняю, почему, какой принцип/gate global-design-skill это закрывает. Источник для обновления скила.
> Контекст: vanilla HTML/CSS/JS, тёмная тема, прод проиндексирован — URL и структуру не ломаю, правки хирургические.
> Бэкап каждого файла: `C:\Opencode-test\Kirichenko\.backups\2026-05-30\`. Скриншоты: `before/` и `after/` (10 страниц × desktop 1440 + mobile 390).

## Принятые решения

| # | Файл | Что изменил | Почему / принцип скила | Тип |
|---|------|-------------|------------------------|-----|
| 1 | `404.html` | Добавил header/footer-партиалы, skip-link, `id="main"`, расширил навигацию до 4 кнопок (Главная/Услуги/Инструменты/Блог), `100vh→100dvh` (+fallback), `meta referrer` | Gate 2 (IA): 404 — точка удержания, нужны пути наружу; Banned `100vh`; единообразие с сайтом | structure / a11y |
| 2 | `services.html` | «Стоимость — по запросу» → «Цены — ниже, фиксированные, без «согласуем позже»»; «SEO — это марафон, не спринт» → «накопительный канал: эффект растёт месяцами и держится после остановки работ» — синхронно в видимом FAQ и в JSON-LD FAQPage | Убрал когнитивный диссонанс (цены видны на карточках) + Banned-конструкция «X, не Y» / клише; правило «schema зеркалит видимый текст» | anti-slop / trust |
| 3 | `css/base.css` | `@media (forced-colors: active){ :focus-visible{ outline:3px solid CanvasText !important } }` | Gate 6: box-shadow-фокус-кольца невидимы в Windows High Contrast; один блок покрывает все split-CSS страницы | a11y (systemic) |
| 4 | `css/main.css` | тот же forced-colors блок | покрывает `index.html` (монолитный main.css) | a11y (systemic) |
| 5 | `css/audit.css` | `.audit-cta-form__url:focus-visible`: `outline:none` → `outline:2px solid transparent` (+ существующий box-shadow) | Banned `outline:none`; прозрачный outline проявляется системным цветом в forced-colors | a11y |
| 6 | `js/main.js` | `initMagneticButtons()`: early-return при `prefers-reduced-motion: reduce` | Banned: motion без reduced-motion guard | motion a11y |
| 7 | `tools/seo-audit.html` | URL+captcha: `<label class="sr-only">`+`id`+`aria-required`; error → `role="alert" aria-live="assertive"`; progress → `role="status" aria-live="polite"`; captcha `aria-describedby`; декоративный svg `aria-hidden` | Gate 6: SR не объявлял поля и динамику (ошибки/прогресс) | a11y (forms) |
| 8 | `tools/llms-txt-generator.html` | gen-url `<label>`+`required`+`aria-required`; captcha `aria-describedby`; progress `role="status"`; result `aria-live`; стрелка `aria-hidden`; `transition: all` → перечисление свойств | Gate 6 + Banned `transition: all` | a11y / motion |
| 9 | `contacts.html` | Декоративный side-stripe (`border-left:3px`) → карточка (фон `--bg-elevated`, полный 1px border, radius) | Banned: side-stripe как декоративный акцент; «иерархия через пространство, не декор» | structure |
| 10 | `js/form.js` | `validateField()`: ставит `aria-invalid="true"` + `aria-describedby` к `.form-error` при ошибке, снимает при валидном | Gate 6: ошибки формы были невидимы для SR | a11y (forms) |
| 11 | `about.html` | Вторая секция `// Сообщество` / «Роли в сообществе» → `// Хронология` / «Путь в SEO-сообществе» (контент timeline сохранён) | Дубль eyebrow+heading путал иерархию и краулинг; контент не удалял (бренд-страница) | structure |
| 12 | `css/article.css` | Ссылкам TOC добавлен `:focus-visible` (цвет = hover) | Gate 6: клавиатурный фокус читается так же, как hover; касается 15 статей | a11y |
| 13 | `blog/enterprise-seo-…html` | 3× «… — это не «X». Это Y» → тезис вперёд, контраст в хвост («Y, а не X»); ключевики сохранены | Banned-конструкция «Это не X. Это Y.» (клише ИИ-текста) | anti-slop |
| 14 | `blog/pochemu-kontent-…html` | 2× та же конструкция, включая видимый `article-subtitle` | то же | anti-slop |
| 15 | `tools.html` | JSON-LD ItemList: позиции `1,2,2,3,4,5` → `1..6` | Невалидный ItemList (дубль `position`) | correctness |
| 16 | 28× `*.html`/`*.php` | кэш-бастер `?v=202605301531` → `?v=202605310120` | отдать изменённые CSS/JS свежими при деплое | deploy hygiene |

## Проверено и НЕ изменено (осознанно)

| Находка агента | Вердикт | Причина |
|---|---|---|
| `blog.html` счётчики «—» выглядят брошенными | Ложное срабатывание | Реальная backend-фича: `js/blog-stats.js` → `/php/blog/api.php` наполняет views/likes. «—» = состояние до ответа API. Не трогаю рабочую фичу, которую нельзя засмоук-тестить без PHP локально |
| `enterprise-seo`: ещё ~9 «это не …» | Оставлено | Часть — легитимная эмфатическая проза («Это не нужно. И это не поможет.», «Это не осторожность ради осторожности — это математика») или одно-предложная контрастная форма «это не X, а Y» (не banned). Полный список — в `agent4/agent5` отчётах для ревью владельцем; массово переписывать ранжирующий экспертный контент автономно не стал |
| `audit.css`/`components.css`: ~13 `outline:none` на `:focus` | Покрыто системно | Глобальный `forced-colors` блок с `!important` (п.3-4) перекрывает их все; точечно правил только критичный CTA-инпут |

## Заметки для обновления скила (паттерны, которые повторялись)

1. **`outline:none`+box-shadow — частый ложный «доступный» фокус.** Работает визуально, но мёртв в Windows High Contrast. Рекомендация скилу: в Quality Gate 6 явно требовать `@media (forced-colors: active)` блок ИЛИ `outline: …solid transparent` вместо `outline:none`. Добавить в Banned Patterns строку про forced-colors.
2. **Динамические блоки форм без `aria-live`** — системный пробел на формо-страницах. Стоит вынести в чеклист отдельным жёстким пунктом «каждый error/progress/result контейнер имеет role+aria-live до того, как JS в него пишет».
3. **«Это не X. Это Y.»** в RU-контенте — прямой аналог banned «Not X, it's Y». Текущий скил ловит только EN-формулировку. Стоит добавить RU-вариант в Banned Copy.
4. **404 как точка удержания** — скил не выделяет 404 как отдельный тип с требованием навигации. Кандидат в `patterns/` / Quality Gates.
5. **Кэш-бастер при правке split-CSS** — на проектах без билд-шага правка одного CSS требует синхронного бампа `?v=` во всех HTML/PHP. Стоит упомянуть в blueprint «redesign-existing-page» как обязательный шаг verify.

---

## Раунд 2 — Эмпирический аудит (axe-core + overflow)

> Первый раунд был аудитом по чтению кода. Раунд 2 — инструментальный: axe-core (WCAG 2.0/2.1/2.2 A+AA, контраст с посчитанными ratio) + программная проверка горизонтального overflow на 390/768/1280/1440. 13 страниц × 2 вьюпорта для axe, × 4 для overflow. Скрипт: `_audit.mjs` (CDP через встроенный Node WebSocket, инжект axe обходит CSP как devtools-консоль, эмуляция `prefers-reduced-motion` чтобы раскрыть reveal-контент ниже фолда — иначе axe пропускает `opacity:0` при проверке контраста). Прогон 5 раз: baseline → fixes → final.

**Результат: с десятков нарушений до 0 на всех 13 страницах (mobile+desktop), 0 horizontal-overflow на всех 4 вьюпортах.** Артефакты: `.planning/ui-reviews/audit-2026-05-30/_AXE-RESULTS*.json`.

| # | Файл | Что изменил | Почему / находка axe | Тип |
|---|------|-------------|----------------------|-----|
| 17 | `css/article.css` | `.article-below-header` и fallback-grid: убрал `margin-left: max(0px,calc((100%-800px)/2))` → `justify-content: center` | Sticky-TOC grid (800px+gap+335px) + margin-left складывались и переполняли контейнер → `article.container` 1748px, горизонтальный скролл на ≥1300px (все 15 статей) | responsive |
| 18 | `css/article.css` | `.lever-card__num` opacity 0.25→0.6, `.step-block__num` 0.2→0.6 | axe color-contrast: 1.67 и 1.39 (декоративные цифры accent-green на низкой opacity); ×55 в одной статье | contrast |
| 19 | `css/audit.css` | `.audit-step__num` opacity 0.3→0.6 | axe color-contrast 1.89 | contrast |
| 20 | `404.html` | `.error-code` opacity 0.15→0.5 | axe color-contrast 1.24 (гигантский «404») | contrast |
| 21 | `css/base.css`+`css/main.css` | `p a:not(.btn)`, `li a:not(.btn):not(.nav__link)`, `.legal-content a` → `text-decoration: underline` | axe link-in-text-block: inline-ссылки отличались только цветом (1.03–1.49 к окружающему тексту, нужно ≥3:1) | a11y (WCAG 1.4.1) |
| 22 | 12× `*.html` | inline `text-decoration:none` на accent-green ссылках → `underline` (инлайн перебивал CSS) | то же — inline-стиль выигрывал у моего CSS-правила | a11y |
| 23 | `js/main.js` | `initScrollableRegions()`: `tabindex=0`+`aria-label` на `.conf-gallery/.gaming-case__table-wrap/.article-table-wrap` если scrollWidth>clientWidth | axe scrollable-region-focusable: горизонтально-скроллимые таблицы/галерея недоступны с клавиатуры (WCAG 2.1.1) | a11y |
| 24 | `services.html` | `<label for="roi-multiplier">` | axe label (critical): ROI-слайдер без лейбла | a11y |
| 25 | `css/main.css`+`css/components.css` | `.card__tag` color `--text-muted`→`--text-secondary` | axe color-contrast 3.66 (<4.5) | contrast |
| 26 | `css/article.css` | `.article-author__role a` `text-decoration:none`→`underline` | axe link-in-text-block 1.49 (ссылка не в `<p>`) | a11y |
| 27 | `services.html` | `t.me/vivelopi` → `t.me/staurus_seo` | Мёртвый Telegram-контакт (vivelopi) в ROI-CTA | correctness |
| 27a | footer, contacts, sameAs ×7 | **ОТКАТ ошибки:** сначала ошибочно заменил `skirichenko_seo`→`staurus_seo` (неверно понял «только staurus»). Владелец уточнил: `skirichenko_seo` — живой **канал**, `staurus_seo` — прямой контакт. Восстановил `skirichenko_seo` в «Telegram-канал» (footer+contacts), соц-иконке footer и `sameAs` всех 7 файлов | Урок: не расширять замену на основании двусмысленной фразы; контакт ≠ канал. Битые/перепутанные контакты — спрашивать точное соответствие | correctness / **процесс** |
| 27b | `blog/brendovyy-...html` | Убрал пре-существующую висячую запятую `],}` в JSON-LD (citation array) | Невалидный structured data на странице (не связано с моими правками) | correctness |
| 28 | 27× `*.html`/`*.php` | кэш-бастер `?v=202605310200`→`202605310230` | отдать изменённые CSS/JS свежими | deploy hygiene |

### Новые заметки для обновления скила (из эмпирики)

6. **Аудит контраста ОБЯЗАН эмулировать `prefers-reduced-motion`** или иначе раскрывать reveal-контент — иначе axe пропускает `opacity:0`-элементы и контраст под-аудичивается. Критично для сайтов со scroll-reveal. Добавить в методологию `agents/accessibility-auditor.md`.
7. **Декоративные «ghost»-цифры (низкая opacity accent-цвета)** — повторяющийся анти-паттерн контраста. Дизайнеры ставят 0.15–0.3 ради эстетики, получают 1.2–1.9:1. Минимум для large text — 3:1; ghost-эффект держится примерно с opacity 0.55+. Кандидат в Banned Patterns / contrast rule.
8. **Inline `text-decoration:none` перебивает CSS-фиксы** — при редизайне нельзя полагаться только на правило в стайлшите; нужен аудит инлайн-стилей. И «link-in-text-block» (цвет как единственный признак ссылки) — частый serious-фейл; в чеклист.
9. **Scrollable region без `tabindex`** — горизонтально-скроллимые таблицы на мобиле почти всегда ломают WCAG 2.1.1. Готовый JS-фикс (`initScrollableRegions`) стоит положить в `patterns/` как сниппет.
10. **Эмпирика > чтение кода** — первый (read-only) проход не поймал ни overflow на 1440, ни реальные contrast-ratio. Связка «локальный сервер + headless Chrome CDP + axe-core + overflow-проба» должна быть штатным финальным gate в blueprint редизайна. Скрипты `_capture.mjs`/`_audit.mjs` — переиспользуемый инструмент.
