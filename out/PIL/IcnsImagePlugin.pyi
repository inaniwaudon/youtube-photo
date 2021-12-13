from PIL import (
    Image as Image,
    ImageFile as ImageFile,
    Jpeg2KImagePlugin as Jpeg2KImagePlugin,
    PngImagePlugin as PngImagePlugin,
    features as features,
)
from typing import Any

enable_jpeg2k: Any
MAGIC: bytes
HEADERSIZE: int

def nextheader(fobj): ...
def read_32t(fobj, start_length, size): ...
def read_32(fobj, start_length, size): ...
def read_mk(fobj, start_length, size): ...
def read_png_or_jpeg2000(fobj, start_length, size): ...

class IcnsFile:
    SIZES: Any
    dct: Any
    fobj: Any
    def __init__(self, fobj) -> None: ...
    def itersizes(self): ...
    def bestsize(self): ...
    def dataforsize(self, size): ...
    def getimage(self, size: Any | None = ...): ...

class IcnsImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    @property
    def size(self): ...
    @size.setter
    def size(self, value) -> None: ...
    best_size: Any
    im: Any
    mode: Any
    def load(self) -> None: ...
