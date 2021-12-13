from . import Image as Image, ImageFile as ImageFile
from typing import Any

split: Any
field: Any
gs_windows_binary: Any

def has_ghostscript(): ...
def Ghostscript(tile, size, fp, scale: int = ..., transparency: bool = ...): ...

class PSFile:
    fp: Any
    char: Any
    def __init__(self, fp) -> None: ...
    def seek(self, offset, whence=...) -> None: ...
    def readline(self): ...

class EpsImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    mode_map: Any
    im: Any
    mode: Any
    tile: Any
    def load(self, scale: int = ..., transparency: bool = ...) -> None: ...
    def load_seek(self, *args, **kwargs) -> None: ...
