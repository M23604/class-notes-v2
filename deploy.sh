#!/usr/bin/env sh
mkdocs build
mkdocs gh-deploy
git commit -m "{$1}"
git push -u origin master
