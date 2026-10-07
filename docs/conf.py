# Configuration for the ore website (built with Sphinx).
# Pages are written in Markdown (MyST) inside this docs/ folder.

project = "ore"
author = "ore contributors"
copyright = "2026, ore contributors. Content licensed CC BY 4.0"

extensions = [
    "myst_parser",   # write pages in Markdown
    "sphinx_design", # cards, grids and drop-down solutions
    "sphinx_copybutton", # "copy" button on code blocks
]

source_suffix = {".md": "markdown"}
root_doc = "index"
exclude_patterns = ["_build", "workshops/_template.md", "modules/_lesson-template.md", "Thumbs.db", ".DS_Store"]

myst_enable_extensions = ["colon_fence", "deflist", "attrs_inline"]
myst_heading_anchors = 3

# -- Look and feel -----------------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_title = "ore · Open Resources for Earth Sciences"
html_baseurl = "https://openresearth.github.io/"
html_logo = "_static/logo.svg"
html_favicon = "_static/favicon.svg"
html_static_path = ["_static"]
html_css_files = [
    "https://fonts.googleapis.com/css2?family=Sora:wght@600&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400&display=swap",
    "custom.css",
]
html_show_sourcelink = False

html_theme_options = {
    "logo_only": True,
    "style_nav_header_background": "#17252A",
    "collapse_navigation": False,
    "navigation_depth": 2,
    "prev_next_buttons_location": "both",
}

# "Edit on GitHub" link at the top of every page
html_context = {
    "display_github": True,
    "github_user": "openresearth",
    "github_repo": "openresearth.github.io",
    "github_version": "main",
    "conf_py_path": "/docs/",
}

# Copy button: don't copy the ">>>" or "$" prompts
copybutton_exclude = ".linenos, .gp, .go"

# Pages that exist but are deliberately left out of the sidebar don't need a warning
suppress_warnings = ["toc.not_included"]

# -- Separate sidebar menu for learning modules ------------------------------
# Every page in docs/modules/<name>/ shows a menu with only that module's
# lessons (taken from the toctree in docs/modules/<name>/index.md).
# New modules get this menu automatically; nothing to change here.
templates_path = ["_templates"]


def _module_nav(app, pagename, templatename, context, doctree):
    parts = pagename.split("/")
    if len(parts) < 3 or parts[0] != "modules":
        return
    env = app.builder.env
    root = f"modules/{parts[1]}/index"
    if root not in env.titles:
        return

    def uri(doc):
        # link to a page; for the page itself use its own file name
        return (app.builder.get_relative_uri(pagename, doc)
                or app.builder.get_target_uri(doc).split("/")[-1])

    def sections(doc):
        # second-level headings (##) of a page, for the current lesson only
        from docutils import nodes
        found = []
        toc = env.tocs.get(doc)
        if toc is None or not len(toc):
            return found
        for lst in toc[0].children:              # the page title's item
            if isinstance(lst, nodes.bullet_list):  # its list of ## headings
                for item in lst.children:
                    ref = next(item.findall(nodes.reference), None)
                    if ref is not None:
                        found.append({"title": ref.astext(),
                                      "url": ref.get("anchorname", "")})
        return found

    lessons = []
    for doc in env.toctree_includes.get(root, []):
        current = doc == pagename
        lessons.append({
            "title": env.titles[doc].astext(),
            "url": uri(doc),
            "current": current,
            "sections": sections(doc) if current else [],
        })
    context["module_nav"] = {
        "title": env.titles[root].astext(),
        "url": uri(root),
        "current": pagename == root,
        "home": uri("index"),
        "lessons": lessons,
    }


def setup(app):
    app.connect("html-page-context", _module_nav)
