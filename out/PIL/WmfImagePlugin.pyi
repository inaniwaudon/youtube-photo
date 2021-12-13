from . import Image as Image, ImageFile as ImageFile
from typing import Any

def register_handler(handler) -> None: ...

class WmfHandler:
    bbox: Any
    def open(self, im) -> None: ...
    def load(self, im): ...

class WmfStubImageFile(ImageFile.StubImageFile):
    format: str
    format_description: str
    def load(self, dpi: Any | None = ...) -> None: ...
