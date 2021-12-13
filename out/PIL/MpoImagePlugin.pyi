from . import Image as Image, ImageFile as ImageFile, JpegImagePlugin as JpegImagePlugin
from typing import Any

class MpoImageFile(JpegImagePlugin.JpegImageFile):
    format: str
    format_description: str
    def load_seek(self, pos) -> None: ...
    fp: Any
    offset: Any
    tile: Any
    def seek(self, frame) -> None: ...
    def tell(self): ...
    @staticmethod
    def adopt(jpeg_instance, mpheader: Any | None = ...): ...
