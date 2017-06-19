#!/usr/bin/env bash

archive_name='fixture_images.tar.gz'
images_url="https://www.dropbox.com/s/8abt9s859pq9gz2/${archive_name}?dl=1"

if [ ! -e "${archive_name}" ]; then
    curl -LSC - "${images_url}" -o "${archive_name}"
fi

tar -xzf "${archive_name}"
