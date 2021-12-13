from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, parse_iso8601 as parse_iso8601
from .common import InfoExtractor as InfoExtractor

class MySpaceIE(InfoExtractor): ...

class MySpaceAlbumIE(InfoExtractor):
    IE_NAME: str
