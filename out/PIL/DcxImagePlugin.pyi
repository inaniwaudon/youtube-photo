from . import Image as Image
from .PcxImagePlugin import PcxImageFile as PcxImageFile
from typing import Any

MAGIC: int

class DcxImageFile(PcxImageFile):
    format: str
    format_description: str
    frame: Any
    fp: Any
    def seek(self, frame) -> None: ...
    def tell(self): ...
