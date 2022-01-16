"""
Generate a video for each track.
"""
import subprocess
from util import tracks

duration = 3 * 60

def make_video(track):
  if track['video_file'].exists():
    return

  cmd = [
    'ffmpeg',
    '-y', # overwrite
    '-loop', '1',
    '-i', track['captioned_image_file'],
    '-i', track['path'],
    '-t', str(duration),
    '-filter:v', f'fade=out:st={duration-2}:d=2',
    '-filter:a', f'afade=out:st={duration-2}:d=2',
    # '-c:a', 'copy', # copy audio, don't re-encode
    '-c:v', 'libx264',
    '-crf', '20',
    '-pix_fmt', 'yuv420p',
    '-shortest',
    track['video_file'],
  ]
  subprocess.run(cmd)

for i, track in enumerate(tracks, 1):
  print(f"{i}. {track['path']}")
  make_video(track)
