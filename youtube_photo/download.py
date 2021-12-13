import glob
import os

import cv2
import imagehash
import youtube_dl
from PIL import Image


class Downloader:
    def __init__(
        self,
        video_path="download-temp.mp4",
        youtube_url="https://www.youtube.com/watch?v=",
        movie_size=(4096, 2160),
    ):
        self.video_path = video_path
        self.youtube_url = youtube_url
        self.movie_width, self.movie_height = movie_size

    def download(self, video_id, picture_dir, options=None, description_pattern=None):
        self.__download_video(video_id, options)
        descriptions = self.__get_descriptions(description_pattern)
        self.__capture(picture_dir, descriptions)

    def __download_video(self, video_id, options=None):
        # download a video
        urls = [self.youtube_url + video_id]
        if options is None:
            options = {
                "format": "bestvideo+bestaudio",
                "outtmpl": self.video_path,
                "writedescription": True,
                "merge_output_format": "mp4",
            }
        else:
            options = options

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download(urls)

    def __get_descriptions(self, description_pattern=None):
        # get a descrption:
        path = glob.glob(
            "*.description" if description_pattern is None else description_pattern
        )[0]
        options = []
        with open(path, "r") as f:
            for line in f.readlines():
                options_line = line.split(" ")
                options.append(
                    {
                        "finename": options_line[0],
                        "rotates": options_line[1] == "True",
                        "width": int(options_line[2]),
                        "height": int(options_line[3]),
                    }
                )
        return options

    def __capture(self, picture_dir, descriptions):
        # capture
        cap = cv2.VideoCapture(self.video_path)
        before_hash = None
        x = 0
        ret, frame = cap.read()
        while cap.isOpened() and ret:
            description = descriptions[x]

            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img).resize(
                (self.movie_width, self.movie_height), Image.BICUBIC
            )

            # calculate the hash
            img_hash = imagehash.average_hash(img)
            if before_hash is None or img_hash - before_hash >= 2:
                before_hash = img_hash

                # crop, rotate
                img = img.crop((0, 0, description["width"], description["height"]))
                if description["rotates"]:
                    img = img.rotate(-90, expand=True)

                img.save(os.path.join(picture_dir, descriptions["finename"]))
                x += 1

            ret, frame = cap.read()
