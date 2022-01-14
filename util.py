from pathlib import Path
import json

input_dir = Path('input')

tracks = json.loads((input_dir / 'tracks.json').read_bytes())
