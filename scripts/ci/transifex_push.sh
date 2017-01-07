#!/bin/bash
if test "$TRAVIS_SECURE_ENV_VARS" = "true" -a "$TRAVIS_BRANCH" = "master";
then
  echo -e "[https://www.transifex.com]\nhostname = https://www.transifex.com\nusername = opengisch\npassword = $TRANSIFEX_PASSWORD\ntoken =\n" > ~/.transifexrc
  ./scripts/create_transifex_resources.sh;
  tx push -s
fi
