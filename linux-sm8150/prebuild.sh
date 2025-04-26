#!/usr/bin/env bash

VERSION=$(grep Version: linux-sm8150.spec | awk '{print $2}')

wget -nc "https://gitlab.com/sm8150-mainline/linux/-/archive/sm8150/$VERSION/linux-sm8150-$VERSION.tar.gz"