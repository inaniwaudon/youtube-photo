import datetime, glob, os
import numpy as np
import cv2
import youtube_uploader
from PIL import Image

# movie
fps = 24.0
width, height = (4096, 2160)
temp_name = "temp.mp4"

# photo
extensions = [".png", ".jpg"]
orientation_exif_key = 274
transpose_no = [0, 3, 1, 5, 4, 6, 2]

# collect files
files = glob.glob("img/*")
codec = cv2.VideoWriter_fourcc(*"avc1")
video = cv2.VideoWriter(temp_name, codec, fps, (width, height))

description = ""

for file in files :
	if os.path.splitext(file)[1].lower() not in extensions :
		continue

	# read an image
	img = Image.open(file)
	description += "%s " % os.path.basename(file)

	# get the EXIF and transpose
	exif = img._getexif()
	if orientation_exif_key in exif :
		orientation = exif[orientation_exif_key]
		if orientation > 1 :
			img = img.transpose(transpose_no[orientation-2])

	img.save("a/%s" % os.path.basename(file))

	# rotate
	rotates = img.height > img.width
	if rotates :
		img = img.rotate(90, expand=True)

	# resize
	magnification = width / img.width if img.width / img.height > width / height else height / img.height
	resized_w = int(img.width * magnification)
	resized_h = int(img.height * magnification)

	img = img.resize((resized_w, resized_h), Image.BICUBIC)
	description += "%s %s %s\n" % (rotates, resized_w, resized_h)

	# make a frame
	frame = Image.new("RGB", (width, height))
	frame.paste(img, (0, 0))
	frame_cv = cv2.cvtColor(np.asarray(frame), cv2.COLOR_RGB2BGR)

	for i in range(2) :
		video.write(frame_cv)

video.release()
print(description)

# upload
now = datetime.datetime.now()
now_str = now.strftime("%Y%m%d-%H:%M:%S")
title = "test-" + now_str

url = youtube_uploader.upload(temp_name, title, description)