from pathlib import Path
import re
import urllib.parse
import jinja2


output_file = Path('eargod.html')

def get_tracks():
  for line in Path('documents/eargod-2021.txt').read_text().strip().splitlines():
    try:
      num, title, artist = re.match(r'(\d+)、(\w+)  (\w+)', line).groups()
      query = 'https://www.youtube.com/results?' + urllib.parse.urlencode({'search_query': f'{title}  {artist}'})
      yield dict(num=num, title=title, artist=artist, query=query)
    except:
      pass

tmpl = jinja2.Template("""
<!doctype html>
<html lang="en">
  <head>
    <title>EarGod 2021</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no, viewport-fit=cover">
  </head>
  <body>
    {% for track in tracks %}
      <p>
        {{ track['num'] }}
        <a href="{{ track['query'] }}" target="_blank">{{ track['title'] }}</a>
        ✪ {{ track['artist'] }}
      </p>
    {% endfor %}
  </body>
</html>
""")

output_file.write_text(tmpl.render(tracks=get_tracks()))
