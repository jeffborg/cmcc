# Cessnock Motor Cycle Club — Static Site

## Tech stack
- **Python 3** static site generator (zero external dependencies). No frameworks, no build tools beyond standard library.
- **Python 3.12+** — confirmed via `site_data.cpython-314.pyc` in `__pycache__/`.
- **CSS** custom properties (CSS variables) for theming — `assets/styles.css` is the single stylesheet (~5.5 KB).
- **Pages CMS** for non-technical editors managing news/events. See `.pages.yml`.
- **Cloudflare Pages** for hosting. No package manager required.

## Build, dev, and test
| Task | Command |
|------|---------|
| Build site | `python3 build.py` |
| Live-reload dev server | `npm install && npm run dev` (serves `dist/` on port 8001, watches `assets/`, `content/`, `build.py`, `site_data.py`) |
| Serve built site | `python3 -m http.server 8000 -d dist` |
| Deploy | Push to `main` — Cloudflare Pages builds automatically via `.github/workflows/deploy.yml` |

**No tests or linters exist.** The entire site is ~1,000 lines of Python in two files (`build.py` + `site_data.py`) plus CSS.

## Architecture overview

```
build.py                      ← Build script; reads PAGES from site_data.py, writes HTML to dist/
site_data.py                  ← ALL page content + metadata (PAGES list, NAV_ITEMS, FOOTER_LINKS)
assets/styles.css             ← Single stylesheet with CSS custom properties
assets/media/                 ← Images (logos, heroes, sponsors, gallery)
content/news/*.md             ← News articles (yaml frontmatter, markdown body)
content/events/*.md           ← Event listings (yaml frontmatter, markdown body)
.pages.yml                    ← Pages CMS configuration (media + news + events collections)
.github/workflows/deploy.yml  ← Cloudflare Pages deploy workflow
```

### How pages are generated
1. **`site_data.py`** defines a `PAGES` list — each entry has `slug`, `title`, `eyebrow`, `intro`, `description`, optional `body_class`, and HTML `content`.
2. **`build.py`** imports `PAGES`, `NAV_ITEMS`, and `FOOTER_LINKS` from `site_data.py`.
3. It also loads markdown files from `content/news/` and `content/events/`.
4. Pages are written to `dist/{slug}/index.html` (root page → `dist/index.html`).
5. News/event details are generated dynamically from markdown files.
6. **The homepage** gets injected "latest news" and "events" sections via `with_dynamic_sections()`.

### Key design patterns in `build.py`
- **`relative_href()` / `relative_prefix()`** — computes `../` navigation depth from each page's slug.
- **`inline_markdown()`** — a custom inline markdown parser (links, **bold**, *italic*). Not a full library.
- **`markdown_to_html()`** — block-level markdown → HTML (headings, lists, paragraphs).
- **`parse_frontmatter()`** — parses `---\nkey: value\n---` from content files (no yaml library dependency).
- **`render_page()`** — produces a complete HTML document with header/nav/hero/footer shell.

### Content management
- **Static pages** (about, membership, gallery, etc.) live in `PAGES` inside `site_data.py`. Edit them directly.
- **News & events** are markdown files in `content/news/` and `content/events/`. They can also be edited via Pages CMS (see `.pages.yml`).
- News and event markdown files use **yaml frontmatter** with fields like `title`, `slug`, `date`/`start_date`, `published`, `summary`, `featured_image`, `body`.

## Conventions
- **Slug-based routing**: page slugs determine output paths (`'get-involved'` → `dist/get-involved/index.html`).
- **All HTML in Python**: page content is raw HTML strings inside `site_data.py`. Do not refactor this to a templating engine — the entire site fits in ~1,000 lines and is intentionally dependency-free.
- **CSS uses custom properties**: `--bg`, `--panel`, `--text`, `--brand`, `--brand-dark`, `--shadow`, `--radius`, `--max`. See `assets/styles.css` for all CSS class names and structure.
- **No JavaScript** on the site (beyond BrowserSync for dev). Navigation is static HTML.
- **`dist/` is gitignored** — never commit built output.
- **`__pycache__/` is gitignored**.
- **Sponsor/media references** use absolute paths like `/assets/media/...` in page content but relative paths in generated HTML.
- **Pages CMS slugs** must match the pattern `^[a-z0-9-]+$` (lowercase letters, numbers, hyphens only).

## When editing pages
- To add/modify a static page: edit `site_data.py` → `PAGES` list. Add a new dict entry with `slug`, `title`, `content`, etc.
- To add a news article: create `content/news/{slug}.md` with frontmatter + body.
- To add an event: create `content/events/{slug}.md` with frontmatter + body.
- After any change, run `python3 build.py` to regenerate.
- For live preview: `npm run dev`.

## Important notes
- **`site_data.py` is the single source of truth for page content.** This is the file that editors with Python knowledge (or developers) should modify for static pages.
- **The build is idempotent.** It deletes `dist/` before regenerating.
- **No npm dependencies** beyond `browser-sync` (dev only). Production deploys with `python3 build.py` and no `npm install`.
- **The site is a club website** — keep edits family-friendly, community-oriented, and consistent with the existing tone.
