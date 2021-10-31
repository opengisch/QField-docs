
import os
import yaml
import shutil
import tempfile
from github import Github
from dotenv import load_dotenv
from mkdocs.commands import build
from mkdocs import config

def download_github_directory(repo, remote_path, local_path):
    load_dotenv()

    github = Github(os.getenv("GITHUB_TOKEN"))
    repository = github.get_repo(repo)

    contents = repository.get_contents(remote_path)
    # os.makedirs(os.path.join(local_path, remote_path))

    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repository.get_contents(file_content.path))
            # os.makedirs(os.path.join(local_path, file_content.path))
        else:
            with open(os.path.join(local_path, file_content.name), "wb") as f:
                f.write(file_content.decoded_content)


def update_mkdocs_yml():
    pass


if __name__ == "__main__":

    # Create a temp directory
    temp_dir = tempfile.mkdtemp()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    print(temp_dir)

    # Copy this repo to temp directory
    shutil.copytree(current_dir, temp_dir, dirs_exist_ok=True)

    # Download directories from other repos into temp directory at the correct place
    download_github_directory(
        "opengisch/opencomptage",
        "docs",
        os.path.join(temp_dir, 'docs', 'reference', 'qfieldcloud'))

    # List md files in downloaded directories
    files = ["reference/qfieldcloud/" + f for f in os.listdir(os.path.join(temp_dir, 'docs', 'reference', 'qfieldcloud')) if f.endswith(".md")]

    # Update temp/mkdocs.yml with files from other repos
    with open(os.path.join(temp_dir, 'mkdocs.yml')) as f:
        mkdocs_yml = yaml.safe_load(f)
        navs = mkdocs_yml["nav"]

        for nav in navs:
            print(nav)
            if "Technical reference" in nav:
                print("NPLA")
                nav.update({"Technical reference": ["reference.md", {"QFfieldCloud": files}]})
            print(nav)
        print(navs)
    with open(os.path.join(temp_dir, 'mkdocs.yml'), 'w') as f:
        yaml.dump(mkdocs_yml, f)

    # Build mkdocs into build directory
    build.build(config.load_config(config_file=os.path.join(temp_dir, 'mkdocs.yml'), site_dir=os.path.join(current_dir, 'build')))
