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
HEADERS = {
        'Authorization': "Zoho-oauthtoken "+ AUTH_CODE,
    }


category_map = {
    'Get started': '116946000000448345',
    'How-to guides': '116946000000448334',
    'Technical reference': '116946000000469726',
    'Success stories': '116946000000469737',
}

article_map = {}



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


def harmonise_permalink(permalink):
    permalink = permalink.replace('documentation_', 'test_')
    permalink = permalink.replace('_', '-').replace(' ', '-')
    permalink = permalink.lower()

    return permalink


def get_current_articles():
    url = 'https://desk.zoho.eu/api/v1/articles/count'
    req = requests.get(url, headers=HEADERS)
    if req.status_code == 401:
        raise RuntimeError(req.text)
    count = req.json()['count']

    step = 50
    for counter in range(1, count, step):
        url = 'https://desk.zoho.eu/api/v1/articles?categoryId=116946000000449001&from={}&limit={}'.format(counter, step)
        req = requests.get(url, headers=HEADERS)
        articles = req.json()['data']
        for article in articles:
            permalink = harmonise_permalink(article['permalink'])
            article_map[permalink] = article['id']

    return article_map


def push_article(category, path):
    slug, title, html = convert_md(path)

    url = 'https://desk.zoho.eu/api/v1/articles'

    category_id = category_map[category]
    permalink = harmonise_permalink(slug)
    payload = {
        "permission" : "ALL",
        "title" : title,
        "permalink" : permalink,
        "answer" : html,
        "categoryId" : category_id,
        "status" : "Published"
        }

    if permalink in article_map:
        url = '{}/{}'.format(url, article_map[permalink])
        req = requests.patch(url, json = payload, headers=HEADERS)
        print('updating: ', permalink, 'id: ', article_map[permalink], ': ', req.status_code)
    else:
        url = '{}?'.format(url)
        req = requests.post(url, json = payload, headers=HEADERS)
        print('creating: ', permalink, ': ', req.status_code)

    if req.status_code == 401:
        raise RuntimeError(req.text)

####################################
#######Main#########################
####################################

with open('mkdocs.yml', 'r') as file:
    config = yaml.full_load(file)
articles = config['nav']

get_current_articles()

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
            push_article(category_title, path)
