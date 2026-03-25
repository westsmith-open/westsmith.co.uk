# westsmith.co.uk

This is the source code for the [Westsmith Ltd](https://westsmith.co.uk) website.

---

## 🧰 Tech Stack

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [GitHub Pages](https://pages.github.com/)
- HTML + CSS (Simple.CSS with some Bootstrap utilities)

---


## Why a custom CMS?

Most CMS platforms push you towards a theme. You pick one, then spend time fighting it to make it look the way you want. The theme brings its own opinions about layout, CSS and structure, and unpicking those can take longer than building from scratch.

The goal here was something simpler: Markdown files for content, Jinja2 templates for HTML, and full control over the CSS. No theme to override, no framework making layout decisions for you.

There may be tools out there that work this way already, but none obvious enough to find quickly. The longer-term ambition is to extract this into a proper standalone CMS that others could use, but that hasn't happened yet.

[Pelican](https://getpelican.com/) turns out to be a close match — Python, Markdown, Jinja2, bring your own CSS. The plan is to trial a migration at some point and see whether it offers the same flexibility without the maintenance overhead.

---

## How pages work

Every page requires a `.md` file in `content/`. The CMS walks that directory and registers a route for each file — no `.md` file means no route.

Templates are optional. For each route, the CMS looks for a matching template in this order:
1. `templates/{route}.html`
2. `templates/{route}/index.html`
3. Falls back to `templates/page.html`

The rendered Markdown is always passed to the template as `{{ content|safe }}`. Pages can be Markdown-only, template-only (with an empty `.md` file), or a mix of both.

Frontmatter is supported at the top of any `.md` file:

```markdown
description: Meta description for search engines.
title: Custom Page Title | Westsmith

# Page content starts here
```

---

## Development

### Setup

Install Python dependencies:

```bash
uv sync
```

Install Node dependencies (required for Simple.CSS and Prettier):

```bash
yarn install
```

Install pre-commit hooks:

```bash
pre-commit install
```

### Running locally

To run the Flask dev server with live reloading:

```bash
uv run flask --app flask_servce run --debug
```

To build the static site and preview it:

```bash
uv run python build_and_run.py
```

To build only:

```bash
uv run python build.py
```
