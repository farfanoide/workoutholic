#!/usr/bin/env bash

archive_name='fixture_images.tar.gz'
images_url="https://www.dropbox.com/s/8abt9s859pq9gz2/${archive_name}?dl=1"

curl -LSC - "${images_url}" \
    -o "${archive_name}" \
    && tar -xzf "${archive_name}"

