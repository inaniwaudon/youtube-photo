from . import Image as Image, ImageFile as ImageFile
from typing import Any

SUPPORTED: bool

class WebPImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    def seek(self, frame) -> None: ...
    fp: Any
    tile: Any
    def load(self): ...
    def tell(self): ...
