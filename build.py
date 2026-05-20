from __future__ import annotations

import hashlib
import html
import re
import shutil
from datetime import date
from pathlib import Path

from site_data import FOOTER_LINKS, NAV_ITEMS, PAGES, SITE_DESCRIPTION, SITE_NAME

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
ASSETS_SRC = ROOT / "assets"
ASSETS_DST = DIST / "assets"
CONTENT_ROOT = ROOT / "content"

ASSET_MAP: dict[str, str] = {}

def _fingerprint(path):
    """Return a short hex digest of a file's content."""
    return hashlib.sha256(path.read_bytes()).hexdigest()[:8]

def build_asset_map() -> None:
    """Fingerprint every file under assets/ and populate ASSET_MAP."""
    ASSET_MAP.clear()
    for fpath in ASSETS_SRC.rglob("*"):
        if fpath.is_file():
            rel = fpath.relative_to(ASSETS_SRC)
            key = f"assets/{rel.as_posix()}"
            stem = fpath.stem
            suffix = fpath.suffix
            h = _fingerprint(fpath)
            ASSET_MAP[key] = f"{stem}-{h}{suffix}"

def asset_href(path):
    """Turn an asset reference into a fingerprinted one."""
    for prefix_str in ("../assets/", "./assets/"):
        if path.startswith(prefix_str):
            stripped = path[len(prefix_str):]
            key = f"assets/{stripped}"
            if key in ASSET_MAP:
                return f"{prefix_str}{ASSET_MAP[key]}"
            return path
    if path.startswith("/assets/"):
        key = path[1:]
        if key in ASSET_MAP:
            return f"/{ASSET_MAP[key]}"
    return path


_ASSET_RE = re.compile(r'((?:\.\./)*(?:\./)?(?:/)?assets/)([\w\-]+(?:/[\w\-]+)*\.\w+)')

def _replace_assets(m: re.Match) -> str:
    """Replace an asset path with its fingerprinted version, preserving prefix."""
    prefix = m.group(1)
    path = m.group(2)
    key = f"assets/{path}"
    if key in ASSET_MAP:
        return prefix + ASSET_MAP[key]
    return m.group(0)


def _fingerprint_html(html: str) -> str:
    """Scan HTML and fingerprint all /assets/... references."""
    return _ASSET_RE.sub(_replace_assets, html)


def page_depth(slug: str) -> int:
    return 0 if not slug else len(slug.split('/'))


def relative_prefix(slug: str) -> str:
    depth = page_depth(slug)
    return './' if depth == 0 else '../' * depth


def relative_href(from_slug: str, to_slug: str) -> str:
    prefix = relative_prefix(from_slug)
    if not to_slug:
        return f"{prefix}"
    return f"{prefix}{to_slug}/"


def is_active(current_slug: str, nav_slug: str) -> bool:
    if nav_slug == '':
        return current_slug == ''
    return current_slug == nav_slug or current_slug.startswith(f"{nav_slug}/")


def render_nav(current_slug: str) -> str:
    items = []
    for item in NAV_ITEMS:
        cls = 'nav-link active' if is_active(current_slug, item['slug']) else 'nav-link'
        href = relative_href(current_slug, item['slug'])
        items.append(f'<a class="{cls}" href="{href}">{html.escape(item["label"])}</a>')
    return ''.join(items)


def render_footer(current_slug: str) -> str:
    links = []
    for item in FOOTER_LINKS:
        href = item['href'] if item['external'] else relative_href(current_slug, item['href'])
        links.append(f'<a href="{href}">{html.escape(item["label"])}</a>')
    return ''.join(links)


def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    if not text.startswith('---\n'):
        return {}, text

    lines = text.splitlines()
    data: dict[str, object] = {}
    index = 1
    while index < len(lines):
        line = lines[index]
        index += 1
        if line.strip() == '---':
            break
        if not line.strip() or ':' not in line:
            continue
        key, value = line.split(':', 1)
        data[key.strip()] = parse_scalar(value.strip())
    body = '\n'.join(lines[index:]).strip()
    return data, body


def parse_scalar(value: str) -> object:
    if not value:
        return ''
    if value.lower() in {'true', 'false'}:
        return value.lower() == 'true'
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    if value.startswith('[') and value.endswith(']'):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [item.strip().strip('"').strip("'") for item in inner.split(',')]
    return value


