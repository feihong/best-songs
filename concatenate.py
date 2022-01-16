"""
Concatenate individual track videos into one big video
"""
from pathlib import Path
import itertools
import subprocess
from util import output_dir, tracks

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)

def get_group_text(group):
  return '\n'.join(f"file '{track['video_file'].name}'" for track in group)

for i, group in enumerate(grouper(tracks, 10), 1):
  print(f'Group {i}')
  group_txt_file = output_dir / f'group-{i}.txt'
  group_txt_file.write_text(get_group_text(group))

  for track in group:
    print(' ', track['video_file'])

  group_video_file = output_dir / f'group-{i}.mp4'
  cmd = [
    'ffmpeg',
    '-f', 'concat',
    '-safe', '0',
    '-i', group_txt_file,
    '-c', 'copy',
    group_video_file,
  ]
  print(' '.join(str(s) for s in cmd))
  subprocess.run(cmd)
