from . import (
    ImageFile as ImageFile,
    ImagePalette as ImagePalette,
    UnidentifiedImageError as UnidentifiedImageError,
)

class GdImageFile(ImageFile.ImageFile):
    format: str
    format_description: str

def open(fp, mode: str = ...): ...
