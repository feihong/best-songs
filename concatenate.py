"""
Concatenate individual track videos into one big video
"""
from pathlib import Path
import itertools
import subprocess
import ffmpeg
from util import output_dir, tracks


title = '2021年度最值得听的歌曲'

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)

for i, group in enumerate(grouper(tracks, 10), 1):
  if i != 4: continue
  group_title = f'{title} Part {i}'
  print(group_title)
  group_video_file = output_dir / f'{group_title}.mp4'

  for track in group:
    print(' ', track['video_file'])

  comment_lines = [
    group_title,
    '\n'.join(f'{track["number"]}. {track["title"]} by {track["artist"]}' for track in group),
    '【影片使用的照片及文字和音乐版权归唱片公司和歌手所有，如侵犯您的权益，请通知我，我将马上删除。】',
  ]
  comment = '\n\n'.join(comment_lines)

  if group_video_file.exists():
    continue

  inputs = itertools.chain.from_iterable(('-i', track['video_file']) for track in group)
  filter_complex = ' '.join(f'[{i}:v] [{i}:a]' for i in range(len(group))) + ' concat=n=10:v=1:a=1 [vv] [aa]'

  cmd = [
    'ffmpeg',
  ] + list(inputs) + [
    '-filter_complex', filter_complex,
    '-map', '[vv]',
    '-map', '[aa]',
    '-metadata', f'comment={comment}',
    'output/2021年度最值得听的歌曲 Part 4.mp4'
  ]
  print(cmd)
  subprocess.run(cmd)
