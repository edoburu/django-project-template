#!/bin/sh
#
# This is the most simplistic Sass compilation script.
# 
cd `dirname $0`
npm run gulp sass:watch

# sass --load-path=frontend/sass-vendor/ --compass --style=expanded --sourcemap=auto --precision=5 --watch frontend/sass/:frontend/static/frontend/css/ "$@"
