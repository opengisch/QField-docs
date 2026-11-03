"""MkDocs hook that writes redirect pages for moved or removed pages.

Runs once per language build of mkdocs-static-i18n, so every locale gets its redirects.
"""

from pathlib import Path

# old page: new page (optionally with an #anchor) or full external URL
REDIRECTS = {
    "how-to/general/settings": "fieldwork/general/settings",
    "how-to/general/projects": "fieldwork/general/projects",
    "how-to/project-setup/create-project": "fieldwork/create-project",
    "how-to/navigation-and-positioning/navigation": "fieldwork/navigation-and-positioning/navigation",
    "how-to/data-collection/processing": "fieldwork/data-collection/processing",
    "how-to/qfield-interface/bookmarks": "fieldwork/qfield-interface/bookmarks",
    "how-to/qfield-interface/measuring-tool": "fieldwork/qfield-interface/measuring-tool",
    "how-to/qfield-interface/search": "fieldwork/qfield-interface/search",
    "how-to/advanced-how-tos/cogo-framework": "fieldwork/data-collection/cogo-framework",
    "how-to/qfield-interface/map-themes": "how-to/qfield-interface/map-interaction#map-themes",
    "how-to/qfield-interface/map-styling": "how-to/qfield-interface/map-interaction#map-styling",
    "how-to/advanced-how-tos/live-default-value": "how-to/project-setup/attributes-form#define-default-values",
    "how-to/advanced-how-tos/movable-project": "how-to/project-setup/data_source_and_project_paths",
    "success-stories": "https://qfield.org/success-stories/",
}

TEMPLATE = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Redirecting...</title>
<link rel="canonical" href="{url}">
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={url}">
</head>
<body>
This page has moved to <a href="{url}">a new location</a>.
</body>
</html>
"""


def on_post_build(config, **kwargs):
    i18n = config.plugins["i18n"]
    site_dir = Path(config.site_dir)
    base_url = config.site_url.rstrip("/") + "/"
    if i18n.current_language != i18n.default_language:
        site_dir = site_dir / i18n.current_language
        base_url += i18n.current_language + "/"

    for old, new in REDIRECTS.items():
        if new.startswith("https://"):
            url = new
        else:
            new_path, hash_sign, anchor = new.partition("#")
            url = base_url + new_path + "/" + hash_sign + anchor
        target = site_dir / old / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(TEMPLATE.format(url=url), encoding="utf-8")
