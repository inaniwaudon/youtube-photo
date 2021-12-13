from . import Image as Image, ImageFile as ImageFile

def register_handler(handler) -> None: ...

class BufrStubImageFile(ImageFile.StubImageFile):
    format: str
    format_description: str
