#!/bin/bash

IMAGE_NAME=post-file-server

if [[ $(docker images | grep $IMAGE_NAME) ]]; then
    echo "Removing old image..."
    docker rmi $IMAGE_NAME
fi

docker build -t $IMAGE_NAME .
