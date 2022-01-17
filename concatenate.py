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

def get_comment(group_title, tracks):
  def gen():
    for track in tracks:
      yield f'{track["number"]}. {track["title"]} by {track["artist"]}'

  comment_lines = [
    group_title,
    '\n'.join(gen()),
    '【影片使用的照片及文字和音乐版权归唱片公司和歌手所有，如侵犯您的权益，请通知我，我将马上删除。】',
  ]
  return '\n\n'.join(comment_lines)

def get_inputs(tracks):
  for track in tracks:
    yield ffmpeg.input(str(track['video_file'])).video  # should already be trimmed
    yield ffmpeg.input(str(track['path'])).audio.filter('atrim', duration=track['duration'])

for i, group in enumerate(grouper(tracks, 10), 1):
  group_title = f'{title} Part {i}'
  print(group_title)
  group_video_file = output_dir / f'{group_title}.mp4'

  if group_video_file.exists():
    continue

  stream = (
    ffmpeg
    .concat(*get_inputs(group), v=1, a=1)
    .output(str(group_video_file), metadata=f'comment={get_comment(group_title, group)}')
  )
  print(stream.compile())
  stream.run()
