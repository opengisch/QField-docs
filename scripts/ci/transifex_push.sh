#!/bin/bash
if test "$TRAVIS_SECURE_ENV_VARS" = "true" -a "$TRAVIS_BRANCH" = "master";
then
  ./scripts/create_transifex_resources.sh;
  tx init --user=opengisch --pass=$TRANSIFEX_PASSWORD
  tx push -s
fi
