#!/usr/bin/env bash

repo="marc"
name="healthapp"
version="latest"

target_img="${repo}/${name}:${version}"

printf "Build image %s\n" "${image}"

docker build -t ${target_img} --build-arg BASE_CONTAINER=${target_img} .
docker tag "${target_img}" "${repo}/${name}:latest"

printf "Tag %s as latest\n" "${repo}/${name}:latest"
docker tag ${target_img} "${repo}/${name}:latest"

docker images | grep ${name}
