import sys, glob
import cv2
import imagehash
import youtube_dl
from PIL import Image

video_path = "download-temp.mp4"
picture_dir = "download-img/"
description_pattern = "*.description"
youtube_url = "https://www.youtube.com/watch?v="

movie_width, movie_height = (4096, 2160)

# download a video
urls = [youtube_url + sys.argv[1]]
options = {
	"format" : "bestvideo+bestaudio",
	"outtmpl" : "download-temp.mp4",
	"writedescription" : True,
	"merge_output_format" : "mp4"
}

with youtube_dl.YoutubeDL(options) as ydl :
	ydl.download(urls)

# get a descrption
path = glob.glob(description_pattern)[0]
with open(path) as fp :
	options = fp.read().split("\n")

# capture
cap = cv2.VideoCapture(video_path)
x = 0

while cap.isOpened() :
	ret, frame = cap.read()
	
	if ret :
		options_line = options[x].split(" ")
		finename = options_line[0]
		rotates = options_line[1] == "True"
		width = int(options_line[2])
		height = int(options_line[3])

		img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		img = Image.fromarray(img).resize((movie_width, movie_height), Image.BICUBIC)
		
		# calculate the hash
		img_hash = imagehash.average_hash(img)
		if "before_hash" in locals() and img_hash - before_hash < 2 :
			continue
		before_hash = img_hash

		# crop, rotate
		img = img.crop((0, 0, width, height))
		if rotates :
			img = img.rotate(-90, expand=True)
		
		img.save("%s%s" % (picture_dir, finename))
		x += 1

	else :
		break