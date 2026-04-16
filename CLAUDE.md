# westsmith.co.uk — Claude Code Guide

## Project overview

Static site generator for the Westsmith Ltd website. Flask reads Markdown files from `content/`, renders them via Jinja2 templates, and outputs a static `build/` directory deployed to GitHub Pages.

## Architecture

- `app/__init__.py` — Flask app factory. On startup, combines `node_modules/simpledotcss/simple.min.css` and `static/styles/styles.css` into `static/external/combined.min.css`
- `app/utils.py` — Walks `content/` and creates Flask routes from Markdown files. File paths map directly to URL routes; `index.md` files map to the directory route
- `content/` — All site content as Markdown files
- `templates/` — Jinja2 templates. Flask falls back to `page.html` if no specific template exists for a route
- `flask_servce.py` — Dev server entry point (note the typo in the filename)
- `build.py` — Builds the static site to `build/`
- `build_and_run.py` — Builds then serves the static site locally on port 8080

## Setup

```bash
uv sync          # Python deps
yarn install     # Node deps (Simple.CSS, Prettier)
pre-commit install
```

## Running

```bash
# Dev server (live Flask)
uv run flask --app flask_servce run --debug

# Build static site
uv run python build.py

# Build and preview static site
uv run python build_and_run.py
```

## Utilities

- `utils/check_links.py` — checks all internal routes and external links for 404s. Run with `uv run python utils/check_links.py`. Not in CI — run manually every now and again or before a release.

## Key things to know

- `node_modules/` must exist before running the app — `yarn install` must be run first
- Pre-commit runs ruff, bandit, pyupgrade, vulture and markdownlint — run `pre-commit run --all-files` before committing
- Deployment is automatic via GitHub Actions on push to `main`

## How pages work

Every page requires a `.md` file in `content/`. The CMS walks that directory and registers a route for every file it finds — no `.md` file means no route, even if a template exists.

Templates are optional. For each route, the CMS looks for a matching template in this order:
1. `templates/{route}.html` (e.g. `templates/services.html`)
2. `templates/{route}/index.html`
3. Falls back to `templates/page.html`

The rendered Markdown is always passed to the template as `{{ content|safe }}`. This means a page can be:

- **Markdown only** — no custom template, content comes entirely from the `.md` file, rendered via `page.html`
- **Template only** — the `.md` file exists but is empty (just frontmatter); all content is in the template. The homepage (`content/index.md` + `templates/index.html`) works this way
- **Mixed** — the template renders `{{ content|safe }}` alongside its own HTML. The about page works this way

## Frontmatter

Markdown files support optional frontmatter using `key: value` pairs at the top of the file (before any blank line). Supported keys:

- `description:` — sets the page meta description
- `title:` — overrides the auto-generated page title

Example:
```markdown
description: A short description for search engines.
title: Custom Page Title | Westsmith

# Page heading

Content here...
```
