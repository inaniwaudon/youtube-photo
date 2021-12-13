from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, js_to_json as js_to_json, mimetype2ext as mimetype2ext
from .common import InfoExtractor as InfoExtractor

class ImgurIE(InfoExtractor): ...

class ImgurGalleryIE(InfoExtractor):
    IE_NAME: str

class ImgurAlbumIE(ImgurGalleryIE):
    IE_NAME: str
