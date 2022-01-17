"""
For each track, generate a video file using the cover art. Add fade-in and fade-out effects. Do not include audio stream
in the generated video file. This script takes a surprisingly long time to run.
"""
import subprocess
from util import tracks



def make_video(track):
  if track['video_file'].exists():
    return

  # cmd = [
  #   'ffmpeg',
  #   '-y', # overwrite
  #   '-loop', '1',
  #   '-i', track['captioned_image_file'],
  #   '-i', track['path'],
  #   '-t', str(duration),
  #   '-filter:v', f'fade=in:st=0:d=2, fade=out:st={duration-2}:d=2',
  #   '-filter:a', f'afade=out:st={duration-2}:d=2',
  #   # '-c:a', 'copy', # you cannot use streamcopy when you use filters
  #   '-c:v', 'libx264',
  #   "-c:a", "libfdk_aac", # use best encoder
  #   "-vbr", "4", # use high quality (5 is highest)
  #   '-crf', '20',
  #   '-pix_fmt', 'yuv420p',
  #   '-shortest',
  #   track['video_file'],
  # ]
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
