import glob
import os
from typing import List, Optional, Tuple, TypedDict

import cv2  # type: ignore
import imagehash  # type: ignore
import youtube_dl  # type: ignore
from PIL import Image  # type: ignore


class YTOption(TypedDict):
    format: str
    outtmpl: str
    writedescription: bool
    merge_output_format: str


class Option(TypedDict):
    filename: str
    rotates: bool
    width: int
    height: int


Options = List[Option]


class Downloader:
    def __init__(
        self,
        video_path: str = "download-temp.mp4",
        youtube_url: str = "https://www.youtube.com/watch?v=",
        movie_size: Tuple[int, int] = (4096, 2160),
    ) -> None:
        self.video_path = video_path
        self.youtube_url = youtube_url
        self.movie_width, self.movie_height = movie_size

    def download(
        self,
        video_id: str,
        picture_dir: str,
        options: Optional[YTOption] = None,
        description_pattern: Optional[str] = None,
    ) -> None:
        self.__download_video(video_id, options)
        descriptions = self.__get_descriptions(description_pattern)
        self.__capture(picture_dir, descriptions)

    def __download_video(
        self, video_id: str, options: Optional[YTOption] = None
    ) -> None:
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

    def __get_descriptions(self, description_pattern: Optional[str] = None) -> Options:
        # get a descrption:
        path = glob.glob(
            "*.description" if description_pattern is None else description_pattern
        )[0]
        options: Options = []
        with open(path, "r") as f:
            for line in f.readlines():
                options_line = line.split(" ")
                options.append(
                    {
                        "filename": options_line[0],
                        "rotates": options_line[1] == "True",
                        "width": int(options_line[2]),
                        "height": int(options_line[3]),
                    }
                )
        return options

    def __capture(self, picture_dir: str, descriptions: Options) -> None:
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

                img.save(os.path.join(picture_dir, description["filename"]))
                x += 1

            ret, frame = cap.read()
