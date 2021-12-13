from . import Image as Image, ImageFile as ImageFile, ImagePalette as ImagePalette
from ._binary import o8 as o8
from typing import Any

xpm_head: Any

class XpmImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    def load_read(self, bytes): ...
