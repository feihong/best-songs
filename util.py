from pathlib import Path
import json

import mutagen.mp4


input_dir = Path('input')

output_dir = Path('output')

ext_map = {
  mutagen.mp4.MP4Cover.FORMAT_JPEG: '.jpg',
  mutagen.mp4.MP4Cover.FORMAT_PNG: '.png',
}

tracks = json.loads((input_dir / 'tracks.json').read_bytes())

# Add more metadata
for track in tracks:
  path = input_dir / Path(track['location'])
  track['path'] = path

  mp4 = mutagen.mp4.MP4(str(path))
  covr = mp4['covr'][0]
  ext = ext_map[covr.imageformat]
  image_file = path.with_suffix(ext)
  track['image_file'] = image_file
  track['resized_image_file'] = input_dir / (image_file.stem + '-resized' + image_file.suffix)
  track['output_file'] = output_dir / (path.stem + '.mp4')
