#!/bin/bash

# Exit on error
set -e

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/..
pushd ${DIR}
make clean
if test "$TRAVIS_SECURE_ENV_VARS" = "true" -a "$TRAVIS_BRANCH" = "master";
then
    echo -e "[https://www.transifex.com]\nhostname = https://www.transifex.com\nusername = opengisch\npassword = $TRANSIFEX_PASSWORD\ntoken =\n" > ~/.transifexrc
    make transifex_pull
else
    echo "Skipping translation because we are not on a secure master branch and therefore do not provide authentication for transifex."
fi
make html
# make all-pdf # latex doesn't like utf-8
popd
