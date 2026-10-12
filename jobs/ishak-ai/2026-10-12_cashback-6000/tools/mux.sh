#!/bin/bash
# usage: mux.sh <framesDir> <sourceVideo> <sfx.wav> <out.mp4>
set -e
F=$1; SRC=$2; SFX=$3; OUT=$4
ffmpeg -v error -y -framerate 30 -i "$F/%05d.jpg" -i "$SRC" -i "$SFX" \
  -filter_complex "[1:a]aresample=48000,pan=stereo|c0=c0|c1=c0,apad=whole_dur=28.9[v];[2:a]aresample=48000,pan=stereo|c0=c0|c1=c0,volume=0.30[s];[v][s]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.95[a]" \
  -map 0:v -map "[a]" -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p -profile:v high -r 30 \
  -c:a aac -b:a 192k -t 28.9 -movflags +faststart "$OUT"
