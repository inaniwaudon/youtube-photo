from . import Image as Image, ImageFile as ImageFile
from typing import Any

xbm_head: Any

class XbmImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
