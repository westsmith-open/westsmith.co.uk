# westsmith.co.uk

This is the source code for the [Westsmith Ltd](https://westsmith.co.uk) website.

---

## 🧰 Tech Stack

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [GitHub Pages](https://pages.github.com/)
- HTML + CSS (Simple.CSS with some Bootstrap utilities)

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
