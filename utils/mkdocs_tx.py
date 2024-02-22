#!/usr/bin/env python

import argparse
import copy

from ruamel.yaml import YAML

# This scripts helps with translatable content from mkdocs.yml
# It provides commands:
#   * to create the YAML translatable file
#   * to update the mkdocs.yml with the translated content


def read_config(file_path: str):
    yaml = YAML(typ="rt")
    yaml.preserve_quotes = True
    with open(file_path) as f:
        return yaml.load(f)


def nav_config(config) -> dict:
    _nav_config = {}

    def add_nav_entry(title, content):
        if title:
            _nav_config[title] = title
        for _entry in content:
            if type(_entry) == str:
                # this is pointing to a page directly, skipping
                continue
            for _title, _content in _entry.items():
                add_nav_entry(_title, _content)

    add_nav_entry(None, config["nav"])

    return _nav_config


def site_description(config, source_language) -> str:
    _site_description = None
    found = 0
    try:
        _site_description = config["site_description"]
        found += 1
    except KeyError:
        pass
    try:
        for plugin in config["plugins"]:
            if not isinstance(plugin, str) and "i18n" in plugin:
                for lang_info in plugin["i18n"]["languages"]:
                    lang = lang_info["locale"]
                    if lang == source_language:
                        _site_description = lang_info["site_description"]
                        found += 1
    except KeyError:
        pass
    if not found:
        print("No site description found")
    elif found > 1 and _site_description != config["site_description"]:
        print("ERROR: site description found twice and different")
        assert False

    return _site_description


def create_translation_source(config_path, source_path, source_language):
    config = read_config(config_path)

    tx_cfg = {
        "nav": nav_config(config),
        "site_description": site_description(config, source_language)
    }

    try:
        tx_cfg["theme"] = {"palette": []}
        for palette in config["theme"]["palette"]:
            tx_cfg["theme"]["palette"].append(
                {"toggle": {"name": palette["toggle"]["name"]}}
            )
    except KeyError:
        print("No theme/palette/toggle/name to translate")

    with open(source_path, "w") as f:
        yaml = YAML()
        yaml.dump(tx_cfg, f)


def update_config(config_path, source_path, source_language):
    config = read_config(config_path)

    found = False
    for plugin in config["plugins"]:
        if type(plugin) != str and "i18n" in plugin:
            found = True
            for lang_info in plugin["i18n"]["languages"]:
                lang = lang_info["locale"]
                print(f"language found: '{lang}'")

                if lang == source_language:
                    print("skipping source language")
                    continue

                tx_file = f'{source_path.removesuffix(".yml")}.{lang}.yml'
                with open(tx_file) as f:
                    yaml = YAML()
                    tx = yaml.load(f)

                    for _title, _translation in tx["nav"].items():
                        if not _translation:
                            tx["nav"][_title] = _title
                    lang_info["nav_translations"] = tx["nav"]

                    try:
                        lang_info["site_description"] = tx["site_description"] or site_description(config, source_language)
                    except KeyError:
                        print("No site description in translation")

                    try:
                        lang_info["palette"] = copy.deepcopy(config["theme"]["palette"])
                        i = 0
                        for palette in tx["theme"]["palette"]:
                            _name = (
                                palette["toggle"]["name"]
                                or config["theme"]["palette"][i]["toggle"]["name"]
                            )
                            lang_info["palette"][i]["toggle"]["name"] = _name
                            i += 1
                    except KeyError:
                        print("No theme/palette/toggle/name in translation")

    assert found

    with open(config_path, "w") as f:
        yaml = YAML()
        yaml.indent(mapping=2, sequence=4, offset=2)
        yaml.dump(config, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--config_path", default="mkdocs.yml", help="mkdocs.yml complete path"
    )
    parser.add_argument(
        "-s", "--source_language", default="en", help="source language of the config"
    )
    parser.add_argument(
        "-t",
        "--translation_file_path",
        default="mkdocs_tx.yml",
        help="Translation file to create and translate",
    )

    subparsers = parser.add_subparsers(title="command", dest="command")

    # create the parser for the create_source command
    parser_source = subparsers.add_parser(
        "create_source", help="Creates the source file to be translated"
    )

    # create the parser for the update_config command
    parser_update = subparsers.add_parser(
        "update_config",
        help="Updates the mkdocs.yml config file from the downloaded translated files",
    )

    args = parser.parse_args()

    if args.command == "create_source":
        create_translation_source(args.config_path, args.translation_file_path, args.source_language)

    elif args.command == "update_config":
        update_config(
            args.config_path, args.translation_file_path, args.source_language
        )

    else:
        raise ValueError
