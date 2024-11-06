#!/usr/bin/env bash
set -e
COPR_PROJECT="nabu-support"
RELEASE_VER="f41"

projects=(alsa-ucm-conf-xiaomi-nabu tqftpserv xiaomi-nabu-firmware)

# Build all projects if no arguments are passed
if [ "$#" -gt 0 ]; then
    projects=("$@")
fi

for project in "${projects[@]}"; do
    echo "[*] Building $project"
    cd "$project" || (echo "Error: $project not found" && exit)
    # Run prebuild.sh if exists
    if [ -f prebuild.sh ]; then
        echo "[*] Running prebuild.sh for $project"
        ./prebuild.sh
    fi
    spectool -g "$project".spec
    if [ "$LOCAL" == "1" ]; then 
        fedpkg --release $RELEASE_VER local
    else
        fedpkg --release $RELEASE_VER copr-build $COPR_PROJECT --nowait
    fi
    cd ..
done