#!/bin/zsh
REPO_NAME=chau-custom
REPO_PATH=/home/chau/Resources/ChauRepo

build_packages() {
    for package in *
    do
        if [[ -f $package || "$package" == version-check ]]
        then
            continue
        fi
        cd $package
        echo $package
        if [[ "$(find -maxdepth 1 -iname '*.pkg.tar.*')" == "" ]];
        then
            makepkg -s
            makepkg --printsrcinfo > .SRCINFO
        fi
        cd ..
    done
}

create_repo() {
    rm -rf "${REPO_PATH}"
    mkdir "${REPO_PATH}"
    cp */*.pkg.tar.* "${REPO_PATH}"
    repo-add "${REPO_PATH}/${REPO_NAME}.db.tar.zst" "${REPO_PATH}"/*.pkg.tar.*
    cd -
}

build_packages
create_repo
