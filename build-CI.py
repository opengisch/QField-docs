#!/usr/bin/env python

"""
This builds the documentation in parallel, with a single (mono-lingual) search index each time,
allowing to side-step the "crowded index" + slow builds problems.

Requirements:

*** Env file ***

.env
----
# example #
TX_TOKEN=<token>
LANGUAGE_CODES=de,en,es,fr,it
LANGUAGES=Deutsch,English,Espagñol,Français,Italien

*** Image and container ***

An image built from:

    docker build . -f Dockerfile-CI --build-arg tx_token=... -t qfield-docs

and run as:

    docker run -it -v ${PWD}/build:/opt/app/build --rm qfield-docs

"""
from collections import namedtuple
from os import environ
from dotenv import load_dotenv
from subprocess import Popen, PIPE
from timeit import default_timer

Config = namedtuple(
    "Config", ["languages", "website_default_language", "output_dir", "temp_lang_dir"]
)


def set_config() -> Config:
    """Import languages from an .env file"""
    language_codes = environ.get("LANGUAGE_CODES").split(",")
    languages_names = environ.get("LANGUAGES").split(",")
    return Config(
        languages=dict(zip(language_codes, languages_names)),
        website_default_language="en",
        output_dir="build",
        temp_lang_dir="more_languages",
    )


def construct_build_cmd(config: Config, language_code: str) -> list[str]:
    """Build the shell command to call the subprocess with"""
    return [
        "env",
        f"LANG={language_code}",
        "mkdocs",
        "build",
        "-d",
        f"{config.output_dir}"
        if language_code == config.website_default_language
        else f"{config.output_dir}/{language_code}",
    ]


def run_builds(config: Config):
    """Build all languages available as config.languages in parallel"""
    t0 = default_timer()
    try:
        futures = [
            Popen(
                construct_build_cmd(config=config, language_code=lang_code),
                stdout=PIPE,
                universal_newlines=True,
            )
            for lang_code in config.languages
        ]

        for f in futures:
            f.wait()

        if any(p.returncode != 0 for p in futures):
            raise Exception("A build process failed; please restart.")

        t1 = default_timer()
        print(
            f"Built docs for {len(config.languages)} languages ({', '.join(config.languages.values())}) in {round(t1-t0, 2)} seconds"
        )

    except Exception as error:
        print(f"Failed! This exception occured: {error}")


if __name__ == "__main__":
    load_dotenv()
    run_builds(set_config())
