import os
import glob
import re

TX_ORGANIZATION = "opengisch"
TX_PROJECT = "qfield-documentation"
TX_SOURCE_LANG = "en"
TX_TYPE = "GITHUBMARKDOWN"

def create_transifex_config():
    """ Parse all source documentation files and add the ones with tx_slug metadata
    defined to transifex config file.
    """
    print("Start creating transifex configuration")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(current_dir, "..", ".tx", "config")
    root = os.path.join(current_dir, "..")
    count = 0

    with open(config_file, "w") as f:
        f.write("[main]\n")
        f.write("host = https://www.transifex.com\n\n")

        for file in glob.iglob(current_dir + '/../documentation/**/*.en.md', recursive=True):

            # Get relative path of file
            relative_path = os.path.relpath(file, start = root)

            tx_slugs = [re.match(r"^tx_slug: +(.*)", line) for line in open(file)]
            tx_slugs = [t for t in tx_slugs if t]

            if not tx_slugs:
                print(f"No TX slug found for {relative_path}")

            if len(tx_slugs) > 1:
                print(f"More than 1 TX slug found for {relative_path}")

            if tx_slugs:
                tx_slug = tx_slugs[0].group(1)
                print(
                    f"Found file with tx_slug defined: `{relative_path}`, `{tx_slug}`"
                )
                f.write(f"[o:{TX_ORGANIZATION}:p:{TX_PROJECT}:r:{tx_slug}]\n")
                f.write(
                    f"file_filter = {''.join(relative_path.split('.')[:-2])}.<lang>.md\n"
                )
                f.write(f"source_file = {relative_path}\n")
                f.write(f"source_lang = {TX_SOURCE_LANG}\n")
                f.write(f"type = {TX_TYPE}\n\n")
                count += 1

    print(f"Transifex configuration created. {count} resources added.")

create_transifex_config()
