# Copilot / AI Agent Instructions for Video-Game-Creation-Website

This project is a minimal Flask-based static UI site for a Video Game Creation tutorial. The guidance below is focused, actionable, and tailored to the repository layout and conventions.

## Big picture
- **Runtime:** Flask app defined in [server.py](server.py). The app serves template pages (no REST API endpoints present).
- **Templates:** Jinja2 templates live in [templates/](templates/) with a base `layout.html` and pages like `homepage.html` that `extend` the base template.
- **Static assets:** Served from [static/](static/). `main.css` exists but is currently empty.
- **External UI libs:** `layout.html` links to Bootstrap and jQuery via CDNs — changes to markup should account for those versions.

## Where to look to implement or change behavior
- Add routes and view logic in [server.py](server.py). Current root handler renders [templates/homepage.html](templates/homepage.html).
- Modify site-wide layout, scripts and CSS includes in [templates/layout.html](templates/layout.html).
- Place or edit custom CSS in [static/main.css](static/main.css).
- Dependencies are pinned in [requirements.txt](requirements.txt) (currently `Flask==3.1.2`).

## Developer workflows (exact commands)
- Install deps: `pip install -r requirements.txt`.
- Run locally (recommended):

```bash
export FLASK_APP=server.py
export FLASK_DEBUG=1
flask run --reload
```

- Alternative (if adding an `app.run()`): `python server.py` — note the repository currently lacks an explicit `if __name__ == '__main__': app.run(...)` block.

## Project-specific patterns & conventions
- Templates use Jinja2 block inheritance. Example: `homepage.html` starts with `{% extends "layout.html" %}` and overrides `{% block content %}`.
- Keep global layout changes in [templates/layout.html](templates/layout.html); page-specific markup belongs in per-page templates.
- Static assets are referenced with absolute `/static/...` paths in templates — follow that pattern.

## Integration & external considerations
- UI depends on CDN-hosted Bootstrap 5 and jQuery versions declared in `layout.html`. When editing those includes, test in-browser to confirm compatibility.
- There are no DB, background workers, or external APIs in the repository; any integrations should add clear config and mention in this file.

## Quick examples
- Add a new route (in [server.py](server.py)):

```python
@app.route('/about')
def about():
    return render_template('about.html')
```

- Create `templates/about.html` by extending the base:

```jinja
{% extends "layout.html" %}
{% block content %}
<h1>About</h1>
{% endblock %}
```

## What the AI should not assume
- Do not assume a database or environment variables beyond what the repo shows.
- Do not change external CDN versions without testing; they're intentionally included in `layout.html`.

## When you need more context
- Ask the human owner for intended runtime command if you plan to add `app.run()`.
- Request details for any external service integration (credentials, endpoints, schema).

---
If you want, I can also (1) add a simple `app.run()` guard in `server.py` for `python server.py` local running, (2) create a small `about.html` example, or (3) add a short CONTRIBUTING note — which would you like next?
