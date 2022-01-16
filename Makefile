zip:
	cd input && zip -r ../tracks.zip *

page:
	python generate_page.py

clean:
	rm output/*.txt; rm output/*.mp4