def parse_date(value: object | None) -> date | None:
    if not value or not isinstance(value, str):
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def format_date(value: object | None) -> str:
    parsed = parse_date(value)
    if not parsed:
        return ''
    return f'{parsed.day} {parsed.strftime("%b %Y")}'


def inline_markdown(text: str) -> str:
    result: list[str] = []
    last = 0
    for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', text):
        result.append(html.escape(text[last:match.start()]))
        label, href = match.groups()
        result.append(f'<a href="{html.escape(href, quote=True)}">{html.escape(label)}</a>')
        last = match.end()
    result.append(html.escape(text[last:]))
    output = ''.join(result)
    output = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', output)
    output = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', output)
    return output


def markdown_to_html(markdown: str) -> str:
    blocks: list[str] = []
    lines = markdown.strip().splitlines()
    paragraph: list[str] = []
    in_list = False

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            blocks.append(f'<p>{inline_markdown(" ".join(paragraph))}</p>')
            paragraph = []

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            blocks.append('</ul>')
            in_list = False

    for raw in lines:
        line = raw.strip()
        if not line:
            flush_paragraph()
            close_list()
            continue
        if line.startswith('### '):
            flush_paragraph()
            close_list()
            blocks.append(f'<h3>{inline_markdown(line[4:])}</h3>')
            continue
        if line.startswith('## '):
            flush_paragraph()
            close_list()
            blocks.append(f'<h2>{inline_markdown(line[3:])}</h2>')
            continue
        if line.startswith('# '):
            flush_paragraph()
            close_list()
            blocks.append(f'<h1>{inline_markdown(line[2:])}</h1>')
            continue
        if line.startswith('- '):
            flush_paragraph()
            if not in_list:
                blocks.append('<ul>')
                in_list = True
            blocks.append(f'<li>{inline_markdown(line[2:])}</li>')
            continue
        paragraph.append(line)

    flush_paragraph()
    close_list()
    return '\n'.join(blocks)


def load_collection(name: str, date_key: str) -> list[dict[str, object]]:
    entries: list[dict[str, object]] = []
    folder = CONTENT_ROOT / name
    if not folder.exists():
        return entries
    for path in sorted(folder.glob('*.md')):
        data, body = parse_frontmatter(path.read_text(encoding='utf-8'))
        entry = dict(data)
        entry['body'] = body
        entry['slug'] = str(entry.get('slug') or path.stem)
        entry['published'] = bool(entry.get('published', True))
        entry['source_path'] = str(path.relative_to(ROOT))
        entries.append(entry)
    return sorted(entries, key=lambda item: (parse_date(item.get(date_key)) or date.min, str(item.get('title', ''))), reverse=True)


def render_news_index(entries: list[dict[str, object]]) -> str:
    cards = []
    published = [entry for entry in entries if entry.get('published')]
    for entry in published:
        cards.append(
            f'''<article class="card">
  {'<img class="media-image" src="' + html.escape(str(entry["featured_image"])) + '" alt="' + html.escape(str(entry["title"])) + '">' if entry.get('featured_image') else ''}
  <p class="meta-line">{html.escape(format_date(entry.get("date")))}</p>
  <h2>{html.escape(str(entry["title"]))}</h2>
  <p>{html.escape(str(entry.get("summary", "")))}</p>
  <p><a class="button button-secondary" href="{html.escape(str(entry["slug"]))}/">Read article</a></p>
</article>'''
        )
    if not cards:
        cards.append('<article class="card"><h2>No news posts yet</h2><p>Publish the first article from the repo.</p></article>')
    return f'<section class="grid two-up">{"".join(cards)}</section>'


def render_news_detail(entry: dict[str, object]) -> str:
    hero_image = ''
    if entry.get('featured_image'):
        hero_image = f'<img class="media-image" src="{html.escape(str(entry["featured_image"]))}" alt="{html.escape(str(entry["title"]))}">'
    return f'''<article class="card prose">
  <p class="meta-line">{html.escape(format_date(entry.get("date")))}</p>
  {hero_image}
  <p>{html.escape(str(entry.get("summary", "")))}</p>
  {markdown_to_html(str(entry.get("body", "")))}
</article>'''


