#!/bin/bash
if test "$TRAVIS_SECURE_ENV_VARS" = "true" -a "$TRAVIS_BRANCH" = "master";
then
  printf "[https://www.transifex.com]\nusername = opengisch\npassword = $TRANSIFEX_PASSWORD\n" > ~/.transifexrc
  ./scripts/create_transifex_resources.sh;
  tx push -s
fi
