#!/bin/sh
find . -maxdepth 2 -name '*.pkg.tar*'
echo 'Do you want to delete them? [y/N]'
read confirmed
if [ "$confirmed" == y ]; then
    find . -maxdepth 2 -name '*.pkg.tar*' -exec rm {} \;
fi