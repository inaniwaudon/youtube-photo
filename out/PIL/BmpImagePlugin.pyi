from . import Image as Image, ImageFile as ImageFile, ImagePalette as ImagePalette
from ._binary import o8 as o8
from typing import Any

BIT2MODE: Any

class BmpImageFile(ImageFile.ImageFile):
    format_description: str
    format: str
    COMPRESSIONS: Any

class DibImageFile(BmpImageFile):
    format: str
    format_description: str

SAVE: Any
