import yaml
import markdown
import re
import requests

import os.path
import materialx.emoji

from collections.abc import Iterable


AUTH_CODE = ''
if not AUTH_CODE:
    exit("ERROR: use generate_zoho_auth.py to generate the oauth2 code")


category_map = {
    'Get started': '116946000000448345',
    'How-to guides': '116946000000448334',
    'Technical reference': '116946000000469726',
    'Success stories': '116946000000469737',
}


# skip !ENV tags see https://github.com/yaml/pyyaml/issues/86
yaml.add_multi_constructor('!ENV', lambda loader, suffix, node: None)


def extract_path(paths):
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


def flatten(xs):
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x


def convert_md(path):
    with open(path, 'r') as file:
        md_text = file.read()

    docs_url = "https://docs.qfield.org"
    docs_url = path.replace('documentation', docs_url)[:-6]
    docs_url_warning = "> ***The complete documentation is at <{}>***\n\n".format(docs_url)

    header, body = md_text.split('#', 1)
    body = "{}#{}".format(docs_url_warning, body)

    #replace relative url with absolute
    body = body.replace('../assets/images/', 'https://docs.qfield.org/assets/images/')
    
    html = markdown.markdown(body)
    title = re.search('title: (.*)\n', header).group(1)
    slug = re.search('tx_slug: (.*)\n', header).group(1)
    return(slug, title, html)


def publish_article(category, path):
    slug, title, html = convert_md(path)

    url = 'https://desk.zoho.eu/api/v1/articles?'

    category_id = category_map[category]
    payload = {
        "permission" : "ALL",
        "title" : title,
        "permalink" : slug,
        "answer" : html,
        "categoryId" : category_id,
        "status" : "Published"
        }
    headers = {
        'Authorization': "Zoho-oauthtoken "+ AUTH_CODE,
    }

    req = requests.post(url, json = payload, headers=headers)
    print('pushing: ', slug, ': ', req.status_code)
    if req.status_code == 401:
        raise RuntimeError(req.text)
        

####################################
#######Main#########################
####################################

with open('mkdocs.yml', 'r') as file:
    config = yaml.full_load(file)
articles = config['nav']

for category in articles: 
    for category_title, paths in category.items():
        paths = extract_path(paths)
        if isinstance(paths, str):
            paths = [paths]
        else:
            paths = list(flatten(paths))
        
        for path in paths:
            if path == "index.md":
                continue
            path =  "documentation/{}.en.md".format(path[:-3])
            publish_article(category_title, path)
