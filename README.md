# Cessnock Motor Cycle Club static rebuild

This repository contains a dependency-free static rebuild of the public-facing Cessnock Motor Cycle Club website.

Instead of relying on a CMS, the site is generated with a small Python build script and deployed as plain static files. That keeps it easy to manage in git and simple to host on Cloudflare Pages.

The current rebuild carries over the main public images as project-local files under `assets/media/`, preserves a broader sweep of legacy public files under `assets/legacy-sweep/`, and includes a locally generated `assets/docs/club-constitution.pdf` based on the full legacy constitution page. The embedded homepage video still uses YouTube.

## Project structure

- `site_data.py` stores page content and site metadata.
- `build.py` generates the static site into `dist/`.
- `.pages.yml` configures Pages CMS collections and media folders.
- `content/news/` stores editable news articles.
- `content/events/` stores editable events.
- `assets/` contains the shared stylesheet.
- `assets/media/` contains exported images copied from the legacy site
- `assets/legacy-sweep/` contains additional preserved public legacy images
- `assets/docs/` contains preserved and generated downloadable documents

## Local development

Build the site:

```bash
python3 build.py
```

Preview the generated site locally:

```bash
python3 -m http.server 8000 -d dist
```

Then open `http://localhost:8000`.

## Cloudflare Pages setup

Create a new Cloudflare Pages project connected to this GitHub repository and use:

- Build command: `python3 build.py`
- Build output directory: `dist`

No package installation is required.

## Pages CMS setup

This project is now structured for [Pages CMS](https://pagescms.org/).

After the repository is on GitHub:

- open the repository in Pages CMS
- keep `.pages.yml` at the repository root
- use the `News` and `Events` collections to create and edit entries
- upload reusable images into `assets/media/`

The static build will automatically generate:

- `/news/` and individual news article pages
- `/events/` and individual event pages
- homepage summary sections for the latest news and events

## Content review before launch

This conversion is based on the public content available on the legacy site. Before pointing the real domain at the new build, review these details carefully:

- committee names and roles
- membership pricing
- meeting schedule and venue
- sponsorship references
- any historical pages you may no longer want publicly listed
- whether you want additional legacy galleries or documents copied into this repo as well

## Legacy document note

The old site did not expose a directly linked constitution PDF during migration. `assets/docs/club-constitution.pdf` was generated locally from the full public constitution HTML so the new site can offer a downloadable copy.

## Suggested next improvements

- add a small editor guide for committee members using Pages CMS
- add a contact form using Cloudflare Forms, Workers, or a third-party form service
