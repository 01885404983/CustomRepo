#!/bin/zsh
for package in *
do
    if [[ -f $package || "$package" == version-check ]]
    then
        continue
    fi
    cd $package
    echo $package
    if find -maxdepth 1 -iname '*.pkg.tar.*' > /dev/null
    then
        makepkg --printsrcinfo > .SRCINFO
    fi
    cd ..
done