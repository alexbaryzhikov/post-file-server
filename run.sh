#!/bin/bash

IMAGE_NAME=post-file-server

if [[ ! $(docker images | grep $IMAGE_NAME) ]]; then
    echo "Docker image not found. Run 'build.sh' first."
    exit 1
fi

while [ -n "$1" ]; do
    case "$1" in
    -u | --upload-dir)
        [ -n "$2" ] && UPLOAD_DIR=$2
        shift
        ;;
    -p | --port)
        [ -n "$2" ] && PORT=$2
        shift
        ;;
    -h | --help)
        echo -e \
            "Usage: $(basename $0) [ARG...]\n" \
            "\n" \
            "  -u, --upload-dir DIR  directory to place uploaded files\n" \
            "  -p, --port PORT       port to listen to\n" \
            "  -h, --help            display this help and exit"
        exit 0
        ;;
    *)
        echo "Bad argument: $1"
        exit 2
        ;;
    esac
    shift
done

[ -n "$PORT" ] || PORT=5000
[ -n "$UPLOAD_DIR" ] || UPLOAD_DIR=$PWD

IPV4_ADDR=$(ip addr show scope global |
    grep -A2 -E "state UP" |
    grep -oE "[[:digit:]]+\.[[:digit:]]+\.[[:digit:]]+\.[[:digit:]]+" |
    head -n1)
echo "Base URL: http://$IPV4_ADDR:$PORT/"
echo "Upload dir: $UPLOAD_DIR"

USER_ID=$(id -u $USER)
GROUP_ID=$(id -g $USER)

docker run -i --rm \
    -v $UPLOAD_DIR:/upload \
    -e UPLOAD_DIR=/upload \
    -p $PORT:5000 \
    -u $USER_ID:$GROUP_ID \
    $IMAGE_NAME
