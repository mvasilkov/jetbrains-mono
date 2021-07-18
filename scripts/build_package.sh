#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

# clean
DIRS='css scss test'
rm -rf $DIRS
mkdir -p $DIRS

# build
./sources/build-webfonts.sh
./scripts/write_styles.py
./node_modules/.bin/node-sass -o css scss/jetbrains-mono.scss
./node_modules/.bin/node-sass -o css scss/jetbrains-mono-nl.scss
