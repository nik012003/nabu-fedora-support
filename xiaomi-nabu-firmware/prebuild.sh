#!/usr/bin/env bash

VERSION=$(grep Version: xiaomi-nabu-firmware.spec | awk '{print $2}')

rm -f "xiaomi-nabu-firmware-$VERSION.tar.gz"
tar -czf "xiaomi-nabu-firmware-$VERSION.tar.gz" src