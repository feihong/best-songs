zip:
	cd input && zip -r ../tracks.zip *

page:
	python generate_page.py

images:
	python extract_images.py

videos:
	python generate_videos.py

clean:
	rm output/*.txt; rm output/*.mp4
