#!/bin/bash

# Exit on error
set -e

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/../..

if test "$TRAVIS_SECURE_ENV_VARS" = "true" -a "$TRAVIS_BRANCH" = "master";
then
  echo "Publish docs to https://qfield.github.io/docs";

  pushd ${DIR}
  mkdir publish
  cd publish
  git clone git@github.com:opengisch/QField.git --branch gh-pages
  mkdir -p QField/docs
  cd QField/docs
  git rm . -r || true
  cp ../../../build/html/* . -r
  git add -A
  git commit -m "Automatic doc update\n\nhttps://github.com/opengisch/QField-docs/commit/${TRAVIS_COMMIT}"
  git push
  popd
else
  echo "Not publishing: Not the latest master version."
fi