def render_events_index(entries: list[dict[str, object]]) -> str:
    cards = []
    published = [entry for entry in entries if entry.get('published')]
    for entry in published:
        when = format_date(entry.get('start_date'))
        if entry.get('end_date') and entry.get('end_date') != entry.get('start_date'):
            end = format_date(entry.get('end_date'))
            when = f'{when} to {end}'
        location = str(entry.get('location', ''))
        meta = ' | '.join(part for part in [when, location] if part)
        cards.append(
            f'''<article class="card card-v">
  {'<img class="media-image" src="' + html.escape(str(entry["featured_image"])) + '" alt="' + html.escape(str(entry["title"])) + '">' if entry.get('featured_image') else ''}
  <p class="meta-line">{html.escape(meta)}</p>
  <h2>{html.escape(str(entry["title"]))}</h2>
  <p>{html.escape(str(entry.get("summary", "")))}</p>
  <p class="btn-fill"><a class="button button-secondary" href="{html.escape(str(entry["slug"]))}/">View event</a></p>
</article>'''
        )
    if not cards:
        cards.append('<article class="card"><h2>No events yet</h2><p>Add the first event from the repo.</p></article>')
    return f'<section class="grid two-up">{"".join(cards)}</section>'


def render_event_detail(entry: dict[str, object]) -> str:
    meta_items = []
    if entry.get('start_date'):
        start = format_date(entry.get('start_date'))
        if entry.get('end_date') and entry.get('end_date') != entry.get('start_date'):
            start = f'{start} to {format_date(entry.get("end_date"))}'
        meta_items.append(f'<li><strong>Date:</strong> {html.escape(start)}</li>')
    if entry.get('location'):
        meta_items.append(f'<li><strong>Location:</strong> {html.escape(str(entry["location"]))}</li>')
    hero_image = ''
    if entry.get('featured_image'):
        hero_image = f'<img class="media-image" src="{html.escape(str(entry["featured_image"]))}" alt="{html.escape(str(entry["title"]))}">'
    meta_html = f'<ul class="detail-list">{"".join(meta_items)}</ul>' if meta_items else ''
    return f'''<article class="card prose">
  {hero_image}
  <p>{html.escape(str(entry.get("summary", "")))}</p>
  {meta_html}
  {markdown_to_html(str(entry.get("body", "")))}
</article>'''


def with_dynamic_sections(page: dict[str, str], news: list[dict[str, object]], events: list[dict[str, object]]) -> dict[str, str]:
    if page['slug'] != '':
        return page
    published_news = [entry for entry in news if entry.get('published')][:2]
    published_events = [entry for entry in events if entry.get('published')][:2]

    news_items = ''.join(
        f'<li><a href="news/{html.escape(str(entry["slug"]))}/">{html.escape(str(entry["title"]))}</a> <span class="meta-inline">{html.escape(format_date(entry.get("date")))}</span></li>'
        for entry in published_news
    ) or '<li>No news posts yet.</li>'
    event_items = ''.join(
        f'<li><a href="events/{html.escape(str(entry["slug"]))}/">{html.escape(str(entry["title"]))}</a> <span class="meta-inline">{html.escape(format_date(entry.get("start_date")))}</span></li>'
        for entry in published_events
    ) or '<li>No events yet.</li>'

    extra = f'''
<section class="grid two-up">
  <article class="card card-v">
    <h2>Latest news</h2>
    <ul class="link-list">{news_items}</ul>
    <p class="btn-fill"><a class="button button-secondary" href="news/">All news</a></p>
  </article>
  <article class="card card-v">
    <h2>Events</h2>
    <ul class="link-list">{event_items}</ul>
    <p class="btn-fill"><a class="button button-secondary" href="events/">All events</a></p>
  </article>
</section>
'''
    updated = dict(page)
    updated['content'] = page['content'] + extra
    return updated


