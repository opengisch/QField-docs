#!/usr/bin/env bash

set -e

pre-commit install
pre-commit run --files mkdocs.yml || true

if [[ $(git diff --exit-code mkdocs.yml) ]]; then
  git config --global user.email "github-actions[bot]@users.noreply.github.com"
  git config --global user.name "github-actions[bot]"

  echo "detected changes in mkdocs.yml"
  git stash push -- mkdocs.yml
  if [[ ${GITHUB_EVENT_NAME} == "pull_request" ]]; then
    git stash pop
    git add mkdocs.yml
    git commit -m "Update mkdocs.yml translation" --no-verify
    git push
  else
    git stash pop
    git add mkdocs.yml
    git commit -m "Update mkdocs.yml translation" --no-verify
    git push -u origin ${GITHUB_REF_NAME}
  fi
else
  echo "no change mkdocs.yml"
fi
