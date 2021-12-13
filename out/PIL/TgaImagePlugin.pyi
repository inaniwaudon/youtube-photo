from . import Image as Image, ImageFile as ImageFile, ImagePalette as ImagePalette
from ._binary import o8 as o8
from typing import Any

MODES: Any

class TgaImageFile(ImageFile.ImageFile):
    format: str
    format_description: str

SAVE: Any
