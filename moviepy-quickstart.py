from pathlib import Path
import json

from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip, concatenate_videoclips

input_dir = Path('input')
tracks = json.loads((input_dir / 'tracks.json').read_bytes())

def get_clips(tracks):
  tracks = tracks[:5] # temporary

  for track in tracks:
    path = input_dir / track['location']
    print(path)
    audio = VideoFileClip(str(path)).subclip(0, 10)
    print(audio.duration)
    print(track['title'])
    text = TextClip(track['title']).set_fps(24).set_pos('center').set_duration(audio.duration)

    yield CompositeVideoClip([audio, text])

clips = list(get_clips(tracks))
final_clip = concatenate_videoclips(clips)
final_clip.write_videofile('output.mp4')
