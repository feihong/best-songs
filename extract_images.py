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

  subprocess.run([
    'convert',
    track['image_file'],
    '-resize', '426x240',
    '-background', 'black',
    '-gravity', 'center',
    '-extent', '426x240',
    track['resized_image_file'],
  ])
