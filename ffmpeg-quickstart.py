import json
from pathlib import Path
import ffmpeg

input_dir = Path('input')
tracks = json.loads((input_dir / 'tracks.json').read_bytes())

def get_inputs(tracks):
  tracks = tracks[:5] # temporary

  for track in tracks:
    path = input_dir / track['location']
    yield ffmpeg.input(str(path)).trim(start=0, end=30).filter('scale', 400, 300)

(
  ffmpeg
  .concat(*get_inputs(tracks))
  .output('output.mp4')
  .overwrite_output()
  .run()
)
