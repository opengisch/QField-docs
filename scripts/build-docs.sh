#!/bin/bash

# Exit on error
set -e

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/..
pushd ${DIR}
make clean
make html
# make all-pdf # latex doesn't like utf-8
popd
