#!/usr/bin/env bash

port=8080

repo="marc"
name="healthapp"
version="latest"

target_img="${repo}/${name}:${version}"

cmd="docker run --rm -idt -p ${port}:${port} --name healthapp ${target_img}"
echo ${cmd}
eval ${cmd}

docker container ls | grep ${name}

sleep 7

python -m webbrowser -t "http://localhost:${port}/polls/happ" 