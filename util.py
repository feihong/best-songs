from pathlib import Path
import json

import mutagen.mp4


input_dir = Path('input')

output_dir = Path('output')

ext_map = {
  mutagen.mp4.MP4Cover.FORMAT_JPEG: '.jpg',
  mutagen.mp4.MP4Cover.FORMAT_PNG: '.png',
}

max_duration = 3 * 60  # must be no longer than 3 minutes

tracks = json.loads((input_dir / 'tracks.json').read_bytes())

# Add more metadata
for i, track in enumerate(tracks, 1):
  track['number'] = i
  path = input_dir / Path(track['location'])
  track['path'] = path

  mp4 = mutagen.mp4.MP4(str(path))
  track['duration'] = min(max_duration, mp4.info.length)
  covr = mp4['covr'][0]
  ext = ext_map[covr.imageformat]
  image_file = path.with_suffix(ext)
  track['image_file'] = image_file
  track['resized_image_file'] = input_dir / (image_file.stem + '-resized' + image_file.suffix)
  track['captioned_image_file'] = input_dir / (image_file.stem + '-captioned' + image_file.suffix)
  track['video_file'] = output_dir / (path.stem + '.mp4')
