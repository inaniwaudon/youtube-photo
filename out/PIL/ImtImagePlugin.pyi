from . import Image as Image, ImageFile as ImageFile
from typing import Any

field: Any

class ImtImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
