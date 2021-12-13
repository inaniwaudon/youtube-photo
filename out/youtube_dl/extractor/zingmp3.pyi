from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none
from .common import InfoExtractor as InfoExtractor

class ZingMp3BaseIE(InfoExtractor): ...

class ZingMp3IE(ZingMp3BaseIE):
    IE_NAME: str
    IE_DESC: str

class ZingMp3AlbumIE(ZingMp3BaseIE):
    IE_NAME: str
