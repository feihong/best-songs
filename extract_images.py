"""
Extract cover art images and for each image, generate a resized copy
"""
import subprocess
import mutagen.mp4
from util import tracks


for track in tracks:
  print(track['path'])
  mp4 = mutagen.mp4.MP4(str(track['path']))
  track['image_file'].write_bytes(mp4['covr'][0])

  # Copy and resize image
  subprocess.run([
    'convert',
    track['image_file'],
    '-resize', '426x240',
    '-background', 'black',
    '-gravity', 'center',
    '-extent', '426x240', # 240p
    track['resized_image_file'],
  ])

  # Add text to resized image
  # https://legacy.imagemagick.org/Usage/annotating/
  subprocess.run([
    'convert',
    '-background', '#0008',
    '-fill', 'white',
    '-gravity', 'center',
    '-size', '426x40',
    '-font', 'WenQuanYi-Zen-Hei', # run `identify -list font` to find an appropriate font
    f"caption:{track['title']}\n{track['artist']}",
    track['resized_image_file'],
    '+swap',
    '-gravity', 'south',
    '-composite',
    track['captioned_image_file'],
  ])
