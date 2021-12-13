from ._binary import o8 as o8
from typing import Any

class PaletteFile:
    rawmode: str
    palette: Any
    def __init__(self, fp) -> None: ...
    def getpalette(self): ...
