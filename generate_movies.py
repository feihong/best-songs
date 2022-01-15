"""
Generate a video for each track.
"""
import subprocess
from util import tracks


def make_video(track):
  print(track['path'])
  cmd = [
    'ffmpeg',
    '-y', # overwrite
    '-loop', '1',
    '-i', track['resized_image_file'],
    '-t', '10', # duration of 10 seconds (temporary)
    '-i', track['path'],
    '-c:a', 'copy', # copy audio, don't re-encode
    '-c:v', 'libx264',
    '-crf', '20',
    '-pix_fmt', 'yuv420p',
    '-shortest',
    track['output_file'],
  ]
  subprocess.run(cmd)

for track in tracks:
  make_video(track)
