#!/usr/bin/env sh

pip3 install -r requirements.txt

mkdocs build
mkdocs gh-deploy
