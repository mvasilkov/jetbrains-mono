#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

./sources/build-webfonts.sh
./scripts/write_styles.py
node-sass -o css scss/jetbrains-mono.scss
node-sass -o css scss/jetbrains-mono-nl.scss
