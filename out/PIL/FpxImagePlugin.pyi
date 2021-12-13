from . import Image as Image, ImageFile as ImageFile
from typing import Any

MODES: Any

class FpxImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    fp: Any
    def load(self): ...
