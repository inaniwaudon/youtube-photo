from . import Image as Image, ImageFile as ImageFile
from ._binary import o8 as o8
from typing import Any

MODES: Any

class SgiImageFile(ImageFile.ImageFile):
    format: str
    format_description: str

class SGI16Decoder(ImageFile.PyDecoder):
    def decode(self, buffer): ...
