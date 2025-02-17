import markdown
import material.extensions.emoji # needed by yaml!
import re
import requests
import yaml
import os

from typing import Any, Generator, Iterable

from generate_zoho_auth import get_fresh_token

category_map = {
    "Get started": "116946000000448345",
    "How-to guides": "116946000000448334",
    "Technical reference": "116946000000469726",
    "Success stories": "116946000000469737",
}


def extract_path(paths: list[str] | str) -> list[str] | str:
    # extract paths from a list of dict
    flat_paths = []
    if isinstance(paths, str):
        return paths
    elif isinstance(paths, dict):
        for _, path in paths.items():
            flat_paths.append(extract_path(path))

    elif isinstance(paths, list):
        for path in paths:
            flat_paths.append(extract_path(path))
    return flat_paths


def flatten(xs) -> Generator[list[str] | str | bytes, None, None]:
    # flatten list of lists
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x


def convert_md(path: str) -> tuple[str, str, str]:
    # convert md to html
    with open(path, "r") as file:
        md_text = file.read()

    docs_url = "https://docs.qfield.org"
    docs_url = path.replace("documentation", docs_url)[:-6]
    docs_url_warning = "> ***The original version of this document is located at at <{}>***\n\n".format(
        docs_url
    )

    # Check if the markdown file has the correct header and starts with a title
    parts = md_text.split("---", 2)
    if len(parts) != 3:
        raise ValueError("Markdown file {} seems to miss an header".format(path))
    _, header, body = parts
    if not body.strip().startswith("# "):
        raise ValueError("Markdown file {} seems to miss a # title".format(path))
    body = "{}{}".format(docs_url_warning, body)

    # replace relative url with absolute
    body = body.replace("../../assets/images/", "https://docs.qfield.org/assets/images/")
    body = body.replace("../assets/images/", "https://docs.qfield.org/assets/images/")
    
    # replace fancy markdown image tags with standard
    body = body.replace("!![", "![")
    body = re.sub(r"\.png,\d+px\)", ".png)", body)

    # replace emojis
    emojis = {
        ":material-monitor:": "🖥️",
        ":material-phone:": "📱",
        ":material-tablet:": "📱",
        ":material-web:": "🌐",
        ":material-usb:": "🔌",
        ":material-sd-card:": "📦",
        ":material-gps:": "🛰️",
        ":material-compass:": "🧭",
        ":material-battery:": "🔋",
        ":material-ios:": "🍏",
        ":material-android:": "🤖",
        ":material-microsoft-windows:": "🪟",
        ":material-linux:": "🐧",
        ":material-mac:": "🍎",
        ":material-apple:": "🍏",
        ":material-bee:": "🐝",
        ":material-bee-flower:": "🌼",
        ":material-check:": "✅",
        ":material-close:": "❌",
        ":material-cloud-outline:": "☁️", 
    }
    
    for emoji, char in emojis.items():
        body = body.replace(emoji, char)
    
    print(re.search(r":material-[\w-]+:", body).group(0) if re.search(r":material-[\w-]+:", body) else None)
    html = markdown.markdown(body, extensions=["tables", "admonition", "nl2br", "sane_lists", "smarty"])
    title = re.search("title: (.*)\n", header).group(1)
    slug = re.search("tx_slug: (.*)\n", header).group(1)
    return (slug, title, html)


def harmonise_permalink(permalink: str) -> str:
    # harmonise mkdocs slugs and zoho permalink
    permalink = permalink.replace("documentation_", "")
    permalink = permalink.replace("_", "-").replace(" ", "-")
    permalink = permalink.lower()
    return permalink


def get_current_articles(headers: dict[str, Any]) -> dict[str, Any]:
    # get published articles from zoho
    url = "https://desk.zoho.eu/api/v1/articles/count"
    req = requests.get(url, headers=headers)
    # map between mkdocs slugs (and zoho permalinks) and zoho api article id
    article_map = {}

    if req.status_code == 401:
        raise RuntimeError(req.text)

    count = req.json()["count"]
    step = 50  # given max by zoho api
    for counter in range(1, count, step):
        url = "https://desk.zoho.eu/api/v1/articles?categoryId=116946000000449001&from={}&limit={}".format(
            counter, step
        )
        req = requests.get(url, headers=headers)
        articles = req.json()["data"]

        for article in articles:
            permalink = harmonise_permalink(article["permalink"])
            article_map[permalink] = article["id"]

    return article_map


def push_article(
    category: str, path: str, headers: dict[str, Any], article_map: dict[str, Any]
):
    # create or update an article
    slug, title, html = convert_md(path)

    url = "https://desk.zoho.eu/api/v1/articles"

    category_id = category_map[category]
    permalink = harmonise_permalink(slug)
    payload = {
        "permission": "ALL",
        "title": title,
        "permalink": permalink,
        "answer": html,
        "categoryId": category_id,
        "status": "Published",
    }

    if permalink in article_map:
        url = "{}/{}".format(url, article_map[permalink])
        req = requests.patch(url, json=payload, headers=headers)
        print(
            "updating: ",
            permalink,
            "id: ",
            article_map[permalink],
            ": ",
            req.status_code,
        )
    else:
        url = "{}?".format(url)
        req = requests.post(url, json=payload, headers=headers)
        print("creating: ", permalink, ": ", req.status_code)

    if req.status_code >= 400:
        raise RuntimeError(req.text)


def get_headers() -> dict:
    auth_code = get_fresh_token()

    if not auth_code:
        exit("ERROR: use generate_zoho_auth.py to generate the oauth2 code")
    return {
        "Authorization": "Zoho-oauthtoken " + auth_code,
    }


def main():
    # skip !ENV tags see https://github.com/yaml/pyyaml/issues/86
    yaml.add_multi_constructor("!ENV", lambda loader, suffix, node: None)

    with open("mkdocs.yml", "r") as file:
        # NOTE please do not use the `full_load` or `yaml.FullLoader` as there is way too much magic in the `mkdocs.yml` file and it breaks miserably.
        config = yaml.load(file, Loader=yaml.BaseLoader)

    articles = config["nav"]
    headers = get_headers()

    for category in articles:

        for category_title, paths in category.items():
            paths = extract_path(paths)

            if isinstance(paths, str):
                paths = [paths]
            else:
                paths = list(flatten(paths))

            if os.getenv("IS_PR") in ("true", True):
                print(
                    "Not running in PRs, but at least it seems that all imports were resolved."
                )
                exit(0)

            article_map = get_current_articles(headers)

            for path in paths:
                if path == "index.md":
                    continue
                path = "documentation/{}.en.md".format(path[:-3])
                if os.path.exists(path):
                    print("Processing: ", path)
                    push_article(category_title, path, headers, article_map)
                else:
                    raise FileNotFoundError("File missing: ", path)


if __name__ == "__main__":
    if os.getenv("IS_PR") in ("true", True):
        print(
            "Not running in PRs, but at least it seems that all imports were resolved."
        )
        exit(0)
    main()
