import os
import markdown


def load_markdown(filename):
    """Load and convert a Markdown file from the /content folder."""
    path = os.path.join("content", filename)
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    html = markdown.markdown(text, extensions=["fenced_code", "tables"])
    return html
