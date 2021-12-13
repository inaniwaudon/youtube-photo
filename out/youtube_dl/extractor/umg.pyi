from ..utils import int_or_none as int_or_none, parse_filesize as parse_filesize, parse_iso8601 as parse_iso8601
from .common import InfoExtractor as InfoExtractor

class UMGDeIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
