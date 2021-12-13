import datetime
import glob
import os

import cv2
import numpy as np
from PIL import Image

from .youtube_uploader import YTUploader


class Uploader:
    TEMP_NAME = "temp.mp4"

    def __init__(self):
        pass

    def upload(self, img_dir, auth_path):
        description = self.img_to_video(img_dir, auth_path)
        url = YTUploader(auth_path).upload(self.TEMP_NAME, title, description)
        return url

    def get_images(self, img_dir):
        filenames = glob.glob(os.path.join(img_dir, "*"))
        return [
            f
            for f in filenames
            if os.path.splitext(f)[1].lower() not in [".png", ".jpg"]
        ]

    def img_to_video(
        self,
        img_dir,
        auth_path,
        fps=24.0,
        img_size=(4096, 2160),
        orientation_exif_key=274,
        transpose_no=[0, 3, 1, 5, 4, 6, 2],
    ):
        width, height = img_size
        codec = cv2.VideoWriter_fourcc(*"avc1")
        video = cv2.VideoWriter(self.TEMP_NAME, codec, fps, img_size)
        descriptions = []
        for f in self.get_images(img_dir):
            # read an image
            img = Image.open(f)
            # get the EXIF and transpose
            exif = img._getexif()
            if orientation_exif_key in exif:
                orientation = exif[orientation_exif_key]
                if orientation > 1:
                    img = img.transpose(transpose_no[orientation - 2])

            img.save(os.path.join("a", os.path.basename(f)))

            # rotate
            rotates = img.height > img.width
            if rotates:
                img = img.rotate(90, expand=True)

            # resize
            magnification = (
                width / img.width
                if img.width / img.height > width / height
                else height / img.height
            )
            resized_w = int(img.width * magnification)
            resized_h = int(img.height * magnification)

            img = img.resize((resized_w, resized_h), Image.BICUBIC)
            descriptions.append(
                "{} {} {} {}".format(os.path.basename(f), rotates, resized_w, resized_h)
            )

            # make a frame
            frame = Image.new("RGB", (width, height))
            frame.paste(img, (0, 0))
            frame_cv = cv2.cvtColor(np.asarray(frame), cv2.COLOR_RGB2BGR)

            for i in range(2):
                video.write(frame_cv)
        else:
            video.release()
            return "\n".join(descriptions)


# upload
now = datetime.datetime.now()
now_str = now.strftime("%Y%m%d-%H:%M:%S")
title = "test-" + now_str
