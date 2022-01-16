"""
Generate a video for each track.
"""
import subprocess
from util import tracks

max_duration = 3 * 60

# https://video.stackexchange.com/a/23109
def make_video(track):
  if track['video_file'].exists():
    return

  duration = min(max_duration, track['duration'])

  cmd = [
    'ffmpeg',
    '-y', # overwrite
    '-loop', '1',
    '-i', track['captioned_image_file'],
    '-i', track['path'],
    '-t', str(duration),
    '-filter:v', f'fade=in:st=0:d=2, fade=out:st={duration-2}:d=2',
    '-filter:a', f'afade=out:st={duration-2}:d=2',
    # '-c:a', 'copy', # you cannot use streamcopy when you use filters
    '-c:v', 'libx264',
    "-c:a", "libfdk_aac", # use best encoder
    "-vbr", "4", # use high quality (5 is highest)
    '-crf', '20',
    '-pix_fmt', 'yuv420p',
    '-shortest',
    track['video_file'],
  ]
  subprocess.run(cmd)

for i, track in enumerate(tracks, 1):
  print(f"{i}. {track['path']}")
  make_video(track)
