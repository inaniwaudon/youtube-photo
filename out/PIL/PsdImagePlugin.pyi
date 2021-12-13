from . import Image as Image, ImageFile as ImageFile, ImagePalette as ImagePalette
from ._binary import i8 as i8
from typing import Any

MODES: Any

class PsdImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    mode: Any
    tile: Any
    frame: Any
    fp: Any
    def seek(self, layer): ...
    def tell(self): ...
    im: Any
    def load_prepare(self) -> None: ...
