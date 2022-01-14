from pathlib import Path

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
