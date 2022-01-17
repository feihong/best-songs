from pathlib import Path
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
    <style>
      html {
        font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        font-size: 14px;
      }
      .big {
        font-size: 1.5em;
      }
    </style>
  </head>
  <body>
    <h1>2021年最值得听的歌曲</h1>
    <p>
      <a href="tracks.zip">Download ZIP file</a>
    </p>
    <p>
      <a href="https://www.youtube.com/playlist?list=PLKPg6d3PEwV1j4LoyJa9281vWdJ9r4WoD">YouTube playlist</a>
    </p>
    <ol>
    {% for track in tracks %}
      <li>
        <span class="big">
          <a href="{{ track['comments'] }}" target="_blank">{{ track['title'] }}</a>
        </span>
        ✪ {{ track['artist'] }}
      </li>
    {% endfor %}
    </ol>
  </body>
</html>
""")

output_file.write_text(tmpl.render(tracks=tracks))

