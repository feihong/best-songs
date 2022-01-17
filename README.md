# Best Songs

Generate videos and web page from collection of music files.

## Intallation

    pip install --user --requirement requirements.txt

## Commands


## Links

- [MoviePy User Guide](https://zulko.github.io/moviepy/index.html)
- [YouTube Video resolution & aspect ratios](https://support.google.com/youtube/answer/6375112?hl=en)

## Notes

When concatenating MP4 files, you can't get predictable results without using [concat filter](http://trac.ffmpeg.org/wiki/Concatenate#filter). Previous attempts to use [concat demuxer](http://trac.ffmpeg.org/wiki/Concatenate#demuxer) would sometimes work but fail miserably depending on the input files (audio and video would be out of sync).

You can't use `-acodec copy` when using `-filter_complex`. You'll get this error:

    Streamcopy requested for output stream 0:0, which is fed from a complex filtergraph. Filtering and streamcopy cannot be used together.

