from . import Image as Image, ImageFile as ImageFile
from typing import Any

class WalImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    im: Any
    def load(self) -> None: ...

def open(filename): ...

quake2palette: bytes
