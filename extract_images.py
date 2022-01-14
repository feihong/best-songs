from pathlib import Path
import subprocess

import mutagen.mp4

from util import input_dir, tracks

ext_map = {
  mutagen.mp4.MP4Cover.FORMAT_JPEG: '.jpg',
  mutagen.mp4.MP4Cover.FORMAT_PNG: '.png',
}

for track in tracks:
  path = input_dir / Path(track['location'])
  mp4 = mutagen.mp4.MP4(str(path))
  covr = mp4['covr'][0]
  ext = ext_map[covr.imageformat]
  image_file = path.with_suffix(ext)
  image_file.write_bytes(covr)

  resized_file = input_dir / (image_file.stem + '-resized' + image_file.suffix)
  print(resized_file)
  subprocess.run([
    'convert',
    image_file,
    '-resize', '800x600',
    '-background', 'black',
    '-gravity', 'center',
    '-extent', '800x600',
    resized_file,
  ])
