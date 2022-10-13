import os
import glob
import frontmatter

TX_ORGANIZATION = "opengisch"
TX_PROJECT = "qfield-documentation"
TX_SOURCE_LANG = "en"
TX_TYPE = "GITHUBMARKDOWN"

def create_transifex_config():
    """ Parse all source documentation files and add the ones with tx_slug metadata
    defined to transifex config file.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(current_dir, "..", ".tx", "config")
    root = os.path.join(current_dir, "..")

    with open(config_file, "w") as f:
        f.write("[main]\n")
        f.write("host = https://www.transifex.com\n\n")

        for file in glob.iglob(current_dir + '/../documentation/**/*.en.md', recursive=True):

            # Get relative path of file
            relative_path = os.path.relpath(file, start = root)

            tx_slug = frontmatter.load(file).get('tx_slug', None)

            if tx_slug:
                f.write(f"[o:{TX_ORGANIZATION}:p:{TX_PROJECT}:r:{tx_slug}]\n")
                f.write(f"file_filter = {''.join(relative_path.split('.')[:-2])}.<lang>.md\n")
                f.write(f"source_file = {relative_path}\n")
                f.write(f"source_lang = {TX_SOURCE_LANG}\n")
                f.write(f"type = {TX_TYPE}\n\n")

create_transifex_config()
