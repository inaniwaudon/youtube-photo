from . import Image as Image, ImageFile as ImageFile
from typing import Any

class PcdImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    im: Any
    def load_end(self) -> None: ...