def build_pages() -> list[dict[str, str]]:
    news_entries = load_collection('news', 'date')
    event_entries = load_collection('events', 'start_date')

    pages: list[dict[str, str]] = [with_dynamic_sections(page, news_entries, event_entries) for page in PAGES]
    pages.append({
        'slug': 'news',
        'title': 'News',
        'eyebrow': 'Club updates',
        'intro': 'Announcements and public updates from the club.',
        'description': 'News posts for Cessnock Motor Cycle Club.',
        'content': render_news_index(news_entries),
    })
    pages.append({
        'slug': 'events',
        'title': 'Events',
        'eyebrow': 'Club calendar',
        'intro': 'Public event listings for the club.',
        'description': 'Event listings for Cessnock Motor Cycle Club.',
        'content': render_events_index(event_entries),
    })

    for entry in news_entries:
        if not entry.get('published'):
            continue
        pages.append({
            'slug': f'news/{entry["slug"]}',
            'title': str(entry['title']),
            'eyebrow': 'News article',
            'intro': str(entry.get('summary', '')),
            'description': str(entry.get('summary', SITE_DESCRIPTION)),
            'content': render_news_detail(entry),
        })
    for entry in event_entries:
        if not entry.get('published'):
            continue
        pages.append({
            'slug': f'events/{entry["slug"]}',
            'title': str(entry['title']),
            'eyebrow': 'Event',
            'intro': str(entry.get('summary', '')),
            'description': str(entry.get('summary', SITE_DESCRIPTION)),
            'content': render_event_detail(entry),
        })
    return pages


def render_page(page: dict[str, str]) -> str:
    slug = page['slug']
    title = page['title']
    description = page.get('description', SITE_DESCRIPTION)
    page_title = SITE_NAME if slug == '' else f"{title} | {SITE_NAME}"
    prefix = relative_prefix(slug)
    body_class = page.get('body_class', '')
    eyebrow = page.get('eyebrow', 'Cessnock Motor Cycle Club')
    intro = page.get('intro', '')

    body_cls = f' {body_class}' if body_class else ''
    hero = f'''
<section class="hero{body_cls}">
      <div class="container hero-inner">
        <p class="eyebrow">{html.escape(eyebrow)}</p>
        <h1>{html.escape(title)}</h1>
        <p class="intro">{intro}</p>
      </div>
    </section>
    '''

    return f'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html.escape(page_title)}</title>
    <meta name="description" content="{html.escape(description)}">
    <link rel="icon" href={asset_href(f"{prefix}assets/media/favicon-32x32.png")} type="image/png">
    <link rel="icon" href={asset_href(f"{prefix}assets/media/favicon.png")} sizes="any" type="image/png">
    <link rel="stylesheet" href={asset_href(f"{prefix}assets/styles.css")}>
  </head>
  <body>
    <header class="site-header">
      <div class="container header-inner">
        <a class="brand" href="{relative_href(slug, '')}">
          <img class="brand-logo" src={asset_href(f"{prefix}assets/media/club-logo.png")} alt="Cessnock Motor Cycle Club logo">
        </a>
        <nav class="site-nav" aria-label="Primary">
          {render_nav(slug)}
        </nav>
      </div>
    </header>
    {hero}
    <main class="container main-content">
      {page['content']}
    </main>
    <footer class="site-footer">
      <div class="container footer-inner">
        <div>
          <strong>{html.escape(SITE_NAME)}</strong>
          <p>{html.escape(SITE_DESCRIPTION)}</p>
        </div>
        <div class="footer-links">
          {render_footer(slug)}
        </div>
      </div>
    </footer>
  </body>
</html>
'''


def write_page(page: dict[str, str]) -> None:
    slug = page['slug']
    target_dir = DIST if slug == '' else DIST / slug
    target_dir.mkdir(parents=True, exist_ok=True)
    html = render_page(page)
    html = _fingerprint_html(html)
    (target_dir / 'index.html').write_text(html, encoding='utf-8')


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    build_asset_map()
    for fpath in ASSETS_SRC.rglob("*"):
        if fpath.is_file():
            rel = fpath.relative_to(ASSETS_SRC)
            for key, fname in ASSET_MAP.items():
                if rel == Path(key.replace("assets/", "", 1)):
                    dst = ASSETS_DST / fname
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(fpath, dst)
                    break
    pages = build_pages()
    for page in pages:
        write_page(page)
    shutil.copy(ROOT / '404.html', DIST / '404.html')
    print(f"Built {len(pages)} pages into {DIST}")


if __name__ == '__main__':
    main()
