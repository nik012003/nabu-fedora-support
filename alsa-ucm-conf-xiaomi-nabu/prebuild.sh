#!/usr/bin/env bash

VERSION=$(grep Version: alsa-ucm-conf-xiaomi-nabu.spec | awk '{print $2}')

rm -f "alsa-ucm-conf-xiaomi-nabu-$VERSION.tar.gz"
tar -czf "alsa-ucm-conf-xiaomi-nabu-$VERSION.tar.gz" src