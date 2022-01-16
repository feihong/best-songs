"""
Concatenate individual track videos into one big video
"""
from pathlib import Path
import itertools
import subprocess
from util import output_dir, tracks

title = '2022年度最值得听的歌曲'

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

  group_title = f'{title} Part {i}'

  comment_lines = [
    group_title,
    '\n'.join(f'{track["number"]}. {track["title"]} by {track["artist"]}' for track in group),
    '【影片使用的照片及文字和音乐版权归唱片公司和歌手所有，如侵犯您的权益，请通知我，我将马上删除。】',
  ]
  comment = '\n\n'.join(comment_lines)

  group_video_file = output_dir / f'{group_title}.mp4'
  cmd = [
    'ffmpeg',
    '-y',
    '-f', 'concat',
    '-safe', '0',
    '-i', group_txt_file,
    '-c', 'copy',
    '-metadata', f'comment={comment}',
    group_video_file,
  ]
  print(' '.join(str(s) for s in cmd))
  subprocess.run(cmd)
