from . import Image as Image
from typing import Any

WIDTH: int

def puti16(fp, values) -> None: ...

class FontFile:
    bitmap: Any
    info: Any
    glyph: Any
    def __init__(self) -> None: ...
    def __getitem__(self, ix): ...
    ysize: Any
    metrics: Any
    def compile(self): ...
    def save(self, filename) -> None: ...