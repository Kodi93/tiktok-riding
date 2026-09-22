#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "usage: $0 master.mp4 [master2.mp4 ...]" >&2
  exit 2
fi

command -v ffprobe >/dev/null || { echo "ffprobe is required" >&2; exit 2; }
command -v ffmpeg >/dev/null || { echo "ffmpeg is required" >&2; exit 2; }

failed=0
for file in "$@"; do
  echo "== $file =="
  if [[ ! -s "$file" ]]; then
    echo "FAIL: missing or empty file" >&2
    failed=1
    continue
  fi

  vcodec=$(ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=nw=1:nk=1 "$file")
  width=$(ffprobe -v error -select_streams v:0 -show_entries stream=width -of default=nw=1:nk=1 "$file")
  height=$(ffprobe -v error -select_streams v:0 -show_entries stream=height -of default=nw=1:nk=1 "$file")
  pix_fmt=$(ffprobe -v error -select_streams v:0 -show_entries stream=pix_fmt -of default=nw=1:nk=1 "$file")
  fps=$(ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of default=nw=1:nk=1 "$file")
  acodec=$(ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of default=nw=1:nk=1 "$file")
  sample_rate=$(ffprobe -v error -select_streams a:0 -show_entries stream=sample_rate -of default=nw=1:nk=1 "$file")
  channels=$(ffprobe -v error -select_streams a:0 -show_entries stream=channels -of default=nw=1:nk=1 "$file")
  duration=$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$file")

  [[ "$vcodec" == "h264" ]] || { echo "FAIL: video codec=$vcodec (want h264)" >&2; failed=1; }
  [[ "$width" == "1080" && "$height" == "1920" ]] || { echo "FAIL: geometry=${width}x${height} (want 1080x1920)" >&2; failed=1; }
  [[ "$pix_fmt" == "yuv420p" ]] || { echo "FAIL: pixel format=$pix_fmt (want yuv420p)" >&2; failed=1; }
  [[ "$fps" == "30/1" ]] || { echo "FAIL: frame rate=$fps (want 30/1)" >&2; failed=1; }
  [[ "$acodec" == "aac" ]] || { echo "FAIL: audio codec=$acodec (want aac)" >&2; failed=1; }
  [[ "$sample_rate" == "48000" ]] || { echo "FAIL: sample rate=$sample_rate (want 48000)" >&2; failed=1; }
  [[ "$channels" == "2" ]] || { echo "FAIL: channels=$channels (want 2)" >&2; failed=1; }
  awk -v d="$duration" 'BEGIN { exit !(d >= 4 && d <= 60) }' || { echo "FAIL: duration=$duration (want 4–60 seconds)" >&2; failed=1; }

  if ! ffmpeg -v error -i "$file" -f null -; then
    echo "FAIL: decode test failed" >&2
    failed=1
  elif [[ "$vcodec" == "h264" && "$width" == "1080" && "$height" == "1920" && "$pix_fmt" == "yuv420p" && "$fps" == "30/1" && "$acodec" == "aac" && "$sample_rate" == "48000" && "$channels" == "2" ]]; then
    echo "PASS: TikTok master profile and full decode"
  fi
done

exit "$failed"