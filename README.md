# westsmith.co.uk

This is the source code for the [Westsmith Ltd](https://westsmith.co.uk) website.  
It’s a simple, fast, and fully open-source static site built with [Frozen-Flask](https://pythonhosted.org/Frozen-Flask/) and hosted on [GitHub Pages](https://pages.github.com).

---

## 🛤️ Evolution of the Site

This site has gone through several iterations:

- **Early days:** Built with [Hugo](https://gohugo.io) and deployed via [Netlify](https://www.netlify.com) — fast, but limited in flexibility.
- **Then:** Rebuilt using [Google Sites](https://sites.google.com) for its ease of drag-and-drop editing. It worked but didn’t feel like "code".
- **Now:** Fully rebuilt from scratch using Python and [Frozen Flask](https://pythonhosted.org/Frozen-Flask/), giving full control over content, structure, and generation.  
  This version is statically generated, committed to GitHub, and hosted via GitHub Pages.

This project is inspired in part by [danielball.com](https://danielball.com), a sister site that follows a similar philosophy — simplicity, control, and developer-friendliness. That site is built with [Jekyll](https://jekyllrb.com) and also hosted on GitHub Pages.

---

## 🧰 Tech Stack

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Frozen-Flask](https://pythonhosted.org/Frozen-Flask/)
- [GitHub Pages](https://pages.github.com/)
- HTML + CSS (Simple.CSS with some Bootstrap utilities)

---

## 🚀 Development

To run locally:

```bash
pip install -r requirements.txt
flask run
```

To build the static site:

```bash
python freeze.py
```

Then commit the build/ directory to the main branch for GitHub Pages deployment.

📄 License

The source code for this website is open source and available under the MIT License.
However, all branding, logos, product names, and written content are the property of Westsmith Ltd and are not covered under the open-source license.

See LICENSE and license.html for details.

© 2019–2025 Westsmith Ltd. All rights reserved.