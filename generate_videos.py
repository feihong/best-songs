"""
For each track, generate a video file using the cover art. Add fade-in and fade-out effects. Do not include audio stream
in the generated video file. This script takes a surprisingly long time to run.
"""
import subprocess
from util import tracks



def make_video(track):
  if track['video_file'].exists():
    return

  duration = track['duration']

  cmd = [
    'ffmpeg',
    '-loop', '1',
    '-i', track['captioned_image_file'],
    '-t', str(duration),
    '-filter:v', f'fade=in:st=0:d=2, fade=out:st={duration-2}:d=2',
    '-c:v', 'libx264',
    '-crf', '20',
    '-pix_fmt', 'yuv420p',
    track['video_file'],
  ]
  subprocess.run(cmd)

for i, track in enumerate(tracks, 1):
  print(f"{i}. {track['path']}")
  make_video(track)
