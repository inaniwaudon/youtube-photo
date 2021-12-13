from . import FontFile as FontFile, Image as Image
from typing import Any

bdf_slant: Any
bdf_spacing: Any

def bdf_char(f): ...

class BdfFontFile(FontFile.FontFile):
    def __init__(self, fp) -> None: ...
