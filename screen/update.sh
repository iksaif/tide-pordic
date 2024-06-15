#!/bin/sh

set -x

URL="$1"
SCREEN="screen.bmp"

TEMP=$(mktemp "$(basename "$0")-XXX")
trap "rm -f ${TEMP}" EXIT

cd $(dirname $0)
curl ${URL} -o ${TEMP}
convert ${TEMP} -dither FloydSteinberg -define dither:diffusion-amount=90%  -remap eink-2color.png BMP3:${SCREEN}
python3 update.py --image ${SCREEN}

