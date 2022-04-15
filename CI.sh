#!/usr/bin/env sh

pip3 install mkdocs
pip3 install mkdocs-material

mkdocs build
mkdocs gh-deploy
git add -f site && git commit -m "Make Relevant Changes to the Site"
