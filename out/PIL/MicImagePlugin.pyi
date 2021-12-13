from . import Image as Image, TiffImagePlugin as TiffImagePlugin
from typing import Any

class MicImageFile(TiffImagePlugin.TiffImageFile):
    format: str
    format_description: str
    fp: Any
    frame: Any
    def seek(self, frame) -> None: ...
    def tell(self): ...
