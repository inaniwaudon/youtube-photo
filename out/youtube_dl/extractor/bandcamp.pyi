from ..compat import compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, KNOWN_EXTENSIONS as KNOWN_EXTENSIONS, float_or_none as float_or_none, int_or_none as int_or_none, parse_filesize as parse_filesize, str_or_none as str_or_none, try_get as try_get, unified_strdate as unified_strdate, unified_timestamp as unified_timestamp, update_url_query as update_url_query, url_or_none as url_or_none, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class BandcampIE(InfoExtractor): ...

class BandcampAlbumIE(BandcampIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class BandcampWeeklyIE(BandcampIE):
    IE_NAME: str
