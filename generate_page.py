from jinja2 import Template

from util import tracks


output_file = Path('index.html')

tmpl = Template("""
<!doctype html>
<html lang="en">
  <head>
    <title>2021年最值得听的歌曲</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no, viewport-fit=cover">
  </head>
  <body>
    <h1>2021年最值得听的歌曲</h1>
    <a href="tracks.zip">Download ZIP file</a>
    <ol>
    {% for track in tracks %}
      <li> <a href="{{ track['comments'] }}" target="_blank"> {{ track['title'] }} - {{ track['artist'] }} </a> </li>
    {% endfor %}
    </ol>
  </body>
</html>
""")

output_file.write_text(tmpl.render(tracks=tracks))

