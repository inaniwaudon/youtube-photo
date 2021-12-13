from . import Image as Image, ImageFile as ImageFile
from typing import Any

b_whitespace: bytes
MODES: Any

class PpmImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
